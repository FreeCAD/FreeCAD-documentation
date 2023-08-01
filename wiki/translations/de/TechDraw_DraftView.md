---
- GuiCommand:
   Name:TechDraw DraftView
   Name/de:TechDraw DraftAnsicht
   MenuLocation:TechDraw → Views From Other Workbenches → Objekt des Draft-Arbeitsbereiches einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md), [Draft](Draft_Workbench/de.md)
   SeeAlso:[TechDraw ArchAnsicht](TechDraw_ArchView/de.md)
---

# TechDraw DraftView/de



## Beschreibung

Das Werkzeug **TechDraw DraftAnsicht** fügt eine Ansicht eines ausgewählten [Part](Part_Workbench/de.md)-basierten Objekts oder eines Gruppenobjekts in ein Zeichnungsblatt ein. Anders als beim Standardwerkzeug <img alt="" src=images/TechDraw_View.svg  style="width:24px;"> [Ansicht](TechDraw_View/de.md), werden die mit diesem Werkzeug erstellten Ansichten mit dem Arbeitsbereich <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/de.md) bearbeitet und sind besonders für die Darstellung von 2D-Objekten entwickelt. Siehe [Hinweise](#Hinweise.md).

![](images/TechDraw_DraftView_example.png ) 
*Draft-Elemente wie Kreise und Anordnungen importiert in ein TechDraw-Zeichnungsblatt*



## Anwendung

1.  Wahlweise die [3D-Ansicht](3D_view/de.md) drehen. Die Kameraausrichtung der [3D-Ansicht](3D_view/de.md) legt den Startwert der {{PropertyData/de|Direction}} der Ansicht fest.
2.  Ein oder mehrere Objekte in der [3D-Ansicht](3D_view/de.md) oder der [Baumansicht](Tree_view/de.md) auswählen. Für jedes Objekt wird eine separate Ansicht erstellt.
3.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswahl in der [Baumansicht](Tree_view/de.md) aktivieren.
4.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_DraftView.svg" width=16px> [Objekt des Arbeitsbereichs Draft einfügen](TechDraw_DraftView/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Views From Other Workbenches → <img src="images/TechDraw_DraftView.svg" width=16px> Objekt des Arbeitsbereichs Draft einfügen** auswählen.
5.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und noch kein Blatt aktiviert wurde, wird das Dialogfeld **Blattauswahl** geöffnet: {{Version/de|0.20}}
    1.  Das gewünschte Blatt auswählen.
    2.  Die Schaltfläche **OK** drücken.



## Optionen

-   Das Erstellen einer Draft-Ansicht (DraftView-Objekt) von einer Ebene verwendet rekursiv alle Objekte, die auf dieser Ebene gefunden wurden. Die Ansicht wird automatisch aktualisiert, wenn sich der Inhalt der Ebene ändert.
-   Es werden keine verdeckten Kanten entfernt. Jede Fläche, die in dem (den) verwendeten Objekt(en) gefunden wird, wird einfach entlang des Richtungsvektors projiziert, es werden keine besonderen Maßnahmen ergriffen, wenn sich Flächen überlappen.
-   Die Draft-Ansicht unterstützt auch alle Draft-Objekte, die nicht auf Bauteilen basierten, wie z.B. Maße und Texte.
-   Farbe, Linienbreite und Linienart können in den Eigenschaften angegeben werden. Linienarten können durch direkte Angabe eines [stroke-dasharray](https://www.w3.org/TR/SVG/painting.html#StrokeProperties) Wertes, wie z.B. 3,5 fein abgestimmt werden.
-   Projizierte Flächen werden mit der Flächenfarbe gefüllt



## Hinweise

Die Draft-Ansicht wird innerhalb des Arbeitsbereiches [Draft](Draft_Workbench/de.md) gerendert, daher hat TechDraw nur eingeschränkte Kontrolle über ihr Erscheinungsbild. Man muss möglicherweise Änderungen innerhalb von Draft vornehmen, um die gewünschte Darstellung zu erhalten.



## Eigenschaften

Siehe auch [TechDraw Ansicht](TechDraw_View/de#Eigenschaften.md)



### Daten


{{TitleProperty|Draft view}}

-    **Source|Link**: Das Draft-Objekt, das angezeigt werden soll.

-    **Line Width|Float**: Die Breite der Linien, unabhängig vom Maßstab.

-    **Font Size|Float**: Die Schrifthöhe aller Texte in dieser Ansicht (Texte und Maße).

-    **Direction|Vector**: Die zu verwendende Projektionsrichtung.

-    **Color|Color**: Die Linienfarbe.

-    **Line Style|String**: Eine Linienart, die für diese Ansicht zu verwenden ist. Kann {{Value|Solid}}, {{Value|Dashed}}, {{Value|Dashdot}}, {{Value|Dot}} (für Voll-, Strich-, Strich-Punkt-, Punktlinie) oder ein SVG-Linienmuster wie {{Value|0.20,0.20}} sein..

-    **Line Spacing|Float**: Der zu verwendende Zeilenabstand bei mehrzeiligen Texten.

-    **Override Style|Bool**: Wenn `True`, überschreiben Linienfarbe, Linienbreite und Linienart dieser Ansicht jene des gerenderten Objekts.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug DraftAnsicht kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit folgenden Funktionen verwendet werden:


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDraft','TestDraft')
dv.Source = myDraftbject
rc = page.addView(dv)
```





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DraftView/de
