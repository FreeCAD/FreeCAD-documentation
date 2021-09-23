---
- GuiCommand:/it
   Name:Draft Downgrade
   Name/it:Declassa
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Declassa
   Shortcut:**D** **N**
   SeeAlso:[Promuovi](Draft_Upgrade/it.md), [Taglio di Part](Part_Cut/it.md)
---

# Draft Downgrade/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_Downgrade.svg  style="width:16px;"> [Declassa](Draft_Downgrade/it.md) scompone gli oggetti selezionati (converte un oggetto in diversi oggetti di livello inferiore). Lo strumento esegue il declassamento degli oggetti selezionati in modi diversi.


</div>

<img alt="" src=images/Draft_Downgrade_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


*Faccia tagliata con un'altra faccia; quindi faccia declassata in un contorno chiuso; e poi contorno scomposto in singole linee
*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare uno o più oggetti che si desidera declassare.
2.  Premere il pulsante **<img src="images/Draft_Downgrade.png" width=16px> [Declassa](Draft_Downgrade/it.md)** o premere i tasti **D** e **N**. Se nessun oggetto è selezionato, si viene invitati a selezionarne uno.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Declassa può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
downgrade_list = downgrade(objects, delete=False, force=None)
```


<div class="mw-translate-fuzzy">

-   Declassa gli `objects` dati, che può essere un singolo oggetto o un elenco di oggetti.
-   Se `delete` è `True`, i vecchi oggetti vengono cancellati.
-   Se è dato `force`, è la funzione interna chiamata per forzare un certo modo di declassamento. Può essere: `"explode"`, `"shapify"`, `"subtr"`, `"splitFaces"`, `"cut2"`, `"getWire"`, o `"splitWires"`.
-   Viene restituita una `upgrade_list`, che è una lista contenente due liste: la lista di nuovi oggetti (`addList`) e la lista degli oggetti da eliminare (`deleteList`).


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle = Draft.make_circle(1000)
rectangle = Draft.make_rectangle(2000, 800)
doc.recompute()

add_list1, delete_list1 = Draft.upgrade([circle, rectangle], delete=True)

compound = add_list1[0]
add_list2, delete_list2 = Draft.downgrade(compound, delete=False)
face = add_list2[0]
add_list3, delete_list3 = Draft.downgrade(face, delete=False)

box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 800
box.Height = 1000

add_list4, delete_list4 = Draft.downgrade(box, delete=True)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Downgrade/it
