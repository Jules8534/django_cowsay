from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from cowsmoo.models import CowsMooText

from cowsmoo.forms import MooText
import subprocess


def index(request):
    output = None
    if request.method == 'POST':
        form = MooText(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowsMooText.objects.create( 
                text=data['text']
            )
            cmd = data['text']
            output = subprocess.run(['cowsay', cmd], capture_output=True)
            return render(request, 'index.html', {'form': MooText(),'output': output.stdout.decode()})
    form = MooText()
    return render(request, 'index.html', {'form': form})


def history(request):
    text_history = CowsMooText.objects.all().order_by('-id')[:10]
    # recent_history = text_history[-10:][::-1]
    return render(request, 'history.html', {'text_history': text_history})

    

