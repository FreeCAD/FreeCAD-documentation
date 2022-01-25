---
- GuiCommand:/de
   Name:Std OrthographicCamera
   Name/de:Std OrthogonaleAnsicht
   MenuLocation:Ansicht → Orthogonale Ansicht
   Workbenches:Alle
   Shortcut:**V** **O**
   SeeAlso:[Std PerspektivAnsicht](Std_PerspectiveCamera/de.md)
---

# Std OrthographicCamera/de

## Beschreibung

Der Befehl **Std OrthogonaleKamera** schaltet die Kamera in der aktiven [3D Ansicht](3D_view/de.md) in den orthogonalen Ansichtsmodus. In diesem Modus erscheinen Objekte, die weiter von der Kamera entfernt sind, nicht kleiner als solche, die näher sind.

![](images/Std_OrthographicCamera_example.svg ) 
*Zwei Würfel mit den gleichen Abmessungen in orthogonaler Ansicht*

## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Wähle die Option **Ansicht → <img src="images/Std_OrthographicCamera.svg" width=16px> Orthogonale Ansicht** aus dem Menü.
    -   Verwende das Tastaturkürzel: **V** dann **O**.

## Hinweise

-   Es ist auch möglich, über das Miniwürfel Menü des [Navigationswürfels](Navigation_Cube/de.md) in den orthogonalen Ansichtsmodus zu wechseln.

## Einstellungen

-   Der Kameratyp kann in den Einstellungen geändert werden: **Bearbeiten → Voreinstellungen... → Anzeige → 3D Ansicht → Kameratyp**. Der gewählte Typ wird für alle 3D Ansichten aller geöffneten Dokumente und auch für neue Dokumente verwendet. Siehe [Einstellungseditor](Preferences_Editor/de#3D_Ansicht.md).

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht auf orthogonal zu ändern, verwende die Methode `setCameraType` des AktiveAnsicht Objekts. Diese Methode ist nicht verfügbar, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setCameraType('Orthographic')
FreeCADGui.ActiveDocument.ActiveView.getCameraType()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std OrthographicCamera/de
