# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Banner'
        db.create_table(u'banner_banner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('link_option', self.gf('django.db.models.fields.CharField')(default='T', max_length=20)),
        ))
        db.send_create_signal(u'banner', ['Banner'])

        # Adding model 'BannerImages'
        db.create_table(u'banner_bannerimages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('banner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['banner.Banner'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('image_alt', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'banner', ['BannerImages'])


    def backwards(self, orm):
        # Deleting model 'Banner'
        db.delete_table(u'banner_banner')

        # Deleting model 'BannerImages'
        db.delete_table(u'banner_bannerimages')


    models = {
        u'banner.banner': {
            'Meta': {'object_name': 'Banner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_option': ('django.db.models.fields.CharField', [], {'default': "'T'", 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'banner.bannerimages': {
            'Meta': {'object_name': 'BannerImages'},
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['banner.Banner']"}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_alt': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['banner']