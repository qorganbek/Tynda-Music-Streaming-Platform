# Generated by Django 4.1.7 on 2023-04-07 09:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('second_name', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25, verbose_name='Category name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Title')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Image')),
                ('audio', models.FileField(upload_to='audios/%Y/%m/%d/', verbose_name='Audio File')),
                ('is_top', models.BooleanField(verbose_name='Is Top ?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artist', models.ManyToManyField(related_name='song', to='main.artist', verbose_name='Artists')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song', to='main.category', verbose_name='Categories')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
                'ordering': ['is_top', '-created_at'],
            },
        ),
    ]