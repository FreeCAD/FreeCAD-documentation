---
- GuiCommand:/it
   Name:PartDesign Plane
   Name/it:Piano di riferimento
   Workbenches:[PartDesign](PartDesign_Workbench/it.md)
   MenuLocation:PartDesign → Piano di riferimento
   Version:0.17
   SeeAlso:[Punto di riferimento](PartDesign_Point/it.md), [Linea di riferimento](PartDesign_Line/it.md)
---

# PartDesign Plane/it


</div>

## Descrizione

Crea un **piano di riferimento** che può essere utilizzato come riferimento per schizzi o altre geometrie di riferimento. Gli schizzi possono essere associati ai piani di Riferimento. ![](images/Datum_plane.png ) *Piano di riferimento che attraversa 3 angoli del Cubo con un Cilindro disegnato su di esso usando il Piano di riferimento come suo Piano X-Y.*

## Prerequisiti


<div class="mw-translate-fuzzy">

A partire da FreeCAD 0.18 un piano di riferimento può essere creato solo all\'interno di un corpo. Ogni corpo ha un\'origine che di default è nascosta. Per poter fare riferimento ai piani di base dell\'origine, rendere visibile l\'origine. È possibile farlo prima di creare un piano di riferimento.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_Plane.svg" width=24px> '''Crea un piano di riferimento'''**.
2.  Definire i parametri del piano. Selezionare un primo riferimento nella vista 3D per filtrare le modalità di [associazione](Part_Attachment/it.md) disponibili.
3.  A seconda del riferimento selezionato, nell\'elenco possono essere disponibili una o più modalità di associazione. La più probabile è automaticamente selezionata e mostrata in grassetto nell\'elenco. Il testo *Associato in modalità* insieme al nome della modalità do associazione appare in verde nella parte superiore del pannello Parametri.
4.  Per aggiungere un riferimento aggiuntivo, premere il successivo tasto **Riferimento**. Una volta premuto, l\'etichetta cambia in \"Seleziona \...\" fino a quando viene effettuata una selezione.
5.  Selezionare una modalità di aassociazione nell\'elenco.
6.  **Offsets:** Definisce i valori di offset dell\'associazione. **Nota** che l\'offset x, y e z rappresenta il sistema di coordinate locale del piano di riferimento, non il sistema di coordinate globali. Pertanto, l\'offset z è sempre l\'offset lungo il vettore normale al piano di riferimento.
7.  **Rotation:** Cambiando Yaw si fa ruotare il piano attorno al suo asse Z locale. Cambiando Pitch si fa ruotare il piano attorno al suo asse Y locale. Cambiando Roll si fa ruotare il piano attorno al suo asse X locale.
8.  Premere **OK**.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

Fare doppio clic sull\'etichetta DatumPlane nell\'albero del modello o fare clic con il tasto destro e selezionare **Modifica il riferimento** nel menu contestuale per modificarne i parametri. Per ulteriori dettagli sulla modalità e l\'offset di associazione, vedere [Associazione](Part_Attachment/it.md).


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
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Plane/it
