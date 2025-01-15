# Introduction to Python/ro
## Introduction


<div class="mw-translate-fuzzy">

Acesta este un scurt tutorial pentru cei nou veniți în Python. [Python](http://en.wikipedia.org/wiki/Python_%28programming_language%29) is an open-source, multiplatform [programming language](http://en.wikipedia.org/wiki/Programming_language). Python are mai multe caracteristici care o fac foarte diferită de alte limbaje și este foarte accesibil utilizatorilor noi ca tine:


</div>


<div class="mw-translate-fuzzy">

-   A fost special conceput pentru a fi ușor de citit de ființe umane, și de aceea este foarte ușor de învățat și de înțeles.
-   Este un limbaj interpretat, este faptul că, spre deosebire de limbajele compilate cum ar fi C, programul nu trebuie să fie compilate înainte de a fi executat. Codul pe care îl scrieți, dacă doriți. Pentru că puteți merge încet, pas cu pas, este extrem de ușor de a învăța și de a găsi erori în cod.
-   Poate fi încorporat în alte programe pentru a fi folosit ca limbaj de scripting. FreeCAD are un interpretor Python încorporat; puteți scrie cod Python în freecad, Aceasta va Manipulează părți ale freecad, de exemplu, pentru a crea geometrie. Acest lucru este extrem de puternic, în loc de doar clic pe butonul închidere a Etichetat „creați sferă" pe care unii ARE program de coduri; tu ai libertatea de a construi cu ușurință propriul instrument, care crează exact geometria dorită, într-o formă de și manieră pe care programatorul nu o putea prevedea.
-   Este extensibil, vă puteți conecta cu ușurință la funcționalitatea dvs. De exemplu,sunt modulele care permit Python-ului să citească și să scrie imagini jpg pentru a comunica cu Twitter, pentru a programa sarcinile care trebuie efectuate de sistemul de operare, etc.


</div>


<div class="mw-translate-fuzzy">

Vă recomandăm cu tărie să introduceți fragmentele de cod de mai jos într-un interpret Python. Pentru multe dintre exemplele noastre, punctul important este linia după execuția codului, rezultatul. Și acum la muncă! Rețineți că următoarea este o introducere simplificată și, în nici un caz, un tutorial complet. Dar sperăm că după această lectură ați dobândit bazele necesare pentru a cunoaște și exploata mai profund mecanismele FreeCad.


</div>



## Interpretorul


<div class="mw-translate-fuzzy">

De obicei, când scrieți programe de calculator, deschideți pur și simplu un editor de text sau mediul de programare special (care este, de obicei, un editor de text cu mai multe instrumente suplimentare), scrieți programul, apoi compilați și executați. În mod obișnuit, au fost făcute una sau mai multe erori la intrare, astfel încât programul dvs. nu va funcționa. S-ar putea să primiți chiar și un mesaj de eroare care să vă spună ce sa întâmplat. Apoi, reveniți la editorul de text, corectați greșelile, executați din nou, repetând până când programul dvs. funcționează așa cum doriți.


</div>


<div class="mw-translate-fuzzy">

Întregul proces, în Python, poate fi făcut transparent în interiorul interpretrului Python. Interpretorul este o fereastră Python cu un prompt de comandă, unde puteți introduce pur și simplu codul Python. Dacă instalați Python pe computerul dvs. (descărcați-l din [Python website](http://www.python.org) dacă sunteți pe Windows sau Mac, instalați-l din depozitul de pachete dacă sunteți pe GNU / Linux), veți avea un interpretor Python în meniul de pornire. Însă FreeCAD are și un interpretor Python în fereastra inferioară:


</div>

![](images/FreeCAD_Python_console.png )


<div class="mw-translate-fuzzy">

![](images/Screenshot_pythoninterpreter.jpg )


</div>


<div class="mw-translate-fuzzy">

(Dacă nu o aveți, click pe View \--\> Panels \--\> Python console.)


</div>


<div class="mw-translate-fuzzy">

Interpretorul arată versiune Python, apoi un simbol \>\>\> , care este promptul comenzii, chiar așa, unde introduceți codul Python. Scrierea unui cod în interpretor este simplă: o linie este o instrucțiune. Când apăsați Enter, linia de cod va fi executată (după ce a fost compilată instant și netransparent pentru user). De exemplu, încercați să scrieți acest lucru:


</div>


```python
print("hello")
```


<div class="mw-translate-fuzzy">

print este un cuvânt cheie în Python care înseamnă ca, bineînțeles, că printezi ceva pe ecran. Când apeși Enter, operația este executată , și mesajul \"hello\" este afișat. Dacă faci o greșeală, să scriem de exemplu:


</div>


```python
print(hello)
```


<div class="mw-translate-fuzzy">

Python îți va spune că nu știe ce este hello . Ghilimelele \" spun despre conținut că este un șir de caractere, care pur și simplu în jargonul informatic înseamnă o bucată de test. Fără ghilimele \", comanda de afișare a lui hello, acesta nu este recunoscut ca fiind un text , ci ca un cuvânt comandă special rezervat în Python.Important este că obțineți imediat o notificare de eroare. Apăsând săgeata sus (sau, în interpretorul FreeCAD CTRL+Săgeată sus), puteți merge înapoi la ultima comandă și să o scrieți corect.


</div>


<div class="mw-translate-fuzzy">

Interpretorul Python dispune de asemenea de un sistem integrat de help. Încercați să tastați:


</div>


```python
help(print)
```


<div class="mw-translate-fuzzy">

Veți obține o descriere lungă și completă a tot ceea ce poate face comanda "print".


</div>


<div class="mw-translate-fuzzy">

Acum că stăpânim total interpretorul nostru , putem începe lucrurile serioase.


</div>


{{Top}}



## Varibile


<div class="mw-translate-fuzzy">

Desigur, tipărirea lui \"hello\" nu este foarte interesantă. Mai interesant este să imprimați lucruri pe care nu le cunoșteați înainte sau să lăsați Python să le găsească pentru dvs. Aici vine conceptul de variabilă. O variabilă este pur și simplu o valoare pe care o stocați sub un nume. De exemplu, tastați:


</div>


```python
a = "hello"
print(a)
```


<div class="mw-translate-fuzzy">

Presupun că ați înțeles ce sa întâmplat, am \"salvat\" șirul \"hello\" într-o variabilă care poartă numele \"a\". Acum, \"a\" nu mai este un nume necunoscut! Putem să o folosim oriunde, de exemplu în comanda de afișare pe ecran. Putem folosi orice nume dorim, trebuie doar să urmați câteva reguli simple, cum ar fi nu folosiți spații sau punctuație. De exemplu, am putea scrie:


</div>


```python
hello = "my own version of hello"
print(hello)
```


<div class="mw-translate-fuzzy">

Vedeți? acum hello nu mai este un cuvânt nedefinit. Dacă, printr-un ghinion teribil, alegem un nume care există deja în Python? Să presupunem că dorim să stocăm șirul nostru sub numele \"print\":


</div>


```python
myVariable = "hello"
print(myVariable)
myVariable = "good bye"
print(myVariable)
```


<div class="mw-translate-fuzzy">

Noi am schimbat valoarea myVariable. Putem copia de asemenea variabile:


</div>


```python
var1 = "hello"
var2 = var1
print(var2)
```


<div class="mw-translate-fuzzy">

Rețineți că este important să oferiți nume descriptive variabilelor dvs. După un timp, nu vă veți aminti ce reprezintă variabila numită \"a\". Dar dacă l-ați numit, de exemplu, myWelcomeMessage, îți vei aminti cu ușurință scopul. Plus codul dvs. este un pas mai aproape de a fi auto-documentare.


</div>


<div class="mw-translate-fuzzy">

Cazul este foarte important. myVariable nu este aceeași cu myvariable, diferența dintre majuscule / minuscule *\'v\'*. Dacă trebuia să introduceți \"print myvariable\", s-ar întoarce cu o eroare pentru că nu a fost definită.


</div>


{{Top}}



## Numere


<div class="mw-translate-fuzzy">

Desigur, trebuie să știți că programarea este utilă pentru a trata toate tipurile de date, și mai ales numere, nu numai șiruri de text. Un lucru este important, Python trebuie să știe cu ce fel de date are de-a face. Am văzut în exemplul nostru de afișarea a lui "hello", că comanda de afișare a recunoscut șirul de caractere \"hello\". Acest lucru se datorează faptului că prin utilizarea ghilimelelor \" \", am spus în mod specific că această comanda de afișare va trata un șir de caractere alfabetice (text).


</div>


<div class="mw-translate-fuzzy">

Întotdeauna putem verifica tipul de date al unei variabile folosind cuvântul cheie special Python type():


</div>


```python
myVar = "hello"
type(myVar)
```


<div class="mw-translate-fuzzy">

Aceasta ne va spune că conținutul lui myVar este \'str\', scurt pentru șir în jargonul Python. De asemenea, avem și alte tipuri de date de bază, cum ar fi numere întregi (integer) și cu virgulă flotantă (float)


</div>


```python
firstNumber = 10
secondNumber = 20
print(firstNumber + secondNumber)
type(firstNumber)
```


<div class="mw-translate-fuzzy">

Acest lucru este mult mai interesant, nu-i așa? Acum avem un calculator puternic! Uită-te la cât de bine funcționează, Python știe că 10 și 20 sunt numere întregi. Deci, ele sunt stocate ca \"int\", iar Python poate face cu ele tot ce poate face cu numere întregi. Uită-te la rezultatele de acest lucru:


</div>


```python
firstNumber = "10"
secondNumber = "20"
print(firstNumber + secondNumber)
```


<div class="mw-translate-fuzzy">

Vedeți? L-am forțat pe Python să considere că cele două variabile nu sunt numere, ci simple piese de text. Python poate adăuga două bucăți de text împreună, dar nu va încerca să afle nici o sumă. Dar am vorbit despre numere întregi. Există și numere cu virgulă. Diferența este că numerele întregi nu au o parte zecimală, în timp ce numerele cu virgulă flotantă pot avea o parte zecimală:


</div>


```python
var1 = 13
var2 = 15.65
print("var1 is of type ", type(var1))
print("var2 is of type ", type(var2))
```


<div class="mw-translate-fuzzy">

Int și Floats pot fi amestecate fără probleme:


</div>


```python
total = var1 + var2
print(total)
print(type(total))
```


<div class="mw-translate-fuzzy">

Desigur, totalul are zecimale, nu? Apoi, Python a decis automat că rezultatul este un număr cuzecimale. În mai multe cazuri, cum ar fi acesta, Python decide automat ce tip este de utilizat. În alte cazuri, nu. De exemplu:


</div>


```python
varA = "hello 123"
varB = 456
print(varA + varB)
```


<div class="mw-translate-fuzzy">

Acest lucru ne va da o eroare, varA este un șir și varB este un int, iar Python nu știe ce să facă. Cu toate acestea, putem forța Python să convertească între tipuri:


</div>


```python
varA = "hello"
varB = 123
print(varA + str(varB))
```


<div class="mw-translate-fuzzy">

Acum, ambele sunt șiruri, operația funcționează! Rețineți că am \"convetit\" varB în șir la momentul afișării, dar nu am schimbat varB în sine. Dacă vrem să transformăm varB permanent într-un șir, ar trebui să o facem așa:


</div>


```python
varB = str(varB)
```


<div class="mw-translate-fuzzy">

Putem de asemenea să utilizăm int() și float() pentru a converti în întreg și cu virgulă mobilă dacă dorim:


</div>


```python
varA = "123"
print(int(varA))
print(float(varA))
```


<div class="mw-translate-fuzzy">

Probabil că ați observat că în această secțiune am folosit comanda de afișare în mai multe moduri. Am tipărit variabile, sume, mai multe lucruri separate prin virgule și chiar rezultatul altor comenzi Python, cum ar fi type(). Poate că ați văzut de asemenea că făcând aceste două comenzi,


</div>


```python
type(varA)
print(type(varA))
```


<div class="mw-translate-fuzzy">

avem exact același rezultat. Asta pentru că suntem în interpretor și totul este afișat automat. Când scriem programe mai complexe care rulează în afara interpretorului, nu se vor imprima automat, deci va trebui să folosim comanda de afișare. De acum încolo, haideți să-l oprim aici, va merge mai repede. Deci putem scrie pur și simplu:


</div>


```python
myVar = "hello friends"
myVar
```


{{Top}}



## Liste/matrici


<div class="mw-translate-fuzzy">

Un alt tip de date interesant este formată de către liste. O listă este pur și simplu o colecție de alte date. În același mod în care definim un șir de text folosind \"\", definim o listă folosind \[\]:


</div>


```python
myList = [1, 2, 3]
type(myList)
myOtherList = ["Bart", "Frank", "Bob"]
myMixedList = ["hello", 345, 34.567]
```


<div class="mw-translate-fuzzy">

Vedeți că poate conține orice tip de date. Listele sunt foarte utile deoarece puteți grupa împreună variabilele. Puteți face apoi tot felul de lucruri din cadrul grupului, de exemplu, numărarea acestora:


</div>


```python
len(myOtherList)
```


<div class="mw-translate-fuzzy">

sau recuperarea unui articol dintr-o listă:


</div>


```python
myName = myOtherList[0]
myFriendsName = myOtherList[1]
```


<div class="mw-translate-fuzzy">

Veți vedea că în timp ce comanda len () returnează numărul total de elemente dintr-o listă, poziția lor din listă începe cu 0. Primul element dintr-o listă este întotdeauna la poziția 0, așa că în \"myOtherList\", \"Bob\" va fi în poziția 2. Putem face mult mai mult cu listele, puteți citi [here](http://www.diveintopython.net/native_data_types/lists.html), ca de exemplu sortarea conținutului, ștergerea sau adăugarea elementelor.


</div>


<div class="mw-translate-fuzzy">

Un lucru amuzant și interesant este acela că: un șir de text este foarte asemănător cu o listă de caractere! Încercați să faceți acest lucru:


</div>


```python
myvar = "hello"
len(myvar)
myvar[2]
```


<div class="mw-translate-fuzzy">

De obicei, ceea ce puteți face cu listele se poate face și cu șiruri de caractere. De fapt, atât listele cât și șirurile sunt secvențe pe care Python le vede în aceeași manieră.


</div>


<div class="mw-translate-fuzzy">

Outside strings, ints, floats and lists, există mai multe tipuri de date încorporate, cum ar fi [dictionaries](http://www.diveintopython.net/native_data_types/index.html#d0e5174), sau care le puteți crea ca pe propriile tipuri de date cu [classes](http://www.freenetpages.co.uk/hp/alan.gauld/tutclass.htm).


</div>


{{Top}}

## Indentation


<div class="mw-translate-fuzzy">

O mare utilizare rece a listelor este, de asemenea, navigarea prin ele și să facă ceva cu fiecare element. De exemplu, uitați-vă la acest lucru:


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for dalton in alldaltons:
    print(dalton + " Dalton")
```


<div class="mw-translate-fuzzy">

Am iterat(jargonul informatic) prin lista noastră cu comanda \"for \... in \...\" și am făcut ceva cu fiecare dintre ele. Rețineți sintaxa specială: comanda **for** se termină cu **:** indicând că următorul lucru va fi un bloc al uneia sau mai multor comenzi. În interpretor, imediat după ce ați introdus linia de comandă care se termină cu:, promptul de comandă se va schimba la \... Notați sintaxa particulară a buclei , comanda se termină cu un \" : \" ceea ce indică lui Python că urmarea va fi un bloc de una sau mai multe comenzi.


</div>


<div class="mw-translate-fuzzy">

Cum va ști Python câte linii vor fi executate în interiorul buclei FOR \... IN ? Pentru asta, Python utilizează indentare. Adică liniile următoare nu vor începe imediat. Veți începe cu un spațiu gol sau mai multe spații goale sau un tab sau câteva tabs. Alte limbaje de programare utilizează alte metode, cum ar fi punerea totul în paranteză etc. Atâta timp cât scrieți liniile următoare cu aceeași indentare **same** , ele vor fi considerate parte a blocului for-in. Dacă începeți o linie cu 2 spații și următoarea cu 4, va exista o eroare. Când ați terminat, scrieți o altă linie fără indentare sau apăsați pe Enter pentru a reveni din blocul for-in.


</div>


<div class="mw-translate-fuzzy">

Indentarea este cool, deoarece ajută la lizibilitatea programului. Dacă utilizați indentări mari (de exemplu, utilizați tabs în loc de spații deoarece este mai mare), atunci când scrieți un program mare, veți avea o imagine clară a ceea ce este executat în interiorul a buclei for-in. Vom vedea că comenzile, altele decât cele for-in, pot avea și blocuri de cod.


</div>


<div class="mw-translate-fuzzy">

Comenzile for-in pot fi folosite pentru mai multe lucruri care trebuie efectuate mai mult decât o dată. Acesta poate fi, de exemplu, combinat cu comanda range():


</div>


```python
serie = range(1, 11)
total = 0
print("sum")
for number in serie:
    print(number)
    total = total + number
print("")
print(total)
```


<div class="mw-translate-fuzzy">

(Dacă ați executat exemplele de cod într-un interpretor prin copy and paste, veți găsi că blocul anterior de text vă va arunca o eroare în față. În schimb, copiați la sfârșitul blocului indentat, adică sfârșitul liniei \"\" total = total + number \"și apoi lipiți la interpretor păsați pe  până până la dispariția promptului cu trei puncte și codul se execută Apoi, copiați ultimele două linii în interpretor urmate de una sau mai multe  ar trebui să apară răspunsul final.)


</div>


<div class="mw-translate-fuzzy">

Dacă veți tasta în interpretor **help(range)** veți vedea: 
```python
range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
``` Aici parantezele pătrate denotă un parametru opțional. Totuși tot ce se așteptă este să fie numere întregi. Mai jos vom forța parametrii domeniului să fie un număr întreg folosind int()


</div>


```python
range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
```

Here the square brackets denote an optional parameter. However all are expected to be integers. Below we will force the step parameter to be an integer using `int()`:


```python
number = 1000
for i in range(0, 180 * number, int(0.5 * number)):
    print(float(i) / number)
```


<div class="mw-translate-fuzzy">

Sau lucruri mai complexe ca de exemplu:


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for n in range(4):
    print(alldaltons[n], " is Dalton number ", n)
```


<div class="mw-translate-fuzzy">

Vedeți că și comanda range () are acea particularitate ciudată că începe cu 0 (dacă nu specificați numărul de început) și că ultimul său număr va fi unul mai mic decât numărul de sfârșit pe care îl specificați. Aceasta este, bineînțeles, așa pentru că funcționează bine cu alte comenzi Python. De exemplu:


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
total = len(alldaltons)
for n in range(total):
    print(alldaltons[n])
```


<div class="mw-translate-fuzzy">

O altă utilizare interesantă a blocurilor indentate este cu comanda if. IF execută un bloc de cod numai dacă o anumită condiție este îndeplinită, de exemplu:


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Joe" in alldaltons:
    print("We found that Dalton!!!")
```


<div class="mw-translate-fuzzy">

Desigur, aceasta va imprima întotdeauna prima propoziție, dar încercați să înlocuiți a doua linie prin:


</div>


```python
if "Lucky" in alldaltons:
```


<div class="mw-translate-fuzzy">

Apoi nimic nu este afișat. De asemenea, putem specifica o altă afirmație

:   


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Lucky" in alldaltons:
    print("We found that Dalton!!!")
else:
    print("Such Dalton doesn't exist!")
```


{{Top}}



## Funcții


<div class="mw-translate-fuzzy">

Sunt câteva comenzi standard [standard Python commands](http://docs.python.org/reference/lexical_analysis.html#identifiers). În versiunea actuală a Python, există aproximativ 30, iar noi deja știm mai multe dintre ele. Dar imaginați-vă dacă am putea să ne inventăm propriile comenzi? Ei bine, putem, și este extrem de ușor. De fapt, majoritatea modulelor suplimentare pe care le puteți conecta la instalarea dvs. Python faceți exact acest lucru, adăugând comenzi pe care le puteți utiliza. O comandă personalizată în Python se numește o funcție și se face astfel:


</div>


```python
def printsqm(myValue):
    print(str(myValue) + " square meters")

printsqm(45)
```


<div class="mw-translate-fuzzy">

Extrem de simplu: comanda def () definește o nouă funcție. Dă-i un nume, iar în paranteză definiți argumente pe care le vom folosi în funcția noastră. Argumentele sunt date care vor fi transmise funcției. De exemplu, uitați-vă la comanda len (). Dacă scrieți len () singur, Python vă va spune că are nevoie de un argument. Asta este, vrei len () ceva, nu? Apoi, de exemplu, veți scrie len (myList) și veți obține lungimea myList. Ei bine, lista mea este un argument să-l treci la funcția len (). Funcția len () este definită astfel încât să știe ce să facă cu ceea ce este transmis acesteia. La fel cum am făcut aici.


</div>


<div class="mw-translate-fuzzy">

Numele \"myValue\" poate fi orice, și va fi utilizat numai în interiorul funcției rexpective. Este doar un nume pe care îl oferiți argumentului, astfel încât să puteți face ceva cu el, dar servește și pentru a spune funcției câte argumente să așteptați. De exemplu, dacă faceți acest lucru:


</div>


```python
printsqm(45, 34)
```


<div class="mw-translate-fuzzy">

Va exista o eroare. Funcția noastră a fost programată să primească un singur argument, dar a primit două, 45 și 34. Am putea să facem ceva în felul următor:


</div>


```python
def sum(val1, val2):
    total = val1 + val2
    return total

myTotal = sum(45, 34)
```


<div class="mw-translate-fuzzy">

Am făcut o funcție care primește două argumente, le însumează și returnează acea valoare. Returnarea a ceva este foarte utilă, deoarece putem face ceva cu rezultatul, cum ar fi stocarea în variabila myTotal. Bineînțeles, din moment ce suntem în interpretor și totul este afișat, faci:


</div>


{{Top}}



## Module


<div class="mw-translate-fuzzy">

Acum că avem o idee completă de cum lucrează Python, vom avea nevoie de un ultim lucru: Cum să lucrăm cu fișiere și cu module.


</div>


<div class="mw-translate-fuzzy">

Până acum, am scris linii de instrucțiuni Python în linie în interpretor, nu-i așa? Dacă am putea scrie câteva rânduri împreună și le-am fi executat imediat? Cu siguranță ar fi mai ușor să facem lucruri mai complexe. Și ne-am putea salva munca. Și asta este extrem de ușor. Pur și simplu deschideți un editor de text (cum ar fi notepad-ul din Windows, sub Linux: gedit, emacs sau vi) și scrieți toate liniile dvs. Python, la fel cum le scrieți în interpretor, cu indentări etc. , Apoi salvați fișierul undeva, de preferință cu o extensie .py. Asta e, aveți un program Python complet. Desigur, există editori mult mai buni decât notepad-ul, dar aceasta este doar să vă arătăm că un program Python nu este altceva decât un fișier text.


</div>


<div class="mw-translate-fuzzy">

Pentru a face Python să execute acel program, există sute de moduri. În Windows, pur și simplu faceți clic dreapta pe fișierul dvs., deschideți-l cu Python și executați-l. Dar o puteți executa și din interpretorul Python. Pentru aceasta, interpretorul trebuie să știe unde este programul dvs. .py. În FreeCAD, cel mai simplu mod este să plasați programul într-un loc în care interpretul Python al FreeCAD îl cunoaște în mod implicit, ca de exemplu FreeCAD\'s bin folder, sau orice folder Mod. (In Linux, aveți probabil un director /home//.FreeCAD/Mod, haideți să-i adăugăm un subdirector to that called scripts unde vom pune fișierul text.) Presupunem că scriem fișierul de maniera:


</div>


```python
def sum(a,b):
    return a + b

print("myTest.py succesfully loaded")
```


<div class="mw-translate-fuzzy">

Și noi salvăm asta ca pe myTest.py în direcotrul nostru FreeCAD/bin directory (sau în Linux la /home//.FreeCAD/Mod/scripts.) Acum , hai să pornim FreeCAD, și în fereastra interpretorului, scrie :


</div>


```python
import myTest
```


<div class="mw-translate-fuzzy">

fără extensia .py . Aceasta va executa pur și simplu conținutul fișierului, linie cu linie, ca și cum l-am fi scris în interpret. Se va crea funcția sumă, iar mesajul va fi imprimat. Există o mare diferență: comanda de import este făcută nu numai pentru a executa programe scrise în fișiere, ca și pentru ale noastre, dar și pentru a încărca funcțiile din interior, astfel încât acestea să devină disponibile în interpretor. Fișierele care conțin funcții, precum cele ale noastre, sunt numite module.


</div>


<div class="mw-translate-fuzzy">

În mod normal când scrii o funcție sum() in interpreter, noi o executăm simplu ca:


</div>


```python
sum(14, 45)
```


<div class="mw-translate-fuzzy">

La el am făcut și noi. Atunci când importăm un modul care conține funcția sum(), sintaxa este puțin diferită. Noi facem:


</div>


```python
myTest.sum(14, 45)
```


<div class="mw-translate-fuzzy">

Asta e, modulul este importat ca un \"container\", și cu toate funcțiile sale în interior. Acest lucru este extrem de util, deoarece putem importa o mulțime de module și să păstrăm totul bine organizat. Deci, practic, oriunde vedeți **something.somethingElse**, cu punct între, asta înseamnă că **somethingElse** este în interiorul lui **something**.


</div>


<div class="mw-translate-fuzzy">

De asemenea, putem importa funcția sum() direct în spațiul principal al interpretorului, astfel:


</div>


```python
from myTest import *
sum(12, 54)
```


<div class="mw-translate-fuzzy">

Practic, toate modulele se comportă așa. Importați un modul, apoi puteți utiliza funcțiile sale: module.function(argument). Aproape toate modulele fac acest lucru: definesc funcții, noi tipuri de date și clase pe care le puteți utiliza în interpretor sau în propriile module Python, deoarece nimic nu vă împiedică să importați alte module în modulul dvs.!


</div>


<div class="mw-translate-fuzzy">

Un ultim lucru extrem de util. Cum știm ce module avem, ce funcții există și cum să le folosim (adică, ce argumente au nevoie)? Am văzut deja că Python are o funcție help(). Face:


</div>


```python
help("modules")
```


<div class="mw-translate-fuzzy">

Ne va da o lista cu toate modulele disponibile. Acum putem introduce q pentru a ieși din ajutorul interactiv și pentru a importa oricare dintre ele. Putem chiar să răsfoim conținutul lor cu comanda dir()


</div>


```python
import math
dir(math)
```


<div class="mw-translate-fuzzy">

Vom vedea toate funcțiile conținute în modulul de matematică, precum și lucruri ciudate named \_\_doc\_\_, \_\_file\_\_, \_\_name\_\_. The \_\_doc\_\_ is extrem de utili, este un text de comentariu. Orice funcție a unui modul binefăcut are a \_\_doc\_\_ that care explică cum se folosește. De exemplu, vedem că este o funcție sin în interiorul modului de matematică. Vreți să știți cum se folosește?


</div>


```python
print(math.sin.__doc__)
```


<div class="mw-translate-fuzzy">

(Este posibil să nu fie evident, dar din ambele părți ale docului există două caractere subliniate.)


</div>


<div class="mw-translate-fuzzy">

Și în cele din urmă o bombonică: Când lucrăm la un modul nou sau existent, este mai bine să înlocuiți extensia de fișier cu py cum ar fi: myModule.FCMacro =\> myModule.py. Vrem adesea să o testeze astfel încât să o încărcăm ca mai sus.


</div>


```python
import importlib
importlib.reload(myTest)
```


<div class="mw-translate-fuzzy">

Cu toate acestea, există două alternative: în cadrul macro-ului se utilizează funcțiile exec sau execfile ale lui Python.


</div>


```python
exec(open("C:/PathToMyMacro/myMacro.FCMacro").read())
```


{{Top}}



## Începeți cu FreeCAD 


<div class="mw-translate-fuzzy">

Ei bine, cred că acum aveți o idee bună despre modul în care funcționează Python și puteți începe să explorați ce oferă FreeCAD. Funcțiile Python ale FreeCAD sunt bine organizate în diferite module. Unele dintre ele sunt deja încărcate (importate) când porniți FreeCAD. Deci, pur și simplu


</div>


```python
dir()
```


{{Top}}

## Notes

-   FreeCAD was originally designed to work with Python 2. Since Python 2 reached the end of its life in 2020, future development of FreeCAD will be done exclusively with Python 3, and backwards compatibility will not be supported.
-   Much more information about Python can be found in the [official Python tutorial](https://docs.python.org/3/tutorial/index.html) and the [official Python reference](https://docs.python.org/3/reference/).


{{Top}}


<div class="mw-translate-fuzzy">


{{docnav|Macros|Python scripting tutorial}}


</div>



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Introduction to Python/ro
