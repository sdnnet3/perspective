from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from prints.models import ArtisticPrint


def artistic_prints_list(request):
    prints = ArtisticPrint.objects.all()
    prints_info = []
    for print_instance in prints:
        info = print_instance.fetch_print_info()
        prints_info.append(info)
    return render(request, 'coderedcms/pages/artistic_prints_list.html', {'prints_info': prints_info})
