# Part Offset/it
---
- GuiCommand:/it   Name:Part Offset   Name/it:Offset 3D   MenuLocation:Part → Offset 3D...   |Workbenches:[SeeAlso:[[Part_Thickness/it|Spessore](Part_Workbench/it___Part]].md), [Offset 2D](Part_Offset2D/it.md)---


</div>

## Descrizione

Lo strumento Offset 3D di Parte crea delle copie parallele di una forma selezionata ad una certa distanza dalla forma base, dando un nuovo oggetto.

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;">

## Utilizzo

1.  Selezionare l\'oggetto da cui si vuole creare l\'offset.
2.  Premere il pulsante **<img src="images/Part_Offset.svg" width=16px> '''Offset 3D'''
**
3.  Regolare la distanza e i parametri che dipendono dall\'oggetto originale e dagli oggetti risultanti.

## Proprietà

-    **Offset**: Distanza a cui sfalsare le facce della forma

-    **Mode**: Modalità di creazione. Skin crea una nuova forma attorno alla forma sorgente. Pipe ( todo ) . RectoVerso ( todo )

-    **Join type**: Come si costruiscono i nuovi angoli. Intersection dà angoli acuti sull\'estensione lineare dei bordi. Arc e Tangent danno angoli arrotondati.

1.  Option ː Intersection ː Consente gli offset rivolti verso l\'interno per \"sovrapporre\" il gap intersecando la forma risultante fino a raggiungere le facce opposte.
2.  Option ː Self Intersection ː ( todo )
3.  Option ː Fill Offset ː Quando la forma è bidimensionale, lo spazio tra le 2 forme viene riempito. Il riempimento ora è un solido, ma la forma sorgente non è un solido. Quindi le operazioni booleane possono portare a risultati strani. (vedi esempio).


<div class="mw-translate-fuzzy">

## Esempio


</div>

Oggetto con angoli sfalsati e arrotondati (arco).

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;"> 

Stesso oggetto con angoli acuti (intersezione).

<img alt="" src=images/PartOffset3.png  style="width:400" height="200px;"> 

Lo stesso oggetto con una distanza notevole sovraccaricando lo spazio anteriore sinistro e consentendo incroci.

<img alt="" src=images/PartOffset2.png  style="width:400" height="200px;"> 

Forma arbitraria (polilinea di Draft) con un offset 3D (ignora il parametro MODE)

<img alt="" src=images/PartOffset4.png  style="width:400" height="200px;"> 

Stessa forma con un offset 3D come Skin e *filled*.

<img alt="" src=images/PartOffset5.png  style="width:400" height="200px;"> 

offset \"riempito\" con 2 cilindri che creano tagli booleani. Il cilindro A passa attraverso il RIEMPIMENTO mentre il cilindro B passa solo attraverso il RIEMPIMENTO e NON attraverso la forma 2D sorgente.

<img alt="" src=images/PartOffset6.png  style="width:400" height="200px;"> 


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Offset/it
