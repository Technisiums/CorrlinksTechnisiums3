# Generated by Django 3.1.1 on 2020-10-11 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corrSMS', '0007_auto_20201011_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMSCustomer2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('phone_Number', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='corrlinks_ID',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='sms_Customer_2',
            field=models.ManyToManyField(to='corrSMS.SMSCustomer2'),
        ),
    ]