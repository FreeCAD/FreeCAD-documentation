---
- GuiCommand:
   Name:Std SaveCopy
   Name/de:Std KopieSpeichern
   MenuLocation:Datei - Speichern einer Kopie...
   Workbenches:Alle
   Shortcut:**C**
   SeeAlso:[Std Speichern](Std_Save/de.md), [Std SpeichernUnter](Std_SaveAs/de.md)
---

# Std SaveCopy/de

## Beschreibung

Der Befehl **Std KopieSpeichern** speichert eine Kopie des aktiven Dokuments unter einem neuen Dateinamen.

## Anwendung

1.  Menüeintrag **Datei → <img src="images/Std_SaveCopy.svg" width=16px> Speichern einer Kopie...** auswählen.
2.  Einen Dateinamen im Dialogfeld eingeben.
3.  Schaltfläche **Speichern** drücken.

## Optionen

-    **Esc**oder Schaltfläche **Abbrechen** drücken, um den Befehl abzubrechen.

## Einstellungen

-   Der zuletzt verwendete Dateispeicherort wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp (BasisAnwendung) → Preferences (Einstellungen) → General (Allgemein) → FileOpenSavePath**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um eine Kopie eines Dokuments zu speichern, kann man die Methode `saveCopy` des Document-Objekts verwenden.


```python
import FreeCAD
from pathlib import Path

# The folder and filename we will use:
fld = 'D:/testfiles/'
fnm = fld + 'testCopy.FCStd'

# Make sure fld exists:
Path(fld).mkdir(parents=True, exist_ok=True)

doc = FreeCAD.newDocument()
doc.saveCopy(fnm)
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std SaveCopy/de
