# Generated by Django 2.2.4 on 2019-09-21 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_native', models.CharField(max_length=30, unique=True)),
                ('lang_english', models.CharField(max_length=30, unique=True)),
                ('lang_iso', models.CharField(default='en', max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('text_native', models.TextField()),
                ('lang_native', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='babel.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_translated', models.TextField()),
                ('lang_target', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='babel.Language')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babel.Message')),
            ],
            options={
                'unique_together': {('message', 'lang_target')},
            },
        ),
    ]
