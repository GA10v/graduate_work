# Generated by Django 4.1.7 on 2023-03-03 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='template',
            options={'ordering': ['title'], 'verbose_name': 'Template', 'verbose_name_plural': 'Templates'},
        ),
        migrations.AlterField(
            model_name='template',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='template',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]
