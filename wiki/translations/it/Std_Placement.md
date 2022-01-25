---
- GuiCommand:/it
   Name:Std_Placement
   Name/it:Posizionamento
   MenuLocation:Modifica → Posizionamento...
   Workbenches:Tutti
   SeeAlso:[Allinea](Std_Alignment/it.md), [Azioni di posizionamento](Tasks_Placement/it.md), [Posizionamento](Placement/it.md)
---

# Std Placement/it


</div>

## Descrizione

Il comando **Posizionamento** visualizza la [scheda azioni](Task_panel/it.md) per il posizionamento di un oggetto selezionato.

![](images/Std_Placement_taskpanel.png ) 
*La scheda di Posizionamento*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un singolo oggetto. L\'oggetto deve avere una [proprietà](Property_editor/it.md) **Placement**.
2.  Selezionare l\'opzione **Modifica → Posizionamento...** dal menu.
3.  Modificare uno o più parametri di traslazione e rotazione.
4.  Effettuare una delle seguenti operazioni:
    -   Premere il pulsante **OK** per applicare le modifiche e chiudere il pannello delle azioni.
    -   Premere il pulsante **Applica** per applicare le modifiche, ma tenere aperto il pannello delle azioni per ulteriori modifiche.


</div>

The dialog can also be launched by clicking on the ellipsis button **...** that appears in the [property editor](Property_editor.md) when you click on the **Placement** property.

## Note


<div class="mw-translate-fuzzy">

-   Il pannello delle azioni di posizionamento viene visualizzato anche quando si seleziona un oggetto, fare clic nel campo **Placement** nell\'[editor delle proprietà](Property_editor/it.md) o nella [vista combinata](Combo_view/it.md), quindi premere il pulsante **...**.
-   Per ulteriori informazioni sui parametri di posizionamento, consultare le pagine [Azioni di posizionamento](Tasks_Placement/it.md) e [Posizionamento](Placement/it.md) e il tutorial [Aeroplano](Aeroplane/it.md).


</div>

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Vedere il [tutorial di script Python](Python_scripting_tutorial/it#Vettori_e_posizionamenti.md).

A placement is internally defined by a matrix; in many cases it is simpler to represent it by means of two components, a `Base` point (vector), and a `Rotation` value. The `Rotation` itself has different representations; it can be entirely defined by the value of a \"[quaternion](https://en.wikipedia.org/wiki/Quaternion)\" `(xi + yj + zk + w)`, but it can also be described by a rotation `Axis` (unit vector) and a rotation `Angle` (radians).


```python
import FreeCAD as App

doc = App.newDocument()
obj = doc.addObject("Part::Cylinder", "Cylinder")

print(obj.Placement)
# Placement [Pos=(0,0,0), Yaw-Pitch-Roll=(0,0,0)]
print(obj.Placement.Base)
# Vector (0.0, 0.0, 0.0)
print(obj.Placement.Rotation)
# Rotation (0.0, 0.0, 0.0, 1.0)

print(obj.Placement.Rotation.Angle)
# 0.0
print(obj.Placement.Rotation.Axis)
# Vector (0.0, 0.0, 1.0)
print(obj.Placement.Rotation.Q)
# (0.0, 0.0, 0.0, 1.0)
```

Move the base point of the object, then rotate the object 45 degrees around the X axis. 
```python
import math

obj.Placement.Base = App.Vector(5, 3, 1)
obj.Placement.Rotation.Axis = App.Vector(1, 0, 0)
obj.Placement.Rotation.Angle = math.radians(45)

print(obj.Placement)
# Placement [Pos=(5,3,1), Yaw-Pitch-Roll=(0,0,45)]
print(obj.Placement.Rotation.Q)
# (0.3826834323650898, 0.0, 0.0, 0.9238795325112867)
print(obj.Placement.Matrix)
# Matrix ((1,0,0,5),(0,0.707107,-0.707107,3),(0,0.707107,0.707107,1),(0,0,0,1))
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Placement/it
