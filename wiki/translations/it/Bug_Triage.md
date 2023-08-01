# Bug Triage/it
## Perchè


{{ColoredParagraph|Triageː

1a: lo smistamento e l'assegnazione delle cure ai pazienti e in particolare alle vittime di battaglie e disastri secondo un sistema di priorità è progettato per massimizzare il numero di sopravvissuti

1b : lo smistamento dei pazienti (come in un pronto soccorso) è in base all'urgenza del loro bisogno di cure

2: l'assegnazione di un ordine di priorità ai progetti sulla base di dove i fondi e le altre risorse possono essere utilizzati al meglio o sono più necessari o hanno maggiori probabilità di ottenere successo
}}

La valutazione dei bug è importante per organizzare e dare priorità a bug/funzionalità/patch rispetto al [Bug Tracker](Tracker/it.md) di FreeCAD. Se questa attività viene trascurata, un progetto può soffrire di quello che viene chiamato \"Bugtracker Bloat\", che è essenzialmente l\'accumulo e la decomposizione dei ticket trascurati. Il triage aiuta anche a identificare i ticket duplicati che hanno la tendenza ad accumularsi, soprattutto se c\'è un problema irrisolto di lunga data di cui il team FC è ben consapevole ma non ha le risorse per qualsiasi motivo per risolverlo in quel momento.



## Come eseguire il triage 



### Stato del Ticket 

#### New

Per documenti MantisBTː {{ColoredText|Questo è lo stato di atterraggio per i nuovi problemi. I problemi rimangono in questo stato finché non vengono assegnati, riconosciuti, confermati o risolti. }}

In altre parole, lo stato **NEW** indica diverse coseː

1.  Il ticket non è stato confermato.
2.  Il ticket è ancora in corso, ovvero Triage/Sviluppatori stanno ancora valutando/chiarendo i dettagli del ticket dall\'OP.
3.  Il team di FreeCAD non ha ancora deciso cosa fare con questo ticket.

Tutti i [ticket di FreeCAD vengono aperti con lo stato **NEW**](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=10&hide_status=80).

#### Acknowledged

#### Feedback

I ticket vengono contrassegnati con questo stato quando all\'OP viene richiesto di fornire ulteriori informazioni.

Il ticket è in sospeso in base alla partecipazione di OP. Ad esempioː nel ticket mancano le informazioni sulla versione FC; o forse è richiesto un nome o una versione di una libreria di terze parti ecc \... Gli sviluppatori devono impostare questo stato ogni volta che rispondono a OP per indicare che il ticket è in sospeso. Questo è importante a causa della possibilità che OP trascuri di rispondere, il che ha un\'alta probabilità che il ticket \"marcisca\" nel tracker.

Quando l\'OP risponde, lo stato del ticket torna automaticamente a **Nuovo**. Quindi il ticket deve essere riesaminato per decidere cosa è necessario.

Ulteriori discussioni su questo argomento nel [forum di FreeCAD](https://forum.freecadweb.org/viewtopic.php?f=10&t=23005).

Tutti gli attuali [ticket FreeCAD aperti con stato **FEEDBACK**](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=20&hide_status=80) nel bugtracker FC.

#### Confirmed

Quando un ticket è confermato significa cheː

-   è un bug che è stato riprodotto
-   è una caratteristica che è stata approvata per essere considerata valida.

Ora è pronto per essere assegnato ad uno sviluppatore.

Tutti gli attuali [ticket FreeCAD aperti con lo stato **CONFIRMED**](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=40&hide_status=80) nel tracker FC.

#### Assigned

Autoesplicativo, questi sono i ticket che sono stati assegnati ad uno sviluppatore specifico.

Tutti i [ticket aperti di FreeCAD con lo stato **ASSIGNED**](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=50&hide_status=80) nel tracker FC.

#### Resolved

Questi ticket sono stati risolti ma non ancora chiusi, molto probabilmente perché necessitano di conferma che il ticket sia stato corretto.





### Risoluzione del ticket 

#### Open

Si spiega da sé, tutti i ticket rimangono \"aperti\" se sono ancora rilevanti a discrezione della squadra FC.

#### Fixed

Ticket che sono stati sistemati.

#### Unable to reproduce 

Ticket ritenuti non riproducibili.

#### Duplicate

Ticket che sono o hanno un ticket duplicato.

#### No change required 

Ticket dove è stato accertato che non sono necessarie modifiche.

#### Won\'t fix 

La squadra FC ha rifiutato la richiesta del ticket per un qualsiasi motivo indicato.

#### Not fixable 

#### Reopened

Ticket che sono stati chiusi ma che sono stati poi riaperti per un motivo rilevante. Molto probabilmente il problema si è ripresentato o non è stato completamente risolto.

#### Suspended

### Ticket Priority 

#### Immediatə

#### Urgent

#### High

#### Normal

#### Low

#### None

### Ticket Severity 

#### Block

#### Crash

#### Major

#### Minor

#### Tweak

#### Text

#### Trivial

#### Feature

## Tagging Tickets 

Una metodologia importante per tenere traccia dei ticket in base ad un determinato argomento/tema/categoria. È importante che vengano utilizzati **Tag esistenti** per taggare i problemi **prima** che vengano creati nuovi tag. Se vengono creati tag duplicati o superflui, l\'amministratore del bug tracker è responsabile della rimozione e, se possibile, ritaggare detti ticket.

## Pagine correlate 

[Bugtracker](Tracker/it.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Administration](Category_Administration.md) > Bug Triage/it
