# Generated by Django 4.0.3 on 2022-03-07 11:52

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViajesIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduccion', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='viaje',
            name='slug',
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]
