---
- GuiCommand:/de
   Name:Draft SubelementHighlight
   Name/de:Draft UnterelementHervorheben
   MenuLocation:Entwurf → Änderung → Unterelement hervorheben
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**H** **S**
   Version:0.19
   SeeAlso:[Draft Verschieben](Draft_Move/de.md), [Draft Drehen](Draft_Rotate/de.md), [Draft Skalieren](Draft_Scale/de.md)
---

# Draft SubelementHighlight/de



## Beschreibung

Der <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:24px;"> **Entwurf UnterelementMarkieren** Befehl markiert ausgewählte Objekte oder die Basisobjekte ausgewählter Objekte temporär hervor. Er ist in Verbindung mit dem Unterelementmodus des Befehls [Entwurf Bewegen](Draft_Move/de.md), dem Befehl [Entwurf Drehen](Draft_Rotate/de.md) oder dem Befehl [Entwurf Skalieren](Draft_Scale/de.md) zu verwenden. Zurzeit funktioniert der Unterelementmodus nur bei [Entwurf Linien](Draft_Line/de.md) und [Entwurf WDrähte](Draft_Wire/de.md) richtig.

![](images/Draft_SubelementHighlight_example.png ) 
*Eine Architektur Wand, deren Basis, ein Entwurf Draht, wurde markiert*



## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle ein Objekt.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Draft_SubelementHighlight.svg" width=16px> [UnterelementMarkieren](Draft_SubelementHighlight/de.md)** Schaltfläche
    -   Verwende den **D** dann **E** Tastaturkürzel
    -   Verwende den **Änderung → UnterelementMarkieren** Eintrag im Menü Entwurf
    -   Klicke auf alle Punkte, die du verschieben möchtest.
    -   Klicke einen anderen Punkt in der 3D Ansicht an, oder gib eine Koordinate ein und drücke den **<img src="images/Draft_AddPoint.svg" width=24px> Punkt hinzufügen**.
3.  Drücke **Esc** oder die **Schliessen** Schaltfläche , um den aktuellen Befehl abzuschließen.


</div>



## Hinweise

-   If objects have been highlighted with this command the temporary visual changes should be reverted before saving and reopening the file.
-   Highlighted objects should not be copied if subelement mode is off. The temporary visual changes cannot be reverted for copies created in this manner.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SubelementHighlight/de
