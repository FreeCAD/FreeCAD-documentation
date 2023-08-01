---
- GuiCommand:
   Name:Arch Building
   Name/it:Edificio
   MenuLocation:Arch - Edificio
   Workbenches:[Architettura](Arch_Workbench/it.md)
   Shortcut:**B** **U**
   SeeAlso:[Parte di edificio](Arch_BuildingPart/it.md), [Sito](Arch_Site/it.md)
---

# Arch Building/it



## Descrizione

L\'Edificio di Arch è un gruppo speciale di oggetti di FreeCAD particolarmente adatto per rappresentare un edificio completo. Viene prevalentemente utilizzato per organizzare gli oggetti [Piano](Arch_Floor/it.md) nel modello che li contiene.



## Utilizzo

1.  Selezionare uno o più oggetti da includere nel nuovo edificio.
2.  Premere il pulsante **<img src="images/Arch_Building.svg" width=16px> Edificio**, oppure premere i tasti **B** e **U**.



## Opzioni

-   A partire dalla versione 0.18 di FreeCAD, l\'oggetto Edificio è in realtà una [Parte di edificio](Arch_BuildingPart/it.md) con la proprietà **IFC Type** impostata su \"Building\". È possibile convertire qualsiasi BuildingPart, Parte di edificio, in un edificio semplicemente modificando il suo tipo IFC.
-   Dopo aver creato un edificio, è possibile aggiungere ad esso altri oggetti con il drag-and-drop nella struttura ad albero o utilizzando lo strumento **<img src="images/Arch_Add.svg" width=16px> [Aggiungi](Arch_Add/it.md)**.
-   È possibile rimuovere gli oggetti da un edificio trascinandoli fuori con il drag-and-drop nella vista ad albero o utilizzando lo strumento **<img src="images/Arch_Remove.svg" width=16px> [Rimuovi](Arch_Remove/it.md)**.



## Proprietà

-    **Building Type**: Il tipo di edificio, da scegliere da una lista

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Edificio può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione: 
```python
Building = makeBuilding(objectslist=None, baseobj=None, name="Building")
```

-   Crea un oggetto `Building` da una `objectslist`, che è una lista di oggetti, o da un `baseobj`, che è una `Shape`.

Esempio:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

Building = Arch.makeBuilding([Wall1, Wall2])

Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Building/it
