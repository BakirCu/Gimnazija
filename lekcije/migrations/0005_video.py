# Generated by Django 2.2.6 on 2020-03-28 16:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lekcije', '0004_auto_20200328_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naslov', models.CharField(max_length=300)),
                ('nalepi_link', models.CharField(max_length=100)),
                ('predmet', models.CharField(choices=[('Matematika', 'Matematika'), ('Fizika', 'Fizika'), ('Srpski jezik i književnost', 'Srpski jezik i književnost'), ('Srpski kao nematernji jezik', 'Srpski kao nematernji'), ('Bosanski jezik i književnost', 'Bosanski jezik i književnost'), ('Engleski jezik', 'Engleski jezik'), ('Nemački jezik', 'Nemački jezik'), ('Francuski jezik', 'Francuski jezik'), ('Latinski jezik', 'Latinski jezik'), ('Istorija', 'Istorija'), ('Geografija', 'Geografija'), ('Biologija', 'Biologija'), ('Hemija', 'Hemija'), ('Računarstvo i informatika', 'Računarstvo i informatika'), ('Muzička kultura', 'Muzička kultura'), ('Likovna kultura', 'Likovna kultura'), ('Fizičko vaspitanje', 'Fizičko vaspitanje'), ('Građansko vaspitanje', 'Građansko vaspitanje'), ('Islamska veronauka', 'Islamska veronauka'), ('Pravoslavna veronauka', 'Pravoslavna veronauka'), ('Jezik medija i kultura', 'Jezik medija i kultura'), ('Primenjene nauke', 'Primenjene nauke'), ('Umetnost i dizajn', 'Umetnost i dizajn'), ('Zdravlje i sport', 'Zdravlje i sport'), ('Psihologija', 'Psihologija'), ('Filozofija', 'Filozofija'), ('Sociologija', 'Sociologija'), ('Ustav i prava građana', 'Ustav i prava građana')], max_length=40)),
                ('godina', models.CharField(choices=[('Prva godina', 'Prva godina'), ('Druga godina', 'Druga godina'), ('Treća godina', 'Treća godina'), ('Četvrta godina', 'Četvrta godina')], max_length=40)),
                ('autor', models.CharField(max_length=40)),
                ('vreme_posta', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Dodaj video(ako želiš)',
                'ordering': ['autor'],
            },
        ),
    ]
