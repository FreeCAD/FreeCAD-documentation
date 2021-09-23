# Crowdin Scripts/it
{{TOCright}}

## Gestire le traduzioni per FreeCAD 

Per gestire le traduzioni FreeCAD utilizza un servizio di traduzione di terzi chiamato [Crowdin](https://crowdin.com/project/freecad).

In FreeCAD/src/Tools ci sono 3 script che sono usati per gestire i file di traduzione:

1.  updatets.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatets.py)
2.  updatecrowdin.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatecrowdin.py)
3.  updatefromcrowdin.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatefromcrowdin.py)

### Note

-   Questi script vengono eseguiti dalla radice della directory FreeCAD/.
-   Affinché questi script funzionino, è necessario che la chiave API Crowdin di FreeCAD sia inserita nel loro file ~/.crowdin-freecad. (Per motivi di sicurezza, disponibile solo per le persone con diritti di amministratore sul progetto FreeCAD)
-   Attualmente questi strumenti sono compatibili con Python2.

### updatets.py

Lo script updatets.py crea i file .ts nella directory locale FreeCAD/. Genera i file .ts (Qt Translation Source File).

Viene invocato con: python2 updatets.py

### updatecrowdin.py

Lo script updatecrowdin.py trasferisce le modifiche dalla directory locale FreeCAD/ a Crowdin (Servizio di traduzione crowdsource di traduzione di terze parti). Lo script attualmente supporta 4 argomenti:

-   updatecrowdin.py status stampa uno stato delle traduzioni
-   updatecrowdin.py update aggiorna Crowdin alla versione corrente dei file .ts trovati nel codice sorgente
-   updatecrowdin.py build crea un nuovo pacchetto scaricabile su crowdin con tutte le stringhe tradotte
-   updatecrowdin.py download scarica l\'ultima versione

### updatefromcrowdin.py

Lo script updatefromcrowdin.py estrae le modifiche da crowdin alla directory locale FreeCAD/.

## Inviare le stringhe più recenti a crowdin 

-   Testato solo su Linux
-   È necessario un file .credentials nella propria directory /home/YourUser. Questo file è un semplice file di testo contenente solo una riga, che è la chiave API che si trova su <https://crowdin.com/project/freecad/settings#api> (solo per gli amministratori)
-   Accertarsi che il proprio repository sia pulito (git pull, git stash se necessario)
-   cd /path/to/freecad-source-code/src/Tools
-   python updatets.py (riempie tutti i file .ts trovati nella sorgente con le stringhe più recenti)
-   python updatecrowdin.py update (invia i file ts a crowdin. Crowdin aggiorna solo le stringhe che sono nuove)
-   cd ../.. (torna alla cartella radice del codice sorgente)
-   git checkout . (annulla tutte le modifiche ai file .ts, non c\'è motivo di convalidarli in questo momento in quanto non sono ancora stati tradotti)

## Unire le ultime traduzioni da crowdin 

-   Testato solo su Linux
-   È necessario un file .credentials nella propria directory /home/YourUser. Questo file è un semplice file di testo contenente solo una riga, che è la chiave API che si trova su <https://crowdin.com/project/freecad/settings#api> (solo per gli amministratori)
-   Accertarsi che il proprio repository sia pulito (git pull, git stash se necessario)
-   cd /path/to/freecad-source-code/src/Tools
-   python updatecrowdin.py build (crea un file zip nel sito di crowdin con tutti i file, può richiedere un po \'di tempo. Questo passaggio può essere fatto anche sul sito Web di crowdin)
-   python updatecrowdin.py download (scarica un file freecad.zip in questa directory)
-   mv freecad.zip \~ sposta il file zip nella vostra directory home, per evitare un commit accidentalmente in seguito)
-   (optionale) edita lo updatefromcrowdin.py script e controlla che le default\_languages contengano tutte le lingue che si vuole (in pratica tutte quelle che superano il 50% di traduzione)
-   python updatefromcrowdin.py -z /home/YourUser/freecad.zip
-   cd ../.. (torna alla cartella radice del codice sorgente)
-   Se qualcosa è andato storto o non si è sicuri, pulire tutto con il git checkout.
-   Se tutto sembra ok (git status), convalidare con git add . && git commit
-   Creare un PR su FreeCAD

## Generare un file di traduzione dal sito Web 

-   Clonare il repository della home page
-   cd /path/to/FreeCAD-homepage
-   xgettext \--from-code=UTF-8 -o lang/homepage.pot \*.php
-   Aggiornare la \"homepage.po\" sul sito Web di crowdin manualmente, utilizzando il file lang/homepage.pot

## Aggiornare le traduzioni del sito web 

-   Scaricare il file freecad.zip dal sito Web crowdin o seguendo le istruzioni sopra (python updatecrowdin.py download)
-   cd /path/to/FreeCAD-homepage
-   Accertarsi che il proprio repository sia pulito (git pull, git stash se necessario)
-   python updatefromcrowdin.py -z /path/to/freecad.zip
-   Se qualcosa è andato storto o non si è sicuri, pulire tutto con il git checkout.
-   Se tutto sembra ok (git status), convalidare con git add . && git commit
-   Creare un PR su FreeCAD-Homepage
-   Dopo la fusione del PR, uno degli amministratori manda un ftp al webhost

## Relazioni

-   [Localizzazione](Localisation/it.md)
-   [Crowdin Administration](Crowdin_Administration/it.md)
-   [Release process](Release_process/it.md)




[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Administration](Category:Administration.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Crowdin Scripts/it
