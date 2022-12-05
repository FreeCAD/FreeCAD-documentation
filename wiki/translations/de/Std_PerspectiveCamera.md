---
- GuiCommand:/de
   Name:Std PerspectiveCamera
   Name/de:Std PerspektivKamera
   MenuLocation:Ansicht → Perspektiv Ansicht
   Workbenches:Alle
   Shortcut:**V** **P**
   SeeAlso:[Std OrthogonalKamera](Std_OrthographicCamera/de.md)
---

# Std PerspectiveCamera/de

## Beschreibung

Der Befehl **Std PerspectivKamera** schaltet die Kamera in der aktiven [3D Ansicht](3D_view/de.md) in den perspektivischen Ansichtsmodus. In diesem Modus erscheinen Objekte, die weiter von der Kamera entfernt sind, kleiner als solche, die näher sind.

![](images/Std_PerspectiveCamera_example.svg ) 
*Zwei Würfel mit den gleichen Abmessungen in perspektivischer Ansicht*

## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Wähle die Option **Ansicht → <img src="images/Std_PerspectiveCamera.svg" width=16px> Perspektiv Ansicht** aus dem Menü.
    -   Verwende das Tastaturkürzel: **V** dann **P**.

## Hinweise

-   Es ist auch möglich, über das Miniwürfel Menü des [Navigationswürfels](Navigation_Cube/de.md) in den perspektivischen Ansichtsmodus zu wechseln.

## Einstellungen

-   Der Kameratyp kann in den Einstellungen geändert werden: **Bearbeiten → Voreinstellungen... → Anzeige → 3D Ansicht → Kameratyp**. Der gewählte Typ wird für alle 3D Ansichten aller geöffneten Dokumente und auch für neue Dokumente verwendet. Siehe [Einstellungseditor](Preferences_Editor/de#3D_Ansicht.md).

## Skripten


**Siehe auch:**

[FreeCAD Skripten Grundlagen](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht auf perspektivisch zu ändern, verwende die Methode `setCameraType` des AktiveAnsicht Objekts. Diese Methode ist nicht verfügbar, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setCameraType('Perspective')
FreeCADGui.ActiveDocument.ActiveView.getCameraType()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std PerspectiveCamera/de
