---
 GuiCommand:
   Name: TechDraw AreaDimension
   Name/de: TechDraw Flächeninhalt
   MenuLocation: TechDraw , Maßeinträge , Flächeninhalt einfügen
   Workbenches: TechDraw_Workbench/de
   Version: 1.0
   SeeAlso: TechDraw_ExtensionAreaAnnotation/de
---

# TechDraw AreaDimension/de



## Beschreibung

Das Werkzeug **TechDraw Flächeninhalt** fügt einen Hinweis mit dem Flächeninhalt zu einer Fläche in einer Bauteilansicht hinzu.

![](images/TechDraw_AreaDimension_Example.png ) 
*Flächenangabe einer Fläche mit einem Loch. Siehe [Einschränkungen](#Einschränkungen.md).*



## Anwendung

1.  Eine Fläche auswählen. Die Geometrie kann in der [3D-Ansicht](3D_view/de.md) oder in der Zeichnung ausgewählt werden.
2.  Wenn die Geometrie in der 3D-Ansicht ausgewählt wurde: Die richtige TechDraw-Ansicht zur Auswahl hinzufügen, indem sie in der [Baumansicht](Tree_view/de.md) ausgewählt wird.
3.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Wenn die [Einstellung](TechDraw_Preferences/de#Maßeinträge.md) **Maß-Werkzeuge** auf {{Value|Einzelnes Werkzeug}} (Standardwert) gesetzt ist: Den Nach-unten-Pfeil rechts neben der Schaltfläche **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** drücken und die Option **<img src="images/TechDraw_AreaDimension.svg" width=16px> Flächeninhalt einfügen** im Ausklappen auswählen.
    -   Wenn diese Einstellung einen anderen Wert besitzt: die Schaltfläche **<img src="images/TechDraw_AreaDimension.svg" width=16px> [Flächeninhalt einfügen](TechDraw_AreaDimension/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Maßeinträge → <img src="images/TechDraw_AreaDimension.svg" width=16px> Flächeninhalt einfügen** auswählen.
4.  Ein Maß wird zur Ansicht hinzugefügt.
5.  Das Maß kann an die gewünschte Position gezogen werden.
6.  Wenn erforderlich, die Toleranz hinzufügen, wie auf [dieser Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben.



## Einschränkungen

-    {{VersionMinus/de|1.0}}: Das Werkzeug kann nur Löcher in Flächen erkennen, die in der 3D-Ansicht ausgewählt wurden. Um den richtigen Flächeninhalt für so eine Fläche zu erhalten, die in der Zeichnung ausgewählt wurde, gibt es folgende Möglichkeit:

    1.  Die richtige {{PropertyData/de|References 3D}} mit ![\|x16px](images/TechDraw_DimensionRepair.svg ) [TechDraw Maßreparatur](TechDraw_DimensionRepair/de.md) einstellen.
    2.  Die {{PropertyData/de|Measure Type}} auf {{Value|True}} ändern.
    3.  ![\|x16px](images/Std_Refresh.svg ) [Std Aktualisieren](Std_Refresh/de.md) aufrufen. falls erforderlich.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw AreaDimension/de
