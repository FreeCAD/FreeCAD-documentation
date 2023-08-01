# Part Thickness/it
---
- GuiCommand:   Name:Part_Thickness   Name/it:Spessore   MenuLocation:Parte - Spessore...   |Workbenches:[SeeAlso:[[Part_Offset/it|Offset](Part_Workbench/it___Parte]].md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Lo strumento <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> **Spessore** funziona su una forma solida, la trasforma in un oggetto cavo, dando a ciascuna delle sue facce un dato spessore. In alcuni solidi permette di velocizzare notevolmente il lavoro ed evita noiose estrusioni e tasche.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Utilizzo

1.  Creare un solido
2.  Selezionare una o più facce
3.  Cliccare sullo strumento **<img src="images/Part_Thickness.svg" width=16px> '''Spessore...'''
**
4.  Impostare i parametri
5.  Cliccare su **OK** per confermare, creare l\'operazione e uscire dal comando
6.  Se è necessario, adattare i parametri nella tabella delle proprietà.


</div>

## Options


<div class="mw-translate-fuzzy">

### Opzioni

-   Thickness: Spessore della parete nell\'oggetto risultante, impostare il valore desiderato
    -   Un valore positivo aggiunge lo spessore verso l\'esterno
    -   Un valore negativo aggiunge lo spessore verso l\'interno
-   Mode
    -   Skin: Selezionare questa opzione se si desidera ottenere un oggetto simile a un vaso, senza testa, ma con il fondo
    -   Pipe: Selezionare questa opzione se si desidera ottenere un oggetto simile a un tubo, senza testa e senza fondo. In questo caso può essere conveniente selezionare le facce da eliminare prima di avviare lo strumento. Aiutarsi con i pulsanti delle viste predefinite o utilizzare i tasti numerici.
    -   RectoVerso:
-   Join Type
    -   Arc: rimuove i bordi esterni e crea dei raccordi con raggio pari allo spessore definito
    -   Tangent:
    -   Intersection:
-   Intersection:
-   Self-intersection: abilita self-intersection
-   Facce / Fatto: Selezionare le facce da rimuovere, quindi fare clic su Fatto
-   Update view: Aggiorna automaticamente la visualizzazione in tempo reale


</div>

## Notes


<div class="mw-translate-fuzzy">

## Limitazioni

A volte, su qualche forma, produce risultati bizzarri. Salvare il lavoro prima di applicare Spessore su oggetti complessi


</div>

## Links


<div class="mw-translate-fuzzy">

### Links 

Un buon esempio su come utilizzare questo strumento nel forum: [Re: Help designing a simple enclosure](http://forum.freecadweb.org/viewtopic.php?f=3&t=3766&p=29741&hilit=enclosure#p29547)


</div>



## Esempi

**Hollow cylinder**

1.  Create **<img src="images/Part_Cylinder.svg" width=16px> [Cylinder](Part_Cylinder.md)** with radius 10mm and height 20mm
2.  Select the top and bottom surface of the cylinder
3.  Click on the **<img src="images/Part_Thickness.svg" width=16px> Thickness
** button (no need to change default settings) and press **OK**

Notes:

-   For this shape, consider using **<img src="images/Part_Tube.svg" width=16px> [Tube](Part_Tube.md)** instead.
-   Select the cylinder\'s top surface only to create a receptacle.

![](images/ThicknessEsempio1.png )

![](images/ThicknessEsempio2.png )

**Box-Enclosure**

![](images/ThicknessEsempio3.png )

![](images/ThicknessEsempio4.png )


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Thickness/it
