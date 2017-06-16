from django.shortcuts import render
from .backend import *
from .forms import InputForm


#def some_view(request):
    #do some stuff
  #  request.session['_old_post'] = request.POST
 #   return HttpResponseRedirect('next_view')

#def next_view(request):
 #   old_post = request.session.get('_old_post')
    #do some stuff using old_post


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


		text = request.POST.get("text")
		ngrams = int(request.POST.get('n_gram'))

		df = get_filtered_content(text)
		counted_lemmas = count_attribute(df,"lemmas")
		counted_basewords = count_basewords(df)

		letter_sequence = get_letter_sequence(df.lemmas, ngrams)
		adjacency_matrix, headers = get_adjandency_matrix(text, ngrams)


		form = InputForm()
		return render(request, "website/index.html", {'form': form, "basewords": counted_basewords,  'lemmas': counted_lemmas, 'letters':letter_sequence, 'matrix': adjacency_matrix, 'header': headers})
