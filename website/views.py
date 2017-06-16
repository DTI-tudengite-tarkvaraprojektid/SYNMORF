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


#def post_list(request):
 #   return render(request, 'website/post_list.html', {})
	




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
		maatriks = request.POST.get("maatriks")
		df = make_dataframe(text)
		counted_lemmas = count_attribute(df, "lemmas")  # [['lemma', kogus], ['lemma', kogus]]
		letter_sequence = get_letter_sequence(df, ngrams)  # [['tähejäriend', kogus], ['tähejäriend', kogus]]
		adjacency_matrix, headers = get_adjandency_matrix(text, ngrams)  # Annab välja maatriksi ja maatriksi tulpade pealkirjad.

		form = InputForm()
		if maatriks == "Vaikimisi":
			return render(request, "website/index.html", {'form': form, 'lemmas': counted_lemmas, 'letters': letter_sequence, 'header': headers})
		else:
			return render(request, "website/index.html", {'form': form, 'lemmas': counted_lemmas, 'letters': letter_sequence, 'matrix': adjacency_matrix, 'header': headers})