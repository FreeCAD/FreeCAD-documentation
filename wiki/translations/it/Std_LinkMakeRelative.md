---
- GuiCommand:
   Name: Std_LinkMakeRelative
   Name/it: Crea un link relativo
   MenuLocation: Nessuna
   Workbenches: Tutti
   Version: 0.19
   SeeAlso: Std_Part/it, Std_Group/it, Std_LinkMake/it
---

# Std LinkMakeRelative/it

## Descrizione

Lo strumento **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Crea un link relativo](Std_LinkMakeRelative/it.md)** crea un [App Link](App_Link/it.md) (classe `App::Link`), così come fa **[<img src=images/Std_LinkMake.svg style="width:16px"> [Crea un link](Std_LinkMake.md)**, ma opera prima sui sottoelementi selezionati e imposta **Link Transform** su `True`.

## Utilizzo

Con selezione:

1.  Selezionare un sottoelemento nella [vista 3D](3D_view/it.md), ad esempio un vertice, uno spigolo o una faccia o una qualsiasi combinazione di questi. Questi sottoelementi devono appartenere a un singolo oggetto.
2.  Premere il pulsante **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Crea un link relativo](Std_LinkMakeRelative/it.md)**. L\'oggetto prodotto ha la stessa icona dell\'oggetto originale, ma ha due frecce sovrapposte che indicano che è un collegamento relativo.

Senza selezione:

-   Se non è selezionato alcun oggetto, questo comando non fa nulla.
-   Se un oggetto è selezionato solo nella [vista ad albero](tree_view/it.md), ma nella [vista 3D](3D_view/it.md) non è selezionato nessun sottoelemento, questo comando non fa nulla.

<img alt="" src=images/Std_Link_tree_sublink_example.png ) ![](images/Std_Link_sublink_example.png  style="width:500px;">



*Corpo originale e tre collegamenti creati dai suoi elementi secondari, inclusi bordi e facce.*

## Proprietà

Questo comando crea un nuovo [App Link](App_Link/it.md); le sue proprietà sono descritte in <img alt="" src=images/Std_LinkMake.svg  style="width:16px;"> [Crea un link](Std_LinkMake/it.md).

In particolare, **Link Transform** è impostata su `True`, quindi **Placement** viene nascosto e invece **Link Placement** controlla la posizione del Link rispetto alla posizione di **Linked Object**.

## Script

Vedere [Crea link](Std_LinkMake/it.md) per le informazioni generali.

Viene creato un App Link con il metodo `addObject()` del documento. Per definire un collegamento relativo, il suo metodo `setLink` viene utilizzato per selezionare l\'oggetto sorgente e uno o più dei suoi sottoelementi. Quindi l\'attributo `LinkTransform` è impostato su `True`.


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
⏵ [documentation index](../README.md) > Std LinkMakeRelative/it
