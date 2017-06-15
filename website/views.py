from django.shortcuts import render
from .backend import *
from .forms import InputForm


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
		form = InputForm()

		df = get_filtered_content(request.POST.get("Tekst"))
		lists_of_words = list_of_words(df["word_texts"].tolist())
		#letter_sequence = get_letter_sequence(list(df.word_tekst), int(request.POST.get('n_gram')))
		text = massiiv()
		


		form = InputForm()
		return render(request, "website/index.html", {'form': form, 'word_texts': lists_of_words, 'massiiv': text}) #'letters':letter_sequence})
		


		
		
