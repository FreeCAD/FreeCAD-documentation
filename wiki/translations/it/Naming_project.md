# Naming project/it
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

Questo modello contiene le linea guida per il progetto di sviluppo di FreeCAD. Esso segue le regole della metodologia [Getting Things Done (GTD)](https://it.wikipedia.org/w/index.php?title=Getting_Things_Done). I progetti sono raccolti nel [Piano di sviluppo](Development_roadmap/it.md) (Development roadmap).

## Scopo e principi 

Si tratta di un lavoro di sviluppo e progettazione per implementare un sistema di denominazione topologica **robusta** (persistente e coerente) in FreeCAD.

Maggiori dettagli sulla denominazione topologica in **[Problema di denominazione topologica](Topological_naming_problem/it.md)**.

## Risultati

1.  **Interfaccia** in (Part::TopoShape) per referenziare in modo robusto le forme (nome) e le sotto-forme (facce, bordi, vertici) attraverso una stringa (nome dei sotto-elementi del tipo \"Face1\").
    Per fare questo bisogna fornire una interfaccia per Part::TopoShape con tutte le informazioni necessarie per produrre la Denimonazione (Naming), ad esempio, NewShape, con le informazioni addizionali di un algoritmo come le facce cancellate, i passaggi della modellazione (es. suddivisione in 2) e \...




1.  **Associazione** dei passaggi della modellazione con le facce o i bordi risultanti.
    Nel caso di un grande modello l\'utente si perde se ha a che fare con centinaia di raccordi o di fori. Per questo motivo, se le facce o i bordi ricordano quale fase della modellazione le ha create, è possibile implementare che un doppio click sul bordo o sulla faccia apra l\'operazione corrispondente!




1.  **Algoritmo** per mantenere coerente la denominazione nello storico della modellazione durante le modifiche, come la suddivisione di bordi o di facce e il movimento dei vertici
    ![](images/NamingExample.jpg )




1.  (opzional) **Ottimizzare la struttura dei dati in memoria** per mantenere in memoria solo le facce o i bordi modificati nelle operazioni di modellazione.
    Questo diventa importante quando i modelli diventano grandi. Non è efficace copiare la maggior parte della forma. E\' molto più efficace condividere le facce o i bordi rimasti invariati nelle operazioni (Features) e copiare solo quello che viene modificato.

## l'Ideazione

Si è discusso molto nel post [\"Robust Reference\"](http://forum.freecadweb.org/viewtopic.php?f=10&t=2656) di jrheinlaender.

### Altro

-   [Catia V5 Topology and Generic Naming](http://www.maruf.ca/files/caadoc/CAATopTechArticles/JournalMethodology.htm#Definition) e [Catia V5 Obiettivi della denominazione generica](http://www.maruf.ca/files/caadoc/CAAMmrTechArticles/CAAMmrGenericNaming.htm#Objectives%20of%20GN)

-   [Denominazione topologica in OCAF (Open CASCADE Applicazione Framework)](https://www.opencascade.com/doc/occt-7.4.0/overview/html/occt_user_guides__ocaf.html#occt_ocaf_5_6)

### Letteratura & documentazione 

-   J Kripac, \"Un meccanismo per la denominazione persistente di entità topologiche in modelli solidi parametrici basati sulla storia, Simposio sulla modellazione solida e le applicazioni 1995, p.21-30

\"

:   Descrive un metodo per realizzare i primi tre punti della lista. Direi che è l\'approccio utilizzato da Catia e OCC-TNaming. Almeno l\'interfaccia sembra la stessa. Il documento non è disponibile per essere scaricato. Ho dovuto comprarlo. Se qualcuno è interessato posso inviarlo via e-mail.

-   [Dago AGBODAN, David MARCHEIX e Guy PIERRA, \"Denominazione persistente per modelli parametrici, 2000\"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.29.2836&rep=rep1&type=pdf)

:   Approccio interessante via shell-grafica, affronta il quarto punto della lista per il riutilizzo delle facce o dei bordi non modificati.

-   [Duhwan Mun and Soonhung Han, \"Identification of Topological Entities and Naming Mapping for Parametric CAD Model Exchanges, INTERNATIONAL JOURNAL OF CAD/CAM, 2005, p 69-82\"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.106.3087&rep=rep1&type=pdf)

:   Panoramica molto buona e esempi

-   [Farjana, S.H., Han, S. \"Mechanisms of Persistent Identification of Topological Entities in CAD Systems: A Review\", Alexandria Engineering Journal, Volume 57, numero 4, dicembre 2018, pagine 2837-2849](https://research-management.mq.edu.au/ws/portalfiles/portal/100931773/Publisher_version_open_access_.pdf)

-   [Assembly Solving for Neutral Re-Imported Product Models Tahir A. Jauhar, Soonhung Han, Soonjo Kwon , p.108-123 , CAD Journal 2020, Volume 17 Numero 1](http://www.cad-journal.net/files/vol_17/CAD_17(1)_2020_108-123.pdf)

### Sintesi del lavoro fino ad oggi 

Questa è la sintesi del lavoro che è stato fatto per questo progetto fino al 13 giugno 2016:

-   jrheinlaender nel 2012 ha prodotto un sacco di codice basato essenzialmente sull\'ambiente Schizzo per risolvere il \"Riferimento Robusto\"
-   ickby ha provato a incorporare alcuni codici di jrheinlaender in FreeCAD moderno. [Questo post](http://forum.freecadweb.org/viewtopic.php?f=10&t=2656&start=60#p124844) ha un link al suo repo GitHub.
-   Nel 2016, ezzieyguywuf ha rianimato il progetto di jrheinlaender e, successivamente, ha iniziato il suo. E\' visibile [qui](http://forum.freecadweb.org/viewtopic.php?f=10&t=15847)
-   ezzieyguywuf ha messo a punto un programma di opencascade \"leggero\" per duplicare il problema della Denominazione Topologica e per testare le possibili soluzioni. Vedere il suo repo github [freecadTopoTesting freecadTopoTesting](https://github.com/ezzieyguywuf/freecadTopoTesting) qui
-   ezzieyguywuf ha incorporato il TNaming toolkit opencascade nel suo codice di test, e ha mostrato come questo potrebbe contribuire a risolvere alcuni dei problemi di Denominazione Topologica. Vedere il repo github
-   [Topological Naming](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming) repo github di realthunder
-   [Topological Naming Algorithm](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming-Algorithm) repo github di realthunder

## Organizzazione

### Informazioni su TNaming 

Vedere [qui](https://github.com/ezzieyguywuf/freecadTopoTesting/blob/master/TNaming_Writeup.md) per un dignitoso rapporto sul repo GitHub di ezzieyguywuf. Ecco alcuni punti salienti:

-   Il TNaming di opencascade si basa sul [TDF\_Data data framework](https://dev.opencascade.org/doc/occt-7.5.0/refman/html/class_t_d_f___reference.html#details).
-   TDF\_Data è un componente chiave dell\'OCAF di opencascade, ma può essere usato indipendentemente da esso
-   TDF\_Data è essenzialmente un albero in cui i dati vengono aggiunti e poi letti in un secondo momento
-   Ogni volta che un attributo TNaming\_NamedShape viene aggiunto ad un nodo dell\'albero TDF\_Data, un attributo TNaming\_UsedShapes viene aggiunto alla radice dell\'albero
    -   *\'NOTA:* questo attributo TNaming\_UsedShapes è fondamentale per l\'utilità del toolkit TNaming. Contiene una storia di tutti i TopoDS\_Shape usati durante la \'storia\' della parte
-   TNaming\_Builder è usato per aggiungere informazioni all\'albero TDF\_Data. Aggiunge un TNaming\_NamedShape ad un dato nodo dell\'albero, oltre ad aggiornare il database TNaming\_UsedShapes come necessario.
-   Ogni volta che il TopoDS\_Shape viene cambiato, deve essere registrato nella struttura TDF\_Data
    -   Di nuovo, TNaming\_Builder è usato per questo
    -   Vedi [qui](http://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__ocaf.html#occt_ocaf_5_6_1) nella documentazione di opencascade per una tabella che elenca cosa deve essere memorizzato nel database. **NOTA:** questa tabella sembra essere incompleta. Potrebbero essere necessari alcuni test aggiuntivi
    -   In breve, ogni volta che il TopoDS\_Shape viene modificato, ogni caratteristica modificata/generata/cancellata deve essere registrata. Per la maggior parte, dato che abbiamo a che fare con i solidi, questo significa che dobbiamo registrare le Faces modificate/generate/cancellate sul solido
-   La classe TNaming\_Selector è usata per \"selezionare\" una caratteristica che viene tracciata sull\'albero TDF\_Data
    -   Una caratteristica \"selezionata\" è una caratteristica a cui l\'algoritmo TNaming di opencascade manterrà un riferimento costante, indipendentemente dai cambiamenti topologici

## Azioni successive 

-   Definire il campo di applicazione
-   Testare in Python
-   Interfaccia in Part::TopoShape (+ legami con Python)

### Passi successivi (a partire dal 13 giugno 2016) 

1.  Determinare se opencascade TNaming toolkit risolve completamente il problema della Denominazione Topologica in FreeCAD
    -   Quali sono tutti i casi in cui la Denominazione Topologica è un problema?
    -   Quali sono gli scenari complessi in cui questo approccio dovrà lavorare?
2.  Incorporare il codice di TNaming in FreeCAD
    1.  Iniziare con un approccio essenziale, vale a dire creare un Cubo e un Cilindro, Fonderli, fare un Raccordo, e poi ridimensionare il cilindro. Il raccordo non deve muoversi
    2.  Gradualmente aggiungere ulteriori funzionalità
3.  Determinare se TNaming è la soluzione a lungo termine
4.  O se TNaming non è la soluzione a lungo termine, trovare un modo per \'serializzare / deserializzare\' i dati che TNaming utilizza per la persistenza tra le sessioni




[Category:Roadmap](Category:Roadmap.md)

---
[documentation index](../README.md) > [Roadmap](Category:Roadmap.md) > Naming project/it
