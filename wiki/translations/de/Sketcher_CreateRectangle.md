---
 GuiCommand:
   Name: Sketcher CreateRectangle
   Name/de: Sketcher RechteckErstellen
   MenuLocation: Skizze , Skizzengeometrien , Rechteck erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **R**
   SeeAlso: Sketcher_CreateOblong/de, Sketcher_CreatePolyline/de
---

# Sketcher CreateRectangle/de



## Beschreibung

Dieses Werkzeug zeichnet ein Rechteck, indem zwei gegenüberliegende Punkte gegriffen werden. Wenn das Werkzeug gestartet wird, ändert sich der Mauszeiger in ein weißes Kreuz mit einem roten Rechtecksymbol. Die Koordinaten des Mauszeigers werden daneben in Echtzeit blau angezeigt.

Um ein Rechteck über einen Mittelpunkt und einen Kantenpunkt zu definieren, verwende das Werkzeug [Zentriertes Rechteck](Sketcher_CreateRectangle_Center/de.md).

![](images/SketcherCreateRectangleExample.png‎ )



## Anwendung

-   Nach Drücken der <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> *Rechteck erstellen* Werkzeugleisten Taste, klicke einmal, um die erste Ecke zu setzen, bewege dann die Maus und klicke ein zweites Mal, um die gegenüberliegende Ecke zu setzen.
-   Drücken von **Esc** oder Klicken mit der rechten Maustaste bricht die Funktion ab.



## Hinweise

-   Wenn sie gestartet werden, fügen die Rechteck-Werkzeuge einen Abschnitt **Versatz Parameter** im oberen Teil des [Aufgaben-Bereichs](Task_panel/de.md) des Sketchers hinzu. ({{Version/de|0.22}}). Er enthält:

1.  Ein Auswahlfeld **Modus** in dem eine der Methoden zum Zeichnen des Rechtecks ausgewählt werden kann:
    -   Corner, length & width (Eckpunkt, Länge & Breite)
    -   Center, length & width (Mittelpunkt, Länge & Breite)
    -   3 corners (3 Eckpunkte)
    -   Center and two corners (Mittelpunkt und zwei Eckpunkte)
2.  Eine Checkbox **Abgerundete Ecken**, um das Rechteck mit runden Ecken zu versehen.
3.  Eine Checkbox **Rahmen**, um eine Kontur mit konstantem Abstand von dem (verrundeten) Rechteck zu erstellen.

-   Alle drei Schaltflächen in dieser Auswahl starten jetzt dasselbe Werkzeug, aber mit unterschiedlichen voreingestellten Kombinationen von Modus und Optionen, die auch nach dem ersten Klick noch geändert werden können.
-   Wenn **Abgerundete Ecken** aktiviert ist, die Versatzkontur innen verläuft und der Versatzwert größer als der Eckradius ist, wird die Versatzkontur ohne Verrundngen erstellt.
-   Die Methoden **3 corners**, (3 Eckpunkte) und **Center and two corners** (Mittelpunkt und zwei Eckpunkte) erstellen eher Parallelogramme als Rechtecke.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRectangle/de
