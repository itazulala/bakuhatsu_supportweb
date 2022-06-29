from django.core.management.base import BaseCommand
from django.db import transaction
from pathlib import Path
from contents.models import Article, Category, Tag
from yaml import safe_load


class Command(BaseCommand):
    help = 'markdownファイルをcontents_articleに登録します。'

    def add_arguments(self, parser):
        parser.add_argument('-a', '--action', nargs='?', default='', type=str)
        parser.add_argument('-f', '--filepath', nargs='?', default='', type=str)

    def handle(self, *args, **options):

        try:
            if options['action'] != 'deleted':
                with open(options['filepath'], encoding='utf-8') as file:
                    if file.readline().strip('\n') != '---':
                        raise Exception(file.name + ': Front matter must begin with "---"')

                    lines = file.readlines()
                    yaml_header = ''
                    end_row = 0

                    for i, line in enumerate(lines):
                        if line == '---\n':
                            end_row = i
                            break
                        yaml_header += line
                    del lines[0:end_row + 1]
                    contents_text = ''.join(lines)
                    json_obj = safe_load(yaml_header)

                    if options['action'] == 'created':
                        with transaction.atomic():
                            article = Article.objects.create(
                                title=json_obj['title'],
                                content=contents_text,
                                file_path=file.name,
                                draft=json_obj['draft'],
                                category_id=Category.objects.get(name=json_obj['categories'][0]),
                                created_at=json_obj['date']
                            )

                            article_tags = Article.objects.get(title=article)
                            for tag_name in json_obj['tags']:
                                tag = Tag.objects.get(name=tag_name)
                                article_tags.tags.add(tag)

                    elif options['action'] == 'modified':
                        print(json_obj['categories'][0])
                        with transaction.atomic():
                            article = Article.objects.get(file_path=file.name)
                            article.title = json_obj['title']
                            article.content = contents_text
                            article.draft = json_obj['draft']
                            article.category_id = Category.objects.get(name=json_obj['categories'][0])
                            article.save()

                            article_tags = Article.objects.get(title=article)
                            for tag in article_tags.tags.all():
                                article_tags.tags.remove(tag)

                            for tag_name in json_obj['tags']:
                                tag = Tag.objects.get(name=tag_name)
                                article_tags.tags.add(tag)

            else:
                with transaction.atomic():
                    article = Article.objects.get(file_path=Path(options['filepath']))
                    article.delete()

        except Exception as e:
            print(e)

