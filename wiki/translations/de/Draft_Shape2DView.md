---
 GuiCommand:
   Name: Draft Shape2DView
   Name/de: Draft Form2DAnsicht
   MenuLocation: Änderung , Form in 2D Ansicht
   Workbenches: Draft_Workbench/de
   SeeAlso: TechDraw_ProjectShape/de
---

# Draft Shape2DView/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Shape2DView.svg  style="width:24px;"> **Draft Form2DAnsicht** erstellt 2D-Projektionen von ausgewählten Objekten, in der Regel 3D-Festkörper oder [Arch Schnittebenen](Arch_SectionPlane/de.md). Die Projektionen werden in der [3D-Ansicht](3D_view/de.md) dargestellt.

Draft Form2DAnsichten können im [Arbeitsbereich TechDraw](TechDraw_Workbench/de.md) auf einer Seite mit dem [TechDraw DraftAnsicht](TechDraw_DraftView/de.md) Befehl angezeigt werden. Wahlweise bietet der Arbeitsbereich [TechDraw](TechDraw_Workbench/de.md) seine eigenen Befehle zum Projizieren an. Aber diese Projektionen werden nur in der Seite der Zeichnung, nicht in der [3D Ansicht](3D_view/de.md) angezeigt.

![](images/Draft_Shape2DView_example.jpg ) 
*Projektion einer Festkörper Form in der XY Ebene*



## Anwendung

1.  Drehe wahlweise die [3D Ansicht](3D_view/de.md). Die Blickrichtung der Kamera in der [3D Ansicht](3D_view/de.md) bestimmt den Projektionsvektor. Zum Beispiel eine [Draufsicht](Std_ViewTop/de.md) wird auf die XY Ebene projiziert. Bei Projektionen die aus einer [Arch Schnittebene](Arch_SectionPlane/de.md) entstehen wird der Projektionsvektor nicht beachtet.
2.  Wahlweise wähle eines oder mehrere Objekte.
3.  Es gibt verschiedene Möglichkeiten um den Befehl zu aktivieren:
    -   Drücke die **<img src="images/Draft_Shape2DView.svg" width=16px> [Form 2D Ansicht](Draft_Shape2DView/de.md)** Schaltfläche.
    -   Wähle die **Änderungen → <img src="images/Draft_Shape2DView.svg" width=16px> Form 2D Ansicht** Option aus dem Menü.
4.  Wenn du bis jetzt noch kein Objekt ausgewählt hast: wähle ein Objekt in der [3D Ansicht](3D_view/de.md).
5.  Die projizierten Objekte werden in der XY Ebene erzeugt.



## Wie erzeugt man Pläne und Schnitte mit unterschiedlicher Strichbreite 

<img alt="" src=images/Draft_shape2dview_example_plan.png  style="width:700px;">

Zeichnungen mit unterschiedlicher Strichbreite für gesehene und geschnittene Linien können durch Verwendung von zwei shape2Dview Objekten aus der selben [Arch Schnittebene](Arch_SectionPlane/de.md) erzeugt werden. Eines der Form2DAnsichten Objekte hat seinen Projektionsmodus auf **Solid** gesetzt, was zum Zeichnen der gesehenen Linien führt, und ein anderes ist auf **Schnittlinien** gesetzt um die Schnittlinien zu zeichnen. Die zwei Form2DAnsichten werden dann über einander an dem selben Ort platziert.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft Shape2DView-Objekt wird von einem [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Draft}}

-    **Auto Update|Bool**: legt fest, ob die Projektion automatisch neu berechnet wird, wenn sich das **Base** Objekt ändert. Wählen von {{False}} kann ützlich sein, wenn es in einem Dokument viele Draft Form2DAnsichten gibt oder sie kompliziert sind. Falls auf {{False}} gesetzt muss der Befehl [Std Refresh](Std_Refresh.md) zum neuberechnen der Projektion verwendet werden.

-    **Base|Link**: legt das Objekt welches projiziert werden muss fest.

-    **Clip|Bool**: falls True, wird der Inhalt falls möglich mit dem Rand der Schnittebene abgeschnitten. Dies überschreibt die Abschneiden Eigenschaft des Objektes.

-    **Face Numbers|IntegerList**: legt die Indizes der zu projizierenden Flächen fest. Funktioniert nur wenn {{PropertyData/de|Projektionsmodus}} auf {{Value|Individual Faces}} gesetzt ist.

-    **Fuse Arch|Bool**: legt fest ob [BIM Objekte](BIM_Workbench/de.md) mit gleichem Typ und Material vereinigt werden oder nicht.

-    **Hidden Lines|Bool**: legt fest, ob versteckte Linien dargestellt werden oder nicht.

-    **In Place|Bool**: funktioniert nur wenn das gewählte Objekt ein [Arch Schnittebene](Arch_SectionPlane/de.md) ist, und {{PropertyData/de|Projektionsmodus}} den Wert {{Value|Cutlines}} oder {{Value|Cutfaces}}hat, legt fest, ob die Projektion co-planar mit der Schnittebene erscheint.

-    **Projection|Vector**: legt die Richtung der Projektion fest. Wird ignoriert wenn **Base** eine [Arch Schnittebene](Arch_SectionPlane/de.md) ist.

-    **Projection Mode|Enumeration**: legt dem Modus der Projektion fest. Folgende Modi sind möglich:

    -   
        {{Value|Solid}}
        
        : projiziert das gesamte gewählte Objekt.

    -   
        {{Value|Individual Faces}}
        
        : projiziert nur die Flächen aus der {{PropertyData/de|Flächen Nummern}} Liste.

    -   
        {{Value|Cutlines}}
        
        : funktioniert nur wenn das gewählte Objekt eine [Arch Schnittebene](Arch_SectionPlane/de.md) ist, projiziert nur die von der Schnittebene geschnittenen Kanten.

    -   
        {{Value|Cutfaces}}
        
        : funktioniert nur wenn das gewählte Objekt eine [Arch Schnittebene](Arch_SectionPlane/de.md) ist, projiziert jene Bereiche die von der Schnittebene durch Festkörper geschnitten wurden als Flächen.

    -   
        {{Value|Solid faces}}
        
        : projiziert das gesamte gewählte Objekt durch schneiden der Flächen eine nach der anderen. Kann verwendet werden, falls der {{Value|Solid}} Modus falsche Ergebnisse liefert.

-    **Segment Length|Float**: legt die Größe von linearen Elemente in Millimetern fest falls {{PropertyData/de|Mosaik}} auf `True` steht.

-    **Tessellation|Bool**: legt fest, ob ein Mosaik erzeugt werden soll. Mosaik bedeutet, dass Kurven durch eine Reihe von Liniensegmenten ersetzt werden. Das kann zu intensiven Rechnungen führen wenn die {{PropertyData/de|Segment Länge}} zu kurz ist.

-    **Visible Only|Bool**: legt fest, ob die Projektion wenn sie sichtbar ist neu berechnet werden soll.

-    **Exclusion Points|Vector list**: Eine Liste mit ausgeschlossenen Punkten. Kanten die durch einen dieser Punkte gehen werden nicht gezeichnet.

-    **Exclusion Names|String list**: Eine Liste mit Objektnamen. Jedes sichtbare oder geschnittene Kind Objekt in dieser Liste wird nicht gezeichnet. <small>(v0.21)</small> 



### Ansicht


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: nicht verwendet.

-    **Pattern Size|Float**: nicht verwendet.



## Skripten

Siehe auch: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Verwende zum Erzeugen einer Projektion die Methode `make_shape2dview` (<small>(v0.19)</small> ) des Moduls Draft. Diese Methode ersetzt die veraltete Methode `makeShape2DView`.


```python
shape2dview = make_shape2dview(baseobj, projectionVector=None, facenumbers=[])
```

-    `baseobj`ist das Objekt, welches projiziert werden soll.

-    `projectionVector`ist der Projektionsvektor. Falls nicht angegeben wird die Z Achse verwendet.

-    `facenumbers`ist eine Liste der Flächennummern (0-beginnend). Falls vorhanden werden nur diese Flächen berücksichtigt.

-    `shape2dview`wird mit der erzeugten 2D Projektion zurück geliefert.

Ändere falls notwendig die Eigenschaft `ProjectionMode` des erzeugten Objektes. Sie kann `"Solid"`, `"Individual Faces"`, `"Cutlines"`, `"Cutfaces"` oder `"Solid faces"` sein.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 500
box.Height = 1000

shape1 = Draft.make_shape2dview(box)

shape2 = Draft.make_shape2dview(box, App.Vector(1, -1, 1))

shape3 = Draft.make_shape2dview(box, App.Vector(-1, 1, 1), [0, 5])
shape3.ProjectionMode = "Individual Faces"

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Shape2DView/de
