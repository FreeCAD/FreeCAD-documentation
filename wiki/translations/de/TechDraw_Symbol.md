---
- GuiCommand:/de
   Name:TechDraw Symbol   Name/de:TechDraw Symbol
   MenuLocation:TechDraw → SVG Symbol einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Vorlagen](TechDraw_Templates/de.md), [Entwurf SVG](Draft_SVG/de.md)
---

## Beschreibung

Das Symbolwerkzeug fügt eine [SVG](SVG/de.md)-Datei als Ansicht in die Zeichnungsseite ein. Dieses Symbol kann alles sein, was als Notiz zur Zeichnung beiträgt und nicht weiter verändert werden muss.

<img alt="" src=images/TechDraw_SymbolSVG_sample.png  style="width:250px;"> 
*Kompassrose zur Zeichnungsseite hinzugefügt; dieses Symbol ist verfügbar durch Installation der Symbol Bibliothek Erweiterung mit dem [Erweiterungsverwalter](Std_AddonMgr/de.md)*

## Anwendung

1.  Drücke die **<img src="images/TechDraw_Symbol.svg" width=16px> [SVG Symbol einfügen](TechDraw_Symbol/de.md)** Schaltfläche
2.  Ein Dateispeicher Dialog wird geöffnet.
3.  Wähle einen Speicherort und einen Dateinamen.
4.  Drücke **OK**

Wenn das Symbol größer als erwartet dargestellt wird, kann die Skalierungseigenschaft genutzt werden, um die Größe anzupassen.

## Hinweise

-    **Scale Type**für Symbole wird bei der Erstellung immer auf *Angepasst* gesetzt. Dies dient der Bequemlichkeit, da Symbole fast immer anders skaliert werden als der Rest der Objekte auf der Seite.

## Scripting


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics/de.md).

Das Symbol Werkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole aus mit den folgenden Funktionen verwendet werden:


```python
sym = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewSymbol','TestSymbol')
rc = page.addView(anno)
f = open(unicode(symbolFileSpec,'utf-8'),'r')
svg = f.read()
f.close()
sym.Symbol = svg
rc = page.addView(sym)
```





{{TechDraw Tools navi

}}  
