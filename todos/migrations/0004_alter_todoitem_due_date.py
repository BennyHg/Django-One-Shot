# Generated by Django 4.0.3 on 2022-06-14 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_todoitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
    ]
