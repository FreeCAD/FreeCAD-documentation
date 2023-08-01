---
- GuiCommand:
   Name:Std LinkSelectLinkedFinal
   Name/it:
   MenuLocation:''None''
   Workbenches:All
   Version:0.19
   SeeAlso:[Std LinkSelectLinked](Std_LinkSelectLinked/it.md), [Std LinkSelectAllLinks](Std_LinkSelectAllLinks/it.md), [Std SelBack](Std_SelBack/it.md), [Std SelForward](Std_SelForward/it.md)
---

# Std LinkSelectLinkedFinal/it

## Descrizione

The **Std LinkSelectLinkedFinal** command selects the **Linked Object**, the source object, of an [App Link](App_Link.md) object, a link. But if that source object is also a link its linked object is selected instead. This is repeated until the linked object is not a link. This final source object is the deepest linked object.

## Utilizzo

1.  Select a link.
2.  Select the **Link actions → <img src="images/Std_LinkSelectLinkedFinal.svg" width=16px> Go to deepest linked object** option from the [Tree view](Tree_view.md) context menu.
3.  The deepest linked object is selected. If this object belongs to an external document that document is activated.
4.  Optionally use **<img src="images/Std_SelBack.svg" width=16px> [Std SelBack](Std_SelBack.md)** to reselect the link.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std LinkSelectLinkedFinal/it
