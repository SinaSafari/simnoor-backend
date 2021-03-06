# Generated by Django 3.1.1 on 2020-09-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='body_text',
            new_name='en_body_text',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='en_title',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='en_description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='en_title',
        ),
        migrations.AddField(
            model_name='news',
            name='fa_body_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='fa_title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='fa_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='fa_title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
