---
 GuiCommand:
   Name: Sketcher SelectConflictingConstraints
   Name/de: Sketcher WidersprüchlicheRandbedingungenAuswählen
   MenuLocation: Skizze , Sketcher visuell , Widersprüchliche Randbedingungen auswählen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **Z** **P** **C**
   Version: 0.15
---

# Sketcher SelectConflictingConstraints/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:24px;"> [Sketcher WidersprüchlicheRandbedingungenAuswählen](Sketcher_SelectConflictingConstraints/de.md) wählt die widersprüchlichen Randbedingungen einer Skizze aus.

Sind solche Randbedingungen in einer Skizze vorhanden, zeigt der Abschnitt [Meldungen des Lösers](Sketcher_Dialog/de#Meldungen_des_Gleichungslösers.md) im Sketcher-Dialog diese Meldung:

-   Überbestimmt: (#, #, #)

Wobei *(#, #, #)* die Indizes der Randbedingungen sind. Anklicken des unterstrichenen Textes wählt die überflüssigen Randbedingungen aus.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Den unterstrichenen Text im Sketcher-Dialog anklicken, wie oben beschrieben.
    -   Den Menüeintrag **Skizze → Sketcher visuell → <img src="images/Sketcher_SelectConflictingConstraints.svg" width=16px> Wiedersprüchliche Randbedingungen auswählen** auswählen.
    -   Das Tastaturkürzel **Z** dann **P** dann **C**.
2.  Die wiedersprüchlichen Randbedingungen werden ausgewählt.
3.  Wahlweise in einen leeren Bereich der [3D-Ansicht](3D_view.md) klicken, um die Auswahl zu leeren.



## Hinweise

-   Wiedersprüchliche Randbedingungen müssen aus der Skizze entfernt werden.
-   Anstelle der vorgeschlagenen Indizes können auch andere Randbedingungen gelöscht werden.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectConflictingConstraints/de
