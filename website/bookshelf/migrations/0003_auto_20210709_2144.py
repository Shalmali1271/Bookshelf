# Generated by Django 3.2.5 on 2021-07-09 16:14

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('101', 'Narrative'), ('102', 'Fiction'), ('103', 'Non-Fiction'), ('104', 'Mystery'), ('105', 'Science-Fiction'), ('106', 'Historical-Fiction'), ('107', 'Fantasy'), ('108', 'Romance'), ('109', 'Horror'), ('110', 'Thriller')], max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('201', 'English'), ('202', 'Hindi'), ('203', 'Marathi'), ('204', 'Sanskrit')], max_length=200),
        ),
    ]
