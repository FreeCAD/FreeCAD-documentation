---
 GuiCommand:
   Name: TechDraw FaceCenterLine
   Name/de: TechDraw FlächenMittellinie
   MenuLocation: TechDraw , Linien hinzufügen , Mittellinie zu Fläche hinzufügen
   Workbenches: TechDraw_Workbench/de
   Version: 0.19
   SeeAlso: TechDraw_2LineCenterLine/de, TechDraw_2PointCenterLine/de
---

# TechDraw FaceCenterLine/de



## Beschreibung

Das Werkzeug \"TechDraw FlächenMittellinie\" fügt ausgewählten Flächen eine Mittellinie hinzu.

<img alt="" src=images/TechDraw_FaceCenterLine_Sample.png  style="width:400px;"> 
*Mittellinie zu einer Fläche hinzufügen (links: Fläche ausgewählt / rechts: Mittellinie hinzugefügt)*



## Anwendung, Erstellen 

1.  Eine oder mehrere Flächen in einer Ansicht auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> [Mittellinie zu Fläche(n) hinzufügen](TechDraw_FaceCenterLine/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Maßeinträge → <img src="images/TechDraw_FaceCenterLine.svg" width=16px> Mittellinie zu Fläche(n) hinzufügen** auswählen.
3.  Ein Aufgaben-Bereich wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
4.  Die Schaltfläche **OK** zum Bestätigen drücken.
5.  Eine Mittellinie wird am Mittelpunkt des Begrenzungsrahmens der ausgewählten Fläche(n) hinzugefügt.



## Anwendung, Bearbeiten 

Jedes der Mittellinienwerkzeuge (<img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:16px;"> Mittellinie zu Fläche(n) hinzufügen, <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:16px;"> [Mittellinie zwischen 2 Linien hinzufügen](TechDraw_2LineCenterLine/de.md) oder <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:16px;"> [Mittellinie zwischen 2 Punkten hinzufügen](TechDraw_2PointCenterLine/de.md)) kann verwendet werden, um Mittellinien zu bearbeiten.

1.  Eine Mittellinie auswählen.
2.  Ein beliebiges Mittellinienwerkzeug aufrufen.
3.  Ein Dialogfeld wird geöffnet. Siehe [Optionen](#Optionen.md) für Weitere Informationen.
4.  Die Schaltfläche **OK** zum Bestätigen drücken.



## Optionen

-   **Orientatierung**:
    -   **Vertikal**: Gibt die vertikale Ausrichtung für die Mittellinie vor. Wird für 2PunkteMittellinien ignoriert.
    -   **Horizontal**: Gibt die horizontale Ausrichtung für die Mittellinie vor. Wird für 2PunkteMittellinien ignoriert.
    -   **Ausgerichtet**: Nicht verfügbar für FlächenMittellinien. Gibt der Mittellinie vor, der ermittelten Ausrichtung der ausgewählten Kanten für 2LinienMittellinien zu folgen. Wird für 2PunkteMittellinien ignoriert.
-   **Horizontal verschieben**: Bewegt die Mittellinie aus ihrer normalen Position nach links oder rechts.
-   **Vertikal verschieben**: Bewegt die Mittellinie aus ihrer normalen Position nach oben oder unten.
-   **Drehen**: Dreht die Mittellinie um ihren Mittelpunkt (in Grad. + gegen den Uhrzeigersinn, - im Uhrzeigersinn).
-   **Verlängern um**: Verlängert die Mittellinie um diesen Wert.
-   **Farbe**: Die Farbe der Mittllinie.
-   **Stärke**: Strichstärke der Mittellinie.
-   **Stil**: Linienart der Mittellinie. Die Optionen sind:
    -   <img alt="" src=images/Continuous-line.svg  style="width:20px;"> 
**Volllinie**
    -   <img alt="" src=images/Dash-line.svg  style="width:20px;"> 
**Strichlinie**
    -   <img alt="" src=images/Dot-line.svg  style="width:20px;"> 
**Punkt**
    -   <img alt="" src=images/DashDot-line.svg  style="width:20px;"> 
**Strich-Punkt**
    -   <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> 
**Strich-Zweipunkt**



## Hinweise

-   Zum Entfernen einer Mittellinie wird <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw HilfsobjektEntfernen](TechDraw_CosmeticEraser/de.md) verwendet.
-   FlächenMittellinien ersetzen letztlich zwei Ansicht-Eigenschaften:
    -   
        {{PropertyView/de|HorizCenterLine}}
        
        : Zeigt eine horizontale Mittellinie durch die Ansicht.

    -   
        {{PropertyView/de|VertCenterLine}}
        
        : Zeigt eine vertikale Mittellinie durch die Ansicht.



## Eigenschaften

Hilfslinien haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw FaceCenterLine/de
