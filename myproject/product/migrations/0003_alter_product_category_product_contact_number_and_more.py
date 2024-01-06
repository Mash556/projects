# Generated by Django 5.0.1 on 2024-01-04 10:45

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('product', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='category.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='contact_number',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Номер контакта автора'),
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]