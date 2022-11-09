from django.shortcuts import render,redirect
from .forms import ReviewForm
from django.urls import reverse
# Create your views here.
def rental_review(request):
    #POST request
    if request.method == "POST":
        form = ReviewForm(request.POST)
        i=0;
        form = form.cleaned_data; 
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









    