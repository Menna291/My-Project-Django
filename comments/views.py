from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment




def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_comments')  # Redirect to the appropriate view after comment submission
    else:
        form = CommentForm()
    return render(request, 'comments/comment_form.html', {'form': form})

from .models import Comment

def show_comments(request):
    comments = Comment.objects.order_by('-created_at')
    return render(request, 'comments/comments.html', {'comments': comments})
