# Generated by Django 3.0.5 on 2020-06-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_auto_20200607_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=15, null=True),
        ),
    ]