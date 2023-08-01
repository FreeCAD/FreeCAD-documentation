---
- GuiCommand:
   Name: Std UserEditMode
   Name/de: Std BenutzerBearbeitungsmodus
   MenuLocation: Bearbeiten - Bearbeitungsmodus - ...
   Workbenches: Alle
   Version: 0.20
   SeeAlso: [Std Berbeiten](Std_Edit/de.md)
---

# Std UserEditMode/de

## Beschreibung

Die Anweisung **Std BenutzerBearbeitungsmodus** legt den Bearbeitungsmodus fest, der verwendet wird, wenn ein Objekt mit einem Doppelklick in der [Baumansicht](Tree_view/de.md) gewählt wird.

## Anwendung

#\* Unter dem Menüpunkt **Bearbeiten → Bearbeitungsmodus** einen Bearbeitungsmodus wählen.

## mögliche Bearbeitungsmodi 

### <img alt="" src=images/Std_UserEditModeDefault.svg  style="width:24px;"> Vorgabe 

Das Objekt wird mit seinem vorgegebenen Bearbeitungsmodus bearbeitet. Dieser Bearbeitungsmodus wird intern mit dem am besten passend für den Objekttyp festgelegt, z.B. wird dies die Formeigenschaftsbearbeitung für [Part Grundelemente](Part_Primitives/de.md) und [PartDesign Formelemente](PartDesign_Feature/de.md) sein, die Positionierungsbearbeitung für [Part Boolesche Operationen](Part_Boolean/de.md) etc.

### <img alt="" src=images/Std_UserEditModeTransform.svg  style="width:24px;"> Transformieren 

Die Positionierung eines Objektes is mit der Anweisung [Std Transformieren](Std_TransformManip/de.md) bearbeitbar.

### <img alt="" src=images/Std_UserEditModeCutting.svg  style="width:24px;"> Abtrennen 

Dieser Bearbeitungsmodus ist verwendbar, scheint aber durch kein Objekt verwendet zu werden.

### <img alt="" src=images/Std_UserEditModeColor.svg  style="width:24px;"> Farbe 

Mit der Anweisung [Part Flächenfarben](Part_FaceColors/de.md) kann die Farbe für jede einzelne Oberfläche des Objektes bestimmt werden.

## Hinweise

Nicht jedes Objekt kann durch alle Bearbeitungsmodi bearbeitet werden. Ist ein Bearbeitunsmodus für ein Objekt nicht zutreffend, wird stattdessen der vorgegebene Bearbeitungsmodus verwendet.

## Einstellungen

-   Der letzte Bearbeitungsmodus wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → General → UserEditMode**

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um mögliche Bearbeitungsmodi anzuzeigen:


```python
import FreeCADGui
FreeCADGui.listUserEditModes()
```

Um den aktiven Bearbeitungsmodus zu erhalten:


```python
import FreeCADGui
FreeCADGui.getUserEditMode()
```

Um den aktiven Bearbeitungsmodus zu einzustellen:


```python
import FreeCADGui
FreeCADGui.setUserEditMode(MODENAME) # Where MODENAME is a string available in the list of edit modes
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std UserEditMode/de
