---
- GuiCommand   */de
   Name   *TechDraw Symbol
   Name/de   *TechDraw Symbol
   MenuLocation   *TechDraw → SVG-Zeichnungselement einfügen
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso   *[TechDraw Vorlagen](TechDraw_Templates/de.md), [Draft SVG](Draft_SVG/de.md)
---

# TechDraw Symbol/de

## Beschreibung

Das Symbolwerkzeug fügt eine [SVG](SVG/de.md)-Datei als Ansicht auf dem Zeichnungsblatt ein. Dieses Symbol kann alles sein, was als Erläuterung zur Zeichnung beiträgt und nicht weiter verändert werden muss.

<img alt="" src=images/TechDraw_SymbolSVG_sample.png  style="width   *250px;"> 
*Kompassrose zum Zeichnungsblatt hinzugefügt; dieses Symbol erhält man durch Installation der Erweiterung "symbols_library" mit dem [Addon-Manager](Std_AddonMgr/de.md)*

## Anwendung

1.  Die Schaltfläche **<img src="images/TechDraw_Symbol.svg" width=16px> [SVG-Zeichnungselement einfügen](TechDraw_Symbol/de.md)** drücken.

2.  Ein Dateidialog wird geöffnet.

3.  Einen Speicherort und einen Dateinamen auswählen.

4.  
    **OK**drücken.

Wenn das Symbol größer als erwartet dargestellt wird, kann die Eigenschaft Scale (Skalierung) genutzt werden, um die Größe anzupassen.

## Hinweise

-    **Scale Type**für Symbole wird bei der Erstellung immer auf *Custom* (benutzerdefiniert) gesetzt. Dies dient der Bequemlichkeit, da Symbole fast immer anders skaliert werden als der Rest der Objekte auf dem Blatt.

## Eigenschaften

See also [TechDraw View](TechDraw_View#Properties.md).


{{TitleProperty|Drawing view}}

-    {{PropertyData/de|Editable Texts}}   * Liste der editierbaren Texte, falls vorhanden.

## Skripten


**Siehe auch   ***

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Symbol kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden   *


```python
sym = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewSymbol','TestSymbol')
rc = page.addView(anno)
f = open(unicode(symbolFileSpec,'utf-8'),'r')
svg = f.read()
f.close()
sym.Symbol = svg
rc = page.addView(sym)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Symbol/de
