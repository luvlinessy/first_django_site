# Generated by Django 4.1.2 on 2022-11-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Caterory',
            new_name='Category',
        ),
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
