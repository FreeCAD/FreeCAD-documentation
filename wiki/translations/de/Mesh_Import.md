---
 GuiCommand:
   Name: Mesh ImportMesh‏‎
   Name/de: Mesh Importieren
   MenuLocation: Netze , Netz importieren...
   Workbenches: Mesh_Workbench/de
   SeeAlso: Std_Import/de,Std_Open/de, Import_Export/de
---

# Mesh Import/de



## Beschreibung

Der Befehl **Mesh Import** importiert Geometrie aus einem Netz-Dateiformat in das aktive Dokument, wobei unterschiedliche Dateiformate unterstützt werden. Der Befehl erzeugt ein nicht-parametrisches Netzobjekt, ein [Mesh Formelement](Mesh_Feature/de.md).



## Anwendung

#\* Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:

#\* Die Schaltfläche **<img src="images/Mesh_Import.svg" width=16px> [Netz importieren...](Mesh_Import/de.md)** drücken.

#\* Den Menüeintrag **Netze → <img src="images/Mesh_Import.svg" width=16px> Netz importieren...** auswählen.

#\* Die Menüoption **<img src="images/Mesh_Import.svg" width=16px> Netz importieren...** im Kontextmenü der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) auswählen. Diese Option steht nur zur Verfügung, wenn ein vorhandenes Netzobjekt ausgewählt wurde. Man beachte, dass das ausgewählte Objekt durch den Befehl eigentlich nicht verwendet oder verändert wird.

1.  Wahlweise das richtige Dateiformat im Dialogfeld auswählen.
2.  Eine Datei auswählen.
3.  Die Schaltfläche **Öffnen** drücken.



## Unterstützte Dateiformate 

Der Befehl unterstützt: stl-, ast-, bms-, obj-, off-, iv-, ply-, nas- und bdf-Dateien. Für das NASTRAN-Dateiformat (nas/bdf) werden nur die Karten GRID, CTRIA3 und CQUAD4 unterstützt.



## Einstellungen

-   Der zuletzt verwendete Dateispeicherort wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp (BasisAnwendung) → Preferences (Einstellungen) → General (Allgemein) → FileOpenSavePath**.



## Eigenschaften

Siehe: [Mesh Formelement](Mesh_Feature/de.md).



## Skripten

Siehe auch: [FreeCAD Skripten Grundlagen](FreeCAD_Scripting_Basics/de.md).

Um eine Netzdatei zu importieren, wird die Methode `insert` des Mesh-Moduls verwendet.


```python
import Mesh
Mesh.insert('D:/testfiles/cylinder.stl')
```





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Import/de
