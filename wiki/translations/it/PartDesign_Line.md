---
 GuiCommand:
   Name: PartDesign Line
   Name/it: Linea di riferimento
   MenuLocation: Part Design , Linea di riferimento
   Workbenches: PartDesign Workbench/it
   Version: 0.17
   SeeAlso: PartDesign Point/it, PartDesign Plane/it
---

# PartDesign Line/it


</div>

## Descrizione

Crea una **linea di riferimento** che può essere utilizzata come riferimento per schizzi, altre geometrie di riferimento o caratteristiche. Ad esempio può essere utilizzata come asse di rivoluzione per le funzioni Rivoluzione e Scanalatura.

<img alt="" src=images/datum_line.png  style="width:600px;"> 
*Due linee di riferimento attraverso gli angoli opposti del cubo si incontrano nel centro di massa.*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_Line.svg" width=24px> '''Linea di riferimento'''**.
2.  Definire i parametri della linea. Selezionare un primo riferimento nella vista 3D per filtrare le modalità di associazione disponibili.
3.  A seconda del riferimento selezionato, nell\'elenco sono disponibili una o più modalità di associazione. La più probabile è selezionata automaticamente e mostrata in grassetto nella lista. Il testo *Associata con modalità* insieme al nome della modalità di associazione appare in verde nella parte superiore del pannello Parametri.
4.  Per aggiungere un riferimento aggiuntivo, premere il successivo pulsante **Riferimento**. Una volta premuto, l\'etichetta cambia in *Selezione\...* fino a quando viene effettuata una selezione.
5.  Selezionare una modalità di associazione nell\'elenco.
6.  Definire i valori di offset dell\'associazione.
7.  Premere **OK**.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

Fare doppio clic sull\'etichetta DatumLine nell\'albero del modello o fare clic con il tasto destro e selezionare **Modifica il riferimento** nel menu contestuale per modificarne i parametri. Per ulteriori dettagli sulla modalità e l\'offset di associazione, vedere [Associazione](Part_EditAttachment/it.md).


</div>

## Proprietà

-    {{PropertyData/it|MapMode}}: elenca la modalità di associazione utilizzata.

-    {{PropertyData/it|Attachment Offset}}: applica una trasformazione (traslazione e rotazione) in riferimento alla posizione di associazione.

-    {{PropertyData/it|Label}}: nome dato all\'oggetto, questo nome può essere cambiato a piacere.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Line/it
