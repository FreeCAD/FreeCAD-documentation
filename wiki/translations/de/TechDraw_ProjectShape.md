---
 GuiCommand:
   Name: TechDraw ProjectShape
   Name/de: TechDraw FormProjizieren
   MenuLocation: TechDraw , TechDraw Ansichten , Form projizieren...
   Workbenches: TechDraw_Workbench/de
   Shortcut: 
   Version: 0.20
   SeeAlso: Draft_Shape2DView/de
---

# TechDraw ProjectShape/de



## Beschreibung

Das Werkzeug **TechDraw FormProjizieren** erzeugt Projektionen von Formen. Die Projektionen werden in der [3D-Ansicht](3D_view/de.md) erzeugt und nicht auf einem [TechDraw-Zeichnungsblatt](TechDraw_PageDefault/de.md).

![](images/ProjectShape1_it.png )



## Anwendung

1.  Wahlweise die [3D-Ansicht](3D_view/de.md) drehen. Die Objekte werden auf eine Ebene parallel zum Bildschirm projiziert d.h. entlang der Blickrichtung der Kamera der 3D-Ansicht, die standardmäßig als {{PropertyData/de|Direction}} verwendet wird.
2.  Ein oder mehrere Objekte auswählen. Für jedes Objekt wird eine eigene Projektion erzeugt.
3.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_ProjectShape.svg" width=16px> [Form projizieren...](TechDraw_ProjectShape/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → TechDraw Views → <img src="images/TechDraw_ProjectShape.svg" width=16px> Form projizieren...** auswählen.
4.  Das Dialogfeld **Formen projizieren** wird geöffnet. Siehe [Eigenschaften](#Eigenschaften.md).
5.  Die gewünschten Optionen einstellen.
6.  Die gewählten Optionen sollten nicht zu einer leeren Projektion führen, weil das einen Fehler verursacht. Bei einem Objekt mit scharfen Kanten, wie etwa [Part Würfel](Part_Box/de.md), muss die Option **Sichtbare scharfe Kanten** und/oder **Verdeckte scharfe Kanten** ausgewählt werden.
7.  Die Schaltfläche **OK** drücken.
8.  Die Projektion wird auf der XY-Ebene dargestellt.
9.  Wahlweise die {{PropertyData/de|Placement}} und/oder {{PropertyData/de|Direction}} der Projektion ändern.



## Eigenschaften

Die Projektion wird von einem [Part Feature](Part_Feature.md) abgeleitet und erbt alle Eigenschaften. Sie hat zusätzlich folgende Eigenschaften:



### Daten


{{TitleProperty|Projection}}

-    **Source|Link**: Die zu projizierende Form.

-    **Direction|Vector**: Die Richtung der Projektion. Das ist der Normalvektor auf die Projektionsfläche.

-    **VCompound|Bool**: Wenn `True`, dann werden sichtbare scharfe Kanten gezeigt. Beispiel: alle Kanten einer [Part Box](Part_Box.md).

-    **Rg1 Line VCompound|Bool**: Wenn `True`, dann werden sichtbare glatte Kanten gezeigt. Beispiel: die Kanten zwischen einer Rundung und den benachbarten Flächen.

-    **Rg NLine VCompound|Bool**: Wenn `True`, dann werden sichtbare Nähte gezeigt. Beispiel: die Naht einer 360° zylindrischen Fläche.

-    **Out Line VCompound|Bool**: Wenn `True`, dann werden sichtbare Konturen (die nicht scharf sind) gezeigt. Beispiel: die Seitenansicht eines [Part Cylinder](Part_Cylinder.md) hat zwei solche Kanten.

-    **Iso Line VCompound|Bool**: Wenn `True`, dann werden sichtbare Isoparameter gezeigt. Dies funktioniert derzeit nicht.

-    **HCompound|Bool**: Wenn `True`, dann werden unsichtbare scharfe Kanten gezeigt.

-    **Rg1 Line HCompound|Bool**: Wenn `True`, dann werden unsichtbare glatte Kanten gezeigt.

-    **Rg NLine HCompound|Bool**: Wenn `True`, dann werden unsichtbare Nähte gezeigt.

-    **Out Line HCompound|Bool**: Wenn `True`, dann werden unsichtbare Konturen gezeigt.

-    **Iso Line HCompound|Bool**: Wenn `True`, dann werden unsichtbare Isoparameter gezeigt. Dies funktioniert derzeit nicht.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ProjectShape/de
