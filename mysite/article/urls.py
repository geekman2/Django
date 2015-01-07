# -------------------------------------------------------------------------------
# Name:        urls
# Purpose:    list urls within app
#
# Created:     '1/7/2015'
#-------------------------------------------------------------------------------
__author__ = 'Geekman2'

from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^all/$','article.views.stuffandthings'),
    url(r'^get/(?<article_id>\d*)/$','articles.views.stuffandthings'),
                        )