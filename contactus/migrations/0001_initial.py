# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactUs'
        db.create_table(u'contactus_contactus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('contact_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contactus', ['ContactUs'])


    def backwards(self, orm):
        # Deleting model 'ContactUs'
        db.delete_table(u'contactus_contactus')


    models = {
        u'contactus.contactus': {
            'Meta': {'object_name': 'ContactUs'},
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'customer': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['contactus']