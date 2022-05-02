from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import post
from django.contrib.auth.models import User
# Create your views here.

@login_required
def feed(request):
	userids = [request.user.id]
	
	for poster in request.user.postitprofile.follows.all():
		userids.append(poster.user.id)
	
	posts = post.objects.filter(created_by_id__in=userids)
	return render(request, 'feed/feed.html', {'posts': posts})


@login_required
def search(request):
	query = request.GET.get('query', '')

	if len(query) > 0:
		poster = User.objects.filter(username__icontains=query)
	else:
		poster = []

	context = {
		'query' : query,
		'poster' : poster
	}

	return render(request, 'feed/search.html', context)
	