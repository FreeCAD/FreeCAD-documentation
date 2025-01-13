---
 GuiCommand:
   Name: Sketcher Intersection
   Name/de: Sketcher Schneiden
   MenuLocation: Skizze , Sketcher-Werkzeuge , Externe Geometrie schneiden
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **I**
   Version: 1.1
   SeeAlso: Sketcher_ToggleConstruction/de
---

# Sketcher Intersection/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_Intersection.svg  style="width:24px;"> [Sketcher Schneiden](Sketcher_Intersection/de.md) schneidet Flächen und/oder Kanten, die zu Objekten außerhalb der Skizze gehören, mit der Skizzenebene. Die Schnittgeometrie wird \"externe Geometrie\" genannt. Sie bleibt parametrisch mit ihrem Quellobjekt verbunden. Externe Geometrie wird mit einer eigenen [Farbe](Sketcher_Preferences/de#Darstellung.md) (standardmäßig Magenta) und einer eigenen Linienart gekennzeichnet. sie kann beschreibende Geometrie sein, die außerhalb der Skizze sichtbar ist oder Hilfsgeometrie, die außerhalb der Skizze nicht sichtbar ist.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_Intersection.svg" width=16px> [Externe Geometrie schneiden](Sketcher_Intersection/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Werkzeuge → <img src="images/Sketcher_Intersection.svg" width=16px> Externe Geometrie schneiden** auswählen.
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_Intersection.svg" width=16px> Externe Geometrie schneiden** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **G** then **I**.
2.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
3.  Eine oder mehrere Flächen und/oder Kanten auswählen. Siehe [Hiweise](#Hinweise.md).
4.  Externe Geometrie wird erstellt.
5.  Dieses Werkzeug läuft immer im Fortsetzen-Modus: Wahlweise weitere externe Flächen und/oder Kanten auswählen.
6.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



## Hinweise

-   Eine Fläche ergibt eine oder mehrere Kanten, eine Kante einen oder mehrere Punkte. Geometrie, die die Skizzenebene nicht berührt, wird ignoriert.
-   Externe Geometrie wird als beschreibende Geometrie oder als Hilfsgeometrie erstellt, je nach Zustand des Werkzeugs [HilfsgeometrieUmschalten](Sketcher_ToggleConstruction/de.md). Dieses Werkzeug kann auch zum Umschalten des Modus individueller Kanten verwendet werden. Die Option **Bearbeiten → Einstellungen... → Sketcher → Allgemein → Externe Geometrie immer als Referenz hinzufügen** aktivieren, un den Zustand dieses Werkzeuges zu ignorieren und externe Geometrie immer als Hilfsgeometrie hinzuzufügen.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Intersection/de
