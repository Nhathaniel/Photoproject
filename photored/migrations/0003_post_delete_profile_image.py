# Generated by Django 4.2.8 on 2024-05-14 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photored', '0002_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='post_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile_image',
        ),
    ]