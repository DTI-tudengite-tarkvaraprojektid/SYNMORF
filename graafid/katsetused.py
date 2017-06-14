#! /usr/bin/python3.5

from estnltk import Text
from pprint import pprint
from collections import Counter


# Matplotlib vajab t��tamiseks l�bi SSH matplotlib.use
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# Eemaldab sisestatud s�nadest arvud, lausem�rgid ja nimed.
# Tagastab DataFrame, ei eemaldata duplikaate.
def get_filtered_content(text):
	dataframe = Text(text).get(["word_texts", "", "postag_descriptions", "descriptions"]).as_dataframe
	filtered_dataframe = dataframe[(dataframe.postag_descriptions != "lausem�rk") & (dataframe.descriptions != "") & (dataframe.lemmas != "") & (dataframe.word_texts != "") & (dataframe.postag_descriptions != "") & (dataframe.postag_descriptions != "p�risnimi") & dataframe.word_texts.apply(lambda sona: sona.isalpha())]
	return filtered_dataframe


# Loendab �ra lemmade arve, tagastab kujul [("lemma", arv), ("lemma2", arv2), (... , ...)]
def count_lemmas(list_of_lemmas):
	c = Counter(list_of_lemmas)
	return c.most_common(10)

def count_sonad(list_of_word_tekst):
	s = Counter(list_of_word_tekst)
	return s.most_common(10)

# Tagastab laisalt postagide arvu kaks korda.
# Salvestab samasse kausta piechard'i posttagide arvude kohta.
# Tight layout hoolitseb selle eest, et sildid m��da ei l�heks.
# Sort j�riestab suuremast-v�iksemani, head v�tab v�lja viis esimest tulemust.
def make_postag_chart(dataframe):
	df1 = dataframe.groupby('postag_descriptions').size().reset_index(name='counts').sort_values("counts", ascending=False).head(5)
	plt.pie(df1["counts"], labels=df1["postag_descriptions"], shadow=False, startangle=90, autopct='%1.1f%%')
	plt.tight_layout()
	plt.savefig("postags.png")
	plt.clf()  # Turvlisuse jaoks "puhatada k�ik"
	
	
def count_word_form(dataframe):
	df1 = dataframe.groupby('descriptions').size().reset_index(name='counts').sort_values("counts", ascending=False).head(5)
	plt.pie(df1["counts"], labels=df1["descriptions"], shadow=False, startangle=90, autopct='%1.1f%%')
	plt.tight_layout()
	plt.savefig("word_forms.png")
	plt.clf()  # Turvlisuse jaoks "puhatada k�ik"


def get_letter_sequence(iterable, n_gram):
	temp = []
	for sona in iterable:
		for i in range(len(sona) - n_gram + 1):
			temp.append(sona[i:i + n_gram])
	return Counter(temp).most_common()


if __name__ == '__main__':
	df = get_filtered_content("Tere pimedus minu vana s�ber.")
	counted_lemmas = count_lemmas(df["lemmas"].tolist())
	make_postag_chart(df)
	count_word_form(df)
	pprint(get_letter_sequence(list(df.lemmas), 2))
