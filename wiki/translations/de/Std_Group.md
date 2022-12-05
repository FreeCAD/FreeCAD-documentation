# Std Group/de
---
- GuiCommand   */de
   Name   *Std Group
   Name/de   *Std Gruppe
   MenuLocation   *Baumansicht → Rechtsklick auf den Dokumentennamen
   |Workbenches   *Alle
   Shortcut   *
   Version   *
   SeeAlso   *[Standard Teil](Std_Part/de.md), [Wähle Gruppe](Draft_SelectGroup/de.md), [zur Gruppe hinzufügen](Draft_AddToGroup/de.md)---

## Beschreibung

Eine [Std Gruppe](Std_Group/de.md), intern [App-DocumentObjectGroup](App_DocumentObjectGroup/de.md) genannt, ist ein allgemein verwendeter Behälter für die Gruppierung unterschiedlicher Objekttypen in der [Baumansicht](Tree_view/de.md), unabhängig von ihrem Datentyp. Er wird als einfacher Ordner zur Kategoriesierung und Organisation der Objekte im Modell verwendet, um eine logische Struktur zu erhalten. Std Gruppen können in anderen Std Gruppen eingebettet werden.

Das Werkzeug Std Group ist nicht durch einen speziellen Arbeitbereich definiert, sondern durch das Basissystem. Daher befindet es sich in der **Structure**-Werkzeugleiste, die in allen [Arbeitsbereichen](Workbenches/de.md) zugänglich ist.

Um 3D-Objekte zu einer einzelnen Einheit zu gruppieren und damit eine Baugruppe zu erstellen, sollte stattdessen [Std Teil](Std_Part/de.md) verwendet werden.

![](images/Std_Group_example.png )



*Verschiedene Elemente innerhalb von Std Gruppen in der Baumansicht.*

## Anwendung

1.  Es gibt mehrere Möglichkeiten eine Gruppe anzulegen   *
    -   Ein Rechtsklick auf den Namen des Dokuments in der [Baumansicht](Tree_view/de.md) und im Kontextmenü **Gruppe erstellen...** auswählen.
    -   Die Schaltfläche **<img src="images/Std_Group.svg" width=16px> [Gruppe erstellen](Std_Group/de.md)** drücken.
2.  Eine leere Gruppe wird erstellt.
3.  Objekte werden einer Gruppe hinzugefügt, indem sie in der [Baumansicht](Tree_view/de.md) ausgewählt und auf die Gruppe gezogen und abgelegt werden.
4.  Objekte werden aus einer Gruppe entfernt, indem sie aus der Gruppe herausgezogen und auf der Dokumentbezeichnung ganz oben in der [Baumansicht](Tree_view/de.md) abgelegt werden.
5.  Objekte können auch hinzugefügt und entfernt werden, indem die {{PropertyData/de|Group}} der Gruppe bearbeitet wird.

## Eigenschaften

Die [Std Gruppe](Std_Group/de.md) wird intern [App-DocumentObjectGroup](App_DocumentObjectGroup/de.md) genannt (Klasse `App   *   *DocumentObjectGroup`) und wird von einem [App-DocumentObject](App_DocumentObject/de.md) (Klasse `App   *   *DocumentObject`) abgeleitet und erbt all seine Eigenschaften.

Die Std Gruppe hat dieselben Eigenschaften wie ein [App-FeaturePython](App_FeaturePython/de#Eigenschaften.md), das die grundlegendste Instanz eines [App-DocumentObjects](App_DocumentObject/de.md) ist. Es zeigt auch die folgenden zusätzlichen Eigenschaften im [Eigenschafteneditor](Property_editor/de.md). Verdeckte Eigenschaften können mit dem Befehl {{MenuCommand/de|Alle anzeigen}} im Kontextmenü des [Eigenschafteneditors](Property_editor.md) angezeigt werden.

### Daten


{{TitleProperty|Base}}

-    {{PropertyData/de|Group|LinkList}}   * Eine Liste referenzierter Objekte. Voreingestellt ist eine leere Liste {{value|[]}}.

-    {{PropertyData/de|_ Group Touched|Bool|Hidden}}   * Gibt an, ob die Gruppe -?- (touched) ist oder nicht.

## Skripten


**Siehe auch   ***

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md) und [Skriptgenerierte Objekte](Scripted_objects/de.md).

Siehe [Part Formelemente](Part_Feature/de.md) zu allgemeinen Informationen über das Hinzufügen von Objekten zum Dokument.

Eine \'Std Gruppe\' ([App-DocumentObjectGroup](App_DocumentObjectGroup/de.md)) wird mit der Methode `addObject()` des Dokuments erstellt. Sobald eine Gruppe existiert, können weitere Objekte mit den Methoden `addObject()` oder `addObjects()` zur Gruppe hinzugefügt werden.


```python
import FreeCAD as App

doc = App.newDocument()
group = App.ActiveDocument.addObject("App   *   *DocumentObjectGroup", "Group")

obj1 = App.ActiveDocument.addObject("PartDesign   *   *Body", "Body")
obj2 = App.ActiveDocument.addObject("Part   *   *Box", "Box")

group.addObjects([obj1, obj2])
App.ActiveDocument.recompute()
```

Diese grundlegende `App   *   *DocumentObjectGroup` hat kein Proxyobjekt und kann daher nicht vollständig zur Erstellung von Unterklassen verwendet werden.

Für die Instanziierung von Unterklassen mit [Python](Python/de.md) sollte ein `App   *   *DocumentObjectGroupPython`-Objekt erstellt werden.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App   *   *DocumentObjectGroupPython", "Name")
obj.Label = "Custom label"
```

Zum Beispiel ist ein [FEM Analyse](FEM_Analysis/de.md) ein `App   *   *DocumentObjectGroupPython`-Objekt mit einem benutzerdefinierten Icon und zusätzlichen Eigenschaften.

## Verweise

-   [Arch Tutorium](Arch_tutorial/de#Organizing_your_model.md)
-   [Dokumentenstruktur](Document_structure/de.md)
-   [Arch Tutorium/Ihr Modell organisieren](http   *//www.freecadweb.org/wiki/index.php?title=Arch_tutorial/de#Ihr_Modell_organisieren)





{{Std_Base_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Group/de
