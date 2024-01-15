---
 GuiCommand:
   Name: Draft SubelementHighlight
   Name/de: Draft UnterelementHervorheben
   MenuLocation: Entwurf , Änderung , Unterelement hervorheben
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **H** **S**
   Version: 0.19
   SeeAlso: Draft_Move/de, Draft_Rotate/de, Draft_Scale/de
---

# Draft SubelementHighlight/de



## Beschreibung

Der <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:24px;"> **Entwurf UnterelementMarkieren** Befehl markiert ausgewählte Objekte oder die Basisobjekte ausgewählter Objekte temporär hervor. Er ist in Verbindung mit dem Unterelementmodus des Befehls [Entwurf Bewegen](Draft_Move/de.md), dem Befehl [Entwurf Drehen](Draft_Rotate/de.md) oder dem Befehl [Entwurf Skalieren](Draft_Scale/de.md) zu verwenden. Zurzeit funktioniert der Unterelementmodus nur bei [Entwurf Linien](Draft_Line/de.md) und [Entwurf WDrähte](Draft_Wire/de.md) richtig.

![](images/Draft_SubelementHighlight_example.png ) 
*Eine Architektur Wand, deren Basis, ein Entwurf Draht, wurde markiert*



## Anwendung

1.  Wahlweise eine oder mehrere [Draft Linien](Draft_Line/de.md), [Draft Kantenzüge](Draft_Wire/de.md) oder Objekte deren {{PropertyData/de|Basis}} Objekte enthält, die [Draft Linien](Draft_Line/de.md) oder [Draft Kantenzüge](Draft_Wire/de.md) sind.

2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_SubelementHighlight.svg" width=16px> [Unterelement hervorheben](Draft_SubelementHighlight/de.md)** drücken.
    -   Den Menüeintrag **Modification → <img src="images/Draft_SubelementHighlight.svg" width=16px> Unterelement hervorheben** auswählen.
    -   Das Tastaturkürzel **H** dann **S**.

3.  Wurde noch kein Element ausgewählt: ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.

4.  Die ausgewählten Ojekte werden (bei Bedarf) eingeblendet, ihre {{PropertyView/de|Line Color}} und {{PropertyView/de|Point Color}} werden auf rot geändert und ihre {{PropertyView/de|Point Size}} wird auf {{Value|10}} geändert.

5.  Es ist ratsam, jetzt die bestehende Auswahl abzuwählen, z.B. durch klicken auf einen beliebigen Punkt in der [3D-Ansicht](3D_view/de.md).

6.  Ein oder mehrere Unterelemente, Kanten oder Punkte, des Objekts, die rot markiert wurden, auswählen.

7.  [Draft Verschieben](Draft_Move/de.md), [Draft Drehen](Draft_Rotate/de.md) oder [Draft Skalieren](Draft_Scale/de.md) aufrufen.

8.  Unterelement-Modus im Aufgaben-Bereich des Befehls umschalten, indem die Checkbox **Unterelemente ändern** aktiviert wird.

9.  Die ausgewählten Unterelemente ändern und den laufenden Draft-Befehl fertigstellen.

10. 
    **Esc**drücken, um die temporären visuellen Änderungen der Objekte zurückzunehmen.



## Hinweise

-   Wurden Objekte mit diesem Befehl hervorgehoben, sollten die temporären visuellen Änderungen zurückgenommen werden, bevor die Datei gespeichert und wieder geöffnet wird.
-   Hervorgehobene Objekte sollten nicht Kopiert werden, wenn der Unterelement-Modus ausgeschaltet ist. Die temporären visuellen Änderungen können für Kopien, die auf diese Art erstellt wurden, nicht zurückgenommen werden.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SubelementHighlight/de
