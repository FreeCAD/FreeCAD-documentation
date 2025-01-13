---
 GuiCommand:
   Name: TechDraw ComplexSection
   Name/de: TechDraw KomplexerSchnitt
   MenuLocation: TechDraw , TechDraw Ansichten , Komplexe Schnittansicht einfügen
   Workbenches: TechDraw_Workbench/de
   Version: 0.21
   SeeAlso: TechDraw_SectionView/de, TechDraw_View/de
---

# TechDraw ComplexSection/de



## Beschreibung

Das Werkzeug **TechDraw KomplexerSchnitt** fügt einem Zeichnungsblatt eine Schnittansicht hinzu, die auf einer vorhandenen Bauteilansicht und einem Schnittprofil (Schnittkontur) basiert.

<img alt="" src=images/TechDraw_QuarterSection_example.png  style="width:350px;"> 
*Halbschnitt, mit dem Werkzeug Komplexe Schnittansicht erstellt*

<img alt="" src=images/TechDraw_AlignedSection_example.png  style="width:350px;"> 
*Abgewinkelter Schnitt, mit dem Werkzeug Komplexe Schnittansicht erstellt*

<img alt="" src=images/TechDraw_OffsetSection_example.png  style="width:350px;"> 
*Abgesetzter Schnitt, mit dem Werkzeug Komplexe Schnittansicht erstellt*



## Anwendung

1.  Eine Bauteilansicht und ein Profilobjekt in der [3D-Ansicht](3D_view/de.md) oder der [Baumansicht](Tree_view/de.md) auswählen. Profile sind normalerweise Skizzen, aber jedes Objekt, dessen Form in einen Draht (wire) umgewandelt werden kann, funktioniert.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_ComplexSection.svg" width=16px> [Komplexe Schnittansicht](TechDraw_ComplexSection/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → TechDraw Ansichten → <img src="images/TechDraw_ComplexSection.svg" width=16px> Komplexe Schnittansicht einfügen** auswählen.
3.  Im Aufgabenbereich wird ein Dialog geöffnet, der bei der Berechnung verschiedener Eigenschaften hilft. Für die Blickrichtung werden sinnvolle Werte ermittelt, diese können aber verändert werden.

<img alt="" src=images/TechDraw_ComplexSection_Taskview1.png  style="width:" height="380px;"> <img alt="" src=images/TechDraw_ComplexSection_Taskview2.png  style="width:" height="380px;">



## Eigenschaften

Eine komplexe Schnittansicht, formal ein {{Incode|TechDraw::DrawComplexSection}}-Objekt, wird von einer [Schnittansicht](TechDraw_SectionView/de#Eigenschaften.md), formal ein {{Incode|TechDraw::DrawViewSection}}-Objekt abgeleitet und erbt alle seine Eigenschaften. Es besitzt außerdem die folgenden Eigenschaften:



### Daten


{{TitleProperty|Cutting Tool}}

-    {{PropertyData/de|Cutting Tool Wire Object}}: Das Dokumentobjekt, dessen Form verwendet wird, um die Schnittkontur zu erstellen.

-    {{PropertyData/de|Projection Strategy}}: Steuert, wie der Schnitt durchgeführt wird und wie das Ergebnis auf dem Blatt projiziert wird:

    -   
        {{Value|Offset}}
        
        : Erzeugt einen einfachen Schnitt der Ausgangsform und projiziert das Ergebnis.

    -   
        {{Value|Aligned}}
        
        : Schneidet die Ausgangsform unter Verwendung eines Werkzeuges das jede Kante (edge) der Schnittkontur verwendet. Die Ergebnisse aller Schnitte werden, abhängig von der Orientierung der Schnittkontur, in einer vertikalen oder horizontalen Anordnung projiziert.

    -   
        {{Value|NoParallel}}
        
        : Wie Aligned, aber Abschnitte der Schnittkontur, die parallel zur Blickrichtung verlaufen, werden übersprungen.



## Hinweise

Siehe [TechDraw Schnittansicht](TechDraw_SectionView/de#Hinweise.md)



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Eine komplexe Schnittansicht kann mit [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen erstellt werden:


```python
doc = FreeCAD.ActiveDocument
box = doc.Box
profile = doc.Sketch
page = doc.Page

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = box
view.Direction = (0, 0, 1)

section = doc.addObject("TechDraw::DrawComplexSection", "ComplexSection")
page.addView(section)
section.BaseView = view
section.CuttingToolWireObject = profile
section.Direction = (0, 1, 0)
section.SectionNormal = (-1, 0, 0)
```



## Beispiele

Für weitere Information über Schnittansichten und einige Beispiele siehe: [TechDraw Schnittbeispiele](TechDraw_Section_Examples/de.md).

<img alt="" src=images/TechDraw_ExampleSection-10.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-13.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-15.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-17.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-34.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-35.png  style="width:80px;">





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ComplexSection/de
