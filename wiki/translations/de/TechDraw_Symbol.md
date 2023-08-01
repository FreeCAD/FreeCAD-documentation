---
- GuiCommand:
   Name: TechDraw Symbol
   Name/de: TechDraw Symbol
   MenuLocation: TechDraw - TechDraw Views - SVG-Zeichnungselement einfügen
   Workbenches: [TechDraw](TechDraw_Workbench/de.md)
   SeeAlso: [TechDraw Vorlagen](TechDraw_Templates/de.md), [Draft SVG](Draft_SVG/de.md)
---

# TechDraw Symbol/de



## Beschreibung

Das Werkzeug *TechDraw Symbol* fügt eine [SVG](SVG/de.md)-Datei als Ansicht auf dem Zeichnungsblatt ein. Dieses Symbol kann alles sein, was als Erläuterung zur Zeichnung beiträgt und nicht weiter verändert werden muss.

<img alt="" src=images/TechDraw_SymbolSVG_sample.png  style="width:250px;"> 
*Kompassrose zum Zeichnungsblatt hinzugefügt; dieses Symbol erhält man durch Installation der Erweiterung "symbols_library" mit dem [Addon-Manager](Std_AddonMgr/de.md)*



## Anwendung

1.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswahl in der [Baumansicht](Tree_view/de.md) aktivieren.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_Symbol.svg" width=16px> [SVG-Zeichnungselement einfügen](TechDraw_Symbol/de.md)** button.
    -   Den Menüeintrag **TechDraw → TechDraw Views → <img src="images/TechDraw_Symbol.svg" width=16px> SVG-Zeichnungselement einfügen** auswählen.
3.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und noch kein Blatt aktiviert wurde, wird das Dialogfeld **Blattauswahl** geöffnet: {{Version/de|0.20}}
    1.  Das gewünschte Blatt auswählen.
    2.  Die Schaltfläche **OK** drücken.
4.  Ein Dateidialog wird geöffnet.
5.  Einen Speicherort und einen Dateinamen auswählen.
6.  Das Symbol wird eingefügt.
7.  Wahlweise seine {{PropertyData/de|Scale}} ändern, um seine Größe anzupassen.



## Hinweise

-    **Scale Type**für Symbole wird bei der Erstellung immer auf *Custom* (benutzerdefiniert) gesetzt. Dies dient der Bequemlichkeit, da Symbole fast immer anders skaliert werden als der Rest der Objekte auf dem Blatt.



## Eigenschaften

Siehe auch [TechDraw Ansicht](TechDraw_View/de#Eigenschaften.md).


{{TitleProperty|Drawing view}}

-    {{PropertyData/de|Editable Texts}}: Liste der editierbaren Texte, falls vorhanden.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Symbol kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


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



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Symbol/de
