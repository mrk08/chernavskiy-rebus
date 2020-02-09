from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AnswerForm
from .models import Rebus
from .utils import preprocess_text


def new_rebus(request):
    rebus = Rebus.objects.order_by("?").first()
    return render(request, "polls/rebus.html", {
        "rebus": rebus,
    })


def solve(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            rebus = Rebus.objects.get(pk=form.cleaned_data['rebus_id'])
            answers = set(preprocess_text(" ".join([
                form.cleaned_data['word1'],
                form.cleaned_data['word2'],
                form.cleaned_data['word3']])))
            expected = set(preprocess_text(rebus.title))
            counter = len([answer for answer in answers if answer in expected])
            return render(request, "polls/result.html", {
                "rebus": rebus,
                "counter": counter,
                "expected": len(expected)
            })
    return HttpResponseRedirect("/")

