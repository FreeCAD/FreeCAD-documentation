# Macro FCInfo/it
<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Macro FCInfo
|Translate=Infoin scheda
|Icon=FCInfo.png
|Description=Fornisce una ampia serie di informazioni sulla forma selezionata.<br />FRench Version [https   *//gist.githubusercontent.com/mario52a/6afc64081c4eb8be3b93/raw/c1dd823886fe2e75dc5c6dd490157c259051b651/FCInfo_fr_Ver_1-22-rmu_Docked.FCMacro]
|Author=Mario52
|Version=1.22
|Date=2020/11/12
|FCVersion=Tutte
|Download=Tele-carica il zip file [https   *//forum.freecadweb.org/download/file.php?id=50755 Macro_FCInfo_Icon] e copia le imagine nello stesso repertorio ché la macro.
|SeeAlso=[Arch Survey|<img src=images/Arch_Survey.svg style="width   *24px"> [Arch Survey](Arch_Survey/it.md)<br />[Macro SimpleProperties](Macro_SimpleProperties/it.md)
}}


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Fornisce una ampia serie di informazioni sulla forma selezionata quali lunghezza, angoli, superficie, inclinazione, volume e peso secondo la densità della forma selezionata, sia nelle unità del Sistema Internazionale che in quelle del Sistema Anglosassone.


</div>


{{Codeextralink|https   *//gist.githubusercontent.com/mario52a/8d40ab6c018c2bde678f/raw/4ecf1b82162b7a9e600c9ee511410ddf06c6e534/FCInfo_en_Ver_1-25d-rmu_Docked.FCMacro}}

<img alt="FCInfo" src=images/Macro_FCInfo_00_en.png  style="width   *480px;"> 
*FCInfo*

## Utilisation


<div class="mw-translate-fuzzy">

## Utilizzo

Selezionare un oggetto e avviare l\'applicazione o viceversa. Viene visualizzata la tabella delle informazioni. I calcoli sono basati sull\'unità di FreeCAD, che è il **mm**. Ogni nuova selezione ripristina il **mm** per l\'unità di lunghezza e i **gradi sessadecimali** (**°**) per gli angoli. <img alt="upper window" src=images/Macro_FCInfo_06.png  style="width   *200px;"><img alt="lower window" src=images/Macro_FCInfo_07.png  style="width   *200px;">


</div>




**Settore 1   * Documento**

-   Nome del documento
-   Etichetta dell\'oggetto
-   Nome interno dell\'oggetto
-   Nome dei sottoelementi dell\'oggetto
-   Tipo di oggetto


<div class="mw-translate-fuzzy">

**Settore 2   * Coordinate del clic mouse**

-   Coordinate X,Y e Z del punto cliccato con il mouse
-   Il bottone crea un punto, asso, piano, copia dei vettori su la forma **FreeCAD.Vector(-24.0, 240.0, 7.0)**


</div>


<div class="mw-translate-fuzzy">

**Settore 3   * Value**

-   Lunghezza dell\'oggetto, se l\'oggetto è una faccia viene visualizzato il perimetro. Si può scegliere l\'unità di misura    *
    km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.
-   Perimetro della forma (lunghezza di tutti i bordi).


</div>


<div class="mw-translate-fuzzy">

**Settore 4   * Vertexes and details**

-   CheckBox per attivare la funzione spreadSheet ché prende molto tempo a ogni clic mouse con uno obietto complicato perché la ricerca dei completi dati si fa a ogni clic mouse.
-   Vertici e dettagli della forma (compt\_Edge), (compt\_Faces), (compt\_Vector of the Face)
    la tabella contiene al massimo 200 righe, se ci sono più di 200 righe appare (!+ 200) e il numero di righe
    (tutti i dettagli possono essere salvati con il pulsante **Save** in un file in formato CSV e possono essere visualizzati nel foglio di calcolo con **Read** o da un foglio esterno come [LibreOffice](https   *//www.libreoffice.org/) [OpenOffice](http   *//openoffice.apache.org/downloads.html) o altri)


</div>


<div class="mw-translate-fuzzy">

**Settore 5   * Inclination**

-   Inclinazione dell\'oggetto che può essere visualizzata in   *
-   **gradi decimali**, ex   * 174.831872611°
-   **gradi minuti secondi**, ex   * 174° 49\' 54.741401\'\'
-   **radianti**, ex   * 3.05139181449 rad
-   **gradi gon**, ex   * 194.257636235 gon
-   **percentuale** ex   * 30° = 57.74% \*Inclinazione nei piani XY, YZ, ZX e loro coordinate

-   Inclinazione su i piani XY, YZ, ZX é le loro coordinate
-   **Direction object**, calcola la direzione del obietto, il calcolo si fa    * coord\_1 - coord\_2 = direzione (o reverse)
    -   
        **Line**
        
        , questo pulsante crea una linea con la direzione del obietto.
-   **ValueAt**, ritorna il 3D vector corrispondente ai parametri Value.


</div>


<div class="mw-translate-fuzzy">

**Settore 6   * Surface and Volume**

-   Superficie della forma visualizzata. Si può scegliere l\'unità di misura
-   Superficie della faccia visualizzata. Si può scegliere l\'unità di misura
-   Volume della forma con l\'unita scelta
-   density of the material in **kg by dm3**
    (lo \"spinBox\" e regolato a **1,0** kg. Se volette cambiare il valore modificate il valore della linea 230)
-   Il bottone **gram** e l\'unita di massa a schegliere    *
    ton,quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
    lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct
-   weight of the form il peso del obietto con la densità e unita scelti.


</div>


<div class="mw-translate-fuzzy">

**Settore 7   * BoundBox**

-   BoundBox, dimensioni estreme della forma


</div>


<div class="mw-translate-fuzzy">

**Settore 8   * Center of   ***

-   Centro della forma e le sue coordinate XYZ
-   Centro di massa e sue coordinate XYZ
-   Il bottone crea un punto, asso, piano, copia dei vettori su la forma **FreeCAD.Vector(-24.0, 240.0, 7.0)**


</div>


<div class="mw-translate-fuzzy">

**Settore 9   * Inertia**

-   Momento di inerzia e le sue coordinate, calcolo su lunghezza et peso
-   Il bottone crea un punto, asso, piano, copia dei vettori su la forma **FreeCAD.Vector(-24.0, 240.0, 7.0)**
    -   action line 1    * x1, y1, z1
    -   action line 2    * x2, y2, z2
    -   action line 3    * x3, y3, z3
    -   action 4 diagonal    * x1, y2, z3

stesso per lunghezza e peso

-   Determinant 1    * calcola il determinanti della matrizza scientific value
-   Determinant 2    * calcola il determinanti della matrizza decimala value


</div>

**Section 10   * SpreadSheet**

-    **Read**   * Apre un file **.FCInfo**

-    **Save**   * Salva un file **.FCInfo**

-    **Tabulation**   * il separatore e una Tabulation

-    **Comma**   * il separatore e una Virgola

-    **Semicolon**   * il separatore e un Punto virgola

-    **Space**   * il separatore e uno Spaccio


<div class="mw-translate-fuzzy">

L\'opzione per salvare e leggere lo spreadsheet con differenti separatori, Tabulazioni, Virgola, Punto virgola, Spazzio
La Tabulazione e il separatore dello spreadsheet di FreeCAD
Il numero di separatori e calcolato per dare una potenziale informazione di chi sarebbe il separatore dentro il filo aperto.
La virgola e il separatore delle versione anteriore de FCInfo (01.16 e inferiore)
Adesso (versione 01.17 e più) il separatore per difetto e la tabulazione
Se volete convertire le vecchie fili di FCInfo, caricate il file con il separatore del file e salvatelo con la casella Tabulazione selezionata.


</div>


<div class="mw-translate-fuzzy">

**Section 11   * Main**

-    **CheckBox Clip Board**   * se questa casella e validata le coordinate sono salvate in memoria di forma    * **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    **CheckBox Point**   * se questa casella e validata uno punto e creato alle coordinate visualizzate.

-    **CheckBox Axis **   * se questa casella e validata uno asso XYZ e creato alle coordinate visualizzate.

-    **CheckBox Plane**   * se questa casella e validata uno piano XYZ e creato alle coordinate visualizzate.

-    **Ref**   * Raffresca la vista rapporto.

-    **Exit**   * Esce della macro. La macro resta in memoria (per riavviare con il pulsante della barra degli strumenti o dal menu \"Visualizza → Pannelli → FCInfo\").

-    **CheckBox****1**    * se questa casella e validata le informazione sono visualizzati dentro la vita report.

-    **CheckBox****2**    * se questa casella e validata la finestra si mette a la sinistra della vista 3D. (Difetto non validata la finestra e a destra)


</div>

Una volta lanciata, la macro rimane attiva e la finestra rimane visibile. Per chiudere la macro si deve usare il pulsante **Exit**. Se si esce tramite il pulsante con la croce, la macro rimane in memoria ed i dati vengono visualizzati nel report di FreeCAD.


<div class="mw-translate-fuzzy">


<center>

Image   *Macro\_FCInfo\_04.png\|La tabella dei dati può essere dislocata a destra, Image   *Macro FCInfo 05.png\|o a sinistra con Vista combinata , o non dislocata, a piacere.


</center>





</div>

## Options


<div class="mw-translate-fuzzy">

## Opzioni

### Unità di misura utilizzate 

#### Lunghezza    *

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.


</div>

#### Length unit   * 

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.

#### Angle degrees    * 


<div class="mw-translate-fuzzy">

#### Angoli   *

1.  **gradi sessadecimali**, esempio   * 174.831872611°
2.  sessagesimali gradi primi secondi, es   * 174° 49\' 54.741401\'\'
3.  radianti, es   * 3.05139181449 rad
4.  centesimali, es   * 194.257636235 gon
5.  pendenza %, es   * 30° = 57.74%


</div>

Visualizzazione degli angoli in FCInfo.


<center>

Image   *Macro FCInfo 02.png\|Visualizzazione degli angoli in FCInfo. Image   *Macro FCInfo 03.gif\|Visualizzazione della pendenza in FCInfo.
Clicca due volte sopra l\'immagine per vedere l\'animazione (l\'immagine deve essere in pieno schermo per vedere l\'animazione)


</center>




#### Weight unit    * 


<div class="mw-translate-fuzzy">

#### Peso   *

tonne, quintal, kg, hg, dag, **grammo**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy), lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct
Il valore della massa volumica è preimpostato su **7,5** kg/dm3, che è la densità media dell\'acciaio. Per impostare un valore predefinito diverso, modificare il valore della densità nella riga 208   *


</div>


```python
 global densite       ; densite       = 7.5  # (steel = 7.5 kg par dm3)
```


<div class="mw-translate-fuzzy">

Tramite il pulsante **Save** è possibile archiviare i dati ottenuti in un file di tipo [csv](https   *//it.wikipedia.org/wiki/Comma-separated_values) e utilizzarli in una tabella dentro FreeCAD o [OpenOffice](http   *//www.openoffice.org/it/), [LibreOffice](https   *//it.libreoffice.org/) \...


</div>


<div class="mw-translate-fuzzy">

## Script

Copiare il contenuto della macro in un file chiamato \"FCInfo.FCMacro\"

-   Windows   * di solito \"C   *Utenti\\nome\_utente\\AppData\\Roaming\\FreeCAD\\ \"

-   Ubuntu   * di solito \"/home/nome\_utente/.FreeCAD\".

Oppure, direttamente nell\'interfaccia di FreeCAD

L\'icona deve essere nella stessa directory della macro.

Scaricare l\'immagine posizionando il puntatore sull\'icona <img alt="" src=images/FCInfo.png  style="width   *64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width   *64px;"> e poi fare clic destro e selezionare \"Salva come\" (senza cambiare il nome).


</div>

Copy the contents of the macro in a file named \"FCInfo.FCMacro\"

-   Windows   * the form is usually **\" drive   *Users\\your\_user\_name\\AppData\\Roaming\\FreeCAD\\ \"**
-   Ubuntu   * the form is usually **\" /home/your\_user\_name/.FreeCAD \"**.

Or, directly in the interface of FreeCAD
The icon must be in the same directory as the macro.
Download image positioning on the icon <img alt="" src=images/FCInfo.png  style="width   *64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width   *64px;"> and then drag the mouse right click \"save as\" (do not change the name)


<div class="mw-translate-fuzzy">

Dato che, per il momento, le pagine wiki accettano solo 64 KB e il file della macro è più grande, il suo codice è stato inserito nel forum.


</div>


<div class="toccolours mw-collapsible mw-collapsed">

There is also FCInfo\_Alternate\_Linux for only for FreeCAD version 0.13\... and PyQt4


<div class="mw-collapsible-content">


<div class="mw-translate-fuzzy">

There is also a [Macro\_FCInfo\_Alternate\_Linux](http   *//www.freecadweb.org/wiki/index.php?title=Macro_FCInfo_Alternate_Linux) here the code is changed (due to the character display error    * **² ³ ° μ** ordinal not in range (128)\") which posed problems in certain configurations the functions are the same
Example    * 
```python
global uniteSs       ; uniteSs       = u"mm²"
global uniteVs       ; uniteVs       = u"mm³"
global uniteAs       ; uniteAs       = u"°"
``` remplacés par 
```python
global uniteSs       ; uniteSs       = "mm"+iso8859(unichr(178))
global uniteVs       ; uniteVs       = "mm"+iso8859(unichr(179))
global uniteAs       ; uniteAs       = iso8859(unichr(176))
``` **Files saved with this version is incompatible with the other version (docked or not)**


</div>


</div>



</div>

Carisa il file contenente le icon della macro [Macro\_FCInfo\_Icon](https   *//forum.freecadweb.org/download/file.php?id=50755) unzip e copia li fili dentro lo steso repertorio che la macro.


<div class="mw-translate-fuzzy">

Scaricare il file **docked to right** [FCInfo\_en\_Ver\_latest\_Docked.FCMacro](https   *//gist.github.com/mario52a/8d40ab6c018c2bde678f). PySide


</div>


<div class="mw-translate-fuzzy">


{{CodeDownload|https   *//gist.github.com/mario52a/8d40ab6c018c2bde678f|Ultima versione di Macro_FCInfo}}


</div>


<div class="mw-translate-fuzzy">

Oppure scaricare **[Dal forum.](http   *//forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=47748#p47748)**
**PS   *** Questa macro utilizza il comando **getSelection()** e la lista degli oggetti comincia da 1 ex   * per uno cubo **Edge1 to Edge12** e il codice dentro la console Python comincia da 0 ex   * per uno cubo **Edge\[0\] fino Edge\[11\]**
Questo è normale il contatore della lista dentro OpenCascade comincia sempre da **1 e non da 0**


</div>

### Limitations


<div class="mw-translate-fuzzy">

### Limitazioni

Uscire sempre dalla macro tramite il pulsante **Exit**, altrimenti il programma rimane in memoria e continua a funzionare fino a quando non si chiude FreeCAD.

La tabella riporta solo i primi 200 elementi dell\'oggetto, quando l\'oggetto contiene più di 200 elementi viene visualizzato l\'avviso **(! +200)**. In questo caso, l\'elenco completo dei dati è visibile nel file csv che può essere creato e salvato cliccando sul pulsante {{KEY/it|Save}}.


</div>


<div class="mw-translate-fuzzy">

Se dopo avere lanciato la macro la macro non e visibile, guardate a la base della finestra.


</div>

![](images/Macro_FCInfo_08.png )

![](images/FCInfo_begin_00.gif ) 


<div class="mw-translate-fuzzy">

**In progetto    ***

~~leggere i dati direttamente in una tabella.~~ fatto

~~mappare dgli spigoli (\"Edges\") e le loro coordinate~~ fatto

associare una sostanza alla sua massa volumica

~~angoli di inclinazione riferiti all\'elemento piuttosto che all\'oggetto globale~~ fatto

~~alloggiamento a destra nell\'interfaccia di FreeCAD~~ fatto


</div>

## Versione


<div class="mw-translate-fuzzy">

-   ver 1.22 , 12/11/2020    * adesso la macro si disinstallare totalmente utilizzo    *


</div>


```python
FreeCAD.ActiveDocument.openTransaction(u"FCInfo")    # memorise les actions (avec annuler restore)
FreeCAD.ActiveDocument.commitTransaction()           # restore les actions  (avec annuler restore)
#FreeCAD.ActiveDocument.abortTransaction()            # abandonne les actions(avec annuler restore)
```

-   ver 1.25d, 13/12/2021 little correction material field uncomment the \"\'try\...Except\" !!!
-   ver 1.25c, 12/12/2021 little correction new material
-   ver 1.23b, 20/11/2021 little correction, add text info in beginning run macro, and ordinal the text code
-   ver 1.23 , 19/11/2021 include icon in macro, number decimal displayed, text height, configure options in the Preference FC, correct info for elements of sketch in edit mode.
-   ver 1.22 , 12/11/2020    * now the macro is totally uninstalled i use    *


```python
try   *
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)    # destroy
        self.window.deleteLater()                                     # destroy
        self.window.destroy()                                         # destroy
except Exception   *
        None
```

[How do i exit from FreeCAD instead of Python?](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=48013#p411508)

instead   * 
```python
self.window.hide()
``` e aggiungendo la possibilità di visualizzare o meno la finestra \"Error Message\" \"Falso\" per impostazione predefinita, se si attiva la finestra di avviso vai a 
```python
FreeCAD >Menu >Tools >Edit parameters... >BaseApp/Preferences/Macros/FCMmacros/FCInfo > switchWarning
```

-   ver 1.21-3.01 , 07/11/2019 \# 07/11/2019 ver \"01.21-3-rmu\" replace character micro = \"U\", square = \"2\", cube = \"3\", degrees = \" deg\" see \"<https   *//forum.freecadweb.org/viewtopic.php?f=3&t=6005&start=70#p345819>\"

-   ver 1.21-2.01 (1.21-rmu) 11/06/2019 rmu replace all characters over 127 in ex   * \"°\" in chr(176)) \#degree

ver 1.21.01 (1.21-rmu) 30/05/2019 rmu change fixed positions to qt layouts grid.addWidget() by rmu75 see the rmu75 fork \"<https   *//gist.github.com/rmu75/b165147bd1c2f2659c014103793ae1d8>\"

ver 1.21 , 16/04/2019 optimization for Py 3\... Qt 5\... FreeCAD 0.15 to 0.19 release

ver 1.20 , 29/01/2018 optimization

ver 1.19 , 20/01/2018 create checkBox for use detection all elements of the object if wanted or not , the macro is faster. Optimisation

ver 1.18 , 19/12/2017 \...

ver 1.17c , 14/12/2017 create plane with coordinate give in one project in other project and replace \"FCInfo\" by \"\_\_title\_\_\"

ver 1.17b , 13/12/2017 little correction replace FCTreeView to FCInfo

ver 1.17 , 12/12/2017 add upgrade Moment of inertia mm and kg by pinq [FCMacro and moment of inertia of assembly](https   *//forum.freecadweb.org/viewtopic.php?t=23888), and create plane, axis, point, and add options separator for spreadsheet

ver 1.16 , 21/06/2017 aggiunto controllo della altezza della pollice (qui PointSize 8), casella di posizione della finestra della macro sinistra o destra e nuovo sistema di ricerca del imposta mento delle macro
ver 1.15 , 19/12/2015 soppressione PyQt4 option [see](http   *//forum.freecadweb.org/viewtopic.php?f=12&t=13541) , add checkBox for editing infos in report view
ver 1.14 , 04/08/2014 PyQt4 and PySide, corretto tooltip che non funzionava con PySide, aggiunto \"fg\"

ver 1.13 , 27/07/2014 sostituzione FCInfo\_en\_Ver\_1-12\_Docked.FCMacro con FCInfo\_en\_Ver\_1-13\_Docked.FCMacro accetta PyQt4 and PySide

ver 1.12 , 10/03/2014 aggiunto tooltip sopra i pulsanti

ver 1.11 , 04/03/2014 aggiunto µm, nm, pm, fm, µg, ng, pg, percento, correzione dell\'errore carat ~~\"cd\"~~ con **\"ct\"**, visualizzazione dell\'etichetta e del nome interno, correzione del calcolo degli angoli XY YZ ZX, funzionava bene su un oggetto semplice, ma ha dato un valore sbagliato su un pezzo composto (ha preso altre coordinate ! scoperto confrontando la tabella e le coordinate visualizzate nella sezione inclinazioni), finestra mobile o ancorabile in qualsiasi parte della GUI di FreeCAD
ver 1.10.b, 19/11/2013 pulsanti esterni alla scrollbar e bloccaggio delle dimensioni della finestra

ver 1.10 , 18/11/2013 agggiunto una scrollbar per diminuire la dimensione della finestra

ver 1.08.b 10/10/2013 correzione dell\'errore di superficie delle facce elencati nella tabella e sostituzione di \"**print**\" con \"**App.Console.PrintMessage**\"

~~ver 1.09 , 04/11/2013 funziona perfettamente su Windows e Linux (causa dell\'errore i caratteri    * ² ³ ° \" ordinal not in range (128)\")~~

In alcune distribuzioni Linux e nel caso di un errore **\"ordinal not in range (128)\"** esiste un\'altra versione su questa pagina [Macro\_FCInfo\_Alternate\_Linux](Macro_FCInfo_Alternate_Linux.md)

ver 1.08 , 24/10/2013 correzione della mappa dei titoli \"Faces\" e \"Edges\" sopra 100 objeti

ver 1.07 , 11/10/2013 mappare gli spigoli (\"Faces\") e le loro coordinate.

ver 1.06 , 22/09/2013 mappare gli spigoli (\"Edges\") e le loro coordinate, angoli di inclinazione riferiti all\'elemento piuttosto che all\'oggetto globale

ver 1.05 , 17/09/2013 aggiunto un\'icona per il foglio di calcolo, conversione in tonneau fr, dà le dimensioni fuori tutto invece di dare le coordinate.

ver 1.04 , 11/09/2013   * leggere i dati direttamente in una tabella.

ver 1.03 , 09/09/2013   * visualizzazione più chiara nella \"vista report\" e sostituzione di \"typeObject = sel\[0\].Shape.ShapeType\"

ver 1.02 , 7/09/2013    * piccole modifiche

ver 1.0 , 6/09/2013


<div class="mw-translate-fuzzy">

## Links

Vedere [Arch Survey](Arch_Survey/it.md) <img alt="Arch Survey" src=images/Arch_Survey.svg  style="width   *36px;">


</div>

See Also   * <img alt="Arch Survey" src=images/Arch_Survey.svg  style="width   *36px;"> [Arch Survey](Arch_Survey.md)

Si può commentare questa macro nel forum [Info Workbench - Help with icons please.](http   *//forum.freecadweb.org/viewtopic.php?f=10&t=3185)
Qui uno altro post ché parla di [FCInfo Macro](http   *//forum.freecadweb.org/viewtopic.php?f=8&t=6005)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FCInfo/it
