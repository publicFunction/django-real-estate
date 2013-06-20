# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Staff'
        db.create_table(u'staff_staff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('blurb', self.gf('django.db.models.fields.TextField')()),
            ('comment', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
        ))
        db.send_create_signal(u'staff', ['Staff'])


    def backwards(self, orm):
        # Deleting model 'Staff'
        db.delete_table(u'staff_staff')


    models = {
        u'staff.staff': {
            'Meta': {'object_name': 'Staff'},
            'blurb': ('django.db.models.fields.TextField', [], {}),
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['staff']