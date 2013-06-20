# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Office.contact_number'
        db.add_column(u'office_office', 'contact_number',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=25),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Office.contact_number'
        db.delete_column(u'office_office', 'contact_number')


    models = {
        u'office.office': {
            'Meta': {'object_name': 'Office'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['property.City']"}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '500'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'street_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'street_number': ('django.db.models.fields.IntegerField', [], {})
        },
        u'office.officegeolocation': {
            'Meta': {'object_name': 'OfficeGeoLocation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'office': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['office.Office']"})
        },
        u'property.city': {
            'Meta': {'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['property.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'property.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['office']