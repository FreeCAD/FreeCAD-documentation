---
- GuiCommand   */it
   Name   *Std_MeasureDistance
   Name/it   *Misura la distanza
   MenuLocation   *Strumenti → Misura la distanza
   Workbenches   *Tutti
   SeeAlso   *[Menu Misure](Std_Measure_Menu/it.md), [Dimensioni di Draft](Draft_Dimension/it.md), [Ispeziona di Arch](Arch_Survey/it.md)
---

# Std MeasureDistance/it


</div>

## Descrizione

Il comando **Misura la distanza** crea un oggetto distanza che misura e visualizza la distanza tra due punti.

## Utilizzo

1.  Esistono diversi modi per invocare il comando   *
    -   Premere il pulsante **<img src="images/Std_MeasureDistance.svg" width=16px> [Misura la distanza](Std_MeasureDistance/it.md)**.
    -   Selezionare l\'opzione **Strumenti → <img src="images/Std_MeasureDistance.svg" width=16px> Misura la distanza** nel menu.
2.  Selezionare il primo punto della dimensione in qualsiasi punto di un oggetto nella [vista 3D](3D_view/it.md).
3.  Selezionare il secondo punto della dimensione in qualsiasi punto di un oggetto nella vista 3D.
4.  L\'ordine di selezione dei punti può avere un impatto sulla posizione della linea di quota.
5.  Facoltativamente, capovolgere la posizione della linea di quota modificando la proprietà **Mirror** dell\'oggetto distanza.

## Note


<div class="mw-translate-fuzzy">

-   Con questo comando non è possibile utilizzare gli strumenti snap di [Draft](Draft_Workbench/it.md).
-   Per aggiungere quote ai disegni, utilizzare gli strumenti di quotatura di [TechDraw](TechDraw_Workbench/it.md).


</div>

## Proprietà

### Dati


{{TitleProperty|Base}}

-    **Label**   * di default l\'etichetta contiene la distanza misurata, ma questa distanza non viene aggiornata quando P1 o P2 vengono successivamente modificati.


{{TitleProperty|Measurement}}

-    **P1**   * il primo punto di dimensione.

-    **P2**   * il secondo punto di dimensione.

-    **Distance**   * (sola lettura) la distanza misurata tra P1 e P2.

### Vista


{{TitleProperty|Base}}

-    **Dist Factor**   * questo fattore, moltiplicato per la distanza misurata, determina l\'offset della linea di quota.

-    **Font Size**   * l\'altezza delle lettere (altezza della linea in pixel).

-    **Mirror**   * se impostato su `True`, la posizione della linea di quota relativa a P1 e P2 viene invertita.


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std MeasureDistance/it
