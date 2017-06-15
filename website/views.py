from django.shortcuts import render
from .backend import *
from .forms import InputForm
import json

def post_list(request):
	return render(request, 'website/post_list.html', {})


def index(request):
	# Genereerib tavalise formi HTML's kui formi ei ole saadetud.
	if request.method != "POST":
		form = InputForm()
		return render(request, "website/index.html", {'form': form})


	# Juhul kui form on saadetud, võta POST sees tekst ja lase läbi EstNLTK backendi.
	# df filtreerib tekstist välja arvud (300), nimed ja lausemärgid/sümbolid.
	else:
		text = request.POST.get("text")
		ngrams = int(request.POST.get('n_gram'))

		df = make_dataframe(text)
		counted_lemmas = count_attribute(df, "lemmas")  # [['lemma', kogus], ['lemma', kogus]]
		letter_sequence = get_letter_sequence(df, ngrams)  # [['tähejäriend', kogus], ['tähejäriend', kogus]]
		adjacency_matrix, headers = get_adjandency_matrix(text, ngrams)  # Annab välja maatriksi ja maatriksi tulpade pealkirjad.

		form = InputForm()
		return render(request, "website/index.html", {'form': form, 'lemmas': counted_lemmas, 'letters': letter_sequence, 'matrix': adjacency_matrix, 'header': headers})
