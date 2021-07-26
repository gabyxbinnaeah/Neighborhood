from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm ,ProfileForm,UpdateProfileForm ,BusinessForm,EventsForm,PostForm,NeighborhoodForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile,Neighborhood,UpcomingEvents,Business,Post
from django.shortcuts import get_object_or_404


# Create your views here.

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)



def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


def index(request):
	found_neighborhood=Neighborhood.neighborhood_list()
	return render(request, 'index.html',{"found_neighborhood":found_neighborhood})

def create_neighborhood(request):
    if request.method == 'POST':
        form =  NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            # hood.admin = request.user.profile
            hood.save()
            return redirect('index')
    else:
        form = NeighborhoodForm() 
    return render(request, 'newhood.html', {'form': form}) 

@login_required(login_url='login') 
def profile(request):
    '''
    methods that defines profile view
    '''
    current_user=request.user
    profile= Profile.objects.filter(user=current_user).first()
    # my_posts=Project.objects.filter(author=request.user)
    # "my_posts":my_posts
    
    return render(request,'profile.html',{"profile":profile,"current_user":current_user})


@login_required(login_url='login')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('profile')

    else:
        form = UpdateProfileForm()
        return render(request,'edit_profile.html',{"form":form})




def single_neighborhood(request, hood_id):
    singlehood= Neighborhood.objects.get(id=hood_id)
    business = Business.objects.filter(hood=singlehood)
    posts = Post.objects.filter(hood=singlehood)
    posts = posts[::-1] 
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            formdata = form.save(commit=False)
            formdata.hood = singlehood
            formdata.user = request.user 
            formdata.save()
            return redirect('singlehood', singlehood.id)
    else:
        form = BusinessForm() 
    params = {
        'singlehood': singlehood,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'singlehood.html', params) 



def create_post(request, hood_id):
    singlehood = Neighborhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.hood = singlehood
            post.user=request.user
            post.save()
            return redirect('singlehood', singlehood.id)

    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


def join_neighbourhood(request, id):
    neighbourhood = get_object_or_404(Neighborhood, id=id)
    request.user.neighbourhood = neighbourhood
	# request.user.profile.neighbourhood = neighbourhood
    request.user.save()
    return redirect('index')


def leave_neighbourhood(request, id):
    hood = get_object_or_404(Neighborhood, id=id)
    request.user.neighbourhood = None
    request.user.save()
    return redirect('index')