from django.shortcuts import render

# Create your views here.
import qrcode
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.core.files.base import ContentFile


def generate_qr(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        img = qrcode.make(data)


        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)

        response = HttpResponse(buffer, content_type="image/png")
        response['Content-Disposition'] = 'attachment; filename=qr_code.png'
        return response

    return render(request, 'qr_form.html')
