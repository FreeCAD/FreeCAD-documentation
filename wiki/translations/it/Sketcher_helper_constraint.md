# Sketcher helper constraint/it
## Introduzione

<img alt="Esempio di vincolo di supporto (il Constraint5 - punto su cerchio) per un vincolo di tangenza (il Constraint6 nel modo \"tangenza in un punto\"). In questo caso viene usato un solo vincolo di supporto, poiché il punto di tangenza è il punto finale del diametro maggiore dell\'ellisse, che si trova intrinsecamente sull\'ellisse." src=images/Sketcher_helper_constraint_example1.png ). In questo caso viene usato un solo vincolo di supporto, poiché il punto di tangenza è il punto finale del diametro maggiore dell'ellisse, che si trova intrinsecamente sull'ellisse." style="width:500px;">

Il vincolo di supporto è un normale vincolo di Sketcher che viene richiesto come parte di un vincolo più complesso, ed è mostrato nell\'interfaccia per aiutare l\'utente a gestire le ridondanze. Ad esempio, nel vincolo di [Rifrazione](Sketcher_ConstrainSnellsLaw/it.md), le due linee che rappresentano i raggi di luce devono essere collegate tra di loro con il vincolo di [Coincidenza](Sketcher_ConstrainCoincident/it.md) applicato nei punti finali, e la congiunzione deve trovarsi sull\'interfaccia con il vincolo [Punto su oggetto](Sketcher_ConstrainPointOnObject/it.md).

Quando sono necessari, i vincoli di supporto sono aggiunti automaticamente. Attualmente la decisione se sono necessari viene presa valutando l\'errore del vincolo di supporto per lo stato attuale della geometria, ma questo potrebbe cambiare nelle future versioni. Se l\'errore è sufficientemente piccolo, il vincolo è considerato inutile, e non viene aggiunto. In alcuni casi, questa logica può portare ad errori; ad esempio, il vincolo può essere soddisfatto per caso, e questo può accadere facilmente quando in Sketcher è attiva la funzione \"Aggancia alla griglia\".

Se manca un vincolo di supporto, e le condizioni richieste non sono soddisfatte in altro modo, il \"vincolo complesso\" sarà difettoso. Si ottiene qualcosa di imprevedibile. Il vincolo difettoso può essere riparato aggiungendo manualmente il vincolo di supporto mancante.

Attualmente, i vincoli di supporto sono necessari per i seguenti vincoli:

-   [Tangente](Sketcher_ConstrainTangent/it.md) nel modo \"tangenza in un punto\" sono necessari due vincoli \"punto su oggetto\"
-   [Perpendicolare](Sketcher_ConstrainPerpendicular/it.md) nel modo \"perpendicolare in un punto\" sono necessari due vincoli \"punto su oggetto\"
-   [Angolo](Sketcher_ConstrainAngle/it.md) nel modo \"angolo in un punto\" sono necessari due vincoli \"punto su oggetto\"
-   [Rifrazione](Sketcher_ConstrainSnellsLaw/it.md) sono necessari un vincolo \"coincidenza\" e un vincolo \"punto su oggetto\"

## Script

Quando i vincoli che richiedono dei supporti sono aggiunti tramite gli script Python, i vincoli di supporto non vengono aggiunti automaticamente. In uno script si può replicare la decisione presa automaticamente dai comandi della UI testando le seguenti funzioni, che sono state aggiunte specificamente per questo scopo e che sono usate nelle routine dell\'interfaccia: 
```python
Sketch.isPointOnCurve(icurve,x,y)
``` isPointOnCurve verifica se un punto virtuale, dato dalle coordinate x,y (virgola mobile) dello schizzo, è idoneo per soddisfare un virtuale vincolo di punto su oggetto - cioè si trova sulla curva specificata dalla curva di indice icurve. Restituisce True se il punto è sulla curva, e False se non lo è.


```python
Sketch.calculateConstraintError(iconstr)
```

calculateConstraintError valuta una funzione di errore di un vincolo specificato dal suo indice iconstr nello schizzo. Se nel vincolo vi è una sola funzione di errore, il valore restituito è il valore restituito firmato della funzione di errore. Se al vincolo è associata più di una funzione di errore (cioè il vincolo rimuove più di un grado di libertà), il valore restituito è la radice della media del quadrato (RMS) di tutte le funzioni di errore (sempre positivo).



## Versione

I vincoli di supporto sono stati introdotti nella versione 0.15.4387


{{Sketcher Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher helper constraint/it
