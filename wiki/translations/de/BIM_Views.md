---
- GuiCommand:Addon/de
   Name: BIM Views
   Name/de: BIM Ansichten
   Workbenches: <img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench/de.md)
   Addon: BIM
   MenuLocation: Verwalten - Ansichten
---

# BIM Views/de

## Beschreibung

Der BIM Ansichten und Ebenenmanager ist ein andockbares Fenster, das sich unterhalb der normalen Baumansicht öffnet und alle [GebäudeTeile](Arch_BuildingPart/de.md) und [Arbeitsebenen Proxies](Draft_WorkingPlaneProxy/de.md) deines Modells enthält.

Das Ziel dieses Fensters ist es, einen schnellen Zugriff auf deine Ebenen- und Arbeitsebenen-Konfigurationen zu ermöglichen, ohne dass du durch den Baum navigieren musst, um sie zu finden.

<img alt="" src=images/BIM_views_screenshot.png  style="width:800px;">

## Anwendung

Der BIM Ansichtenverwalter zeigt alle Ebenen (Gebäudeteile) und Arbeitsebenen Proxys deines Dokuments an. Er kann an einer beliebigen Stelle in der FreeCAD Oberfläche angedockt oder in einem eigenständigen Fenster belassen werden. Gebäudeteile zeigen auch ihre Ebene an (die Z Koordinate ihrer Positionierung).

-   Gleichzeitiges drücken von **Strg**+**9** oder klicken der <img alt="" src=images/BIM_Views.png  style="width:24px;">-Schaltfläche in der unteren rechten Ecke des Bildschirms zeigt oder verbirgt den BIM-Views-Manager
-   Anklicken eines beliebigen Eintrags wählt das entsprechende Objekt aus
-   Doppelklicken der Höhe einer Ebene ermöglicht die Änderung
-   Doppelklicken des Namens eines beliebigen Objekts setzt die Arbeitsebene darauf und, falls die **Restore View**-Option aktiviert ist und eine Ansichtskonfiguration darin gespeichert wurde, wird der Blickpunkt ebenfalls wiederhergestellt
-   Anklicken der **Add a new level**-Schaltfläche erstellt eine neue [Ebene](Arch_BuildingPart/de.md)
-   Anklicken der **Add a new working plane proxy**-Schaltfläche erstellt einen neuen [Arbeitsebenen-Proxy](Draft_WorkingPlaneProxy/de.md)
-   Anklicken der **Delete**-Schaltfläche löscht das ausgewählte Element
-   Anklicken der **Toggle on/off**-Schaltfläche schaltet eine ausgewählte Ebene ein/aus (genau wie die Leertaste)
-   Anklicken der **Isolate**-Schaltfläche schaltet alle Ebenen aus bis auf die ausgewählte
-   Anklicken der **Save camera position**-Schaltfläche speichert die aktuellen Ansichteinstellungen im ausgewählten Objekt, um sie beim Setzen der **Restore View**-Eigenschaft auf {{PropertyData/de|True}} wiederherzustellen
-   Anklicken der **Rename**-Schaltfläche erlaubt das Umbenennen eine ausgewählten Objekts



---
⏵ [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > BIM Views/de
