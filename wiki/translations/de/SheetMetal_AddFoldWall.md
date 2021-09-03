---
- GuiCommand:/de
   Name:SheetMetal AddFoldWall
   Name/de:SheetMetal Abkanten
   MenuLocation:SheetMetal → Fold a Wall
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**C** **F**
---

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:24px;"> [Abkanten](SheetMetal_AddFoldWall/de.md) kantet eine Fläche entlang einer gewählten Linie mit einem vorgegebenen Radius ab.

## Anwendung

1.  Eine ebene Fläche des Blechobjekts auswählen
2.  Eine komplanare Linie auswählen
3.  Schaltfläche  or use the keyboard shortcut: **C** then **F**.

## Eigenschaften

-    **Bend Line**: Biegelinie. Voreingestellt: none

-    **Position**: Lage der Biegelinie. Mögliche Werte: forward, middle, backward; Voreingestellt: forward

-    **angle**: Biegewinkel. Voreingestellt: 90.0

-    **base Object**: Basisobjekt. Voreingestellt: none

-    **invert**: Biegerichtung umkehren. Voreingestellt: False

-    **invert bend**: Abzukantende Seite wechseln. Voreingestellt: False

-    **kfactor**: Lage der neutralen Faser. Voreingestellt: 0.50

-    **radius**: Biegeradius. Voreingestellt: 1.0

-    **unfold**: Abwickeln. Voreingestellt: False

## Beispiel

<img alt="" src=images/SheetMetal_AddFoldWall-01.png  style="width:300px;"> 
*Ein einfacher Klipp*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Vorbereitung

Dieser Klipp wird aus einer Platine hergestellt, die dreimal abgekantet wird, d.h. es müssen vier Skizzen vorbereitet werden:

:   \- Eine für den Platinenzuschnitt
:   \- Eine für die Kantung an der Vorderkante
:   \- Eine für die Kantung nach oben
:   \- Eine für die Kantung nach unten

Der einfachste Weg, um sicherzustellen, dass eine Fläche der Platine (Rohling) und alle Biegelinien komplanar sind, ist das Erstellen aller Skizzen auf derselben Ebene - der X-Y-Ebene in diesem Falle.

Die Biegelinien könnten mit einem anderen Werkzeug erstellt werden, aber hey, wir haben einen <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench.md)!

<img alt="" src=images/SheetMetal_AddFoldWall-21.png  style="width:280px;"> <img alt="" src=images/SheetMetal_AddFoldWall-20.png  style="width:200px;"> 
*Skizzen auf ihrer gemeinsamen Ebene und ihre Darstellung im Konstruktionsbaum*

## Arbeitsablauf

1.  Eine Platine erzeugen
    1.  Die Skizze für den Platinenzuschnitt auswählen
    2.  Schaltfläche  oder das Tastenkürzel  <img alt="" src=images/SheetMetal_AddFoldWall-02.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-03.png  style="width:280px;"> 
2.  Abkanten der Vorderkante
    1.  **Unterseite** der Platine auswählen
    2.  Die \'\'\'Skizze \'\'\' namens ***Tip Fold line*** auswählen (vorzugsweise aus der Baumansicht)  (und nicht die Steuerung- bzw. Befehlstaste vergessen)
    3.  Schaltfläche  oder das Tastenkürzel  <img alt="" src=images/SheetMetal_AddFoldWall-10.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-04.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-05.png  style="width:280px;">
    4.  Die Kante sollte 90° nach unten zeigen, d.h. einige werte des Eigenschaftenfensters müssen geändert werden z.B.:  - Der Wert des *Biegewinkels* **angle** auf 60°  - Der Wert für *Biegerichtung umkehren* **invert** auf true für eine Kantung nach oben  
3.  Abkanten nach unten
    1.  **Unterseite** der Platine auswählen
    2.  Die \'\'\'Skizze \'\'\' namens ***Down-Fold line*** auswählen (vorzugsweise aus der Baumansicht)
    3.  Schaltfläche  oder das Tastenkürzel  <img alt="" src=images/SheetMetal_AddFoldWall-11.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-06.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-07.png  style="width:280px;">
    4.  Den Wert des *Biegewinkels* **angle** auf 92° setzen
    5.  Wenn die falsche Seite des Teiles bewegt wurde, den Wert für *Abzukantende Seite wechseln* **invertbend** auf true setzen  
4.  Abkanten nach oben
    1.  **Unterseite** der Platine auswählen
    2.  Die \'\'\'Skizze \'\'\' namens ***Up-Fold line*** auswählen (vorzugsweise aus der Baumansicht)
    3.  Schaltfläche  oder das Tastenkürzel  <img alt="" src=images/SheetMetal_AddFoldWall-12.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-08.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-09.png  style="width:280px;">
    4.  Den Wert des *Biegewinkels* **angle** auf 80° setzen
    5.  Wenn die Kantung nach unten ausgeführt wurde, Wert für *Biegerichtung umkehren* **invert** auf true setzen
    6.  Falls nötig, den Wert für *Abzukantende Seite wechseln* **invertbend** auf true setzen  

Fertig!

Achtung!: Im wirklichen Leben muss die Kantung nach oben vor der Kantung nach unten erfolgen. Nur die virtuelle CAD-Welt erlaubt es, durch festes Werkstoffe hindurch zu biegen. Auf diesem Weg ändert sich die Lage des feststehenden Bereiches nicht.  Alle Skizzen liegen auf derselben Ebene, um Skizzen, die bewegten Flächen zugeordnet sind, zu vermeiden.


</div>


</div>




[Category:SheetMetal{{\#translation:}}](Category:SheetMetal.md) [Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Command Reference{{\#translation:}}](Category:External_Command_Reference.md)
