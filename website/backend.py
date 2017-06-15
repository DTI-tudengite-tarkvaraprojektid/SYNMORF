from estnltk import Text
from pprint import pprint
from collections import Counter


# Eemaldab sisestatud sõnadest arvud, lausemärgid ja nimed.
# Tagastab DataFrame, ei eemaldata duplikaate.
def get_filtered_content(text):
	dataframe = Text(text).get(["word_texts", "lemmas", "postag_descriptions", "descriptions"]).as_dataframe
	filtered_dataframe = dataframe[(dataframe.postag_descriptions != "lausemärk") & (dataframe.descriptions != "") & (dataframe.lemmas != "") & (dataframe.word_texts != "") & (dataframe.postag_descriptions != "") & (dataframe.postag_descriptions != "pärisnimi") & dataframe.word_texts.apply(lambda sona: sona.isalpha())]
	return filtered_dataframe

# Tagastab laisalt postagide arvu kaks korda.
# Salvestab samasse kausta piechard'i posttagide arvude kohta.
# Tight layout hoolitseb selle eest, et sildid mõõda ei läheks.
# Sort järiestab suuremast-väiksemani, head võtab välja viis esimest tulemust.
def make_postag_chart(dataframe):
	df1 = dataframe.groupby('postag_descriptions').size().reset_index(name='counts').sort_values("counts", ascending=False).head(5)

# dataframe sõnade  list loomine
def word_counter(dataframe):
	list_of_words = dataframe["word_texts"].tolist()
	

# Annab piechart'i sõnavormidest.
# Salvestab tulemuse static kausta, kust Django saab staatilisi resursse kasutada.
def wordform_chart(dataframe):
	df1 = dataframe.groupby('descriptions').size().reset_index(name='counts').sort_values("counts", ascending=False).head(5)
	
# Loendab ära tekstis olevad sonad arvudena, tagastab kujul [("sona", arv), ("sona", arv2), (... , ...)]
def list_of_words(list_of_words):
	c = Counter(list_of_words)
	return c.most_common(100)
 
	
# võtab sisse listi, numbrid 	
def get_word_sequence(iterable, word_texts):
	temp=[]
	for pikkus in iterable:		
		for i in range(len(pikkus)):
			temp.append(pikkus[i:i])
	return Counter(temp).most_common(100)




def sona_listid(dataframe):
    # Saab kätte unikaalsete loetelu listina.
    # ['ühendkuningriik','toimuma','mandaat','erakorraline','parlamendivalimine','kuulutama', ...]
    pikkus = list(dataframe.word_texts)



def massiiv():
	fail = open('/home/mart/Suvepraktika 2017/Martin/Suvepraktika-2017/website/file.txt', "r")
	text = fail.read().split(' ')
	return text
	


#def pikkus(dataframe):
	#return len(pikkus)	
#def proov(dataframe):
#	proov = [203,156,99,251,305,247,111]	