# Interface creation/it
{{TOCright}}

## Introduzione

Gli utenti esperti hanno la possibilità di [creare delle interfacce](Interface_creation.md) che li aiutino a produrre strumenti complessi per i loro [addon](Addon/it.md) personalizzati, come le [macro](Macros/it.md) o interi [ambienti](Workbenches/it.md).

Le interfacce vengono create usando [PySide](PySide/it.md), che è una libreria per l\'utilizzo di Qt con [Python](Python/it.md).

<img alt="" src=images/FreeCAD_creating_interfaces.svg  style="width:600px;"> 
*Due metodi generali per creare delle interfacce, includendo l'interfaccia nel file Python o usando i file `.ui*.`

## Descrizione

Esistono in genere due modi per creare delle interfacce con PySide.

### Interfaccia in un file .ui 

Con questo metodo l\'interfaccia è definita in un file `.ui` (un documento XML che definisce la struttura dell\'interfaccia), che viene poi importato nel codice [Python](Python/it.md) che lo utilizza. Questo è l\'approccio consigliato.

-   Consente al programmatore di lavorare con l\'interfaccia grafica separatamente dalla logica che la utilizzerà.
-   Permette a chiunque di guardare solo l\'interfaccia, cioè il file `.ui`, senza dover eseguire codice Python.
-   Il file `.ui` può essere progettato da chiunque non abbia conoscenze di programmazione.
-   L\'interfaccia `.ui` può essere utilizzata in una finestra autonoma (modale) o in una finestra incorporata (non modale); pertanto, questo metodo è ideale per creare una [Scheda Azioni](Task_panel/it.md).
-   Dato che il file `.ui` descrive solo \"l\'aspetto\" dell\'interfaccia, non ha bisogno di essere legato a un particolare linguaggio di programmazione; può essere utilizzato sia nel codice [Python](Python/it.md) che in quello C++.

### Interfaccia completamente in codice Python 

In questo metodo l\'intera interfaccia è definita da diverse chiamate Python.

-   Questo è un vecchio modo di lavorare con le interfacce.
-   Questo metodo produce un codice molto prolisso perché molti dettagli dell\'interfaccia devono essere specificati manualmente.
-   Non è semplice separare l\'interfaccia dalla logica che utilizza quel codice, il che significa che un utente dovrebbe eseguire il file [Python](Python/it.md) nel contesto corretto per vedere come dovrebbe apparire l\'interfaccia.
-   Questo metodo ha il vantaggio che diverse interfacce possono essere contenute all\'interno di un singolo documento, a costo di rendere il file molto grande.
-   Questo metodo è consigliato solo per piccole interfacce che non definiscono più di alcuni widget, ad esempio in [macro](Macro/it.md).

Per esempi su questo metodo vedi [Creare delle finestre di dialogo](Dialog_creation/it.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Interface creation/it
