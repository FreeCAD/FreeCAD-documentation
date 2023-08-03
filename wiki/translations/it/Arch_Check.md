---
 GuiCommand:
   Name: Arch Check
   Name/it: Controlla
   Workbenches: Arch_Workbench/it
   MenuLocation: Arch , Utilità , Controlla
   SeeAlso: Arch CloseHoles/it
---

# Arch Check/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento controlla il documento corrente o gli oggetti selezionati alla ricerca di oggetti <img alt="" src=images/_Workbench_Part.svg  style="width:16px;"> [Parte](Part_Workbench/it.md) o <img alt="" src=images/_Workbench_Arch.svg  style="width:16px;"> [Architettura](Arch_Workbench/it.md) non-solidi, che potrebbero dare problemi, poiché la maggior parte delle operazioni del modulo Architettura richiedono oggetti solidi.


</div>



## Utilizzo

1.  Premere il pulsante **<img src="images/Arch_Check.svg" width=16px> [Controlla](Arch_Check/it.md)**, o **Arch** → **Utilità** → **<img src="images/Arch_Check.svg" width=16px> [Controlla](Arch_Check/it.md)** nel menu principale.




<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Lo strumento può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
list_bad = check(objectslist, includehidden=False)
```

-   Controlla se gli oggetti dati in `objectslist` contengono solo solidi.
-   Se `includehidden` è `True` include tutti gli oggetti nascosti, altrimenti li esclude dalla ricerca.
-   Restituisce una `list_bad`, una lista con gli oggetti che non sono derivati da una `Part::Feature`, o componenti che non sono chiusi, non validi, non contengono solidi o che contengono facce che non fanno parte di alcun solido. Questo è usato per rilevare contorni e profili di [Arch](Arch_Workbench/it.md) o [Draft](Draft_Workbench/it.md) che non sono solidi.
    -   Ogni elemento in `list_bad` è un\'altra lista `[object, message]`, dove `object` è l\'oggetto rilevato non solido, e `message` indica il motivo per cui è stato incluso in questo elenco.

Esempio:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
FreeCAD.ActiveDocument.recompute()

Circle = Draft.makeCircle(450)
Wire = Draft.makeWire([FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(1500, 1000, 0), FreeCAD.Vector(2500, -1000, 0)])

list_bad = Arch.check([Wall1, Wall2, Circle, Wire], includehidden=True)
print(list_bad)
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Check/it
