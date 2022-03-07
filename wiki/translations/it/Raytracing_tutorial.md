---
- TutorialInfo:/it
   Topic: Raytracing
   Level: Base
   Time: 10 minuti + tempo per il Render
   Author:[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
   FCVersion:0.16 o superiore
   Files:
---

# Raytracing tutorial/it



## Raytracing Workbench 


**The [Raytracing workbench](Raytracing_Workbench.md) is being superseded by the new [https://github.com/FreeCAD/FreeCAD-render Render Workbench], which is intended as its replacement. The Render Workbench can be installed through the [Addon Manager](Std_AddonMgr.md). The information here is provided because by default FreeCAD is still shipped (as of 0.19-24276) with the Raytracing Workbench, and because the new module should basically work in the same way**




<div class="mw-translate-fuzzy">

### Introduzione

Questo tutorial ha lo scopo di introdurre il lettore al flusso di lavoro di base dell\'ambiente Raytracing, e alla maggior parte degli strumenti che sono a disposizione per creare una immagine renderizzata.


</div>

<img alt="" src=images/Raytracing_tutorial_result.png  style="width:480px;">


<div class="mw-translate-fuzzy">

### Requisiti

-   FreeCAD versione 0.16 o superiore
-   [POV-Ray](http://www.povray.org/) e/o [LuxRender](http://www.luxrender.net/) installati nel sistema
-   Nel caso di POV-Ray, non è sufficiente avere solo l\'eseguibile binario installato, ma ***è richiesta*** anche l\'installazione dei \'\'\'\'\'file di supporto \'\'\'\'\', e in Ubuntu questi sono forniti dal pacchetto dei file raccomandati [povray-includes](https://packages.ubuntu.com/search?keywords=povray-includes). Potenziali problemi sono stati riscontrati anche con installazioni Linux che richiedono la creazione manuale di file di configurazione locali nella cartella home dell\'utente, come discusso [qui](https://forum.freecadweb.org/viewtopic.php?f=3&t=27548&start=10#p224576).
-   Nel caso di POV-Ray, si raccomanda di installare la [macro di psicofil](https://github.com/psicofil/Macros_FreeCAD)
-   Il lettore abbia le conoscenze di base per utilizzare gli ambienti Parte e PartDesign


</div>


<div class="mw-translate-fuzzy">

### Procedura


</div>


<div class="mw-translate-fuzzy">

#### Il modello 

In questo esempio viene utilizzato un cubo come oggetto di studio, ma al suo posto si possono usare i modelli creati con Parte o PartDesign.


</div>

1.  Creare un nuovo documento
2.  Attivare l\'ambiente Parte
3.  Creare un Cubo. Siete liberi di cambiare le sue proprietà in qualsiasi modo.

Ora abbiamo un modello con il quale lavorare.


<div class="mw-translate-fuzzy">

#### Preparativi per il render 

1.  Passare all\'ambiente Raytracing
2.  Cambiare la Vista in **Prospettiva**. Andare nel menu **Vista** e selezionare **Prospettiva**.
3.  Impostare il percorso del renderer. Andare nel menu **Modifica** e selezionare **Preferenze**. Cliccare su **Raytracing** e impostare il percorso del file eseguibile.
4.  Impostare le dimensioni dell\'immagine di rendering. Andare nel menu **Modifica** e selezionare **Preferenze**. Cliccare su **Raytracing** e impostare la dimensione desiderata dell\'immagine.


</div>


<div class="mw-translate-fuzzy">

##### POV-Ray 

1.  Selezionare <img alt="" src=images/Raytracing_New.png  style="width:32px;"> [Nuovo progetto PovRay](Raytracing_New.md). Nel menu a discesa impostare 
**RadiosityNormal**


</div>


<div class="mw-translate-fuzzy">

##### LuxRender

1.  Selezionare <img alt="" src=images/Raytracing_Lux.png  style="width:32px;"> [Nuovo progetto LuxRender](Raytracing_Lux.md). Nel menu a discesa impostare 
**LuxClassic**


</div>


<div class="mw-translate-fuzzy">

#### Impostare la posizione della camera 

1.  Posizionare la **Vista 3D** nella posizione e alla distanza desiderata dal modello. In questo caso, useremo la **Vista assonometrica**.
2.  Selezionare il **Project Folder** nella **Vista ad albero**
3.  Selezionare <img alt="" src=images/Raytracing_ResetCamera.png  style="width:32px;"> [Reset camera](Raytracing_ResetCamera/it.md)


</div>


<div class="mw-translate-fuzzy">

#### Importare il modello 

1.  Selezionare il modello per il rendering.
2.  Selezionare <img alt="" src=images/Raytracing_InsertPart.png  style="width:32px;"> [Inserisci parte](Raytracing_InsertPart/it.md)


</div>


<div class="mw-translate-fuzzy">

#### Eseguire il renderer 

1.  Selezionare <img alt="" src=images/Raytracing_Render.png  style="width:32px;"> [Render](Raytracing_Render/it.md).
2.  Impostare il percorso in cui memorizzare l\'immagine.
3.  Attendere che il rendering finisca. Questo potrebbe richiedere alcuni minuti.


</div>


<div class="mw-translate-fuzzy">

#### Visualizzare i risultati 

Appena il rendering è finito FreeCAD apre immediatamente l\'immagine.


</div>


<div class="mw-translate-fuzzy">

Il flusso di lavoro di base per l\'ambiente [Raytracing](Raytracing_Workbench/it.md) è concluso.


</div>


 {{Raytracing Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Raytracing](Raytracing_Workbench.md) > Raytracing tutorial/it
