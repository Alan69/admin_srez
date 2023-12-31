# Generated by Django 4.1.1 on 2022-12-28 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quizes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel_file', models.FileField(upload_to='files', verbose_name='Excel ученики')),
            ],
            options={
                'verbose_name_plural': 'Список школьников',
            },
        ),
        migrations.CreateModel(
            name='RequestQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=120, verbose_name='Школа')),
                ('student_amount', models.IntegerField(null=True, verbose_name='колво учеников')),
                ('summa', models.IntegerField(null=True, verbose_name='Сумма')),
                ('dogovor', models.CharField(blank=True, max_length=120, verbose_name='Договор')),
                ('name', models.CharField(blank=True, max_length=120, verbose_name='Ответственное лицо(ФИО)')),
                ('iin', models.CharField(blank=True, max_length=120, verbose_name='ИИН')),
                ('number', models.CharField(blank=True, max_length=120, verbose_name='Номер')),
                ('limit_in_month', models.IntegerField(null=True, verbose_name='Лимит в месяц')),
                ('limit_start', models.DateField(blank=True, default=None, null=True, verbose_name='начало')),
                ('limit_end', models.DateField(blank=True, default=None, null=True, verbose_name='конец')),
                ('kvitancia', models.FileField(blank=True, null=True, upload_to='files', verbose_name='Квитанция договор')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активность договора')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.region', verbose_name='Регион')),
            ],
            options={
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
