# Generated by Django 2.2 on 2019-04-23 01:35

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stemmers_comparer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('total', models.PositiveIntegerField(default=0)),
                ('average', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=6)),
                ('stemmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stemmers_comparer.Stemmer')),
            ],
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('user_email_address', models.EmailField(max_length=254, unique=True)),
                ('user_github_account_link', models.CharField(max_length=255, null=True)),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now=True)),
                ('score', models.PositiveSmallIntegerField()),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ratings', to='stemmers_comparer.Rate')),
            ],
            options={
                'unique_together': {('user_email_address', 'rating')},
            },
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]