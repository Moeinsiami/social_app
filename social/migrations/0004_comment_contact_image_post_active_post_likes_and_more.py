# Generated by Django 5.1.2 on 2024-11-14 18:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_post_tags'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='نام')),
                ('body', models.TextField(verbose_name='متن کامنت')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('active', models.BooleanField(default=True, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت ها',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='post_images/')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصویر ها',
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='saved_by',
            field=models.ManyToManyField(blank=True, related_name='saved_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='total_likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='total_saves',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='account_images/'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-total_likes'], name='social_post_total_l_b22ce0_idx'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='social.post', verbose_name='پست'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_from_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contact',
            name='user_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_to_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='social.Contact', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='social.post', verbose_name='پست'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['created'], name='social_comm_created_44dada_idx'),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['-created'], name='social_cont_created_5581d1_idx'),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['created'], name='social_imag_created_9b48a6_idx'),
        ),
    ]
