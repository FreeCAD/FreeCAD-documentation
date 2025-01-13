# Macro Center Align Objects with Faces or Edges/it
**Ora questi strumenti sono inclusi nell'ambiente [Manipulator](Manipulator_Workbench/it.md). Installare questo workbench per gli ultimi aggiornamenti su questi strumenti.**


{{Macro/it
|Name=Center Faces of Parts
|Translate=Centra e allinea facce e bordi
|Icon=Macro_Center_Align_Objects_with_Faces_or_Edges.svg
|Description=Allinea gli oggetti vincolando le facce o i bordi. Ora questi strumenti sono inclusi nell'ambiente [Manipulator](Manipulator_Workbench/it.md). Installare questo workbench per gli ultimi aggiornamenti su questi strumenti
|Author=easyw-fc
|Version=1.5.3
|Date=2017-10-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/e/ee/Macro_Center_Align_Objects_with_Faces_or_Edges.svg ToolBar Icon]<br/>[https://www.freecadweb.org/wiki/images/3/3d/Manipulator_Mover.svg Mover-icon]<br/>[https://www.freecadweb.org/wiki/images/1/10/Manipulator_Caliper.svg Caliper-icon]
}}

## Descrizione

Questa macro allinea gli oggetti tramite i vincoli di facce o bordi


{{Codeextralink|https://raw.githubusercontent.com/easyw/FreeCAD_Macros/master/Align%20Objects/CenterAlignObjectswFacesEdges.py}}



## Strumenti

**Aligner** <img alt="" src=images/Macro_Center_Align_Objects_with_Faces_or_Edges.svg  style="width:32px;">: un set di strumenti per spostare e allineare le parti 3D

**Mover** <img alt="" src=images/Manipulator_Mover.svg  style="width:32px;">: una serie di strumenti per spostare e ruotare parti 3D su diversi assi

**Measure** <img alt="" src=images/Manipulator_Caliper.svg  style="width:32px;">: una serie di strumenti per misurare le parti 3D, con alcune funzioni di Snap e di misurazione di Raggio, Lunghezza, Angolo.

Questi supporti lavorano con **Part, App::Part e Body objects**. Ogni strumento può essere **Floating** o **Docked Left o Right**.





## Vecchie riferimenti 

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

## Utilizzo

Per vincolare facce o bordi tra parti non cilindriche, basta aprire un documento FC, lanciare la Macro, selezionare due o più facce o bordi da allineare, fare clic sul pulsante Allinea e il gioco è fatto!

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
⏵ [documentation index](../README.md) > Macro Center Align Objects with Faces or Edges/it
