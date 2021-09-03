


<div class="mw-translate-fuzzy">

Alcune letture sulle unità di misura:

-   [Sistema Internazionale di Misura SI](http://it.wikipedia.org/wiki/Sistema_internazionale_di_unit%C3%A0_di_misura)
-   [Sistema imperiale britannico](http://it.wikipedia.org/wiki/Sistema_imperiale_britannico)
-   [SI derived unit](http://en.wikipedia.org/wiki/SI_derived_unit) (in italiano si trovano nella stessa pagina del SI)
-   [Grado d\'arco - Unità angolari](http://it.wikipedia.org/wiki/Grado_d%27arco)


</div>

## Esempi


```python
# -- some examples of the FreeCAD unit translation system --
# make a shortcut for the examples
pq = FreeCAD.Units.parseQuantity

# 10 meters in internal numbers
pq('10 m')

# doing math
pq('3/8 in')

# combined stuff
pq('100 km/h')

# transfer to other units
pq('100 km/h')/tu('m/s')

# derived units (Ohm)
pq('m^2*kg*s^-3*A^-2')

# or
pq('(m^2*kg)/(A^2*s^3)')

# angles 
pq('2*pi rad') # full circle

# as gon
pq('2*pi rad') / tu('gon')

# more imperial
tu('1ft (3+7/16)in')

# or 
pq('1\' (3+7/16)"') # the ' we have to escape because of python

# trigonometry
pq('sin(pi)')

# Using translated units as parameters, this command will create a 50.8mm x 20mm x 10mm box
b = Part.makeBox(pq('2in'), pq('2m')/100, 10)
```

## Unità di misura supportate 

Un elenco completo di tutte le unità supportate [si trova quì](Expressions/it#Unità.md).

## Finalità e principi: proposta di una estensione del sistema di gestione delle unità 

Nelle sezioni successive, sviluppando il concetto di *sistema di unità*, si propone un sistema di gestione delle unità di misura attivato nel corso dell\'esecuzione di una istanza di FreeCAD. Definire tale nuovo concetto offre il vantaggio di lavorare più facilmente con tanti tipi di unità **fisiche**, quante si vuole, anche con quelle create dall\'utente, senza aumentare la complessità di gestione delle unità, né per l\'utente, né per gli sviluppatori di FreeCAD.

In breve, gli eventi di scalatura delle unità sono localizzati con precisione, e realizzati in modo globale.

Il raggiungimento di tale flessibilità è necessario specialmente quando si passa a lavorare con le proprietà dei materiali che possono avere unità molto diverse e quindi difficili da gestire manualmente una ad una.

Il ragionamento proposto permette di gestire le unità come descritto nella [Guida per l\'uso del Sistema Internazionale delle unità di misura (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) e nel [Sistema internazionale delle unità di misura (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf), entrambi documenti del NIST.

In questa proposta, la prima analisi nella sezione [Riflessioni](Units/it#Riflessioni.md) riguarda i possibili contesti per i quali è utile la gestione delle unità.

Nella sezione [Organizzazione](Units/it#Organizzazione.md) è presentato il modello di dati prescelto per realizzare la gestione delle unità, sulla base di 3 oggetti, la *unità*, il *dizionario delle unità*, e il *sistema delle unità*. Infine, è anche presentata una breve API di un quarto oggetto chiamato *gestore delle unità*.

## Risultati

Grazie a questa estensione, si mira ad agevolare la scalatura della unità che può verificarsi tra i differenti settori di lavoro di una azienda. Ad esempio, i disegni tecnici possono essere realizzati nel sistema di unità standard, mentre la modellazione per elementi finiti può essere gestita in un sistema di unità più adatto per questo scopo.

Con questa estensione lo scambio di dati tra questi due tipi di attività diventa più facile.

## Riflessioni

In questa sezione sono evidenziati i contesti (casi) di uso del sistema di gestione delle unità. Partendo da questi contesti, dopo siamo in grado di definire le loro specifiche tecniche.

Essenzialmente sono considerati 2 contesti, come esempio.

### Contesto 1: apertura di un file di dati 

Questo caso probabilmente è quello più frequente. Si riceve un file contenente ad esempio un modello geometrico, o descrivente un materiale con un bel po\' di proprietà. Il modello geometrico è espresso in metri, oppure le proprietà del materiale sono espresse secondo il sistema internazionale di unità di misura.

Peccato \...

Sei un esperto di modellazione di elementi finiti (FE modelling), e di solito lavori con i millimetri per la lunghezza, megapascal per la pressione, tonnellate per la massa \...

In questo contesto, la gestione delle unità è necessaria per scalare i dati da un sistema di unità iniziale definito nel file di input a un diverso sistema di unità definito dall\'utente.

### Contesto 2: commutare il sistema di unità in fase di esecuzione 

In questo caso, si può essere allo stesso tempo, la persona che realizza un disegno, e anche chi gestirà la modellazione per elementi finiti. Analogamente al caso precedente, i sistemi di unità di misura per questi due lavori non sono gli stessi, ed è necessario cambiare il sistema di unità iniziale in quello preferito durante l\'esecuzione.

## Organizzazione

### Logica di scalatura delle unità 

Nella sezione [Riflessioni](Units/it#Riflessioni.md) sono stati presentati due contesti in merito a quando si utilizza la scalatura delle unità. Devono essere evidenziati alcuni aspetti di questi due contesti.


<div class="mw-translate-fuzzy">

#### Coerenza di unità in tutta l\'istanza in esecuzione in FreeCAD 

Il sistema proposto si basa su un assunto primario: l\'utente sta lavorando in un sistema di unità coerenti. Ad esempio, questo significa che, se l\'utente esprime la lunghezza in millimetri, necessariamente le aree saranno espresse in termini di millimetri quadrati e non in metri quadrati. Questa è la **Ipotesi numero uno**.


</div>

#### Sistema di unità 

In conseguenza della *Ipotesi numero uno*, è possibile e pertinente definire un sistema di unità. Un sistema di unità si applica a:

-   una istanza in esecuzione in FreeCAD su cui si sta lavorando
-   oppure si può anche applicare globalmente al contenuto di un file di input

Secondo la [Guida per l\'uso del Sistema Internazionale di unità di misura (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) del NIST, ci sono 7 unità fisiche di base. Abbiamo scelto di formulare un sistema di unità in termini di questi 7 unità di base.

Quando si lavora all\'interno di un\'istanza di FreeCAD, l\'utente deve quindi definire il sistema di unità base con cui sta lavorando prima di decidere di passare a un altro sistema di unità, o prima di importare dati da un file di input.

Questo sistema di unità si applica fino a che l\'utente non decide di cambiarlo. Se lo fà, tutti i dati con dimensioni vengono scalati.

Considerando l*\'Ipotesi numero uno*, si presume che tutti i dati che l\'utente inserirà manualmente in FreeCAD saranno coerenti con il sistema di unità prescelto.

Il vantaggio di lavorare con un *sistema di unità* definito a livello di un\'istanza in esecuzione in FreeCAD, o a livello di file di dati (al posto delle singole *unità* che sono definite a livello di dati) consiste nella notevole semplificazione della gestione delle unità.

Ecco alcuni esempi di sistemi di unità.

-   metro, kilogrammo, secondo, ampere, Kelvin, mole, candela
-   millimetro, tonnellata, millisecondo, ampere, Kelvin, mole, candela
-   millimetro, kilogrammo, millisecondo, ampere, Kelvin, mole, candela
-   \...

#### Unità di base e derivate 

Le Unità derivate sono create mediante la combinazione delle unità di base. Ad esempio, un\'accelerazione (m/s^2^) unisce contemporaneamente la lunghezza e il tempo. Un quadro interessante che presenta le relazioni tra le unità base e le unità derivate si può vedere in [questo documento](http://physics.nist.gov/cuu/pdf/SIDiagramColorAnnot.pdf), anche esso del NIST.

Grazie alla definizione del *sistema di unità*, l\'utente può lavorare con qualsiasi tipo di unità derivata, senza la necessità che gli sviluppatori di FreeCAD le prevedano prima.

#### Simboli delle unità base e delle derivate 

Secondo il [Sistema Internazionale delle unità di misura (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf), i simboli per specificare una unità sono ufficialmente approvati. Da questo possono essere evidenziate due conseguenze.

-   per un programma del computer non è facile lavorare con i simboli delle unità perché, per esempio, alcuni sono lettere greche. Quindi per un programma possono essere un po\' difficili da elaborare
-   anche se alcune unità (e i suoi simboli) possono essere ampiamente (normalmente) utilizzate, esse possono non essere approvate ufficialmente, come ad esempio l\'unità di tonnellata (si veda p32 del [Sistema Internazionale di unità di misura (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf))

Per superare queste limitazioni e rimanere flessibili, il sistema proposto privilegia l\'impiego di unità di grandezze (magnitudini) invece dei simboli di unità, che rimangono comunque disponibili per motivi di ergonomia.

### Modello dei dati 

Sono presentati i tre oggetti principali del sistema di gestione di unità di misura , vale a dire l*\'unità*, il *dizionario delle unità* e il *sistema di unità*.

#### Unità (unità di misura) 

Come premessa, è importante sottolineare che un oggetto *unità* di per sé indica solo una **dimensione** (grandezza fisica) come lunghezza, massa, tempo \... Esso non specifica una **grandezza** (unità di misura) come metro, millimetro, chilometri \... Questa ultima informazione è specificata attraverso il sistema di unità.

##### Dimensione (Grandezza fisica) 

Stringa obbligatoria che indica la *dimensione* (grandezza fisica) dell\'unità. La *dimensione* delle 7 unità di base (le 7 grandezze fisiche di base) sono indicate di seguito (dalla [Guide for the Use of the International System of Units (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf)) (Guida per l\'uso del Sistema Internazionale di unità di misura).

-   LENGTH - LUNGHEZZA
-   MASS - MASSA
-   TIME - TEMPO
-   ELECTRIC CURRENT - CORRENTE ELETTRICA
-   THERMODYNAMIC TEMPERATURE - TEMPERATURA TERMODINAMICA
-   AMOUNT OF SUBSTANCE - QUANTITA\' DI SOSTANZA
-   LUMINOUS INTENSITY - INTENSITA\' LUMINOSA

L\'attributo *Dimension* permette di identificare l\'unità. Due unità non possono condividere la stessa *dimensione*.

##### Firma (Identificazione della grandezza fisica) 

E\' un gruppo di 7 cifre intere obbligatorie (numero delle unità di misura di base) che definisce di quale unità si tratta. La firma delle 7 unità di base sono:

-   LENGTH - LUNGHEZZA: \[1,0,0,0,0,0,0\]
-   MASS - MASSA: \[0,1,0,0,0,0,0\]
-   TIME - TEMPO: \[0,0,1,0,0,0,0\]
-   ELECTRIC CURRENT - CORRENTE ELETTRICA: \[0,0,0,1,0,0,0\]
-   THERMODYNAMIC TEMPERATURE - TEMPERATURA TERMODINAMICA: \[0,0,0,0,1,0,0\]
-   AMOUNT OF SUBSTANCE - QUANTITA\' DI SOSTANZA: \[0,0,0,0,0,1,0\]
-   LUMINOUS INTENSITY - INTENSITA\' LUMINOSA: \[0,0,0,0,0,0,1\]

Con queste 7 unità siamo poi in grado di esprimere tutte le unità di misura derivate definite nella [Guida per l\'uso del Sistema Internazionale di unità di misura (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) e anche di crearne di nuove secondo le esigenze personali, quali ad esempio:

-   MASS DENSITY - DENSITA\' : \[-3,1,0,0,0,0,0\]
-   AREA - AREA: \[0,2,0,0,0,0,0\]

*Signature* è l\'attributo grazie al quale la scalatura delle unità può essere realizzata in modo generale.

##### Simboli

Insieme di \[numero reale, stringa\] (rappresentante \[*grandezza*, *simbolo*\]) che elenca tutti i *simboli* noti a FreeCAD. Grazie a questo insieme, l\'API di scalatura delle unità diventa più ergonomica perché i *simboli* sono collegati alle *grandezze* correlate .

Questo insieme (array) può essere esteso quanto necessario.

Ad esempio, la lista dei *simboli* della unità di misura di lunghezza, e le loro relative *grandezze* è:

 [1e+12,"Tm"],[1e+09,"Gm"],[1e+06,"Mm"],
[1e+03,"km"],[1e+02,"hm"],[1e+01,"dam"],
[1e+00,"m"],[1e-01,"dm"],[1e-02,"cm"],
[1e-03,"mm"],[1e-06,"µm"],[1e-09,"nm"],
[1e-12,"pm"],[1e-15,"fm"]

I *simboli* standard possono essere trovati sul [sito web del NIST](http://physics.nist.gov/cuu/Units/units.html) e da pag. 26 a pag. 23 e a pag. 32 (*tonnellata metrica o tonnellata*) di [The International System of Units (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf).

#### Dizionario delle unità 

Tutte le unità di misura disponibili in FreeCAD, e anche quelle nuove create dall\'utente, devono essere conservate nel *dizionario delle unità*, che è un file XML (file di configurazione di FreeCAD), in modo da poter essere recuperate quando è necessario, ad esempio quando si realizza la scalatura delle unità.

##### Unità

Insieme delle unità, contenute nel *dizionario delle unità*.

#### Unit system 

Un *sistema di unità* è l\'oggetto che permette all\'utente di definire la *grandezza* dell\'unità corrente di ciascuna delle unità di base con cui si sta lavorando. Ad esempio, sapendo che l\'utente sta lavorando con i millimetri, le tonnellate e i secondi, grazie all\'utilizzo di un sistema di unità, FreeCAD può sapere che l\'energia è espressa in termini di milliJoule, la forza in termini di Newton, e la pressione in termini di MegaPascal. Quindi un sistema di unità è definito solo da un *nome* (ad esempio *Sistema di unità standard*) e da una *tabella di grandezza* specifica per ciascuna delle unità di base 7, che è la sua grandezza corrispondente.

##### Nome

Stringa che permette all\'utente di identificare il sistema di unità.

##### Grandezze

Specificando la grandezza delle 7 unità di base si definisce un sistema di unità.

Ad esempio \[1e-03, 1e+03, 1, 1, 1, 1, 1\], significa millimetri, tonnellata, secondo, ampere, Kelvin, mole, candela

#### API di gestione di unità 

E\' presentata solo la logica di alcuni metodi, per evidenziare alcune caratteristiche. Questi metodi potrebbero appartenere a un oggetto chiamato *Gestore di unità*.

##### Verifica del dizionario delle unità 

###### isValid - Validità 

Il dizionario delle unità può essere un file XML (file di configurazione di FreeCAD). Esso contiene la lista delle unità definite. Tale dizionario è necessario affinchè il sistema di gestione dell\'unità proposto funzioni.

Deve soddisfare alcune condizioni che devono essere controllate prima di attivare il sistema di gestione dell\'unità. Queste condizioni sono:

-   verificare che tutte le unità di base siano definite
-   verificare che una *dimensione* non sia definita due volte tramite le unità
-   verificare in tutti i simboli esistenti che un *simbolo* non sia definito due volte
-   verificare che le *firme* di tutte le unità abbiano tutte la stessa dimensione
-   verificare che per tutte le unità sia definito un *simbolo standard* (per cui la *grandezza* è 1)

###### isCompatibleWithThisSignature - Compatibilità 

Un dizionario di unità definisce un insieme di unità e le loro grandezze note. Quando si gestisce una unità, è opportuno controllare che la sua firma sia compatibile con l\'insieme di unità registrate nel dizionario di unità, in modo da elaborarla. Questo controllo comprende:

-   verificare che la lunghezza della *firma* da inserire sia della stessa dimensione delle *firme* del dizionario di unità

##### Scalare le unità 

###### scaleUnitFromSymbolToSymbol

Conoscendo un valore, l\'unità iniziale tramite il suo simbolo e l\'unità di destinazione tramite il suo simbolo, scalare il valore.

###### scaleUnitFromSymbolToUnitSystem

Conoscendo un valore, l\'unità iniziale tramite il suo simbolo e il sistema di unità di destinazione, scalare il valore.

###### scaleUnitFromUnitSystemToSymbol

Conoscendo un valore, un sistema di unità iniziale, l\'unità di destinazione tramite il suo simbolo, scalare il valore.

#### Le motivazioni per una tale gestione: esempio di applicazione 

Supponiamo di accingerci a creare un modello di elementi finiti. Per costruire il nostro modello, abbiamo bisogno della griglia (forma mesh), delle proprietà del materiale ed è necessario definire i parametri numerici. Considerando che possono esserci decine di proprietà dei materiali da gestire, espresse con diverse unità e a volte non sempre molto comuni, per l\'utente è importante dover solo indicare un sistema globale di unità, senza altre preoccupazioni.

Poi FreeCAD farebbe lui il lavoro.

Per gli sviluppatori e gli utenti di FreeCAD non è necessario conoscere tutte le unità che possono essere definite nei file delle proprietà del materiale, è utile fare affidamento su un sistema generico.

Supponiamo che in un file abbiamo un buon numero di proprietà dei materiali esotiche espresse con unità esotiche, e che vogliamo lavorare in un sistema di unità specifico.

Con l\'estensione proposta è facile scalare qualsiasi di queste proprietà conoscendo la loro firma, la grandezza e il sistema di unità di destinazione.

Per ciascuna delle proprietà, la scalatura si ottiene moltiplicando il valore iniziale della proprietà per il fattore $\frac{Grandezzainiziale}{Grandezzafinale}$.

La *Grandezza finale* viene ottenuta semplicemente con l\'operazione $\prod_{bu} targetMagnitude_{bu}^{signature_{bu}}$, dove *bu* stà per *unità di base*.

Diventa così molto facile gestire un numero qualsiasi di unità con qualsiasi tipo di unità tramite poche righe di Python.


<div class="mw-translate-fuzzy">

## Prossime azioni 

-   Implementing Quantity and Unit classes (mostly done)
-   Implementing InputField as User front end (in progress)
-   UnitsCalculator as test bed (in progress)
-   [Quantity](Quantity/it.md) documentation (in progress)
-   [UnitsCalculator](Std_UnitsCalculator/it.md) documentation
-   Update Material framework to work only with Quantities
-   Test Cases


</div>

-   The [Expressions](Expressions#Units.md) page for a list of all known units.
-   The documentation of [Quantity](Quantity.md).
-   The [Std UnitsCalculator](Std_UnitsCalculator.md) tool.


{{Powerdocnavi

}} 
