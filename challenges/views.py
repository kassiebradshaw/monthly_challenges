from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january" : "January - Eat no meat for the entire month",
    "february": "February - Walk for at least 20 minutes every day",
    "march": "March - Learn Django for at least 20 minutes every day",
    "april": "April - Eat no meat for the entire month",
    "may": "May - Walk for at least 20 minutes every day",
    "june": "June - Learn Django for at least 20 minutes every day",
    "july": "July - Eat no meat for the entire month",
    "august": "August -  for at least 20 minutes every day",
    "september": "September - Learn Django for at least 20 minutes every day",
    "october": "October - Eat no meat for the entire month",
    "november": "November - Walk for at least 20 minutes every day",
    "december": "December - Learn Django for at least 20 minutes every day",
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month -1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)