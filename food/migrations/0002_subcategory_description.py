# Generated by Django 2.0 on 2019-05-04 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
