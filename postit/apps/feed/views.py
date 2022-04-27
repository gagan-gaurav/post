from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import post
# Create your views here.

@login_required
def feed(request):
	userids = [request.user.id]
	
	for poster in request.user.postitprofile.follows.all():
		userids.append(poster.user.id)
	
	posts = post.objects.filter(created_by_id__in=userids)
	return render(request, 'feed/feed.html', {'posts': posts})