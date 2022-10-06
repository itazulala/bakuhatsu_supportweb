# Generated by Django 3.2.13 on 2022-10-06 22:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='アプリケーション名')),
                ('action_url', models.URLField(verbose_name='アクションURL')),
                ('explanation', models.CharField(max_length=256, verbose_name='説明')),
                ('help_url', models.URLField(verbose_name='ヘルプページURL')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('key_name', models.CharField(max_length=32, verbose_name='キー')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tools.application')),
            ],
        ),
    ]
