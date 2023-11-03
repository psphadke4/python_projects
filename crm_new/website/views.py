from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import create_user,AddRecordForm
from .models import Record


#@login_required
def home(request):
    records=Record.objects.all()

    if request.method == "POST" :
        username=request.POST['Username']
        password=request.POST['Password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You are logged In")
            return redirect('home')
        else:
            messages.error(request, "Please enter valid credentials.")
            return redirect('home')

    else:
        return render(request,template_name='website/home.html',context={'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You are logged Out")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form=create_user(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,f'{user} is Registered Successfull')
            return redirect('home')
    else:
        form=create_user
        return render(request,template_name='website/register.html',context={'form':form})
    return render(request, template_name='website/register.html', context={'form': form})


def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_records=Record.objects.get(id=pk)
        return render(request, template_name='website/record.html', context={'customer_records': customer_records})
    else:
        messages.warning(request,f"You must be logged in to view Page")
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Records Deleted")
        return redirect('home')
    else:
        messages.warning(request, "Please login before Deleting the record")
        return redirect('home')

def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request,f"Record Added Successfully")
                return redirect('home')

        return render(request, template_name='website/add_record.html', context={'form':form})
    else:
        messages.warning(request, f"Please login befor adding record")
        return redirect('home')

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been updated")
            return redirect('home')
        return render(request, template_name='website/update_record.html', context={'form': form})
    else:
        messages.warning(request, f"Please login befor adding record")
        return redirect('home')