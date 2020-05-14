from django.shortcuts import render

from cowsmoo.models import CowsMooText
from cowsmoo.forms import MooText
import subprocess


def index(request):
    if request.method == 'POST':
        form = MooText(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form = MooText()
            cowsmoo_text = subprocess.run(
                ['cowsay', data['text']], capture_output=True
            ).stdout.decode()
            CowsMooText.objects.create(
                text=data['text']
            )

        return render(request, 'index.html',
        {'cowsmoo_text': cowsmoo_text, 'form': form })
    form = MooText()
    return render(request, 'index.html', {'form': form})


def history_view(request):
    text_history = list(CowsMooText.objects.all())
    recent_history = text_history[-10:][::-1]


    return render(request, 'history.html', {'recent_history': recent_history})

    

