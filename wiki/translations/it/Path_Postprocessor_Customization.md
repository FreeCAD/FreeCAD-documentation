# Path Postprocessor Customization/it

 





{{TOCright}}

## Introduzione

FreeCAD usa come rappresentazione interna dei percorsi generati i cosiddetti G-codes. Possono descrivere cose come: velocità e avanzamenti, arresto del motore, ecc. Ma la cosa più importante sono i movimenti che descrivono. Questi movimenti sono piuttosto semplici: Possono essere linee rette o archi di cerchio. Curve più sofisticate come le B-spline sono già approssimate dal <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> di FreeCAD. [Ambiente Path](Path_Workbench/it.md).

## Cosa può fare il postprocessore per voi 


<div class="mw-translate-fuzzy">

Molti fresatrice usano anche i G-codes per controllare il processo di fresatura. Possono assomigliare quasi ai codici interni, ma ci possono essere alcune differenze:

-   la macchina può avere una sequenza di avvio speciale
-   può avere una speciale sequenza di arresto
-   gli archi possono essere definiti con un centro relativo o assoluto
-   può richiedere numeri di linea in un certo formato
-   Può utilizzare i cosiddetti cicli \"canned\" per sottoprocessi predefiniti come la foratura.
-   Si può preferire l\'output del G-code in unità metriche o imperiali.
-   Potrebbe essere utile eseguire una serie di mosse prima di chiamare un cambio utensile per rendere l\'azione più facile per l\'operatore
-   Potreste voler includere commenti per la leggibilità o sopprimerli per mantenere il programma piccolo
-   Potresti voler includere un\'intestazione personalizzata per identificare o documentare il programma per riferimenti futuri.
-   \...


</div>

Inoltre ci sono altri linguaggi per controllare un fresatrice, come HPGL, DXF o altri.

Il postprocessore è un programma che traduce i codici interni in un file completo, che può essere caricato sulla vostra macchina.

## Preparazione per scrivere il proprio postprocessore 

Puoi iniziare con un modello molto semplice che mostri come la tua macchina legge linee rette e archi. Preparalo con qualsiasi programma adatto alla tua macchina.

Un file per tali percorsi che iniziano a (0,0,0) e vanno verso Y sarebbe utile. Assicuratevi che sia l\'utensile stesso a muoversi lungo questo percorso, vale a dire che non deve essere applicata alcuna compensazione del raggio dell\'utensile.

![](images/Path_PostProcessorSketch.png )

Il percorso in FreeCAD sarebbe simile a questo. Notate la piccola freccia blu che indica la direzione di partenza. Per un primo tentativo si può fornire solo un livello nel piano XY.

![](images/Path_PostProcessorModel.png )

Puoi quindi dare un\'occhiata al file e confrontarlo con l\'output di postprocessori esistenti come {{FileName|linux_cnc_post.py}} o {{FileName|grbl_post.py}} e provare tu stesso ad adattarli o caricare il tuo sul forum di Path <https://forum.freecadweb.org/viewforum.php?f=15> per ricevere aiuto.

## Convenzione dei nomi 


<div class="mw-translate-fuzzy">

Per un formato di file {{FileName|<filename>}} il postprocessore dovrebbe ottenere il nome {{FileName|<filename>_post.py}}. Si prega di notare che {{FileName|_post.py}} deve essere in tutte le lettere minuscole.


</div>

Se la state testando, mettetela nella vostra directory delle macro. Se funziona bene, considera di metterla a disposizione degli altri (postala nel forum di FreeCAD Path) in modo che possa essere inclusa nella distribuzione di FreeCAD in futuro.

## Altri postprocessori esistenti 


<div class="mw-translate-fuzzy">

Per fare un paragone si possono guardare i postprocessori che vengono forniti con l\'installazione di FreeCAD. Si trovano sotto la directory Mod in Path/PathScripts/post. Molto usati sono i postprocessori <img alt="" src=images/linuxcnc.png  style="width:64px;"> [linuxcnc](http://linuxcnc.org/) e <img alt="" src=images/grbl.png  style="width:64px;"> [grbl](https://github.com/grbl/grbl). Studiare il loro codice può dare indicazioni utili.

-   Su Linux il percorso è /usr/share/freecad/Mod/Path/PathScripts/post


</div>

## Programmare il proprio postprocessore 

Questo post discute alcuni elementi interni dei postprocessori linuxcnc. La stessa struttura è usata anche in altri postprocessori.

Guardando linux\_cnc\_post.py, vedrete la funzione di esportazione (dalla 0.19.20514 alla linea 156)


```python
def export(objectslist, filename, argstring):
    # pylint: disable=global-statement
    ...
    gcode = ""
    ...
    ...
```

raccoglie passo dopo passo nella variabile \"gcode\" i codici G elaborati e gestisce l\'esportazione complessiva degli oggetti post-processabili (operazioni, utensili, lavori, ecc.). L\'esportazione gestisce le cose di alto livello come i commenti e il refrigerante, ma tutti gli oggetti che hanno più comandi di percorso (cambi di utensili e operazioni) li delega alla funzione parse (a partire dalla 0.19.20514 è alla linea 288).


```python
def parse(pathobj):
    ...
    out = ""
    lastcommand = None
    ...
    ...
```

Analogamente alla funzione \"export\" raccoglie i G-codes nella variabile \"out\". Nella variabile \"command\" i comandi visti nella funzione \"inspect G-code\" del Ambiente Path sono memorizzati e possono essere esaminati per ulteriori elaborazioni.


```python
        for c in pathobj.Path.Commands:

            command = c.Name
```

Riconosce i diversi codici G, M, F, S e altri G-codes. Ricordando l\'ultimo comando nella variabile \"lastcommand\" può sopprimere successive ripetizioni di comandi modali.

Sia il parse che l\'export non fanno altro che formattare le stringhe e concatenarle insieme in quello che sarà l\'output finale.

Vedrete che entrambe le funzioni chiamano anche la funzione \"linenumber()\". Se l\'utente vuole i numeri di linea, la funzione linenumber restituisce la stringa da incollare nel punto appropriato, altrimenti restituisce una stringa vuota quindi non viene aggiunto nulla.

## Relazioni


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_PostProcess.svg  style="width:24px;"> [Path PostProcesso](Path_Post/it.md)


</div>





{{Path_Tools_navi

}} 
