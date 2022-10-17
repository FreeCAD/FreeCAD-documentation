---
- GuiCommand   */it
   Name   *PartDesign CoordinateSystem
   Name/it   *Sistema di coordinate locale
   MenuLocation   *PartDesign → Sistema di coordinate locale
   Workbenches   *[PartDesign](PartDesign_Workbench/it.md)
   Version   *0.18
   SeeAlso   *[Punto di riferimento](PartDesign_Point/it.md), [Linea di riferimento](PartDesign_Line/it.md), [Piano di riferimento](PartDesign_Plane/it.md)
---

# PartDesign CoordinateSystem/it


</div>

## Descrizione

Crea un **sistema di coordinate locali** che può essere usato come riferimento per altre geometrie di riferimento. Aiuta anche a identificare l\'orientamento della geometria di riferimento referenziata nello spazio 3D. ![](images/PartDesign_LocalCoordinateSystem_Example.png ) 
*Sistema di coordinate locale originato dall'origine di un piano di riferimento.*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **[<img src=images/PartDesign_CoordinateSystem.svg style="width   *16px"> [Sistema di coordinate locale](PartDesign_CoordinateSystem/it.md)**.
2.  Definire i parametri del sistema di coordinate. Selezionare un primo riferimento nella vista 3D per filtrare le modalità di associazione disponibili.
3.  A seconda del riferimento selezionato, nell\'elenco possono essere disponibili una o più modalità di associazione. La più probabile viene selezionata automaticamente e mostrata in grassetto nell\'elenco. Nella parte superiore del pannello Parametri appare in verde il testo *Associato con modalità* insieme al nome della modalità di associazione.
4.  Per aggiungere un riferimento aggiuntivo, premere il successivo pulsante **Riferimento**. Una volta premuto, l\'etichetta cambia in \"Selezione \...\" fino a quando viene effettuata una selezione.
5.  Selezionare una modalità di associazione nell\'elenco.
6.  Definire i valori di offset dell\'associazione.
7.  Premere **OK**.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

Fare doppio clic sull\'etichetta **Local_CS** nell\'albero del modello o fare clic con il tasto destro e selezionare **Modifica il riferimento** nel menu contestuale per modificarne i parametri. Per ulteriori dettagli sulla modalità e l\'offset di associazione, vedere [Associazione](Part_EditAttachment/it.md).


</div>

## Proprietà

### Dati

-    **MapMode**   * elenca le modalità di associazione utilizzabili.

-    **Attachment Reversed**   * indica se l\'orientamento del sistema di coordinate è invertito.

-    **Attachment Offset**   * applica una trasformazione (traslazione e rotazione) in riferimento alla posizione del riferimento.

-    **Placement**   * indica le coordinate e l\'allineamento dell\'origine del sistema di coordinate.

-    **Label**   * nome dato all\'oggetto, questo nome può essere cambiato a piacere.

## Script


```python
lcs = App.activeDocument().addObject( 'PartDesign   *   *CoordinateSystem', 'LCS' )
```


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign CoordinateSystem/it
