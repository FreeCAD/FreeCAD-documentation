# Macro Normal Vector/it
{{Macro/it
|Name=Normal Vector Macro
|Icon=Macro_Normal_Vector.png
|Translate=Vettore normale
|Description=Fornisce un vettore normale alla faccia prescelta
|Author=ulrich1a
|Version=1.0
|Date=2016-09-26
|FCVersion=Tutte versione
|Download=[https://www.freecadweb.org/wiki/images/8/8b/Macro_Normal_Vector.png ToolBar Icon]
}}

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Macro semplice per ottenere l\'output nella console python di un vettore normale alla faccia selezionata in precedenza nella vista 3D.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Uso

-   Selezionare una faccia nella vista 3D.
-   Copiare il codice della Macro nella console python.
-   FreeCAD visualizza le informazioni del vettore normale nella console python.
-   Utilizzare questi valori per impostare la direzione mentre si crea una vista di disegno.


</div>

## Script

ToolBar Icon ![](images/Macro_Normal_Vector.png )

**Macro\_Normal\_Vector.FCMacro**


```python

Gui.Selection.getSelectionEx()[0].SubObjects[0].Faces[0].normalAt(0,0)
```

## Link

[La discossione nel forum, in tedesco](http://forum.freecadweb.org/viewtopic.php?f=13&t=10959)

---
[documentation index](../README.md) > Macro Normal Vector/it
