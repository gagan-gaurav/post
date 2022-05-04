from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import postitprofileform

def postitprofile(request, username):
	user = get_object_or_404(User, username=username)

	psts= user.posts.all()
	for p in psts:
		likes = p.likes.filter(created_by_id = request.user.id)

		if likes.count() > 0:
			p.liked = True
		else:
			p.liked = False

	context = {
		'user' : user,
		'posts' : psts
	}

	return render(request, 'postitprofile/postitprofile.html', context)

@login_required
def follow_poster(request, username):
	user = get_object_or_404(User, username=username)
	request.user.postitprofile.follows.add(user.postitprofile)

	return redirect('postitprofile', username=username)

@login_required
def unfollow_poster(request, username):
	user = get_object_or_404(User, username=username)
	request.user.postitprofile.follows.remove(user.postitprofile)

	return redirect('postitprofile', username=username)

def followers(request, username):
	user = get_object_or_404(User, username=username)
	return render(request, 'postitprofile/followers.html', {'user' : user })

def follows(request, username):
	user = get_object_or_404(User, username=username)
	return render(request, 'postitprofile/follows.html', {'user' : user })

@login_required
def edit_profile(request):
	if request.method == 'POST':
		form = postitprofileform(request.POST, request.FILES, instance = request.user.postitprofile)

		if form.is_valid():
			form.save()
			return redirect('postitprofile', username = request.user.username)
	else:
		form = postitprofileform(instance = request.user.postitprofile)
	
	context = {
		'user' : request.user,
		'form' : form
	}

	return render(request, 'postitprofile/edit_profile.html', context)
