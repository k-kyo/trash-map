# Generated by Django 3.2.8 on 2021-10-31 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='緯度')),
                ('lon', models.FloatField(verbose_name='経度')),
                ('type', models.CharField(blank=True, max_length=10, verbose_name='種類')),
                ('remark', models.CharField(blank=True, max_length=30, verbose_name='備考')),
                ('crated_at', models.DateField(auto_now_add=True, verbose_name='作成日時')),
            ],
        ),
    ]