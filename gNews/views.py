from rest_framework.decorators import api_view
from django.http import HttpResponse

from django.core.cache import cache
from rest_framework.response import Response

import requests




@api_view(['POST'])
def search(request):
  query = request.data.get('query')
  lang = request.data.get('lang')
  country = request.data.get('country')
  page = request.data.get('page')
  sortby = request.data.get('sortby')
  max = request.data.get('max')
  max = str(max)

  if query:
    # If query is provided then proceed
    redisKey = 'news/searchs/'
    redisKey += query
    if lang:
      redisKey += '/'+lang
    if country:
      redisKey += '/'+country
    if page:
      redisKey += '/'+page
    if sortby:
      redisKey += '/'+sortby
    if max:
      redisKey += '/'+max
    data = cache.get(redisKey)
    # If data is cached then return it instead of making a request to the API
    if data: 
      return Response(data)
    else:
      # API request to gNews API to fetch articles based on query and other parameters
      apikey="a5fe2c522e585935f61686ec7ea95462" # gNews API key
      url = "https://gnews.io/api/v4/search?q="+ query 
      if lang:
        url += "&lang="+ lang
      if country:
        url += "&country="+ country
      if page:
        url += "&page="+ page
      if sortby:
        url += "&sortby="+ sortby
      if max:
        url += "&max="+ max
      url += "&apikey="+ apikey
      # Make a request to the API and get the response
      response = requests.request("GET", url)
      # Convert the response to JSON
      data = response.json()
      response = {
        "success": True,
        "message": "Successfully fetched articles",
        "totalArticles": data['totalArticles'],
        "articles": data['articles']
      }
      # Cache the response for 1 day (60*60*24*1) = 86400 seconds 
      cache.set(redisKey, response, 60*60*24*1) # Cached for 1 day
      return Response(response)
  else:
    # If query is not provided then return a 400 Bad Request response
    return HttpResponse(status=400, content="Bad Request")


@api_view(['POST'])
def headlines(request):
  category = request.data.get('category')
  lang = request.data.get('lang')
  country = request.data.get('country')
  sortby = request.data.get('sortby')
  page = request.data.get('page')
  max = request.data.get('max')
  max = str(max)

  redisKey = 'news/headlines/'
  if category:
    redisKey += category
  if lang:
    redisKey += '/'+lang
  if country:
    redisKey += '/'+country
  if sortby:
    redisKey += '/'+sortby
  if page:
    redisKey += '/'+page
  if max:
    redisKey += '/'+max
  print(redisKey)
  data = cache.get(redisKey)
  # If data is cached then return it instead of making a request to the API
  if data: 
    return Response(data)
  else:
    # API request to gNews API to fetch articles based on category and other parameters
    apikey="a5fe2c522e585935f61686ec7ea95462" # gNews API key
    url = "https://gnews.io/api/v4/top-headlines?apikey="+ apikey 
    if category:
      url += "&category="+ category
    if lang:
      url += "&lang="+ lang
    if country:
      url += "&country="+ country
    if sortby:
      url += "&sortby="+ sortby
    if page:
      url += "&page="+ page
    if max:
      url += "&max="+ max
    print(url)
    # Make a request to the API and get the response
    response = requests.request("GET", url)
    # Convert the response to JSON
    data = response.json()
    response = {
      "success": True,
      "message": "Successfully fetched articles",
      "totalArticles": data['totalArticles'],
      "articles": data['articles']
    }
    # Cache the response for 1 day (60*60*24*1) = 86400 seconds 
    cache.set(redisKey, response, 60*60*24*1) # Cached for 1 day
    return Response(response)
