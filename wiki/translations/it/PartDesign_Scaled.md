# PartDesign Scaled/it
 {{GuiCommand/it|Name=PartDesign Scaled|Name/it=Scala|Workbenches=[PartDesign](PartDesign_Workbench/it.md), Completo|MenuLocation=PartDesign → Multitrasformazione}}

## Descrizione

Lo strumento **Scala** prende come input un insieme di una o più operazioni selezionate (\'gli originali\') e li scala per un determinato fattore. Poiché la scalatura avviene attorno al centro di gravità delle operazioni selezionate, di solito gli originali scompaiono all\'interno delle versioni in scala. Pertanto, in genere è utile solo per effettuare il ridimensionamento come parte di una operazione di Multi-trasformazione.

A partire da FreeCAD 0.15, questa funzione non è disponibile direttamente, ma è inclusa come componente dello strumento [Multitrasformazione](PartDesign_MultiTransform/it.md).

### Opzioni

+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/Scaled_parameters.png ) | Quando si crea una operazione Scala, la finestra di dialogo **Parametri della scalatura** offre le seguenti opzioni:                                                   |
|                                                    |                                                                                                                                                                        |
|                                                    | #### Selezionare gli originali                                                                                                             |
|                                                    |                                                                                                                                                                        |
|                                                    | La finestra *Vista combinata* mostra lista delle operazioni (oggetti) \"originali\" che devono essere scalati. Fare clic su una operazione per aggiungerla alla lista. |
|                                                    |                                                                                                                                                                        |
|                                                    | #### Fattore di scala e numero di copie                                                                                           |
|                                                    |                                                                                                                                                                        |
|                                                    | **Factor** e **Occurrences** specificano rispettivamente il fattore di scala massimo e il numero totale di forme scalate (inclusa l\'originale) che si vuole ottenere. |
+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+




## Limitazioni

-   La scalatura avviene sempre utilizzando il centro di gravità delle operazioni come punto base.
-   La trasformazione di scalatura non deve essere la prima della lista
-   La trasformazione di scalatura deve avere lo stesso numero di occorrenze della trasformazione immediatamente precedente nella lista
-   Vedere la funzione [Schiera lineare](PartDesign_LinearPattern/it.md) per altre limitazioni
-   Vedere le [MultiTrasformazioni](PartDesign_MultiTransform/it.md) per maggiori dettagli

## Esempi

![c\|center\|800px](images/mt_example2.png ) Il pad più piccolo è stato riprodotto tre volte in direzione X e poi scalato con un fattore due (così le tre occorrenze hanno il fattore di scala 1.0, 1.5 e 2.0). Poi è stata applicata una schiera polare con 8 occorrenze.

Poiché la scalatura viene eseguita rispetto al centro di gravità, nel caso di un Pad, è necessario che il pad penetri anche nel corpo principale, altrimenti gli oggetti scalati sono flottanti, staccati dal corpo. Per avere un pad che interseca il corpo principale possono essere utilizzate le opzioni \"due dimensioni\" o \"simmetrica al piano\". 
