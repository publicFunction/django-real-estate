# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BannerImages.link'
        db.add_column(u'banner_bannerimages', 'link',
                      self.gf('django.db.models.fields.URLField')(default='#', max_length=500),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BannerImages.link'
        db.delete_column(u'banner_bannerimages', 'link')


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
            'image_alt': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'link': ('django.db.models.fields.URLField', [], {'default': "'#'", 'max_length': '500'})
        }
    }

    complete_apps = ['banner']