# Generated by Django 4.0.2 on 2022-05-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0017_acntspayslip_net_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_head', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('description_paymenthead', models.TextField()),
            ],
        ),
    ]
