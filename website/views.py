from django.shortcuts import render
from .backend import *
from .forms import InputForm


def post_list(request):
    return render(request, 'website/post_list.html', {})



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
		form = InputForm()

		df = get_filtered_content(request.POST.get("Tekst"))
		lists_of_words = list_of_words(df["word_texts"].tolist())
		#letter_sequence = get_letter_sequence(list(df.word_tekst), int(request.POST.get('n_gram')))
		text = massiiv()
		


		form = InputForm()
		return render(request, "website/index.html", {'form': form, 'word_texts': lists_of_words, 'massiiv': text}) #'letters':letter_sequence})
		


		
		
=======

		text = request.POST.get("text")
		ngrams = int(request.POST.get('n_gram'))

		df = get_filtered_content(text)
		counted_lemmas = count_lemmas(df["lemmas"])
		letter_sequence = get_letter_sequence(df.lemmas, ngrams)
		adjacency_matrix, headers = get_adjandency_matrix(text, ngrams)


		form = InputForm()
		return render(request, "website/index.html", {'form': form, 'lemmas': counted_lemmas, 'letters':letter_sequence, 'matrix': adjacency_matrix, 'header': headers})
>>>>>>> 59e624cf8807579d493f5d10cdda9a93964c97c3
