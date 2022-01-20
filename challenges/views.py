from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

#------------------------------------------------------------------

# View that displays the challenges landing page, listing each month as a link to it's challenge
def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # try:
    #     return HttpResponse(response_data)
    # except:
    #     return HttpResponseNotFound("That didn't seem to work...")
#------------------------------------------------------------------

# View that takes an int as a parameter and redirects to the appropriate month
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

#------------------------------------------------------------------

# View for the individual monthly challenges
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month,
        })
    except:
        return HttpResponseNotFound("<h1>It doesn't look like that worked...")

#------------------------------------------------------------------