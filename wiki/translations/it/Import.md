# Import/Export IFC - compiling IfcOpenShell/it
<div class="mw-translate-fuzzy">


{{TutorialInfo/it
|Topic=Arch
|Level=Avanzato
|Time=120 minuti
|Author=Pablo Gil
|FCVersion=
|Files=
}}


</div>

## Introduzione

Dato che mi è stato molto difficile scoprire come fare per avere una copia di IfcOpenShell-python operante su OSX / MacOS per importare e esportare i file IFC condivido questo tutorial che può essere di aiuto ad altri. Il mio sistema è OSX 10.11.6, 64bit con Python 2.7.11, e questo dovrebbe funzionare per quelli che hanno anche un OSX in quanto sono spesso a 64bit, ma che possono essere diversi dal mio. Se si esegue Linux o Windows, la procedura potrebbe essere molto simile, ma probabilmente ci sono alcune differenze.

## Requirements

-   [IfcOpenShell](IfcOpenShell.md)
-   FreeCAD v0.19 or higher


<div class="mw-translate-fuzzy">

## Passaggi

1\. Scaricare o clonare l\'intero progetto GitHub da <https://github.com/IfcOpenShell/IfcOpenShell> (sarà sempre l\'ultima versione)


</div>


<div class="mw-translate-fuzzy">

2\. Da un terminale andare nella cartella **/nix/** e lanciare lo script. In OSX si può fare con: 
```python
./build-all.sh
``` Ci vorranno da 30 fino a 120 minuti per compilare tutto. Non è il modo più intelligente di compilare IfcOpenShell ma questo semplice script compila tutte le dipendenze, le versioni di Python, etc.


</div>


<div class="mw-translate-fuzzy">

3\. Una volta completato (viene stampato qualcosa di simile a \"Built IfcOpenShell\...\" e torna al prompt) si ha una nuova cartella **/IfcOpenShell/build/** piena di file e cartelle. Dalla mia esperienza personale, tempo fa lo script nix \"build-all.sh\" non si è concluso con successo, ma dopo, con gli aggiornamenti più recenti, ha funzionato bene, quindi penso che potrebbe capitare qualcosa di simile nel caso in cui lo sviluppo vada avanti. .. In questo modo. ora c\'è tutto il necessario, ma si deve fare un certo lavoro manuale per farlo funzionare: 4. Aprire FreeCAD, aprire la console Python e la Vista Report. Quindi scrivere nella console Python quanto segue: 
```python
import sys
print sys.path
``` Si ottiene una lunga lista con tutti i percorsi che sono letti da FreeCAD. Si può installare ifcopenshell in qualsiasi di essi, ma consiglio di posizionarlo all\'interno di quello in cui si trova un **/site-packages/** dopo un **/Python/** o **/python-something/**. Nel mio caso è stato */Library/Python/2.7/site-packages*. (trovate i percorsi all\'interno della vostra cartella app ma vi suggerisco di non utilizzarlo perché altrimenti dopo IfcOpenShell sarà disponibile solo per questa applicazione)


</div>

4\. Open FreeCAD and open the [Python console](Python_console.md) and [Report view](Report_view.md). Then write into the Python console the following: 
```python
import sys
print sys.path
``` You will get a looooong line with all the paths that FreeCAD reads. You may be able to install IfcOpenShell in any of them but I suggest you to place it inside one where you find a {{FileName|/site-packages/}} after a {{FileName|/Python/}} or {{FileName|/python-something/}}. In my case it was {{FileName|/Library/Python/2.7/site-packages}}. (Note: you will find paths inside your app directory but I suggest you to not use them because then IfcOpenShell will only be available for this app)


<div class="mw-translate-fuzzy">

5\. Quindi, una volta che si trova nel posto in cui si desidera che sia installato, andare lì con l\'esploratore dei file (Finder in OSX). Cioè, andare nella cartella **/site-packages/**


</div>

6\. Aprire una nuova finestra del browser dei file e navigare nel progetto GitHub scaricato: **/IfcOpenShell/src/ifcopenshell-python/** e copiare l\'intera cartella **/ifcopenshell/**

7\. Incollarla all\'interno della cartella **/site-packages/**. Ora si dovrebbe avere qualcosa di simile a: 
```python
/site-packages/ifcopenshell/__init__.py
/site-packages/ifcopenshell/entity_instance.py
/site-packages/ifcopenshell/file.py
/site-packages/ifcopenshell/geom/app.py
/site-packages/ifcopenshell/geom/main.py
/site-packages/ifcopenshell/geom/occ_utils.py
/site-packages/ifcopenshell/geom/__init__.py
/site-packages/ifcopenshell/guid.py
```


<div class="mw-translate-fuzzy">

8\. Ora dobbiamo trovare due file all\'interno della cartella /build/ , essi sono: 
```python
_ifcopenshell_wrapper.so
ifcopenshell_wrapper.py
``` ma dato che abbiamo compilato ogni cosa, si dovrà scegliere quelli che corrispondono alla versione di Python usata da FreeCAD. È facile controllare leggendo la prima riga all\'interno della console Python di FreeCAD. Nel mio caso è stato Python 2.7.11.


</div>

9\. Ora copiare i file che si trovano all\'interno del percorso corrispondente alla propria versione di Python. Nel mio caso: 
```python
/IfcOpenShell/build/Darwin/x86_64/build/ifcopenshell/[b]python-2.7[/b].10/ifcwrap/
```


<div class="mw-translate-fuzzy">

10\. Incollarli all\'interno di /site-packages/ifcopenshell/


</div>

11\. Controllare se tutto è a posto: 
```python
/site-packages/ifcopenshell/__init__.py                  (1)
/site-packages/ifcopenshell/entity_instance.py           (1)
/site-packages/ifcopenshell/_ifcopenshell_wrapper.so     (2)
/site-packages/ifcopenshell/file.py                      (1)
/site-packages/ifcopenshell/geom/__init__.py             (1)
/site-packages/ifcopenshell/geom/app.py                  (1)
/site-packages/ifcopenshell/geom/main.py                 (1)
/site-packages/ifcopenshell/geom/occ_utils.py            (1)
/site-packages/ifcopenshell/guid.py                      (1)
/site-packages/ifcopenshell/ifcopenshell_wrapper.py      (2)
```

\(1\) dal progetto GitHub
(2) dalla cartella /build/

12\. Chiudere e riaprire FreeCAD

## Test

Ora che è installato, controlliamo se tutto funziona come previsto:

12.1 nella console Python scrivere: 
```python
import ifcopenshell
from ifcopenshell import geom
``` se non si genera alcun errore significa che dovrebbe essere installato correttamente


<div class="mw-translate-fuzzy">

12.2 Andare nel Manuale FreeCAD di Yorik, a fondo pagina e scaricare i seguenti file per fare un test: 
```python
house.FCStd
house.ifc
```


</div>


<div class="mw-translate-fuzzy">

12.3 Aprire **house.FCStd**, nella directory principale selezionare l\'oggetto \"Building\" e esportarlo (menu File/esporta/) impostare il tipo di file \"Industry Foundation Classes (\*.ifc)\". Premere il tasto \"Salva\" e se funziona e non genera nessun errore nel Rapporto, allora sta funzionando


</div>


<div class="mw-translate-fuzzy">

12.4 Prova finale, importare **house.ifc** in un nuovo file in modo da aprire un nuovo file e importare il file \... ci vorrà un po\'.


</div>

13\. Godetevi BIM con FreeCAD!

## Pensieri finali 

La mia opinione è che FreeCAD stesso dovrebbe avere una versione di IfcOpenShell precompilata in impacchettata con la distribuzione in quanto costruirlo da soli è una tortura e utente medio non lo farà mai (non sa come compilare, gestire GitHub, ecc), ma forse in futuro ci sarà.

Spero che questo sia di aiuto.

Cheers


<div class="mw-translate-fuzzy">

## Link

La discussione nel Forum [qui](http://forum.freecadweb.org/viewtopic.php?f=23&t=17536)


</div>

-   Related forum thread [discussion](http://forum.freecadweb.org/viewtopic.php?f=23&t=17536)
-   [IfcOpenShell](IfcOpenShell.md)




_ _ _ _

---
[documentation index](../README.md) > [BIM](Category_BIM.md) > Import/Export IFC - compiling IfcOpenShell/it
