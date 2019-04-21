# Generated by Django 2.2 on 2019-04-21 18:58

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('stemmers_comparer', '0004_auto_20190421_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='average',
            field=models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=6),
        ),
        migrations.AddField(
            model_name='review',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='review',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('content_type', 'object_id')},
        ),
        migrations.RemoveField(
            model_name='review',
            name='stemmer',
        ),
    ]
