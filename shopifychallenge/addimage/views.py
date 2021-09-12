from .forms import DocumentForm
from django.shortcuts import render, redirect

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()
    return render(request, 'model_form_updated.html', {
        'form': form
    })