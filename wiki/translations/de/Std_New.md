---
 GuiCommand:
   Name: Std New
   Name/de: Std Neu
   MenuLocation: Datei , Neu
   Workbenches: Alle
   Shortcut: **Strg**+**N**
   SeeAlso: Std_Open/de, Std_Import/de
---

# Std New/de



## Beschreibung

Der Befehl **Std Neu** erzeugt ein neues leeres Dokument und macht es zum aktiven Dokument.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Std_New.svg" width=16px> [Neu](Std_New/de.md)** drücken.
    -   Den Menüeintrag **Datei → <img src="images/Std_New.svg" width=16px> Neu** auswählen.
    -   Das Tastaturkürzel: **Strg** + **N**.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md).

-   Standardmäßig startet FreeCAD ohne ein neues Dokument. Unter **Bearbeiten → Einstellungen... → Allgemein → Dokument → Neues Dokument beim Start erzeugen** auf `True` gesetzt ist. Diese Einstellung kann auch im [Voreinstellungseditor](Preferences_Editor/de#Dokument.md) geändert werden.
-   Einige Dokumenteigenschaften: Name des Bearbeiters, Firmenname und Lizenzinformationen können unter **Bearbeiten → Einstellungen... → Allgemein → Dokument → Autorenschaft und Lizenz** voreingestellt werden.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Die meisten Eigenschaften können auch im Dialogfeld des [Std ProjektInfo](Std_ProjectInfo/de.md) Befehls geändert werden.



### Daten


{{TitleProperty|Basis}}

-    **Comment|String**: Irgendein passender Kommentar.

-    **Company|String**: Firmenname.

-    **Created By|String**: Autorenname.

-    **Creation Date|String**: Automatischer Datumstempel (schreibgeschützt).

-    **File Name|String**: Der vollständige Dateipfad. Leer, falls das Dokument bisher nicht gespeichert wurde (schreibgeschützt).

-    **Id|String**: Bisher nicht implementiert.

-    **Label|String**: Der Name, der in der [Baumansicht](Tree_view/de.md) erscheint. Wird nach erneutem Öffnen durch den Namen des Dokuments ersetzt.

-    **Last Modified By|String**: Autorenname.

-    **Last Modified Date|String**: Automatischer Datumstempel (schreibgeschützt).

-    **License|String**: Lizenztyp.

-    **License URL|String**: Lizenz-URL.

-    **Material|Map|Hidden**: Map with material properties.

-    **Meta|Map|Hidden**: Map with additional meta information.

-    **Show Hidden|Bool**: Falls aktiviert, werden in der [Baumansicht](Tree_view/de.md) verborgene Elemente trotzdem angezeigt. Elemente in der Baumansicht zu verbergen kann bei der Arbeit an größeren Modellen nützlich sein.

-    **Tip|Link**: Bisher nicht implementiert.

-    **Tip Name|String**: Bisher nicht implementiert.

-    **Transient Dir|String**: Das flüchtige Verzeichnis wird für Sicherheitskopien benutzt (schreibgeschützt)..

-    **Uid|UUID|Hidden**: UUID des Dokuments (schreibgeschützt).

-    **Unit System|Enumeration**: Das Dokument-Einheitensystem. Der Ausgangswert hängt vom [Standard-Einheitensystem](Preferences_Editor/de#Allgemein_2.md) ab. <small>(v1.0)</small> 



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

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





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std New/de
