# Generated by Django 3.2.2 on 2023-10-20 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0003_auto_20231020_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='comic',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.comic'),
        ),
    ]
