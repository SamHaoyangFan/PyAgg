# Generated by Django 4.0.4 on 2022-07-12 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_post_p_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='p_title',
            field=models.TextField(),
        ),
    ]
