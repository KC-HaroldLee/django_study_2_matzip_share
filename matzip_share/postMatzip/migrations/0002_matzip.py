# Generated by Django 4.0.3 on 2022-04-17 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postMatzip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matzip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matzip_name', models.CharField(max_length=50)),
                ('matzip_link', models.CharField(max_length=100)),
                ('matzip_content', models.TextField()),
                ('matzip_keyword', models.CharField(max_length=50)),
                ('category', models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, to='postMatzip.category')),
            ],
        ),
    ]
