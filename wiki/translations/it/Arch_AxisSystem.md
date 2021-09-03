---
- GuiCommand:/it
   Name:Arch AxisSystem
   Name/it:Sistema di assi
   Icon:Arch Axis System.svg
   MenuLocation:Arch → Sistema di assi
   Workbenches:[Arch](Arch_Workbench/it.md)
   SeeAlso:[Assi](Arch_Axis/it.md), [Griglia](Arch_Grid/it.md)
---


</div>

## Descrizione

Lo strumento Sistema di assi consente di combinare 2 o 3 oggetti [Assi](Arch_Axis/it.md).

Questo è utile per definire i punti di intersezione tra i diversi assi. Gli oggetti Arch possono quindi utilizzare questo sistema per duplicare la loro forma sui diversi punti di intersezione.

<img alt="" src=images/Arch_AxisSystem_example.jpg  style="width:600px;"> 
*Tre oggetti [Assi](Arch_Axis/it.md) combinati in un unico [Sistema di assi](Arch_AxisSystem/it.md). Un oggetto [Struttura](Arch_Structure/it.md) usa questo sistema come sua proprietà **Axis*, per duplicare la sua forma in ogni punto di intersezione.**

## Utilizzo

1.  Facoltativamente, selezionare gli oggetti [Assi](Arch_Axis/it.md) che si desidera includere in questo sistema.
2.  Premere il pulsante **<img src="images/Arch_Axis_System.svg" width=16px> [Sistema di assi](Arch_AxisSystem/it.md)**.
3.  Fare clic con il tasto destro del mouse sull\'oggetto Sistema di assi appena creato nella vista ad albero per aggiungere o modificare gli oggetti [Assi](Arch_Axis/it.md) incluso in questo sistema.
4.  Selezionare qualsiasi [Asse](Arch_Axis/it.md) esistente e premere i pulsanti **<img src="images/Arch_Add.svg" width=16px> [Aggiungi](Arch_Add/it.md)** o **<img src="images/Arch_Remove.svg" width=16px> [Rimuovi](Arch_Remove/it.md)** per aggiungerlo o rimuoverlo dal sistema.
5.  Impostare le proprietà **Axis** per fare in modo che un oggetto Arch punti a questo sistema, e la sua forma venga duplicata nei punti di intersezione di questo sistema

## Opzioni

-   Uno stesso oggetto [Asse](Arch_Axis/it.md) può essere parte di più di un sistema
-   Qualsiasi oggetto basato su una forma può anche essere usato come proprietà **Asse** di oggetti Arch. In questo caso, la forma dell\'oggetto viene duplicata lungo i vertici dell\'oggetto Axis

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Sistema di assi può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione: 
```python
AxisSystem = makeAxisSystem(axes, name="Axis System")
```

-   Crea un oggetto `AxisSystem` da un dato `axes`, che è un singolo [Asse](Arch_Axis/it.md), o un elenco di assi.

Esempio: 
```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()

AxisSystem = Arch.makeAxisSystem([Axes, Axes2])

Structure = Arch.makeStructure(length=200, width=200, height=100)
Draft.move(Structure, FreeCAD.Vector(-100, 0, 0))
Structure.Axis = AxisSystem
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
