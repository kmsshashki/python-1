from django.http import HttpResponse
from django.template import loader

from .models import News


def news(request):
    latest_news_list = News.objects.order_by('-pub_date')[:5]
    template = loader.get_template('news/index.html')
    context = {
        'latest_news_list': latest_news_list,
    }
    return HttpResponse(template.render(context, request))