---
- GuiCommand:
   Name:Std LinkUnlink
   Name/de:Std VerknüpfungAuflösen
   MenuLocation:None
   Workbenches:All
   Version:0.19
   SeeAlso:[Std VerknüpfungErstellen](Std_LinkMake/de.md), [Std UnterverknüpfungErstellen](Std_LinkMakeRelative/de.md), [Std DurchVerknüpfungErsetzen](Std_LinkReplace/de.md)
---

# Std LinkUnlink/de



## Beschreibung


**[<img src=images/Std_LinkUnlink.svg style="width:16px"> [Std VerknüpfungAuflösen](Std_LinkUnlink/de.md)**

ist im wesentlichen die Umkehrung der Funktion **[<img src=images/Std_LinkReplace.svg style="width:16px"> [Std DurchVerknüpfungErsetzen](Std_LinkReplace/de.md)**.

Diese Funktion entfernt eine Verknüpfung aus einem Behälter, wie etwa einem **[<img src=images/Std_Part.svg style="width:16px"> [Standard Teil](Std_Part/de.md)** und fügt statt dessen das reale Objekt ein.



## Anwendung

1.  Wir benötigen einen Behälter mit einer Verknüpfung zum Beispiel auf eine **[<img src=images/Part_Sphere.svg style="width:16px"> [Part Kugel](Part_Sphere/de.md)** innerhalb eines **[<img src=images/Std_Part.svg style="width:16px"> [Standard Teil](Std_Part/de.md)**s.
2.  Wähle eine interne Verknüpfung in der [Baumansicht](tree_view/de.md).
3.  Klicke auf die Schaltfläche **[<img src=images/Std_LinkUnlink.svg style="width:16px"> [Std VerknüpfungAuflösen](Std_LinkUnlink/de.md)**.

Jetzt muß die Original-<img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:16px;"> [Part Kugel](Part_Sphere/de.md) im **[<img src=images/Std_Part.svg style="width:16px"> [Standard Teil](Std_Part/de.md)** sein und die Verknüpfung muß außerhalb liegen. Jetzt kann auch die Verknüpfung gelöscht werden, sofern sie nicht mehr benötigt wird, ohne den Behälter zu kaputt zu machen.

![](images/Std_Link_tree_replace_1_example.png ) ![](images/Std_Link_tree_unlink_1_example.png )



*Eine Verknüpfung innerhalt eines anderen Objektes wird gelöst und das reale Objekt wird anstatt dessen eingefügt.*

![](images/Std_Link_tree_replace_2_example.png ) ![](images/Std_Link_tree_unlink_2_example.png )



*Eine Verknüpfung in einer Gruppe wird gelöst und das reale Objekt wird anstatt dessen eingefügt.*





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std LinkUnlink/de
