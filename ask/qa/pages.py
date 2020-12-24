from django.shortcuts import render
from django.core.paginator import Paginator
from qa.models import Question, Answer
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseNotFound

def pages(request):
    ques = Question.objects.new()
    prfx = reverse('home')
    page = request.GET.get('page', 1)
    pagin = Paginator(ques, 10)
    pagin.baseurl = prfx + '?page='
    page = pagin.page(page)
    return render(request, 'pages.html', {
        'ques': page.object_list,
        'pagin': pagin, 'page': page,
        'header': 'Home'
        }
    )

def populs(request):
    prfx = reverse('popular')
    ques = Question.objects.popular()
    page = request.GET.get('page', 1)
    pagin = Paginator(ques, 10)
    pagin.baseurl = prfx + '?page='
    page = pagin.page(page)
    return render(request, 'pages.html', {
        'ques': page.object_list,
        'pagin': pagin, 'page': page,
        'header': 'Most popular'
        }
    )

def quest(request, npag):
    try:
        n = int(npag)
        que = Question.objects.get(id=n)
    except:
        return HttpResponseNotFound()
    ans = Answer.objects.filter(question=n)
    ans = ans.order_by('added_at')
    return render(request, 'quest.html', {
        'quest': que,
        'ans': ans
        }
    )

