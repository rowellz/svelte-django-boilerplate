# Generated by Django 3.2.16 on 2023-01-11 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChefyRecipeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_gpt_response', models.CharField(max_length=5000)),
                ('user', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Chefy Recipe Gen',
                'verbose_name_plural': 'Chefy Model',
                'db_table': 'chefy_recipe',
            },
        ),
    ]
