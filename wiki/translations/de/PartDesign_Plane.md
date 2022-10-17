---
- GuiCommand   */de
   Name   *PartDesign Plane
   Name/de   *PartDesign Bezugsebene erstellen
   MenuLocation   *Part Design → Bezugselement erstellen → Bezugsebene erstellen
   Workbenches   *[PartDesign](PartDesign_Workbench/de.md)
   Version   *0.17
   SeeAlso   *[PartDesign Bezugspunkt](PartDesign_Point/de.md), [PartDesign Bezugslinie](PartDesign_Line/de.md)
---

# PartDesign Plane/de

## Beschreibung

Erstelle eine **Bezugsebene** (DatumPlane) die als Referenz für Skizzen oder andere Bezugselemente genutzt werden kann. Skizzen können auf einer Bezugsebene erstellt werden. ![](images/Datum_plane.png ) *Eine Bezugsebene, die drei Ecken eines Quaders schneidet mit einem Zylinder der aus einer Skizze auf dieser Bezugsebene erzeugt wurde.*

## Voraussetzungen

In FreeCAD 0.18 kann eine Bezugsebene nur innerhalb eines <img alt="" src=images/PartDesign_Body.svg  style="width   *16px;"> [Körpers](PartDesign_Body.md) erstellt werden. Jeder Körper hat einen Ursprung, der durch Voreinstellung versteckt ist. Um sich auf diese Ursprungsebenen beziehen zu können, müssen sie sichtbar gemacht werden. Dies sollte gemacht werden, bevor eine Bezugsebene erstellt wird.

## Anwendung

1.  Schaltfläche **<img src="images/PartDesign_Plane.svg" width=16px> [Bezugsebene erstellen](PartDesign_Plane/de.md)** drücken.

2.  Die Parameter der Bezugsebene definieren. Eine erste Referenz in der 3D-Ansicht auswählen, um die verfügbaren [Part Befestigungsarten](Part_EditAttachment/de.md) zu filtern.

3.  Abhängig von der ausgewählten Referenz, können eine oder mehrere Verbindungsarten in der Liste vorhanden sein. Die wahrscheinlichste wird automatisch ausgewählt und in der Liste fett dargestellt. Der Text *Angehängt im Modus   ** zusammen mit dem Namen der Verbindungsart erscheint in grün über der Liste der Referenzen.

4.  Um eine weitere Referenz hinzuzufügen, drückt man die nächste Schaltfläche **Referenz2**. Sobald sie gerückt wurde ändert sich die Beschriftung zu *Auswählen\...*, bis etwas ausgewählt wurde.

5.  Einen Befestigungsmodus aus der Liste Wählen.

6.  **Versatz   *** zur Festlegung von Werten für den Versatz beim Anhängen oder Referenzieren. **Hinweis**   * Der X-, Y- und Z-Versatz bezieht sich auf das lokale Koordinatensystem der Bezugsebene und nicht auf das globale. Deshalb ist der Z-Versatz immer ein Versatz entlang des Normalenvektors der Bezugsebene.

7.  **Drehen   *** Das Ändern des Wertes \"Um die X-Achse\" läßt die Ebene um ihre lokale X-Achse drehen. Das Ändern des Wertes \"Um die Y-Achse\" läßt die Ebene um die lokale Y-Achse drehen. Das Ändern des Wertes \"Around z-axis\" läßt die Ebene um die lokale Z-Achse drehen.

8.  
    **OK**drücken.

## Optionen

Mit einem Doppelklick auf die Beschriftung der Bezugsebene in der Baumstruktur oder durch einen Rechtsklick und Auswählen von **Bezug ändern** im Kontextmenü können die Einstellungen der Bezugsebene geändert werden. Mehr Details zum Anhängemodus und dem Positionsversatz gibt es in [Part Anhang bearbeiten](Part_EditAttachment/de.md).

## Eigenschaften

-    {{PropertyData/de|Abbildungsmodus}}   * zeigt den verwendeten Modus zum Anhängen an.

-    {{PropertyData/de|Anhangversatz}}   * fügt eine Transformation (Verschiebung und Rotation) ein, bezogen auf die Position des Anhanges.

-    {{PropertyData/de|Ettikett}}   * Objektname; der Name kann zur Arbeitserleichterung geändert werden.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Plane/de
