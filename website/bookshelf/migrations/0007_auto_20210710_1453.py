# Generated by Django 3.2.5 on 2021-07-10 09:23

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0006_auto_20210710_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Narrative', 'Narrative'), ('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Mystery', 'Mystery'), ('Science-Fiction', 'Science-Fiction'), ('Historical-Fiction', 'Historical-Fiction'), ('Fantasy', 'Fantasy'), ('Romance', 'Romance'), ('Horror', 'Horror'), ('Thriller', 'Thriller')], max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Marathi', 'Marathi'), ('Sanskrit', 'Sanskrit')], max_length=200),
        ),
    ]
