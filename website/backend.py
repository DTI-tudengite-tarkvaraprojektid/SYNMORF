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
def count_lemmas(dataframe):
	list_of_lemmas = dataframe.tolist()
	c = Counter(list_of_lemmas)
	return c.most_common(100)


# Tagastab laisalt postagide arvu kaks korda.
# Salvestab samasse kausta piechard'i posttagide arvude kohta.
# Tight layout hoolitseb selle eest, et sildid mõõda ei läheks.
# Sort järiestab suuremast-väiksemani, head võtab välja viis esimest tulemust.
def make_postag_chart(dataframe):
	df1 = dataframe.groupby('postag_descriptions').size().reset_index(name='counts').sort_values("counts", ascending=False).head(5)


# Annab piechart'i sõnavormidest.
# Salvestab tulemuse static kausta, kust Django saab staatilisi resursse kasutada.
def wordform_chart(dataframe):
	df1 = dataframe.groupby('descriptions').size().reset_index(name='counts').sort_values("counts", ascending=False).head(5)



# [[lemma], [lemma], [lemma]]
def find_ngrams(input_list, n):
	temp = []
	for word in input_list:
		temp.append([word[i:i + n] for i in range(len(word) - n + 1)])
	return temp


# Võtab sisse dataframe, muudab listiks, numbri selleks kui suur on tähejäriendid.
def get_letter_sequence(dataframe, n_gram):
	iterable = list(dataframe.unique())
	temp = []
	for sona in iterable:
		for i in range(len(sona) - n_gram + 1):
			temp.append(sona[i:i + n_gram])
	return Counter(temp).most_common(100)

	
# # argument on dataframe'i kujul
# def get_base_words(lemma):
# 	df = filtered_dataframe[filtered_dataframe.lemmas == lemma]
# 	df = list(df.word_texts)
# 	return anti_lemma


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
	flatten = flatten
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
	if checkbox=true
		return value_matrix, flatten
	else
		print("Maatriksit ei kuvata")
			
	

