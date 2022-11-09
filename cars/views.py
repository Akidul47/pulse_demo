from ast import increment_lineno
from re import I
from typing import Counter
from django.shortcuts import render,redirect
from .forms import ReviewForm
from django.urls import reverse
# Create your views here.
def rental_update(request):
    #POST request
    if request.method == "POST":
        with open('cars/counter.txt', 'r') as c: ##reading counter number
            n = c.read()
        c = int(n)+1 ##updating counter
        form = ReviewForm(request.POST) 
        if form.is_valid():
            print(form.cleaned_data)
            filename = "form%s.txt" %c ##adjusting the name
            with open(filename, 'w') as f:
                f.write(str(form.cleaned_data)) 
            
            ##updating counter
            with open('cars/counter.txt', 'w') as f:
                f.write(str(c))
            return redirect(reverse('cars:thank_you'))


    else:
        form = ReviewForm()

    return render(request, 'cars/rental_review.html', context={'form':form})

def rental_review(request):
    #POST request
    if request.method == "POST":
        form = ReviewForm(request.POST) 
        if form.is_valid():
            print(form.cleaned_data)
            with open('form.txt', 'a') as f:
                f.write(str(form.cleaned_data)) 
            return redirect(reverse('cars:thank_you'))
    else:
        form = ReviewForm()

    return render(request, 'cars/rental_review.html', context={'form':form})

def thank_you(request):
    return render(request, 'cars/thank_you.html')









    