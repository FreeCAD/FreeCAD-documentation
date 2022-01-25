---
- GuiCommand:/de
   Name:Part Slice
   Name/de:Part Zerschneiden
   MenuLocation:Part → Trennen → Zerschneiden
   Workbenches:[Part](Part_Workbench/de.md)
   Version:0.17
   SeeAlso:[Part Boolesche Bruchstücke](Part_BooleanFragments/de.md), [Part XOR](Part_XOR/de.md), [Part Grundelemente verbinden](Part_CompJoinFeatures/de.md), [Part Boolesche](Part_Boolean/de.md)
---

# Part Slice/de


</div>

## Beschreibung

Das <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Part zerschneiden](Part_Slice/de.md) auch bekannt als **Schnitt zu Verbund** Werkzeug wird verwendet, um Formen durch Überschneidung mit anderen Formen zu teilen. Zum Beispiel wird für einen Kasten und eine Ebene ein Verbund aus zwei Körpern erzeugt.

![600px](images/Part_Slice_Demo.png)



*Oben: die Stücke wurden anschließend manuell auseinander bewegt, um das Zerschneiden deutlich zu machen*


<div class="mw-translate-fuzzy">

Es gibt zwei Befehle, um eine Form zu zerschneiden: <img alt="" src=images/Part_SliceApart.svg  style="width:24px;">[Auseinander Zerschneiden](Part_SliceApart/de.md) und <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Zu Verbund zerschneiden](Part_Slice/de.md). Beide erzeugen ein parametrisches \'zerschnittenes\' Formelement, das die zerschnittenen Teile in einen Verbund legt. Jedoch <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Auseinander Zerschneiden](Part_SliceApart/de.md) explodiert den resultierenden Verbund in separate Objekte. \"Zerschneiden zum Verbund\" ist voll parametrisch und verursacht keine Probleme, wenn sich die Anzahl der Teile ändert. \"Auseinander zerschneiden\" aktualisiert die Anzahl der Objekte nicht, wenn sich die Anzahl der Teile ändert.


</div>


<div class="mw-translate-fuzzy">

Die Ausgabeform nimmt den gleichen Raum ein wie das Original. Sie wird jedoch dort getrennt, wo sie sich mit anderen Formen überschneidet. Die getrennten Teile werden in einen Verbund (oder BildeVolumenkörper) gesetzt, so dass das Objekt in einem Stück zu bleiben scheint. Du musst den Verbund sprengen, um die einzelnen Teile zu erhalten. Wenn du auf die einzelnen Teile parametrisch zugreifen möchtest, kannst du zu diesem Zweck <img alt="" src=images/Part_CompoundFilter.svg  style="width:24px;"> [Part VerbundFilter](Part_CompoundFilter/de.md) verwenden. Für schnellen nichtparametrischen Zugriff verwende <img alt="" src=images/Draft_Downgrade.svg  style="width:24px;"> [Entwurf herabstufen](Draft_Downgrade/de.md).


</div>

Das Werkzeug hat drei Modi: \"Standard\", \"Geteilt\" und \"BildeVolumenkörper\". Es gibt kein Auswahlformular, sie sind vordefiniert, können aber nach der Operation auf der Ebene der sich ergebenden Scheiben abgerufen werden.

\"Standard\" und \"Geteilt\" unterscheiden sich durch die Wirkung des Werkzeugs auf Drähte, Schalen und ZusammengesetzteVolumenkörper: Bei \"Geteilt\" werden diese getrennt; bei \"Standard\", werden sie zusammengehalten (zusätzliche Abschnitte entstehen).

Die Verbundstruktur in den \"Standard\" und \"Geteilt\" Modi folgt der Verbundstruktur der zu kappenden Form.

Im \"Volumenkörperverbund\" Modus ist das Ergebnis ein zusammengesetzterVolumenkörper (oder ein Verbund von zusammengesetztenVolumenkörpern wenn die resultierenden Festkörper mehr als eine Insel der Verbundenheit bilden). Volumenkörperverbund ist ein Satz von Körpern; Sie sind mit Festkörpern verwandt, so wie Drähte mit Kanten und Schalen mit Flächen verwandt sind; der Name ist wahrscheinlich ein verkürzter Ausdruck von \"Zusammengesetzter Volumenkörper\".


<div class="mw-translate-fuzzy">

Die Gesamtwirkung des Werkzeugs ist der von <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Boolesche Bruchstücke](Part_BooleanFragments/de.md) sehr ähnlich, außer dass nur die Teile aus der ersten Form im Ergebnis enthalten sind.


</div>

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle zuerst das zu zerschneidende Objekt und dann einige Objekte, die damit zerschnitten werden sollen.
    Die Reihenfolge der Auswahl ist wichtig. Verbünde mit Selbstüberschneidungen sind nicht zulässig (Selbstüberschneidungen können sich manchmal durch das hindurchgehen des Verbunds durch

<img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;">[BoolescheBruchstücke](Part_BooleanFragments/de.md)) erklären lassen

1.  Rufe den Part Zerschneiden Befehl auf mehrere Arten auf:
    -   Drücke die <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Part Zerschneiden](Part_Slice/de.md) Schaltfläche in der Part Werkzeugleiste
    -   Verwende den **Part → Aufteilen → Zerschneiden** Eintrag im Part Menü


</div>

1.  Hinweis: Die zu zerschneidenden Objekte müssen das zu schneidende Objekt vollständig trennen. Daher kann ein Würfel nicht durch einen Draht geschnitten werden, sondern z.B. durch eine von einem extrudierten Draht abgeleitete Ebene.


<div class="mw-translate-fuzzy">

Ein parametrisches Scheibenobjekt wird erzeugt. Die Originalobjekte werden ausgeblendet, und das Ergebnis der Überschneidung wird in der [3D Ansicht](3D_view/de.md) angezeigt.


</div>


<div class="mw-translate-fuzzy">

### Baumstruktur der Scheiben 

Der Zerschneidebefehl erzeugt ein in Scheiben geschnittenes Objekt. Im folgenden Beispiel wird ein Würfel durch eine Fläche zerschnitten.


</div>

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


<div class="mw-translate-fuzzy">

1.  Wechsle zum [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md), erstelle eine neue Skizze. Zeichne ein Rechteck, das die Gesamtform des Puzzles darstellt. Schließe die Skizze.
    ![320px](images/slice_example_step1.png)
2.  Wechsle zum [Part Arbeitsbereich](Part_Workbench/de.md). Wähle die Skizze aus und wähle Formteil → Erstelle Fläche aus Skizze (im Menü).
    ![320px](images/slice_example_step2.png)
3.  Wechsle zum [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md), erstelle eine neue Skizze auf derselben Ebene. Zeichne mit dem Polylinien Werkzeug die Linien, welche das Puzzle in Stücke aufteilen sollen.
    ![320px](images/slice_example_step3.png)
4.  Wechsle zum Part Arbeitsbereich. Wähle die Aufteilungsskizze aus und wende [Part Boolesche Bruchstücke](Part_BooleanFragments/de.md) an. Dadurch werden Knoten eingefügt, an denen sich die Linien der Aufteilungsskizze kreuzen. Sie zu haben ist wesentlich für den nächsten Arbeitsschritt.
    ![320px](images/slice_example_step4.png)
5.  Wähle die rechteckige Fläche und alle Boolesche Bruchstücke der Aufteilungsskizze aus und wende Part kappen an.
    ![320px](images/slice_example_step5.png)
6.  Verwende [Part SprengeVerbund](Part_ExplodeCompound/de.md) auf der gekappten Fläche, um den von Part Kappen hergestellten Verbund in einzelne Stücke zu zerlegen.


</div>


<div class="mw-translate-fuzzy">

*Hinweis:*\' Die Schritte 5 und 6 können mit einem einzigen Klick mit <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Part Auseinander kappen](Part_SliceApart/de.md) durchgeführt werden.


</div>

## Hinweise


<div class="mw-translate-fuzzy">

-   Das Werkzeug wurde in FreeCAD v0.17.8053 eingeführt. FreeCAD muss mit OCC 6.9.0 oder höher kompiliert werden; andernfalls ist das Werkzeug nicht verfügbar.
-   ̈Eigenschaften sind auf dem inneren Objekt des Scheiben zugänglich, nicht auf der Ergebnisebene.
-   Die Objekte, mit denen zerteilt werden sollen, müssen das zu zerteilende Objekt vollständig trennen. So kann z. B. ein Würfel nicht durch einen Draht zerteilt werden, sondern durch eine Ebene, die von einem extrudierten Draht abgeleitet ist.
-   Zerteilungsobjekt muss BOP Prüfung bestehen. Siehe <img alt="" src=images/Part_CheckGeometry.svg  style="width:24px;"> [Part CheckGeometry](Part_CheckGeometry.md).


</div>

## Skripten


<div class="mw-translate-fuzzy">

Das Werkzeug kann in [Makros](macros/de.md) ebenso wie aus der Python Konsole heraus durch folgende Funktion angesprochen werden:


</div>


```pythonBOPTools.SplitFeatures.makeSlice(name)```

-   Erstellt eine leeres Kapp Grundelement. Die \'Basis\' und \'Werkzeug\' Eigenschaften müssen anschließend explizit zugewiesen werden.
-   Gibt das neu erstellte Objekt zurück.

Kappen kann auch auf einfache Formen angewendet werden, ohne dass ein Dokumentobjekt erforderlich ist, über: 
```pythonBOPTools.SplitAPI.slice(base_shape, tool_shapes, mode, tolerance = 0.0)``` Dies kann nützlich sein, um benutzerdefinierte Python Skriptfunktionen zu erstellen.

Beispiel: {{code|code=
import BOPTools.SplitFeatures
j = BOPTools.SplitFeatures.makeSlice(name= 'Slice')
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tools = FreeCADGui.Selection.getSelection()[1:]
}}

Das Werkzeug selbst ist in Python implementiert, siehe {{FileName|/Mod/Part/BOPTools/SplitFeatures.py}} ([GitHub link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/BOPTools/SplitFeatures.py)) innerhalb des FreeCAD Installationsverzeichnisses.

## Tutorien

-   <https://www.youtube.com/watch?v=tzHkQaHgrfQ> FreeCad 0.18 PART WB using Slice and Slice Apart (Englisch), Autor: Ha Gei

-   <https://www.youtube.com/watch?v=JJAL5JmqqKQ> FreeCAD Slice und Slice Apart und andere Tricks (Deutsch), Autor: Ha Gei


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Slice/de
