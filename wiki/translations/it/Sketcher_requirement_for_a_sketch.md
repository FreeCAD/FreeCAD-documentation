---
 TutorialInfo:t
   Topic: Sketch
   Level: Base
   Author: User:Maker
   Time: 
   FCVersion: Tutte
---

# Sketcher requirement for a sketch/it





## Requisito minimo per uno schizzo 

Per creare un Corpo nell\'ambiente PartDesign è possibile utilizzare un profilo *solo* quando esso è chiuso. Non è necessario che siano definite tutte le sue dimensioni e proprietà ovvero che lo schizzo sia *completamente vincolato*.

Se un profilo è chiuso o aperto non è evidente e non riconoscibile. Ad esempio, quando si collega un arco a una retta i due punti finali possono essere creati uno vicino all\'altro, ma non essere coincidenti. È necessario utilizzare il vincolo <img alt="" src=images/_Constraint_PointOnPoint.svg  style="width:32px;"> [Coincidente](Sketcher_ConstrainCoincident/it.md) per creare un singolo punto che colleghi effettivamente la linea e l\'arco.

![](images/Skizze2a.png )



*Un semplice schizzo. A sinistra una curva chiusa solo in quattro punti indicati in rosso, che sono i vincoli automatici applicati quando si disegna con lo strumento [<img src=images/_Sketcher_CreatePolyline.svg style="width:32px"> [Polilinea](Sketcher_CreatePolyline.md). Al centro un avviso di faccia non valida perché il contorno è aperto. A destra il contorno chiuso nei restanti quattro punti indicati in verde.*

Un funzionamento parametrico coerente significa che lo schizzo è completamente determinato.

## Definire completamente uno schizzo 

Anche uno schizzo relativamente semplice può contenere numerose indeterminazioni, indicate nella vista combinata come numero di \"gradi di libertà\". Eliminarle tutte insieme alla fine è un compito abbastanza complicato.

![](images/Skizze4a.png )



*Un semplice schizzo, completamente determinato da 25 vincoli, di cui solo 5 sono vincoli di dimensione*

Questo lavoro è più chiaro e più semplice se si eliminano immediatamente le \"libertà\" di ciascun elemento geometrico aggiunto, definendo subito i valori delle loro dimensioni ed i posizionamenti. La completezza provvisoria viene raggiunta se tutte le linee sono visualizzate in verde.

Se si aspetta fino alla fine del disegno per determinare le \"libertà\" rimanenti esse sono trovabili toccando i punti e le linee con il puntatore del mouse e determinando dove non sono ancora state fissate. Al termine, l\'intero disegno viene visualizzato in verde.

Se si crea accidentalmente una \"ridondanza\", nella vista combinata viene visualizzato un avviso che richiede di annullare i vincoli corrispondenti.


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher requirement for a sketch/it
