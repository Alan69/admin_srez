# Generated by Django 4.1.1 on 2022-10-26 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0002_remove_quiz_name_quiz_grade2_quiz_lng_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lng_id', models.CharField(blank=True, max_length=200, null=True)),
                ('lng_title', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='grade',
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('level', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('subcategory', models.CharField(blank=True, max_length=200, null=True)),
                ('decision', models.CharField(blank=True, max_length=200, null=True)),
                ('question', models.CharField(blank=True, max_length=200, null=True)),
                ('var1', models.CharField(blank=True, max_length=200, null=True)),
                ('var2', models.CharField(blank=True, max_length=200, null=True)),
                ('var3', models.CharField(blank=True, max_length=200, null=True)),
                ('var4', models.CharField(blank=True, max_length=200, null=True)),
                ('var5', models.CharField(blank=True, max_length=200, null=True)),
                ('answers', models.CharField(blank=True, max_length=200, null=True)),
                ('subject_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quizes.quiz')),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quizes.quizlanguage'),
            preserve_default=False,
        ),
    ]
