# Generated by Django 5.0.6 on 2024-05-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=900)),
                ('Price', models.IntegerField(default=0)),
                ('Description', models.CharField(max_length=300)),
                ('Photo', models.ImageField(upload_to='images')),
            ],
        ),
    ]
