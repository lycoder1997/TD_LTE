# Generated by Django 2.1.1 on 2018-09-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0007_delete_test2'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbSecAdjcell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_SECTOR_ID', models.CharField(max_length=50)),
                ('N_SECTOR_ID', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tbSecAdjCell',
            },
        ),
    ]
