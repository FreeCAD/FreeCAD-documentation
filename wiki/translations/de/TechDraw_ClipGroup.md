---
 GuiCommand:
   Name: TechDraw ClipGroup
   Name/de: TechDraw Ausschnittsgruppe
   MenuLocation: TechDraw , Clipped Views , Ausschnittsgruppe einfügen
   Workbenches: TechDraw_Workbench/de
   SeeAlso: TechDraw_ClipGroupAdd/de, TechDraw_ClipGroupRemove/de
---

# TechDraw ClipGroup/de



## Beschreibung

Das Werkzeug **TechDraw Ausschnittsgruppe** erstellt ein Ausschnittfenster, das Ansichten enthalten kann.

![](images/TechDraw_Clipview.png ) 
*Ausschnittfenster, das verschiedene vorhandene Ansichten beschneidet*



## Verwendung

1.  \# Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswahl in der [Baumansicht](Tree_view/de.md) aktivieren.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_ClipGroup.svg" width=16px> [Ausschnittsgruppe einfügen](TechDraw_ClipGroup/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Clipped Views → <img src="images/TechDraw_ClipGroup.svg" width=16px> Ausschnittsgruppe einfügen** auswählen.
3.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und noch kein Blatt aktiviert wurde, wird das Dialogfeld **Blattauswahl** geöffnet: {{Version/de|0.20}}
    1.  Das gewünschte Blatt auswählen.
    2.  Die Schaltfläche **OK** drücken.



## Eigenschaften

-    {{PropertyData/de|Width}}: Die Breite des Ausschnittfensters in Einheiten.

-    {{PropertyData/de|Height}}: Die Höhe des Ausschnittfensters in Einheiten.

-    {{PropertyData/de|ShowFrame}}: Wenn `True`, wird ein Rahmen um das Ausschnittfenster herum dargestellt.

-    {{PropertyData/de|ShowLabels}}: Wenn `True`, werden Benennungen der Ansichten im Ausschnittfenster angezeigt. **HINWEIS:** entfernt in v0.19.

-    {{PropertyData/de|Views}}: Die im Ausschnittfenster enthaltenen Ansichten.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ClipGroup/de
