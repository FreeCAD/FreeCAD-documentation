---
 GuiCommand:
   Name: Std_MeasureDistance
   Name/it: Misura la distanza
   MenuLocation: Strumenti , Misura la distanza
   Workbenches: Tutti
   SeeAlso: Std_Measure/it, Draft_Dimension/it
---

# Std MeasureDistance/it



## Descrizione

Il comando **Misura la distanza** crea un oggetto distanza che misura e visualizza la distanza tra due punti.



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_MeasureDistance.svg" width=16px> [Misura la distanza](Std_MeasureDistance/it.md)**.
    -   Selezionare l\'opzione **Strumenti → <img src="images/Std_MeasureDistance.svg" width=16px> Misura la distanza** nel menu.
2.  Selezionare il primo punto della dimensione in qualsiasi punto di un oggetto nella [vista 3D](3D_view/it.md).
3.  Selezionare il secondo punto della dimensione in qualsiasi punto di un oggetto nella vista 3D.
4.  L\'ordine di selezione dei punti può avere un impatto sulla posizione della linea di quota.
5.  Facoltativamente, capovolgere la posizione della linea di quota modificando la proprietà **Mirror** dell\'oggetto distanza.



## Note

-   Non è possibile utilizzare gli strumenti snap di [Draft](Draft_Workbench/it.md) con questo comando.
-   Per aggiungere quote ai disegni utilizzare gli strumenti di quotatura da [TechDraw](TechDraw_Workbench/it.md).
-   Per strumenti di misurazione più completi, installare <img alt="" src=images/Manipulator_workbench_icon.svg  style="width:24px;"> [Manipulator](Manipulator_Workbench/it.md) (un [ambiente complementare](External_workbenches/it.md)).



## Proprietà



### Dati


{{TitleProperty|Base}}

-    **Label**: di default l\'etichetta contiene la distanza misurata, ma questa distanza non viene aggiornata quando P1 o P2 vengono successivamente modificati.


{{TitleProperty|Measurement}}

-    **P1**: il primo punto di dimensione.

-    **P2**: il secondo punto di dimensione.

-    **Distance**: (sola lettura) la distanza misurata tra P1 e P2.



### Vista


{{TitleProperty|Base}}

-    **Dist Factor**: questo fattore, moltiplicato per la distanza misurata, determina l\'offset della linea di quota.

-    **Font Size**: l\'altezza delle lettere (altezza della linea in pixel).

-    **Mirror**: se impostato su `True`, la posizione della linea di quota relativa a P1 e P2 viene invertita.





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std MeasureDistance/it
