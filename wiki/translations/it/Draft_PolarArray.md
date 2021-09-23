---
- GuiCommand:/it
   Name:Draft PolarArray
   Name/it:Serie polare
   MenuLocation:Draft → Serie polare
   Workbenches:[Draft](Draft_Workbench/it.md)
   Version:0.19
   SeeAlso:[Serie](Draft_Array/it.md), [Serie circolare](Draft_CircularArray/it.md), [Serie su tracciato](Draft_PathArray/it.md), [Serie su punti](Draft_PointArray/it.md), [Clone](Draft_Clone/it.md)
---

# Draft PolarArray/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_PolarArray.svg  style="width:16px;"> [Serie polare](Draft_PolarArray/it.md) crea una serie da un oggetto selezionato posizionando le copie lungo una circonferenza.


</div>


<div class="mw-translate-fuzzy">

Questo strumento può essere utilizzato su forme 2D create con [Draft](Draft_Workbench/it.md) ma può anche essere utilizzato su molti tipi di oggetti 3D come quelli creati con [Part](Part_Workbench/it.md) o [PartDesign](PartDesign_Workbench/it.md).


</div>

<img alt="" src=images/Draft_PolarArray_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">


*Una serie polare di un oggetto.*


</div>

## Utilizzo

See also: [Draft Snap](Draft_Snap.md).


<div class="mw-translate-fuzzy">

1.  Selezionare un oggetto da cui si desidera creare la matrice polare.
2.  Premere il pulsante **<img src=images/Draft_PolarArray.svg style="width:16px"> [Serie polare](Draft_PolarArray/it.md)**. Se non viene selezionato alcun oggetto, si aprirà il [pannello azioni](task_panel/it.md), ma è comunque necessario selezionare un oggetto per procedere.
3.  Scegli l\'angolo polare, che determina dove sarà posizionato l\'ultimo elemento della serie.
4.  Scegliere il numero di elementi della serie. Minimo 2, massimo 99.
5.  Scegliere il centro dell\'asse di rotazione. È possibile fare clic nella [vista 3D](3D_view/it.md), per impostare contemporaneamente la posizione del centro di rotazione e completare il comando.
6.  Facoltativamente, attivare le opzioni di fusione o link.
7.  Premere **OK** per completare il comando.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

-   Premere **Reset point** per impostare il centro di rotazione sull\'origine {{Value|(0, 0, 0)}}.
-   Se la casella **Fuse** è spuntata, gli oggetti risultanti nella serie saranno fusi in una singola forma, se si toccano o si intersecano.
-   Se la casella di controllo **Use Links** è selezionata, gli oggetti risultanti nella serie saranno degli [App Links](App_Link/it.md) anziché semplici copie. Ciò migliora l\'utilizzo della memoria della serie, poiché l\'App Link riutilizza la [forma](Shape/it.md) dell\'oggetto originale e non crea nuove forme. Se si utilizza questa opzione, la casella di controllo **Fuse** non ha alcun effetto.
-   Premere **Esc** o il pulsante **Annulla** per interrompere il comando corrente.


</div>

## Notes


<div class="mw-translate-fuzzy">

Note:

-   Per impostazione predefinita, l\'asse di rotazione è l\'asse Z positivo {{Value|(0, 0, 1)}}. Questo può essere modificato nell\'[editor delle proprietà](property_editor/it.md) dopo la creazione dell\'oggetto.
-   L\'angolo polare è positivo in senso antiorario e negativo in senso orario.
-   Ogni elemento della serie è un clone esatto dell\'oggetto originale, ma l\'intera serie è considerata una singola unità in termini di proprietà e aspetto.
-   Questo comando crea lo stesso oggetto di quello creato con gli strumenti [Serie](Draft_Array/it.md) e [Serie circolare](Draft_CircularArray/it.md). Pertanto, la serie può essere convertita in ortogonale, polare o circolare semplicemente modificandone le proprietà.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Proprietà


<div class="mw-translate-fuzzy">

Vedere lo strumento **<img src="images/Draft_Array.svg" width=16px> [Serie ortogonale](Draft_OrthoArray/it.md)** per l\'informazione completa.


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>

### Parametric array 


<div class="mw-translate-fuzzy">

Lo strumento Serie può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>

The main method:


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

The wrapper for polar arrays is:


```python
array = make_polar_array(base_object,
                         number=5, angle=360, center=App.Vector(0, 0, 0),
                         use_link=True)
```


<div class="mw-translate-fuzzy">

-   Crea una serie dagli oggetti contenuti in `obj`, che può essere un singolo oggetto o un elenco di oggetti.

-   Il valore di `center` è un vettore che definisce il centro del cerchio della serie; `angle` è l\'angolo dell\'arco in gradi e `number` è il numero di copie nel modello polare, incluso l\'oggetto originale.

-   Se `use_link` è `True` le copie create saranno degli [App Link](App_Link/it.md) e non copie regolari.

-    `array_list`viene restituito con le nuove copie.

    -   
        `array_list`
        
        è un singolo oggetto o un elenco di oggetti, a seconda dell\'input di `obj`.


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

tri = Draft.make_polygon(3, 600)
center = App.Vector(-1600, 0, 0)

array = Draft.make_polar_array(tri, 8, 270, center)
doc.recompute()
```

### Non-parametric array 

To create a non-parametric polar array use the `array` method of the Draft module. This method returns `None`.


```python
array(objectslist, center, angle, number)
```

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

tri = Draft.make_polygon(3, 600)
center = App.Vector(-1600, 0, 0)

Draft.array(tri, center, 270, 8)
doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PolarArray/it
