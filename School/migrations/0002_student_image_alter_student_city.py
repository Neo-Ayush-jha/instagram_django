# Generated by Django 4.1.5 on 2023-01-16 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(choices=[('Purnea', 'Purnea'), ('jalandher', 'jalandher'), ('Patna', 'Patna')], max_length=150),
        ),
    ]