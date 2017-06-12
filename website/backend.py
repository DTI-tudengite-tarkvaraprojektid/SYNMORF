from estnltk import Text
from pprint import pprint
from collections import Counter


# Eemaldab sisestatud sõnadest arvud, lausemärgid ja nimed.
# Tagastab DataFrame, ei eemaldata duplikaate.
def get_filtered_content(text):
	dataframe = Text(text).get(["word_texts", "lemmas", "postag_descriptions", "descriptions"]).as_dataframe
	filtered_dataframe = dataframe[(dataframe.postag_descriptions != "lausemärk") & (dataframe.descriptions != "") & (dataframe.lemmas != "") & (dataframe.word_texts != "") & (dataframe.postag_descriptions != "") & (dataframe.postag_descriptions != "pärisnimi") & dataframe.word_texts.apply(lambda sona: sona.isalpha())]
	return filtered_dataframe


# Loendab ära lemmade arve, tagastab kujul [("lemma", arv), ("lemma2", arv2), (... , ...)]
def count_lemmas(list_of_lemmas):
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


# Võtab sisse listi, numbri selleks kui suur on tähejäriendid.
def get_letter_sequence(iterable, n_gram):
	temp = []
	for sona in iterable:
		for i in range(len(sona) - n_gram + 1):
			temp.append(sona[i:i + n_gram])
	return Counter(temp).most_common(100)

def get_base_words(lemma):
	df = filtered_dataframe[filtered_dataframe.lemmas == lemma]
	df = list(df.word_texts)
	return anti_lemma
