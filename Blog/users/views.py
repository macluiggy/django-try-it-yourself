from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            # authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, new_user)
            return redirect('blogs:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)