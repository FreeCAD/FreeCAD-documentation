---
 GuiCommand:
   Name: Arch Fence
   Name/it: Recinzione
   MenuLocation: Arch , Recinzione
   Workbenches: Arch_Workbench/it
   Version: 0.19
---

# Arch Fence/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

[Recinzione](Arch_Fence/it.md) è un oggetto che costruisce una recinzione ripetendo un piantone e una campata della recinzione lungo un determinato percorso.


</div>

<img alt="" src=images/Arch_Fence_description_example.png  style="width:600px;">



## Utilizzo



### Creare dall\'inizio 


<div class="mw-translate-fuzzy">

1.  Usare un ambiente a scelta per creare un piantone e una campata.
2.  Creare il percorso della recinzione usando [Sketcher](Sketcher_Workbench/it.md) o [Draft](Draft_Workbench/it.md).
3.  Passare nell\'ambiente [Arch](Arch_Workbench/it.md).
4.  Selezionare la campata, il piantone e il percorso esattamente nell\'ordine indicato.
5.  Premere il pulsante **<img src="images/Arch_Fence.svg" width=16px> [Recinzione](Arch_Fence/it.md)**.


</div>



## Opzioni

Per ora lo strumento assume quanto segue.

1.  Il percorso è disegnato sul piano XY.
2.  La campata e il piantone sono disegnati nell\'origine in modo che siano in posizione verticale nella vista frontale.



## Proprietà



### Dati

-    **Path**: il percorso che la recinzione deve seguire

-    **Post**: un singolo piantone della recinzione da ripetere

-    **Section**: una singola campata da ripetere

-    **Number Of Posts**: il numero totale dei piantoni utilizzati per costruire la recinzione. Questo è calcolato automaticamente.

-    **Number Of Sections**: il numero totale di campate utilizzate per costruire la recinzione. Questo è calcolato automaticamente.



### Vista

-    **Use Original Colors**: Quando impostata su `True` la recinzione utilizza i colori della sezione e del piantone originale. Altrimenti utilizza il ShapeColor della recinzione.



## Note

-   Arch Fence è stato introdotto in FC v0.19 dall\'utente furti.
-   [Discussione del forum](https://forum.freecadweb.org/viewtopic.php?t=36149) dove si discute della funzionalità di Arch Fence



## Script

Lo strumento Recinzione può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


```python
Fence = buildFence(section, post, path)
```

Esempio:


```python
import FreeCAD
import Part
import Arch

parts = []

parts.append(Part.makeBox(2000, 50, 30, FreeCAD.Vector(0, 0, 1000 - 30)))
parts.append(Part.makeBox(2000, 50, 30))
parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector(0, 15, 30)))
parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector(1980, 15, 30)))

for i in range(8):
    parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector((2000 / 9 * (i + 1)) - 10, 15, 30)))

Part.show(Part.makeCompound(parts), "Fence_section")
fence_section = FreeCAD.ActiveDocument.Fence_section

sketch = FreeCAD.ActiveDocument.addObject("Sketcher::SketchObject", "Path")
sketch.Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(0, 0, 0, 1))
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(20000, 0, 0)), False)
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(20000, 0, 0), FreeCAD.Vector(20000, 20000, 0)), False)

post = Part.makeBox(100, 100, 1000, FreeCAD.Vector(0, 0, 0))
Part.show(post, "Post")
post = FreeCAD.ActiveDocument.Post

Fence = Arch.buildFence(fence_section, post, sketch)
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Arch Fence/it
