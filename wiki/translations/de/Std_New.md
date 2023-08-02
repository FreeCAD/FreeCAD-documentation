---
- GuiCommand:
   Name: Std New
   Name/de: Std Neu
   MenuLocation: Datei -> Neu
   Workbenches: Alle
   Shortcut: **Strg**+**N**
   SeeAlso: Std_Open/de, Std_Import/de
---

# Std New/de

## Beschreibung

Der Befehl **Std Neu** erzeugt ein neues leeres Dokument und macht es zum aktiven Dokument.

## Anwendung

1.  Es gibt mehrere Wege, um den Befehl aufzurufen:
    -   Drücke die **<img src="images/Std_New.svg" width=16px> [Std Neu](Std_New/de.md)**-Schaltfläche.
    -   Wähle die **Datei → <img src="images/Std_New.svg" width=16px> Neu**-Option aus dem Menü.
    -   Benutze das Tastaturkürzel: **Strg**+**N**.

## Einstellungen

-   FreeCAD wird ein neues Dokument beim Start erstellen, falls **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Document → CreateNewDoc** auf `True` gesetzt ist. Diese Einstellung kann auch im [Voreinstellungseditor](Preferences_Editor/de#Document.md) geändert werden.
-   Einige Dokumenteigenschaften: Name des Autors, Firmenname und Lizenzinformationen können im [Voreinstellungseditor](Preferences_Editor/de#Document.md) vorgegeben werden.

## Eigenschaften

Die meisten Eigenschaften können auch im Dialogfeld des [Std ProjektInfo](Std_ProjectInfo/de.md) Befehls geändert werden.

-    {{PropertyData/de|Kommentar}}: Jeder Kommentar, der zutreffen könnte.

-    {{PropertyData/de|Firma}}: Firmenname. **Kann voreingestellt werden**.

-    {{PropertyData/de|Erstellt von}}: Autorenname. **Kann voreingestellt werden**.

-    {{PropertyData/de|Erstelldatum}}: Automatischer Datumstempel. **Nicht änderbar**.

-    {{PropertyData/de|Pfad}}: Der komplette Pfad zur Datei. Leer, falls das Dokument bisher nicht gespeichert wurde. **Nicht änderbar**.

-    {{PropertyData/de|Id}}: Bisher nicht implementiert.

-    {{PropertyData/de|Label}}: Der Name wird in der [Baumansicht](Tree_view/de.md) erscheinen. Standard ist der Name des Dokuments.

-    {{PropertyData/de|Zuletzt geändert von}}: Autorenname. **Kann voreingestellt werden**.

-    {{PropertyData/de|Zuletzt geändert am}}: Automatischer Datumstempel. **Nicht änderbar**.

-    {{PropertyData/de|Lizenzinformationen}}: Lizenztyp. **Kann voreingestellt werden**.

-    {{PropertyData/de|Lizenz-URL}}: Lizenz-URL. **Kann voreingestellt werden**.

-    {{PropertyData/de|Show Hidden}}: Falls aktiviert, werden in der [Baumansicht](Tree_view/de.md) verborgene Elemente trotzdem angezeigt. Verborgene Elemente im Baum können bei der Arbeit an größeren Modellen nützlich sein.

-    {{PropertyData/de|Tip}}: Bisher nicht implementiert.

-    {{PropertyData/de|Tip Name}}: Bisher nicht implementiert.

-    {{PropertyData/de|Transient Dir}}: Das flüchtige Verzeichnis wird für Sicherheitskopien benutzt. **Nicht änderbar**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um ein neues Dokument zu erstellen, verwende die `newDocument([name], [hidden<nowiki>=</nowiki>False])`-Methode der FreeCAD-Anwendung. Der Dokumentname muss eindeutig sein, was automatisch geprüft wird. Falls kein Name eingeben wird, bekommt das Dokument den Namen \"Untitled\". Falls `hidden<nowiki>=</nowiki>True` benutzt wird, wird das neue Dokument nicht in der GUI angezeigt und es wird kein Reiter dafür erscheinen.


```python
import FreeCAD
from pathlib import Path

# The folder and filename we will use:
fld = 'D:/testfiles/'
fnm = fld + 'test.FCStd'

# Make sure fld exists:
Path(fld).mkdir(parents=True, exist_ok=True)

doc = FreeCAD.newDocument()
doc.saveAs(fnm)

FreeCAD.closeDocument(doc.Name)

doc = FreeCAD.open(fnm)
doc.save()

FreeCAD.closeDocument(doc.Name)
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std New/de
