from django.shortcuts import render, redirect
from .models import Question, Category, Team


# Create your views here.
def home_page(request):
    categories = Category.objects.all()
    teams = Team.objects.all()
    data = {}
    for category in categories:
        data[category] = Question.objects.filter(category=category)
    context = {'teams': teams, 'data': data}
    return render(request, 'home.html', context)


def question(request, pk):
    question = Question.objects.get(id=pk)

    context = {'question': question}
    if request.method == 'POST':
        context['answer'] = question.answer
        context['home'] = '/'
    return render(request, 'question.html', context)


def show_teams(request):
    teams = Team.objects.all()
    numbers = [10, 20, 30, 40, 50]

    context = {'teams': teams, 'numbers': numbers}
    return render(request, 'teams.html', context)


def add_score(request, pk):
    team = Team.objects.get(id=pk)
    if request.method == 'POST':
        num = int(request.POST.get('score'))
        team.team_score = team.team_score + num
        team.save(update_fields=['team_score'])

        return redirect('/teams')
