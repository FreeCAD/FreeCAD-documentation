---
- GuiCommand:
   Name: Std LinkMakeRelative
   Name/de: Std UnterverknüpfungErstellen
   MenuLocation: Kein
   Workbenches: Alle
   Version: 0.19
   SeeAlso: Std_Part/de, Std_Group/de, Std_LinkMake/de
---

# Std LinkMakeRelative/de



## Beschreibung


**[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Std UnterverknüpfungErstellen](Std_LinkMakeRelative/de.md)**

erstellt ein [App Link](App_Link.md)-Objekt (`App::Link` class), so wie **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std VerknüpfungErstellen](Std_LinkMake/de.md)**, wird aber in erster Linie auf ausgewählte Unterelemente angewendet und setzt die {{PropertyData/de|Link Transform}} auf `True`.



## Anwendung

Mit Auswahl:

1.  Ein Unterelement in der [3D-Ansicht](3D_view/de.md) auswählen, d.h. ein Knoten, eine Kante oder eine Fläche auswählen oder irgendeine Kombination aus diesen. Die Unterelemente müssen zu einem einzigen Objekt gehören.
2.  Die Schaltfläche **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [UnterverknüpfungErstellen](Std_LinkMakeRelative/de.md)** drücken. Das erstellte Objekt besitzt das gleiche Symbol, wie das Originalobjekt, das aber mit zwei Pfeilen überlagert ist, die darauf hinweisen, dass es sich um eine Unterverknüpfung handelt.

Ohne Auswahl:

-   Wenn kein Objekt ausgewählt wurde, macht dieser Befehl nichts.
-   Wenn ein Objekt nur in der [Baumansicht](tree_view/de.md) ausgewählt wurde, aber kein Unterelement in der [3D-Ansicht](3D_view/de.md) ausgewählt wurde, macht dieser Befehl auch nichts.

<img alt="" src=images/Std_Link_tree_sublink_example.png ) ![](images/Std_Link_sublink_example.png  style="width:500px;">



*Originaler Körper und drei Verknüpfungen, die von seinen Unterelementen erstellt wurden, inklusive Kanten und Flächen.*



## Eigenschaften

Diese Anwendung erstellt eine neue [Anwendung Verknüpfung](App_Link/de.md). Seine Eigenschaften sind in **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std VerknüpfungErstellen](Std_LinkMake/de.md)** beschrieben.

Vor allem **Link Transform** ist auf `True` gesetzt. Damit wird **Placement** versteckt und an dessen statt steuert **Link Placement** die Position der Verknüpfung, bezogen auf die Position **Linked Object**.



## Skripten

Zu allgemeinen Informationen, siehe [Std VerknüpfungErstellen](Std_LinkMake/de.md).

Die Anwendung Link wurde mit der `addObject()`-Methode des Dokumentes erstellt. Um eine relative Verknüpfung zu erstellen, wird seine `setLink`-Methode verwendet, um das Quellobjekt und eines oder mehrerer seiner Unterelemente aufzunehmen. Dann wird das `LinkTransform`-Attribut auf `True` gesetzt.


```python
import FreeCAD as App

doc = App.newDocument()
body = App.ActiveDocument.addObject("Part::Box", "Box")

obj = App.ActiveDocument.addObject("App::Link", "Link")
obj.setLink(body, '', ['Edge1', 'Edge6', 'Edge7', 'Edge10', 'Face2', 'Face3'])
obj.LinkTransform = True
obj.LinkPlacement.Base = App.Vector(20, 20, 0)
App.ActiveDocument.recompute()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std LinkMakeRelative/de
