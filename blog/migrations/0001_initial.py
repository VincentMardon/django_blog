# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('auteur', models.CharField(max_length=42)),
                ('contenu', models.TextField(null=True)),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
                ('is_visible', models.BooleanField(verbose_name='Article publié ?', default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('pseudo', models.CharField(max_length=42)),
                ('email', models.EmailField(max_length=254)),
                ('contenu', models.TextField()),
                ('date', models.DateTimeField(verbose_name='Date de publication', auto_now_add=True)),
                ('is_visible', models.BooleanField(verbose_name='Commentaire publié ?', default=True)),
                ('article', models.ForeignKey(to='blog.Article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ForeignKey(to='blog.Categorie'),
        ),
    ]
