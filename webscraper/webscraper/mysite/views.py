from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect

def scrape(request):
    
    if request.method == 'POST':
        site            = request.POST.get('url', '')
        url             = site if site.startswith('http://') or site.startswith('https://') else 'http://' + site
        print(url)
        try:
            page = requests.get(url, timeout=10)
        except Exception as e:
            links = Link.objects.all()
            return render(request, 'scrape.html', {'links': links, 'error': str(e)})
        # link_address    = []
        soup            = BeautifulSoup(page.content, 'html.parser')
        created = 0
        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            if link_address:
                Link.objects.create(url=link_address, name=link_text)
                created += 1

        links = Link.objects.all()
        return render(request, 'scrape.html', {'links': links, 'created': created})

    else:
        links = Link.objects.all()

    return render(request, 'scrape.html', {'links': links})

def clear(request):
    Link.objects.all().delete()
    return render(request, 'scrape.html')