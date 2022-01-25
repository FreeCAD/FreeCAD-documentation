---
- GuiCommand:/it
   Name:Draft Mirror
   Name/it:Simmetria
   MenuLocation:Draft → Simmetria
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   SeeAlso:[Draft Scala](Draft_Scale/it.md), [Clone](Draft_Clone/it.md)
---

# Draft Mirror/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_Mirror.svg  style="width:16px;"> Simmetria produce una copia speculare di un oggetto selezionato, usando l\'operazione [Specchia di Part](Part_Mirror/it.md). La copia è collegata all\'oggetto originale, esattamente come un [Clone](Draft_Clone/it.md). Ciò significa che se l\'oggetto originale cambia forma e proprietà, anche la forma specchiata cambia.


</div>


<div class="mw-translate-fuzzy">

Questo strumento può essere utilizzato su forme 2D create con [Draft](Draft_Workbench/it.md) ma può anche essere utilizzato su molti tipi di oggetti 3D come quelli creati con [Part](Part_Workbench/it.md) o [PartDesign](PartDesign_Workbench/it.md) o [Arch](Arch_Workbench/it.md).


</div>

<img alt="" src=images/Draft_Mirror_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Oggetto speculare creato utilizzando una linea di riflessione*


</div>

## Utilizzo

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Selezionare un oggetto che si desidera riflettere
2.  Premere il pulsante **<img src="images/Draft_Mirror.svg" width=16px> [Simmetria](Draft_Mirror/it.md)**. Se nessun oggetto è selezionato, si viene invitati a selezionarne uno.
3.  Fare clic su un primo punto nella vista 3D o digitare una coordinata e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> aggiungi punto**.
4.  Fare clic su un secondo punto nella vista 3D o digitare una coordinata e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> aggiungi punto**. Questi punti definiscono una linea che, insieme alla vista della telecamera, definisce un piano specchiante che viene utilizzato per creare l\'oggetto specchiato.


</div>

## Options

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

## Opzioni

-   Premere **X**, **Y** o **Z** dopo il primo punto per vincolare il secondo punto su un dato asse.
-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** tra ciascun componente X, Y e Z.
-   Premere **R** o fare clic sulla casella di controllo per attivare la modalità \"relativa\". Se la modalità relativa è attiva, le coordinate del secondo punto sono relative alla prima; se no, sono assolute, prese dall\'origine (0,0,0).
-   Premere **T** oppure fare clic sulla casella di controllo per attivare la modalità \"continua\". Se la modalità continua è attiva, lo strumento Simmetria si riavvia dopo aver assegnato il secondo punto, consentendo di inserire un altro oggetto senza premere nuovamente il pulsante dello strumento.
-   Tenere premuto **Ctrl** mentre si disegna per forzare lo [snap](Draft_Snap.md) al punto di aggancio più vicino, indipendentemente dalla distanza.
-   Tenere premuto **Maiusc** mentre si disegna per [vincolare](Draft_Constrain.md) il secondo punto in orizzontale o in verticale rispetto al primo.
-   Premere il pulsante **Esc** o **Chiudi** per interrompere il comando corrente.


</div>

## Notes

-   Mirrored copies of [Draft Lines](Draft_Line.md), [Draft Wires](Draft_Wire.md), [Draft Arcs](Draft_Arc.md) and [Draft Circles](Draft_Circle.md) can be turned into independent editable Draft objects by using [Draft Downgrade](Draft_Downgrade.md) and then [Draft Upgrade](Draft_Upgrade.md).
-   The [Part SimpleCopy](Part_SimpleCopy.md) command can be used to create a copy of a mirrored object that is not linked to its source object.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Properties

See also: [Property editor](property_editor.md).

A [Part Mirror](Part_Mirror.md) object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Base}}

-    **Source|Link**: specifies the object that is mirrored.


{{TitleProperty|Plane}}


<div class="mw-translate-fuzzy">

## Proprietà

-    **Source**: specifica l\'oggetto da rispecchiare,

-    **Base**: specifica il punto base del piano speculare.

-    **Normal**: specifica la direzione normale del piano speculare.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Simmetria può essere usato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
mirrored_list = mirror(objlist, p1, p2)
```


<div class="mw-translate-fuzzy">

-   Crea unoggetto [Simmetria](Part_Mirror/it.md) di Part da una `objlist`, che può essere un singolo oggetto o un elenco di oggetti.
-   Til piano di riflessione è definito dalla linea costruita con i punti `p1` e `p2`, e parallelo alla vista corrente.
-   Viene restituita una `mirrored_list` con i nuovi oggetti.
    -   
        `mirrored_list`
        
        è un singolo oggetto o un elenco di oggetti, a seconda dell\'input di `objlist`.


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

place = App.Placement(FreeCAD.Vector(1000, 0, 0), App.Rotation())
polygon1 = Draft.make_polygon(3, 750)
polygon2 = Draft.make_polygon(5, 750, placement=place)

p1 = App.Vector(2000, -1000, 0)
p2 = App.Vector(2000, 1000, 0)

line1 = Draft.make_line(p1, p2)
mirrored1 = Draft.mirror(polygon1, p1, p2)

Line2 = Draft.make_line(-p1, -p2)
mirrored2 = Draft.mirror([polygon1, polygon2], -p1, -p2)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Mirror/it
