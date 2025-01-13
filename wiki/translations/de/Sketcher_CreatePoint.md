---
 GuiCommand:
   Name: Sketcher CreatePoint
   Name/de: Sketcher PunktErstellen
   MenuLocation: Skizze , Skizzengeometrien , Punkt erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **Y**
---

# Sketcher CreatePoint/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:24px;"> [Sketcher PunktErstellen](Sketcher_CreatePoint/de.md) erstellt einen Punkt.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences/de#Allgemein.md) (In-Ansicht-Parameter zur Lagebestimmung). {{Version/de|1.0}}

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_CreatePoint.svg" width=16px> [Punkt erstellen](Sketcher_CreatePoint/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Skizzengeometrien → <img src="images/Sketcher_CreatePoint.svg" width=16px> Punkt erstellen** auswählen.
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_CreatePoint.svg" width=16px> Punkt erstellen** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **G** then **Y**.

Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.

1.  Einen Punkt auswählen. Oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben.
2.  Der Punkt wird erstellt und passende Pos-OVP-basierte Randbedingungen werden hinzugefügt.
3.  Wenn das Werkzeug im [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetze-Modi.md) läuft:
    1.  Wahlweise weitere Punkte erstellen.
    2.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



## Hinweise

-    {{VersionMinus/de|0.21}}: Punkte werden immer als Hilfsgeometrie erstellt. Wahlweise können sie mit [Sketcher HilfsgeometrieUmschalten](Sketcher_ToggleConstruction/de.md) in normale Geometrie umgewandelt werden, um sie außerhalb des Sketcher-Bearbeitungsmodus sichtbar zu machen.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePoint/de
