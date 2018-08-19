# Generated by Django 2.0.7 on 2018-07-28 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hello', '0002_auto_20180728_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('label', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('country', models.CharField(blank=True, max_length=30)),
                ('region', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('postcode', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('longditude', models.FloatField(blank=True)),
                ('latitude', models.FloatField(blank=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceLabelLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Label')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Place')),
            ],
        ),
    ]