---
 GuiCommand:
   Name: Std SaveCopy
   Name/de: Std KopieSpeichern
   MenuLocation: Datei , Speichern einer Kopie...
   Workbenches: Alle
   Shortcut: **C**
   SeeAlso: Std_Save/de, Std_SaveAs/de
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



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

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



---
⏵ [documentation index](../README.md) > Std SaveCopy/de
