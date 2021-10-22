# Std Group/de
---
- GuiCommand:/de
   Name:Std Group
   Name/de:Std Gruppe
   MenuLocation:Baumansicht → Rechtsklick auf den Dokumentennamen
   |Workbenches:Alle
   Shortcut:
   Version:
   SeeAlso:[Standard Teil](Std_Part/de.md), [Wähle Gruppe](Draft_SelectGroup/de.md), [zur Gruppe hinzufügen](Draft_AddToGroup/de.md)---

## Beschreibung

[Standard Gruppe](Std_Group.md), intern [Anwendung DokumentObjektGruppe](App_DocumentObjectGroup/de.md) genannt, ist ein allgemein verwendeter Behälter für die Gruppierung unterschiedlicher Objekttypen in der [Baumansicht](tree_view.md), unabhängig von ihrem Datentyp. Er wird als einfacher Ordner zur Kategoriesierung und Organisation der Objekte im Modell verwendet, um eine logische Struktur zu erhalten. Std Gruppen kann in anderen Std Gruppen eingebettet werden.

Das Std Group Werkzeug ist nicht durch einen speziellen Arbeitbereich definiert, sondern durch das Basissystem. Daher befindet es sich in der **Strukturwerkzeugleiste**, die in allen [Arbeitsbereichen](Workbenches/de.md) zugänglich ist.

Um 3D-Objekte zu einer einzelnen Einheit zu gruppieren, um Baugruppen zu erzeugen, sollte stattdessen [Standard Teil](Std_Part/de.md) verwendet werden.

![](images/Std_Group_example.png )



*Verschiedene Elemente innerhalb Standart Gruppe in der Baumansicht.*

## Anwendung

1.  Auf den Namen des Dokumentes in der [Baumansicht](tree_view/de.md) klicken, das Kontextmenü mit einem Rechtsklick öffnen und **Erstelle Gruppe** wählen.
2.  Oder die Schaltfläche **<img src="images/Std_Group.svg" width=16px> [Gruppe](Std_Group/de.md)** in der Strukturwerkzeugleiste betätigen. Es wird eine leere Gruppe erstellt.
3.  Um Objekte einer Gruppe hinzuzufügen, werden sie in der [Baumansicht](tree_view/de.md) gewählt und mit Drag & Drop auf die Gruppe gezogen.
4.  Um Objekte aus einer Gruppe zu entfernen, werden sie aus der Gruppe auf die Dokumentbezeichnung oben in der [Baumansicht](tree_view/de.md) gezogen .

### Hinweise

-   Das Gruppenobjekt beeinflusst nicht die Positionen der enthaltenen Elemente in der [3D-Ansicht](3D_view/de.md). Im wesentlichen ist es nur ein Ordner zur Organisation der [Baumansicht](tree_view/de.md).
-   Die Gruppe kann auch aus der [Pythonkonsole](Python_console/de.md) als Unterklasse erstellt werden, um besondere \"Grupppen\" zu erzeugen, wie im Abschnitt [Skripten](Std_Group/de#Skripten.md) dargestellt.

## Eigenschaften

Eine _ (`App::DocumentObject` Klasse). Deshalb hat es die meisten Eigenschaften mit letzterem gemein.

Zusätzlich zu den Eigenschaften, die in [App FeaturePython](App_FeaturePython.md), einer wesentlichen Instanz des [DokumentObjektes](App_DocumentObject/de.md), hat die App DocumentObjectGroup die {{PropertyData/de|Group}} Eigenschaft.

Diese Eigenschaften stehen im [Eigenschaftseditor](property_editor/de.md) zur Verfügung. Versteckte Eigenschaften werden durch den Befehl **Alle anzeigen** im Kontextmenü des [Eigenschaftseditors](property_editor/de.md) angezeigt.

### Daten


{{TitleProperty|Base}}

-    {{PropertyData/de|Bezeichnung|String}}: der Name dieses Objekts, vom Benutzer als beliebige UTF8-Zeichenkette veränderbar.

-    **Gruppe|LinkList**: eine Liste referenzierter Objekte. Ein leerer Wert {{value|[]}} ist vorgegeben.

#### Ausgeblendete Dateneigenschaften 

-    {{PropertyView/de|Proxy|PythonObject}}: eine benutzerdefinierte Klasse, die mit diesem Objekt verknüpft ist. Das gibt es nur für die [Python](Python/de.md) Version. Siehe [Skripten](Std_Group/de#Skripten.md).

### Ansicht


{{TitleProperty|Base}}

Siehe [App FeaturePython](App_FeaturePython.md) zu grundlegenden Ansichtseigenschaften.

#### Ansicht ausgeblendeter Eigenschaften 

-    **Proxy|PythonObject**: eine benutzerdefinierte Providerklasse, die mit diesem Objekt verknüpft ist. Das gibt es nur für die [Python](Python/de.md) Version. Siehe [Skripten](Std_Group/de#Skripten.md).

## Vererbung

_(`App::DocumentObject`) ist und um eine Gruppen-Erweiterung erweitert wird.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten im Programm. Die `App::DocumentObjectGroup* Klasse ist ein einfacher Behälter der der die Gruppenerweiterung nutzt, um alle Typen von Objekten aufzunehmen.`

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md) und [Skriptgenerierte Objekte](scripted_objects/de.md).

Siehe [Part Formelemente](Part_Feature/de.md) zu allgemeinen Informationen über das Hinzufügen von Objekten zum Dokument.

Eine \'Std Group\' ([Anwendung DokumentObjektGruppe](App_DocumentObjectGroup/de.md))-wird mit der `addObject()`-Methode des Dokumentes erstellt. Sobald eine Gruppe existiert, können andere Objekte mit der `addObject()`- oder der `addObjects()`-Methode der Gruppe hinzugefügt werden. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObjectGroup", "Group")

bod1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
bod2 = App.ActiveDocument.addObject("Part::Box", "Box")

obj.addObjects([bod1, bod2])
App.ActiveDocument.recompute()
```

Diese grundlegende `App::DocumentObjectGroup` hat kein Proxyobjekt, sodass es vollständig für Unterklassen verwendet werden kann.

Deshalb sollte ein `App::DocumentObjectGroupPython`-Objekt für Unterklassen mit [Python](Python/de.md) erzeugt werden.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "Name")
obj.Label = "Custom label"
```

Zum Beispiel ist ein [FEM Analyse](FEM_Analysis/de.md) ein `App::DocumentObjectGroupPython`-Objekt mit einem benutzerdefinierten Icon und zusätzlichen Eigenschaften.

## Verweise

-   [Arch Tutorium](Arch_tutorial/de#Organizing_your_model.md)
-   [Dokumentenstruktur](Document_structure/de.md)
-   [Arch Tutorium/Ihr Modell organisieren](http://www.freecadweb.org/wiki/index.php?title=Arch_tutorial/de#Ihr_Modell_organisieren)





{{Std Base navi

}}

---
[documentation index](../README.md) > Std Group/de
