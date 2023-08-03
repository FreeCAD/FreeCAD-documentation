# Part Builder/it
---
 GuiCommand:   Name: Part Builder   Name/it: Crea forme   Workbenches: Part_Workbench/it   Parte, Draft_Upgrade/it, Draft_Downgrade/it---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

È uno strumento per creare diverse forme complesse basate su geometrie primitive parametriche.


</div>




<div class="mw-translate-fuzzy">

## Uso

Questo strumento permette di creare delle forme creando

1.  Bordo da due vertici
2.  Faccia da vertici
    1.  Selezionare nella vista 3D i vertici che delimitano la faccia
    2.  Selezionare se la faccia deve essere planare
    3.  Cliccare su ** Crea**
    4.  L\'oggetto viene creato nella vista 3D ed elencato nella vista ad albero
3.  Polilinea da bordi {{Version/it|0.18}}##Selezionare un set di bordi adiacenti nella vista 3D
    1.  Cliccare su ** Crea**
4.  Faccia da spigoli
    1.  Selezionare nella vista 3D un insieme chiuso di spigoli che delimitano la faccia
    2.  Selezionare se la faccia deve essere planare
    3.  Cliccare su ** Crea**
    4.  L\'oggetto viene creato nella vista 3D ed elencato nella vista ad albero
5.  Shell (guscio) da facce
    1.  Selezionare le facce di un oggetto nella vista 3D
    2.  Selezionare se la forma deve essere affinata
    3.  Selezionare se tutte le facce devono essere incluse nel guscio
    4.  Cliccare su ** Crea**
    5.  L\'oggetto viene creato nella vista 3D ed elencato nella vista ad albero
6.  Solido da shell
    1.  Selezionare se la forma deve essere affinata
    2.  Cliccare su ** Crea**
    3.  L\'oggetto viene creato nella vista 3D ed elencato nella vista ad albero


</div>


<div class="mw-translate-fuzzy">


{{Part Tools navi/it}}


</div>

 {{Userdocnavi/it}}

1.  Select two vertices
2.  Click on **Create**

![](images/Edge_from_verts-1.gif )

### Wire from edges 

1.  Select a set of adjacent edges in the [3D view](3D_view.md)
2.  Click on **Create**

![](images/Wire_from_edges-1.gif )

### Face from vertices 

1.  Select vertices bounding the face in the [3D view](3D_view.md)
2.  Select if face should be planar
3.  Click on **Create**
4.  Object will be created in [3D view](3D_view.md) and will be listed in [tree view](Tree_view.md)

![](images/Face_from_verts.gif )

### Face from edges 

1.  Select a closed set of edges bounding the face in the [3D view](3D_view.md)
2.  Select if face should be planar
3.  Click on **Create**
4.  Object will be created in [3D view](3D_view.md) and will be listed in [tree view](Tree_view.md)

![](images/Face_from_edges.gif )

### Shell from faces 

1.  Select faces in the [3D view](3D_view.md)
2.  Select if the shape should be refined
3.  Select if all faces should be included in shell
4.  Click on **Create**
5.  Object will be created in [3D view](3D_view.md) and will be listed in [tree view](Tree_view.md)

### Solid from shell 

1.  Select if the shape should be refined
2.  Click on **Create**
3.  Object will be created in [3D view](3D_view.md) and will be listed in [tree view](Tree_view.md)

## Notes


<div class="mw-translate-fuzzy">

## Note

Un possibile flusso di lavoro potrebbe essere:

-   Disegnare un modello filiforme della forma utilizzando gli strumenti dell\'ambiente Draft (ad esempio, linea e polilinea)
-   Creare tutte le facce con \"Faccia da bordi\"
-   Creare un \"Shell da facce\"
-   Creare un \"Solido da shell\"

Nell\'ambiente [Draft](Draft_Workbench/it.md) sono disponibili gli strumenti **<img src="images/Draft_Upgrade.png" width=16px> [Promuovi](Draft_Upgrade/it.md)** e **<img src="images/Draft_Downgrade.png" width=16px> [Declassa](Draft_Downgrade/it.md)** che permettono di lavorare sulla composizione e scomposizione delle forme.


</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Builder/it
