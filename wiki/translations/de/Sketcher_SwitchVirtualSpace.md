---
 GuiCommand:
   Name: Sketcher SwitchVirtualSpace
   Name/de: Sketcher VirtuellenBereichWechseln
   MenuLocation: Skizze , Sketcher visuell , Virtuellen Bereich wechseln
   Workbenches: Sketcher_Workbench/de
   Shortcut: **Z** **Z**
   Version: 0.17
---

# Sketcher SwitchVirtualSpace/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:24px;"> [Sketcher VituellenBereichWechseln](Sketcher_SwitchVirtualSpace/de.md) schaltet entweder die Sichtbarkeit von Randbedingungen um oder wechselt den sichtbaren virtuellen Bereich.

Eine Skizze besitzt zwei virtuelle Bereiche, die Randbedingungen enthalten können. Alle Randbedingungen werden im virtuellen Hauptbereich erstellt, können aber ausgeblendet werden, was sie in den anderen virtuellen Bereich verschiebt.



## Anwendung



### Randbedingungen aus- und einblenden 

1.  Eine oder mehrere Randbedingungen auswählen. Randbedingungen, die im aktiven virtuellen Bereich nicht sichtbar sind, können im [Abschnitt Randbedingungen des Sketcher-Dialogs](Sketcher_Dialog/de#Randbedingungen.md) ausgewählt werden.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_SwitchVirtualSpace.svg" width=16px> [Virtuellen Bereich wechseln](Sketcher_SwitchVirtualSpace/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Randbedingugen → <img src="images/Sketcher_SwitchVirtualSpace.svg" width=16px> Virtuellen Bereich wechseln** auswählen.
    -   Das Tastaturkürzel **Z** dann **Z**.



### Virtuelle Bereiche wechseln 

1.  Sicherstellen, dass keine Randbedingungen ausgewählt sind.
2.  Das Werkzeug aufrufen, wie oben beschrieben.
3.  Unsichtbare Randbedingungen werden sichtbar und sichtbare werden unsichtbar.



## Hinweise

-   Randbedingungen können auch im [Sketcher-Dialog](Sketcher_Dialog#Constraints/de.md) ein- bzw. ausgeblendet werden.
-   Die Einstellung für den virtuellen Bereich einer Skizze gilt nur in der aktuellen Sitzung und wird nicht in der FreeCAD-Datei gespeichert.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SwitchVirtualSpace/de
