# Generated by Django 4.0.4 on 2022-07-19 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_remove_post_p_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
