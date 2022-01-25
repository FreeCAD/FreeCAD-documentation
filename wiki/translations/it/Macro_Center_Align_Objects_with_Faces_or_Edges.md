# Macro Center Align Objects with Faces or Edges/it
**Ora questi strumenti sono inclusi nell'ambiente [Manipulator](Manipulator_Workbench/it.md). Installare questo workbench per gli ultimi aggiornamenti su questi strumenti.**


<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Center Faces of Parts
|Translate=Centra e allinea facce e bordi
|Icon=Macro_Center_Align_Objects_with_Faces_or_Edges.png
|Description=Allinea gli oggetti vincolando le facce o i bordi. Ora questi strumenti sono inclusi nell'ambiente [Manipulator](Manipulator_Workbench/it.md). Installare questo workbench per gli ultimi aggiornamenti su questi strumenti
|Author=easyw-fc
|Version=1.5.3
|Date=2017-10-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/e/ee/Macro_Center_Align_Objects_with_Faces_or_Edges.svg ToolBar Icon]<br/>[https://www.freecadweb.org/wiki/images/8/8b/Mover-ico.png Mover-ico]<br/>[https://www.freecadweb.org/wiki/images/e/ee/Caliper-ico.png Caliper-ico]
}}


</div>

## Descrizione

Questo macro si allinea oggetti con i volti o i bordi vincoli


{{Codeextralink|https://raw.githubusercontent.com/easyw/FreeCAD_Macros/master/Align%20Objects/CenterAlignObjectswFacesEdges.py}}

## Strumenti


<div class="mw-translate-fuzzy">

**Aligner** ![](images/Aligner-ico.png ): un set di strumenti per spostare e allineare le parti 3D


</div>


<div class="mw-translate-fuzzy">

**Mover** ![](images/Mover-ico.png ): una serie di strumenti per spostare e ruotare parti 3D su diversi assi


</div>


<div class="mw-translate-fuzzy">

**Measure** ![](images/Caliper-ico.png ): una serie di strumenti per misurare le parti 3D, con alcune funzioni di Snap e di misurazione di Raggio, Lunghezza, Angolo.


</div>

Questi supporti lavorano con **Part, App::Part e Body objects**. Ogni strumento può essere **Floating** o **Docked Left o Right**.



## Vecchie referenze 

Questa macro applica i seguenti vincoli:

-   vincolo concentrico tra parti non cilindriche;
-   vincolo nel centro di facce e bordi.
-   Funziona anche con i nuovi contenitori Body e App::Part, funziona lo stesso anche con la gerarchia STEP.

![](images/Center-align-faces.png )

![](images/center-align-faces-in-action.gif )

![](images/center-align-Body-objects.gif )

![](images/utube-alignment-tool-tutorial.png )

[Aligning tool video tutorial](https://youtu.be/qzixT157jJU)

![](images/utube-alignment-STEP-models.png )

[Aligning STEP models video tutorial](https://youtu.be/aQcPqhlgHBU)


<div class="mw-translate-fuzzy">

## Uso

Per vincolare facce o bordi tra parti non cilindriche, basta aprire un documento FC, lanciare la Macro, selezionare due o più facce o bordi da allineare, fare clic sul pulsante Allinea e il gioco è fatto!


</div>

## Script

L\'icona per la barra degli strumenti <img alt="" src=images/Macro_Center_Align_Objects_with_Faces_or_Edges.png  style="width:50px;">

**CenterAlignObjectswFacesEdges.py**

Dopo aver scaricato il file dalla pagina GitHub
<https://github.com/easyw/FreeCAD_Macros/tree/master/Align%20Objects>
il codice:
<https://github.com/easyw/FreeCAD_Macros/raw/master/Align%20Objects/CenterAlignObjectswFacesEdges.py>
è necessario copiare il file nella directory delle macro.
Per maggiori informazioni vedere la pagina [Come installare le macro](How_to_install_macros/it.md)

## Link

Nel forum : [Faces or Edges constraint among non cylindrical parts Macro](http://forum.freecadweb.org/viewtopic.php?f=22&t=18655)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Center Align Objects with Faces or Edges/it
