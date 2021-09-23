---
- GuiCommand:/it
   Name:Arch Equipment
   Name/it:Arredo
   MenuLocation:Arch → Arredo
   Workbenches:[Arch](Arch_Workbench/it.md)
   Shortcut:**E** **Q**
   SeeAlso:[3 viste da mesh](Arch_3Views/it.md)
---

# Arch Equipment/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Arredo offre un modo semplice e comodo per inserire nei progetti degli elementi autonomi non strutturali come ad esempio i mobili, le attrezzature idrosanitarie o gli apparecchi elettrici. Gli Arredi sono basati su [forme Part](Part_Workbench/it.md), che permettono loro di beneficiare della solidità e delle possibilità delle geometrie BRep, e che generano una bella vista durante il rendering dei piani e viste in sezione.


</div>

![](images/Arch_equipment_example.jpg ) *Oggetti di arredamento racchiusi in un oggetto [Arredo](Arch_Equipment/it.md). Le proiezioni piatte possono essere ottenute dallo strumento [Vista 2D di Draft](Draft_Shape2DView/it.md)*


<div class="mw-translate-fuzzy">

A partire dalla versione 0.17, gli oggetti arredo hanno anche una proprietà **HiRes** in cui può essere collegato un oggetto [Mesh](Mesh_Workbench/it.md). Quindi gli oggetti arredo possono essere creati in modo che nella vista 3D sia visualizzata tale mesh invece che la loro forma, e questo permette di utilizzare qualsiasi oggetto mesh ad alta risoluzione, ad esempio i mobili dettagliati che si trovano comunemente sui siti web.


</div>

![](images/Arch_equipment_mesh.jpg ) *Oggetti di arredamento racchiusi in un oggetto [Arredo](Arch_Equipment/it.md), con allegata una mesh ad alta risoluzione*

Quando si utilizza l\'esportatore OBJ di Arch, tutti gli oggetti arredo che si trovano in modalità di visualizzazione Mesh vengono esportati come loro mesh, invece della loro forma.

## Utilizzo

1.  Selezionare una forma [Part](Part_Workbench/it.md) e, opzionalmente, un oggetto [Mesh](Mesh_Workbench/it.md).
2.  Premere il pulsante **<img src="images/Arch_Equipment.svg" width=16px> [Arredo](Arch_Equipment/it.md)**, o premere i tasti **E** poi **Q**.

## Opzioni

-   Gli elementi Arredo condividono le proprietà e i comportamenti comuni di tutti i [Componenti Arch](Arch_Component/it.md)

## Proprietà

-    {{PropertyData/it|Model}}: Una descrizione del modello di questo arredo.

-    {{PropertyData/it|Url}}: Un URL della pagina del prodotto dove si possono trovare maggiori informazioni su questo arredo.

-    {{PropertyData/it|Mesh}}: Una rappresentazione [Mesh](Mesh_Workbench/it.md) da utilizzare per questo arredo. Quando è impostata, diventa disponibile la modalità di visualizzazione **Mesh**.

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Arredo può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione: 
```python
Equipment = makeEquipment(baseobj=None, placement=None, name="Equipment")
```

-   Crea un oggetto `Equipment` dal `baseobj` dato, che può essere una `Part` o una `Mesh`.
-   Se viene dato un `placement`, esso viene utilizzato.
-   Restituisce `None` se l\'operazione fallisce.

Esempio: 
```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 500
Box.Width = 2000
Box.Height = 600

Equip = Arch.makeEquipment(Box)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Equipment/it
