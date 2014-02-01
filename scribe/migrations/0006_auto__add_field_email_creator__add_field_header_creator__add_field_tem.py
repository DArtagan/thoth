# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Email.creator'
        db.add_column('scribe_email', 'creator',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.User'], default=0, related_name='creator'),
                      keep_default=False)

        # Adding field 'Header.creator'
        db.add_column('scribe_header', 'creator',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.User'], default=0),
                      keep_default=False)

        # Adding field 'Template.creator'
        db.add_column('scribe_template', 'creator',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.User'], default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Email.creator'
        db.delete_column('scribe_email', 'creator_id')

        # Deleting field 'Header.creator'
        db.delete_column('scribe_header', 'creator_id')

        # Deleting field 'Template.creator'
        db.delete_column('scribe_template', 'creator_id')


    models = {
        'accounts.user': {
            'Meta': {'db_table': "'auth_user'", 'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'db_index': 'True', 'max_length': '255'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'scribe.email': {
            'Meta': {'object_name': 'Email'},
            'content': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.User']", 'related_name': "'creator'"}),
            'date_edited': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now': 'True'}),
            'header': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scribe.Header']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scribe.Template']"})
        },
        'scribe.header': {
            'Meta': {'object_name': 'Header'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.User']"}),
            'date_edited': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'scribe.template': {
            'Meta': {'object_name': 'Template'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.User']"}),
            'date_edited': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'template': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['scribe']