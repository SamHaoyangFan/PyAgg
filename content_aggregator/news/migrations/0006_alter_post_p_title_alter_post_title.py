# Generated by Django 4.0.4 on 2022-07-13 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_post_p_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='p_title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
