import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import post
from .models import Like

@login_required
def api_add_post(request):
	data = json.loads(request.body)
	body = data['body']
	post_data = post.objects.create(body = body, created_by = request.user)
	return JsonResponse({'success' : True, 'post_id': post_data.id})


@login_required
def api_add_like(request):
	data = json.loads(request.body)
	post_id = data['post_id']

	if not Like.objects.filter(post_id = post_id).filter(created_by = request.user).exists():
		like = Like.objects.create(post_id = post_id, created_by = request.user)
	
	return JsonResponse({'success' : True})