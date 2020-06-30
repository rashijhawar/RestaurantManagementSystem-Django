# Generated by Django 3.0.3 on 2020-06-06 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerId', models.IntegerField(primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=30)),
                ('phoneNo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemNo', models.IntegerField(primary_key=True, serialize=False)),
                ('itemName', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('managerID', models.IntegerField(primary_key=True, serialize=False)),
                ('managerName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('waiterID', models.IntegerField(primary_key=True, serialize=False)),
                ('waiterName', models.CharField(max_length=30)),
                ('managerID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rms.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('chefID', models.IntegerField(primary_key=True, serialize=False)),
                ('chefName', models.CharField(max_length=30)),
                ('managerID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rms.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='Cashier',
            fields=[
                ('cashierID', models.IntegerField(primary_key=True, serialize=False)),
                ('cashierName', models.CharField(max_length=30)),
                ('managerID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rms.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billNo', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('cashierID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rms.Cashier')),
                ('customerId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rms.Customer')),
                ('itemNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rms.Item')),
            ],
            options={
                'unique_together': {('billNo', 'itemNo')},
            },
        ),
    ]
