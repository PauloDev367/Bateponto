# Generated by Django 4.2.20 on 2025-03-25 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceverifier', '0003_applicationuser_user_webapp_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClockIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255, null=True)),
                ('user_email', models.EmailField(max_length=254, null=True)),
                ('user_id', models.BigIntegerField(null=True)),
                ('status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('insert_method', models.CharField(max_length=255)),
                ('foto_sended', models.ImageField(null=True, upload_to='clockin-submition/')),
            ],
        ),
        migrations.AddField(
            model_name='applicationuser',
            name='end_work_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='applicationuser',
            name='start_work_time',
            field=models.TimeField(null=True),
        ),
    ]
