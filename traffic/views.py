from django.db.models.expressions import Value
from django.db.models.lookups import Contains
from django.http import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
import requests
from requests.api import request
from .forms import SiteUrl

# Create your views here.


# def test_form(request):
#     if request.method == "POST":
#         mssg = 'site not found'
#         site = request.POST.get("site_url")
#         print({"site": site})
#         return render(
#                 request,
#                 "page_data.html",
#                 {
#                     "site": site,
#                     'error':mssg})

#     else:
#         return render(request,'index.html')


def test_form(request):
    if request.method == "POST":

        site = request.POST.get("site_url")
        print({"site": site})

        form = SiteUrl(request.POST)

        #     site = 'www.google.com'

        url = "https://similarweb2.p.rapidapi.com/pageoverview"

        querystring = {"website": "https://" + site}

        headers = {
            "x-rapidapi-host": "similarweb2.p.rapidapi.com",
            "x-rapidapi-key": "23a1830e2amshb300f3a2bac9a56p1793d1jsn2b8cb9b48d12",
        }
        # ##########This gets the data from the api
        response = requests.request("GET", url, headers=headers, params=querystring)
        # test_response = requests.request("GET",'https://' + site)

        if response.status_code == 200:
            print("works")
        else:
            mssg = 'Input a website with the format "www.example.com"'
            return render(request, "index.html",{'error':mssg})


        ####Convert the api response to json
        context = response.json()
        # from the json data, we get whatever data we need
        description = context["siteDescription"]
        rank = context["categoryRank"]["rank"]
        screenshot = context["pageScreenshot"]
        print(response.text)

        ######Here, we render the data to the html template
        return render(
            request,
            "page_data.html",
            {
                "site": site,
                # 'response':context,
                "" "rank": rank,
                "description": description,
                "screenshot": screenshot,
            },
        )
    
  

    else:
        mssg = 'Input a website with the format "www.example.com"'
        return render(request, "index.html",{'error':mssg})



###################REGEX

# if site Contains a schema, no need to add schema else add https:// to the url
# for example, app.netlify.test should work if the site is valid...
# if it diwsnt work we have an error page sha....To create new page or nah...think......

# import re
# regex = “((http|https)://)(.)?” + “[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]” + “{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)”
# website = re.search(r'((http|https)://)')
