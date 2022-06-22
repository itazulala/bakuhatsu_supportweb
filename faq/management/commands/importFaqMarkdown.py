from django.core.management.base import BaseCommand
from django.db import transaction
from faq.models import MarkdownFile
from faq.models import Article
from faq.models import Category
from faq.models import Tag
import yaml


class Command(BaseCommand):
    help = 'uploads/contents配下のmarkdownファイルのデータをDBにインポートします'

    def handle(self, *args, **options):
        try:
            markdown_files = MarkdownFile.objects.all().filter(uploaded=False)
            for markdown_file in markdown_files:
                with open('uploads/' + str(markdown_file.upload_path), encoding='utf-8') as file:

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
                    json_obj = yaml.safe_load(yaml_header)
                    with transaction.atomic():
                        article = Article.objects.create(
                            question=json_obj['title'],
                            answer=contents_text,
                            draft=json_obj['draft'],
                            category_id=Category.objects.get(name=json_obj['categories'][0]),
                            markdown_file_id=MarkdownFile.objects.get(id=markdown_file.id),
                            created_at=json_obj['date']
                        )

                        article_tags = Article.objects.get(title=article)
                        for tag_name in json_obj['tags']:
                            tag = Tag.objects.get(name=tag_name)
                            article_tags.tags.add(tag)

                        markdown_up = MarkdownFile.objects.get(id=markdown_file.id)
                        markdown_up.uploaded = True
                        markdown_up.save()

        except Exception as e:
            print(e)
