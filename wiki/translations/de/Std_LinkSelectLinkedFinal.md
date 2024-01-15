---
 GuiCommand:
   Name: Std LinkSelectLinkedFinal
   Name/de: Std ZumLetztenVerknüpftenObjektGehen
   MenuLocation: Ansicht , Verknüpfungsnavigation , Zum tiefsten verknüpften Objekt gehen
   Workbenches: Alle
   Version: 0.19
   Shortcut: **S** **D**
   SeeAlso: Std_LinkSelectLinked/de, Std_LinkSelectAllLinks/de
---

# Std LinkSelectLinkedFinal/de



## Beschreibung

Der Befehl **Std ZumLetztenVerknüpftenObjektGehen** wählt die {{PropertyData/de|Linked Object}}, das Quellobjekt eines [App-Link](App_Link/de.md)-Objekts, eine Verknüpfung. Wenn aber das Quellobjekt auch eine Verknüpfung ist, wird sein verlinktes Objekt an seiner Stelle ausgewählt. Dies wiederholt sich, bis das verlinkte Objekt keine Verknüpfung ist. Dieses letzte Quellobjekt ist das am tiefsten verknüpfte Objekt.



## Anwendung

1.  Ein Link-Objekt auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Den Menüeintrag **Ansicht → Verknüpfungsnavigation → <img src="images/Std_LinkSelectLinkedFinal.svg" width=16px> Zum tiefsten verknüpften Objekt gehen** auswählen.
    -   Die Menüoption **Verknüpfungen... → <img src="images/Std_LinkSelectLinkedFinal.svg" width=16px> Zum letzten verlinkten Objekt gehen** im Kontextmenü der [Baumansicht](Tree_view/de.md) auswählen.
    -   Das Tastaturkürzel **S** dann **D**.
3.  Das letzte verknüpfte Objekt ist ausgewählt. Wenn dieses Objekt zu einem externen Dokument gehört, ist jenes jetzt aktiviert.
4.  Wahlweise kann **<img src="images/Std_SelBack.svg" width=16px> [Std AuswahlZurück](Std_SelBack/de.md)** benutzt werden, um das Link-Objekt erneut auszuwählen.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std LinkSelectLinkedFinal/de
