# Part Loft/it
---
- GuiCommand:   Name: Part Loft   Name/it: Loft   MenuLocation: Part -> Loft...   ---


</div>

## Overview


<div class="mw-translate-fuzzy">

## Introduzione

Lo strumento Loft di FreeCAD (dell\'ambiente Parte), viene utilizzato per creare una faccia, un guscio o una forma solida da due o più profili. I profili possono essere un punto (vertice), una linea (bordo), una spezzata o una faccia. I bordi e le polilinee possono essere di tipo aperto o chiuso. Ci sono varie [limitazioni e complicazioni](Part_Loft/it#Limitazioni_e_complicazioni.md), descritte in seguito, tuttavia i profili possono provenire da primitive di Parte, da funzioni di Draft e da Schizzi.


</div>


<div class="mw-translate-fuzzy">

Loft dispone di tre parametri, \"Ruled\", \"Solid\" e \"Closed\" ciascuno con il valore di \"vero\" o \"falso\".


</div>


<div class="mw-translate-fuzzy">

Se \"Solid\" è \"true\" FreeCAD crea un solido se i profili sono una geometria chiusa, se è \"false\" crea una faccia oppure un guscio se c\'è più di una faccia, sia per profili aperti che chiusi.


</div>


<div class="mw-translate-fuzzy">

Se \"Ruled\" è \"true\" FreeCAD crea una faccia, oppure delle facce o un solido dalle superfici rigate. Vedere la pagina [Ruled surface in Wikipedia.](http://en.wikipedia.org/wiki/Ruled_surface)


</div>

Se \"Closed\" è \"true\" FreeCAD tenta di collegare l\'ultimo profilo al primo profilo per creare una figura chiusa.


<div class="mw-translate-fuzzy">

Per ulteriori informazioni su come sono uniti i profili, fare riferimento alla pagina [Dettagli tecnici di Part Loft](Part_Loft_Technical_Details/it.md).


</div>


<div class="mw-translate-fuzzy">

![centre\|Part_Loft. Da tre profili di cui due sono Part_Circles e uno è Part_Ellipse. I parametri sono Solid \"True\" e Ruled \"True\"](images/Part_Loft_solid_ruled_from3profiles_example_FreeCAD_0_13.jpg )


</div>

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as profiles and paths. <small>(v0.20)</small> 

## Limitations and complications 


<div class="mw-translate-fuzzy">

## Limitazioni e complicazioni 

-   Un vertice o un punto
    -   vertice o punto possono essere utilizzati solo come primo e/o ultimo profilo nella lista dei profili.
        -   Per esempio
            -   non si può realizzare un Loft da un cerchio ad un punto,e poi ad una ellisse.
            -   Tuttavia si può realizzare un Loft da un punto a un cerchio a un\'ellisse a un altro punto.
-   Profili geometrici aperti o chiusi non possono essere mischiati in un unico Loft
    -   In un Loft, tutti i profili usati (wire, linee ecc) devono essere dello stesso tipo, aperto o chiuso.
        -   Per esempio
            -   FreeCAD non può creare un Loft tra un cerchio di Parte e una linea di default di Parte.
-   Funzioni di Draft
    -   Le funzioni di Draft possono essere utilizzate direttamente come profilo in FreeCAD 0.14 o versioni successive.
        -   Ad esempio, le seguent funzioni di Draft possono essere utilizzate come profili in un Loft di Part
            -   Poligono.
            -   Punto, Linea, Wire (polilinea)
            -   B-spline, Curva di Bezier
            -   Cerchio, Ellisse, Rettangolo
-   Schizzi e PartDesign
    -   Il profilo può essere creato con uno schizzo. Tuttavia solo gli schizzi validi verranno visualizzati nell\'elenco di quelli disponibili per la selezione.
    -   Lo schizzo deve contenere un solo wire o linea aperta o chiusa (può essere composto da più segmenti, in quanto se questi segmenti sono tutti collegati costituiscono un unico wire)
-   Part
    -   il profilo può essere una primitiva geometrica valida di Part che può essere creata con lo strumento [Crea Primitive](Part_CreatePrimitives/it.md)
        -   Per esempio le seguenti primitive geometriche di Part possono essere un profilo valido
            -   Punto o vertice (Vertex), Linea o bordo (Edge)
            -   Elica, Spirale
            -   Cerchio, Ellisse
            -   Poligono regolare
            -   Piano o facce (Face)


</div>


<div class="mw-translate-fuzzy">

-   Loft chiusi
    -   I risultati dei loft chiusi possono essere inaspettati - il loft può produrre torsioni o piegature. L\'operazione Loft è molto sensibile al posizionamento dei profili e per collegare i corrispondenti vertici in tutti i profili servono curve molto complesse.


</div>

## An example Loft 


<div class="mw-translate-fuzzy">

## Un esempio di Loft 

Lo strumento Loft si trova nell\'ambiente Parte, menu Parte -\> Loft \... o tramite l\'icona nella barra degli strumenti.


</div>

![](images/Part_Loft_Ikon_Ballon_Hilfe.png )


<div class="mw-translate-fuzzy">

Nella sezione \"Azioni\" della \"Vista Combinata\" ci sono due liste: \"Vertice/Spigolo/Wire/Faccia\" e \"Loft\".


</div>

![](images/Loft_it_2.png )


<div class="mw-translate-fuzzy">

### Selezione delle sezioni 

In \"Vertice/Spigolo/\...\" vengono visualizzati tutti gli oggetti disponibili. In questo elenco devono essere selezionati due elementi, uno dopo l\'altro.


</div>

![](images/Loft_it_3.png )


<div class="mw-translate-fuzzy">

Successivamente, con la freccia blu l\'elemento deve essere aggiunto alla lista di \"Loft\".


</div>

![](images/Loft_it_4.png )

Gli elementi selezionati devono essere dello stesso tipo, come nella figura.


<div class="mw-translate-fuzzy">

Suggerimento: le voci attive o selezionate nell\'elenco vengono visualizzati nell\'area 3D come attive o selezionate.


</div>

### Command complete 


<div class="mw-translate-fuzzy">

### Completare il comando 

Se sono state selezionate entrambe le sezioni, il comando può essere completato cliccando su \"OK\".


</div>

![](images/Loft_it_5.png )

### Result


<div class="mw-translate-fuzzy">

## Risultato

Dalle linee chiuse sono sorte delle superfici che al primo sguardo potrebbero essere considerate superfici di solidi.


</div>

![](images/Loft_it_6.png )


<div class="mw-translate-fuzzy">

Se invece si vuole effettivamente creare un solido, questo si può fare utilizzando il pulsante \"Crea Solid\" quando si crea oppure, dopo aver creato, utilizzando il campo \"Solid\" delle proprietà nella scheda *Dati*.


</div>

La procedura è analoga a quella descritta per le polilinee aperte.

### Changing the selection of sections 


<div class="mw-translate-fuzzy">

### Modifica della selezione delle sezioni 

Se si desidera modificare la selezione delle sezioni dopo la creazione del loft, è possibile selezionare il campo Sezioni nella scheda Dati e fare clic sul pulsante con i puntini di sospensione. Appare l\'elenco di tutte le sezioni selezionabili, e la selezione corrente viene evidenziata. Si può rimuovere o aggiungere ulteriori sezioni.


</div>


<div class="mw-translate-fuzzy">

La sequenza delle sezioni dipende dalla sequenza di selezione nell\'elenco. Se si desidera apportare modifiche sostanziali, si consiglia di deselezionare tutto e quindi avviare la selezione nell\'ordine corretto.


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft/it
