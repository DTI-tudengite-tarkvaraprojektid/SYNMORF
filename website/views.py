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
		df = get_filtered_content(request.POST.get("Tekst"))
		counted_lemmas = count_lemmas(df["lemmas"].tolist())
		letter_sequence = get_letter_sequence(list(df.lemmas), int(request.POST.get('n_gram')))
		form = InputForm()
		return render(request, "website/index.html", {'form': form, 'lemmas': counted_lemmas, 'letters':letter_sequence})