# Generated by Django 4.1.6 on 2023-02-12 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('askit', '0002_alter_answer_answer_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_tag',
            field=models.ManyToManyField(blank=True, to='askit.tag'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_tag',
            field=models.ManyToManyField(blank=True, to='askit.tag'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='askit.topic'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
