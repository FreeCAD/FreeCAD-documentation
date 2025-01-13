---
 GuiCommand:
   Name: TechDraw Symbol
   Name/de: TechDraw Zeichnungselement
   MenuLocation: TechDraw , TechDraw Views , SVG-Zeichnungselement einfügen
   Workbenches: TechDraw_Workbench/de
   SeeAlso: TechDraw_Templates/de, Draft_SVG/de
---

# TechDraw Symbol/de



## Beschreibung

Das Werkzeug **TechDraw Zeichnungselement** fügt ein Symbol-Objekt ein. Ein Zeichnungselement ist eine abgespeckte Ansicht, die nur eine einzige [SVG](SVG/de.md)-Datei enthält, die der Spezifikation svg-tiny entspricht (siehe [TechDraw Vorlagen](TechDraw_Templates/de#Hinweise.md)). (Das Zeichnungselement wird an anderen Stellen auch noch mit Symbol bezeichnet. Bitte nicht mit den hier ebenfalls Symbol genannten [Icons](Artwork_Guidelines/de.md) verwechseln)

Ein Zeichnungselement kann alles sein, das beim Beschriften einer Zeichnung hilft und das nicht weiter verändert werden muss; trotzdem darf es [editierbare Texte](Svg_Namespace/de#freecad_editable.md) enthalten.


{{Version/de|1.0}}

: Auch das Werkzeug [TechDraw Ansicht](TechDraw_View/de.md) kann ein Zeichnungselement erstellen.

<img alt="" src=images/TechDraw_SymbolSVG_sample.png  style="width:250px;"> 
*Kompassrose zum Zeichnungsblatt hinzugefügt; dieses Zeichnungselement erhält man durch Installation der Erweiterung "symbols_library" mit dem [Addon-Manager](Std_AddonMgr/de.md)*



## Anwendung

1.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswahl in der [Baumansicht](Tree_view/de.md) aktivieren.
2.  Den Menüeintrag **TechDraw → TechDraw Views → <img src="images/TechDraw_Symbol.svg" width=16px> SVG-Zeichnungselement einfügen** auswählen.
3.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und noch kein Blatt aktiviert wurde, wird das Dialogfenster **Blattauswahl** geöffnet:
    1.  Das gewünschte Blatt auswählen.
    2.  Die Schaltfläche **OK** drücken.
4.  Ein Datei-Browser wird geöffnet.
5.  Eine SVG-Datei auswählen.
6.  Ein Zeichnungselement wird eingefügt.
7.  Wahlweise seine {{PropertyData/de|Scale}} ändern, um seine Größe anzupassen.



## Hinweise

-    **Scale Type**für Zeichnungselemente ist bei der Erstellung immer *Custom* (benutzerdefiniert) eingestellt. Dies dient der Bequemlichkeit, da Zeichnungselemente fast immer anders skaliert werden als der Rest der Objekte auf dem Blatt.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Eine Zeichnungselement, oder formal ein {{Incode|TechDraw::DrawViewSymbol}}-Objekt, besitzt die gemeinsamen [Eigenschaften](TechDraw_View/de#Eigenschaften_der_Bauteilansicht.md) aller Ansichtsarten. Sie enthält außerdem die folgenden Eigenschaften:



### Daten


{{TitleProperty|Drawing view}}

-    {{PropertyData/de|Symbol|String|Hidden}}: Der SVG-Code, der dieses Zeichnungselement definiert.

-    {{PropertyData/de|Editable Texts|StringList|Hidden}}: Ersatzwerte für bearbeitbare Zeichenfolgen in diesem Zeichnungselement.

-    {{PropertyData/de|Owner|Link}}: Element dem dieses Zeichnungselement zugeordnet ist. {{Version/de|1.0}}



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Zeichnungselement (Symbol) kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
sym = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewSymbol','TestSymbol')
rc = page.addView(anno)
f = open(unicode(symbolFileSpec,'utf-8'),'r')
svg = f.read()
f.close()
sym.Symbol = svg
rc = page.addView(sym)
```





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Symbol/de
