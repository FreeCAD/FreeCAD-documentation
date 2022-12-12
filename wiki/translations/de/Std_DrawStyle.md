---
- GuiCommand:/de
   Name:Std DrawStyle
   Name/de:Std DrawStyle
   MenuLocation:Ansicht → Darstellungsart → ...
   Workbenches:Alle
   Shortcut:**V** **1** - **V** **7**
   SeeAlso:[Std SelBoundingBox](Std_SelBoundingBox/de.md)
---

# Std DrawStyle/de

## Beschreibung

Der Befehl **Std Darstellungsart** kann den Effekt der {{PropertyView/de|Display Mode}} von Objekten in einer [3D-Ansicht](3D_view.md) überlagern.

## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Ein Klick auf den schwarzen Abwärtspfeil rechts von der Schaltfläche **<img src="images/Std_DrawStyleAsIs.svg" width=16px> [Std Darstellungsart](Std_DrawStyle/de.md)** und eine Darstellungsart aus dem Ausklappmenü wählen.
    -   Den Menüeintrag **Ansicht → Darstellungsart** auswählen und anschließend eine Darstellungsart aus dem Ausklappmenü wählen.
    -   Im Kontextmenü der [3D-Ansicht](3D_view/de.md) die Option **Darstellungsart** auswählen und anschließend eine Darstellungsart aus dem Ausklappmenü wählen.
    -   Eines der Tastaturkürzel **V** dann **1**, **2**, **3**, **4**, **5**, **6** oder **7**.

## Verfügbare Darstellungsarten 

### <img alt="" src=images/Std_DrawStyleAsIs.svg  style="width:24px;"> Original 

Die Darstellungsart **Original** überlagert nicht die {{PropertyView/de|Display Mode}} von Objekten.

![](images/Std_DrawStyleAsIs_example.png ) 
*4 identische Objekte mit jeweils unterschiedlichen Display-Modes (von links nach rechts: 'Punkte', 'Drahtgitter', 'Schattiert' und 'Flat lines') mit der aktivierten Darstellungsart 'Original'*

### <img alt="" src=images/Std_DrawStylePoints.svg  style="width:24px;"> Punkte 

Die Darstellungsart **Punkte** überlagert die {{PropertyView/de|Display Mode}} von Objekten. Diese Darstellungsart entspricht dem Display_Mode \'Points\'. Knoten werden in deckenden Farben dargestellt. Kanten und Flächen werden nicht dargestellt.

![](images/Std_DrawStylePoints_example.png ) 
*Dieselben Objekte mit Darstellungsart 'Punkte' aktiviert*

### <img alt="" src=images/Std_DrawStyleWireFrame.svg  style="width:24px;"> Drahtgitter 

Die Darstellungsart **Drahtgitter** überlagert die {{PropertyView/de|Display Mode}} von Objekten. Diese Darstellungsart entspricht dem Display_Mode \'Wireframe\'. Knoten und Kanten werden in deckenden Farben dargestellt. Flächen werden nicht dargestellt.

![](images/Std_DrawStyleWireframe_example.png ) 
*Dieselben Objekte mit Darstellungsart 'Drahtgitter' aktiviert*

### <img alt="" src=images/Std_DrawStyleHiddenLine.svg  style="width:24px;"> Versteckte Linie 

Die Darstellungsart **Versteckte Line** überlagert die {{PropertyView/de|Display Mode}} von Objekten. Objekte werden dargestellt, als wären sie in Dreiecksnetzen Konvertiert

![](images/Std_DrawStyleHiddenLine_example.png ) 
*Dieselben Objekte mit Darstellungsart 'Hidden ' aktiviert*

### <img alt="" src=images/Std_DrawStyleNoShading.svg  style="width:24px;"> Keine Schattierung 

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

## Hinweise

-   Objekte in einer [3D-Ansicht](3D_view/de.md) besitzen auch eine {{PropertyView/de|Draw Style}}. Diese Eigenschaft bestimmt die Linienart, die für die Kanten verwendet wird. Der Befehl Std Darstellungsart überlagert diese Eigenschaft nicht.
-   Ein Makro zum Umschalten zwischen zwei Darstellungsarten findet sich unter: [Macro Toggle Drawstyle](Macro_Toggle_Drawstyle.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std DrawStyle/de
