---
- GuiCommand:/de
   Name:PartDesign CoordinateSystem
   Name/de:PartDesign Koordinatensystem
   MenuLocation:PartDesign → Erstelle ein lokales Koordinatensystem
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.18
   SeeAlso:[Datum point](PartDesign_Point.md), [PartDesign Datum line](PartDesign_Line.md), [Datum plane](PartDesign_Plane.md)
---

## Beschreibung

Erzeugt ein **lokales Koordinatensystem**, welches als Referenz für andere Bezugsgeometrie verwendet werden kann. Es hilft auch, die Orientierung der referenzierten Bezugsgeometrie im 3D Raum zu ermitteln. ![](images/PartDesign_LocalCoordinateSystem_Example.png ) {{Caption | Lokales Koordinatensystem, das aus dem Ursprung einer Bezugsebene entspring.}}

## Anwendung

1.  Drücken Sie die **<img src=images/PartDesign_CoordinateSystem.svg style="width:16px"> [Erstelle lokales Koordinatensystem](PartDesign_CoordinateSystem.md)**.
2.  Definieren Sie die Parameter des Koordinatensystems. Wählen Sie in der 3D-Ansicht eine erste Referenz aus, um die verfügbaren Anhangsmodi zu filtern.
3.  Abhängig von der ausgewählten Referenz stehen in der Liste möglicherweise ein oder mehrere Anhangsmodi zur Verfügung. Das wahrscheinlichste wird automatisch ausgewählt und in der Liste fett dargestellt. Der Text \'\' Mit Modus verbunden \'\' wird zusammen mit dem Namen des Anhangsmodus oben im Parameterfenster grün angezeigt.
4.  Um eine weitere Referenz hinzuzufügen, drücken Sie die nächste Taste {{Button | Referenz}}. Nach dem Drücken ändert sich das Label in \'\' Auswählen \... \'\', bis eine Auswahl getroffen wird.
5.  Wählen Sie in der Liste einen Anhangmodus aus.
6.  Anhängeoffsetwerte definieren.
7.  Drücken Sie {{Button | OK}}.

## Optionen

Mit einem Doppelklick auf den Eintrag DatumPlane in der Baumstruktur oder durch einen Rechtsklick und Auswählen von **Bezug ändern** in dem Kontextmenü können die Einstellungen der Bezugsebene geändert werden. Mehr Details zum Befestigungsmodus und dem Befestigungsversatz gibt es in [Attachment](Part_Attachment/de.md).

## Eigenschaften

### Daten

-    **MapMode**: listet den verwendeten Anhängemodus auf.

-    **Attachment Reversed**: Gibt an, ob das Koordinatensystem in seiner Ausrichtung umgekehrt ist.

-    **Attachment Offset**: Wendet eine Transformation (Übersetzung und Drehung) in Bezug auf die Platzierung von Anhängen an.

-    **Placement**: Gibt die Koordinaten und Ausrichtung des Ursprungs des Koordinatensystems an .

-    **Label**: Name des Objekts. Dieser Name kann beliebig geändert werden.

## Skripten


```python
lcs = App.activeDocument().addObject( 'PartDesign::CoordinateSystem', 'LCS' )
```





{{PartDesign Tools navi

}} 
