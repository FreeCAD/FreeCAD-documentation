---
- GuiCommand:
   Name: Mesh ImportMesh‏‎
   Name/de: Polygonnetz Import
   MenuLocation: Polygonnetze -> Polygonnetz importieren...
   Workbenches: Mesh_Workbench/de
   SeeAlso: Std_Import/de,Std_Open/de, Import_Export/de
---

# Mesh Import/de

## Beschreibung

Der Befehl **Polygonnetz Import** importiert Geometrie aus einem Netzdateiformat in das aktive Dokument. Mehrere Dateiformate werden unterstützt. Der Befehl erzeugt ein nicht-parametrisches Polygonnetzobjekt, ein [Polygonnetz Formelement](Mesh_Feature/de.md).

## Anwendung

#\* Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:

#\* Drücke den **<img src="images/Mesh_Import.svg" width=16px> [Polygonnetz Import](Mesh_Import/de.md)**.

#\* Wähle die **Polygonnetze → <img src="images/Mesh_Import.svg" width=16px> Polygonnetz importieren...** aus dem Menü.

#\* Wähle die **<img src="images/Mesh_Import.svg" width=16px> Polygonnetz importieren...** aus dem Kontextmenü der [Baumansicht](3D_view/de.md) oder der [3D Ansicht](3D_view/de.md) aus. Diese Option ist nur verfügbar, wenn ein bestehendes Polygonnetzobjekt ausgewählt wurde. Beachte, dass das ausgewählte Objekt durch den Befehl eigentlich nicht verwendet oder verändert wird.

1.  Wähle optional das richtige Dateiformat im Dialogfeld aus.
2.  Wähle eine Datei aus.
3.  Drücke die **Öffnen** Schaltfläche.

## Supported file formats 

The command supports: stl, ast, bms, obj, off, iv, ply, nas and bdf files. For the NASTRAN (nas/bdf) file format, only GRID, CTRIA3 and CQUAD4 cards are supported.

## Einstellungen

-   Der zuletzt verwendete Dateispeicherort wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BasisAnwendung → Einstellungen → Allgemein → FileOpenSavePath**.

## Eigenschaften

Siehe: [Polygonnetz Formelement](Mesh_Feature/de.md).

## Skripten

Siehe auch: [FreeCAD Skripten Grundlagen](FreeCAD_Scripting_Basics/de.md).

Um eine Polygonnetzdatei zu importieren, verwende die Methode `Einfügen` des Polygonnetz Moduls.


```python
import Mesh
Mesh.insert('D:/testfiles/cylinder.stl')
```





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Import/de
