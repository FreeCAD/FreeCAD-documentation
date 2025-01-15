---
 GuiCommand:
   Name: Sketcher External
   Name/de: Sketcher ExterneGeometrie
   MenuLocation: Skizze , Sketcher-Werkzeuge , Externe Geometrie erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **X**
   SeeAlso: Sketcher_ToggleConstruction/de
---

# Sketcher External/de



## Beschreibung


{{VersionMinus/de|1.0}}

: Das Werkzeug <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [Externe Geometrie](Sketcher_External/de.md) projiziert Kanten und/oder Knoten, die zu Objekten außerhalb der Skizze gehören, auf die Skizzenebene. Die projizierte Geometrie wird \"externe Geometrie\" genannt. Sie bleibt dauerhaft mit den zugrundeliegenden Objekten verknüpft. Kanten der externen Geometrie werden mit einer bestimmten [Farbe](Sketcher_Preferences/de#Erscheinungsbild.md) (Standardfarbe Magenta) und ({{Version/de|1.0}}) mit einer bestimmten Linienart gekennzeichnet. Ähnlich der Hilfsgeometrie ist externe Geometrie außerhalb der Skizze nicht sichtbar. Sie ist dazu gedacht, bei der Festlegung von Randbedingungen oder anderen Geometrien innerhalb der Skizze zu helfen.


{{VersionPlus/de|1.1}}

: Siehe <img alt="" src=images/Sketcher_Projection.svg  style="width:24px;"> [Sketcher Projektion](Sketcher_Projection/de.md)

![](images/Sketcher_ExternalEsempio1.png ) 
*Die zwei magentafarbenen Linien sind externe Geometrie, die mit Kanten eines vorhandene [Blocks](PartDesign_Pad/de.md) verknüpft sind. Sie werden eingesetzt, um die Kreise festzulegen.*



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_External.svg" width=16px> [Externe Geometrie erstellen](Sketcher_External/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Werkzeuge → <img src="images/Sketcher_External.svg" width=16px> Externe Geometrie erstellen** auswählen.
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_External.svg" width=16px> Externe Geometrie erstellen** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **G** then **X**.
2.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
3.  Eine externe Kante oder einen externen Knoten auswählen. Siehe [Hinweise](#Hinweise.md).
4.  Externe Geometrie wird erstellt.
5.  Dieses Werkzeug läuft immer in Fortsetzen-Modus: Wahlweise weitere externe Kanten und/oder Knoten auswählen.
6.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



## Hinweise

-   Nur Kanten und Knoten von Objekten innerhalb desselben Koordinatensystems können ausgewählt werden. Die Skizze und das Objekt müssen sich im selben [Körper](PartDesign_Body/de.md) oder im selben [Part](Std_Part/de.md) befinden; oder beide müssen sich im globalen Koordinatensystem befinden. Mit einem [Binder](PartDesign_SubShapeBinder/de.md) kann eine Kopie des Objekts in das gerade aktive Koordinatensystem eingefügt werden, wenn erforderlich.
-   Zirkelbezüge sind nicht erlaubt. Ein Objekt, das selbst von der Skizze abhängt, kann nicht (wieder) mit die Skizze verknüpft werden.
-   Verknüpfungen zu Elementen aus anderen Skizzen sind möglich und werden empfohlen, da sie zuverlässiger sind als Verknüpfungen zu generierter (Festkörper-) Geometrie. Letztere kann unter dem [Problem der Topologischen Benennung](Topological_naming_problem/de.md) (TNP) leiden. Siehe [Ratschläge zur Erstellung stabiler Modelle](Feature_editing/de#Ratschläge_zur_Erstellung_stabiler_Modelle.md).



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/de
