# Generated by Django 2.1 on 2019-12-27 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0008_auto_20191204_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2019-12-27'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(blank=True, default='2019-12-27', null=True),
        ),
    ]
