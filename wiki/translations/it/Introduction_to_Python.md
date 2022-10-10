# Introduction to Python/it
{{TOCright}}

## Introduzione

Quello che segue è un breve tutorial per chi non conosce [Python](https   *//it.wikipedia.org/wiki/Python). Python è un [Linguaggio di programmazione](https   *//it.wikipedia.org/wiki/Linguaggio_di_programmazione) open source e multipiattaforma . Ha diverse caratteristiche, che lo rendono diverso dagli altri linguaggi di programmazione, ed è facilmente accessibile ai nuovi utenti   *

-   È stato progettato per essere leggibile dagli esseri umani, rendendolo relativamente facile da imparare e da capire.
-   Viene interpretato, questo significa che i programmi non devono essere compilati prima di poter essere eseguiti. Il codice Python può essere eseguito immediatamente, anche riga per riga, se si desidera.
-   Può essere incorporato in altri programmi come linguaggio di scripting. FreeCAD ha un interprete Python incorporato. Si può scrivere codice Python per manipolare parti di FreeCAD. Questa funzionalità è molto potente e comporta che puoi costruire i tuoi strumenti personalizzati.
-   È estensibile, si può facilmente inserire nuovi moduli nella tua installazione di Python ed estenderne la funzionalità. Ad esempio, ci sono moduli che consentono a Python di leggere e scrivere immagini, di comunicare con Twitter, di pianificare attività che devono essere eseguite dal tuo sistema operativo, ecc.

Quella che segue è un\'introduzione molto semplice e non un tutorial completo. Ma si spera che fornisca un buon punto di partenza per un\'ulteriore esplorazione di FreeCAD e dei suoi meccanismi. Si consiglia vivamente di inserire i seguenti frammenti di codice in un interprete Python.

## L\'interprete

Di solito, per scrivere programmi per computer, basta aprire un editor di testo (o l\'ambiente di programmazione preferito che di base è un editor di testo con alcuni strumenti aggiuntivi), scrivere il programma, quindi compilarlo ed eseguirlo. Spesso si fanno degli errori di scrittura, per cui il programma non funziona, e si ottiene un messaggio di errore che dà informazioni su cosa è andato storto. Quindi si ritorna all\'editor di testo, si correggono gli errori, si esegue di nuovo, e così via fino a quando il programma funziona bene.

In Python l\'intero processo può essere eseguito in modo trasparente all\'interno dell\'interprete Python. L\'interprete è una finestra Python con un prompt dei comandi, in cui puoi semplicemente digitare il codice Python. Se hai installato Python sul tuo computer (scaricalo dal [sito Web Python](https   *//www.python.org/) se sei su Windows o Mac, installalo dal repository del tuo pacchetto se sei su GNU/Linux), avrai un interprete Python nel tuo menu di avvio. Ma, come già accennato, FreeCAD ha anche un interprete Python integrato   * la [Console Python](Python_console/it.md).

![](images/FreeCAD_Python_console.png ) 
*La console di FreeCAD Python*

Se non la vedi, clicca su **Visualizza → Pannelli → Console Python**. La console Python può essere ridimensionata e anche sganciata.

L\'interprete mostra la versione di Python, poi un simbolo `>>>` che è il prompt dei comandi. Scrivere codice nell\'interprete è semplice   * una linea è un\'istruzione. Quando premete **Invio**, la vostra linea di codice verrà eseguita (dopo essere stata istantaneamente e invisibilmente compilata). Per esempio, provate a scrivere questo   *


```python
print("hello")
```


`print()`

è un comando Python che, ovviamente, stampa qualcosa sullo schermo. Quando si preme **Invio**, l\'operazione viene eseguita e viene stampato il messaggio `"hello"`. Se si commette un errore, per esempio scriviamo   *


```python
print(hello)
```

Python ve lo dirà immediatamente. In questo caso Python non sa cosa sia `hello`. I caratteri `" "` specificano che il contenuto è una stringa, gergo di programmazione per un pezzo di testo. Senza questi il comando `print()` non riconosce `hello`. Premendo la freccia su si può tornare indietro all\'ultima linea di codice e correggerla.

L\'interprete Python ha anche un sistema di aiuto integrato. Diciamo che non capiamo cosa è andato storto con `print(hello)` e vogliamo informazioni specifiche sul comando   *


```python
help("print")
```

Si ottiene una lunga e completa descrizione di tutto quello che può fare il comando `print()`.

Ora che si è capito cos\'è l\'interprete Python, possiamo continuare con le cose più serie. {{Top}}

## Variabili

Molto spesso nella programmazione è necessario memorizzare un valore sotto un nome. È qui che entrano in gioco le variabili. Ad esempio, digita questo   *


```python
a = "hello"
print(a)
```

Sicuramente si capisce quello che succede, la stringa \"ciao\" viene \"salvata\" sotto il nome \"a\". Ora, \"a\" non è più un nome sconosciuto! Si può usare ovunque, per esempio nel comando print. È possibile utilizzare qualsiasi nome che si desideri, basta rispettare alcune semplici regole, tipo non usare spazi o segni di punteggiatura. Ad esempio, si potrebbe tranquillamente scrivere   *


```python
hello = "my own version of hello"
print(hello)
```

Ora `hello` non è più un indefinito. Le variabili possono essere modificate in qualsiasi momento, per questo si chiamano variabili, il loro contenuto può variare. Per esempio   *


```python
myVariable = "hello"
print(myVariable)
myVariable = "good bye"
print(myVariable)
```

Il valore di `myVariable` è stato cambiato. Le variabili possono anche essere copiate   *


```python
var1 = "hello"
var2 = var1
print(var2)
```

È consigliabile assegnare nomi significativi alle variabili. Dopo un po\' ci si ricorderà più cosa rappresenta la variabile denominata `a`. Ma se l\'hai chiamata, ad esempio, `myWelcomeMessage`, ricorderai facilmente il suo scopo. Inoltre, il tuo codice sarà un passo avanti verso l\'autodocumentazione.

Il Maiuscolo o minuscolo è molto importante, `myVariable` non è lo stesso di `myvariable`. Se si dovesse inserire `print(myvariable)`, verrebbe restituito un errore come nome non definito. {{Top}}

## Numeri

Ovviamente i programmi Python possono gestire tutti i tipi di dati, non solo le stringhe di testo. Una cosa è importante, Python deve sapere con che tipo di dati ha a che fare. Abbiamo visto nel nostro esempio print hello, che il comando `print()` ha riconosciuto la nostra stringa `"hello"`. Utilizzando i caratteri `" "`, abbiamo specificato che quella che segue è una stringa di testo.

Possiamo sempre controllare il tipo di dati di una variabile con il comando `type()`   *


```python
myVar = "hello"
type(myVar)
```

Questo significa che il contenuto di `myVar` è un `'str'`, che è l\'abbreviazione di string. Esistono anche altri tipi di dati di base come numeri interi e a virgola mobile   *


```python
firstNumber = 10
secondNumber = 20
print(firstNumber + secondNumber)
type(firstNumber)
```

Python sa che 10 e 20 sono numeri interi, quindi sono archiviati come `'int'` e Python può fare con loro tutto ciò che può fare con i numeri interi. Osserva i risultati di questo codice   *


```python
firstNumber = "10"
secondNumber = "20"
print(firstNumber + secondNumber)
```

Qui abbiamo costretto Python a considerare che le nostre due variabili non sono numeri ma parti di testo. Python può unire due parti di testo insieme, anche se in tal caso, ovviamente, non eseguirà alcuna operazione aritmetica. Ma si stava parlando di numeri interi. Ci sono anche i numeri a virgola mobile. La differenza è che i numeri a virgola mobile possono avere una parte decimale, mentre i numeri interi no   *


```python
var1 = 13
var2 = 15.65
print("var1 is of type ", type(var1))
print("var2 is of type ", type(var2))
```

Numeri interi e a virgola mobile possono essere mescolati insieme senza problemi   *


```python
total = var1 + var2
print(total)
print(type(total))
```

Poiché `var2` è un numero a virgola mobile, Python decide automaticamente, che anche il risultato deve essere un numero a virgola mobile. Ma ci sono casi in cui Python non sa quale tipo adottare. Per esempio   *


```python
varA = "hello 123"
varB = 456
print(varA + varB)
```

Quel codice provoca un errore, `varA` è una stringa e `varB` è un numero intero e Python non sa cosa fare. Tuttavia, possiamo forzare Python a convertire tra tipi   *


```python
varA = "hello"
varB = 123
print(varA + str(varB))
```

Ora che entrambe le variabili sono stringhe l\'operazione funziona. Nota che abbiamo \"stringificato\" `varB` al momento della stampa, ma non abbiamo modificato `varB` stesso. Se volessimo trasformare `varB` in modo permanente in una stringa, dovremmo farlo in questo modo   *


```python
varB = str(varB)
```

Possiamo anche usare `int()` e `float()` per convertire tra numeri interi e numeri a virgola mobile se vogliamo   *


```python
varA = "123"
print(int(varA))
print(float(varA))
```

Avrai notato che abbiamo usato il comando `print()` in diversi modi. Abbiamo stampato variabili, somme, diverse cose separate da virgole e persino il risultato di un altro comando Python. Forse hai anche notato che questi due comandi   *


```python
type(varA)
print(type(varA))
```

hanno lo stesso risultato. Questo perché siamo nell\'interprete e tutto viene stampato automaticamente. Quando scriviamo programmi più complessi, che vengono eseguiti al di fuori dell\'interprete, non verranno stampati automaticamente, quindi dovremo usare il comando `print()`. Tenendo questo presente, smetteremo di usarlo. D\'ora in poi scriveremo semplicemente   *


```python
myVar = "hello friends"
myVar
```


{{Top}}

## Liste

Un altro tipo di dati utile è la lista. Una lista è una raccolta di altri dati. Per definire una lista utilizziamo `[ ]`   *


```python
myList = [1, 2, 3]
type(myList)
myOtherList = ["Bart", "Frank", "Bob"]
myMixedList = ["hello", 345, 34.567]
```

Come puoi notare una lista può contenere qualsiasi tipo di dato. Puoi fare molte cose con una lista. Ad esempio, contare i suoi elementi   *


```python
len(myOtherList)
```

o recuperare un elemento   *


```python
myName = myOtherList[0]
myFriendsName = myOtherList[1]
```

Mentre il comando `len()` restituisce il numero totale di elementi in una lista, il primo elemento in una lista è sempre nella posizione `0`, quindi nella nostra `myOtherList` `"Bob"` sarà nella posizione `2`. Possiamo fare molto di più con le liste, come l\'ordinamento degli elementi e la rimozione o l\'aggiunta di elementi.

È interessante notare che una stringa di testo è molto simile a un elenco di caratteri in Python. Prova a fare questo   *


```python
myvar = "hello"
len(myvar)
myvar[2]
```

In genere tutto quello che si può fare con le liste si può fare anche con le stringhe. In effetti le liste e le stringhe sono entrambe delle sequenze.

Oltre a stringhe, numeri interi, numeri a virgola mobile e liste, ci sono altri tipi di dati incorporati, come i dizionari, e puoi persino creare i tuoi tipi di dati con le classi. {{Top}}

## Indentazione

Un uso importante delle liste è la possibilità di \"attraversarle\" e fare qualcosa con ogni loro elemento. Ad esempio, si noti quanto segue   *


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for dalton in alldaltons   *
    print(dalton + " Dalton")
```

In questo esempio, la lista viene iterata (nuovo gergo di programmazione!) con il comando `for in` e con ognuno dei suoi elementi viene eseguito qualcosa.

Notare la speciale sintassi. Il comando `for` termina con un `   *` questo indica a Python che ciò che segue è un blocco di uno o più comandi. Subito dopo che viene inserita la riga con il comando che termina con `   *`, il prompt dei comandi cambia in `...` il che significa che Python sa che c\'è dell\'altro in arrivo..

Come fa Python a sapere quante delle prossime righe devono essere eseguite all\'interno dell\'operazione `for in`? Per sapere questo, Python si basa sull\'indentazione. Le righe successive devono iniziare con uno spazio vuoto, o più spazi vuoti, o una tabulazione, o più tabulazioni. E finché l\'indentazione rimane la stessa, le righe saranno considerate parte del blocco `for in`. Se si inizia una riga con 2 spazi e la successiva con 4, darà un errore. Quando si finisce, scrivere un\'altra riga senza indentazione o premere **Enter** per uscire dal blocco `for in`.

L\'indentazione è molto utile anche per la leggibilità del programma. Se si usano rientri lunghi (ad esempio le tabulazioni invece degli spazi) quando si scrive un programma di grandi dimensioni, si avrà una visione chiara di ciò che viene eseguito all\'interno dei blocchi. Vedremo che anche altri comandi utilizzano blocchi di codice indentati.

Il comando `for in` può essere utilizzato per molte cose che devono essere eseguite più di una volta. Può, ad esempio, essere combinato con il comando `range()`   *


```python
serie = range(1, 11)
total = 0
print("sum")
for number in serie   *
    print(number)
    total = total + number
print("")
print(total)
```

Se è stato eseguito l\'esempio di codice in un interprete copiando e incollando, si noterà che il blocco di testo precedente genera un errore. Si copi invece fino alla fine del blocco rientrato, cioè alla fine della riga `total <nowiki>=</nowiki> total + number` e poi si incolli nell\'interprete. Quindi nell\'interprete si prema **Enter** fino a quando il prompt dei tre punti scompare e il codice viene eseguito. Infine, si copino le ultime due righe seguite da un altro **Enter**. Dovrebbe apparire la risposta finale.

Se si digita nell\'interprete `help(range)` si otterrà   *


```python
range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
```

Qui le parentesi quadre denotano un parametro opzionale. Tuttavia, tutti dovrebbero essere interi. Di seguito forzeremo il parametro step a essere un intero usando `int()`   *


```python
number = 1000
for i in range(0, 180 * number, int(0.5 * number))   *
    print(float(i) / number)
```

Un altro esempio con `range()`   *


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for n in range(4)   *
    print(alldaltons[n], " is Dalton number ", n)
```

Il comando `range()` ha la strana particolarità di iniziare con `0` (quando non si specifica il numero di partenza) e che il suo ultimo numero è uno in meno del numero finale specificato. Ciò, naturalmente, perché questo sistema funziona bene con gli altri comandi di Python. Ad esempio   *


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
total = len(alldaltons)
for n in range(total)   *
    print(alldaltons[n])
```

Un altro uso interessante dei blocchi indentati si ha con il comando `if`. Questo comando esegue un blocco di codice solo se una certa condizione è soddisfatta, ad esempio   *


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Joe" in alldaltons   *
    print("We found that Dalton!!!")
```

Naturalmente, questo esempio stampa sempre la prima frase, ma si provi a sostituire la seconda riga con   *


```python
if "Lucky" in alldaltons   *
```

Qui non viene stampato nulla. Possiamo anche specificare un\'istruzione `else`   *


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Lucky" in alldaltons   *
    print("We found that Dalton!!!")
else   *
    print("Such Dalton doesn't exist!")
```


{{Top}}

## Funzioni

I [comandi standard di Python](https   *//docs.python.org/3/reference/lexical_analysis.html#identifiers) non sono molti e ne conosciamo già alcuni di loro. Ma i comandi possono anche essere creati. In effetti, la maggior parte dei moduli aggiuntivi, che si possono inserire nella propria installazione di Python, fanno esattamente questo e aggiungono dei comandi, che si possono utilizzare. In Python un comando personalizzato si chiama funzione e si crea in questo modo   *


```python
def printsqm(myValue)   *
    print(str(myValue) + " square meters")

printsqm(45)
```

Il comando `def()` definisce una nuova funzione, le si assegna un nome e tra parentesi si definiscono gli argomenti, che la funzione utilizzerà. Gli argomenti sono dati, che verranno passati alla funzione. Ad esempio, si osservi il comando `len()`. Se si scrive semplicemente `len()`, Python dirà che ha bisogno di un argomento. Il che è ovvio   * vuoi conoscere la lunghezza di qualcosa. Se si scrive `len(myList)` allora `myList` è l\'argomento, che si passa alla funzione `len()`. E la funzione `len()` è definita in modo tale da sapere cosa fare con questo argomento. Abbiamo fatto la stessa cosa con la nostra funzione `printsqm`.

Il nome `myValue` può essere un qualsiasi oggetto e verrà utilizzato solo all\'interno della funzione. È solo un nome, che dai all\'argomento, in modo da poterci fare qualcosa. Definendo gli argomenti si deve anche dire alla funzione quanti aspettarsene. Ad esempio, se facendo quanto segue   *


```python
printsqm(45, 34)
```

si otterrà un errore. La nostra funzione è stata programmata per ricevere un solo argomento, ma ne ha ricevuti due, `45` e `34`. Proviamo un altro esempio   *


```python
def sum(val1, val2)   *
    total = val1 + val2
    return total

myTotal = sum(45, 34)
```

Qui abbiamo creato una funzione che riceve due argomenti, li somma e restituisce quel valore. Restituire qualcosa è molto utile, perché possiamo fare qualcosa con il risultato, come memorizzarlo nella variabile `myTotal`. {{Top}}

## Moduli

Ora che si ha una buona idea di come funziona Python, c\'è bisogno di sapere un\'altra cosa   * come lavorare con file e moduli.

Fino ad ora, abbiamo scritto le istruzioni Python riga per riga nell\'interprete. Questo metodo ovviamente non è adatto per programmi più grandi. Normalmente il codice per i programmi Python è memorizzato in file con estensione **.py**. Che sono solo semplici file di testo e qualsiasi editor di testo (Linux gedit, emacs, vi o persino Blocco note di Windows) può essere utilizzato per crearli e modificarli.

Esistono diversi modi per eseguire un programma Python. In Windows, fai semplicemente clic con il pulsante destro del mouse, aprilo con Python ed eseguilo. Ma puoi anche eseguirlo dall\'interprete Python stesso. Per questo, l\'interprete deve sapere dove si trova il tuo programma. In FreeCAD il modo più semplice è posizionare il programma in una cartella, che l\'interprete Python di FreeCAD conosce per impostazione predefinita, come la cartella utente **Mod** di FreeCAD   *

-   Su Linux è solitamente **/home/<username>/.local/share/FreeCAD/Mod/** ({{VersionPlus/it|0.20}}) o **/home/<username>/. FreeCAD/Mod/** ({{VersionMinus/it|0.19}}).
-   Su Windows è **%APPDATA%\FreeCAD\Mod\**, che di solito è **C   *Users\<username>\Appdata\Roaming\FreeCAD\Mod\**.
-   Su Mac OSX è solitamente **/Users/<username>/Library/Preferences/FreeCAD/Mod/**.

Aggiungiamo una sottocartella chiamata **scripts** e quindi scriviamo un file come questo   *


```python
def sum(a,b)   *
    return a + b

print("myTest.py succesfully loaded")
```

Salviamo il file come **myTest.py** nella cartella **scripts** e nella finestra dell\'interprete si scriva   *


```python
import myTest
```

senza l\'estensione **.py**. Questo eseguirà il contenuto del file, riga per riga, proprio come se lo avessimo scritto nell\'interprete. Verrà creata la funzione di somma e il messaggio verrà stampato. I file contenenti funzioni, come la nostra, sono chiamati moduli.

Quando scriviamo una funzione `sum()` nell\'interprete, la eseguiamo in questo modo   *


```python
sum(14, 45)
```

Ma quando importiamo un modulo contenente una funzione `sum()` la sintassi è leggermente diversa   *


```python
myTest.sum(14, 45)
```

Cioè, il modulo viene importato come un \"contenitore\" e tutte le sue funzioni sono all\'interno di quel contenitore. Questo è molto utile, perché possiamo importare molti moduli e mantenere tutto ben organizzato. Fondamentalmente quando vedi `something.somethingElse`, con un punto in mezzo, significa che `somethingElse` è all\'interno di `something`.

Possiamo anche importare la nostra funzione sum() direttamente nello spazio dell\'interprete principale   *


```python
from myTest import *
sum(12, 54)
```

Quasi tutti i moduli lo fanno   * definiscono funzioni, nuovi tipi di dati e classi, che puoi usare nell\'interprete o nei tuoi moduli Python, perché nulla impedisce di importare altri moduli all\'interno del tuo modulo!

Come facciamo a sapere quali moduli abbiamo, quali funzioni ci sono all\'interno e come usarli (ovvero, di che tipo di argomenti hanno bisogno)? Abbiamo già visto che Python ha una funzione `help()`. Facendo   *


```python
help("modules")
```

ci restituirà un elenco di tutti i moduli disponibili. Possiamo importarne uno qualsiasi e sfogliarne il contenuto con il comando `dir()`   *


```python
import math
dir(math)
```

Vedremo tutte le funzioni contenute nel modulo `math`, oltre a cose strane denominate `__doc__`, `__file__`, `__name__`. Ogni funzione in un modulo ben fatto ha un `__doc__` che spiega come usarla. Ad esempio, vediamo che c\'è una funzione `sin()` all\'interno del modulo matematico. Vuoi sapere come usarlo? 
```python
print(math.sin.__doc__)
```

(Potrebbe non essere evidente, ma su entrambi i lati del `doc` ci sono due caratteri di sottolineatura.)

E infine un ultimo consiglio   * quando si lavora su del codice nuovo o esistente, è meglio non utilizzare l\'estensione del file macro di FreeCAD, **.FCMacro**, ma utilizzare invece l\'estensione standard **.py**. Questo perché Python non riconosce l\'estensione **.FCMacro**. Se usi **.py** il tuo codice può essere facilmente caricato con `import`, come abbiamo già visto, e anche ricaricato con `importlib.reload()`   *


```python
import importlib
importlib.reload(myTest)
```

C\'è comunque un\'alternativa   *


```python
exec(open("C   */PathToMyMacro/myMacro.FCMacro").read())
```


{{Top}}

## Iniziare con FreeCAD 

Spero che ora tu ti sia fatto una buona idea di come funziona Python e che tu possa iniziare a esplorare ciò che FreeCAD ha da offrire. Le funzioni Python di FreeCAD sono tutte ben organizzate in diversi moduli. Alcuni di essi sono già caricati (importati) all\'avvio di FreeCAD. Prova   *


```python
dir()
```


{{Top}}

## Note

-   FreeCAD è stato originariamente progettato per funzionare con Python 2. Poiché Python 2 ha raggiunto la fine del suo ciclo di vita nel 2020, lo sviluppo futuro di FreeCAD sarà effettuato esclusivamente con Python 3 e la compatibilità con le versioni precedenti non sarà supportata.
-   Molte più informazioni su Python possono essere trovate nel [tutorial ufficiale di Python](https   *//docs.python.org/3/tutorial/index.html) e nel [manuale di riferimento ufficiale di Python](https   *//docs.python.org/3/reference/).


{{Top}}







[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Introduction to Python/it
