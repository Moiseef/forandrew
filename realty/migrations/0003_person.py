# Generated by Django 4.0.3 on 2023-03-03 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0002_remove_question_pub_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
