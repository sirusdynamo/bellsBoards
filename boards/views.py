from django.shortcuts import render ,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Board ,User ,Topic, Post
from .forms import NewTopicForm

# Create your views here.
def home(request):
    boards =Board.objects.all()
    return render(request, 'home.html',{'boards':boards})


def board_topics(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'topics.html', {'board':board})

def new_topics(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            Post.objects.create(
                message = form.cleaned_data.get('message'),
                topic = topic,
                created_by = user
            )
            
            return redirect('board_topics', board_id=board.id )

    else:
        form = NewTopicForm()
    return render(request, 'new_topics.html', {'board':board, 'form': form})