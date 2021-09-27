# Part Ellipsoid/it
---
- GuiCommand:/it   Name:Part Ellipsoid   Name/it:Ellissoide   MenuLocation:Parte → _---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Il comando <img alt="" src=images/Part_Ellipsoid.svg  style="width:24px;"> [Ellissoide](Part_Ellipsoid/it.md) command crea un ellissoide solido parametrico.


</div>

In FreeCAD la forma prodotta è limitata ad essere un solido sferoide (opzionalmente troncato), per crearlo è necessario ruotare un\'ellisse attorno ad uno dei sui assi. Per impostazione predefinita, si tratta di uno [sferoide oblato](http://it.wikipedia.org/wiki/Sferoide), [oblate spheroid](http://en.wikipedia.org/wiki/Oblate_spheroid), cioè la forma che si creerebbe ruotando un\'ellisse attorno al suo asse minore, ma i parametri possono essere modificati per formare uno sferoide prolato, [prolate spheroid](http://en.wikipedia.org/wiki/Prolate_spheroid).

In FreeCAD ogni sezione trasversale parallela al piano xy lo sferoide predefinito è un cerchio . La sezione trasversale parallela agli altri due piani è un\'ellisse.

In geometria, un [ellissoide](http://it.wikipedia.org/wiki/Ellissoide), [Ellissoide](http://en.wikipedia.org/wiki/Ellipsoid) avrebbe una sezione ellittica in tutti e tre i piani.

## Utilizzo


<div class="mw-translate-fuzzy">

La primitiva geometrica Ellissoide è disponibile dalla finestra di dialogo Crea primitive di Parte.

1.  Attivare l\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Parte](Part_Workbench/it.md)
2.  Ci sono diversi modi per accedere alla finestra di dialogo Crea ellisoide:
    -   Premere il pulsante <img alt="" src=images/Part_CreatePrimitives.svg  style="width:24px;"> [Crea primitive](Part_CreatePrimitives/it.md) nella barra degli strumenti di Part
    -   Usare **Part → [Crea primitive](Part_CreatePrimitives/it.md) → Ellissoide**


</div>

## Proprietà

-   Radius 1: Di default il raggio minore parallelo all\'asse Z,
-   Radius 2: Per default il raggio maggiore parallelo al piano XY, è anche il raggio massimo della sezione circolare trasversale
-   Angle 1: Troncamento inferiore dell\'ellissoide, parallelo alla sezione circolare (-90 gradi in uno sferoide completo)
-   Angle 2: Troncamento superiore dell\'ellissoide, parallelo alla sezione circolare (90 gradi in uno sferoide completo)
-   Angle 3: angolo di rotazione della sezione trasversale ellittica (360 gradi in uno sferoide completo)

![](images/Part_Ellipsoid_screenshot.jpg )

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Ellipsoid/it
