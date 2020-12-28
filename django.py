def main(request):
        
    if request.method == "POST":
        audio_data = request.FILES.get('data')
        path = default_storage.save('123' + '.wav', ContentFile(audio_data.read()))
        return render(request, 'web-recorder.html')
    else:
        return render(request, 'web-recorder.html')
