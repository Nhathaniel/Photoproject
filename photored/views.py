from django.shortcuts import render,redirect
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserProfileForm
import requests
from django.contrib.auth.decorators import login_required 
from .forms import PostForm
from .models import Post
from django.contrib import messages


# def index(request):
#     posts = Post.objects.all().order_by('-created_at')[:10]  # Retrieve latest 10 posts
#     return render(request, 'index.html', {'posts': posts})


from .models import VideoPost, GraphicsPost, thDPost, twDPost

def index(request):
    video_posts = VideoPost.objects.order_by('-post__created_at')[:10]
    graphics_posts = GraphicsPost.objects.order_by('-post__created_at')[:10]
    thD_posts = thDPost.objects.order_by('-post__created_at')[:10]
    twD_posts = twDPost.objects.order_by('-post__created_at')[:10]
    return render(request, 'index.html', {'video_posts': video_posts, 'graphics_posts': graphics_posts, 'thD_posts': thD_posts, 'twD_posts': twD_posts})



def profile(request):
    return render(request, 'profile.html')
def details(request):
    return render(request, 'photo-details.html')
def profile_details(request):
    return render(request, 'profile-details.html')
def edit_profile(request):
    return render(request, 'edit-profile.html')
def donate(request):
    return render(request, 'donate.html')
def donate_faq(request):
    return render(request, 'donate-faq.html')
def classroom(request):
    return render(request, 'classroom.html')
def jobs(request):
    return render(request, 'jobs.html')
def faqs(request):
    return render(request, 'faqs.html')
def customer_support(request):
    return render(request, 'customer_support.html')
def terms(request):
    return render(request, 'terms-of-service.html')
def ways_to_give(request):
    return render(request, 'ways-to-give.html')

@login_required
def update_profile(request):
    user_profile = request.user
    if requests:
        form = UserProfileForm(request.POST, instance=user_profile)
        form.save() 
        return redirect('update_profile')
    else:
       form = UserProfileForm(instance=user_profile)
       return(request, 'profile', {'form':form})

def logout_view(request):
    # Clear any user-specific data from the session
    request.session.pop('cart', None)  # Assuming 'cart' is the key storing cart items

    # Perform logout
    logout(request)

    # Redirect to the index page
    return redirect('/')

def login_view(request):
    if request.method == 'POST':
        # Your existing login form handling

        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if the user is authenticated
            if user.is_authenticated:
                # Transfer cart data from session to user's account
                if 'cart' in request.session:
                    # Assuming 'cart' is the key storing cart items
                    user.profile.cart = request.session['cart']
                    user.profile.save()

                # Perform login
                login(request, user)
                return redirect('index')

    # Handle unsuccessful login here
    return render(request, 'login.html', {'error': 'Invalid login credentials'})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately after registration
            return redirect('index')  # Redirect to the index page after successful registration
        else:
            print(form.errors)
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

# from django.shortcuts import render, redirect
# from .forms import ProfilePictureForm

# def update_profile_picture(request):
#     if request.method == 'POST':
#         form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = ProfilePictureForm(instance=request.user)
#     return render(request, 'update_profile_picture.html', {'form': form})


# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
from .models import Post, VideoPost, GraphicsPost, thDPost, twDPost

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False )
            category = form.cleaned_data['category']
            post.save()
            if category == 'Video':
                video_post = VideoPost.objects.create()
                post.category = category
                post.save()
                video_post.post = post
                video_post.save()
                messages.success(request, 'Post created successfully!')
            elif category == 'Graphics':
                graphics_post = GraphicsPost.objects.create(post_id=post.id)
                post.category = category
                post.save()
                graphics_post.post = post
                graphics_post.save()
                messages.success(request, 'Post created successfully!')
            elif category == 'thDPost':
                thD_post = thDPost.objects.create(post_id=post.id)
                post.category = category
                post.save()
                thD_post.post = post
                thD_post.save()
                messages.success(request, 'Post created successfully!')
            elif category == 'twDPost':
                twD_post = twDPost.objects.create(post_id=post.id)
                post.category = category
                post.save()
                twD_post.post = post
                twD_post.save()
                messages.success(request, 'Post created successfully!')
            # Add similar handling for other categories
            return redirect('index')  # Redirect to the index page
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
