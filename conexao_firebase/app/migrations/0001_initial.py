# Generated by Django 4.1.3 on 2022-11-22 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questEconomico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modalidade', models.CharField(max_length=20)),
                ('nome_estudante', models.CharField(max_length=20)),
                ('matricula', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=20)),
                ('data_nascimento', models.DateTimeField(verbose_name='Data_nascimento')),
                ('curso', models.CharField(max_length=20)),
                ('Identidade', models.CharField(max_length=10)),
                ('renumeracao', models.CharField(max_length=20)),
                ('nome_Completo', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=20)),
                ('Data_Nascimento', models.DateField(verbose_name='Data_nascimento')),
                ('endereco', models.CharField(max_length=20)),
                ('nrTelCelular', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone celular')),
            ],
        ),
    ]
