# Generated by Django 3.2.5 on 2021-07-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0008_auto_20210710_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Marathi', 'Marathi')], max_length=200),
        ),
    ]
