# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 13:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mpinstaller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('sf_oauth', models.TextField(blank=True, null=True)),
                ('github_issue', models.IntegerField(blank=True, null=True)),
                ('fork_branch', models.CharField(blank=True, max_length=255, null=True)),
                ('fork_merge_branch', models.CharField(blank=True, max_length=255, null=True)),
                ('main_branch', models.CharField(blank=True, max_length=255, null=True)),
                ('fork_pull', models.IntegerField(blank=True, null=True)),
                ('main_pull', models.IntegerField(blank=True, null=True)),
                ('default_branch_synced', models.BooleanField(default=False)),
                ('state_behind_main', models.BooleanField(default=False)),
                ('state_undeployed_commit', models.BooleanField(default=False)),
                ('state_uncommitted_changes', models.BooleanField(default=False)),
                ('last_deployed_date', models.DateTimeField(blank=True, null=True)),
                ('last_deployed_commit', models.CharField(blank=True, max_length=255, null=True)),
                ('last_retrieve_checksum', models.CharField(blank=True, max_length=255, null=True)),
                ('date_started', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('release_url', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContributionSync',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(b'pending', b'Pending'), (b'in_progress', b'In Progress'), (b'success', b'Successful'), (b'fail', b'Failed')], default=b'pending', max_length=32)),
                ('log', models.TextField(blank=True, default=b'', null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('new_commit', models.CharField(blank=True, max_length=64, null=True)),
                ('initial_state_behind_main', models.BooleanField()),
                ('initial_state_undeployed_commit', models.BooleanField()),
                ('initial_state_uncommitted_changes', models.BooleanField()),
                ('pre_state_behind_main', models.BooleanField()),
                ('pre_state_undeployed_commit', models.BooleanField()),
                ('pre_state_uncommitted_changes', models.BooleanField()),
                ('post_state_behind_main', models.BooleanField()),
                ('post_state_undeployed_commit', models.BooleanField()),
                ('post_state_uncommitted_changes', models.BooleanField()),
                ('date_started', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('contribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='syncs', to='contributor.Contribution')),
                ('new_installation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contribution_syncs', to='mpinstaller.PackageInstallation')),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contribution',
            name='contributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributions', to='contributor.Contributor'),
        ),
        migrations.AddField(
            model_name='contribution',
            name='last_deployment_installation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contributions', to='mpinstaller.PackageInstallation'),
        ),
        migrations.AddField(
            model_name='contribution',
            name='package_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributions', to='mpinstaller.PackageVersion'),
        ),
    ]
