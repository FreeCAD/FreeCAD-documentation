---
- GuiCommand:/de
   Name:Std AnsichtEinpassenAlles
   MenuLocation:Ansicht → Standardansichten‏‎ → EinpassenAlles
   Workbenches:Alle
   Shortcut:**V** **F**
   SeeAlso:[Std AnsichtEinpassenAuswahl](Std_ViewFitSelection/de.md)
---

## Beschreibung

Der **Std AnsichtEinpassenAlles**-Befehl zoomt und schwenkt, bis alle sichtbaren Objekte in die aktive [3D Ansicht](3D_view/de.md) passen.

## Anwendung

==

1.  Es gibt mehrere Wege, den ViewFitAll Befehl aufzurufen:
    -   Drücke die **<img src="images/Std_ViewFitAll.svg" width=16px> [Std AnsichtEinpassenAlles](Std_ViewFitAll/de.md)**-Schaltfläche.
    -   Wähle die **Ansicht → Standardansicht → <img src="images/Std_ViewFitAll.svg" width=16px> Alles einpassen**-Option aus dem Menü.
    -   Wähle die **Ansicht → Standardansichten → <img src="images/Std_ViewFitAll.svg" width=16px>Alles einpassen**-Option aus dem [3D-Ansicht](3D_view/de.md)-Kontextmenü.
    -   Benutze den Tastaturkurzbefehl **V**, dann **F**.

## Hinweise

-   Es ist auch möglich, über das Miniwürfel-Menü des [Navigationswürfels](Navigation_Cube/de.md) über \'Alles einpassen\' zu zoomen.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht auf \'Alles einpassen\' zu ändern, verwende die Methode `fitAll` des AktiveAnsicht-Objekts. Diese Methode ist nicht verfügbar, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.fitAll()
```

Alternativ kann die `SendMsgToActiveView`-Methode des FreeCADGui-Objekts benutzt werden. Diese Methode ist im FreeCAD-Konsolenmodus nicht verfügbar.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewFit')
```





{{Std Base navi

}}  
