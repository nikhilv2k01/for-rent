# Generated by Django 4.0.2 on 2022-06-09 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_postproperty_bachelors_allowed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userreg')),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.postproperty')),
            ],
            options={
                'db_table': 'favourites',
            },
        ),
    ]
