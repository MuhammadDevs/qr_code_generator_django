from django.shortcuts import render
from django.http import HttpResponse
import qrcode
import io

def home(request):
    return render(request, 'index.html')

def generate_qr(request):
    if request.method == 'POST':
        url = request.POST['url']
        img = qrcode.make(url)
        buf = io.BytesIO()
        img.save(buf)
        buf.seek(0)
        return HttpResponse(buf.getvalue(), content_type='image/png')
