---
- GuiCommand:/it
   Name:Draft Arc 3Points
   Name/it:Arco da tre punti
   MenuLocation:Draft → Arco da tre punti
   Workbenches:[Draft](Draft_Module/it.md), [Arch](Arch_Module/it.md)
   Shortcut:**A** **T**
   SeeAlso:[Arco](Draft_Arc/it.md), [Cerchio](Draft_Circle/it.md), [Ellisse](Draft_Ellipse/it.md)
   Version:0.19
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_Arc_3Points.svg  style="width:16px;"> [Arco da tre punti](Draft_Arc_3Points/it.md) crea un arco circolare nell\'attuale [piano di lavoro](Draft_SelectPlane/it.md) inserendo tre punti che si trovano sulla circonferenza; il centro e il raggio sono determinati da questi tre punti. Usa [il tipo di linea e il colore](Draft_Linestyle/it.md) impostati in precedenza nella [barra di Draft](Draft_Tray/it.md).


</div>

A Draft Arc is in fact a [Draft Circle](Draft_Circle.md) with a **First Angle** that is not the same as its **Last Angle**.

<img alt="" src=images/Draft_Arc_3Points_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">


*Arco definito da tre punti giacenti su una circonferenza*


</div>

## Utilizzo

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_Arc_3Points.svg" width=16px> [Arco da tre punti](Draft_Arc_3Points/it.md)**, o premere i tasti **A** e poi **T**.
2.  Selezionare un primo punto nella vista 3D, oppure digitare le sue [coordinate](Draft_Coordinates/it.md) poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)**.
3.  Selezionare un secondo punto nella vista 3D, oppure digitare le sue [coordinate](Draft_Coordinates/it.md) poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)**.
4.  Selezionare un terzo punto nella vista 3D, oppure digitare le sue [coordinate](Draft_Coordinates/it.md) poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)**.
5.  L\'arco viene creato dopo aver assegnato il terzo punto.


</div>

## Opzioni

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Premere **X**, **Y** o **Z** dopo un punto per vincolare il punto seguente sull\'asse dato.
-   Per inserire le coordinate manualmente, basta inserire i valori, quindi premere **Invio** tra ciascun componente X, Y e Z.
    -   Per inserire il punto è possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)** dopo aver inserito i valori desiderati.
-   Premere **R** oppure fare clic sulla casella di controllo per attivare la modalità *relativo*. Se la modalità relativo è attiva, le coordinate del punto seguente sono relative al punto precedente; in caso contrario, sono assolute, prese dall\'origine `(0, 0, 0)`.
-   Tenere premuto **Maiusc** mentre si disegna per [vincolare](Draft_Constrain/it.md) in orizzontale o in verticale il prossimo punto rispetto al precedente.
-   Premere il pulsante **Esc** o **Chiudi** per interrompere il comando corrente.


</div>

## Notes

-   A Draft Arc can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a non-editable [Part Feature](Part_Feature.md) instead of a Draft Circle.

## Proprietà


<div class="mw-translate-fuzzy">

Un oggetto Arco condivide tutte le proprietà di un [Cerchio](Draft_Circle/it.md), ma alcune proprietà hanno senso solo per il cerchio. Vedere [Arco](Draft_Arc/it.md) per ulteriori informazioni.


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Arco da tre punti può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
arc = make_arc_3points(points, placement=None, face=False, support=None, map_mode="Deactivated", primitive=False)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `arc` da una data lista di `points`.
-   Se viene fornito un `placement`, il centro dell\'arco verrà spostato in questo punto. Per ulteriori informazioni vedere [Posizionamento](Placement/it.md).
-   Se `face` è `True`, l\'arco formerà una faccia, cioè apparirà pieno.
-   Se viene fornito un `support`, esso è un `LinkSubList`, vale a dire un elenco che indica un oggetto e un sottoelemento di quell\'oggetto. Viene utilizzato in modo che l\'oggetto appaia riferito a questo supporto.

:   Per esempio, support=[(obj, ("Face1"))]

-   Se viene fornito un `map_mode`, è una stringa che definisce un tipo di mappatura, ad esempio,map_mode='FlatFace', map_mode='ThreePointsPlane', etc. Per ulteriori informazioni vedere [Part Associazione](Part_Attachment/it.md).
-   Se `primitive` è `True`, l\'arco creato sarà un semplice [Part Feature](Part_Feature/it.md), e non un oggetto Draft complesso.


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

points = [App.Vector(0, 0, 0),
          App.Vector(5, 10, 0),
          App.Vector(10, 0, 0)]

arc = Draft.make_arc_3points(points)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
