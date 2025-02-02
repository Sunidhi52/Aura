# Generated by Django 5.0.7 on 2024-09-30 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skinapp', '0004_alter_combinationskin_image_alter_dryskin_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='combinationskin',
            old_name='image',
            new_name='face_image',
        ),
        migrations.RenameField(
            model_name='dryskin',
            old_name='image',
            new_name='face_image',
        ),
        migrations.RenameField(
            model_name='normalskin',
            old_name='image',
            new_name='face_image',
        ),
        migrations.RenameField(
            model_name='oilyskin',
            old_name='image',
            new_name='face_image',
        ),
        migrations.AddField(
            model_name='combinationskin',
            name='moisturizer_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='combinationskin',
            name='serum_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='combinationskin',
            name='sunscreen_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='dryskin',
            name='moisturizer_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='dryskin',
            name='serum_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='dryskin',
            name='sunscreen_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='normalskin',
            name='moisturizer_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='normalskin',
            name='serum_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='normalskin',
            name='sunscreen_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='oilyskin',
            name='moisturizer_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='oilyskin',
            name='serum_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='oilyskin',
            name='sunscreen_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
