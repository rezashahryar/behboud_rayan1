# Generated by Django 4.2.3 on 2024-03-09 17:42

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('description', tinymce.models.HTMLField(verbose_name='توضیحات')),
                ('image', models.ImageField(default='04.jpg', upload_to='post/image/%Y/%m/%d/', verbose_name='عکس')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='مسیر یو ار ال')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ انتشار')),
                ('status', models.BooleanField(default=True)),
                ('counted_views', models.IntegerField(default=0, verbose_name='تعداد بازدید')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='datetime_created')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='datetime_updated')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
                'ordering': ('-published_date',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'بر چسب',
                'verbose_name_plural': 'بر چسب ها',
            },
        ),
    ]