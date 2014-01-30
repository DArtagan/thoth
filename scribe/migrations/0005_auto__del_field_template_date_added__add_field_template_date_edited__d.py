# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Template.date_added'
        db.delete_column('scribe_template', 'date_added')

        # Adding field 'Template.date_edited'
        db.add_column('scribe_template', 'date_edited',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, default=datetime.datetime(2014, 1, 30, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Header.date_added'
        db.delete_column('scribe_header', 'date_added')

        # Adding field 'Header.date_edited'
        db.add_column('scribe_header', 'date_edited',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, default=datetime.datetime(2014, 1, 30, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Email.date_edited'
        db.add_column('scribe_email', 'date_edited',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, default=datetime.datetime(2014, 1, 30, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Template.date_added'
        raise RuntimeError("Cannot reverse this migration. 'Template.date_added' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Template.date_added'
        db.add_column('scribe_template', 'date_added',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True),
                      keep_default=False)

        # Deleting field 'Template.date_edited'
        db.delete_column('scribe_template', 'date_edited')


        # User chose to not deal with backwards NULL issues for 'Header.date_added'
        raise RuntimeError("Cannot reverse this migration. 'Header.date_added' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Header.date_added'
        db.add_column('scribe_header', 'date_added',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True),
                      keep_default=False)

        # Deleting field 'Header.date_edited'
        db.delete_column('scribe_header', 'date_edited')

        # Deleting field 'Email.date_edited'
        db.delete_column('scribe_email', 'date_edited')


    models = {
        'scribe.email': {
            'Meta': {'object_name': 'Email'},
            'content': ('tinymce.models.HTMLField', [], {}),
            'date_edited': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scribe.Header']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scribe.Template']"})
        },
        'scribe.header': {
            'Meta': {'object_name': 'Header'},
            'date_edited': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'scribe.template': {
            'Meta': {'object_name': 'Template'},
            'date_edited': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'template': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['scribe']