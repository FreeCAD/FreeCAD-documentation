---
- GuiCommand:
   Name: Part Slice
   Name/de: Part Zerschneiden
   MenuLocation: Part -> Teilen -> Schneiden zu Verbund
   Workbenches: Part_Workbench/de
   Version: 0.17
   SeeAlso: Part_BooleanFragments/de, Part_XOR/de, Part_CompJoinFeatures/de, Part_Boolean/de
---

# Part Slice/de



## Beschreibung

Das <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Part zerschneiden](Part_Slice/de.md) auch bekannt als **Schnitt zu Verbund** Werkzeug wird verwendet, um Formen durch Überschneidung mit anderen Formen zu teilen. Zum Beispiel wird für einen Kasten und eine Ebene ein Verbund aus zwei Körpern erzeugt.

![600px](images/Part_Slice_Demo.png)



*Oben: die Stücke wurden anschließend manuell auseinander bewegt, um das Zerschneiden deutlich zu machen*

Es gibt zwei Befehle, um eine Form zu zerschneiden: <img alt="" src=images/Part_SliceApart.svg  style="width:24px;">[Auseinanderschneiden](Part_SliceApart/de.md) und <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Schneiden zu Verbund](Part_Slice/de.md). Beide erzeugen ein parametrisches Formelement \'Slice\', das die zerschnittenen Teile in einen Verbund ablegt. Dabei sprengt <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Auseinanderschneiden](Part_SliceApart/de.md) den resultierenden Verbund in separate Objekte. \"Schneiden zu Verbund\" ist voll parametrisch und verursacht keine Probleme, wenn sich die Anzahl der Teile ändert. \"Auseinanderschneiden\" aktualisiert die Anzahl der Objekte nicht, wenn sich die Anzahl der Teile ändert.

Die Ausgabeform nimmt den gleichen Raum ein wie das Original. Sie wird jedoch dort getrennt, wo sie sich mit anderen Formen überschneidet. Die getrennten Teile werden in einen Verbund (compsolid) abgelegt, so dass das Objekt in einem Stück zu bleiben scheint. Man muss den Verbund sprengen, um die separaten Teile zu erhalten. Soll auf die einzelnen Teile parametrisch zugegriffen werden, kann zu diesem Zweck <img alt="" src=images/Part_CompoundFilter.svg  style="width:24px;"> [Part VerbundFiltern](Part_CompoundFilter/de.md) verwendet werden. Für schnellen nichtparametrischen Zugriff wird <img alt="" src=images/Draft_Downgrade.svg  style="width:24px;"> [Draft herabstufen](Draft_Downgrade/de.md) verwendet.

Das Werkzeug hat drei Modi: \"Standard\", \"Geteilt\" und \"BildeVolumenkörper\". Es gibt kein Auswahlformular, sie sind vordefiniert, können aber nach der Operation auf der Ebene der sich ergebenden Scheiben abgerufen werden.

\"Standard\" und \"Geteilt\" unterscheiden sich durch die Wirkung des Werkzeugs auf Drähte, Schalen und ZusammengesetzteVolumenkörper: Bei \"Geteilt\" werden diese getrennt; bei \"Standard\", werden sie zusammengehalten (zusätzliche Abschnitte entstehen).

Die Verbundstruktur in den \"Standard\" und \"Geteilt\" Modi folgt der Verbundstruktur der zu kappenden Form.

Im \"Volumenkörperverbund\" Modus ist das Ergebnis ein zusammengesetzterVolumenkörper (oder ein Verbund von zusammengesetztenVolumenkörpern wenn die resultierenden Festkörper mehr als eine Insel der Verbundenheit bilden). Volumenkörperverbund ist ein Satz von Körpern; Sie sind mit Festkörpern verwandt, so wie Drähte mit Kanten und Schalen mit Flächen verwandt sind; der Name ist wahrscheinlich ein verkürzter Ausdruck von \"Zusammengesetzter Volumenkörper\".

Die Gesamtwirkung des Werkzeugs ist der von <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Part BoolescheFragmente](Part_BooleanFragments/de.md) sehr ähnlich, außer dass nur die Teile aus der ersten Form im Ergebnis enthalten sind.



## Anwendung

1.  Zuerst das zu zerschneidende Objekt auswählen und dann einige Objekte, die damit zerschnitten werden sollen.
    Die Reihenfolge der Auswahl ist wichtig. Verbünde mit Selbstüberschneidungen sind nicht zulässig (Selbstüberschneidungen lassen sich manchmal dadurch erklären, dass der Verbunds

<img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;">[Part BoolescheFragmente](Part_BooleanFragments/de.md)) durchläuft.

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Zerschneiden](Part_Slice/de.md) in der Part-Werkzeugleiste drücken.
    -   Den Menüeintrag **Part → Aufteilen → Zerschneiden** auswählen.




1.  Hinweis: Die zu zerschneidenden Objekte müssen das zu schneidende Objekt vollständig trennen. Daher kann ein Würfel nicht durch einen Draht geschnitten werden, sondern z.B. durch eine von einem extrudierten Draht abgeleitete Ebene.

Ein parametrisches Slice-Objekt wird erzeugt. Die Originalobjekte werden ausgeblendet, und das Ergebnis der Überschneidung wird in der [3D-Ansicht](3D_view/de.md) dargestellt.

### Baumstruktur der Slice-Objekte 

Der Befehl Zerschneiden erzeugt ein geteiltes Objekt. Im folgenden Beispiel wird ein Würfel durch eine Fläche geteilt.

Die Scheibe wird erzeugt, und jedes Stück davon wird in einem Verbund vereint.

![](images/Part_SliceTree.png )



## Eigenschaften


{{TitleProperty|Scheiben}}

-    {{PropertyData/de|Basis}}: Zu zerschneidendes Objekt.

-    {{PropertyData/de|Werkzeuge}}: Liste der damit zu schneidenden Objekte. (bis v0.17.8053 wird diese Eigenschaft nicht im Eigenschaftseditor angezeigt und kann nur über Python abgerufen werden).

-    {{PropertyData/de|Modus}}: \"Standard\", \"Geteilt\" oder \"ZusammengesetzterVolumenkörper\". \"Zerschnitten\" ist Vorgabe. Standard und Geteilt unterscheiden sich durch die Wirkung des Werkzeugs auf Formen des Gruppierungsstyps: Wenn Geteilt, werden diese getrennt, andernfalls werden sie zusammengehalten (erhalten zusätzlicher Abschnitte).

-    {{PropertyData/de|Toleranz}}:\"Unschärfe\" Wert. Dies ist eine zusätzliche Toleranz, die bei der Suche nach Schnittpunkten angewendet wird, zusätzlich zu den in den Eingabeformen gespeicherten Toleranzen.

Hinweisː Eigenschaften sind auf dem inneren Objekt der Scheiben zugänglich, nicht auf der Ergebnisebene.



## Beispiel



### Puzzle erstellen 

1.  Zum Arbeitsbereich <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/de.md) wechseln.
    -   Eine neue Skizze erstellen.
    -   Ein Rechteck zeichnen, das die gesamte Form des Puzzles umfasst.
    -   Die Skizze schließen.
        ![320px](images/slice_example_step1.png)
2.  Zum Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench.md) wechseln.
    -   Die Skizze auswählen und **Part → <img src="images/Part_MakeFace.svg" width=24px>  [Fläche aus Liniezug erstellen](Part_MakeFace.md)** auswählen.
        ![320px](images/slice_example_step2.png)
3.  Zum Arbeitsbereich <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/de.md) zurück wechseln.
    -   Eine neue Skizze auf derselben Ebene erstellen.
    -   Mit dem Werkzeug Linienzug erstellen die Linien zeichnen, die das Puzzle in Stücke teilt.
        ![320px](images/slice_example_step3.png)
4.  Zum Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) zurück wechseln.
    -   Die Aufteilungsskizze auswählen und <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Boolesche Bestandteile](Part_BooleanFragments/de.md) anwenden. Dies setzt Knotenpunkte an die Schnittstellen der Linien in der Aufteilungsskizze ein. Diese werden gebraucht, damit der nächste Schritt funktioniert.
        ![320px](images/slice_example_step4.png)
5.  Die rechteckige Fläche sowie die booleschen Bestandteile der Aufteilungsskizze auswählen und <img alt="" src=images/Part_Slice.svg  style="width:16px;"> Part Zerschneiden anwenden.
    ![320px](images/slice_example_step5.png)
6.  <img alt="" src=images/Part_ExplodeCompound.svg  style="width:16px;"> [Part VerbundobjektSprengen](Part_ExplodeCompound/de.md) auf die zerteilte Fläche anwenden, um dem von Part Zerschneiden erstellten Verbund in einzelne Stücke aufzubrechen.

*Hinweis:*\' Die Schritte 5 und 6 können mit einem einzigen Klick auf <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Part Auseinanderschneiden](Part_SliceApart/de.md) durchgeführt werden.



## Hinweise

-   Das Werkzeug wurde in FreeCAD v0.17.8053 eingeführt. FreeCAD muss mit OCC 6.9.0 oder höher kompiliert werden, andernfalls steht das Werkzeug nicht zur Verfügung.
-   Eigenschaften sind über die inneren Elemente des Slice-Objekts erreichbar, nicht über das Ergebniselements.
-   Die Objekte, mit denen zerteilt werden soll, müssen das zu teilende Objekt vollständig durchtrennen. So kann z. B. ein Würfel nicht durch einen Draht zerteilt werden, aber durch eine Ebene, die von einem extrudierten Draht abgeleitet ist.
-   Das Zerteilungsobjekt muss die BOP-Prüfung bestehen. Siehe <img alt="" src=images/Part_CheckGeometry.svg  style="width:24px;"> [Part GeometriePrüfen](Part_CheckGeometry.md).



## Skripten

Dieses Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch folgende Funktion verwendet werden: 
```pythonBOPTools.SplitFeatures.makeSlice(name)```

-   Erstellt ein leeres Slice-Formelement. Die Eigenschaften \'Base\' und \'Tools\' müssen anschließend explizit zugewiesen werden.
-   Gibt das neu erstellte Objekt zurück.

Zerschneiden kann auch auf einfache Formen angewendet werden, ohne dass ein Dokumentobjekt erforderlich ist, durch: 
```pythonBOPTools.SplitAPI.slice(base_shape, tool_shapes, mode, tolerance = 0.0)``` Dies kann nützlich sein, um angepasste Funktionen mit Python-Skripten zu erstellen.

Beispiel: {{code|code=
import BOPTools.SplitFeatures
j = BOPTools.SplitFeatures.makeSlice(name= 'Slice')
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tools = FreeCADGui.Selection.getSelection()[1:]
}}

Das Werkzeug selbst ist in Python implementiert, siehe **/Mod/Part/BOPTools/SplitFeatures.py** ([GitHub link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/BOPTools/SplitFeatures.py)) innerhalb des FreeCAD-Installationsverzeichnisses.



## Tutorien

-   <https://www.youtube.com/watch?v=tzHkQaHgrfQ> FreeCad 0.18 PART WB using Slice and Slice Apart (Englisch), Autor: Ha Gei

-   <https://www.youtube.com/watch?v=JJAL5JmqqKQ> FreeCAD Slice und Slice Apart und andere Tricks (Deutsch), Autor: Ha Gei



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Slice/de
