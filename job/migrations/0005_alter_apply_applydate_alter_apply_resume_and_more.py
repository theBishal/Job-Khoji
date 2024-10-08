# Generated by Django 5.1.1 on 2024-09-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_apply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='applydate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='apply',
            name='resume',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='start_date',
            field=models.DateField(),
        ),
    ]
