# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, View

from .models import Url
from .utils import get_url_hash
from .forms import UrlCreateForm


class UrlCreateView(CreateView):
    model = Url
    form_class = UrlCreateForm
    success_url = reverse_lazy('create_url')
    template_name = 'create_url.html'

    def form_valid(self, form):
        self.object = form.save()
        self.object.hash = get_url_hash()
        messages.success(
            self.request, 'Your shorten url is: http://{domain}/{hash}'.format(
                domain=self.request.get_host(), hash=self.object.hash
            )
        )
        return super(UrlCreateView, self).form_valid(form)


class UrlResolveView(View):
    def get(self, request, url_hash):
        url = get_object_or_404(Url, hash=url_hash)
        return HttpResponseRedirect(url.origin)
