# Generated by Django 2.1.15 on 2021-06-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassAvails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CRN', models.PositiveIntegerField()),
                ('department', models.CharField(max_length=200)),
                ('courseNumber', models.PositiveIntegerField()),
            ],
        ),
    ]