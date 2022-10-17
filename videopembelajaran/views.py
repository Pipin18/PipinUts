from django.shortcuts import render

# Create your views here.
def videopembelajaran(request):
    videopembelajaran = "Videopembelajaran"
    gambaranumum = "videopembelajaran"

    konteks = {
        'videopembelajaran': videopembelajaran,
        'gbrumum': gambaranumum,
    }
    return render(request, 'videopembelajaran.html', konteks)
