---
- GuiCommand:
   Name:Std LinkReplace
   Name/de:Std DurchVerknüpfungErsetzen
   MenuLocation:None
   Workbenches:All
   Version:0.19
   SeeAlso:[Std VerknüpfungErstellen](Std_LinkMake/de.md), [Std UnterverknüpfungErstellen](Std_LinkMakeRelative/de.md), [Std VerknüpfungAuflösen](Std_LinkUnlink/de.md)
---

# Std LinkReplace/de



## Beschreibung


**[<img src=images/Std_LinkReplace.svg style="width:16px"> [Std DurchVerknüpfungErsetzen](Std_LinkReplace/de.md)**

ersetzt ein Objekt, das sich in einem anderen befindet, durch eine [Anwendung Verknüpfung](App_Link/de.md)-Version von diesem Objekt.

Dies wirkt auf das \"Kind\"-Objekt eines \"Eltern\"-Objectes wie in der [Baumansicht](tree_view/de.md) zu sehen. Sind beispielsweise zwei Objekte A und B gegeben, die Teil einer **[<img src=images/Part_Boolean.svg style="width:16px"> [Part BoolescheOperation](Part_Boolean/de.md)** sind, z.B. C = A + B, kann das Objekt A durch eine Verknüpfung ersetzt werden, so daß C = A_link + B wird.

Damit können in einer komplexen Baugruppe eingebettete Objekte durch eine Verknüpfung ersetzt werden. Das ist effizienter, als eingebettete Objekte mehrere Male in unterschiedlichen Unterbaugruppen zu verwenden. Die hierzu entgegengerichtete Funktion ist **[<img src=images/Std_LinkUnlink.svg style="width:16px"> [Std VerknüpfungAuflösen](Std_LinkUnlink/de.md)**. Um eine allgemeine Verknüpfung zu erstellen, siehe **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std VerknüpfungErstellen](Std_LinkMake/de.md)**.



## Anwendung

1.  Wir benötigen ein Ojekt, das sich in einem anderen befindet. Betrachten wir z.B. eine **[<img src=images/Part_Fuse.svg style="width:16px"> [Part Vereinigung](Part_Fuse/de.md)**, die sich in zwei zuvor erstellten Objekten befindet, z.B. einer **[<img src=images/Part_Sphere.svg style="width:16px"> [Part Kugel](Part_Sphere/de.md)** und einem **[<img src=images/Part_Cylinder.svg style="width:16px"> [Part Zylinder](Part_Cylinder/de.md)**.
2.  Wähle <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:16px;"> [Part Kugel](Part_Sphere/de.md) in der [Baumansicht](tree_view/de.md).
3.  Klicke auf die Schaltfläche **[<img src=images/Std_LinkReplace.svg style="width:16px"> [Std DurchVerknüpfungErsetzen](Std_LinkReplace/de.md)**.

Die Original-<img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:16px;"> [Part Kugel](Part_Sphere/de.md) muß sich nun außerhalb von **[<img src=images/Part_Fuse.svg style="width:16px"> [Part Vereinigung](Part_Fuse/de.md)** und innerhalb eine Verknüpfung statt dessen befinden. Im Icon wird ein kleiner überlagernder Pfeil gezeigt.

![](images/Std_Link_tree_replace_fuse_1_example.png ) ![](images/Std_Link_tree_replace_fuse_2_example.png )



*Ein Objekt in einem anderen wird durch eine Verknüpfung ersetzt. Jetzt ist die Verknüpfung innen und das reale Objekt liegt außerhalb.*

Dies ist auch bei Objekten, die {{button|[<img src=images/Std_Part.svg style="width:16px"> [Standard Teile](Std_Part/de.md)}} und {{button|[<img src=images/Std_Group.svg style="width:16px"> [Std Gruppe](Std_Group/de.md)}} enthalten möglich.

![](images/Std_Link_tree_replace_part_1_examples.png ) ![](images/Std_Link_tree_replace_part_2_examples.png )



*Ein Objekt in einem Behälter wird durch eine Verknüpfung ersetzt. Die Verknüpfung liegt nun innerhalb und das reale Objekt liegt außerhalb.*



## Eigenschaften

Diese Anweisung erstellt eine neue [Anwendung Verknüpfung](App_Link/de.md). Seine Eigenschaften sind unter **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std VerknüpfungErstellen](Std_LinkMake/de.md)** beschrieben.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std LinkReplace/de
