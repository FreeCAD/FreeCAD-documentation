---
- GuiCommand:/it
   Name:Draft Circle
   Name/it:Cerchio
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Cerchio   Shortcut:**C** **I**
   SeeAlso:[Arco](Draft_Arc/it.md), [Ellisse](Draft_Ellipse/it.md)<br/>[Macro CirclePlus](Macro_CirclePlus/it.md)
---

# Draft Circle/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Crea un cerchio nel [piano di lavoro](Draft_SelectPlane/it.md). Si può definire il cerchio inserendo due punti, il centro, il raggio, oppure selezionando le tangenti, oppure con qualsiasi combinazione di questi elementi. Il cerchio assume [il tipo di linea e il colore](Draft_Linestyle/it.md) impostati in precedenza nella [barra di Draft](Draft_Tray/it.md).


</div>


<div class="mw-translate-fuzzy">

Questo strumento funziona allo stesso modo dello strumento [Arco](Draft_Arc/it.md), tranne per il fatto che crea una circonferenza completa. Per disegnare un\'ellisse usare [Ellisse](Draft_Ellipse/it.md).


</div>

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Cerchio definito da due punti*


</div>

## Utilizzo

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_Circle.svg" width=16px> [Cerchio](Draft_Circle/it.md)
**, o premere i tasti **C** e **I**
2.  Selezionare un primo punto nella vista 3D per stabilire il centro, oppure digitare le sue coordinate e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto
**
3.  Selezionare un secondo punto nella vista 3D, o introdurre il valore del raggio.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opzioni

-   L\'uso principale dello strumento cerchio è selezionando due punti, il centro e un punto sulla circonferenza.
    -   Premendo **Alt**, si può selezionare una tangente invece di selezionare un punto. È quindi possibile costruire diversi tipi di cerchi selezionando una, due o tre tangenti.
-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** per ciascun componente X, Y e Z. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando si hanno i valori desiderati per inserire il punto.
-   Premere il tasto **T** oppure fare clic sulla casella di controllo per attivare la modalità \"continua\". Se la modalità continua è attiva, lo strumento Cerchio si riavvia dopo aver terminato il cerchio in costruzione, e consente di disegnare un nuovo cerchio senza premere nuovamente il pulsante dello strumento.
-   Premere il tasto **L** oppure fare clic sulla casella di controllo per attivare la modalità *riempito*. Se la modalità di riempimento è attiva, il cerchio crea una faccia piena (**Make Face** `True`); in caso contrario, il cerchio non crea una faccia (**Make Face** `False`).
-   Tenere premuto **Ctrl** mentre si disegna per forzare [l\'aggancio](Draft_Snap.md) del proprio punto alla posizione di aggancio più vicina, indipendentemente dalla distanza.
-   Tenere premuto **Maiusc** mentre si disegna per [vincolare](Draft_Constrain.md) il prossimo punto in orizzontale o in verticale rispetto all\'ultimo.
-   Premere il tasto **Esc** o il pulsante {{button|Chiudi}} per interrompere il comando corrente.


</div>

## Notes


<div class="mw-translate-fuzzy">

Il cerchio può essere modificato facendo doppio clic sull\'elemento nella vista ad albero o premendo il pulsante **<img src="images/Draft_Edit.svg" width=16px> [Modifica](Draft_Edit/it.md)**. Quindi si può spostare il il centro e il raggio in una nuova posizione.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and radii: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Circle object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Dati

-    **First Angle**: specifica l\'angolo iniziale del cerchio; normalmente 0°.

-    **Last Angle**: specifica l\'angolo finale del cerchio; normalmente 0°.

-    **Radius**: specifica il raggio del cerchio.

-    **Make Face**: specifica se il Cerchio crea una faccia o no. Se è `True` viene creata una faccia, altrimenti solo la circonferenza è considerata parte dell\'oggetto. Questa proprietà funziona solo se la forma è una circonferenza completa.

:   Per essere un cerchio completo **First Angle** e **Last Angle** devono avere lo stesso valore; altrimenti, viene visualizzato un [Arco](Draft_Arc/it.md). I valori 0° e 360° non sono considerati uguali, quindi se si utilizzano questi due valori, il cerchio non forma una faccia.


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Vista

-    **Pattern**: specifica un tipo di [Campitura](Draft_Pattern/it.md) con cui riempire la faccia del cerchio. Questa proprietà funziona solo se **Make Face** è `True`, e se **Display Mode** è \"Flat Lines\".

-    **Pattern Size**: specifica la dimensione della [Campitura](Draft_Pattern/it.md).


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Cerchio può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
circle = make_circle(radius, placement=None, face=None, startangle=None, endangle=None, support=None)
circle = make_circle(Part.Edge, placement=None, face=None, startangle=None, endangle=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `Circle` dal dato `radius` in millimetri.
    -   
        `radius`
        
        può anche essere un `Part.Edge`, di cui l\'attributo `Curve` deve essere un `Part.Circle`.
-   Se viene dato un `placement` esso viene usato; altrimenti la forma viene creata all\'origine.
-   Se `face` è `True` e il cerchio è chiuso, diventa una faccia e appare riempita.
-   Se `startangle` e `endangle` sono dati in gradi e hanno valori diversi, sono usati e l\'oggetto appare come un [Arco](Draft_Arc/it.md).


</div>

Esempio: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle1 = Draft.make_circle(200)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(1000, 1000, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 0))
circle2 = Draft.make_circle(500, placement=place2)

p3 = App.Vector(-1000, -1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 0))
circle3 = Draft.make_circle(750, placement=place3)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Circle/it
