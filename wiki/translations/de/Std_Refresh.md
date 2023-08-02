---
- GuiCommand:
   Name: Std Refresh
   Name/de: Std Aktualisieren
   MenuLocation: Bearbeiten -> Aktualisieren
   Workbenches: Alle
   Shortcut: **F5**
---

# Std Refresh/de



## Beschreibung

Der Befehl **Std Aktualisieren** berechnet das aktuelle Dokument neu. Der Befehl ist deaktiviert, solange das Dokument keine Neuberechnung benötigt.



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Std_Refresh.svg" width=16px> [Std Aktualisieren](Std_Refresh/de.md)** drücken.
    -   Den Menüeintrag **Bearbeiten → <img src="images/Std_Refresh.svg" width=16px> Aktualisieren** auswählen.
    -   Das Tastaturkürzel **F5**.



## Optionen

-   Um eine Neuberechnung zu erzwingen, wählt man das Dokument oder ein bzw. mehrere Objekte in der [Baumansicht](Tree_view/de.md) aus, markiert den Menüeintrag **<img src="images/Std_MarkToRecompute.svg" width=16px> Markieren, um neu zu berechnen** im Kontextmenü, und ruft den Befehl auf.
-   Für Objekte, aber nicht für Dokumente, kann man auch **Objekt neu berechnen** aus demselben Kontextmenü auswähen.



## Hinweise

-   Für ein Makro, das das aktive Dokument neu berechnet, siehe: [Makro Neuberechnung Erzwingen](Macro_ForceRecompute/de.md).



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um ein Dokument neu zu berechnen, verwendet man die Methode `recompute` des Document-Objekts.


```python
import FreeCAD

doc = FreeCAD.newDocument()
doc.recompute()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Refresh/de
