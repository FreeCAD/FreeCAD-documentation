---
- GuiCommand   */it
   Name   *Draft Facebinder
   Name/it   *Lega facce
   Workbenches   *[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   MenuLocation   *Draft → Lega facce
   Shortcut   ***F** **F**
   SeeAlso   *[Cubo](Part_Box/it.md) di Part, [Muro](Arch_Wall/it.md) di Arch
   Version   *0.14
---

# Draft Facebinder/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Lega facce (Facebinder) crea un oggetto superficie dalle facce selezionate di un oggetto solido. È parametrico, il che significa che se si modifica l\'oggetto originale, Lega facce si aggiorna di conseguenza. Se si sposta e ruota il Lega facce, esso rimane collegato ale facce originali.


</div>


<div class="mw-translate-fuzzy">

Può essere usato per creare un\'estrusione da una collezione di facce prese da altri oggetti. Un tipico utilizzo è nella progettazione architettonica per costruire un oggetto che copre diverse pareti, ad esempio una carta da parati o un intonaco.


</div>

<img alt="" src=images/Draft_facebinder_example.jpg  style="width   *400px;">


<div class="mw-translate-fuzzy">



*Facebinder creato dalle facce di pareti solide*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Sceglere una faccia o tenere premuto **Ctrl** e sceglere diverse facce da oggetti solidi.
2.  Premere il pulsante **<img src="images/Draft_Facebinder.svg" width=16px> [Lega facce](Draft_Facebinder/it.md)**, o premere i tasti **F** e poi **F**.


</div>


<div class="mw-translate-fuzzy">

## Proprietà

### Dati

-    {{PropertyData/it|Extrusion}}   * specifica uno spessore di estrusione da applicare a tutte le facce della forma.

-    {{PropertyData/it|Remove Splitter}}   * se è `True` cerca di fondere le intersezioni interne del Facebinder quando viene estruso.

-    {{PropertyData/it|Sew}}   * se è `True` tenta di eseguire un\'operazione di cucitura topologica sul Facebinder quando viene estruso.

-    **Offset**   * specifica una distanza di offset da applicare tra le facce legate e le facce originali, prima dell\'estrusione.

-    **Area**   * l\'area totale di queste facce legate.


</div>

See also   * [Property editor](Property_editor.md).

A Draft Facebinder object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties   *

### Data


{{TitleProperty|Draft}}

-    **Area|Area**   * (read-only) specifies the total area of the linked faces of the facebinder.

-    **Extrusion|Distance**   * specifies the extrusion thickness of the facebinder.

-    **Faces|LinkSubList**   * specifies the linked faces of the facebinder.

-    **Offset|Distance**   * specifies an offset distance to apply between the facebinder and the original faces, prior to extrusion.

-    **Remove Splitter|Bool**   * Specifies whether to remove splitter lines that divide co-planar faces of the facebinder.

-    **Sew|Bool**   * Specifies whether to perform a topological sewing operation on the facebinder.

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Vista

-    {{PropertyView/it|Pattern}}   * specifica un modello di [Campitura](Draft_Pattern/it.md) con cui riempire la faccia della forma. Questa proprietà funziona solo se {{PropertyView/it|Display Mode}} è \"Flat Lines\".

-    {{PropertyView/it|Pattern Size}}   * specifica la dimensione della [Campitura](Draft_Pattern/it.md).


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche   ***

[API Draft](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Lega facce può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione   *


</div>


```python
facebinder = make_facebinder(selectionset)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `Facebinder` dalla `selectionset`, che è una lista di `SelectionObject` come quelli restituiti da `FreeCADGui.Selection.getSelectionEx()`.
    -   
        `selectionset`
        
        può anche essere un `PropertyLinkSubList`.

Un `PropertyLinkSubList` è un elenco di tuple; ogni tupla contiene come primo elemento un `oggetto` e come secondo elemento un elenco (o tupla) di stringhe; queste stringhe indicano i nomi dei sotto-elementi (facce) di quell\'oggetto.


</div>


```python
PropertyLinkSubList = [tuple1, tuple2, tuple3, ...]
PropertyLinkSubList = [(object1, list1), (object2, list2), (object3, list3), ...]
PropertyLinkSubList = [(object1, ['Face1', 'Face4', 'Face6']), ...]
PropertyLinkSubList = [(object1, ('Face1', 'Face4', 'Face6')), ...]
```

Lo spessore di Facebinder può essere aggiunto sovrascrivendo il suo attributo `Extrusion`; il valore è inserito in millimetri.

Il posizionamento di Facebinder può essere cambiato sovrascrivendo il suo attributo `Placement`, o sovrascrivendo singolarmente i suoi attributi `Placement.Base` e `Placement.Rotation`.

Esempio   *


```python
import FreeCAD as App
import FreeCADGui as Gui
import Draft

doc = App.newDocument()

# Insert a solid box
box = doc.addObject("Part   *   *Box", "Box")
box.Length = 2300
box.Width = 800
box.Height = 1000

# selection = Gui.Selection.getSelectionEx()
selection = [(box, ("Face1", "Face6"))]
facebinder = Draft.make_facebinder(selection)
facebinder.Extrusion = 50

doc.recompute()

facebinder.Placement.Base = App.Vector(1000, -1000, 100)
facebinder.ViewObject.ShapeColor = (0.99, 0.99, 0.4)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Facebinder/it
