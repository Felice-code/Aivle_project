# Generated by Django 5.0.6 on 2024-07-25 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('query', models.TextField()),
                ('sim1', models.FloatField()),
                ('sim2', models.FloatField()),
                ('sim3', models.FloatField()),
                ('answer', models.TextField()),
            ],
        ),
    ]
