# Generated by Django 5.1.1 on 2024-09-29 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CombinationSkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facewash_name', models.CharField(max_length=200)),
                ('facewash_image', models.ImageField(upload_to='products/combination/facewash/')),
                ('moisturizer_name', models.CharField(max_length=200)),
                ('moisturizer_image', models.ImageField(upload_to='products/combination/moisturizer/')),
                ('serum_name', models.CharField(max_length=200)),
                ('serum_image', models.ImageField(upload_to='products/combination/serum/')),
                ('sunscreen_name', models.CharField(max_length=200)),
                ('sunscreen_image', models.ImageField(upload_to='products/combination/sunscreen/')),
            ],
        ),
        migrations.CreateModel(
            name='DrySkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facewash_name', models.CharField(max_length=200)),
                ('facewash_image', models.ImageField(upload_to='products/dry/facewash/')),
                ('moisturizer_name', models.CharField(max_length=200)),
                ('moisturizer_image', models.ImageField(upload_to='products/dry/moisturizer/')),
                ('serum_name', models.CharField(max_length=200)),
                ('serum_image', models.ImageField(upload_to='products/dry/serum/')),
                ('sunscreen_name', models.CharField(max_length=200)),
                ('sunscreen_image', models.ImageField(upload_to='products/dry/sunscreen/')),
            ],
        ),
        migrations.CreateModel(
            name='NormalSkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facewash_name', models.CharField(max_length=200)),
                ('facewash_image', models.ImageField(upload_to='products/normal/facewash/')),
                ('moisturizer_name', models.CharField(max_length=200)),
                ('moisturizer_image', models.ImageField(upload_to='products/normal/moisturizer/')),
                ('serum_name', models.CharField(max_length=200)),
                ('serum_image', models.ImageField(upload_to='products/normal/serum/')),
                ('sunscreen_name', models.CharField(max_length=200)),
                ('sunscreen_image', models.ImageField(upload_to='products/normal/sunscreen/')),
            ],
        ),
        migrations.CreateModel(
            name='OilySkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facewash_name', models.CharField(max_length=200)),
                ('facewash_image', models.ImageField(upload_to='products/oily/facewash/')),
                ('moisturizer_name', models.CharField(max_length=200)),
                ('moisturizer_image', models.ImageField(upload_to='products/oily/moisturizer/')),
                ('serum_name', models.CharField(max_length=200)),
                ('serum_image', models.ImageField(upload_to='products/oily/serum/')),
                ('sunscreen_name', models.CharField(max_length=200)),
                ('sunscreen_image', models.ImageField(upload_to='products/oily/sunscreen/')),
            ],
        ),
    ]
