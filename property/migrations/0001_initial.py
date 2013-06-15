# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Property'
        db.create_table(u'property_property', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('reference', self.gf('django.db.models.fields.CharField')(unique=True, max_length=300)),
            ('house', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=220)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.City'])),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('property_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.PropertyChoice'])),
            ('sale_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.SaleStatus'])),
            ('furnished', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('rooms', self.gf('django.db.models.fields.IntegerField')()),
            ('bathrooms', self.gf('django.db.models.fields.IntegerField')()),
            ('garden', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('garden_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.GardenChoice'])),
            ('pool', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('parking', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('parking_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.ParkingChoice'])),
            ('property_desc', self.gf('django.db.models.fields.TextField')()),
            ('location_desc', self.gf('django.db.models.fields.TextField')()),
            ('schedule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Schedule'])),
            ('floorplan', self.gf('django.db.models.fields.related.ForeignKey')(default='None', to=orm['property.FloorPlan'])),
        ))
        db.send_create_signal(u'property', ['Property'])

        # Adding model 'PropertyChoice'
        db.create_table(u'property_propertychoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('option', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('value', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal(u'property', ['PropertyChoice'])

        # Adding model 'SaleStatus'
        db.create_table(u'property_salestatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('option', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('value', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal(u'property', ['SaleStatus'])

        # Adding model 'GardenChoice'
        db.create_table(u'property_gardenchoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('option', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('value', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal(u'property', ['GardenChoice'])

        # Adding model 'ParkingChoice'
        db.create_table(u'property_parkingchoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('option', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('value', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal(u'property', ['ParkingChoice'])

        # Adding model 'Country'
        db.create_table(u'property_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'property', ['Country'])

        # Adding model 'City'
        db.create_table(u'property_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Country'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'property', ['City'])

        # Adding model 'Schedule'
        db.create_table(u'property_schedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='None', max_length=50, null=True, blank=True)),
            ('schedule', self.gf('django.db.models.fields.files.FileField')(default='None', max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'property', ['Schedule'])

        # Adding model 'FloorPlan'
        db.create_table(u'property_floorplan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='None', max_length=50, null=True, blank=True)),
            ('floorplan', self.gf('django.db.models.fields.files.FileField')(default='None', max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'property', ['FloorPlan'])


    def backwards(self, orm):
        # Deleting model 'Property'
        db.delete_table(u'property_property')

        # Deleting model 'PropertyChoice'
        db.delete_table(u'property_propertychoice')

        # Deleting model 'SaleStatus'
        db.delete_table(u'property_salestatus')

        # Deleting model 'GardenChoice'
        db.delete_table(u'property_gardenchoice')

        # Deleting model 'ParkingChoice'
        db.delete_table(u'property_parkingchoice')

        # Deleting model 'Country'
        db.delete_table(u'property_country')

        # Deleting model 'City'
        db.delete_table(u'property_city')

        # Deleting model 'Schedule'
        db.delete_table(u'property_schedule')

        # Deleting model 'FloorPlan'
        db.delete_table(u'property_floorplan')


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