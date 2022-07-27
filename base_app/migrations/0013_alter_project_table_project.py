# Generated by Django 4.0.3 on 2022-04-28 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0012_alter_project_module_assign_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_table',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_table_name', to='base_app.project'),
        ),
    ]