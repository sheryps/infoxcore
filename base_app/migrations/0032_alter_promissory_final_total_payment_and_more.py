# Generated by Django 4.0.1 on 2022-07-26 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0031_alter_promissory_final_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promissory',
            name='final_total_payment',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='promissory',
            name='inital_total_payment',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='promissory',
            name='second_total_payment',
            field=models.IntegerField(default='0'),
        ),
    ]