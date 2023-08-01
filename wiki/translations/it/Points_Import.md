---
- GuiCommand:/it
   Name:Points Import
   Name/it:Importa punti
   MenuLocation:Punti → Importa punti
   Workbenches:[Punti](Points_Workbench/it.md)
   SeeAlso:[Esporta punti](Points_Export/it.md)
   Icon:Points_Import.svg
---

# Points Import/it


<div class="mw-translate-fuzzy">

## Descrizione

Questo strumento importa punti da un file nuvola di punti.


</div>

The **Points Import** command imports a point cloud from a file.


<div class="mw-translate-fuzzy">

## Utilizzo

1.  Cliccare su **<img src="images/Points_Import.svg" width=16px> [Importa punti](Points_Import/it.md)** oppure usare il menu **Punti → <img src="images/Points_Import.svg" width=16px> Importa punti**.
2.  Selezionare il file con la nuvola di punti e fare click su **Apri**.


</div>

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Points_Import.svg" width=16px> [Points Import](Points_Import.md)** button.
    -   Select the **Points → <img src="images/Points_Import.svg" width=16px> Import Points...** option from the menu.
2.  Select a point cloud file.
3.  Press the **Open** button.

## Properties

See [Points Convert](Points_Convert.md).

## Point cloud file format 

-   A point cloud file must have the **.asc**, **.pcd** or **.ply** extension.
-   Each line in the file must list the X, Y and Z coordinates of a point.
-   The coordinates must be separated by spaces.
-   The coordinates must use a decimal point, not a decimal comma.


<div class="mw-translate-fuzzy">

## Esempio di file cloud di punti 


</div>

0 0 0
1.4562 -7.2354 12.2367
5.9423 3.1728 -17.6439


<div class="mw-translate-fuzzy">

Per i test si può usare questo file [ASC](https://github.com/FREECAD/Examples/blob/master/Point_cloud_ExampleFiles/PointCloud-Data_Stanford-Bunny.asc), che è una versione di [Stanford Bunny](http://graphics.stanford.edu/data/3Dscanrep/).


</div>





{{Points Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Points](Points_Workbench.md) > Points Import/it
