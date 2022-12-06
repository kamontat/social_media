from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Post

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            return render(request, "signin.html")
    else:
        return render(request, "signin.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.save()

        return redirect(signin)
    else:
        return render(request, "signup.html")

def signout(request):
    logout(request)
    return redirect(signin)

def user_delete(request):
    userid = request.GET.get("userid")
    user = User.objects.get(id=userid) # => return: object
    user.delete()

    return redirect(home)

def home(request):
  if request.user.is_anonymous:
      return redirect(signin)

  # <MODEL>.objects.all() # get all data from database
  # <MODEL>.objects.filter(<PAREMS>) # get filtered data from database
  # <MODEL>.objects.get(<PARAMS>) # get single data from database
  # <MODEL>.objects.create(<PARAMS>) # create new model data to database
  # <VAR>.delete() # delete data from database

  # create post
  # Post.objects.create(
  #   title="hello world",
  #   description="helllllllllooooooo", 
  #   user=request.user,
  # )

  # # get post
  # Post.objects.all()
  # Post.objects.filter(user=request.user)
  # Post.objects.get(id="postid")

  # # delete post
  # post = Post.objects.get(id="postid")
  # post.delete()

  return render(request, "home.html", {
    "users": User.objects.all(),
  })
