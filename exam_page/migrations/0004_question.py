# Generated by Django 2.2.4 on 2019-08-06 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam_page', '0003_exam_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_body', models.CharField(max_length=300)),
                ('question_type', models.CharField(max_length=50)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_deleted', models.IntegerField()),
                ('ip_address', models.GenericIPAddressField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_page.exam')),
            ],
        ),
    ]
