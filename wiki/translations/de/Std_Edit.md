---
- GuiCommand:/de
   Name:Std Edit
   Name/de:Std Bearbeiten
   MenuLocation:Bearbeiten → Umschalten Bearbeitungsmodus
   Workbenches:Alle
---

# Std Edit/de


</div>

## Beschreibung

Der **Std Bearbeiten**-Befehl aktiviert oder deaktiviert den Bearbeitungsmodus eines Objekts.

## Anwendung


<div class="mw-translate-fuzzy">

1.  Falls kein Objekt im Bearbeitungsmodus ist: wähle ein einzelnes Objekt.
2.  Wähle die **Bearbeiten → <img src="images/Std_Edit.svg" width=16px> Bearbeitungsmodus umschalten**-Option aus dem Menü.
3.  Entweder wird der Bearbeitungsmodus des gewählten Objekts aktiviert oder der bestehende Bearbeitungsmodus wird deaktiviert.


</div>

## Hinweise


<div class="mw-translate-fuzzy">

-   Einige Werkzeuge sind in der Benutzeroberfläche deaktiviert (ausgegraut), während der Bearbeitungsmodus eines Objekts aktiviert ist.
-   Nicht alles Objekttypen haben einen Bearbeitungsmodus.
-   Die verfügbare Funktionalität im Bearbeitungsmodus hängt vom Objekttyp ab.
-   Der Bearbeitungsmodus kann auch durch doppelklicken eines Objekts in der [Baumansicht](Tree_view/de.md) aktiviert werden.


</div>

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zur Aktivierung des Bearbeitungsmodus eines Objekts benutze die `setEdit`-Methode des document-Objekts. Diese Methode ist nicht verfügbar, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.setEdit("myObjectName",0)
```

Das zweite Argument ist der EditMode. Die folgenden Optionen sind verfügbar:

0 = Default
1 = Transform
2 = Cutting
3 = Color

Zur Deaktivierung des Bearbeitungsmodus eines Objekts benutze die `resetEdit`-Methode des document-Objekts.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.resetEdit()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}

---
[documentation index](../README.md) > Std Edit/de
