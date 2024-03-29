# Generated by Django 5.0.2 on 2024-02-07 19:48

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Full name of the member.', max_length=200)),
                ('id_number', models.CharField(help_text='ID number of the member.', max_length=100, unique=True)),
                ('phone_number', models.CharField(help_text='Phone number of the member.', max_length=15)),
                ('email', models.EmailField(help_text='Email address of the member.', max_length=254)),
                ('role', models.CharField(help_text='Role of the member in the group.', max_length=100)),
                ('date_of_joining', models.DateField(default=django.utils.timezone.now, help_text='The date when the member joined the group.')),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Dormant')], default='A', help_text='Whether the member is active or dormant.', max_length=1)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], help_text='Gender of the member.', max_length=1)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='silc.silcgroup')),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
        ),
    ]
