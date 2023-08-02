---
- GuiCommand:
   Name: TechDraw FaceCenterLine
   Name/de: TechDraw FlächenMittellinie
   MenuLocation: TechDraw -> Linien hinzufügen -> Mittellinie zu Fläche hinzufügen
   Workbenches: TechDraw_Workbench/de
   Version: 0.19
   SeeAlso: TechDraw_CosmeticVertex/de, TechDraw_2LineCenterLine/de, TechDraw_2PointCenterLine/de, TechDraw_CosmeticEraser/de
---

# TechDraw FaceCenterLine/de


</div>



## Beschreibung

Das Werkzeug \"TechDraw FlächenMittellinie\" fügt ausgewählten Flächen eine Mittellinie hinzu.

<img alt="" src=images/TechDraw_FaceCenterLine_Sample.png  style="width:400px;">


<div class="mw-translate-fuzzy">



*Mittellinie einer Fläche hinzufügen (links: Fläche ausgewählt / rechts: Mittellinie hinzugefügt)*


</div>

## Usage create 


<div class="mw-translate-fuzzy">

1.  Eine oder mehrere Flächen in einer Ansicht auswählen.
2.  Die Schaltfläche **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> Mittellinie zu Fläche(n) hinzufügen** drücken.
3.  Ein Dialogfeld wird geöffnet, in dem die Attribute der neuen Mittellinie angegeben werden können.
4.  Eine Mittellinie wird in der Mitte des Begrenzungsrahmens der ausgewählten Fläche(n) hinzugefügt.


</div>

## Usage edit 


<div class="mw-translate-fuzzy">

Jede der Schaltflächen für Mittellinien-Befehle (**<img src="images/TechDraw_FaceCenterLine.svg" width=16px> Mittellinie zu Fläche(n) hinzufügen**, **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> [Mittellinie zwischen 2 Linien hinzufügen](TechDraw_2LineCenterLine/de.md)**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> [Mittellinie zwischen 2 Punkten hinzufügen](TechDraw_2PointCenterLine/de.md)**) kann verwendet werden, um Mittellinien zu bearbeiten.


</div>


<div class="mw-translate-fuzzy">

1.  Eine Mittellinie auswählen.

2.  Eine beliebige Schaltfläche für Mittellinien-Befehle drücken.

3.  Ein Dialogfeld wird geöffnet, in dem sich die Attribute der Mittellinie bearbeiten lassen.

4.  
    **OK**drücken, um die Änderungen zu sehen.


</div>




<div class="mw-translate-fuzzy">

## Eigenschaften


</div>


<div class="mw-translate-fuzzy">

1.  Modus (Auswahlknöpfe):
    -   **Vertikal**: Erzwingt eine vertikale Mittellinie
    -   **Horizontal**: Erzwingt eine Mittellinie horizontal
    -   **Ausgerichtet**: Folgt der allgemeinen Richtung von Kante für 2 Kanten Mittellinie
2.  **Shift Horiz**: Verschiebt die Mittellinie nach links oder rechts von ihrer normalen Position
3.  **Shift Vert**: Verschiebt die Mittellinie aus ihrer normalen Position nach oben oder unten
4.  **Rotate**: Dreht die Mittellinie um ihren Mittelpunkt (Grad. + gegen den Uhrzeigersinn, - im Uhrzeigersinn)
5.  **Extend**: Macht die Mittellinie um diesen Betrag länger
6.  **Color**: Farbe der Mittellinie
7.  **Weight**: Dicke der Mittellinie
8.  **Style**: <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Durchgehend, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Strich, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Punkt, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> StrichPunkt, <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> StrichPunktPunkt


</div>



## Hinweise


<div class="mw-translate-fuzzy">

-   FlächenMittellinie wird eventuell zwei Ansicht-Eigenschaften ersetzen:
    -   
        {{PropertyView/de|HorizCenterLine}}
        
        : Zeigt eine horizontale Mittellinie durch die Ansicht.

    -   
        {{PropertyView/de|VertCenterLine}}
        
        : Zeigt eine vertikale Mittellinie durch die Ansicht.


</div>

## Properties

Centerlines have no properties of their own, as they are not document objects.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw FaceCenterLine/de
