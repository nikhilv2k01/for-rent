# Generated by Django 4.0.2 on 2022-06-06 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_postproperty_bachelors_allowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postproperty',
            name='bachelors_allowed',
            field=models.CharField(default='NULL', max_length=5),
        ),
    ]
