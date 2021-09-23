# Introduction to Python/it



{{TOCright}}

## Introduzione

Questo è un breve tutorial per quelli nuovi di [Python](https://it.wikipedia.org/wiki/Python). Python è un [Linguaggio di programmazione](https://it.wikipedia.org/wiki/Linguaggio_di_programmazione) sorgente-aperto e multipiattaforma . Ha diverse caratteristiche che lo rendono diverso dagli altri linguaggi di programmazione, e molto accessibile ai nuovi utenti:


<div class="mw-translate-fuzzy">

-   È stato progettato appositamente per essere letto facilmente dalle persone, quindi è molto facile da imparare e da capire.
-   È interpretato, ciò significa che, a differenza dei linguaggi compilati come il C, non è necessario compilare il programma prima di poterlo eseguire. Quando si desidera, il codice che si scrive può essere eseguito immediatamente, riga dopo riga. Siccome si procede gradualmente, passo dopo passo, è facile impararlo e trovare gli eventuali errori nel codice.
-   Può essere incorporato in altri programmi per essere usato come linguaggio di script. FreeCAD ha un interprete Python integrato, così, in FreeCAD, è possibile scrivere dei codici Python che manipolano parti di FreeCAD, ad esempio per creare la geometria. Questo è estremamente performante, perché invece di premere semplicemente un pulsante denominato \"Crea sfera\", che un programmatore ha messo a disposizione, si ha la libertà di creare facilmente dei propri strumenti per produrre una particolare geometria desiderata.
-   È estensibile. Si possono inserire facilmente dei nuovi moduli nella propria installazione di Python ed estenderne le funzionalità. Ad esempio, esistono moduli Python che permettono di leggere e scrivere le immagini jpg, di comunicare con Twitter, di programmare le operazioni del proprio sistema operativo, ecc.


</div>


<div class="mw-translate-fuzzy">

Ora, mettiamoci al lavoro! Ricordare che ciò che verrà dopo è solamente una semplice introduzione e non un tutorial completo. Ma la speranza è che dopo si avranno basi sufficienti per esplorare più in profondità i meccanismi di FreeCAD.


</div>

## L\'interprete


<div class="mw-translate-fuzzy">

Di solito, per scrivere programmi per computer, basta aprire un editor di testo (o l\'ambiente di programmazione preferito che, in genere, è un editor di testo con strumenti aggiuntivi), scrivere il programma, quindi compilarlo ed eseguirlo. Il più delle volte si fanno degli errori di scrittura, per cui il programma non funziona, e si ottiene un messaggio di errore che dà informazioni su cosa è andato storto. Quindi si ritorna all\'editor di testo, si correggono gli errori, si esegue di nuovo, e così via fino a quando il programma funziona bene.


</div>


<div class="mw-translate-fuzzy">

In Python, l\'intero processo, può essere eseguito in modo trasparente all\'interno del suo interprete. L\'interprete Python è una finestra con un prompt dei comandi, dove si può digitare direttamente il codice Python. Se si installa Python sul ​​proprio computer (scaricarlo dal [sito web di Python](http://www.python.org) se lavorate su Windows o Mac, installarlo dal repository dei pacchetti se utilizzate GNU/Linux), si avrà un interprete Python nel menu di avvio. FreeCAD dispone di un proprio interprete Python visualizzato nella sua finestra inferiore:


</div>

![](images/FreeCAD_Python_console.png ) *La console di FreeCAD Python*

Se non la vedi, clicca su **Vista → Pannelli → Console Python**. La console Python può essere ridimensionata e anche sganciata.

L\'interprete mostra la versione di Python, poi un simbolo `>>>` che è il prompt dei comandi. Scrivere codice nell\'interprete è semplice: una linea è un\'istruzione. Quando premete **Invio**, la vostra linea di codice verrà eseguita (dopo essere stata istantaneamente e invisibilmente compilata). Per esempio, provate a scrivere questo:


```python
print("hello")
```


`print()`

è un comando Python che, ovviamente, stampa qualcosa sullo schermo. Quando si preme **Invio**, l\'operazione viene eseguita e viene stampato il messaggio `"hello"`. Se si commette un errore, per esempio scriviamo:


```python
print(hello)
```

Python ve lo dirà immediatamente. In questo caso Python non sa cosa sia `hello`. I caratteri `" "` specificano che il contenuto è una stringa, gergo di programmazione per un pezzo di testo. Senza questi il comando `print()` non riconosce `hello`. Premendo la freccia su si può tornare indietro all\'ultima linea di codice e correggerla.

L\'interprete Python ha anche un sistema di aiuto integrato. Diciamo che non capiamo cosa è andato storto con `print(hello)` e vogliamo informazioni specifiche sul comando:


```python
help("print")
```


<div class="mw-translate-fuzzy">

Si ottiene una lunga e completa descrizione di tutto quello che può fare il comando print.


</div>


<div class="mw-translate-fuzzy">

Ora che si ha il controllo totale dell\'interprete, si può cominciare con le cose significative.


</div>

[top](#top.md)

## Variabili


<div class="mw-translate-fuzzy">

Naturalmente, stampare \"ciao\" non è molto interessante. Più interessante è stampare cose che non si conoscono prima, o lasciare che Python le trovi per noi. Qui entra in gioco il concetto di variabile. Una variabile è semplicemente un valore che viene memorizzato con un nome specifico. Ad esempio, digitare questo:


</div>


```python
a = "hello"
print(a)
```


<div class="mw-translate-fuzzy">

Sicuramente si capisce quello che succede, la stringa \"ciao\" viene \"salvata\" sotto il nome \"a\". Ora, \"a\" non è più un nome sconosciuto! Si può usare ovunque, per esempio nel comando print. È possibile utilizzare qualsiasi nome che si desideri, basta rispettare alcune semplici regole, tipo non usare spazi o segni di punteggiatura. Ad esempio, si potrebbe tranquillamente scrivere:


</div>


```python
hello = "my own version of hello"
print(hello)
```


<div class="mw-translate-fuzzy">

Visto? ciao ora non è più una parola indefinita. E se, per sfortuna, si sceglie un nome che in Python esiste già? Supponiamo di voler conservare una stringa con il nome \"print\":


</div>


```python
myVariable = "hello"
print(myVariable)
myVariable = "good bye"
print(myVariable)
```


<div class="mw-translate-fuzzy">

Il valore di myVariable è stato cambiato. Le variabili possono anche essere copiate:


</div>


```python
var1 = "hello"
var2 = var1
print(var2)
```


<div class="mw-translate-fuzzy">

Notare che è importante dare alle variabili dei nomi descrittivi. Quando si scrivono programmi lunghi, dopo un po\' probabilmente non si ricorda più cosa rappresenta la variabile denominata \"a\". Se invece viene chiamata, ad esempio, MioMessaggioDiBenvenuto, quando la si vede, si capisce facilmente a cosa serve. In più è un passo avanti verso l\'autodocumentazione del proprio codice.


</div>


<div class="mw-translate-fuzzy">

La differenza tra maiuscole e minuscole è molto importante. myVariable non è uguale a myvariable, la differenza è tra **v** maiuscola e minuscola. Se si inserisce \"print myvariable\", viene restituito un errore non definito.


</div>

[top](#top.md)

## Numeri


<div class="mw-translate-fuzzy">

È noto che la programmazione serve per trattare ogni tipo di dati, non solo le stringhe di testo, ma soprattutto i numeri. È molto importante che Python sappia che tipo di dati deve trattare. Nell\'esempio precedente, con print ciao, si è visto che il comando print ha riconosciuto la nostra stringa \"ciao\". Questo perché utilizzando il segno \", abbiamo specificato al comando print che ciò che seguiva era una stringa di testo.


</div>


<div class="mw-translate-fuzzy">

Per controllare in qualsiasi momento di quale tipo sono i dati contenuti in una variabile si utilizza la speciale parola chiave di Python type():


</div>


```python
myVar = "hello"
type(myVar)
```


<div class="mw-translate-fuzzy">

In questo caso ci dice che il contenuto di myVar è \'str\', ovvero una stringa in gergo Python. Ci sono anche altri tipi di dati, ad esempio i numeri interi (integer) e i numeri in virgola mobile (float numbers):


</div>


```python
firstNumber = 10
secondNumber = 20
print(firstNumber + secondNumber)
type(firstNumber)
```


<div class="mw-translate-fuzzy">

Questo è già molto più interessante, vero? Ora si dispone di una potente calcolatrice! Notare bene come funziona. Python capisce che 10 e 20 sono numeri interi, quindi vengono memorizzati come \"int\", e con essi Python può fare tutte le operazioni consentite con numeri interi. Osservare i risultati di questo codice:


</div>


```python
firstNumber = "10"
secondNumber = "20"
print(firstNumber + secondNumber)
```


<div class="mw-translate-fuzzy">

Visto? Python è stato indotto a considerare le due variabili non più come numeri, ma come semplici parti di testo. Python può unire insieme due parti di testo, ma con esse non cerca di produrre una somma. Torniamo ai numeri. Oltre ai numeri interi (int) ci sono anche i numeri in virgola mobile (float). I numeri interi non hanno una parte decimale, mentre i numeri float possono avere una parte decimale:


</div>


```python
var1 = 13
var2 = 15.65
print("var1 is of type ", type(var1))
print("var2 is of type ", type(var2))
```


<div class="mw-translate-fuzzy">

I numeri Int e Float possono essere mescolati tra di loro senza problemi:


</div>


```python
total = var1 + var2
print(total)
print(type(total))
```


<div class="mw-translate-fuzzy">

Naturalmente il totale ha dei decimali, vero? Quindi Python ha deciso automaticamente che il risultato è un float. In molti casi, come in questo, Python decide automaticamente il tipo da usare. In altri casi no. Ad esempio con:


</div>


```python
varA = "hello 123"
varB = 456
print(varA + varB)
```


<div class="mw-translate-fuzzy">

Si produce un errore, varA è una stringa e varB è un int, quindi Python non sa cosa fare. Ma possiamo indurre Python a convertire i tipi:


</div>


```python
varA = "hello"
varB = 123
print(varA + str(varB))
```


<div class="mw-translate-fuzzy">

Ora entrambi sono stringhe, e l\'operazione funziona! Notare che, con questi comandi, varB è convertita in \"stringa\" solo al momento della stampa, però varB originale non viene modificata. Per trasformare varB permanentemente in una stringa, si deve fare:


</div>


```python
varB = str(varB)
```


<div class="mw-translate-fuzzy">

Inoltre è possibile usare int() e float() per convertire in int e in float:


</div>


```python
varA = "123"
print(int(varA))
print(float(varA))
```


<div class="mw-translate-fuzzy">

Sicuramente avete notato che in questa sezione il comando di stampa (print) è stato utilizzato in diversi modi. Abbiamo stampato variabili, somme, parti separati da virgole, e anche il risultato di altri comandi Python, ad esempio type(). Forse avete anche notato che questi due comandi,


</div>


```python
type(varA)
print(type(varA))
```


<div class="mw-translate-fuzzy">

producono esattamente lo stesso risultato. Questo succede perché siamo nell\'interprete, dove ogni cosa viene sempre automaticamente stampata sullo schermo. Per velocizzare, d\'ora in avanti si può fare a meno di usarlo e quindi scrivere semplicemente:


</div>


```python
myVar = "hello friends"
myVar
```

[top](#top.md)

## Liste


<div class="mw-translate-fuzzy">

Un altro tipo di dati interessante è una list (lista). Una lista è semplicemente un elenco di altri dati. In modo analogo a come si definisce una stringa di testo usando \" \", una lista si definisce usando \[\]:


</div>


```python
myList = [1, 2, 3]
type(myList)
myOtherList = ["Bart", "Frank", "Bob"]
myMixedList = ["hello", 345, 34.567]
```


<div class="mw-translate-fuzzy">

Come si vede, una lista può contenere dati di qualsiasi tipo. Le liste sono molto utili perché permettono di raggruppare le variabili. Con il gruppo, successivamente, è possibile fare diverse cose, ad esempio contare i suoi componenti:


</div>


```python
len(myOtherList)
```


<div class="mw-translate-fuzzy">

o recuperare un elemento da una lista:


</div>


```python
myName = myOtherList[0]
myFriendsName = myOtherList[1]
```


<div class="mw-translate-fuzzy">

Come si vede, mentre il comando len() restituisce il numero totale di elementi in una lista, la loro \"posizione\" nella lista inizia con 0. Il primo elemento in una lista si trova sempre in posizione 0, quindi nella lista myOtherList, \"Bob\" è nella posizione 2. Con le liste è possibile eseguire molte altre operazioni, descritte in modo più completo [qui](http://diveintopython.org/native_data_types/lists.html), ad esempio, ordinare i suoi contenuti, rimuovere o aggiungere elementi.


</div>


<div class="mw-translate-fuzzy">

Una cosa curiosa: una stringa di testo è molto simile a una lista di caratteri! Provate a fare questo:


</div>


```python
myvar = "hello"
len(myvar)
myvar[2]
```


<div class="mw-translate-fuzzy">

In genere, tutto quello che si può fare con le liste si può fare anche con le stringhe. In effetti le liste e le stringhe sono entrambe delle sequenze.


</div>


<div class="mw-translate-fuzzy">

Oltre a stringhe, int, float e liste, in Python sono disponibili molti altri tipi di dati built-in (incorporati), quali ad esempio i [dictionaries](http://www.diveintopython.net/native_data_types/index.html#d0e5174) (collezione di oggetti), oppure si possono creare dei propri tipi di dati utilizzando le [classi](http://www.freenetpages.co.uk/hp/alan.gauld/tutclass.htm).


</div>

[top](#top.md)

## Indentazione


<div class="mw-translate-fuzzy">

Un tipico uso della lista consiste nel navigare al suo interno e di operare con i suoi elementi. Per esempio osservare questo:


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for dalton in alldaltons:
    print(dalton + " Dalton")
```


<div class="mw-translate-fuzzy">

In questo esempio, la lista viene iterata (nuovo gergo di programmazione!) con il comando \"for \... in \...\" e con ognuno dei suoi elementi viene eseguito qualcosa.

Notare la speciale sintassi. Il comando \"for\" termina con un \":\" questo indica a Python che ciò che segue è un blocco di uno o più comandi. Subito dopo che viene inserita la riga con il comando che termina con :, il prompt dei comandi cambia in \... il che significa che Python ha riconosciuto un comando terminato con un (:) e quello che segue è parte del comando stesso.


</div>


<div class="mw-translate-fuzzy">

Come fa Python a sapere quante delle prossime righe sono da eseguire all\'interno dell\'operazione for \... in ? Per sapere questo, Python utilizza l\'indentazione. Cioè, le righe successive non iniziano immediatamente, ma iniziano con uno o più spazi vuoti, oppure con uno o più spazi di tabulazione. Altri linguaggi di programmazione utilizzano vari metodi, tipo inserire tutto dentro parentesi, ecc. Finché le righe successive sono scritte con la **stessa indentazione**, esse sono considerate come parte del blocco for-in. Quando si inizia una riga con 2 spazi vuoti e quella successiva con 4, si produce un errore. Per terminare e uscire dal blocco for-in, basta scrivere una nuova riga senza rientro, o semplicemente premere Invio.


</div>


<div class="mw-translate-fuzzy">

L\'indentazione è molto utile perché conferisce leggibilità al promma. Se è ampia (usando, ad esempio, tab che crea più spazi invece di un solo), quando si scrive un programma lungo si ha una visione chiara di ciò che viene eseguito all\'interno di ogni blocco. Vedremo che anche molti altri comandi diversi da for-in richiedono blocchi indentati.


</div>


<div class="mw-translate-fuzzy">

Il comando for-in può essere utilizzato per varie operazioni che devono essere eseguite più volte. Ad esempio, può essere combinato con il comando range():


</div>


```python
serie = range(1, 11)
total = 0
print("sum")
for number in serie:
    print(number)
    total = total + number
print("----")
print(total)
```


<div class="mw-translate-fuzzy">

Per usare i decimali in un loop range.


</div>

If you type into the interpreter `help(range)` you will see:


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

O per operazioni più complesse tipo questa:


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for n in range(4):
    print(alldaltons[n], " is Dalton number ", n)
```


<div class="mw-translate-fuzzy">

Come si vede, anche il comando range() ha la strana particolarità di iniziare con 0 (quando non si specifica il numero di partenza) e che il suo ultimo numero è uno in meno del numero finale specificato. Ciò, naturalmente, perché questo modo funziona bene con gli altri comandi di Python. Ad esempio:


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
total = len(alldaltons)
for n in range(total):
    print(alldaltons[n])
```


<div class="mw-translate-fuzzy">

Un altro uso interessante dei blocchi indentati si ha con il comando if. Il comando if esegue un blocco di codice solo se una certa condizione è soddisfatta, ad esempio:


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Joe" in alldaltons:
    print("We found that Dalton!!!")
```


<div class="mw-translate-fuzzy">

Naturalmente, questo esempio stampa sempre la prima frase, ma provare a sostituire la seconda riga con:


</div>


```python
if "Lucky" in alldaltons:
```


<div class="mw-translate-fuzzy">

Ora non viene più stampato nulla. Si può anche specificare una dichiarazione: else:


</div>


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Lucky" in alldaltons:
    print("We found that Dalton!!!")
else:
    print("Such Dalton doesn't exist!")
```

[top](#top.md)

## Funzioni


<div class="mw-translate-fuzzy">

I [comandi standard di Python](http://docs.python.org/reference/lexical_analysis.html#identifiers) non sono molti. Nella versione corrente di Python ce ne sono circa 30, e ne conosciamo già alcuni di loro. Ma immaginate se potessimo inventare dei nostri propri comandi? Beh, possiamo, ed è estremamente facile. In effetti, la maggior parte dei moduli aggiuntivi che si possono aggiungere nella propria installazione di Python fanno esattamente questo, essi aggiungono dei comandi utilizzabili. In Python un comando personalizzato si chiama funzione e si crea in questo modo:


</div>


```python
def printsqm(myValue):
    print(str(myValue) + " square meters")

printsqm(45)
```


<div class="mw-translate-fuzzy">

Estremamente semplice: il comando def() definisce una nuova funzione. Si può dargli un nome, e dentro la parentesi si definiscono gli argomenti che useremo nella nostra funzione. Gli argomenti sono i dati che verranno passati alla funzione.

Ad esempio, osservare il comando len(). Se si scrive semplicemente len() da solo, Python vi dice che ha bisogno di un argomento. Cioè, si vuole len() di qualcosa. Quindi, ad esempio, bisogna scrivere len(myList) per ottenere la lunghezza di myList. Bene, myList è un argomento che viene passato alla funzione len(). La funzione len() è definita in modo da sapere come utilizzare ciò che gli viene passato. Esattamente come si è appena fatto qui.


</div>


<div class="mw-translate-fuzzy">

Il nome \"myValue\" può contenere qualsiasi oggetto, e viene utilizzato solo all\'interno della funzione. È solo un nome assegnato all\'argomento in modo da poter operare con esso, però serve anche a fare in modo che la funzione sappia quanti argomenti aspettarsi. Se, ad esempio, si esegue:


</div>


```python
printsqm(45, 34)
```


<div class="mw-translate-fuzzy">

Si ottiene un errore. La funzione è stata programmata per ricevere un solo argomento, ma ne ha ricevuto due, 45 e 34. In sostituzione, si può eseguire qualcosa di simile a:


</div>


```python
def sum(val1, val2):
    total = val1 + val2
    return total

myTotal = sum(45, 34)
```


<div class="mw-translate-fuzzy">

Dove si crea una funzione che riceve due argomenti, li somma, e restituisce il valore. Ottenere qualcosa è molto utile, perché permette di utilizzare il risultato ottenuto e, ad esempio, memorizzarlo nella variabile myTotal. Naturalmente, visto che siamo nell\'interprete e tutto quello che facciamo viene stampato, digitando:


</div>

[top](#top.md)

## Moduli


<div class="mw-translate-fuzzy">

Ora che si ha un\'idea di come funziona Python, serve una ultima cosa: Come lavorare con i file e i moduli.


</div>


<div class="mw-translate-fuzzy">

Fino ad ora, abbiamo scritto le istruzioni nell\'interprete di Python riga per riga, vero?

Quando si intende fare delle cose più complesse, è certamente più comodo scrivere prima diverse righe di codice, e poi eseguirle tutte insieme in una unica volta. Bene, anche questo, è estremamente facile da farsi, e inoltre permette anche salvare il proprio lavoro.

È sufficiente aprire un editor di testo (ad es. il Blocco Note di Windows, o gedit, emacs, o vi per Linux), e scrivere tutte le proprie righe di Python, nello stesso modo in cui si scrivono nell\'interprete, con indentazioni, ecc. Quindi, salvare il file da qualche parte, preferibilmente con estensione .py. Tutto qui, ora si dispone di un programma Python completo. Naturalmente, ci sono editor migliori di notepad, citato solo per dimostrare che un programma Python non è altro che un file di testo.


</div>


<div class="mw-translate-fuzzy">

Per far eseguire questo programma da Python, ci sono centinaia di modi. In Windows, è sufficiente fare clic sul file, aprirlo con Python, ed eseguirlo. Ma si può anche eseguire con l\'interprete di Python stesso. Per fare questo, l\'interprete deve sapere dove si trova il programma .py. In FreeCAD, il modo più semplice è quello di inserire il programma in un luogo che l\'interprete Python di FreeCAD conosce di default, quale, ad esempio, la cartella bin di FreeCAD, o una qualsiasi delle cartelle Mod. (In Linux, si ha probabilmente una directory /home//.FreeCAD/Mod, aggiungiamo una sottodirectory a quegli script richiamati dove inseriremo il file di testo.) Supponiamo di scrivere questo file:


</div>


```python
def sum(a,b):
    return a + b

print("myTest.py succesfully loaded")
```


<div class="mw-translate-fuzzy">

e di salvarlo con il nome MioTest.py nella nostra directory /bin di FreeCAD (o on Linux to /home//.FreeCAD/Mod/scripts). Ora, avviamo FreeCAD e nella finestra interprete scriviamo:


</div>


```python
import myTest
```


<div class="mw-translate-fuzzy">

senza l\'estensione. py. Questo comando esegue semplicemente il contenuto del file, riga per riga, esattamente come quando viene scritto nell\'interprete. Viene creata la funzione somma, poi viene stampato il messaggio. Però c\'è una grande differenza: il comando di importazione (import) serve non solo per eseguire i programmi contenuti in un file, come il nostro, ma anche per caricare le funzioni interne, in modo da renderle disponibili nell\'interprete. I file, come il nostro, contenenti funzioni sono chiamati moduli.


</div>


<div class="mw-translate-fuzzy">

Di solito, come si è fatto in precedenza, quando si scrive la funzione sum() nell\'interprete, si digita semplicemente:


</div>


```python
sum(14, 45)
```


<div class="mw-translate-fuzzy">

Invece, quando si importa un modulo contenente una funzione sum(), la sintassi è un po\' diversa. Si scrive:


</div>


```python
myTest.sum(14, 45)
```


<div class="mw-translate-fuzzy">

Cioè, il modulo viene importato come un \"contenitore\", e tutte le sue funzioni sono all\'interno. Dato che è possibile importare più moduli, ciò è estremamente utile per tenere il tutto ben organizzato. In sostanza, quando si vede \"qualcosa.qualcosaAltro\", con un punto in mezzo, significa che \"qualcosaAltro\" è contenuto in \"qualcosa\".


</div>


<div class="mw-translate-fuzzy">

Si può anche estrarre da test una sua parte, e importare la funzione sum() direttamente nello spazio principale dell\'interprete, in questo modo:


</div>


```python
from myTest import *
sum(12, 54)
```


<div class="mw-translate-fuzzy">

In pratica tutti i moduli si comportano in questo modo. È possibile importare un modulo, e poi utilizzare le sue funzioni tramite l\'istruzione: module.function (argomento). Quasi tutti i moduli eseguono le seguenti operazioni: definiscono le funzioni, i nuovi tipi di dati e le classi che è possibile utilizzare nell\'interprete o nei moduli Python, perché nulla impedisce di importare altri moduli all\'interno di un proprio modulo!


</div>


<div class="mw-translate-fuzzy">

Un\'ultima cosa estremamente utile. Come si fa per sapere quali moduli sono disponibili, quali funzioni sono al loro interno e come usarli (cioè, di che tipo di argomenti hanno bisogno)? Si è già visto che Python ha una funzione help(). Digitare:


</div>


```python
help("modules")
```


<div class="mw-translate-fuzzy">

Viene restituito un elenco di tutti i moduli disponibili. Digitare q per uscire dall\'aiuto interattivo e importare qualsiasi di essi.

Si può anche sfogliare il contenuto del modulo tramite il comando dir():


</div>


```python
import math
dir(math)
```


<div class="mw-translate-fuzzy">

In questo caso, si vedono tutte le funzioni contenute nel modulo di matematica (il modulo math), come, ad esempio, cose con strani nomi \_\_ doc\_\_, \_\_ FILE\_\_, \_\_ name\_\_. L\'oggetto doc\_\_ \_\_ è estremamente utile, è un testo di documentazione. Ogni funzione dei moduli (se fatti bene) ha un proprio \_\_doc\_\_ che spiega come usarla. Se, per esempio, si vuole sapere come usare la funzione sin (seno) contenuta all\'interno del modulo math, basta digitare:


</div>


```python
print(math.sin.__doc__)
```


<div class="mw-translate-fuzzy">

(Potrebbe non essere evidente, ma su entrambi i lati del doc ci sono due caratteri di sottolineatura.)


</div>


<div class="mw-translate-fuzzy">

E infine un ultimo piccolo omaggio: quando lavoriamo su un modulo nuovo o esistente, è meglio sostituire l\'estensione del file con py come: myModule.FCMacro =\> myModule.py. Spesso vogliamo testarlo, quindi lo caricheremo come sopra.


</div>


```python
import importlib
importlib.reload(myTest)
```


<div class="mw-translate-fuzzy">

Però, si può fare in due modi: 1. Utilizzare una funzione exec o execfile di Python all\'interno della macro.


</div>


```python
exec(open("C:/PathToMyMacro/myMacro.FCMacro").read())
```

[top](#top.md)

## Iniziare con FreeCAD 


<div class="mw-translate-fuzzy">

Ora che si ha un\'idea di come funziona Python si può iniziare ad esplorare quello che FreeCAD ha da offrire. Le funzioni Python di FreeCAD sono tutte ben organizzate in moduli diversi. Alcuni di loro vengono caricati (importati) all\'avvio di FreeCAD. Quindi, basta solo, digitare:


</div>


```python
dir()
```

[top](#top.md)

## Notes

-   FreeCAD was originally designed to work with Python 2. Since Python 2 reached the end of its life in 2020, future development of FreeCAD will be done exclusively with Python 3, and backwards compatibility will not be supported.
-   Much more information about Python can be found in the [official Python tutorial](https://docs.python.org/3/tutorial/index.html) and the [official Python reference](https://docs.python.org/3/reference/).

[top](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
