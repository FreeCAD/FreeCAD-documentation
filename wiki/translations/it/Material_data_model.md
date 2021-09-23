# Material data model/it
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

## Finalità e principi 

Per memorizzare le proprietà dei materiali in una struttura di dati unificata. Uno degli scopi è quello di facilitare il recupero dei dati che può essere effettuato in diversi contesti:

-   quando si costruisce un modello di elemento finito
-   quando si renderizza un modello 3D
-   per essere in grado di seguire i cambiamenti nel materiale di un *componente* realizzato in FreeCAD, per applicazioni [PDM](http://en.wikipedia.org/wiki/Product_Data_Management),
-   applicazioni BIM (architettura e edilizia)

Per gestire le proprietà dei materiali, si propone di creare un modello di dati specifico da istanziare (replicare) quando viene creato un nuovo materiale all\'interno di FreeCAD.

Esso renderà possibile creare un materiale definendo a mano le sue proprietà mediante un *Ambiente dei materiali*, oppure leggendo le proprietà dei materiali in un file. I formati di questi file sono da definire (alcuni esistono già, come MatML, STEP AP235 e IGR45 \...).

Inoltre, sarà possibile salvare le proprietà del materiale in una collezione di file in un formato che ancora deve essere scelto. I file potranno essere memorizzati in una directory comune e formare il database dei materiali di FreeCAD.

Tramite questo modello di dati, i materiali possono essere definiti in FreeCAD senza la necessità di definire un *componente*.

Nel modello dei dati del *componente* verrà creato un nuovo puntatore, per collegarlo ad un materiale che è stato definito tramite il modello di dati dei materiali.

## Risultati

Tramite questo modello di dati dei materiali, si propone di offrire uno strumento per gestire facilmente i dati dei materiale all\'interno di FreeCAD.

## Riflessioni

## Organizzazione

Per descrivere un materiale devono essere gestiti diversi tipi di dati. Più avanti viene proposto un modello di dati dei materiali. Sono anche forniti alcuni esempi dei dati che possono essere memorizzati all\'interno di questa struttura.

### Modello di dati dei materiali 

Oltre alle classiche \"stringhe\" di attributi quali il nome e la famiglia, per descrivere un materiale in FreeCAD, devono essere gestiti 3 diversi tipi specifici di informazioni.

-   proprietà: struttura generica per memorizzare i dati che descrivono le proprietà ingegneristiche (proprietà fisiche) del materiale
-   composizione chimica: composizione chimica del materiale
-   aspetto: le informazioni che descrivono come sarà mostrato il materiale in FreeCAD (colore, brillantezza \...)

Affinchè il materiale esista, non è necessario che tutti questi tipi di informazioni siano definiti.

Infine, di seguito è mostrato l\'elenco degli attributi salvaguardati per descrivere un materiale in FreeCAD.

#### Nome

Una stringa che indica il nome del materiale. È la sua designazione.

#### Famiglia

Una stringa che indica la famiglia del materiale, quali ad esempio:

-   metallico
-   plastico
-   \...

Addizionalmente, si propone di creare una mappa tra le famiglie (ad esempio memorizzata in un file XML) in modo da poter sfogliare il database dei materiali di FreeCAD.

Tale mappa potrebbe ad esempio contenere un albero che presenta le relazioni tra famiglie, come:

-   metallo -\> acciaio -\> acciaio al carbonio -\> acciaio ad alta resistenza
-   metallo -\> alluminio -\> alluminio pressofuso

#### Produttore

Una stringa che indica il produttore del materiale.

#### URL

Una stringa che indica la pagina web dove è presentato il materiale.

#### Proprietà

##### Descrizione

Il modello di dati dei materiali comprende un insieme di proprietà. La dimensione di detta raccolta non è fissa e può essere estesa con nuove proprietà definite dall\'utente.

Una proprietà contiene i seguenti attributi.

-   name: stringa
-   symbol: stringa per scrivere il simbolo delle proprietà (in formato matematico Latex?)
-   type: \"scalare\" o \"matrice\"
-   value: scalare (se è uno scalare)
-   values: matrice (se è una matrice)
-   parameterNames: matrice di stringhe (per le proprietà di tipo \"matrice\")
-   parameterValues: matrice di scalari (per le proprietà di tipo \"matrice\")
-   unit & unitMagnitude (oggetto specifico descritto in [Unità](Units/it.md)) (Notare che: alcuni esempi includono unitMagnitude, mentre io non sono del tutto sicuro che questo debba essere definito a livello di proprietà. Il sistema di unità deve essere definito a livello materiale.)
-   direction: un vettore che indica la direzione in cui si intende il valore della proprietà. Il vettore stesso è un oggetto di FreeCAD espresso nel sistema di coordinate globale o in un sistema di coordinate definito dall\'utente
-   notes: stringa che può essere usata per descrivere meglio la proprietà come per esempio cosa significa, come si misura \... Può anche aiutare a capire il nome della proprietà

Le proprietà dei materiali saranno identificate grazie al loro nome, al fine di elaborarle, ad esempio per scrivere il limite di snervamento in un modello di elementi finiti. Al fine di agevolare la creazione dei dati dei materiale all\'interno di FreeCAD, sarà proposto all\'utente un elenco standard di nomi di proprietà con le loro unità standard. Tuttavia, l\'utente è libero di creare nuove proprietà, con nuovi nomi, nuove unità, e così via \...

Di seguito si propone il dizionario delle proprietà standard. Sentitevi liberi di aggiungerne di nuove.


<?xml version="1.0" encoding="UTF-8"?>



  
        
     








Note: \"Il coefficiente Lankford è rappresentativo della anisotropia di un laminato metallico sottile, è chiamato anche valore Lankford, R-valore, o rapporto di deformazione plastica .\" \"Il coefficiente Hardening (Incrudimento) è rappresentativo della capacità di incrudimento di un metallo. Appare nella formula di Hollomon che mette in relazione la deformazione plastica cumulata con lo stress.\"

##### Esempio 1: Costo per tonnellata 

Di seguito è riportato un primo esempio per mostrare come può essere memorizzata la proprietà *Cost per tonne* (Costo per tonnellata).

-   name: Cost per tonne
-   symbol: not applicable
-   type: scalar
-   value: 500
-   values: not applicable (ma potrebbe esserlo: per esempio i differenti valori di costo per i diversi paesi)
-   parameterNames: not applicable (ma potrebbe esserlo: per esempio i differenti valori di costo per i diversi paesi)
-   parameterValues: not applicable (ma potrebbe esserlo: per esempio i differenti valori di costo per i diversi paesi)
-   parameterUnits: not applicable
-   unit & unitMagnitude: \[\[ 0, -3, 0, 0, 0, 0, 0\], 1\]
    -   meaning m\^(-3) (maggiori dettagli sulle unità e sulle specifiche del sistema di unità nella pagina [Unità](Units/it.md))
-   direction: not applicable

##### Esempio 2: Limite di elasticità 

Sotto è riportato un secondo esempio per mostrare come può essere memorizzata la proprietà *Yield stress* (Limite di elasticità).

-   name: Yield stress
-   symbol: YS
-   type: scalar
-   value: 450
-   values: not applicable
-   parameterNames: not applicable
-   parameterValues: not applicable
-   parameterUnits: not applicable
-   unit & unitMagnitude: \[\[ -1, 1, -2, 0, 0, 0, 0\], 1\]
    -   significato di: Pa (maggiori dettagli sulle unità e sulle specifiche del sistema di unità nella pagina [Unità](Units/it.md))
-   direction: \[ 1, 0, 0\] nel sistema di coordinate globale
    -   data una lastra di acciaio, questo significa che il limite di snervamento dato è espresso in direzione x, che può essere per esempio la direzione di rotolamento

##### Esempio 3: Incrudimento 

Sotto è riportato un terzo esempio per mostrare come può essere memorizzata la proprietà *Strain hardening* (Incrudimento). Questo è un esempio più complesso perché l\'incrudimento è rappresentato da una serie di curve. Le curve rappresentano l\'evoluzione dello stress rispetto alla deformazione plastica. Sono state ottenute 3 curve con diverse velocità di deformazione. Tutte le curve sono state ottenute a temperatura ambiente.

-   name: Strain hardening
-   symbol: not applicable
-   type: scalar
-   value: not applicable
-   values: \[\[0., 100, 150, 200\], \[ 0., 120, 180, 210\], \[ 0., 140, 190, 220\]\]
-   parameterNames: \[Plastic strain, Strain rate, Temperature\]
-   parameterValues:
    -   Il primo gruppo dei tre insiemi (array) rappresenta le evoluzioni della deformazione plastica
    -   La seconda serie di tre array rappresenta l\'evoluzione dei tassi di deformazione. In ciascuna delle matrici è dato un singolo valore , questo significa che la velocità di deformazione non cambia per ciascuna delle evoluzioni di tensione corrispondente.
    -   La serie finale composta da un singolo array rappresenta l\'evoluzione della temperatura. Questa volta viene scritto un singolo valore in una singola matrice, il che significa che la temperatura non cambia per un determinato array di stress, e questo vale per tutte le matrici di stress.

\[\[\[0. , 0.4, 0.8, 1\], \[ 0, 0.4, 0.8, 1\], \[ 0, 0.4, 0.8, 1\]\],

\[\[0.\] , \[100\] , \[1000.\] \],

\[\[18.\] \],\]

-   parameterUnits & parameterUnitMagnitudes: \[\[\[ 0, 0, 0, 0, 0, 0, 0\], 1\], \[\[ 0, 0, -1, 0, 0, 0, 0\], 1\], \[\[ 0, 0, 0, 0, 1, 0, 0\], 1\]\]
    -   significatio di: nessuna, s\^(-1) e K (maggiori dettagli sulle unità e sulle specifiche del sistema di unità nella pagina [Unità](Units/it.md))
-   unit & unitMagnitude: \[\[ -1, 1, -2, 0, 0, 0, 0\], 1\]
    -   significato di: Pa (maggiori dettagli sulle unità e sulle specifiche del sistema di unità nella pagina [Unità](Units/it.md))
-   direction: not applicable

#### Composizione chimica 

\[Yet to be filled up\]

#### Aspetto

\[Yet to be filled up\]

#### Note

Una stringa in cui l\'utente può aggiungere le proprie osservazioni sul materiale.

### Applicazioni del modello di dati dei materiali: alcuni esempi 

##### Esempio 1: Muratura in mattoni 

###### Nome 

Brick masonry (Muratura in mattoni)

###### Famiglia 

?stringa?

###### Proprietà 

-   *Weight*: 1kg/m³
-   *Cost per cubic meter*: 1€/m³
-   *Number of bricks por base unit*: ?float?
-   *Volume of mortar por base unit*: ?float?
-   *Mortar type*: ?string?
-   *Brick type*: ?string?
-   *Fire resistance class*: ?string?
-   *Thermal conductivity*: 1 W/mK

###### Produttore 

?stringa?

###### URL 

?stringa?

###### Note 

Note sulla manutenzione, cura particolare da adottare, ecc ..

Codice CSI/MasterFormat (dato che nel settore sono utilizzati diversi sistemi per dare a tutto il materiale un codice speciale, propongo di inserirlo nelle note, perché non mi sembra opportuno creare una proprietà specifica che non siamo in grado di nominare con precisione).

## Azioni successive 

-   Definire un set di nomi per le proprietà classiche, che possiamo definire in un dizionario (file di configurazione FreeCAD). Queste proprietà saranno soprattutto riutilizzate in altri contesti, quali il modulo FEM.

-   Compilare la sezione *Composizione chimica*.
-   Compilare la sezione *Aspetto*.

-   Definire un insieme di componenti chimici di default.

-   Revisione da parte di altre persone.

-   Implementare in C++ il modello di dati e la capacità di scrivere e leggere in un file (ISO 10303-45 tramite SCL?).
-   Implementare dizionari XML per archiviare le proprietà predefinite, con le loro unità, che possono essere utilizzati dall\'utente.
-   Implementare la GUI Python per gestire questi dati.



[Category:Roadmap](Category:Roadmap.md)

---
[documentation index](../README.md) > [Material](Material_Workbench.md) > Material data model/it
