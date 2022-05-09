# Macro ForceRecompute/it
<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Ricalcola
|Translate=Macro Force Recompute
|Icon=Force_Recompute.png
|Description=Forza il ricalcolo manuale del modello
|Author=shoogen
|Version=1.0
|Date=2014-09-01
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/8/88/Force_Recompute.png ToolBar Icon]
}}


</div>


<div class="mw-translate-fuzzy">

## Descrizione

A volte in FreeCAD l\'utente applica delle modifiche al modello, ma FreeCAD sembra non riconoscerle e l\'icona blu <img alt="" src=images/View-refresh.svg  style="width   *16px;"> rimane grigia. Questa piccola macro impone un ricalcolo manuale del modello.


</div>

Sometimes when a user applies changes to the model, FreeCAD does not seem to recognize/integrate them. In addition to that, the blue **<img src="images/Std_Refresh.svg" width=24px> [Refresh/Recompute](Std_Refresh.md)** button remains greyed out. Hence this small macro was designed to force a manual recompute of the model.


<div class="mw-translate-fuzzy">

Da FreeCAD v0.17, l\'azione di questa macro può essere ottenuta tramite GUI. Nella vista a albero del modello, fare clic destro sul progetto e scegliere \"Marca da ricalcolare\" dal menu contestuale. Dopo di che, premere il pulsante [Ricalcola](Std_Refresh/it.md).


</div>


<div class="mw-translate-fuzzy">

## Uso

Avviare la macro quando serve.


</div>

Run the macro when necessary.

## Script

ToolBar Icon <img alt="" src=images/Force_Recompute.png  style="width   *24px;">

**Macro Force\_Recompute.py**


{{MacroCode|code=
# -*- coding   * utf-8 -*-
# Force Recompute
# macro provided by shoogen

import FreeCAD
for obj in FreeCAD.ActiveDocument.Objects   *
 obj.touch()
FreeCAD.ActiveDocument.recompute()

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro ForceRecompute/it
