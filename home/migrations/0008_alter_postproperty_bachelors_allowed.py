# Generated by Django 4.0.2 on 2022-06-06 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_postproperty_package_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postproperty',
            name='bachelors_allowed',
            field=models.CharField(default='null', max_length=5),
        ),
    ]