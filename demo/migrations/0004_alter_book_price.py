# Generated by Django 4.0.6 on 2022-07-27 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_book_cover_book_description_book_is_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]