# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SiteTitle'
        db.create_table(u'site_setup_sitetitle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('seperator', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'site_setup', ['SiteTitle'])

        # Adding model 'SiteHeaderImage'
        db.create_table(u'site_setup_siteheaderimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'site_setup', ['SiteHeaderImage'])

        # Adding model 'SiteCurrencyList'
        db.create_table(u'site_setup_sitecurrencylist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('currency_symbol', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('currency_code', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'site_setup', ['SiteCurrencyList'])

        # Adding model 'SiteCurrency'
        db.create_table(u'site_setup_sitecurrency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_setup.SiteCurrencyList'])),
        ))
        db.send_create_signal(u'site_setup', ['SiteCurrency'])


    def backwards(self, orm):
        # Deleting model 'SiteTitle'
        db.delete_table(u'site_setup_sitetitle')

        # Deleting model 'SiteHeaderImage'
        db.delete_table(u'site_setup_siteheaderimage')

        # Deleting model 'SiteCurrencyList'
        db.delete_table(u'site_setup_sitecurrencylist')

        # Deleting model 'SiteCurrency'
        db.delete_table(u'site_setup_sitecurrency')


    models = {
        u'site_setup.sitecurrency': {
            'Meta': {'object_name': 'SiteCurrency'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_setup.SiteCurrencyList']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'site_setup.sitecurrencylist': {
            'Meta': {'object_name': 'SiteCurrencyList'},
            'currency_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'currency_symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'site_setup.siteheaderimage': {
            'Meta': {'object_name': 'SiteHeaderImage'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'site_setup.sitetitle': {
            'Meta': {'object_name': 'SiteTitle'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seperator': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['site_setup']