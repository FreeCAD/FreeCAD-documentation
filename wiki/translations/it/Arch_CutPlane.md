---
- GuiCommand:/it
   Name:Arch CutPlane
   Name/it:Taglia con piano
   Workbenches:[[Arch_Workbench/it   Arch]]|MenuLocation:Arch → Taglia con piano
   SeeAlso:[Taglia con una linea](Arch_CutLine/it.md), [Rimuovi](Arch_Remove/it.md)
---


</div>

## Descrizione

Lo strumento Taglia con piano permette di tagliare un oggetto Arch secondo un piano:

-   È possibile tagliare un oggetto di Arch dalla parte normale a una faccia selezionata, o dalla parte opposta del piano.
-   Questo aggiunge un elemento sottrazione CutVolume all\'oggetto Arch.

<img alt="" src=images/Arch_CutPlane_example.jpg  style="width:640px;">


*A sinistra: prima di applicare lo strumento Taglia con piano. Al centro: parete risultante dopo il taglio. A destra: un altro risultato opzionale*

## Utilizzo

1.  Selezionare prima l\'oggetto da tagliare, quindi la faccia (la faccia deve essere l\'ultimo elemento selezionato, e deve essere selezionata nella [vista 3D](3D_View/it.md)).
2.  Premere il pulsante **<img src="images/Arch_CutPlane.svg" width=24px> [Taglia con piano](Arch_CutPlane/it.md)**.
3.  Scegliere se l\'oggetto deve essere tagliato dalla parte normale **posteriore** alla faccia oppure dalla parte normale **anteriore** della faccia
4.  Cliccare sul pulsante **OK**.

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Taglia con Piano può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione: 
```python
cutObj = cutComponentwithPlane(archObject, cutPlane, sideFace)
```

-   Crea un oggetto `cutObj` dal `archObject` dato, che è tagliato dal `cutPlane`, che è la faccia di un altro oggetto.
    -   
        `archObject`
        
        dovrebbe essere un `SelectionObject` ottenuto da `FreeCADGui.Selection.SelectionEx()[0]`.

    -   
        `cutPlane`
        
        dovrebbe essere un `FaceObject` ottenuto da `FreeCADGui.Selection.SelectionEx()[0].SubObjects[0]`.

-    `sideFace`specifica su quale lato del `FaceObject` verrà creato un volume; questo volume verrà quindi utilizzato per sottrarlo dal `archObject`. Se `sideFace` è `0` crea un volume nella parte posteriore della faccia, altrimenti lo crea davanti alla faccia.

Esempio: 
```python
import FreeCAD, FreeCADGui, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select the Wall
main_object = FreeCADGui.Selection.getSelectionEx()[0]

# Select the face of Wall2
selection = FreeCADGui.Selection.getSelectionEx()[0]
cut_face = selection.SubObjects[0]

cutObj = Arch.cutComponentwithPlane(main_object, cut_face, 0)
FreeCAD.ActiveDocument.recompute()

Wall3 = Draft.move(Wall, FreeCAD.Vector(-4000, 0, 0), copy=True)
Wall4 = Draft.move(Wall2, FreeCAD.Vector(-4000, 0, 0), copy=True)
FreeCAD.ActiveDocument.recompute()

# Select the Wall3
main_object2 = FreeCADGui.Selection.getSelectionEx()[0]

# Select the face of Wall4
selection2 = FreeCADGui.Selection.getSelectionEx()[0]
cut_face2 = selection2.SubObjects[0]

cutObj2 = Arch.cutComponentwithPlane(main_object2, cut_face2, 1)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
