# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Email'
        db.create_table('scribe_email', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scribe.Template'])),
            ('header', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scribe.Header'])),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('scribe', ['Email'])

        # Adding model 'Template'
        db.create_table('scribe_template', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('template', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('scribe', ['Template'])

        # Adding model 'Header'
        db.create_table('scribe_header', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('scribe', ['Header'])


    def backwards(self, orm):
        # Deleting model 'Email'
        db.delete_table('scribe_email')

        # Deleting model 'Template'
        db.delete_table('scribe_template')

        # Deleting model 'Header'
        db.delete_table('scribe_header')


    models = {
        'scribe.email': {
            'Meta': {'object_name': 'Email'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'header': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scribe.Header']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scribe.Template']"})
        },
        'scribe.header': {
            'Meta': {'object_name': 'Header'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'scribe.template': {
            'Meta': {'object_name': 'Template'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'template': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['scribe']