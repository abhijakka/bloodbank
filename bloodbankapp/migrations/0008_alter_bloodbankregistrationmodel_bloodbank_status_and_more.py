# Generated by Django 4.0.3 on 2022-05-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankapp', '0007_alter_bloodbankregistrationmodel_bloodbank_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodbankregistrationmodel',
            name='bloodbank_status',
            field=models.CharField(default='Pending', help_text='bloodbank_status', max_length=200),
        ),
        migrations.AlterField(
            model_name='bloodbanksendrequestmodel',
            name='status',
            field=models.CharField(default='Pending', help_text='status', max_length=50),
        ),
    ]
