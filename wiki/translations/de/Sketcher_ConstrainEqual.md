---
- GuiCommand:/de
   Name:Sketcher ConstrainEqual
   Name/de:Sketcher GleichheitFestlegen 
   MenuLocation:Sketch → Skizzen-Beschränkungen →Gleichheit festlegen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**E**
   SeeAlso:[Sketcher RadiusFestlegen](Sketcher_ConstrainRadius/de.md)
---

# Sketcher ConstrainEqual/de

## Beschreibung

Die Randbedingung GleichheitFestlegen legt fest, dass zwei oder mehr Linienabschnitte einer Linie, eines Linienzuges oder eines Rechtecks die gleiche Länge haben. Wenn sie auf Bögen oder Kreise angewendet wird, werden die Radien auf Gleichheit festgelegt. Sie kann nicht auf geometrische Grundelemente angewendet werden, die nicht vom gleichen Typ sind (z. B. Liniensegmente und Bögen).

## Bedienung

Die folgende Beispielskizze enthält eine Reihe von Skizzengrundelementen (Linie, Polylinie, Rechteck, Bogen und Kreis).

![](images/EqualConstraint1.png )

Wähle zwei oder mehr Liniensegmente (z.B. eine Linie und eine Seite des Rechtecks).

![](images/EqualConstraint2.png )

Klicke auf **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [BeschränkungGleich](Sketcher_ConstrainEqual.md)** in der Skizzierer Werkzeugleiste (entweder im Arbeitsbereich Skizzierer oder Part Design Arbeitsbereich) oder wähle den BeschränkungGleich Menüeintrag vom Untermenü des Skizzierer oder Part Design Menüs abhängig davon, in welchem Arbeitsbereich du arbeitest (Skizzierer oder Part Design), um die Bedingung auf die gewählten Objekte anzuwenden.

![](images/EqualConstraint3.png )

Wähle nun den Bogen und den Kreis in der Skizze.

![](images/EqualConstraint4.png )

und wende **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [BeschränkungGleich](Sketcher_ConstrainEqual/de.md)** wie vorher an.

![](images/EqualConstraint5.png )

Wähle nun das Liniensegment, alle Segmente der Polylinie sowie eine der unbeschränkten Seiten des Rechtecks.

![](images/EqualConstraint6.png )

und wende **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [BeschränkungGleich](Sketcher_ConstrainEqual/de.md)** wie vorher an.

![](images/EqualConstraint7.png )

Wähle das Liniensegment und den Bogen

![](images/EqualConstraint8.png )

und wende **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [BeschränkungGleich](Sketcher_ConstrainEqual/de.md)** wie zuvor an. Eine Ausklappmeldung zeigt an, dass die beschränkten Elemente vom gleichen geometrischen Typ sein müssen (Linien mit Krümmung Null oder Linien mit Krümmung ungleich Null).

![](images/EqualConstraint9.png )

## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

Die [Skizzierer Skripten](Sketcher_scripting/de.md)-Seite erklärt die Werte, die für `Edge1` und `Edge2` verwendet werden können und enthält weitere Beispiele, wie man Beschränkungen aus Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/de
