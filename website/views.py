from django.shortcuts import render
from .backend import *
from .forms import InputForm

<<<<<<< HEAD
def post_list(request):
    return render(request, 'website/post_list.html', {})
	
def index(request):
	
=======

def post_list(request):
	return render(request, 'website/post_list.html', {})

>>>>>>> 2fc00f767cecb808a23904e47e76f3ebdab3771b

def index(request):
	# Genereerib tavalise formi HTML's.
	if request.method != "POST":
		form = InputForm()
		return render(request, "website/index.html", {'form': form})


	# Juhul kui form on saadetud, võta POST sees tekst ja lase läbi EstNLTK backendi.
	# df filtreerib tekstist välja arvud (300), nimed ja lausemärgid/sümbolid.
	# counted_lemmas kujul [['lemma', kogus], ['lemma', kogus], ['lemma', kogus], ['lemma', kogus]]
	# get_letter_sequence võtab sisse lemmade listi ja n-grami suuruse ja tagastab need kujul [['tähejäriendid', kogus], ['tähejäriendid', kogus]].
	else:

<<<<<<< HEAD
		text = request.POST.get("Tekst")
=======
		text = request.POST.get("text")
>>>>>>> 2fc00f767cecb808a23904e47e76f3ebdab3771b
		ngrams = int(request.POST.get('n_gram'))

		df = get_filtered_content(text)
		counted_lemmas = count_lemmas(df["lemmas"])
		letter_sequence = get_letter_sequence(df.lemmas, ngrams)
		adjacency_matrix, headers = get_adjandency_matrix(text, ngrams)

<<<<<<< HEAD

		form = InputForm()
		return render(request, "website/index.html", {'form': form, 'lemmas': counted_lemmas, 'letters':letter_sequence, 'matrix': adjacency_matrix, 'header': headers})
=======
		form = InputForm()
		return render(request, "website/index.html",
		              {'form': form, 'lemmas': counted_lemmas, 'letters': letter_sequence, 'matrix': adjacency_matrix,
		               'header': headers})
>>>>>>> 2fc00f767cecb808a23904e47e76f3ebdab3771b
