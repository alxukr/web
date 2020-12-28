from django.shortcuts import render
from django.core.paginator import Paginator
from qa.models import Question, Answer
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from qa.forms import AnswerForm, AskForm, SignupForm, LoginForm
from django.contrib import auth
from django.contrib.auth.models import User

def pages(request, name):
    if name == 'home':
        ques = Question.objects.new()
        prfx = reverse('home')
    if name == 'popular':
        ques = Question.objects.popular()
        prfx = reverse('popular')
    page = request.GET.get('page', 1)
    pagin = Paginator(ques, 10)
    pagin.baseurl = prfx + '?page='
    page = pagin.page(page)
    return render(request, 'pages.html', {
        'ques': page.object_list,
        'pagin': pagin, 'page': page,
        'header': name.capitalize()
        }
    )


def quest(request, slug):
    try:
        n = int(slug)
        que = Question.objects.get(id=n)
    except:
        return HttpResponseNotFound()
    ans = Answer.objects.filter(question=n)
    ans = ans.order_by('added_at')
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            txt = request.POST['text']
            qw = Question.objects.get(id = request.POST['question'])
            c = Answer.objects.create(text = txt, question = qw, author = request.user)
            return HttpResponseRedirect(que.get_url())
    else:
        form = AnswerForm(initial = {'question': que.id})
    return render(request, 'quest.html', {
        'quest': que,
        'ans': ans, 'form': form,
        }
    )


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            txt = request.POST['text']
            tit = request.POST['title']
            c = Question.objects.create(text = txt, title = tit, author = request.user)
            return HttpResponseRedirect(c.get_url())
        else:
            form = AskForm(initial = {'title': request.POST.get('title', ''), 'text': request.POST.get('text', '')})
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form,
        }
    )


def signup(request):
    if request.method == 'POST':
        pw = request.POST.get('password', '')
        un = request.POST.get('username', '')
        em = request.POST.get('email', '')
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(un, em, pw)
            user = auth.authenticate(username=un, password = pw)
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            form = SignupForm(request.POST)
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form': form })


def login(request):
    if request.method == 'POST':
        pw = request.POST.get('password', '')
        un = request.POST.get('username', '')
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=un, password=pw)
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            form = LoginForm(request.POST)
    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'form': form })
