# Generated by Django 4.1 on 2022-09-07 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('didTheyMove', '0002_rename_date_didtheymove_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='didtheymove',
            name='client',
            field=models.CharField(default='JB', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='didtheymove',
            name='status',
            field=models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent'), ('Recently Sold (6)', 'Recently Sold (6)'), ('Recently Sold (12)', 'Recently Sold (12)'), ('No Change', 'No Change')], default='No Change', max_length=20),
        ),
    ]
