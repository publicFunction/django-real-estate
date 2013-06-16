# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'searchLog'
        db.create_table(u'search_searchlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('searchType', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('no_of_bedrooms', self.gf('django.db.models.fields.IntegerField')()),
            ('price_from', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('price_to', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'search', ['searchLog'])


    def backwards(self, orm):
        # Deleting model 'searchLog'
        db.delete_table(u'search_searchlog')


    models = {
        u'search.searchlog': {
            'Meta': {'object_name': 'searchLog'},
            'address': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_of_bedrooms': ('django.db.models.fields.IntegerField', [], {}),
            'price_from': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price_to': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'searchType': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['search']