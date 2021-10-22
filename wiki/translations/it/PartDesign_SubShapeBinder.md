---
- GuiCommand:/it
   Name:PartDesign SubShapeBinder
   Name/it:Lega forme secondarie
   Workbenches:[PartDesign](PartDesign_Workbench/it.md)
   MenuLocation:Part Design → Forme legate secondarie
   Version:0.19
   SeeAlso:[PartDesign Forme legate](PartDesign_ShapeBinder/it.md), [PartDesign Clona](PartDesign_Clone/it.md)
---

# PartDesign SubShapeBinder/it

## Descrizione


<div class="mw-translate-fuzzy">

[PartDesign SubShapeBinder](PartDesign_SubShapeBinder/it.md) importa un elemento da un altro corpo nel [Corpo](PartDesign_Body/it.md) attivo. Può prendere delle [Forme](Shape/it.md) o essere \"associato\" a uno o più oggetti o sottoelementi (bordi o facce) di un altro oggetto.


</div>


<div class="mw-translate-fuzzy">

Quindi l\'oggetto legato risultante può essere spostato o essere utilizzato per eseguire operazioni avanzate come [operazioni booleane](PartDesign_Boolean/it.md) o [pad](PartDesign_Pad/it.md).


</div>

Può anche legare oggetti nidificati all\'interno di [Parti](Std_Part/it.md) e seguirà il posizionamento relativo di queste funzioni. Ciò è utile nel contesto della creazione di [assemblaggi](Assembly/it.md), poiché spesso si deve fare riferimento a [funzioni](PartDesign_Feature/it.md) che sono già correttamente posizionate in un altro sottoassieme.

<img alt="" src=images/PartDesign_SubShapeBinder_example_1.png  style="width:" height="300px;"> <img alt="" src=images/PartDesign_SubShapeBinder_example_2.png  style="width:" height="300px;">



*A sinistra: due solidi creati in due [corpi](PartDesign_Body/it.md) separati. A destra: due SubShapeBinders estratti dal primo corpo, importati nel secondo corpo e spostati in una posizione diversa.*

<img alt="" src=images/PartDesign_SubShapeBinder_example_3.png  style="width:" height="300px;"> 
*I due SubShapeBinders vengono utilizzati per creare un [taglio booleano](PartDesign_Boolean/it.md) e un [pad](PartDesign_Pad/it.md), con il secondo corpo.*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Iniziare con un **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/PartDesign_AdditivePrism.svg style="width:Corpo](PartDesign_Body/it.md)** già in atto, contenente una singola [funzione](PartDesign_Feature/it.md), per esempio, un **[16px">  [prisma additivo](PartDesign_AdditivePrism/it.md)**.
2.  Creare un secondo corpo, contenente una singola funzione, per esempio, un **<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [cubo additivo](PartDesign_AdditiveBox/it.md)**. Questo sarà il corpo attivo.
3.  Selezionare l\'intero primo corpo e premere **<img src=images/PartDesign_SubShapeBinder.svg style="width:16px"> [SubShapeBinder](PartDesign_SubShapeBinder/it.md)**.
4.  Modificare le proprietà di questo oggetto legato, ad esempio il suo posizionamento.
5.  Usarlo con un\'altra operazione, come ad esempio una **<img src=images/PartDesign_Boolean.svg style="width:16px"> [operazione booleana](PartDesign_Boolean/it.md)**.


</div>

## Proprietà

_, nell\'[editor delle proprietà](property_editor/it.md) sono disponibili le seguenti proprietà.

### Dati


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

-    **Support|XLinkSubList|hidden**: supporto per la geometria.

-    **Fuse|Bool**: se è `True` fonde le forme solide legate.

-    **Make Face|Bool**: se è `True` crea una faccia dalle polilinee connesse.

-    **Claim Children|PropertyBool**: se è `True` richiama gli oggetti collegati come figli nella [vista ad albero](tree_view/it.md).

-    **Relative|Bool**: se è `True` abiliterà il collegamento relativo degli oggetti secondari.

-    **Bind Mode|Enumeration**: modalità di legame, {{value|Synchronized}}, {{Value|Frozen}}, {{Value|Detached}}.

-    **Partial Load|Bool**: se è `True` abiliterà il caricamento parziale degli oggetti.

-    **Context|XLink|hidden**: oggetto contenitore di questo oggetto raccoglitore.

-    **_Version|Integer|hidden**: versione di questo tipo di oggetto.

-    **Shape|PartShape|hidden**: [Part TopoShape](Part_TopoShape.md) di questo oggetto.


</div>


{{TitleProperty|Cache}}

-    **Body|Matrix|hidden**: matrice di unità di questo oggetto.

### Vista

Vedere [Funzioni Part](Part_Feature/it.md).

## Link

-   [New Sublink Link Feature](https://forum.freecadweb.org/viewtopic.php?t=41450), spiegazione sull\'uso con video.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubShapeBinder/it
