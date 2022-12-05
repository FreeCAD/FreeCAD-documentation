---
- GuiCommand:/de
   Name:Std LinkSelectLinkedFinal
   Name/de:Std ZumLetztenVerknüpftenObjektGehen
   MenuLocation:''None''
   Workbenches:All
   Version:0.19
   SeeAlso:[Std ZumVerknüpftenObjektGehen](Std_LinkSelectLinked/de.md), [Std LinkSelectAllLinks](Std_LinkSelectAllLinks/de.md), [Std SelBack](Std_SelBack/de.md), [Std SelForward](Std_SelForward/de.md)
---

# Std LinkSelectLinkedFinal/de

## Beschreibung

Der Befehl **Std ZumLetztenVerknüpftenObjektGehen** wählt die {{PropertyData/de|Linked Object}}, das Quellobjekt eines [App-Link](App_Link/de.md)-Objekts, eine Verknüpfung. Wenn aber das Quellobjekt auch eine Verknüpfung ist, wird sein verlinktes Objekt an seiner Stelle ausgewählt. Dies wiederholt sich, bis das verlinkte Objekt keine Verknüpfung ist. Dieses letzte Quellobjekt ist das am tiefsten verknüpfte Objekt.

## Anwendung

1.  Ein Link-Objekt auswählen.
2.  Den Menüeintrag **Link actions → <img src="images/_Std_LinkSelectLinkedFinal.svg_" width=16px> Zum letzten verlinkten Objekt gehen** aus dem Kontextmenü der [Baumansicht](Tree_view/de.md) auswählen.
3.  Das verknüpfte Objekt ist ausgewählt. Wenn dieses Objekt zu einem externen Dokument gehört, ist jenes jetzt aktiviert.
4.  Optional kann die Schaltfläche **<img src="images/Std_SelBack.svg" width=16px> [Std SelBack](Std_SelBack/de.md)** benutzt werden, um erneut das Link-Objekt auszuwählen.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std LinkSelectLinkedFinal/de
