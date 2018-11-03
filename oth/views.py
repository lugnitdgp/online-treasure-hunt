from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect , JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import models
from django.contrib import messages
from oth import models
import datetime
import json

def landing(request):
    return render(request , 'countdown.html')


def index(request):

    m_level = models.total_level.objects.get(id=1)
    lastlevel = m_level.totallevel

    user = request.user
    if user.is_authenticated:
        player = models.player.objects.get(user_id=request.user.pk)
        if player.current_level > lastlevel:
            return render(request , 'wait.html' , {'player':player})
        try:
            level = models.level.objects.get(l_number=player.current_level)
            #print(request.path)
            #print(level.l_number)
            if request.path == '/home/' or (level.l_number > 1 and level.l_number < 11) or (level.l_number > 11 and level.l_number < 20) or (level.l_number > 20 and level.l_number <=25) :
                return render(request, 'question2.html', {'player': player, 'level': level})
            elif level.l_number == 20 and lastlevel == 25:
                return redirect('story3')
            elif level.l_number == 11 and lastlevel == 25: #11 #25
                return redirect('story2')
            elif level.l_number == 1 and lastlevel == 25:
                return redirect('story')
        except models.level.DoesNotExist:
            if player.current_level > lastlevel:
                # changes from win to wait toggled
                return render(request, 'wait.html', {'player': player})
            return render(request, 'wait.html', {'player': player})

    return render(request, 'index.html')


def story(request):
    if request.method == 'POST':
        return redirect('/home')
    else:
        return render(request , 'story.html')

def story2(request):
    if request.method == 'POST':
        return redirect('/home')
    else:
        return render(request , 'story2.html')


def story3(request):
    if request.method == 'POST':
        return redirect('/home')
    else:
        return render(request , 'story3.html')


def story4(request):
    if request.method == 'POST':
        return redirect('/home')
    else:
        return render(request , 'story4.html')


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        profile = user
        try:
            player = models.player.objects.get(user=profile)
        except:
            player = models.player(user=profile)
            player.name = response.get('name')
            player.timestamp=datetime.datetime.now()
            player.save()
    elif backend.name == 'google-oauth2':
        profile = user
        try:
            player = models.player.objects.get(user=profile)
        except:
            player = models.player(user=profile)
            player.timestamp=datetime.datetime.now()
            player.name = response.get('name')['givenName'] + " " + response.get('name')['familyName']
            player.save()
            

@login_required
def answer(request):
    
    m_level = models.total_level.objects.get(id=1)
    lastlevel = m_level.totallevel

    ans = ""
    if request.method == 'POST':
        ans = request.POST.get('ans')
    player = models.player.objects.get(user_id=request.user.pk)
    if player.current_level > lastlevel:
        return render(request , 'wait.html' , {'player':player})
    try:
        level = models.level.objects.get(l_number=player.current_level)
    except models.level.DoesNotExist:
        if player.current_level > lastlevel:
            # toggled
            return render(request, 'wait.html', {'player': player})
        return render(request, 'wait.html', {'player': player})

    if ans == level.answer:
        player.current_level = player.current_level + 1
        player.score = player.score + 10
        player.timestamp = datetime.datetime.now()
        level.numuser = level.numuser + 1
        level.accuracy = round(level.numuser/(float(level.numuser + level.wrong)),2)
        level.save()
        player.save()

        try:
            level = models.level.objects.get(l_number=player.current_level)
            return render(request, 'level_transition.html')

            return render(request, 'question2.html', {'player': player, 'level': level})
        except:
            if player.current_level > lastlevel:
                # toggled
                return render(request, 'wait.html', {'player': player}) 
            return render(request, 'wait.html', {'player': player})
    elif ans=="" and request.method == 'POST':
        pass 
        messages.error(request , "Please enter an answer !")

    else:
        if request.method == 'POST':
            level.wrong = level.wrong + 1
            level.save()
            messages.error(request, "Wrong Answer!, Try Again")

    return render(request, 'question2.html', {'player': player, 'level': level})



# Leaderboard view
def lboard(request):
    p = models.player.objects.order_by('-score','timestamp')
    cur_rank = 1

    for pl in p:
        pl.rank = cur_rank
        cur_rank += 1

    if request.user.is_authenticated:
        player = models.player.objects.get(user_id=request.user.pk)
        return render(request , 'leaderboard.html' , {'players':p,'player':player})
    return render(request, 'leaderboard.html', {'players': p})


# Rules View 
def rules(request):
    return render(request, 'index.html')


'''Leaderboard API'''
def leaderboard_api(request):
    p = models.player.objects.order_by('-score','timestamp')
    cur_rank = 1

    players_array = []

    for pl in p:
        pl.rank = cur_rank
        players_array.append({
            'name':pl.name,
            'rank':pl.rank,
            'email':'',
            'score':pl.score,
        })
        cur_rank += 1

    return JsonResponse(players_array,safe=False)

    
