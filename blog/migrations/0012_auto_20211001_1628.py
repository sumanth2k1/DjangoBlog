# Generated by Django 3.2.7 on 2021-10-01 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20211001_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postimage',
            field=models.ImageField(blank=True, null=True, upload_to='postImages'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
