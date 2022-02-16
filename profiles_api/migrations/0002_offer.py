# Generated by Django 3.2.12 on 2022-02-16 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_num', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('firm_name', models.CharField(max_length=300)),
                ('city_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]