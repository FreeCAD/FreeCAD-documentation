---
 GuiCommand:
   Name: Mesh Export
   Name/de: Mesh Exportieren
   MenuLocation: Netze , Netz exportieren...
   Workbenches: Mesh_Workbench/de
   SeeAlso: Std_Export/de, Import_Export/de
---

# Mesh Export/de



## Beschreibung

Der Befehl **Mesh Exportieren** exportiert ein Netzobjekt in ein Netz-Dateiformat, wobei unterschiedliche Dateiformate unterstützt werden.



## Anwendung

1.  Ein einzelnes Netzobjekt auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Mesh_Export.svg" width=16px> [Netz exportieren...](Mesh_Export/de.md)** drücken.
    -   Den Menüeintrag **Netze → <img src="images/Mesh_Export.svg" width=16px> Netz exportieren...** auswählen.
    -   Die Menüoption **<img src="images/Mesh_Export.svg" width=16px> Netz exportieren...** im Kontextmenü der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) auswählen.
3.  Im Dialogfeld das richtige Dateiformat auswählen.
4.  Einen Dateinamen eingeben. Wenn im vorherigen Schritt die Option {{Value|Alle Dateien (*.*)}} ausgewählt wurde und hier keine Dateierweiterung angegeben wird, wird die Erweiterung **.stl** verwendet.
5.  Die Schaltfläche **Speichern** drücken.



## Hinweise

Es gibt einige [Exporteinstellungen im Zusammenhang mit Netzformaten](Import_Export_Preferences/de#Verfügbare_Einstellungen.md), aber sie stehen diesem Befehl nicht zur Verfügung. Sie werden von dem Befehl [Std Export](Std_Export/de.md) verwendet.



## Einstellungen

-   Der zuletzt verwendete Dateispeicherort wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp (BasisAnwendung) → Preferences (Einstellungen) → General (Allgemein) → FileOpenSavePath**.



## Skripten

Siehe auch: [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um Objekte (einschließlich Netzobjekte) in ein Netz-Dateiformat zu exportieren, wird die Methode `export` des Mesh-Moduls verwendet.


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
