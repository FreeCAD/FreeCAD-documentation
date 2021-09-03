---
- GuiCommand:/de
   Name:Part SimpleCopy‎
   Name/de:Part EinfacheKopie
   MenuLocation:Part → Erzeuge eine Kopie → Erzeuge eine einfache Kopie
   Workbenches:[Part Arbeitsbereich](Part_Workbench/de.md)
   SeeAlso:[Kopie](Std_Copy/de.md), [Dupliziere Auswahl](Std_DuplicateSelection/de.md), [UmgewandelteKopie](Part_TransformedCopy/de.md), [ElementKopie](Part_ElementCopy/de.md), [FormVerfeinern](Part_RefineShape/de.md)
---


</div>

## Beschreibung


**![](images/)[Part_EinfacheKopie](Part_SimpleCopy/de.md)**

erzeugt eine Kopie, die keine parametrische Historie hat; die Schritte und Arbeitsgänge, die zur Erstellung erforderlich sind, sind nicht mehr zugänglich.

**Alternativ**, um andere nichtparametrische Kopien zu erstellen, verwende <img alt="" src=images/Part_TransformedCopy.svg  style="width:16px;"> [TransformedCopy](Part_TransformedCopy/de.md), <img alt="" src=images/Part_ElementCopy.svg  style="width:16px;">[ElementKopie](Part_ElementCopy/de.md) und und <img alt="" src=images/Part_RefineShape.svg  style="width:16px;">[FormVerfeinern](Part_RefineShape/de.md).

## Anwendung

1.  Wähle ein Objekt aus, für das Du eine Kopie erstellen möchtest.
2.  Gehe zum Menü {{MenuCommand|Part → Erstelle eine Kopie → ![](images/)_[Einfache_Kopie_erstellen](Part_SimpleCopy/de.md)}}.

## Eigenschaften

### Daten

Die Kopie hat eine einfache {{PropertyData/de|Platzierung}} Eigenschaft wie jede andere [Part Feature](Part_Feature/de.md).

### Ansicht

Die Kopie hat einfache Ansichtseigenschaften wie jede andere [Teilfunktion](Part_Feature/de.md).

## Skripten

The **Part SimpleCopy**‎ command can be applied after selecting one or more objects in the [Tree view](Tree_view.md):


```python
FreeCADGui.runCommand('Part_SimpleCopy')
```

The selection can be manual (by using the mouse), or via the [Python console](Python_console.md).
To know more about selecting objects programmatically, refer to [Selection methods](Selection_methods.md).


<div class="mw-translate-fuzzy">





</div>


  
