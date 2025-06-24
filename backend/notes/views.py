from rest_framework import viewsets
from .models import Note, Version
from .serializers import NoteSerializer, VersionSerializer
from .forms import NoteForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer

class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer



@login_required
def home(request):
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(
            Q(user=request.user),
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by('-pinned', '-created_at')
    else:
        notes = Note.objects.filter(user=request.user).order_by('-pinned', '-created_at')

    return render(request, 'home.html', {'notes': notes})


@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    return render(request, 'delete_note.html', {'note': note})


@login_required
def toggle_pin(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.pinned = not note.pinned
    note.save()
    return redirect('home')