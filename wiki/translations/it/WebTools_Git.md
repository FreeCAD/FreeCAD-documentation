---
- GuiCommand:/it
   Name:Arch Git
‏‎   Name/it:Arch Git
   MenuLocation:Arch → Utilità → Git
   Workbenches:[Arch](Arch_Workbench/it.md)
   Shortcut:
‏‎   SeeAlso:
---

# WebTools Git/it


</div>


<div class="mw-translate-fuzzy">

**Nota:** A partire da FreeCAD v0.17, questo strumento è stato rimosso dall\'ambiente Arch e ora fa parte dell\'ambiente esterno Webtools che è possibile installare tramite il menu Strumenti → Addons Manager


</div>

## Descrizione

Questo comando consente di eseguire il commit del documento attivo a un repository [GIT](https://en.wikipedia.org/wiki/Git_%28software%29). GIT è un potente sistema di controllo di versione del file, è in grado di gestire diverse versioni dei file e di conservare la traccia delle modifiche.

Git è uno strumento complesso, prima di utilizzare questo strumento considerare di imparare le sue basi, al fine di evitare operazioni errate che possono causare la perdita di dati. Su internet è disponibile e facile da trovare una abbondante letteratura su GIT.


<div class="mw-translate-fuzzy">

**Note:** Per essere in grado di utilizzare questo comando, sul sistema deve essere installato il pacchetto [gitpython](https://github.com/gitpython-developers/GitPython). Sulla maggior parte delle distribuzioni Linux, gitpython è disponibile nei repository software standard come *gitpython* o *python-git*.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Salvare il documento attivo corrente
2.  Assicurarsi che il file salvato è già parte di un repository git
3.  Selezionare il menu Arch → Utilità → **<img src="images/WebTools_Git.svg" width=16px> [Git](Arch_Git/it.md)
**


</div>

## Opzioni


<div class="mw-translate-fuzzy">

![](images/Arch_Git_panel.jpg )


</div>


<div class="mw-translate-fuzzy">

-   Assicurarsi che il pannello **Report** sia aperto in modo che i messaggi di Git possano essere stampati al suo interno.
-   Lo strumento Git si apre solo se il file corrente è salvato all\'interno di un repository Git. Può essere in una sottodirectory.
-   Il pulsante **Log** apre una finestra di dialogo che mostra i log (le voci di registro) più recenti.
-   Il pulsante **Refresh** esegue una nuova scansione del repository per individuare i file modificati.
-   Il pulsante **Diff** mostra le differenze tra la versione corrente di un file selezionato e la versione precedente memorizzata nel repository.
-   Il pulsante **Select all** seleziona tutti i file di cui fare il commit.
-   Il pulsante **Commit** esegue il commit dei file selezionati. Assicurarsi di scrivere un messaggio di commit che descrive le modifiche che si stanno commettendo.
-   Il pulsante **Pull** scarica le eventuali nuove modifiche nel repository locale da quello remoto selezionato. Se il file attualmente aperto in FreeCAD è stato modificato da un *Pull*, un messaggio di avviso informa l\'utente in modo che egli possa salvare nuovamente il file o salvarlo altrove.
-   Il pulsante **Push** carica il proprio ultimo commit (s) nel repository remoto selezionato.


</div>


<div class="mw-translate-fuzzy">

-   Lo strumento non è ancora in grado di creare dei nuovi repository. È necessario disporre di un repository locale esistente già creato (FreeCAD controllerà se il file del documento corrente è all\'interno di un repository Git)
-   Lo strumento non può modificare o creare rami. È necessario farlo manualmente con gli strumenti standard di Git.


</div>


<div class="mw-translate-fuzzy">

## Attivare la leggibilità delle differenze per i file FCStd 


</div>


<div class="mw-translate-fuzzy">

Il [formato dei file Fcstd](Fcstd_file_format/it.md) di FreeCAD è un formato binario basato su zip, per il quale Git non può produrre differenze corrette. Ciò significa che non si può vedere cosa è cambiato tra una versione e l\'altra, e anche che ogni nuova versione memorizzata nel repository Git è una copia completa del file.


</div>

Anche se il secondo problema attualmente non ha una soluzione, il primo può essere risolto con un piccolo strumento disponibile nel codice sorgente di FreeCAD, chiamato [fcinfo](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/fcinfo). A Git può essere ordinato di utilizzare l\'utilità fcinfo per stampare un rapporto human-friendly (leggibile dalle persone) di un file FCStd, e, quando gli viene chiesto di produrre un differenza tra due file FCStd, produce invece un diff tra i due rapporti fcinfo. Notare che questo è solo un feedback visivo, una copia completa del file rimane ancora memorizzata internamente.

Esempio di una differenza prodotta con fcinfo:


```python
diff --git a/testhouse.FcStd b/testhouse.FcStd
index 08077b6..985b1d8 100644
--- a/testhouse.FcStd
+++ b/testhouse.FcStd
@@ -1,26 +1,25 @@
-Document: /tmp/43un09_testhouse.FcStd (442K)
-   SHA1: 67c1985a45d93cba57d5bf44490897aba460100d
+Document: /tmp/zfXoDd_testhouse.FcStd (370K)
+   SHA1: db1cb5fca18af7bfdca849028f40550df4d845cb
    Comment : This is a test house to showcase FreeCAD's BIM worflow and IFC export capabilities
    Company : uncreated.net
    CreatedBy : Yorik van Havre
    CreationDate : Fri May  9 12:05:54 2014 
    FileVersion : 1
    Id : 
-   Label : testhouse
-   LastModifiedBy : Yorik van Havre
-   LastModifiedDate : 2016-06-28T17:05:57-03:00
+   Label : testhouse2
+   LastModifiedBy : Yorik van Havre
+   LastModifiedDate : Sat Sep 13 20:46:36 2014
+
    License : CC-BY 3.0
    LicenseURL : http://creativecommons.org/licenses/by/3.0/
-   ProgramVersion : 0.17R7800 (Git)
-   TipName : 
+   ProgramVersion : 0.15R3989 (Git)
    Uid : 67e62d8a-6674-4358-92fe-615443be887a
-   Objects: (231)
+   Objects: (221)
        Annotation : Drawing::FeatureViewAnnotation
        Annotation001 : Drawing::FeatureViewAnnotation
        Annotation002 : Drawing::FeatureViewAnnotation
        Annotation003 : Drawing::FeatureViewAnnotation
-       Annotation004 : Drawing::FeatureViewAnnotation
-       Annotation005 : Drawing::FeatureViewAnnotation
        Array : Part::FeaturePython (9K)
        Box : Part::Box (2K)
        Building : App::DocumentObjectGroupPython
@@ -110,7 +109,7 @@ Document: /tmp/43un09_testhouse.FcStd (442K)
        Floor : App::DocumentObjectGroupPython
        Floor001 : App::DocumentObjectGroupPython
        Floor002 : App::DocumentObjectGroupPython
-       Frame : Part::FeaturePython (89K)
```

Ogni file di FreeCAD contiene un numero checksum SHA1, che cambia ogni volta che il file viene salvato, anche se non è stato cambiato nessun contenuto. Così fcinfo stampa sempre qualcosa, non importa se il contenuto cambia.

Per abilitare l\'utilizzo di fcinfo (solo per Linux e Mac - Da fare: aggiungere le istruzioni per Windows)


<div class="mw-translate-fuzzy">

1.  Salvare il file fcinfo da qualche parte nel sistema
2.  Renderlo eseguibile
3.  Creare un file .gitattributes nel proprio repository Git
4.  Aggiungere in esso la seguente riga:

*.FCStd diff=fcinfo


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > WebTools Git/it
