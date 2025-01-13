---
 GuiCommand:
   Name: Part Offset
   Name/it: Offset 3D
   MenuLocation: Part , Offset 3D...
   
   SeeAlso: Part_Thickness/it, Part_Offset2D/it
---

# Part Offset/it



## Descrizione

Lo strumento <img alt="" src=images/Part_Offset.svg  style="width:24px;"> **Part Offset 3D** crea copie parallele di una forma selezionata ad una certa distanza dalla forma base, restituendo un nuovo oggetto.

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;">



## Utilizzo

1.  Selezionare un oggetto da sfalsare.
2.  Premere il pulsante **<img src="images/Part_Offset.svg" width=16px> [3D Offset](Part_Offset/it.md)**.
3.  Regolare la distanza e i parametri in base all\'oggetto originale e alla validità degli oggetti risultanti.



## Note

-   Gli oggetti [App Link](App_Link/it.md) collegati ai tipi di oggetto appropriati e i contenitori [App Part](App_Part/it.md) con gli oggetti visibili appropriati all\'interno possono essere utilizzati anche come oggetti di origine. {{Version/it|0.20}}



## Esempi

<img alt="" src=images/PartOffset0.png  style="width:" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:" height="200px;">

Oggetto con angoli sfalsati e arrotondati (arco).

<img alt="" src=images/PartOffset3.png  style="width:" height="200px;">

Stesso oggetto con angoli acuti (intersezione).

<img alt="" src=images/PartOffset2.png  style="width:" height="200px;">

Lo stesso oggetto con una distanza notevole sovraccaricando lo spazio anteriore sinistro e consentendo incroci.

<img alt="" src=images/PartOffset4.png  style="width:" height="200px;">

Forma arbitraria ([Draft Polilinea](Draft_Wire/it.md)) con un offset 3D (ignora il parametro MODE)

<img alt="" src=images/PartOffset5.png  style="width:" height="200px;">

Stessa forma con un offset 3D come SKIN e *filled*.

<img alt="" src=images/PartOffset6.png  style="width:" height="200px;">

offset \"riempito\" con 2 cilindri che creano tagli booleani. Il cilindro A passa attraverso il RIEMPIMENTO mentre il cilindro B passa solo attraverso il RIEMPIMENTO e NON attraverso la forma 2D sorgente.



## Proprietà

-    **Offset**: Distanza a cui sfalsare le facce della forma.

-    **Mode**: Modalità di creazione. *Skin* crea una nuova forma attorno alla forma sorgente. *Pipe* ( todo ) . *RectoVerso* ( todo ).

-    **Join type**: Come si costruiscono i nuovi angoli. *Intersection* dà angoli acuti sull\'estensione lineare dei bordi. *Arc* e *Tangent* danno angoli arrotondati.

1.  Optionː Intersectionː Consente gli offset rivolti verso l\'interno per \"sovrapporre\" il gap intersecando la forma risultante fino a raggiungere le facce opposte.
2.  Optionː Self Intersectionː (todo).
3.  Optionː Fill Offsetː Quando la forma è bidimensionale, lo spazio tra le 2 forme viene riempito. Il riempimento ora è un solido, ma la forma sorgente non è un solido. Quindi le operazioni booleane possono portare a risultati strani. (vedi esempio sotto).





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Offset/it
