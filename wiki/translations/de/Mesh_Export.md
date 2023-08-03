---
 GuiCommand:
   Name: Mesh Export
   Name/de: Polygonnetz Export
   MenuLocation: Polygonnetze , Polygonnetz exportieren...
   Workbenches: Mesh_Workbench/de
   SeeAlso: Std_Export/de, Import_Export/de
---

# Mesh Export/de

## Beschreibung

Der Befehl **Polygonnetz Exportieren** exportiert ein Polygonnetzobjekt in ein Polygonnetzdateiformat. Es werden mehrere Dateiformate unterstützt.

## Anwendung

1.  Wähle ein einzelnes Netzobjekt aus.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Drücke den **<img src="images/Mesh_Export.svg" width=16px> [Polygonnetz Exportieren](Mesh_Export/de.md)**.
    -   Wähle die **Polygonnetze → <img src="images/Mesh_Export.svg" width=16px> Polygonnetz exportieren...** aus dem Menü.
    -   Wähle die **<img src="images/Mesh_Export.svg" width=16px> Polygonnetz exportieren...** aus dem Kontextmenü der [Baumansicht](Tree_view/de.md) oder der [3D Ansicht](3D_view/de.md).
3.  Wähle im Dialogfeld das richtige Dateiformat aus.
4.  Gib einen Dateinamen ein. Wenn du im vorherigen Schritt die Option {{Value|Alle Dateien (*.*)}} gewählt hast und hier keine Dateierweiterung angibst, wird die Erweiterung **.stl** verwendet.
5.  Drücke die **Speichern** Schaltfläche.

## Hinweise

Es gibt einige [Exporteinstellungen verwandt mit Polygonnetzformaten](Import_Export_Preferences/de#Polygonnetz_Formate/de.md), aber diese werden von Befehlen, die zu diesem Arbeitsbereich gehören, nicht verwendet. Sie werden von dem Befehl [Std Export](Std_Export/de.md) verwendet.

## Einstellungen

-   Der zuletzt verwendete Dateispeicherort wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BasisAnwendung → Einstellungen → Allgemein → FileOpenSavePath**.

## Skripten

Siehe auch: [FreeCAD Skripten Grundlagen](FreeCAD_Scripting_Basics/de.md).

Um Objekte (einschließlich Polygonnetzobjekte) in ein Polygonnetzdateiformat zu exportieren, verwende die Methode `exportieren` des Polygonnetz Moduls.


```python
import FreeCAD
import Mesh

doc = FreeCAD.ActiveDocument

Mesh.export([doc.Cone, doc.Cylinder], 'D:/testfiles/mymodel.stl')
```





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Export/de
