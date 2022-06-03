---
- GuiCommand   */it
   Name   *Draft_Scale
   Name/it   *Scala
   Workbenches   *[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation   *Draft → Scala
   Shortcut   ***S** **C**
   SeeAlso   *[Clona](Draft_Clone/it.md), [Offset](Draft_Offset/it.md)
---

# Draft Scale/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_Scale.svg  style="width   *16px;"> Scala ridimensiona o copia gli oggetti selezionati attorno a un punto base.


</div>


<div class="mw-translate-fuzzy">

Questo strumento può essere utilizzato su forme 2D create con <img alt="" src=images/Workbench_Draft.svg  style="width   *16px;"> [Draft](Draft_Workbench/it.md) ma può anche essere utilizzato su molti tipi di oggetti 3D come quelli creati con <img alt="" src=images/Workbench_Part.svg  style="width   *16px;"> [Part](Part_Workbench/it.md) o <img alt="" src=images/Workbench_PartDesign.svg  style="width   *16px;"> [PartDesign](PartDesign_Workbench/it.md).


</div>

<img alt="" src=images/Draft_Scale_example.png  style="width   *400px;">


<div class="mw-translate-fuzzy">



*Ridimensionamento di un oggetto da un punto di riferimento a un secondo punto*


</div>

## Utilizzo

See also   * [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Selezionare gli oggetti che si desidera scalare
2.  Premere il pulsante **<img src="images/Draft_Scale.svg" width=16px> [Scala](Draft_Scale/it.md)**, o premere i tasti **S** quindi **C**. Se nessun oggetto è selezionato, si viene invitati a selezionarne uno.
3.  Fare clic su un primo punto nella vista 3D o digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> aggiungi punto**. Questo serve come punto base dell\'operazione.
4.  Impostare i fattori X, Y e Z e le opzioni appropriate, quindi premere **Invio** o **OK** per completare l\'operazione.


</div>

## Opzioni

### First task panel 

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   To manually enter the coordinates for the base point enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   The other checkboxes in this task panel, displayed in FreeCAD version 0.19 and earlier, are ignored by the command.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press the **Close** button to abort the command.

### Second task panel 


<div class="mw-translate-fuzzy">

-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** tra ciascun componente X, Y e Z. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> aggiungi punto** quando si hanno i valori desiderati per inserire il punto.
-   Inserire i fattori X, Y e Z per definire il ridimensionamento lungo tali direzione.
    -   Fare clic sulla casella di controllo \"Scalatura uniforme\" per bloccare i fattori X, Y e Z sullo stesso valore.
    -   Fare clic sulla casella di controllo \"Orientamento del piano di lavoro\" per bloccare il ridimensionamento X, Y e Z lungo il corrente [piano di lavoro](Draft_SelectPlane/it.md); altrimenti, vengono utilizzate le direzioni globali X, Y e Z.
-   Tre opzioni controllano il risultato dell\'operazione di ridimensionamento   *
    -   Crea un clone. Viene creato un [Clone](Draft_Clone/it.md) dell\'oggetto originale. Questo funziona per tutti i tipi di oggetto.

   *   ***Nota   *** anche se i fattori di scala vengono lasciati ai valori predefiniti (1.0, 1.0, 1.0), un clone può essere modificato manualmente editando i fattori nell\'[editor delle proprietà](property_editor/it.md).

   ** Modifica l\'originale. Modifica le dimensioni dell\'oggetto originale. Funziona solo con oggetti Draft e forme di Part non parametriche.

   ** Crea una copia. Viene creata una copia ridimensionata dell\'oggetto originale. Questo funziona per tutti i tipi di oggetto, ma solo le copie degli oggetti Draft sono parametriche.

   *   

       *   
        **Nota   ***
        
        una copia è un oggetto completamente diverso, indipendente dalla forma originale; viene creato nella scala specificata e quindi ha il proprio set di proprietà. Invece, un [Clone](Draft_Clone/it.md) è collegato alla forma originale e l\'unica proprietà che può essere modificata è la scala.


</div>

## Notes

-   The command can also scale [Image Planes](Image_CreateImagePlane.md), but not in clone mode.

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of scale factors (<small>(v0.20)</small> ) and coordinates   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the number of decimals used for the input of scale factors ({{VersionMinus|0.19}})   * **Edit → Preferences... → Draft → General settings → General Draft Settings → Internal precision level**.
-   To reselect the base objects after copying objects   * **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying**.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche   ***

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Scala può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione   *


</div>


```python
scaled_list = scale(objectslist, scale=Vector(1,1,1), center=Vector(0,0,0), copy=False)
```


<div class="mw-translate-fuzzy">

-   Scala gli oggetti della `objectslist` con i fattori specificati dai componenti di `delta`, definiti come un `FreeCAD.Vector`, e usando `center` come punto base.
    -   
        `objectslist`
        
        è un singolo oggetto o un elenco di oggetti.
-   Se `copy` è `True` vengono create delle copie invece di modificare gli oggetti originali.
-   Se `legacy` è `True`, viene utilizzata la modalità copia diretta (obsoleta), altrimenti viene eseguita una copia parametrica.
-   Viene restituita una `scaledlist` con gli oggetti in scala originali o con i nuovi cloni.
    -   
        `scaledlist`
        
        è un singolo oggetto o un elenco di oggetti, a seconda dell\'input `objectslist`.


</div>

Esempio   *


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

pts = [App.Vector(0, 0, 0), App.Vector(500, 500, 0), App.Vector(600, 0, 0)]
wire1 = Draft.make_wire(pts, closed=True)
doc.recompute()

scale1 = App.Vector(2.3, 0.75, 0)
wire2 = Draft.scale(wire1, scale1, copy=True)
doc.recompute()

scale2 = App.Vector(-2, -1.5, 0)
wires = Draft.scale([wire1, wire2], scale2, copy=True)
doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Scale/it
