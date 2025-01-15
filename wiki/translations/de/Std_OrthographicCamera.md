---
 GuiCommand:
   Name: Std OrthographicCamera
   Name/de: Std OrthogonaleKamera
   MenuLocation: Ansicht , Orthogonale Ansicht
   Workbenches: Alle
   Shortcut: **V** **O**
   SeeAlso: Std_PerspectiveCamera/de
---

# Std OrthographicCamera/de



## Beschreibung

Der Befehl **Std OrthogonaleKamera** schaltet die Kamera in der aktiven [3D Ansicht](3D_view/de.md) in den orthogonalen Ansichtsmodus. In diesem Modus erscheinen Objekte, die weiter von der Kamera entfernt sind, nicht kleiner als solche, die näher sind.

![](images/Std_OrthographicCamera_example.svg ) 
*Zwei Würfel mit den gleichen Abmessungen in orthogonaler Ansicht*



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Den Menüeintrag **Ansicht → <img src="images/Std_OrthographicCamera.svg" width=16px> Orthogonale Ansicht** auswählen.
    -   Die Menüoption **<img src="images/Std_OrthographicCamera.svg" width=16px> Orthogonale Ansicht** im Miniwürfelmenü des [Navigationswürfels](Navigation_Cube/de.md) auswählen.
    -   Das Tastaturkürzel: **V** dann **O**.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md).

-   Der Kameratyp kann geändert werden: **Bearbeiten → Voreinstellungen... → Anzeige → 3D-Ansicht → Kameratyp**. Der gewählte Typ wird für alle 3D Ansichten aller geöffneten Dokumente und auch für neue Dokumente verwendet.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Die Methode `setCameraType` des View-Objekts wird verwendet, um die Ansicht auf orthogonal oder perspektivisch zu ändern.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.setCameraType("Perspective")
view.setCameraType("Orthographic")
view.getCameraType()
```



---
⏵ [documentation index](../README.md) > Std OrthographicCamera/de
