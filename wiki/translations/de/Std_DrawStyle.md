---
- GuiCommand:/de
   Name:Std DrawStyle
   MenuLocation:{{StdMenu|[Ansicht](Std_View_Menu/de.md)}} → Zeichenstil
   Workbenches:Alle
   SeeAlso:[WahlBegrenzungRahmen](Std_SelBoundingBox/de.md)
---

# Std DrawStyle/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Alle Objekte der [3D Ansicht](3D_view/de.md) werden in verschiedenen Zeichenstilen angezeigt, einschließlich durchgezogener Linien, Drahtgitter und als Punkte.


</div>

## Anwendung


<div class="mw-translate-fuzzy">

-   Gehe zum Menü {{MenuCommand/de|{{StdMenu|[Ansicht](Std_View_Menu/de.md)}} → Zeichenstile}}, und wähle eine Option.
    -   <img alt="" src=images/DrawStyleAsIs.svg  style="width:24px;"> Wie vorhanden
    -   <img alt="" src=images/DrawStyleFlatLines.svg  style="width:24px;"> Flache Linien
    -   <img alt="" src=images/DrawStyleShaded.svg  style="width:24px;"> Schattiert
    -   <img alt="" src=images/DrawStyleWireFrame.svg  style="width:24px;"> Drahtgitter
    -   <img alt="" src=images/DrawStylePoints.svg  style="width:24px;"> Punkte
    -   <img alt="" src=images/DrawStyleWireFrame.svg  style="width:24px;"> Ausgeblendete Linie
    -   <img alt="" src=images/DrawStyleWireFrame.svg  style="width:24px;"> Keine Schattierung


</div>

## Available draw styles 

### <img alt="" src=images/Std_DrawStyleAsIs.svg  style="width:24px;"> As is 

The **As is** style does not override the **Display Mode** of objects.

![](images/Std_DrawStyleAsIs_example.png ) 
*4 identical objects each with a different Display Mode (from left to right: 'Points', 'Wireframe', 'Shaded' and 'Flat lines') with the 'As is' draw style applied*

### <img alt="" src=images/Std_DrawStylePoints.svg  style="width:24px;"> Points 

The **Points** style overrides the **Display Mode** of objects. This style matches the \'Points\' Display Mode. Vertices are displayed in solid colors. Edges and faces are not displayed.

![](images/Std_DrawStylePoints_example.png ) 
*The same objects with the 'Points' draw style applied*

### <img alt="" src=images/Std_DrawStyleWireFrame.svg  style="width:24px;"> Wireframe 

The **Wireframe** style overrides the **Display Mode** of objects. This style matches the \'Wireframe\' Display Mode. Vertices and edges are displayed in solid colors. Faces are not displayed.

![](images/Std_DrawStyleWireframe_example.png ) 
*The same objects with the 'Wireframe' draw style applied*

### <img alt="" src=images/Std_DrawStyleHiddenLine.svg  style="width:24px;"> Hidden line 

The **Hidden line** style overrides the **Display Mode** of objects. Objects are displayed as if converted to triangular meshes.

![](images/Std_DrawStyleHiddenLine_example.png ) 
*The same objects with the 'Hidden line' draw style applied*

### <img alt="" src=images/Std_DrawStyleNoShading.svg  style="width:24px;"> No shading 

The **No shading** style overrides the **Display Mode** of objects. Vertices, edges and faces are displayed in solid colors.

![](images/Std_DrawStyleNoShading_example.png ) 
*The same objects with the 'No shading' draw style applied*

### <img alt="" src=images/Std_DrawStyleShaded.svg  style="width:24px;"> Shaded 

The **Shaded** style overrides the **Display Mode** of objects. This style matches the \'Shaded\' Display Mode. Vertices and edges are not displayed. Faces are illuminated depending on their orientation.

![](images/Std_DrawStyleShaded_example.png ) 
*The same objects with the 'Shaded' draw style applied*

### <img alt="" src=images/Std_DrawStyleFlatLines.svg  style="width:24px;"> Flat lines 

The **Flat lines** style overrides the **Display Mode** of objects. This style matches the \'Flat lines\' Display Mode. Vertices and edges are displayed in solid colors. Faces are illuminated depending on their orientation.

![](images/Std_DrawStyleFlatLines_example.png ) 
*The same objects with the 'Flat lines' draw style applied*


<div class="mw-translate-fuzzy">

### Hinweise


</div>


<div class="mw-translate-fuzzy">

-   Der Stil \"Flache Linien\" gibt den Kanten eine einheitliche Farbe, und die Flächen werden je nach Ausrichtung der Ansicht unterschiedlich beleuchtet.
-   Der Stil \"Schattiert\" entfernt die Farbe der Ränder. Dieser Stil ist besser bei der Anzeige von Objekten mit vielen verschiedenen Flächen mit Normalen, die in verschiedene Richtungen verlaufen, insbesondere in Richtungen, die sich von der X, Y und Z Achse unterscheiden.
-   Der Stil \"Drahtgitter\" entfernt die Farbe der Flächen und lässt nur die Kanten und Eckpunkte stehen. Dies führt zu einem durchsichtigen Modus, so dass es möglich ist, Objekte zu sehen, die ganz oder teilweise durch andere Objekte verdeckt sind.
-   Der Stil \"Punkte\" zeigt nur die Knoten an, an denen zwei Kanten miteinander verbunden sind. Bei Volumenkörpern, die aus relativ einfachen Formen bestehen, werden nur einige wenige Knoten angezeigt. Dieser Stil ist bei der Darstellung von Polygonnetzen besser, da in diesem Fall typischerweise viele Knoten zu sehen sind. Um die Sichtbarkeit zu verbessern, könnte es bei diesem Stil hilfreich sein, den Wert von {{PropertyView/de|Punktgröße}} zu erhöhen.
-   Der Stil \"Ausgeblendete Linie\" zeigt die dreieckigen Flächen und ihre Kanten so an, als ob die Objekte in Dreiecksnetze umgewandelt würden.
-   Der Stil \"Keine Schattierung\" gibt den Kanten eine einheitliche Farbe, und alle Flächen werden unabhängig von der Ausrichtung der Ansicht gleichmäßig beleuchtet.


</div>





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std DrawStyle/de
