# Generated by Django 4.0 on 2022-01-23 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_hospital_locationname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('isRead', models.BooleanField(default=False)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.appointment')),
            ],
        ),
    ]
