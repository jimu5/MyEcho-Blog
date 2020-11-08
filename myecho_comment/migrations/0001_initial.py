# Generated by Django 3.1.3 on 2020-11-08 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myecho_article', '0001_initial'),
        ('sso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, db_column='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, db_column='update_time')),
                ('is_deleted', models.BooleanField(default=False)),
                ('id', models.AutoField(editable=False, help_text='主键', primary_key=True, serialize=False, verbose_name='id')),
                ('user_name', models.CharField(default='null', max_length=50, verbose_name='评论人姓名')),
                ('user_ip', models.GenericIPAddressField(verbose_name='评论人ip')),
                ('user_site', models.CharField(max_length=128, null=True, verbose_name='评论人网站')),
                ('user_email', models.EmailField(max_length=254, null=True, verbose_name='评论人邮箱')),
                ('content', models.CharField(max_length=512, verbose_name='评论内容')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myecho_article.article', verbose_name='文章')),
                ('father_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myecho_comment.comment', verbose_name='父级评论')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sso.user', verbose_name='评论人')),
            ],
            options={
                'db_table': 'myecho_comment',
            },
        ),
    ]
