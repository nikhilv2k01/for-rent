# Generated by Django 4.0.1 on 2022-05-13 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_postproperty_ower_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postproperty',
            name='owner_name',
            field=models.CharField(max_length=20),
        ),
    ]
