---
- GuiCommand:
   Name: TechDraw ShowAll
   Name/de:  TechDraw AllesAnzeigen
   MenuLocation: TechDraw - Linien hinzufügen - Ausgeblendete Kanten ein-/ausblenden
   Workbenches: [TechDraw](TechDraw_Workbench/de.md)
   Version: 0.19
   SeeAlso: [LiniendarstellungÄndern](TechDraw_DecorateLine/de.md)
---

# TechDraw ShowAll/de



## Beschreibung

Das Werkzeug **TechDraw AllesAnzeigen** ist dazu gedacht, unsichtbare Linien einer Ansicht zeitweilig ein- und wieder auszublenden. Linien können mit dem Werkzeug [TechDraw LiniendarstellungÄndern](TechDraw_DecorateLine/de.md) auf unsichtbar gesetzt werden. Dabei ist zu Beachten, dass \"unsichtbar\" hier eine Darstellungseigenschaft ist; nicht zu verwechseln mit verdeckten Kanten, die geometrische Konstrukte sind.



## Verwendung

1.  Eine Ansicht mit unsichtbaren Linien auf einem Zeichnungsblatt oder in der [Baumansicht](Tree_view/de.md). auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_ShowAll.svg" width=16px> [Ausgeblendete Kanten ein-/ausblenden](TechDraw_ShowAll/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Linien hinzufügen → <img src="images/TechDraw_ShowAll.svg" width=16px> Ausgeblendete Kanten ein-/ausblenden** auswählen.
3.  Alle unsichtbaren (ausgeblendeten) Linien in der Ansicht werden entweder eingeblendet oder ausgeblendet.



## Hinweise

-   Um unsichtbare Linien dauerhaft sichtbar zu machen, wird das Werkzeug <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [TechDraw LiniendarstellungÄndern](TechDraw_DecorateLine/de.md) verwendet.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Die Wirkung des AllesAnzeigen Werkzeugs kann in [Makros](Macros/de.md) oder der [Python](Python/de.md)-Konsole dupliziert werden. 
```python
v = App.ActiveDocument.View
vvo = v.ViewObject
vvo.ShowAllEdges = True
App.ActiveDocument.recompute()
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ShowAll/de
