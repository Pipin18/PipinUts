from django.shortcuts import render

# Create your views here.
def latihan(request):
    latihan = "Latihan"
    gambaranumum = "latihan quiziz"

    konteks = {
        'latihan': latihan,
        'gbrumum': gambaranumum,
    }
    return render(request, 'latihan.html', konteks)
