---
- GuiCommand:/de
   Name:Part TransformedCopy
   MenuLocation:Part → Erzeuge eine Kopie → Erzeuge transformierte Kopie
   Workbenches:[Arbeitsbereich Part](Part_Workbench/de.md)
   Version:0.19
   SeeAlso:[SimpleCopy](Part_SimpleCopy.md), [ElementKopie](Part_ElementCopy/de.md), [Form Verfeinern](Part_RefineShape/de.md)
---


</div>

## Beschreibung

[Part TransformierteKopie](Part_TransformedCopy/de.md) erzeugt eine nichtparametrische Kopie eines Objekts, das aus seiner ursprünglichen Position verschoben wurde.


<div class="mw-translate-fuzzy">

To produce other non-parametric copies use [EinfacheKopie](Part_SimpleCopy/de.md), [ElementKopie](Part_ElementCopy/de.md), oder [FormVerfeinern](Part_RefineShape/de.md).


</div>


<div class="mw-translate-fuzzy">

## Anwendung


</div>

1.  Wähle ein Objekt aus, das Du kopieren möchtest.
2.  Gehe zum Menü {{MenuCommand/de|Teil → Erstelle eine Kopie → <img src=images/Part_TransformedCopy.svg style="width:16px"> [Erzeuge transformierte Kopie](Part_TransformedCopy/de.md)}}.

## Eigenschaften

### Daten

Die Kopie hat eine einfache {{PropertyData/de|Positionierung}} Eigenschaft wie jede andere [Part Funktion](Part_Feature/de.md).

### Ansicht

Die Kopie hat einfache Ansichtseigenschaften wie jede andere [Teilfunktion](Part_Feature/de.md).

## Scripting

The **Part TransformedCopy** command can be applied after selecting one or more objects in the [Tree view](Tree_view.md):


```python
FreeCADGui.runCommand('Part_TransformedCopy')
```

The selection can be manual (by using the mouse), or via the [Python console](Python_console.md).
To know more about selecting objects programmatically, refer to [Selection methods](Selection_methods.md).





 
