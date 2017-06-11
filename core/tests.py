# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.core.urlresolvers import reverse_lazy

from .models import Url


class ShortenUrlTestCase(TestCase):
    url = 'http://www.example.com/this/is/a/long/url?foo=bar'

    def setUp(self):
        self.client = Client()
        self.client.post(reverse_lazy('create_url'), {'origin': self.url})

    def test_shorten_url_created(self):
        created_url = Url.objects.filter(origin=self.url).first()
        self.assertIsNotNone(created_url, "Url not created")

    def test_shorten_url_has_hash(self):
        created_url = Url.objects.filter(origin=self.url).first()
        self.assertIsNotNone(created_url.hash, "Url doesn't have hash")

    def test_resolve_shorten_url(self):
        created_url = Url.objects.filter(origin=self.url).first()
        response = self.client.get(
            reverse_lazy('resolve_url', kwargs={'url_hash': created_url.hash})
        )
        self.assertEqual(
            response.status_code, 302, "Url doesn't return redirect"
        )

    def tearDown(self):
        del self.client
