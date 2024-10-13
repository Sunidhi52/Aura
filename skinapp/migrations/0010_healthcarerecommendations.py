# Generated by Django 5.0.7 on 2024-10-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skinapp', '0009_delete_body_recommendations'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthcareRecommendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_image_url', models.URLField(max_length=500)),
                ('purchase_link', models.URLField(max_length=500)),
            ],
        ),
    ]
