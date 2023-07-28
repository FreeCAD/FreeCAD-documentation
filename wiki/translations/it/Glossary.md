# Glossary/it
Questa pagina è un glossario dei termini e delle definizioni comuni in FreeCAD.

Vai alla lettera: {{CompactTOC|center=yes}}

## 0-9


{{gloss}}


{{term|3D view|content=[3D view](3D_view.md)}}


{{defn|defn=La vista 3D è un componente della [interfaccia](Interface/it.md) di FreeCAD. Mostra una rappresentazione 3D del modello.}}


{{glossend}}

## A


{{gloss}}


{{term|term=Arc}}


{{defn|defn=Una porzione o segmento di un cerchio.}}


{{term|term=Arch|content=[Arch](Arch_Workbench/it.md)}}


{{defn|defn=Abbreviazione di [Architectural Workbench](#Workbench.md) un ambiente di lavoro utilizzato principalmente per la modellazione di edifici e di strutture. Strettamente correlato all'ambiente [Draft](#Draft.md).}}


{{term|term=Assembly}}


{{defn|no=1|defn=Un insieme di [Part](#Part.md) che hanno posizioni definite l'una rispetto all'altra.}}


{{defn|no=2|defn=Un [workbench](#Workbench.md) che mira a facilitare la creazione di assiemi. È attualmente in fase di sviluppo e non fa ancora parte di FreeCAD.}}


{{term|term=Axis}}


{{defn|defn=Una linea immaginaria che attraversa l'origine dello spazio di lavoro. Ci sono 3 assi normali. Hanno i nomi classici di X, Y e Z. X è da un lato all'altro. Y è su e giù. Z è dentro e fuori dalla pagina/schermo.}}


{{glossend}}

## B


{{gloss}}


{{term|Backtrace}}


{{defn|defn=Output di un programma di debug che visualizza la serie di istruzioni eseguite da FreeCAD prima che si sia verificato un problema.}}


{{term|Bezier Curve|content=[http://en.wikipedia.org/wiki/B%C3%A9zier_curve Curva di Bezier]}}


{{defn|defn=Un tipo di curva parametrica.}}


{{term|Blueprint}}


{{defn|defn=Vecchio termine usato per [Drawing](#Drawing.md), e coniato per il [http://en.wikipedia.org/wiki/Blueprint processo di riproduzione] di un originale.}}


{{term|Body}}


{{defn|defn=Un tipo di contenitore utilizzato nel [Workbench](#Workbench.md) [PartDesign](PartDesign_Workbench/it.md) che raggruppa sequenze di operazioni di  ([Sketch](#Sketch.md), geometrie di costruzione e [Features](#Feature.md)) per creare un unico solido contiguo. (Introdotto in FreeCAD V0.17.)}}


{{term|Boolean Logic}}


{{defn|defn=Un metodo di manipolazione dei dati utilizzando gli operandi: And, Or, Not.}}


{{term|Boolean Operation}}


{{defn|defn=Un metodo per manipolare gli oggetti utilizzando la logica booleana. In FreeCAD, le operazioni booleane sono: Unione ([Fuse](#Fuse.md)), Differenza ([Cut](#Cut.md)), Intersezione e Sezione.}}


{{term|Boolean OPerations check}}


{{defn|defn=Vedere [BOPcheck](#BOPcheck.md).}}


{{term|BOPcheck}}


{{defn|defn=Un'impostazione che consente agli strumenti Verifica Geometria in Part WB e OpenSCAD WB di controllare anche la geometria creata dalla [Boolean Logic](#Boolean_Logic.md). L'impostazione predefinita Verifica Geometria per BOPcheck è "false" (o disattivata). L'utente può abilitare BOPcheck per fornire una maggiore precisione durante l'esecuzione dello strumento Check Geometry, ma ciò va a discapito di tempi di elaborazione Check Geometry più lunghi. A partire da FreeCAD 0.19, l'impostazione BOPcheck è abilitata più facilmente dalla parte Impostazioni del widget Controlla geometria.}}


{{term|brep}}


{{defn|defn=Formato di file nativo per [Open CASCADE](#Open_CASCADE.md) e condiviso da alcune applicazioni. FreeCAD può salvare in formato *.brep.}}


{{term|B-rep}}


{{defn|defn=Sta per [http://en.wikipedia.org/wiki/B-rep Boundary representation], che è uno dei due tipi di modelli 3D supportati da FreeCAD (l'altro è [Mesh](#Mesh.md)).}}


{{term|B-spline}}


{{defn|defn=Un tipo di curva parametrica. Vedi [http://en.wikipedia.org/wiki/B-spline B-spline]}}


{{glossend}}

## C


{{gloss}}


{{term|Callout}}


{{defn|defn=Stringa di testo collegata a una linea che punta a un oggetto in un [Drawing](#Drawing.md).}}


{{term|Chamfer}}


{{defn|defn=Il taglio di un bordo, ad angolo, per eliminare il suo spigolo; un bordo smussato.}}


{{term|Clipping Plane}}


{{defn|defn=Il piano di taglio viene utilizzato per tagliare il modello nella vista 3D. È solo un aiuto visivo e in realtà non taglia il modello.}}


{{term|Clone}}


{{defn|defn=Una copia di un oggetto con cui la copia rimane parametrica. Quando l'oggetto originale viene modificato, anche i cloni cambiano per mostrare le modifiche apportate all'oggetto originale.}}


{{term|Coin}}


{{defn|defn=Detto anche Coin3D. Libreria software di terze parti utilizzata per la rappresentazione 3D da FreeCAD.}}


{{term|COLLADA}}


{{defn|defn=Un formato file di interscambio per i modelli [Mesh](#Mesh.md). L'estensione del file è *.dae.}}


{{term|Command|content=[Command](Command/it.md)}}


{{defn|defn=Un'azione richiamata dalla [GUI](#GUI.md) quando si preme un pulsante della barra degli strumenti o si digita una scorciatoia da tastiera o si digita nella console Python.}}


{{term|Compound}}


{{defn|defn=Raggruppa gli oggetti insieme senza fonderli come farebbe un'[Boolean Operation](#Boolean_Operation.md).}}


{{term|CompSolid}}


{{defn|defn=Insieme di [Solid](#Solid.md) collegati dalle loro [Face](#Face.md). I CompSolid sono necessari in [FEM](#FEM.md), dove più di un materiale viene utilizzato in una mesh FEM.}}


{{term|Constraint}}


{{defn|defn=Una restrizione sulla relazione geometrica tra le primitive in uno [Sketch](#Sketch.md). Se un vincolo ha un valore numerico, viene indicato come Datum (ad esempio, un vincolo di distanza ha un valore numerico - la lunghezza di una linea immaginaria che collega i due punti). Un vincolo che non ha valore numerico (ad esempio un vincolo orizzontale) viene talvolta definito vincolo geometrico.}}


{{term|Constructive Solid Geometry|content=[http://en.wikipedia.org/wiki/Constructive_solid_geometry Constructive Solid Geometry]}}


{{defn|defn=Un metodo di modellazione solida per creare forme utilizzando [Boolean Operation](#Boolean_Operation.md) su [Primitive](#Primitive.md).}}


{{term|Coordinate}}


{{defn|defn=Un numero che definisce la posizione di un oggetto nello spazio in riferimento a un [http://en.wikipedia.org/wiki/Cartesian_coordinate_system sistema di coordinate].}}


{{term|Coplanar}}


{{defn|defn=Esistente sullo stesso piano.}}


{{term|CSG}}


{{defn|defn=Abbreviazione di [Constructive Solid Geometry](#Constructive_Solid_Geometry.md).}}


{{term|Cut}}


{{defn|defn=Applicazione di una [Boolean Operation](#Boolean_Operation.md) tra le forme.}}


{{glossend}}

## D


{{gloss}}


{{term|DAG}}


{{defn|defn=Vedere [Directed Acyclic Graph.](#Directed_Acyclic_Graph.md)}}


{{term|Degrees Of Freedom}}


{{defn|defn=Il numero di modi in cui la geometria in uno [Sketch](#Sketch.md) può variare. Ad esempio, se abbiamo uno schizzo costituito da un solo punto e al punto non sono applicati [Constraint](#Constraint.md), il punto ha due [DOF](#DOF.md) perché è libero di spostarsi verticalmente e orizzontalmente. Allo stesso modo, uno schizzo costituito da un solo cerchio non vincolato ha tre [DOF](#DOF.md) perché il cerchio può spostarsi verticalmente e orizzontalmente e, inoltre, il raggio non è definito. È buona norma vincolare uno schizzo fino a quando non ha alcun [DOF](#DOF.md) rimanente, nel qual caso si dice che è [Fully Constrained](#Fully_Constrained.md).}}


{{term|Dependency Graph}}


{{defn|defn=Uno strumento grafico di terze parti utilizzato per mostrare come gli oggetti in un modello di FreeCAD utilizzano o sono correlati tra loro. Per ulteriori informazioni, fare riferimento alla pagina wiki [Grafico delle dipendenze](Std_DependencyGraph/it.md).}}


{{term|Difference}}


{{defn|no=1|defn=Il risultato o il resto di una sottrazione.}}


{{defn|no=2|defn=Una [Boolean Operation](#Boolean_Operation.md) in [Part](Part_Workbench/it.md) [workbench](#Workbench.md) che viene utilizzata per sottrarre una geometria da un'altra; risulta in un [Cut](#Cut.md).}}


{{term|Directed Acyclic Graph}}

(abbreviato come \"DAG\") {{defn|defn=Un tipo di [Dependency Graph](#Dependency_Graph.md) in cui la relazione degli oggetti scorre in una direzione generalmente lineare dall'inizio alla fine senza dipendenze circolari. Quando si segue un DAG non c'è flusso da un oggetto A a nessun altro oggetto e poi di nuovo allo stesso oggetto A. In FreeCAD, un grafico del modello deve essere sempre un DAG.}} {{term|DOF}} {{defn|defn=[Degrees Of Freedom](#Degrees_Of_Freedom.md)}} {{term|Draft|content=[Draft](Draft_Workbench/it.md)}} {{defn|no=1|defn=Un [Workbench](#Workbench.md) di FreeCAD utilizzato principalmente per lavori bidimensionali.}} {{defn|no=2|defn=Un angolo di sformo su uno stampo per consentire la rimozione del prodotto finito. Vedere [PartDesign](PartDesign_Draft/it.md).}} {{term|Drawing}} {{defn|defn=Descrive una rappresentazione della geometria attraverso l'uso di viste bidimensionali. Chiamato anche piano o [Blueprint](#Blueprint.md).}} {{glossend}}

## E


{{gloss}}


{{term|Edge}}


{{defn|no=1|defn=Un segmento che unisce due [Vertices](#Vertices.md). Questo segmento può essere una linea retta o una curva. Il kernel CAD lo definisce come: Forma unidimensionale corrispondente a una curva e delimitata da un vertice a ciascuna estremità. Un cerchio chiuso ha quindi un solo vertice, dove inizia e dove finisce. Vedere [https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3 "Open CASCADE Technology, Profile: Defining the Topology"].}}


{{defn|no=2|defn=La linea di congiunzione tra due facce. Può essere curva o dritta.}}


{{term|Element}}


{{defn|defn=Un elemento della geometria di Sketcher come un punto, un segmento di linea, un arco, un cerchio, ecc.}}


{{term|Expression}}


{{defn|no=1|defn=Termine generico utilizzato in matematica e in programmazione.}}


{{defn|no=2|defn=In FreeCAD le [espressioni](Expressions/it.md) sono utilizzate per calcolare i valori. Possono fare riferimento e guidare le proprietà degli oggetti. Sono utilizzati in [fogli di calcolo](Spreadsheet_Workbench/it.md) e per controllare i modelli parametrici.}}


{{term|Extrude}}


{{defn|defn=Un termine generale per estendere un oggetto 2D in 3D lungo una direzione. Vedi anche [Pad](#Pad.md).}}


{{glossend}}

## F


{{gloss}}


{{term|Face}}


{{defn|defn=Un costrutto topologico bidimensionale. Ad esempio, un cubo ha 6 facce. Una faccia può essere curva, come nel caso di una sfera, che in FreeCAD ha una sola faccia. Il kernel CAD la definisce come: Parte di una superficie delimitata da un [Wire](#Wire.md) chiuso. Vedere [https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3 Profile: Defining the Topology].}}


{{term|Facet}}


{{defn|defn=Spesso usato per descrivere facce planari su una [Mesh](#Mesh.md).}}


{{term|FC}}


{{defn|defn=Abbreviazione di FreeCAD.}}


{{term|FCStd}}


{{defn|defn=Formato di file nativo di FreeCAD. Estensione file *.fcstd, *.FCStd}}


{{term|Feature}}


{{defn|defn=Un passo nell'evoluzione di una parte 3D nel flusso di lavoro [Part Design](PartDesign_Workbench/it.md) [Workbench](#Workbench.md). Esempi sono [Pad](#Pad.md), [Pocket](#Pocket.md), [Groove](#Groove.md), [Fillet](#Fillet.md), ecc. Mentre creiamo un modello in [Part Design](PartDesign_Workbench/it.md) [Workbench](#Workbench.md), ogni elemento prende la forma dell'ultimo e aggiunge o toglie qualcosa. Quindi una caratteristica "Tasca" non è solo il foro a tasca stesso, ma l'intera parte con la caratteristica tasca.}}


{{term|FEM|content=[FEM](FEM_Workbench.md)}}


{{defn|defn=[https://en.wikipedia.org/wiki/Finite_element_method Finite Element Method], un [Workbench](#Workbench.md) utilizzato per risolvere problemi di ingegneria e fisica matematica associati a parti, assiemi e strutture.}}


{{term|Fillet}}


{{defn|defn=Un rilievo arrotondato o un taglio su un bordo aggiunto per un aspetto finito e per spezzare gli spigoli vivi. Vedere [Part Fillet](Part_Fillet/it.md) e [PartDesign Fillet](PartDesign_Fillet/it.md).}}


{{term|Fork}}


{{defn|defn=Vedere [Forked Model](#Forked_Model.md).}}


{{term|Forked Model}}


{{defn|defn=Un metodo di modellazione, solitamente accidentale e non corretto in FreeCAD, che crea due o più versioni di un modello da un elemento precedente. (Da non confondere con operazioni intenzionali come Array, Clone, Polar Pattern, ecc.)}}


{{term|Frenet}}


{{defn|defn=Quando si esegue lo sweep di un profilo lungo un percorso 3D, il parametro Frenet controlla l'orientamento del profilo mentre si sposta lungo il percorso. Se Frenet è vero, i profili sono orientati utilizzando il Frenet Frame (tangente, binormale, normale) del percorso. Se Frenet è false la rotazione del profilo non è limitata. [https://en.wikipedia.org/wiki/Differentiable_curve#Frenet_frame Frenet frame]}}


{{term|Freetype|content=[http://www.freetype.org FreeType]}}


{{defn|defn=Una libreria software disponibile gratuitamente utilizzata per estrarre informazioni dai file di definizione dei caratteri.}}


{{term|Frustum|content=[http://en.wikipedia.org/wiki/Frustum Frustum]}}


{{defn|defn=La porzione di un solido che si trova tra due piani paralleli che lo intersecano. Utilizzato nella computer grafica per descrivere la regione tridimensionale visibile sullo schermo, vedere il [http://en.wikipedia.org/wiki/Viewing_frustum "viewing frustum"]}}


{{term|Fully Constrained}}


{{defn|defn=In [Sketcher](#Sketcher.md), quando uno [Sketch](#Sketch.md) non ha [Degrees Of Freedom](#Degrees_Of_Freedom.md), si dice che lo Sketch è "completamente vincolato" dai [Constraint](#Constraint.md).}}


{{term|Fuse}}


{{defn|defn=Termine comunemente usato in FreeCAD per riferirsi a un'[unione booleana](#Boolean_Operation.md) di forme.}}


{{glossend}}

## G


{{gloss}}


{{term|GDB or gdb}}


{{defn|defn=[https://www.gnu.org/software/gdb/ '''G'''NU Project '''D'''e'''B'''ugger], un programma di debug utilizzato su Unix e altri 'nix sistemi operativi per ottenere un [Backtrace](#Backtrace.md). "gdb" (senza virgolette) è anche la prima parte del comando utilizzato per avviare il programma GDB stesso. Un esempio di come utilizzare GDB con FreeCAD è in [http://forum.freecadweb.org/viewtopic.php?t=7052#p56918 questo post del forum]}}


{{term|Geometric modeling kernel}}


{{defn|defn=Chiamato anche kernel CAD. Un insieme di librerie software complesse responsabili della creazione di forme 3D. Tutte le operazioni sugli oggetti (estrusione, operazioni booleane, smusso, raccordo) si basano sul kernel di modellazione geometrica.}}


{{term|Git}}


{{defn|defn=[http://en.wikipedia.org/wiki/Distributed_revision_control Distributed revision control system] utilizzato da FreeCAD per ospitare e gestire la sua base di codice.}}


{{term|[Group](Std_Group.md)}}


{{defn|defn=Utilizzato per organizzare gli elementi nella [Tree view](#Tree_view.md).}}


{{term|GUI}}


{{defn|defn='''G'''raphical '''U'''ser '''I'''nterface. Consente agli utenti di interagire con FreeCAD tramite icone grafiche e il puntatore del mouse.}}


{{glossend}}

## H


{{gloss}}


{{term|Half_Space|content=[http://en.wikipedia.org/wiki/Half-space_%28geometry%29 Half Space]}}


{{defn|defn=Quando un piano divide completamente uno spazio euclideo 3D, il piano forma due semispazi.}}


{{glossend}}

## I


{{gloss}}


{{term|IGES}}


{{defn|defn=Un formato di file per lo scambio di modelli di dati di prodotto. Le estensioni dei file sono *.iges, *.igs. Vedere anche [STEP](#STEP.md).}}


{{term|Intersection|content=[http://en.wikipedia.org/wiki/Intersection Intersection]}}


{{defn|defn=Quella porzione di due o più entità geometriche che è comune a tutte. Ad esempio, l'intersezione di due linee è un punto.}}


{{glossend}}

## J


{{gloss}}


{{term|JT}}


{{defn|defn=Un formato di dati 3D proprietario sviluppato da Siemens PLM Software. FreeCAD non ha supporto per JT in questo momento.}}


{{glossend}}

## K


{{gloss}}


{{term|Kernel}}


{{defn|defn=Vedere [Geometric modeling kernel](#Geometric_modeling_kernel.md).}}


{{term|KML}}


{{defn|defn=Keyhole Markup Language: un file di definizione di dati geospaziali 3D basato su XML utilizzato da Google Earth. FreeCAD non ha supporto per KML in questo momento.}}


{{glossend}}

## L


{{gloss}}


{{term|Label}}


{{defn|no=1|defn=Una proprietà definita dall'utente di un oggetto; usato per rendere la [Tree view](#Tree_view.md) più facile da capire per gli umani.}}


{{defn|no=2|defn=Una stringa di testo descrittivo aggiunta a un disegno (vedere [Draft Label](Draft_Label/it.md)).}}


{{defn|defn= A differenza di [Name](#Name.md).}}


{{term|Line}}


{{defn|defn=Molto spesso questo è usato come sinonimo di [Line Segment](#Line_Segment.md). In Sketcher, è usato a volte con il suo significato esatto di un percorso rettilineo infinito.}}


{{term|Line Segment}}


{{defn|defn=Un percorso rettilineo tra due [Points](#Point.md).}}


{{term|Lock}}


{{defn|defn=[Constraint Lock](Sketcher_ConstrainLock/it.md)}}


{{term|Loft|content=[http://en.wikipedia.org/wiki/Loft_%283D%29 Loft]}}


{{defn|defn=Una forma topologica creata collegando profili consecutivi con una superficie. Simile al processo utilizzato per realizzare aeroplani o barche rivestiti in tessuto. Anche la funzione FreeCAD per creare un tale oggetto.}}


{{glossend}}

## M


{{gloss}}


{{term|Macro}}


{{defn|defn=Una sequenza salvata di istruzioni di FreeCAD, spesso scritta dagli utenti finali.}}


{{term|Manifold}}


{{defn|defn=Detto di una [Shape](#Shape.md) che forma un volume perfettamente chiuso. Un sinonimo familiare che fornisce una buona descrizione è "impermeabile". Per generare un solido, una [Shell](#Shell.md) deve essere manifold.}}


{{term|Mantis}}


{{defn|defn=[Bug tracking system](#Tracker.md) utilizzato dal progetto FreeCAD.}}


{{term|Mesh}}


{{defn|defn=Tipo di oggetto che può essere importato o creato da FreeCAD. Vedere [http://en.wikipedia.org/wiki/Polygon_mesh Polygon mesh] per maggiori dettagli.}}


{{term|Model}}


{{defn|defn=Chiamato anche modello 3D. Rappresentazione al computer di una [Part](#Part.md) o di un [Assembly](#Assembly.md).}}


{{term|MultiTransform|content=[MultiTransform](PartDesign_MultiTransform.md)}}


{{defn|defn=Sta per trasformazione multipla. Una [Feature](#Feature.md) dal [PartDesign](PartDesign_Workbench/it.md) [Workbench](#Workbench.md) che applica una serie di trasformazioni concatenate (modello lineare e circolare, speculare) alle feature selezionate.}}


{{glossend}}

## N


{{gloss}}


{{term|Name}}


{{defn|defn=Un identificatore univoco per un oggetto documento di FreeCAD. Una volta assegnato dal programma, il Name non è facilmente modificabile. A differenza di [Label](#Label.md).}}


{{term|Non-manifold}}


{{defn|defn=La topologia Non-manifold, chiamata anche spessore zero, è costituita da due corpi solidi distinti collegati a un vertice o bordo teorico. È un tipo di forma non supportato (non sempre rilevato da FreeCAD) che dovrebbe essere evitato, in quanto può causare problemi con ulteriori passaggi e con l'esportazione.}}


{{term|Null Shape}}


{{defn|defn=Una proprietà [Shape](#Shape.md) che non è stata inizializzata da un programma/macro. Di solito una condizione di errore.}}


{{glossend}}

## O


{{gloss}}


{{term|OCC}}


{{defn|defn=Acronimo di [Open CASCADE](#Open_CASCADE.md). Prima di essere open source, si chiamava CAS.CADE (abbreviato da Computer Aided Software for Computer Aided Design and Engineering).}}


{{term|OCE}}


{{defn|defn='''O'''pen CASCADE '''C'''ommunity '''E'''dition. Fornisce patch, miglioramenti ed esperienze fornite dagli utenti tramite la libreria ufficiale [Open CASCADE](#Open_CASCADE.md). FreeCAD è noto per funzionare su OCC o OCE.}}


{{term|OCCT}}


{{defn|defn=Tecnologia Open CASCADE. Vedere [OCC](#OCC.md).}}


{{term|Open CASCADE|content=[http://www.opencascade.org Open CASCADE]}}


{{defn|defn=Il [Geometric modeling kernel](#Geometric_modeling_kernel.md) (software library) sottostante a FreeCAD. Anche detto [OCC](#OCC.md) o [OCCT](#OCCT.md) (Per CASCADE Technology). Vedere anche [OCE](#OCE.md).}}


{{term|OpenSCAD|content=[http://www.openscad.org/ OpenSCAD]}}


{{defn|no=1|defn=Nome di un programma CAD basato solo su script.}}


{{defn|no=2|defn=Un [Workbench](#Workbench.md) di FreeCAD. [OpenSCAD](OpenSCAD_Workbench.md) [workbench](#Workbench.md) fornisce un'interfaccia per l'importazione/esportazione di modelli *.scad e *.csg, nonché alcuni strumenti di utilità.}}


{{term|Origin}}


{{defn|defn=Il centro del sistema di coordinate. Tutto parte da questo punto in direzione positiva o negativa. Così come la nostra visione dell'universo con la Terra come "origine".}}


{{term|Orthographic}}


{{defn|defn=Vedere [http://en.wikipedia.org/wiki/Orthographic_projection Orthographic projection] e [http://en.wikipedia.org/wiki/Multiview_orthographic_projection Multiview orthographic projection].}}


{{glossend}}

## P


{{gloss}}


{{term|Pad}}


{{defn|defn=Un'estensione di uno [Sketch](#Sketch.md) in una direzione perpendicolare al piano dello schizzo. Vedere anche [Extrude](#Extrude.md).}}


{{term|Part}}


{{defn|no=1|defn=Un [Workbench](#Workbench.md) di FreeCAD utilizzato principalmente per un flusso di lavoro [http://en.wikipedia.org/wiki/Constructive_solid_geometry Constructive Solid Geometry]. Vedere [Ambiente Part](Part_Workbench/it.md).}}


{{defn|no=2|defn=Un modulo Python di FreeCAD, che si interfaccia direttamente con [OCC](#OCC.md). Vedere [Script di Part](Part_scripting/it.md).}}


{{defn|no=3|defn=Un contenitore che raggruppa qualsiasi tipo di oggetto FreeCAD e ha un [Placement](#Placement.md). Vedere [Part](Std_Part/it.md).}}


{{defn|no=4|defn=Un solido unibody. Il componente di livello più basso in un assieme.}}


{{term|PartDesignNext}}


{{defn|defn=Soprannome usato nei forum per distinguere [PartDesign](PartDesign_Workbench/it.md) [Workbench](#Workbench.md) nella versione FreeCAD 0.17 da quello nella v0.16 e precedenti, a causa delle grandi modifiche introdotte.}}


{{term|PD}}


{{defn|defn=Abbreviazione di [PartDesign](PartDesign_Workbench/it.md), un [Workbench](#Workbench.md) di FreeCAD.}}


{{term|PDN}}


{{defn|defn=Abbreviazione di [PartDesignNext](#PartDesignNext.md).}}


{{term|Perspective}}


{{defn|defn=[http://en.wikipedia.org/wiki/Graphical_projection#Perspective Proiezione prospettica]}}


{{term|Pivy|content=[http://pypi.python.org/pypi/Pivy Pivy]}}


{{defn|defn=Una libreria software che consente a Python di utilizzare Coin.}}


{{term|Placement}}


{{defn|defn=Insieme di proprietà di un oggetto che ne definisce le coordinate e l'orientamento nello spazio. Vedere [Posizionamento](Placement/it.md).}}


{{term|Planar}}


{{defn|defn=Detto della geometria i cui elementi giacciono tutti su uno stesso piano.}}


{{term|Plane}}


{{defn|no=1|defn=Una superficie piana, bidimensionale, che si estende all'infinito.}}


{{defn|no=2|defn=Un oggetto primitivo bidimensionale creato nel [Part](Part_Workbench/it.md) [Workbench](#Workbench.md).}}


{{term|Plot}}


{{defn|no=1|defn=Un sinonimo obsoleto per un disegno tecnico realizzato con un plotter a penna. Vedere [https://en.wikipedia.org/wiki/Plotter Plotter].}}


{{defn|no=2|defn=Abbreviazione di piano di stampa. Vedere [https://en.wikipedia.org/wiki/Site_plan Piano di Stampa].}}


{{defn|no=3|defn=Rappresentazione grafica dei dati. Vedere [https://en.wikipedia.org/wiki/Plot_(graphics) Plot (graphics)].}}


{{term|Pocket}}


{{defn|defn=Una [Feature](#Feature.md) che rimuove materiale da un solido in base a uno [Sketch](#Sketch.md).}}


{{term|Point}}


{{defn|defn=Un elemento utilizzato per fare riferimento a una singola area nell'area di lavoro 3D. Un "punto" è adimensionale. Ha una dimensione sullo schermo, solitamente rappresentata da un "punto" solo per poter vedere dove si trova. Vedere anche [Vertex](#Vertex.md).}}


{{term|Polygon mesh}}


{{defn|defn=Vedere [http://en.wikipedia.org/wiki/Polygonal_mesh Polygonal_mesh]}}


{{term|Polyline}}


{{defn|defn=Una serie di segmenti di linea o arco collegati.}}


{{term|POV-Ray}}


{{defn|defn=[http://en.wikipedia.org/wiki/POV-Ray POV-Ray]}}


{{term|PPA}}


{{defn|defn=Acronimo che sta per '''P'''ersonal '''P'''ackage '''A'''archive. È un tipo di repository software esclusivo del sistema operativo Ubuntu Linux. Il progetto FreeCAD offre l'ultima versione e le versioni di sviluppo attraverso due repository PPA. Gli aggiornamenti sono gestiti dal gestore degli aggiornamenti del sistema host.}}


{{term|Primitive}}


{{defn|defn=Una forma base utilizzata nella costruzione di modelli. Alcune primitive 2D sono: punto, linea, poligono, cerchio, ellisse, spirale, elica. Le primitive 3D sono: scatola, cilindro, cono, toro, sfera, ellissoide, prisma.}}


{{term|PySide|content=[https://wiki.qt.io/PySide PySide]}}


{{defn|defn=Una libreria software disponibile gratuitamente che consente a Python di utilizzare QT.}}


{{term|Python|content=[http://www.python.org Python]}}


{{defn|defn=Un linguaggio di programmazione utilizzato nello sviluppo di FreeCAD così come in [Macro](#Macro.md) o script scritti dall'utente.}}


{{glossend}}

## Q


{{gloss}}


{{term|Qt|content=[https://www.qt.io/developers/ Qt]}}


{{defn|defn=Un'applicazione multipiattaforma e un framework di interfaccia utente.}}


{{glossend}}

## R


{{gloss}}


{{term|Raytracing}}


{{defn|defn=[http://en.wikipedia.org/wiki/Ray_tracing_%28graphics%29 Ray tracing]}}


{{term|Revolve}}


{{defn|defn=Uno strumento del [Part](Part_Workbench/it.md) [workbench](#Workbench.md). Vedere [Part Revolve](Part_Revolve/it.md).}}


{{term|Robot}}


{{defn|defn=[http://en.wikipedia.org/wiki/Industrial_robot Industrial robot]}}


{{term|Rotate}}


{{defn|defn=Azione per ruotare un oggetto su un asse o per cambiarne l'orientamento nello spazio.}}


{{glossend}}

## S


{{gloss}}


{{term|Section}}


{{defn|defn=[http://en.wikipedia.org/wiki/Cross_section_%28geometry%29 Cross section (geometry)]}}


{{term|Self Intersection}}


{{defn|defn=Una condizione in cui una curva attraversa se stessa (es.'8','&'). Ciò confonde gli algoritmi del kernel geometrico e generalmente produce una condizione di errore.}}


{{term|Shape}}


{{defn|defn=Termine generico utilizzato in FreeCAD per descrivere la maggior parte degli elementi (ad eccezione di [Mesh](#Mesh.md)).}}


{{term|Shell}}


{{defn|defn=Forma composta da due o più [Face](#Face.md) contigue. Un guscio [Manifold](#Manifold.md) (chiuso) può essere convertito in un [Solid](#Solid.md).}}


{{term|Sketch}}


{{defn|defn=Una rappresentazione 2D vincolata di un oggetto fissato su un piano o su una [Face](#Face.md). In FreeCAD uno schizzo è sempre un oggetto bidimensionale da qualche parte nello spazio 3D.}}


{{term|Sketcher|content=[Sketcher](Sketcher_Workbench/it.md)}}


{{defn|defn=Un [Workbench](#Workbench.md) utilizzato per creare geometria 2D mediante l'uso di [Element](#Element.md) e [Constraint](#Constraint.md).}}


{{term|Sketcher Solver}}


{{defn|defn=Il meccanismo interno di FreeCAD che calcola le interdipendenze e gli effetti dell'aggiunta, eliminazione e modifica della geometria e dei vincoli associati in ogni schizzo. Sketcher Solver calcola anche la disposizione di tutta la geometria in ogni schizzo in modo che possa essere visualizzata correttamente.}}


{{term|Smooth Line}}


{{defn|defn=In un disegno, una linea che indica un cambiamento tra superfici tangenti, come nella transizione da una superficie piana a un raccordo. Anche "tangent edge". Vedere [Modificare una vista esistente](Drawing_View/it#Modificare_una_vista_esistente.md)}}


{{term|Solid}}


{{defn|defn=Parte dello spazio 3D delimitato da [Shells](#Shell.md). Un solido ha un volume e altre proprietà relative agli oggetti come una massa.}}


{{term|Solver}}


{{defn|defn=Vedere [Sketcher Solver](#Sketcher_Solver.md).}}


{{term|Stable}}


{{defn|defn=Un soprannome per l'ultima versione generale del software FreeCAD. Questa è in genere la versione disponibile da fonti diverse dal progetto FreeCAD. Confrontare con [Unstable](#Unstable.md).}}


{{term|STL}}


{{defn|defn=''STereoLithography'', noto anche come ''Standard Tessellation Language.'' Un formato di file [Mesh](#Mesh.md) che definisce solo la superficie di un oggetto 3D. Le estensioni dei file sono *.stl.}}


{{term|STEP}}


{{defn|defn=Uno standard ISO (ISO 10303) per lo scambio di dati 3D e informazioni sulla produzione dei prodotti. Sostituisce [IGES](#IGES.md). Le estensioni dei file sono *.step, *.stp.}}


{{term|SVG|content=[SVG](SVG.md)}}


{{defn|defn=[https://en.wikipedia.org/wiki/Scalable_Vector_Graphics Scalable Vector Graphics]. Un formato di file di grafica vettoriale.}}


{{term|Sweep}}


{{defn|defn=Una forma 3D generata da almeno una sezione trasversale 2D che segue una traiettoria (percorso). Comunemente utilizzato per definire lo strumento e la forma creata. Vedere [http://en.wikipedia.org/wiki/Solid_modeling#Sweeping Solid modeling]}}


{{glossend}}

## T


{{gloss}}


{{term|Task panel}}


{{defn|defn=Un [https://en.wikipedia.org/wiki/Panel_(computer_software) control panel] in FreeCAD che visualizza il contenuto specifico dell'attività da svolgere. Può mostrare gli strumenti disponibili nell'[Workbench](#Workbench.md) attivo o richiedere valori e opzioni mentre un [Command](#Command.md) è attivo.}}


{{term|Tasks tab}}


{{defn|defn=Vedere [Task panel](#Task_panel.md).}}


{{term|Tessellation}}


{{defn|defn=Una tassellatura di una superficie è la piastrellatura della superficie utilizzando una o più forme geometriche, chiamate tessere, senza sovrapposizioni e senza spazi vuoti. In FreeCAD è necessario visualizzare le forme geometriche nella vista 3D. La tassellatura relativa alle dimensioni di una forma può essere impostata nelle preferenze per ottenere una visualizzazione più uniforme delle superfici rotonde a discapito del tempo di calcolo. Vedere [Editor delle Prefereze](Preferences_Editor/it.md).}}


{{term|Thickness}}


{{defn|no=1|defn=Una misura dello spessore di una forma.}}


{{defn|no=2|defn=Uno strumento [Part](Part_Workbench/it.md) [Workbench](#Workbench.md) per scavare un solido e lasciare uno spessore uniforme definito.}}


{{term|Toggle}}


{{defn|defn=Un'impostazione che può essere modificata tra due opzioni, ad esempio tra True o False o tra Off e On.}}


{{term|Topological Naming}}


{{defn|defn=Uno schema in base al quale a un bordo oa una faccia, una volta creato, viene assegnato un nome permanente. Internamente, FreeCAD identifica bordi e facce su un solido numerandoli come: Edge1, Edge2, Face1, Face2, ecc. Il problema è che questi ID sono applicati in qualche modo in modo casuale e cambieranno dopo che è stato fatto qualcosa al modello che cambia la quantità di spigoli e facce. Ad esempio, se il modello viene rivisto, un elemento collegato a una Faccia2 potrebbe successivamente essere erroneamente collegato a una faccia diversa (che è stata rinominata per diventare la nuova Faccia2), causando all'utente risultati indesiderati. A partire dalla versione 0.20 di FreeCAD, la denominazione topologica non è stata ancora implementata, quindi se un oggetto viene modificato in modo tale da cambiare il numero di spigoli o facce, potrebbero cambiare anche i nomi degli spigoli o delle facce di quell'oggetto.}}


{{term|Torus}}


{{defn|defn=Una forma primitiva.}}


{{term|Tracker}}


{{defn|defn=Abbreviazione di bug tracker, l'applicazione software online utilizzata per tenere traccia dei bug segnalati o delle richieste di funzionalità. Vedere anche [Mantis](#Mantis.md).}}


{{term|Tree view|content=[Tree view](Tree_view/it.md)}}


{{defn|defn=La vista ad albero è un componente dell'[interfaccia](Interface/it.md) di FreeCAD. Può essere mostrato come un elemento [GUI](#GUI.md) separato o come parte della [Vista Combinata](Combo_View/it.md). Contiene una rappresentazione della struttura del documento.}}


{{glossend}}

## U


{{gloss}}


{{term|Union}}


{{defn|defn=Uno strumento [Part](Part_Workbench/it.md) [Workbench](#Workbench.md) che esegue una [Boolean operation](#Boolean_Operation.md) sulle forme selezionate.}}


{{term|Unstable}}


{{defn|defn=Un soprannome per una versione molto recente del software FreeCAD. Questa versione conterrà molte modifiche recentemente implementate dagli sviluppatori. In genere non fallisce o produce risultati errati, ma non ha completato i test.}}


{{term|Upgrade|content=[Upgrade](Draft_Upgrade/it.md)}}


{{defn|defn=Uno strumento [Draft](Draft_Workbench/it.md) [workbench](#Workbench.md).}}


{{glossend}}

## V


{{gloss}}


{{term|Vector}}


{{defn|defn=Una grandezza con una direzione. Spesso rappresentato graficamente come una freccia in 2 o 3 dimensioni. Ad esempio, "cinquanta passi a nord", "9,8 m/s^2 in basso" e "(3,5,6) unità nelle direzioni x, y, z, rispettivamente" sono tutti vettori. In FreeCAD, sono spesso indicati come coppie ordinate (x, y) o triple ordinate (x, y, z).}}


{{term|Vertex}}


{{defn|defn=Un [Point](#Point.md) solitario nello spazio, o l'angolo di una [Shape](#Shape.md) dove gli [Edge](#Edge.md) si incontrano. La Open Cascade Technology lo definisce come una [Shape](#Shape.md) di dimensione zero corrispondente a un punto nella geometria. Vedere [https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3 OCCT Profile: Defining the topology]}}


{{term|Vertices}}


{{defn|defn=Plurale di [Vertex](#Vertex.md)}}


{{term|Viewprovider}}


{{defn|defn=Interfaccia generale per tutte le cose visive in FreeCAD. Un ViewProvider genera e gestisce tutto intorno alla visualizzazione e alla presentazione di oggetti dall'[App layer](#App.md) di FreeCAD all'utente. Questa classe e i suoi discendenti devono essere implementati per qualsiasi tipo di oggetto per mostrarli nella [3D view](#3D_view.md) e [Tree view](#Tree_view.md).}}


{{glossend}}

## W


{{gloss}}


{{term|WB}}


{{defn|defn=Abbreviazione per [Workbench](#Workbench.md).}}


{{term|Wire}}


{{defn|no=1|defn=Una sequenza di [Edge](#Edge.md) connessi da [Vertice](#Vertex.md). Il termine wire è usato in questo senso principalmente da [https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3 Open Cascade Technology] e quindi anche all'interno di FreeCAD.}}


{{defn|no=2|defn=Un comando [Draft](Draft_Workbench/it.md) [Workbench](#Workbench.md) che crea un wire parametrico.}}


{{term|Workbench}}


{{defn|defn=Detto anche modulo, ogni workbench raggruppa una serie di strumenti dedicati a un'attività specifica.}}


{{glossend}}

## X


{{gloss}}


{{term|X}}


{{defn|defn=Si riferisce comunemente all'[Axis](#Axis.md) X in 2D o 3D.}}


{{glossend}}

## Y


{{gloss}}


{{term|Y}}


{{defn|defn=Si riferisce comunemente all'[Axis](#Axis.md) Y in 3D.}}


{{glossend}}

## Z


{{gloss}}


{{term|Z}}


{{defn|defn=Si riferisce comunemente all'[Axis](#Axis.md) Z in 3D.}}


{{glossend}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Wiki](Category_Wiki.md) > [Glossary](Category_Glossary.md) > Glossary/it
