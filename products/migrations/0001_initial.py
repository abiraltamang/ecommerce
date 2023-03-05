# Generated by Django 3.2.12 on 2023-03-03 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('caption', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': '4. Brand',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('caption', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': '1. Category',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('caption', models.CharField(max_length=255)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'verbose_name': '2. Subcategory',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('caption', models.CharField(max_length=255)),
                ('subcategory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.subcategory')),
            ],
            options={
                'verbose_name': '3. Type',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/')),
                ('name', models.CharField(max_length=25)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('discount', models.FloatField(default=0)),
                ('status', models.BooleanField()),
                ('details', models.TextField(blank=True, null=True)),
                ('features', models.TextField(blank=True, null=True)),
                ('specification', models.TextField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.type')),
            ],
            options={
                'verbose_name': '5. Product',
            },
        ),
    ]
