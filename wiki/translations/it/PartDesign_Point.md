---
- GuiCommand:
   Name:PartDesign Point
   Name/it:Punto di riferimento
   Workbenches:[PartDesign](PartDesign_Workbench/it.md)
   MenuLocation:Part Design - Punto di riferimento
   Version:0.17
   SeeAlso:[Linea di riferimento](PartDesign_Line/it.md), [Piano di riferimento](PartDesign_Plane/it.md)
---

# PartDesign Point/it


</div>

## Descrizione

Crea un **punto di riferimento** che può essere utilizzato come riferimento per schizzi o altre geometrie di riferimento.

![](images/DatumPoint.png ) 
*Un punto di riferimento associato a una sfera con un offset di {{Value|2* nella direzione Z}}

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_Point.svg" width=24px> '''Punto di riferimento'''**.
2.  Definire i parametri del punto. Selezionare un primo riferimento nella vista 3D per filtrare le modalità di associazione disponibili.
3.  A seconda del riferimento selezionato, nell\'elenco sono disponibili una o più modalità di associazione. La più probabile è selezionata automaticamente e mostrata in grassetto nella lista. Il testo *Associata con modalità* insieme al nome della modalità di associazione appare in verde nella parte superiore del pannello Parametri.
4.  Per aggiungere un riferimento aggiuntivo, premere il successivo pulsante **Riferimento**. Una volta premuto, l\'etichetta cambia in *Selezione\...* fino a quando viene effettuata una selezione.
5.  Selezionare una modalità di associazione nell\'elenco.
6.  Definire i valori di offset dell\'associazione.
7.  Premere **OK**.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

Fare doppio clic sull\'etichetta DatumPoint nell\'albero del modello o fare clic con il tasto destro e selezionare **Modifica il riferimento** nel menu contestuale per modificarne i parametri. Per ulteriori dettagli sulla modalità e l\'offset di associazione, vedere [Associazione](Part_EditAttachment/it.md).


</div>

## Proprietà

-    {{PropertyData/it|MapMode}}: elenca la modalità di associazione utilizzata.

-    {{PropertyData/it|Attachment Offset}}: applica una trasformazione (traslazione e rotazione) in riferimento alla posizione di associazione.

-    {{PropertyData/it|Label}}: nome dato all\'oggetto, questo nome può essere cambiato a piacere.

## Limitazioni

-   Il punto di riferimento non può essere utilizzato come sezione per le funzionalità di Sweep e Loft.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Point/it
