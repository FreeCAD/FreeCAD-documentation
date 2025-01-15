---
 GuiCommand:
   Name: Sketcher Projection
   Name/de: Sketcher Projektion
   MenuLocation: Skizze , Sketcher-Werkzeuge , Externe Geometrie projizieren
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **X**
   Version: 1.1
   SeeAlso: Sketcher_ToggleConstruction/de
---

# Sketcher Projection/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_Projection.svg  style="width:24px;"> [Sketcher Projektion](Sketcher_Projection/de.md) projiziert Kanten und/oder Knoten, die zu Objekten außerhalb der Skizze gehören, auf die Skizzenebene. Die projizierte Geometrie wird \"externe Geometrie\" genannt. Sie bleibt parametrisch mit ihrem Quellobjekt verbunden. Externe Geometrie wird mit einer eigenen [Farbe](Sketcher_Preferences/de#Darstellung.md) (standardmäßig Magenta) und einer eigenen Linienart gekennzeichnet. sie kann beschreibende Geometrie sein, die außerhalb der Skizze sichtbar ist oder Hilfsgeometrie, die außerhalb der Skizze nicht sichtbar ist.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_Projection.svg" width=16px> [Externe Geometrie projizieren](Sketcher_Projection/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Werkzeuge → <img src="images/Sketcher_Projection.svg" width=16px> Externe Geometrie projizieren** auswählen.
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_Projection.svg" width=16px> Externe Geometrie projizieren** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **G** then **X**.
2.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
3.  Eine oder mehrere Flächen, Kanten und/oder Knoten auswählen. Siehe [Hiweise](#Hinweise.md).
4.  Externe Geometrie wird erstellt.
5.  Dieses Werkzeug läuft immer im Fortsetzen-Modus: Wahlweise weitere externe Flächen, Kanten und/oder Knoten auswählen.
6.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



## Hinweise

-   Alle Kanten einer Fläche werden auf die Skizzenebene projiziert.
-   Externe Geometrie wird als beschreibende Geometrie oder als Hilfsgeometrie erstellt, je nach Zustand des Werkzeugs [HilfsgeometrieUmschalten](Sketcher_ToggleConstruction/de.md). Dieses Werkzeug kann auch zum Umschalten des Modus individueller Kanten verwendet werden. Die Option **Bearbeiten → Einstellungen... → Sketcher → Allgemein → Externe Geometrie immer als Referenz hinzufügen** aktivieren, un den Zustand dieses Werkzeuges zu ignorieren und externe Geometrie immer als Hilfsgeometrie hinzuzufügen.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Projection/de
