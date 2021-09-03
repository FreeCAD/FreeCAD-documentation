---
- GuiCommand:/de
   Name:PartDesign Plane
   Name/de:PartDesign Bezugsebene erstellen
   MenuLocation:PartDesign → Bezugsebene erstellen
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign Bezugspunkt](PartDesign_Point/de.md), [PartDesign Bezugslinie](PartDesign_Line/de.md)
---


</div>

## Beschreibung

Erstelle eine **Bezugsebene** (DatumPlane) die als Referenz für Skizzen oder andere Bezugselemente genutzt werden kann. Skizzen können auf einer Bezugsebene erstellt werden. ![](images/Datum_plane.png ) *Eine Bezugsebene, die drei Ecken eines Quaders schneidet mit einem Zylinder der aus einer Skizze auf dieser Bezugsebene erzeugt wurde.*

## Voraussetzungen

In FreeCAD 0.18 kann eine Bezugsebene nur innerhalb eines <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Körpers](PartDesign_Body.md) erstellt werden. Jeder Körper hat einen Ursprung, der durch Voreinstellung versteckt ist. Um sich auf diese Ursprungsebenen beziehen zu können, müssen sie sichtbar gemacht werden. Dies sollte gemacht werden, bevor eine Bezugsebene erstellt wird.

## Anwendung


<div class="mw-translate-fuzzy">

1.  Auf die Schaltfläche **<img src="images/PartDesign_Plane.svg" width=16px> [Bezugsebene erstellen](PartDesign_Plane/de.md)** klicken.
2.  Die Parameter der Bezugsebene einstellen. Wähle eine erste Referenz in der 3D-Ansicht, um die [verfügbaren Zuordunungsmodi](Part_Attachment.md) einzugrenzen.
3.  Abhängig von dem ausgewählten Bezugselement können eine oder mehrere Befestigungsmodi in der Liste zur Verfügung stehen. Der am wahrscheinlichsten scheinende Modus wird automatisch ausgewählt und erscheint fettgedruckt in der Liste. Der Text *Angehängt im Modus:* zusammen mit dem Befestigungsmodus erscheint in grüner Schrift im oberen Bereich des Parameterdialogs.
4.  Weitere Referenzen können durch Klicken auf die nächste **Referenz** Schaltfläche hinzugefügt werden. Eine angeklickte Schaltfläche wechselt die Beschriftung zu *Auswählen\...* bis eine Auswahl getroffen wurde.
5.  Aus der Liste den gewünschten Befestigungsmodus auswählen.
6.  **Versatz:** zur Festlegung von Werten für den Versatz beim Anhängen oder Referenzieren. **Hinweis**, dass der x, y und z - Versatz sich auf das lokale Koordinatensystem der Bezugsebene bezieht und nicht auf das globale. Deshalb ist der z-Versatz immer ein Versatz entlang des Normalenvektors zur Bezugsebene.
7.  **Drehen:** Das Ändern des Wertes \"Around x-axis\" läßt die Ebene um ihre lokale X-Achse drehen. Das Ändern des Wertes \"Around y-axis\" läßt die Ebene um die lokale Z-Achse drehen. Das Ändern des Wertes \"Around z-axis\" läßt die Ebene um die lokale Y-Achse drehen.
8.  Klicke **OK**.


</div>

## Optionen


<div class="mw-translate-fuzzy">

Mit einem Doppelklick auf die Beschriftung der Bezugsebene in der Baumstruktur oder durch einen Rechtsklick und Auswählen von **Bezug ändern** im Kontextmenü können die Einstellungen der Bezugsebene geändert werden. Mehr Details zum Anhängemodus und dem Positionsversatz gibt es in [Attachment](Part_Attachment/de.md).


</div>

## Eigenschaften

-    {{PropertyData/de|Abbildungsmodus}}: zeigt den verwendeten Modus zum Anhängen an.

-    {{PropertyData/de|Anhangversatz}}: fügt eine Transformation (Verschiebung und Rotation) ein, bezogen auf die Position des Anhanges.

-    {{PropertyData/de|Ettikett}}: Objektname; der Name kann zur Arbeitserleichterung geändert werden.





{{PartDesign Tools navi

}} 
