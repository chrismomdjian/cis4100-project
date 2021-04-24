from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .helper_functions import api_call
from datetime import datetime
import json

def index(request):
	return render(request, 'home.html', {})


def results(request):
	all_games = []
	if request.method == 'POST':
		search_title = request.POST.get('search_title')
		games_query = api_call('games', 
			'fields id,age_ratings,aggregated_rating,category,cover,first_release_date,' + 
			'genres,involved_companies,keywords,multiplayer_modes,name,parent_game,platforms,' +
			'rating,rating_count,release_dates,remakes,remasters,screenshots,similar_games,status,' +
			'storyline,summary,tags,url;' +
			'search "' + search_title + '";')

		for game in games_query:
			screenshot_urls = []
			screenshot_ids = []

			try:
				summary = game['summary']
			except KeyError:
				summary = 'N/A'

			try:
				storyline = game['storyline']
			except:
				storyline = 'N/A'

			try:
				release_date = datetime.utcfromtimestamp( game['first_release_date'] ).strftime('%m-%d-%Y')
			except:
				release_date = 'N/A'

			cover_query = api_call('covers',
				'fields alpha_channel,animated,checksum,game,height,image_id,url,width;' +
				'where game=' + str(game['id']) + ';')

			all_games.append({
				'id': game['id'],
				'title': game['name'],
				'release_date': release_date,
				'cover': 'https:' + cover_query[0]['url'],
				'summary': summary,
				'storyline': storyline,
			})

	return render(request, 'results.html', {'all_games': all_games})