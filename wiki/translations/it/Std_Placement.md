---
- GuiCommand:/it
   Name:Std_Placement
   Name/it:Posizionamento
   MenuLocation:Modifica → Posizionamento...
   Workbenches:Tutti
   SeeAlso:[Allinea](Std_Alignment/it.md), [Posizionamento](Placement/it.md)
---

# Std Placement/it



## Descrizione

Il comando **Posizionamento** visualizza la [scheda azioni](Task_panel/it.md) per il posizionamento di un oggetto selezionato.

![](images/Std_Placement_taskpanel.png ) 
*La scheda di Posizionamento*



## Utilizzo

1.  Seleziona un singolo oggetto che ha una proprietà **Placement** nell\'[editor di proprietà](Property_editor/it.md).
2.  Selezionare l\'opzione **Modifica → Posizionamento...** dal menu.
3.  Modificare uno o più parametri di traslazione e rotazione.
4.  Effettuare una delle seguenti operazioni:
    -   Premere il pulsante **OK** per applicare le modifiche e chiudere il pannello delle azioni.
    -   Premere il pulsante **Applica** per applicare le modifiche, ma tenere aperto il pannello delle azioni per ulteriori modifiche.
5.  Premere **Esc** o il pulsante **Cancel** per interrompere l\'operazione. Questo annullerà tutte le modifiche che non sono state applicate.

La finestra di dialogo può essere avviata anche facendo clic sul pulsante con i puntini di sospensione **...** che appare nell\'[editor di proprietà](Property_editor/it.md) quando si fa clic sulla proprietà **Placement**.



## Note

-   Per ulteriori informazioni sui parametri di posizionamento, vedere la pagina [Posizionamento](Placement/it.md) e il tutorial [Aereo](Aeroplane/it.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Vedere il [tutorial di script Python](Python_scripting_tutorial/it#Vettori_e_posizionamenti.md).

Un posizionamento è definito internamente da una matrice; in molti casi è più semplice rappresentarlo mediante due componenti, un punto `Base` (vettore), e un valore `Rotazione`. Lo stesso `Rotazione` ha diverse rappresentazioni; può essere interamente definito dal valore di un \"[quaternione](https://en.wikipedia.org/wiki/Quaternion)\" `(xi + yj + zk + w)`, ma può anche essere descritto da una rotazione `Axis` (vettore unità) e da una rotazione `Angle` (radianti).


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

Sposta il punto base dell\'oggetto, quindi ruota l\'oggetto di 45 gradi attorno all\'asse X. 
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





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Placement/it
