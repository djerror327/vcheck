from django.shortcuts import render

from .controller import Instances


def index(request):
    instance = Instances()
    instance_list = instance.get_instances_details()

    return render(request, "index.html", {'list': instance_list})
