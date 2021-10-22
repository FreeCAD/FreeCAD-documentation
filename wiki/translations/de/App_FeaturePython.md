# App FeaturePython/de
## Einführung

Ein <img alt="" src=images/Feature.svg  style="width:32px;"> _ in [Python](Python/de.md).

Hierbei handelt es sich um ein einfaches Objekt, das standardmäßig nicht viele Eigenschaften hat, z.B. weder [Platzierung](Placement/de.md) noch [topologische Form](Part_TopoShape/de.md). Dieses Objekt ist für allgemeine Zwecke bestimmt; je nach den Eigenschaften, die ihm zugeordnet sind, kann es zur Verwaltung verschiedener Datentypen verwendet werden.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten im Programm. Die Klasse `App::FeaturePython* ist eine einfache Implementierung der Klasse {{incode|App::DocumentObject`, die für jeden Zweck verwendet werden kann, da sie standardmäßig keinen [TopoForm](Part_TopoShape/de.md) hat.}}

## Anwendung

Die [Anwendung FormelementPython](App_FeaturePython/de.md) ist ein internes Objekt, so dass es nicht über die grafische Oberfläche erstellt werden kann. Es ist dazu gedacht, durch Klassen unterteilt zu werden, die verschiedene Arten von Daten verarbeiten.

Siehe [Skripten](App_FeaturePython#Scripting/de.md) für weitere Information.

## Eigenschaften

Eine _ (`App::DocumentObject` Klasse). Deshalb hat es die meisten Eigenschaften mit letzterem gemein.

Zusätzlich zu den in [Anwendung DokumentObjekt](App_DocumentObject/de.md) beschriebenen Eigenschaften verfügt FormelementPython über einen grundlegenden Ansichtsanbieter, so dass es in der [Baumansicht](tree_view/de.md) angezeigt wird.

Siehe [Eigenschaft](Property/de.md) für alle Eigenschaftstypen, die geskriptete Objekte haben können.

Diese Eigenschaften stehen im [Eigenschaftseditor](property_editor/de.md) zur Verfügung. Versteckte Eigenschaften werden durch den Befehl **Alle anzeigen** im Kontextmenü des [Eigenschaftseditors](property_editor/de.md) angezeigt.

### Daten


{{TitleProperty|Basis}}

-    **Proxy|PythonObject|Hidden**: a custom class associated with this object.

-    **Label|String**: der Nutzer editierbare Name dieses Objekts, es ist eine arbitrary UTF8 Zeichenfolge.

-    **Label2|String**: eine längere, vom Benutzer bearbeitbare Beschreibung dieses Objekts, es ist eine beliebige UTF8 Zeichenkette, die Zeilenumbrüche enthalten kann. Standardmäßig ist es eine leere Zeichenkette {{value|""}}.

-    **Proxy|PythonObject**: eine benutzerdefinierte Klasse, die mit diesem Objekt verknüpft ist.

-    **Visibility|Bool|Hidden**: ob das Objekt angezeigt werden soll oder nicht.

### Ansicht

Diese Eigenschaften entsprechen den grundlegenden Eigenschaften der Basis [Ansichtsanbieter](viewprovider/de.md), `Gui::ViewProviderDocumentObject`, die von allen Ansichtsanbietern in der Software geerbt wird.


{{TitleProperty|Basis}}

-    **Proxy|PythonObject|Hidden**: eine benutzerdefinierte View Provider Klasse, die diesem Objekt zugeordnet ist. Diese Eigenschaft existiert nur für die Klassen, die in der Lage sind, eine benutzerdefinierte Klasse zuzuordnen.


{{TitleProperty|Anzeigeoptionen}}

-    **Anzeigemodus|Aufzählung**: sie ist standardmäßig leer.

-    **Anzeige im Baum|Bool**: die Standardeinstellung ist `True`, in diesem Fall erscheint das Objekt in der [Baumansicht](tree_view/de.md); andernfalls wird das Objekt in der Baumansicht ausgeblendet. Sobald ein Objekt in der Baumansicht unsichtbar ist, kannst du es wieder sehen, indem du das Kontextmenü über dem Namen des Dokuments öffnest (Rechtsklick) und {{CheckBox|TRUE|Anzeige ausgeblendete Elemente}} wählst. Dann kann das ausgeblendete Element ausgewählt und **Im Baum anzeigen** wieder zu `True` zurückgeschaltet werden.

-    **Sichtbarkeit|Bool**: auf `True` voreingestellt. In diesem Fall ist das Objekt in der [3D Ansicht](3D_view/de.md) sichtbar, wenn es eine [Form](Part_TopoShape/de.md) hat, andernfalls ist es unsichtbar. Standardmäßig kann diese Eigenschaft ein- und ausgeschaltet werden, indem das Objekt ausgewählt und die **Leertaste**n Leiste in der Tastatur gedrückt wird.


{{TitleProperty|Auswahl}}

-    **Oben, wenn ausgewählt|Aufzählung**: Sie steuert die Art und Weise, wie die Auswahl in der [3D Ansicht](3D_view/de.md) erfolgt, wenn das Objekt eine [Form](Part_TopoShape/de.md) hat und es viele Objekte gibt, die teilweise von anderen abgedeckt werden. Die Standardeinstellung ist {{value|Deaktiviert}}, was bedeutet, dass keine besondere Hervorhebung erfolgt; {{value|Aktiviert}} bedeutet, dass das Objekt über jedem anderen Objekt erscheint, wenn es ausgewählt wird; {{value|Object}} bedeutet, dass das Objekt nur dann oben erscheint, wenn das gesamte Objekt in der [Baumansicht](tree_view/de.md) ausgewählt ist; {{value|Element}} bedeutet, dass das Objekt nur dann oben erscheint, wenn ein Unterelement (Knoten, Kante, Fläche) in der [3D Ansicht](3D_view/de.md) ausgewählt ist.

-    **Auswahlstil|Aufzählung**: steuert die Art und Weise, wie das Objekt hervorgehoben wird, wenn es eine [Form](Part_TopoShape/de.md) hat. Wenn es {{value|Form}} ist, wird die gesamte Form (Knoten, Kanten und Flächen) in der [3D Ansicht](3D_view/de.md) hervorgehoben; wenn es {{value|Begrenzungsrahmen}} ist, erscheint ein Begrenzungsrahmen um das Objekt herum und wird hervorgehoben.

## Skripten


**Siehe auch:**

[FreeCAD Skripten Grundlagen](FreeCAD_Scripting_Basics/de.md), und [geskriptete Objekte](scripted_objects/de.md).

Siehe [Part Formelement](Part_Feature/de.md) für die allgemeinen Informationen über das Hinzufügen von Objekten zum Programm.

Eine Anwendung FormelementPython wird mit der `addObject()` Methode des Dokuments erstellt.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::FeaturePython", "Name")
obj.Label = "Custom label"
```

Beispielsweise , die _.

Wenn das gewünschte Objekt eine Platzierung, eine Form, einen Anhang oder andere komplexe Eigenschaften haben soll, ist es besser, eine der komplexeren Klassen zu erstellen, zum Beispiel [App GeoFeature](App_GeoFeature/de.md), [Part Formelement](Part_Feature/de.md), oder [Part Teil2DObjekt](Part_Part2DObject/de.md).


{{Document objects navi

}}

---
[documentation index](../README.md) > App FeaturePython/de
