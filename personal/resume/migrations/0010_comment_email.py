# Generated by Django 4.1.5 on 2023-02-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_alter_projects_pro_languages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='no email', max_length=200),
        ),
    ]