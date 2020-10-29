# Generated by Django 3.1.1 on 2020-10-21 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corrSMS', '0016_auto_20201020_0511'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemToCorrlinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('snt', 'Sent'), ('dis', 'Disabled'), ('err', 'Error')], default='new', max_length=3)),
                ('subject', models.CharField(blank=True, max_length=40)),
                ('body', models.TextField(blank=True, max_length=4000, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corrSMS.customer')),
            ],
        ),
    ]