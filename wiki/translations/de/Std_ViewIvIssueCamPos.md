---
- GuiCommand:/de
   Name:Std ViewIvIssueCamPos
   Name/de:Std AnsichtKamerapositionAusgeben
   MenuLocation:Ansicht → Stereo → Kameraposition ausgeben
   Workbenches:Alle
   SeeAlso:[Std AnsichtenEinfrieren](Std_FreezeViews/de.md)
---

# Std ViewIvIssueCamPos/de



## Beschreibung

Der Befehl **Std AnsichtKamerapositionAusgeben** gibt die Kameraeinstellungen der aktiven [3D-Ansicht](3D_view/de.md) im [Ausgabefenster](Report_view/de.md) und in der [Python-Konsole](Python_console/de.md) aus.


```python   OrthographicCamera {   viewportMapping ADJUST_CAMERA   position 57.73505 -57.73502 57.735027   orientation 0.74290609 0.30772209 0.59447283  1.2171158   nearDistance 81.588844   farDistance 109.60551   aspectRatio 1   focalDistance 100   height 100  } 
```



*Beispielausgabe: Kameraeinstellungen nach dem Umstellen der Ansicht auf [Isometrisch](Std_ViewIsometric/de.md) in einem neuen Dokument*



## Anwendung

1.  Den Menüeintrag **Ansicht → Stereo → <img src="images/Std_ViewIvIssueCamPos.svg" width=16px> Kameraposition ausgeben** auswählen.



## Hinweise

-   Die Kameraeinstellungen können verwendet werden, um eingefrorene Ansichten zu einer \*.cam-Datei hinzuzufügen. Siehe [Std AnsichtenEinfrieren](Std_FreezeViews/de.md).



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Die Methode `getCamera` des ActiveView-Objekts gibt dieselben Kameraeinstellungen in einer einzelnen Zeichenkette zurück. Diese Methode steht nicht zur Verfügung, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.getCamera()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewIvIssueCamPos/de
