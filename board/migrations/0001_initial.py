# Generated by Django 2.2.1 on 2019-07-02 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('jumlah', models.IntegerField()),
                ('Jenis', models.CharField(max_length=10)),
                ('bukti', models.ImageField(upload_to='images/')),
                ('keterangan', models.TextField()),
            ],
        ),
    ]
