# Generated by Django 3.2.5 on 2021-07-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0007_auto_20210710_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre_Choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_choices', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='bookshelf.Genre_Choices'),
        ),
    ]