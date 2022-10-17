---
- TutorialInfo   */it
   Topic   * Draft
   Level   * Base
   Time   * 30 minuti
   Author   *[http   *//freecadweb.org/wiki/index.php?title=User   *Drei Drei] e vocx
   FCVersion   *0.19
   Files   *[https   *//forum.freecadweb.org/viewtopic.php?f=36&t=43651 Draft tutorial updated]
---

# Draft tutorial/it





## Introduzione

This tutorial was originally written by Drei, and it was rewritten and illustrated by vocx.

This tutorial is meant to introduce the reader to the basic workflow of the <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> [Draft Workbench](Draft_Workbench.md).

The reader will practice   *

-   creation of lines, arcs, and polygons
-   the use of working planes
-   the creation of dimensions, text, and shapestrings
-   the creation of a technical drawing

This tutorial uses the notation {{Value|(x, y, z)}} to denote the coordinates required to define points in an object. The default unit is millimeters {{Value|mm}}.

<img alt="" src=images/00_Dr01_Draft_Tutorial_final.png  style="width   *" height="400px;"> 
*Final drawing including various Draft objects.*

## Setup

1\. Open FreeCAD, create a new empty document with **File → [<img src=images/Std_New.svg style="width   *16px"> [New](Std_New.md)**.

   *   1.1. Switch to the [Draft Workbench](Draft_Workbench.md) from the [workbench selector](Std_Workbench.md), or the menu **View → Workbench → [<img src=images/Workbench_Draft.svg style="width   *16px"> Draft**.
   *   1.2. Make sure you understand how to use the [property editor](property_editor.md), particularly the **Data** and **View** tabs to change the properties. When changing properties, you may have to do a **<img src="images/Std_Refresh.svg" width=16px> [Std Refresh](Std_Refresh.md)** action to see the result in the [3D view](3D_view.md).
   *   1.3. Since the Draft objects are planar shapes, they are better viewed from the top. Use **[<img src=images/Std_ViewTop.svg style="width   *16px"> [View top](Std_ViewTop.md)** to set the [3D view](3D_view.md).
   *   1.4. Although it is not used in this tutorial, the Draft grid is helpful to position geometrical elements. Use **[<img src=images/Draft_SelectPlane.svg style="width   *16px"> [SelectPlane](Draft_SelectPlane.md)** to set both the working plane and the grid, and then show and hide the grid with **[<img src=images/Draft_ToggleGrid.svg style="width   *16px"> [Toggle grid](Draft_ToggleGrid.md)**.

## Barra degli strumenti di snap 


<div class="mw-translate-fuzzy">

1.  Avviare **FreeCAD**
2.  Se non c\'è un nuovo documento di FreeCAD aperto (la maggior parte della finestra FreeCAD è grigia), dal menu a discesa fare clic su File -\> Nuovo o fare clic sullo strumento Crea un nuovo documento <img alt="" src=images/Document-new.svg  style="width   *32px;">.
3.  Attivare l\'ambiente **Draft**
4.  Selezionare il menu **Modifica**
5.  Cliccare su **Preferenze**
6.  Andare in **Draft** e selezionare la scheda **Griglia e snap**
7.  Verificare che **Mostra la barra degli strumenti snap** sia attiva


</div>


<div class="mw-translate-fuzzy">

Notare che in questo menu è possibile modificare la visibilità della **griglia**, nel caso in cui si desidera disattivarla.


</div>


<div class="mw-translate-fuzzy">

### Usare i piani 

I piani sono usati per limitare l\'azione degli strumenti Draft ad un piano specifico, evitando problemi con la posizione dei punti e delle curve nei pezzi complessi. I piani possono fare riferimento agli assi del sistema di coordinate **(XY, YZ, \...)** oppure possono utilizzare come riferimento una superficie planare del documento.


</div>

Most Draft objects are planar shapes so they are naturally based on a **working plane**. A working plane can be one of the main XY, XZ, and YZ global coordinate planes, or it can be a plane that is parallel to them with a positive or negative offset, or it can be a plane defined by the face of a solid object.


<div class="mw-translate-fuzzy">

1.  Selezionare <img alt="" src=images/Draft_SelectPlane.png  style="width   *32px;"> [Seleziona piano](Draft_SelectPlane/it.md). Può essere situato all\'interno della **barra degli strumenti di Draft** o nella sezione **Utilità** del **menu Draft**.
2.  Selezionare il piano **XY**


</div>

Before pressing the button, you can also change the value of the offset in millimeters, as well as the grid spacing, the main lines and snapping radius.


<div class="mw-translate-fuzzy">

#### Linee e Archi 

1.  Selezionare ![](images/Draft_Arc.png ) [Arco](Draft_Arc/it.md).
2.  Impostare il **centro** a **(0, 0, 0)**
3.  Impostare il **raggio** a 30 mm
4.  Impostare **starting angle** a 60.0°
5.  Impostare l\'ampiezza a 60.0°


</div>


<div class="mw-translate-fuzzy">

Ripetere la stessa procedura per un secondo arco con raggio di 25 mm, e con le altre proprietà invariate.


</div>


<div class="mw-translate-fuzzy">

1.  Selezionare ![](images/Draft_Line.png ) [Linea](Draft_Line/it.md).
2.  Avvicinare il cursore al **Punto finale** di un arco. Dovrebbe apparire un punto bianco, accanto a questa icona <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width   *32px;">.
3.  Selezionare il punto finale dell\'altro arco.
4.  Ripetere per l\'altro lato degli archi.


</div>

<img alt="" src=images/01_Dr01_Draft_Arc_profile.png  style="width   *" height="400px;"> 
*Closed profile created by two arcs and two lines.*

## Fusing or compounding 


<div class="mw-translate-fuzzy">

Ora ci sono diverse curve che definiscono il profilo, ma esse non sono ancora riconosciute come una singola entità. È possibile continuare a lavorare con gli elementi separati, ma in questo caso verranno fusi in un unico oggetto.


</div>


<div class="mw-translate-fuzzy">

1.  Selezionare un arco e tenendo premuto il tasto **Ctrl** selezionare i due segmenti di linea e l\'altro arco.
2.  Con questi quattro oggetti selezionati, fare clic su ![](images/Draft_Upgrade.png ) [Upgrade](Draft_Upgrade/it.md)


</div>

6b. If you wish to maintain the parametric nature of the objects you can create a compound instead.

   *   6b.1. Switch to the <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Part Workbench](Part_Workbench.md).
   *   6b.2. With these objects selected, click on **[<img src=images/Part_Compound.svg style="width   *16px"> [Part Compound](Part_Compound.md)**.


<div class="mw-translate-fuzzy">

#### Piani, Rettangoli e Cerchi 

1.  Cliccare ![](images/Draft_Rectangle.png ) [Rettangolo](Draft_Rectangle/it.md)
2.  Impostare il primo punto a **(-100, -60, 0)**. (Se dopo aver impostato questo punto Relativo appare attivato, deselezionarlo prima di impostare il secondo punto).
3.  Impostare il secondo punto a **(140, 90, 0)**


</div>

7\. We will draw a rectangular frame. (Switch back to the <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> [ Draft Workbench](Draft_Workbench.md).)

   *   7.1. Press **[<img src=images/Draft_Rectangle.svg style="width   *16px"> [Rectangle](Draft_Rectangle.md)**.
   *   7.2. Enter the values of the first point {{Value|(-100, -60, 0)}}, and press **Enter**.
   *   7.3. Make sure the **Relative** option is unchecked, as we will use absolute units. You may press **R** in the keyboard to quickly toggle this option on and off.
   *   7.4. Enter the values for the second point {{Value|(140, 90, 0)}}, and press **Enter**.


<div class="mw-translate-fuzzy">

Il risultato è un **Piano**. Le sue proprietà possono essere modificate per rimuovere il **Riempimento**, cambiando la sua **Visualizzazione** in **Wireframe**.


</div>


<div class="mw-translate-fuzzy">

1.  Selezionare ![](images/Draft_Circle.png )
2.  Impostare il centro a **(0, 0, 0)**
3.  Impostare il raggio a 15 mm


</div>


<div class="mw-translate-fuzzy">

#### Poligoni

1.  Selezionare ![](images/Draft_Polygon.png ) [Poligono](Draft_Polygon/it.md)
2.  Il centro è posizionato a **(0, 0, 0)**
3.  Impostare il numero di lati a 6
4.  Impostare il raggio 50 mm


</div>

Again, you may change the **Make Face** and **Display Mode** properties in the [property editor](property_editor.md) if you want.

The rectangle, the circle, the polygon, and most other objects created with the [Draft Workbench](Draft_Workbench.md) share many data and view properties because they are derived from the same base class, [Part Part2DObject](Part_Part2DObject.md).

<img alt="" src=images/02_Dr01_Draft_Rectangle_circle_polygon.png  style="width   *" height="400px;"> 
*Rectangle, circle and polygon added.*


<div class="mw-translate-fuzzy">

#### Schiere

Gli array sono utilizzati per replicare più volte un oggetto in una direzione, rispetto un asse di rotazione o lungo un percorso.

1.  Selezionare il **Wire** creato in precedenza
2.  Cliccare <img alt="" src=images/Draft_Array.png  style="width   *32px;"> [Schiera](Draft_Array/it.md)
3.  Nella scheda **Dati** dell\'oggetto, cambiare il tipo di schiera da **ortho** a **polar**
4.  Cambiare **Number Polar** da 1 a 3


</div>

Arrays are used to replicate an object several times in an orthogonal direction (X, Y, Z), around a revolution axis, or along a path.

10\. We will create a polar array.

   *   10.1. Select the {{Value|Wire}} object that was previously created with the **[<img src=images/Draft_Upgrade.svg style="width   *16px"> [Upgrade](Draft_Upgrade.md)** tool, or the {{Value|Compound}} created with the **[<img src=images/Part_Compound.svg style="width   *16px"> [Part Compound](Part_Compound.md)** tool.
   *   10.2. Press **[<img src=images/Draft_PolarArray.svg style="width   *16px"> [PolarArray](Draft_PolarArray.md)**.
   *   10.3. Adjust the polar angle to {{Value|360°}}.
   *   10.4. Set the number of elements to {{Value|4}}.
   *   10.5. Enter the values for the center of rotation {{Value|(0, 0, 0)}}, and press **Enter**.

The array object shows copies of the object around the origin.

<img alt="" src=images/03_Dr01_Draft_PolarArray.png  style="width   *" height="400px;"> 
*Polar array of the small profile centered around the origin.*


<div class="mw-translate-fuzzy">

### Aggiungere le dimensioni 

Le Dimensioni richiedono un uso costante di **Snap** per selezionare correttamente i punti che si vogliono quotare. La **Barra degli strumenti Snap** serve per cambiare i punti che è possibile selezionare.


</div>

Linear dimensions work best when using the appropriate [Draft Snap](Draft_Snap.md) methods to select points and edges to measure. However, they can also be created by specifying absolute coordinates.


<div class="mw-translate-fuzzy">

1.  Selezionare ![](images/Draft_Dimension.png ) [Dimensione](Draft_Dimension/it.md)
2.  Selezionare il primo punto. Questo può essere fatto cliccando su un elemento o specificando le coordinate di un punto esistente. In questo tutorial, il primo punto è sempre **(0, 0, 0)**
3.  Selezionare il secondo punto. Avvicinando il cursore al punto medio della linea superiore del poligono, dovrebbe apparire un punto bianco accanto questa icona <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width   *32px;">
4.  Spostare il cursore fino alla posizione desiderata della dimensione e fare clic.
5.  Nella tabella **Vista** cambiare la dimensione del carattere in 6 mm


</div>


<div class="mw-translate-fuzzy">

Ripetere il processo per gli archi ed i cerchi.


</div>

13\. Repeat the process for the circle located in the center. The first point of the measurement will still be the origin. To select the second point make sure **[<img src=images/Draft_Snap_Lock.svg style="width   *16px"> [Toggle snap](Draft_Snap_Lock.md)** is active, and only **[<img src=images/Draft_Snap_Angle.svg style="width   *16px"> [Angle](Draft_Snap_Angle.md)** as well. As you move the pointer to the top of the circle, the <img alt="" src=images/Draft_Snap_Angle.svg  style="width   *24px;"> [Angle](Draft_Snap_Angle.md) icon should appear; click to select this point. Then move the cursor to the right, and click to fix the dimension.

Remember to adjust the **Font Size**, and other properties to see the dimension correctly.

<img alt="" src=images/04_Dr01_Draft_Dimension.png  style="width   *" height="400px;"> 
*Dimensions that measure the vertical distance from the origin to the top of the circle, arcs, and polygon.*


<div class="mw-translate-fuzzy">

### Annotazioni e Testi 

Sono due cose leggermente diverse   * per eseguire delle operazioni 3D è possibile usare solo i testi come profilo.


</div>


<div class="mw-translate-fuzzy">

#### Annotazioni

1.  Selezionare ![](images/Draft_Text.png ) [Testo](Draft_Text/it.md)
2.  Selezionare il punto di riferimento nella **Vista 3D**. In questo caso, il punto medio dell\'arco superiore.
3.  Inserire il testo e premere **Invio**. Ripetere l\'operazione per tutte le righe di testo come si desidera inserire.
4.  Premere **Invio**


</div>


<div class="mw-translate-fuzzy">

#### Testo

1.  Selezionare <img alt="" src=images/Draft_ShapeString.png  style="width   *32px;"> [ShapeString](Draft_ShapeString/it.md)
2.  Selezionare il punto di riferimento nella **Vista 3D**. Questo può essere un punto esistente o la posizione corrente del cursore.
3.  Inserire il testo e premere **Invio**
4.  Impostare la dimensione del carattere
5.  Lasciare tracking a 0 mm
6.  Selezionare il **percorso** per il file di font che si desidera utilizzare


</div>

<img alt="" src=images/05_Dr01_Draft_Text_ShapeString.png  style="width   *" height="400px;"> 
*Text and ShapeString objects added.*

To extrude letters and engrave them on to solids, see the [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md).


<div class="mw-translate-fuzzy">

### Creare le proiezioni 

Per creare le proiezioni, è necessario creare un **Disegno** con gli elementi che si desidera utilizzare. Si prega di leggere il [Tutorial di Drawing](Drawing_tutorial/it.md) per avere una descrizione dettagliata.


</div>

As it is now, the objects that we have created can be saved, exported to other formats like [SVG](SVG.md) or [DXF](DXF.md), or printed.

If you wish, you may create a technical drawing to display these objects together with additional information like a frame.

Before doing anything, hide the Draft grid by pressing **[<img src=images/Draft_ToggleGrid.svg style="width   *16px"> [Toggle  grid](Draft_ToggleGrid.md)**.

16\. Switch to the <img alt="" src=images/Workbench_TechDraw.svg  style="width   *24px;"> [TechDraw Workbench](TechDraw_Workbench.md).

   *   16.1. Create a standard page by pressing **[<img src=images/TechDraw_PageDefault.svg style="width   *16px"> [TechDraw PageDefault](TechDraw_PageDefault.md)**.
   *   16.2. In the [tree view](tree_view.md) select all objects created, except for the Page, and then press **[<img src=images/TechDraw_ActiveView.svg style="width   *16px"> [TechDraw ActiveView](TechDraw_ActiveView.md)**. Press **OK** with the default options; it may take a few seconds to create the view in the page.
   *   16.3. Selecting the Page object in the [tree view](tree_view.md) will automatically display the Page in the main window. With the Page selected, go to the [property editor](Property_editor.md), and change **Scale** to {{Value|0.75}}.
   *   16.4. Expand the Page object in the [tree view](tree_view.md) to select the ActiveView object. With this view selected, go to the [property editor](Property_editor.md), and change **Scale Type** to {{Value|Page}}.
   *   16.5. Recompute the model by using **[<img src=images/Std_Refresh.svg style="width   *16px"> [Refresh](Std_Refresh.md)** or pressing **F5**.
   *   16.6. Hide the frames of the objects by pressing **[<img src=images/TechDraw_ToggleFrame.svg style="width   *16px"> [TechDraw ToggleFrame](TechDraw_ToggleFrame.md)**.

Learn more about the [TechDraw Workbench](TechDraw_Workbench.md) by reading the [Basic TechDraw Tutorial](Basic_TechDraw_Tutorial.md).

<img alt="" src=images/06_Dr01_Draft_TechDraw_page.png  style="width   *" height="400px;"> 
*TechDraw page with a projection of the shapes created with the Draft Workbench.*

TechDraw works best with objects that have a [Part TopoShape](Part_TopoShape.md). Since some objects from Draft, like [Draft Texts](Draft_Text.md) and [Draft Dimensions](Draft_Dimension.md), don\'t have such \"[shapes](Shape.md)\", some operations of TechDraw don\'t work with these elements.

Tools like **[<img src=images/TechDraw_ActiveView.svg style="width   *16px"> [TechDraw ActiveView](TechDraw_ActiveView.md)**, **[<img src=images/TechDraw_DraftView.svg style="width   *16px"> [TechDraw DraftView](TechDraw_DraftView.md)**, and **[<img src=images/TechDraw_ArchView.svg style="width   *16px"> [TechDraw ArchView](TechDraw_ArchView.md)** work by receiving an internal SVG image that is generated by internal Draft functions; therefore, TechDraw doesn\'t have much control about how these views are displayed. More integration of Draft and TechDraw is a work in progress.


<div class="mw-translate-fuzzy">

Il flusso di lavoro di base per l\'ambiente [Draft](Draft_Workbench/it.md) è concluso.


</div>

The [Draft Workbench](Draft_Workbench.md) in many ways is similar to the [Sketcher Workbench](Sketcher_Workbench.md), as both are intended to produce 2D shapes. The main difference is in the way each workbench handles coordinate systems, and how the objects are positioned. In Draft, objects are freely positioned in the global coordinates system, usually snapping their points to a grid, or to other objects. In Sketcher, a \"[sketch object](Sketch.md)\" defines a local coordinate system which serves as the reference for all geometrical elements within that sketch. Moreover, the sketch relies on \"constraints\" to define the final position of its points.

-   The [Draft Workbench](Draft_Workbench.md) is intended for 2D drawings which are suitable to be drawn on a grid. The [Arch Workbench](Arch_Workbench.md) mostly builds on top of the tools defined in the [Draft Workbench](Draft_Workbench.md).

-   The [Sketcher Workbench](Sketcher_Workbench.md) is intended for 2D drawings that require precise relationships between its points. It does not rely on a grid, but on rules of positioning (constraints) to determine where the points and edges will be placed. The [Sketcher Workbench](Sketcher_Workbench.md) is mostly used together with the [PartDesign Workbench](PartDesign_Workbench.md) for the creation of solid [bodies](Body.md).

-   It is possible to transform a Draft object into a [Sketch](Sketch.md), and the other way around, using the **[<img src=images/Draft_Draft2Sketch.svg style="width   *16px"> [Draft Draft2Sketch](Draft_Draft2Sketch.md)** tool.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Draft](Draft_Workbench.md) > Draft tutorial/it
