# Macro Normal Vector/de
{{Macro
|Name=Normal Vector Macro
|Name/de=Normalenvektormakro
|Icon=Macro_Normal_Vector.png
|Description=Erhalte den Normalenvektor auf die zuvor angewählte Oberfläche
|Author=ulrich1a
|Version=1.0
|Date=2016-09-26
|FCVersion=Alle
|Download=[https://www.freecadweb.org/wiki/images/8/8b/Macro_Normal_Vector.png ToolBar Icon]
}}

## Beschreibung

Einfaches Makro, um den aus der zuvor in der 3D-Ansicht gewählten Oberfläche Normalenvektor zu erhalten und an die Pythonkonsole zu übergeben.

## Anwendung

-   Die Oberfläche in der 3D-Ansicht wählen.
-   Die Makroanweisungen in die Pythonkonsole kopieren.
-   FreeCAD wird die Normalenvektorinformationen in der Pythonkonsole anzeigen.
-   Diese Werte können für die Einstellung der Richtung beim Erstellen einer Zeichnungsansicht verwendet werden.

## Skript

ToolBar Icon ![](images/Macro_Normal_Vector.png )

**Macro_Normal_Vector.FCMacro**


{{MacroCode|code=
Gui.Selection.getSelectionEx()[0].SubObjects[0].Faces[0].normalAt(0,0)
}}

## Verweis

[Link to dicussion thread (german)](http://forum.freecadweb.org/viewtopic.php?f=13&t=10959)



---
⏵ [documentation index](../README.md) > Macro Normal Vector/de
