# Generated by Django 4.1.3 on 2022-11-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_delete_feedbackcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=20, null=True)),
                ('age', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=12, null=True)),
                ('satisfied', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=5)),
                ('feedback', models.CharField(max_length=95, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
