# coding: utf-8

from django.shortcuts import render

from services.models import Service


def status(request):
    services = Service.objects.all()
    return render(request, 'core/status.html', { 'services': services })