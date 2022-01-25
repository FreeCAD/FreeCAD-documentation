---
- GuiCommand:/de
   Name:Ship Load‏‎
   Name/de:Schiffslast
   MenuLocation:Schiffkonstruktion → Laden einer Beispielschiffsgeometrie
   Workbenches:[Schiff](Ship_Workbench/de.md)
   Shortcut:
   SeeAlso:
---

# Ship Geometries Examples/de

## Beschreibung


<div class="mw-translate-fuzzy">

Schiff arbeitet über **Schiffseinheiten**, die auf der bereitgestellten Geometrie erstellt werden müssen. Die Geometrie muss ein Festkörper oder ein Satz von Festkörpern sein, wobei folgende Kriterien berücksichtigt werden müssen:

-   Die gesamte Rumpfgeometrie muss bereitgestellt werden (einschließlich symmetrischer Körper).
-   Die Steuerbordgeometrie muss im negativen *y*-Bereich enthalten sein.
-   Ursprungspunkt (0,0,0) ist der Schnittpunkt der *Mittschiffssektion* (Mittelpunkt zwischen der hinteren und vorderen Senkrechten) und der *Basislinie*.


</div>

Ship works over **Ship entities**, that must be created on top of provided geometry. Geometry must be a solid, or set of solids. The following criteria must be taken into account:

-   All hull geometry must be provided (including symmetric bodies).
-   Starboard geometry must be included at negatives *y* domain.
-   Origin (0,0,0) point is the **Midship section** (Midpoint between after and forward perpendicular) and **base line** intersection.

![](images/FreeCAD-Ship-SignCriteria.jpg )


<div class="mw-translate-fuzzy">

![\|Schematische Ansicht der Vorzeichenkriterien](images/FreeCAD-Ship-SignCriteria.jpg ) 
*Kriterien für Schiffszeichen*


</div>

## Anwendung

Um neuen Anwendern zu helfen, enthält Schiff ein Ladeprogramm für Geometriebeispiele mit den folgenden Auswahlmöglichkeiten:

-   Serie 60 von der Universität Iowa
-   Kanonisches Schiff Wigley
-   Katamaran der Serie 60
-   Wigley Katamaran


<div class="mw-translate-fuzzy">

1.  Aufruf des Schiff Ladeprogramms für Geometriebeispiele, entweder durch
    -   drücken auf das <img alt="" src=images/Ship_Load.svg  style="width:24px;">-Symbol in der Werkzeugleiste
    -   wählen von **Ship design → Lade ein Beispiel einer ‏‎Schiffsgeometrie** aus dem Menü
2.  Ein Aufgaben-Dialogfeld wird angezeigt, aus dem eine Beispielschiffsgeometrie ausgewählt werden kann.
    -   Wähle z.B. **Series 60 from Iowa Universität** und drücke **OK**
3.  Das Werkzeug lädt ein neues Dokument mit der entsprechenden Geometrie.


</div>


**Warnung, bevor irgendetwas editiert wird! Du arbeitest jetzt mit der ursprünglichen Beispieldatei. Um das unbearbeitete Original-Beispiel zu erhalten, musst du es zuerst als neue Datei speichern, bevor irgendetwas bearbeitet werden kann.**

## Tutorien

-   [FreeCAD Schiffs s60 Tutorium](FreeCAD-Ship_s60_tutorial/de.md)
-   [FreeCAD Schiffs s60 Tutorium (II)](FreeCAD-Ship_s60_tutorial_(II)/de.md)





{{Ship_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Ship Geometries Examples/de
