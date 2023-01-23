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

Die Darstellungsart **Versteckte Line** überlagert die {{PropertyView/de|Display Mode}} von Objekten. Objekte werden dargestellt, als wären sie in Dreiecksnetze konvertiert.

![](images/Std_DrawStyleHiddenLine_example.png ) 
*Dieselben Objekte mit Darstellungsart 'Versteckte Linie' aktiviert*



### <img alt="" src=images/Std_DrawStyleNoShading.svg  style="width:24px;"> Keine Schattierung 

Die Darstellungsart **Keine Schattierung** überlagert die {{PropertyView/de|Display Mode}} von Objekten. Punkte, Kanten und Flächen werden gleichmäßig, deckend eingefärbt dargestellt.

![](images/Std_DrawStyleNoShading_example.png ) 
*Dieselben Objekte mit Darstellungsart 'Keine Schattierung' aktiviert*



### <img alt="" src=images/Std_DrawStyleShaded.svg  style="width:24px;"> Schattiert 

Die Darstellungsart **Schattiert** überlagert die {{PropertyView/de|Display Mode}} von Objekten. Punkte und Kanten werden nicht dargestellt. Flächen werden abhängig von ihrer Ausrichtung beleuchtet.

![](images/Std_DrawStyleShaded_example.png ) 
*Dieselben Objekte mit Darstellungsart 'Schattiert' aktiviert*



### <img alt="" src=images/Std_DrawStyleFlatLines.svg  style="width:24px;"> Flache Linien 

Die Darstellungsart **Flache Linien** überlagert die {{PropertyView/de|Display Mode}} von Objekten. Diese Darstellungsart entspricht demDisplay-Mode \'Flat Lines\' von Objekten. Punkte und Kanten werden deckend eingefärbt dargestellt. Flächen werden abhängig von ihrer Ausrichtung beleuchtet.

![](images/Std_DrawStyleFlatLines_example.png ) 
*Dieselben Objekte mit Darstellungsart 'Flache Linien' aktiviert*



## Hinweise

-   Objekte in einer [3D-Ansicht](3D_view/de.md) besitzen auch eine {{PropertyView/de|Draw Style}}. Diese Eigenschaft bestimmt die Linienart, die für die Kanten verwendet wird. Der Befehl Std Darstellungsart überlagert diese Eigenschaft nicht.
-   Ein Makro zum Umschalten zwischen zwei Darstellungsarten findet sich unter: [Macro Toggle Drawstyle](Macro_Toggle_Drawstyle.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std DrawStyle/de
