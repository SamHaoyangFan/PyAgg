# Generated by Django 4.0.4 on 2022-07-12 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_post_guid_remove_post_post_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='p_title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
