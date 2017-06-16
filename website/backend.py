from estnltk import Text
from pprint import pprint
from collections import Counter
import pandas as pd


# Eemaldab sisestatud sõnadest arvud, lausemärgid ja nimed.
# Tagastab DataFrame, ei eemaldata duplikaate.
def get_filtered_content(text):
	dataframe = Text(text).get(["word_texts", "lemmas", "postag_descriptions", "descriptions"]).as_dataframe
	filtered_dataframe = dataframe[
		(dataframe.postag_descriptions != "lausemärk") & (dataframe.descriptions != "") & (dataframe.lemmas != "") & (
			dataframe.word_texts != "") & (dataframe.postag_descriptions != "") & (
			dataframe.postag_descriptions != "pärisnimi") & dataframe.word_texts.apply(lambda sona: sona.isalpha())]
	return filtered_dataframe


# Loendab ära lemmade arve, tagastab kujul [("lemma", arv), ("lemma2", arv2), (... , ...)]
def count_attribute(dataframe, attribute):
	dataframe = dataframe[attribute]
	list_of_attributes = dataframe.tolist()
	c = Counter(list_of_attributes)
	return c.most_common()

def count_basewords(dataframe):
	dataframe = dataframe[dataframe["word_texts","lemmas"]]
	list_of_attributes = list(dataframe)
	c = Counter(list_of_attributes)
	return c.most_common()	


# [[lemma], [lemma], [lemma]]
def find_ngrams(input_list, n):
	temp = []
	for word in input_list:
		temp.append([word[i:i + n] for i in range(len(word) - n + 1)])
	return temp


# Võtab sisse dataframe, muudab listiks, numbri selleks kui suur on tähejäriendid.
def get_letter_sequence(dataframe, n_gram):
	iterable = list(dataframe)
	temp = []
	for sona in iterable:
		for i in range(len(sona) - n_gram + 1):
			temp.append(sona[i:i + n_gram])
	return Counter(temp).most_common()



def get_adjandency_matrix(text, ngramms):
	# Filtreerib välja arvud, lausemärgid ja nimed ja tagastab unikaalsed lemmad. [[lemma], [lemma], [lemma]]
	lemma_list = list(get_filtered_content(text).lemmas.unique())

	# Muudab sõnad nende vastavate n-grammiks.
	# meie maa elu -> mina maa elu -> [['mi', 'in', 'na'], ['ma', 'aa'], ['el', 'lu']]
	# Sõnad on eraldi listides, kuna muidu loetakse ühe sõna lõppu ja teise sõna algust kui külgnevaks tulevas maatriksis.
	ngram_lemmas = find_ngrams(lemma_list, ngramms)

	pure_ngram = [item for sublist in ngram_lemmas for item in sublist]
	c = Counter(pure_ngram).most_common()

	# Võtab kokku kõik tähejäriendid ühte listi, muudab set's et eraldada duplikaadid ning listiks jälle tagasi.
	flatten = [count[0] for count in c]
	flat_len = len(flatten)

	# Loob kahedimensionaalse massiivi kuhu andmeid panna.
	two_dimensional_array = [[0 for i in range(flat_len)] for j in range(flat_len)]

	for word in ngram_lemmas:

		# Võtab järiestikku kaks üksteisele järgnevat tähejäriendi n-grammi ning leiab nende indeksid unikaalsete tähejäriendite massiivist.
		for i in range(len(word) - 1):
			index_x = flatten.index(word[i])


			# N-grammi külgnevuse eemaldamiseks võtta välja rida 82.
			# If lause on selleks, et mitte lugeda ainult n-grammi külgnevusi kuid ka reaalsete tähte külgnevusi mingis sõnas.
			# If lause ise on selleks et list indeksist välja ei läheks, hüppab pidevalt üle ühe.
	
			if i < len(word) - ngramms: two_dimensional_array[index_x][flatten.index(word[i + ngramms])] += 1

	# Muutab andmed loetavaks kuujuks.
	value_matrix = pd.DataFrame(two_dimensional_array, index=flatten, columns=flatten).values.tolist()

	return value_matrix, flatten

