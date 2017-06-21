# SYNMORF
Loodud Tallinna Ülikooli digitehnoloogiate instituudi suvepraktika raames TLU eesti vahekeele korpuse palvel, et lihtsustada lingvistilise analüüsi hõlbsustamiseks, pakkudes graafilist tagasisidet tekstile tehtud morfoloogilisest analüüsist. Projekti raames kasutatakse eesti keelele konfigureeritud ning eestlaste poole väljaaretatud lingvistika teeki EstNLTK.

Kujundus põhineb Django Girls Tutoriali kujunduse põhjal.

## Arenduses osalenud isikud:
* Marko Kollo
* Mart Ambur Jr
* Ingo Mägi
* Jaagup Kippar
* Kais Allkivi
* Pille Eslon 
* Joosep Hint
* Martin Kasak

## Kasutatav tarkvara
* Python v3.5
* Django v1.1.11
* EstNLTK v1.4.1
* pandas v0.20.0 (Pythoni teek)
* numpy  v1.13.0 (Pythoni teek)
* django-multiselectfield v0.1.7 (Pythoni teek)

## Installeerimisjuhend
1. Soovitatav on kasutada Anaconda andmeteaduse raamistiku mis lubab hallata tarkvara moodulisiseseid nõuded ka Pythoni väliste teekidega + virtuaalkeskkondade loomist, selleks minna [lehele](https://www.continuum.io/downloads) ning installige oma opsüsteemile vastav Anaconda versioon. Seda sammu saab ka alternatiivselt vahele jätta.
1. Looge uus conda keskkond Python 3.5-ga, selleks käsurealt käsk 
'''conda create --name estnltk_env python=3.5'''
1. Aktiveerige loodud keskkond: käsurealt käsk. 
    * Windowsis: '''activate estnltk_env'''
    * Macis, Linuxis: '''source activate estnltk_env'''
1. Installige estnltk käsuga 
'''conda install -c estnltk -c conda-forge estnltk'''
1. Installige [django-multiselectfield](https://pypi.python.org/pypi/django-multiselectfield) eelnevalt loodud virtuaalkeskkonna endale sobival meetodil,
soovitatavalt käsuga '''pip install django-multiselectfield'''
1. Git clone seda reprot, kasutades projekti interpretaatoriks loodud virtuaalkeskkonna sees olevat Pythonit.
1. Liikuge projektis kausta kus asub manage.py ning käivitage veebiserver käsuga '''manage.py runserver'''.
1. Veebileht peaks olema kättesaadav läbi localhost:8000. Käivitades läbi serveri teha tunnel serverisse ning kasutada käsku 
''' manage.py runserver 0.0.0.0:pordinumber''', peale mida on server kättesaadav läbi localhost:localport.


## Kasutusjuhend
* Teksi, mida analüüsitakse saab sisestada kahte moode, kas pannakse seda käsitsi copy paste abil või laetakse .txt failist läbi
nupu "Choose File" sektsioonist "Teksti lisamine failist". Viimase puhul on võimalik üleslaadida ainult ANSI encodinguga faile (Mis on vaikimise encoding iga salvestamise puhul)
Eduka laadimise puhul tekib paari sekundi pärast "Text" lahtri sisse selle faili sisu. 
* Sisestage n-grammide suurus talle vastavas lahtris, selle abil pannakse paika tähejäriendite pikkus nii tähejäriendite
sagedustabelis kui ka külgnevusmaatriksi sees. Sõna "kuningriik" 2-gram oleks 'ku', 'un', 'ni', 'in', 'ng', 'gr', 'ri', 'ii', 'ik'
TÄHELEPANU! Külgnevusmaatriksi loomise puhul ei tasu n-grammide pikkust panna suuremaks kui 3 kuna selle väljanäitamine võib viia internetilehitsja töö peatuseni.
* Lahtris maatriks saab valida kas soovitakse näidatada sõnade tähejäriendite külgnevusmaatriksid või mitte. Kuna antud tabel on väga resursinõudlik, on ta vaikimise seadistatud
mitte-näitamise peale.
* Vajutage nuppu ja oodake tulemuse laadimiseni.
* Lehe laadimisel ilnevad alati kolm tabelid, ühes on olemas kõik võimalikud tähejäriendid sisestatud teksti sees ja nende sagedus,
teises on enimesinevad lemmad ja nende sagedus ning kolmandas teksti sees olevad sõnad, nende lemmad ja sõnade sagedus.
* Seoste leidmiseks on rakendatud interaktiivsed tabelid, nimelt tähejäriendi rea peale vajutades hiirega näitab lemma tabelis välja
kõik teksi sees olevad lemmad, mille sees on antud tähejäriend ning lemmade peale vajutades ilmud kolmandasse tabelisse,
millisel kujul on need lemmad tekstid põhivormina. Iga hiirevajutuse tulemusena muutub lahter roosaks, et pidada järge läbikäidud lahtritest.
* Igal tabelil on võimalik otsida rea sees olevaid tulemusi, nagu näiteks täejäriendeid, lemmasi, või siis sageduste kogust.
Ülevalt nuppudest on saab valida mitu kirjet näidatakse välja ning soovi korral nupuvajutsega salvestada tabeli sisu csv, excel või pdf formaadis. 
Võimaldab ka alustada tabeli sisu printimist nupuvajutsega.
Samuti on võimalik sorteerida tulemusi vajutades vastava tulba pealkirja peale.
* Külgnevusmaatriks näitab kogu statistakt selle üle, kui palju mingeid tähejäriendeid esineb sõnade sees kogus tekstis.
Horisontaalselt tähejäriendid on alati eespool ning vertikaalsed on need mis järgnevad sõna sees.
Pannes otsingu sisse tähejäriendi annab see kätte rea kus antudd tähejäriend on eespool. Pannes sisse arvu
näitab tabel välja kõik read, kus see esineb.


## Litsents
Antud tarkvara kasutab MIT (Massachusetts Institute of Technology) litsentsi, ehk seda saab kasutda ärieesmärkidel, seda
saab muuta, jagada ning kasutada ilma piiranguta. Autorid ei vastuda kahjude eest ning tarkvara jagamisel
peab see hoidma sama litsensi ja autoriõigusi.


## Pildid
![Teksti lisamine töötluseks](http://www.tlu.ee/~mkollo/SYNMORF/mpWKnDgRRKu65lZxXmX0eQ.png)
![Tabeli kujul informatsioon](http://www.tlu.ee/~mkollo/SYNMORF/MIlbH9F2Su6MkNGrbtxQeg.png)
![Tähejäriendite külgnevusmaatriks](http://www.tlu.ee/~mkollo/SYNMORF/r02EcTT8TSGXUwQxGANTFQ.png)
