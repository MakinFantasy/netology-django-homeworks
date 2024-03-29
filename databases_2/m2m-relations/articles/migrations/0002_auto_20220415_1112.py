# Generated by Django 3.1.2 on 2022-04-15 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255, verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.CreateModel(
            name='Scopeship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Главная')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopeship', to='articles.article')),
                ('scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.scope')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='scope',
            field=models.ManyToManyField(through='articles.Scopeship', to='articles.Scope'),
        ),
    ]
