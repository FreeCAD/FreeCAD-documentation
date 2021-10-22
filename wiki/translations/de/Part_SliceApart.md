---
- GuiCommand:/de
   Name:Part SliceApart
   Name/de:Part AuseinanderSchneiden
   MenuLocation:Formteil → Teilen → Auseinander Kappen
   Version:0.18.15506
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Kappen zu Verbund](Part_Slice/de.md), [Part Verbund Sprengen](Part_ExplodeCompound/de.md)
---

# Part SliceApart/de


</div>

## Beschreibung

Werkzeug zum zerteilen von Formen durch Überschneiden mit anderen Formen. Beispielsweise werden aus einem Quader und einer Ebene zwei Volumenkörper erzeugt. ![600px](images/Part_Slice_Demo.png)



*Oben: Die Stücke wurden anschließend manuell auseinandergeschoben, um das Zerschneiden sichtbar zu machen.*

_, gefolgt von <img alt="" src=images/Part_ExplodeCompound.svg  style="width:24px;"> [Formteil Sprenge Verbund](Part_ExplodeCompound/de.md). Während \"Zerschneiden zu Verbund\" vollparametrisch ist und keine Probleme verursacht, wenn sich die Anzahl der Teile ändern, \"Auseinander Schneiden\" aktualisiert nicht die Anzahl der Objekte, wenn sich die Anzahl der Stücke ändert. Beide erzeugen ein parametrisches Scheiben Formelement, das die geschnittenen Teile in einen Verbund bringt, aber \"Auseinander Schneiden\" sprengt den resultierenden Verbund in separate Objekte.

Die Ausgabeform nimmt den gleichen Platz ein wie das Original. Sie wird jedoch dort wo andere Formen überschnitten werden, zerteilt. Die zerteilten Teile sind einzelne Stücke.

Bitte besuche die [Formteil Zerschneiden](Part_Slice/de.md) Seite für weitere Informationen.

### Baumstruktur von Auseinander Schneiden 

Der Befehl Auseinander Schneiden erzeugt mehr als nur das geschnittene Objekt. Im folgenden Beispiel wird ein Würfel durch eine Fläche geschnitten.

Die Scheibe wird erstellt und für jedes Stück davon wird ein [Part VerbundFilter](Part_CompoundFilter/de.md) erstellt, so dass dieselbe Scheibe mehrfach unter jedem VerbundFilter auftritt. Alle diese VerbundFilter sind in einem Verbund zusammengefasst.

![](images/Part_SliceApartTree.png )

## Beispiel

-   Herstellung eines Puzzle: siehe [Formteil Zerschneiden](Part_Slice/de.md) Beispielschritte 1 bis 6

## Skripten

Das Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole heraus durch Verwendung der folgenden Funktionen verwendet werden:

`BOPTools.SplitFeatures.makeSlice(name)`

Setze Modus auf **zerschneiden** für Auseinander Schneiden

-   Erstellt eine leeres Scheiben Formelement. Die \'Basis\' und \'Werkzeug\' Eigenschaften müssen anschließend explizit zugewiesen werden.
-   Gibt das neu erstellte Objekt zurück.

Scheibe kann auch auf einfache Formen angewendet werden, ohne dass ein Dokumentobjekt erforderlich ist, über: 
```pythonBOPTools.SplitAPI.slice(base_shape, tool_shapes, mode, tolerance = 0.0)``` Dies kann nützlich sein, um benutzerdefinierte Python Skriptfunktionen zu erstellen.

Beispiel: {{code|code=
import BOPTools.SplitFeatures
j = BOPTools.SplitFeatures.makeSlice(name= 'Slice')
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tools = FreeCADGui.Selection.getSelection()[1:]
}}

Das Werkzeug selbst ist in Python implementiert, siehe {{FileName|/Mod/Part/BOPTools/SplitFeatures.py}} ([GitHub link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/BOPTools/SplitFeatures.py)) innerhalb des FreeCAD Installationsverzeichnisses.

## Hinweise

Auseinander Schneiden wurde in FreeCAD v0.18.15506 eingeführt. FreeCAD muss mit OCC 6.9.0 oder später kompiliert werden. Andernfalls ist das Werkzeug nicht verfügbar.

## Videotutorien

-   <https://www.youtube.com/watch?v=tzHkQaHgrfQ> : FreeCad 0.18 PART WB using SLICE and SLICE APART (Englisch), Autor: Ha Gei

-   <https://www.youtube.com/watch?v=JJAL5JmqqKQ> : FreeCAD Slice und Slice Apart und andere Tricks (Deutsch), Autor: Ha Gei


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part SliceApart/de
