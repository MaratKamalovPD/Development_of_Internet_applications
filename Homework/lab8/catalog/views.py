from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Processor
from .models import Report


def index(request):
    processors_list = Processor.objects.all()
    reports_1 = Report.objects.filter(processor_id=1)
    reports_2 = Report.objects.filter(processor_id=2)
    reports_3 = Report.objects.filter(processor_id=3)
    reports_4 = Report.objects.filter(processor_id=4)
    context = {'processors_list': processors_list, 'reports_1': reports_1, 'reports_2': reports_2, 'reports_3': reports_3, 'reports_4': reports_4}
    return render(request, 'catalog/index.html', context)


def detail(request, processor_id):
    processor = Processor.objects.get(id=processor_id)
    report_1 = Report.objects.get(processor_id=processor_id, year=2017)
    report_2 = Report.objects.get(processor_id=processor_id, year=2018)
    report_3 = Report.objects.get(processor_id=processor_id, year=2019)
    report_4 = Report.objects.get(processor_id=processor_id, year=2020)
    report_profit_sum = report_1.profit + report_2.profit + report_3.profit + report_4.profit

    context = {'processor': processor, 'report_1': report_1, 'report_2': report_2, 'report_3': report_3, 'report_4': report_4,
               'report_profit_sum': report_profit_sum}
    return render(request, 'catalog/detail.html', context)