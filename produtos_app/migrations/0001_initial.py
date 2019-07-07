# Generated by Django 2.1.7 on 2019-05-20 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(db_index=True, max_length=20)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
    ]