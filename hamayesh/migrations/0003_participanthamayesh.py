# Generated by Django 4.2.1 on 2024-03-05 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hamayesh', '0002_alter_hamayesh_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantHamayesh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=11)),
                ('full_name', models.CharField(max_length=255)),
                ('hamayesh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='hamayesh.hamayesh')),
            ],
        ),
    ]