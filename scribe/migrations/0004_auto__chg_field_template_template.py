# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Template.template'
        db.alter_column('scribe_template', 'template', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'Template.template'
        db.alter_column('scribe_template', 'template', self.gf('django.db.models.fields.files.FileField')(max_length=100))

    models = {
        'scribe.email': {
            'Meta': {'object_name': 'Email'},
            'content': ('tinymce.models.HTMLField', [], {}),
            'header': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scribe.Header']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scribe.Template']"})
        },
        'scribe.header': {
            'Meta': {'object_name': 'Header'},
            'date_added': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'scribe.template': {
            'Meta': {'object_name': 'Template'},
            'date_added': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'template': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['scribe']