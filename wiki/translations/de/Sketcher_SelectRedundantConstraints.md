---
 GuiCommand:
   Name: Sketcher SelectRedundantConstraints
   Name/de: Sketcher RedundanteRandbedingungenAuswählen
   MenuLocation: Skizze , Sketcher visuell , Überflüssige Randbedingungen auswählen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **Z** **P** **R**
   Version: 0.15
---

# Sketcher SelectRedundantConstraints/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:24px;"> [Sketcher RedundanteRandbedingungenAuswählen](Sketcher_SelectRedundantConstraints/de.md) wählt die überflüssigen Randbedingungen einer Skizze aus.

Sind solche Randbedingungen in einer Skizze vorhanden, zeigt der Abschnitt [Meldungen des Lösers](Sketcher_Dialog/de#Meldungen_des_Gleichungslösers.md) im Sketcher-Dialog diese Meldung:

-   Überflüssige Randbedingungen: (#, #, #)

Wobei *(#, #, #)* die Indizes der Randbedingungen sind. Anklicken des unterstrichenen Textes wählt die überflüssigen Randbedingungen aus.

Bitte beachten, dass eine Skizze auch überflüssige Randbedingungen enthalten kann, wenn eine der anderen [Meldungen des Gleichungslösers](Sketcher_Dialog/de#Meldungen_des_Gleichungslösers.md) angezeigt wird.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Den unterstrichenen Text im Sketcher-Dialog anklicken, wie oben beschrieben.
    -   Den Menüeintrag **Skizze → Sketcher visuell → <img src="images/Sketcher_SelectRedundantConstraints.svg" width=16px> Überflüssige Randbedingungen auswählen** auswählen.
    -   Das Tastaturkürzel **Z** dann **P** dann **R**.
2.  Die überflüssigen Randbedingungen werden ausgewählt.
3.  Wahlweise in einen leeren Bereich der [3D-Ansicht](3D_view.md) klicken, um die Auswahl zu leeren.



## Hinweise

-   Überflüssige Randbedingungen müssen aus der Skizze entfernt werden.
-   Anstelle der vorgeschlagenen Indizes können auch andere Randbedingungen gelöscht werden.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectRedundantConstraints/de
