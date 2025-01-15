---
 GuiCommand:
   Name: Sketcher SelectElementsWithDoFs
   Name/de: Sketcher UnterbestimmteElementeAuswählen
   MenuLocation: Skizze , Sketcher visuell , Unterbestimmte Elemente auswählen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **Z** **F**
   Version: 0.18
---

# Sketcher SelectElementsWithDoFs/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:24px;"> [Sketcher UnterbestimmteElementeAuswählen](Sketcher_SelectElementsWithDoFs/de.md) Wählt die nicht vollständig bestimmten Elemente der Skizze aus.

Sind solche Elemente in einer Skizze vorhanden, zeigt der Abschnitt [Meldungen des Lösers](Sketcher_Dialog/de#Meldungen_des_Gleichungslösers.md) im Sketcher-Dialog diese Meldung:

-   Unterbestimmt: n Freiheitsgrade

Wobei *n* die Anzahl der noch nicht bestimmten (festgelegten) Freiheitsgrade ist. Anklicken des unterstrichenen Textes wählt die unterbestimmten Elemente aus.

Bitte beachten, dass eine Skizze auch überflüssige Randbedingungen enthalten kann, wenn eine der anderen [Meldungen des Gleichungslösers](Sketcher_Dialog/de#Meldungen_des_Gleichungslösers.md) angezeigt wird.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Den unterstrichenen Text im Sketcher-Dialog anklicken, wie oben beschrieben.
    -   Den Menüeintrag **Skizze → Sketcher visuell → <img src="images/Sketcher_SelectElementsWithDoFs.svg" width=16px> Unterbestimmte Elemente auswählen** auswählen.
    -   Das Tastaturkürzel **Z** dann **F**.




1.  Die unterbestimmten Elemente werden ausgewählt.
2.  Wahlweise in einen leeren Bereich der [3D-Ansicht](3D_view.md) klicken, um die Auswahl zu leeren.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectElementsWithDoFs/de
