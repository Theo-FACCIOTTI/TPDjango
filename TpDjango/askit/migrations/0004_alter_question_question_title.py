# Generated by Django 4.1.6 on 2023-02-12 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askit', '0003_alter_answer_answer_tag_alter_answer_answer_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_title',
            field=models.CharField(max_length=50),
        ),
    ]