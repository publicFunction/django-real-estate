# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Property.featured'
        db.add_column(u'property_property', 'featured',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Property.featured'
        db.delete_column(u'property_property', 'featured')


    models = {
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
        },
        u'property.featuredproperty': {
            'Meta': {'object_name': 'FeaturedProperty'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['property.Property']"})
        },
        u'property.floorplan': {
            'Meta': {'object_name': 'FloorPlan'},
            'floorplan': ('django.db.models.fields.files.FileField', [], {'default': "'None'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'property.gardenchoice': {
            'Meta': {'object_name': 'GardenChoice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        u'property.parkingchoice': {
            'Meta': {'object_name': 'ParkingChoice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        u'property.property': {
            'Meta': {'object_name': 'Property'},
            'bathrooms': ('django.db.models.fields.IntegerField', [], {}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['property.City']"}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'floorplan': ('django.db.models.fields.related.ForeignKey', [], {'default': "'None'", 'to': u"orm['property.FloorPlan']"}),
            'furnished': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'garden': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'garden_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['property.GardenChoice']"}),
            'house': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_desc': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'parking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parking_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['property.ParkingChoice']"}),
            'pool': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'property_desc': ('django.db.models.fields.TextField', [], {}),
            'property_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['property.PropertyChoice']"}),
            'reference': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '300'}),
            'rooms': ('django.db.models.fields.IntegerField', [], {}),
            'sale_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['property.SaleStatus']"}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['property.Schedule']"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '220'})
        },
        u'property.propertychoice': {
            'Meta': {'object_name': 'PropertyChoice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        u'property.salestatus': {
            'Meta': {'object_name': 'SaleStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        u'property.schedule': {
            'Meta': {'object_name': 'Schedule'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'schedule': ('django.db.models.fields.files.FileField', [], {'default': "'None'", 'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['property']