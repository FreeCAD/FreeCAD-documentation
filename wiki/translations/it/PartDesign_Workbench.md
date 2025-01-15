# <img alt="L\'icona dell\'ambiente PartDesign" src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/it






## Introduzione

L**\'[Ambiente PartDesign](PartDesign_Workbench/it.md)** <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> fornisce strumenti per la modellazione di componenti solidi. È principalmente focalizzato sulla creazione di componenti meccaniche che possono essere fabbricate e assemblate in un prodotto finito. Tuttavia, i solidi creati possono essere utilizzati per qualsiasi altro scopo come [modellazione BIM](BIM_Workbench/it.md), [analisi degli elementi finiti](FEM_Workbench/it.md), o [lavorazione e stampa 3D](CAM_Workbench/it.md).

L\'ambiente PartDesign utilizza una metodologia basata sulle funzionalità. Un componente è rappresentato dal contenitore dell\'oggetto Body (corpo). Il Body definisce un sistema di coordinate locali e contiene le caratteristiche cumulative che definiscono il componente. La maggior parte delle feature si basa su schizzi parametrici e sono additive o sottrattive. Ad esempio, lo [Strumento Pad](PartDesign_Pad/it.md) aggiunge lo schizzo estruso al solido di sviluppo, lo [Strumento Tasca](PartDesign_Pocket/it.md) sottrae lo schizzo estruso. Ciascuna funzionalità è cumulativa e si basa sul risultato delle funzionalità precedenti. È anche possibile utilizzare le primitive ([Cilindro](PartDesign_AdditiveCylinder/it.md), [Sfera](PartDesign_AdditiveSphere/it.md), ecc.) così come i solidi creati all\'esterno del Body come feature.

Vedere la pagina [modifica delle funzionalità](Feature_editing/it.md) per una spiegazione più completa di questo processo, quindi vedere [Creazione di un componente semplice con PartDesign](Creating_a_simple_part_with_PartDesign/it.md) per iniziare con la creazione di solidi.

L\' <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Ambiente Part](Part_Workbench.md) fornisce una metodologia alternativa, [geometria solida costruttiva](constructive_solid_geometry/it.md) (CSG), per la costruzione di forme. Per una discussione dettagliata dell\'ambiente Part e dell\'ambiente Part Design vedere [Part e Part Design](Part_and_PartDesign/it.md).

![](images/PartDesign_Workbench_Example.jpg )



## Strumenti

Gli strumenti di Part Design si trovano tutti nel menu di **Part Design** e nella barra degli strumenti di PartDesign che appare quando si carica l\'ambiente Part Design.



### Strumenti di supporto di Part Design 

-   <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> [Crea corpo](PartDesign_Body/it.md): crea un oggetto [Corpo](Body/it.md) nel documento attivo e lo rende attivo.

-   <img alt="" src=images/PartDesign_NewSketch.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Crea schizzo:

  -<img alt="" src=images/PartDesign_NewSketch.svg  style="width:32px;"> [Crea schizzo](PartDesign_NewSketch/it.md): crea un nuovo schizzo su una faccia o un piano selezionati. Se non viene selezionata alcuna faccia mentre viene eseguito questo strumento, all\'utente viene richiesto di selezionare un piano dal pannello Azioni. L\'interfaccia passa quindi all\'ambiente [Sketcher](Sketcher_Workbench/it.md) nella modalità di modifica dello schizzo.

  - <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Mappa schizzo su faccia](Sketcher_MapSketch/it.md): collega uno schizzo alla geometria selezionata dal corpo attivo.

  - <img alt="" src=images/Sketcher_EditSketch.png  style="width:32px;"> [Edita schizzo](Sketcher_EditSketch/it.md): apre lo schizzo selezionato per la modifica.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Convalida lo schizzo](Sketcher_ValidateSketch/it.md): controlla se nell\'area di tolleranza ci sono dei punti distinti e li fa coincidere.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Controlla la geometria](Part_CheckGeometry/it.md): Verifica la presenza di errori nella geometria degli oggetti selezionati.

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Crea un Forma legata](PartDesign_ShapeBinder/it.md): crea un raccoglitore di forme che fa riferimento alla geometria da un singolo oggetto principale

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Crea una Forma legata a sotto-oggetti](PartDesign_SubShapeBinder/it.md): crea un raccoglitore di forme che fa riferimento alla geometria da uno o più oggetti principali.

-   <img alt="" src=images/PartDesign_Clone.svg  style="width:32px;"> [Crea un clone](PartDesign_Clone/it.md): crea un clone del corpo selezionato.

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Crea un riferimento (

ː\*<img alt="" src=images/PartDesign_Plane.svg  style="width:32px;"> [Crea un piano di riferimento](PartDesign_Plane/it.md): crea un piano di riferimento nel corpo attivo. ({{VersionMinus/it|1.0}})

ː\*<img alt="" src=images/PartDesign_Line.svg  style="width:32px;"> [Crea una linea di riferimento](PartDesign_Line/it.md): crea una linea di riferimento nel corpo attivo. ({{VersionMinus/it|1.0}})

ː\*<img alt="" src=images/PartDesign_Point.svg  style="width:32px;"> [Crea un punto di riferimento](PartDesign_Point/it.md): crea un punto di riferimento nel corpo attivo. ({{VersionMinus/it|1.0}})

ː\*<img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width:32px;"> [Sistema di coordinate locali](PartDesign_CoordinateSystem/it.md): crea nel corpo attivo un sistema di coordinate locale collegato alla geometria di riferimento. ({{VersionMinus/it|1.0}})

:   
    {{Version/it|1.1}}: questi strumenti sono stati sostituiti dai nuovi [strumenti datum](Std_Base/it#Part_Datums.md).



### Strumenti di modellazione di Part Design 



#### Strumenti Additivi 

Questi sono gli strumenti per creare funzioni di base o per aggiungere del materiale a un corpo esistente.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Estrusione](PartDesign_Pad/it.md): estrude un solido da uno schizzo selezionato.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Rivoluzione](PartDesign_Revolution/it.md): crea un solido ruotando uno schizzo attorno ad un asse. Lo schizzo deve avere un profilo chiuso.

-   <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:32px;"> [Loft additivo](PartDesign_AdditiveLoft/it.md): crea un solido eseguendo una transizione tra due o più schizzi.

-   <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:32px;"> [Sweep additivo](PartDesign_AdditivePipe/it.md): crea un solido spostando uno o più schizzi lungo un percorso aperto o chiuso.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Elica additiva](PartDesign_AdditiveHelix/it.md): crea un solido facendo scorrere uno schizzo lungo un\'elica.

-   <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Crea una primitiva additiva:

  -<img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:32px;"> [Cubo additivo](PartDesign_AdditiveBox/it.md): crea un cubo additivo.

  -<img alt="" src=images/PartDesign_AdditiveCylinder.svg  style="width:32px;"> [Cilindro additivo](PartDesign_AdditiveCylinder/it.md): crea un cilindro additivo.

  -<img alt="" src=images/PartDesign_AdditiveSphere.svg  style="width:32px;"> [Sfera additiva](PartDesign_AdditiveSphere/it.md): crea una sfera additiva.

  -<img alt="" src=images/PartDesign_AdditiveCone.svg  style="width:32px;"> [Cono additivo](PartDesign_AdditiveCone/it.md): crea un cono additivo.

  -<img alt="" src=images/PartDesign_AdditiveEllipsoid.svg  style="width:32px;"> [Ellissoide additivo](PartDesign_AdditiveEllipsoid/it.md): crea un ellissoide additivo.

  -<img alt="" src=images/PartDesign_AdditiveTorus.svg  style="width:32px;"> [Toro additivo](PartDesign_AdditiveTorus/it.md): crea un toro additivo.

  -<img alt="" src=images/PartDesign_AdditivePrism.svg  style="width:32px;"> [Prisma additivo](PartDesign_AdditivePrism/it.md): crea un prisma additivo.

  -<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width:32px;"> [Cuneo additivo](PartDesign_AdditiveWedge/it.md): crea un cuneo additivo.



#### Strumenti sottrattivi 

Questi sono gli strumenti per sottrarre del materiale da un corpo esistente.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Tasca](PartDesign_Pocket/it.md): crea una tasca da uno schizzo selezionato.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> [Foro](PartDesign_Hole/it.md): crea una funzione foro da uno schizzo selezionato. Lo schizzo deve contenere uno o più cerchi.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Gola](PartDesign_Groove/it.md): crea un solco ruotando uno schizzo attorno ad un asse.

-   <img alt="" src=images/PartDesign_SubtractiveLoft.svg  style="width:32px;"> [Loft sottattivo](PartDesign_SubtractiveLoft/it.md): crea una forma solida effettuando una transizione tra due o più schizzi e la sottrae dal corpo attivo.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width:32px;"> [Sweep sottrattivo](PartDesign_SubtractivePipe/it.md): crea una forma solida spostando uno o più schizzi lungo un percorso aperto o chiuso e la sottrae dal corpo attivo.

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Elica sottrattiva](PartDesign_SubtractiveHelix/it.md): crea una forma solida facendo scorrere uno schizzo lungo un\'elica e la sottrae dal corpo attivo.

-   <img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Crea una primitiva sottrativa:

  -<img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:32px;"> [Cubo sottrattivo](PartDesign_SubtractiveBox/it.md): aggiunge un cubo sottrattivo al corpo attivo.

  -<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width:32px;"> [Cilindro sottattivo](PartDesign_SubtractiveCylinder/it.md): aggiunge un cilindro sottrattivo al corpo attivo.

  -<img alt="" src=images/PartDesign_SubtractiveSphere.svg  style="width:32px;"> [Sfera sottattiva](PartDesign_SubtractiveSphere/it.md): aggiunge una sfera sottrattiva al corpo attivo.

  -<img alt="" src=images/PartDesign_SubtractiveCone.svg  style="width:32px;"> [Cono sottrattivo](PartDesign_SubtractiveCone/it.md): aggiunge un cono sottrattivo al corpo attivo.

  -<img alt="" src=images/PartDesign_SubtractiveEllipsoid.svg  style="width:32px;"> [Ellissoide sottrattivo](PartDesign_SubtractiveEllipsoid/it.md): aggiunge un ellissoide sottrattivo al corpo attivo.

  -<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width:32px;"> [Toro sottrattivo](PartDesign_SubtractiveTorus/it.md): aggiunge un toro sottrattivo al corpo attivo.

  -<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width:32px;"> [Prisma sottattivo](PartDesign_SubtractivePrism/it.md): aggiunge un prisma sottrattivo al corpo attivo.

  - <img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width:32px;"> ‎[Cuneo sottrattivo](PartDesign_SubtractiveWedge/it.md): aggiunge un cuneo sottrattivo al corpo attivo.



#### Booleane

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width:32px;"> [Operazione booleana](PartDesign_Boolean/it.md): importa uno o più Corpi o Cloni PartDesign nel corpo attivo e applica un\'operazione booleana.



### Strumenti di abbellimento 

Questi strumenti applicano un trattamento ai bordi o alle facce.

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Raccordo](PartDesign_Fillet/it.md): raccorda (arrotonda) i bordi del corpo attivo.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Smusso](PartDesign_Chamfer/it.md): smussa i bordi del corpo attivo.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Sformo](PartDesign_Draft/it.md): applica uno sformo angolare alle facce selezionate nel corpo attivo.

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width:32px;"> [Spessore](PartDesign_Thickness/it.md): crea un guscio di dato spessore dal corpo attivo e apre la faccia o le facce selezionate.



### Strumenti di trasformazione 

Questi sono gli strumenti per trasformare le funzioni esistenti.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Specchiato](PartDesign_Mirrored/it.md): rispecchia una o più caratteristiche.

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Serie lineare](PartDesign_LinearPattern/it.md): crea un modello lineare di una o più funzioni.

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Serie polare](PartDesign_PolarPattern/it.md): crea una serie polare di una o più funzioni.

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Multitrasformazione](PartDesign_MultiTransform/it.md): crea un modello combinando una qualsiasi delle trasformazioni sopra menzionate, nonché la trasformazione [Scala](PartDesign_Scaled/it.md).
    -   <img alt="" src=images/PartDesign_Scaled.svg  style="width:32px;"> [Scala](PartDesign_Scaled/it.md): ridimensiona una o più funzioni. Questo non è disponibile come strumento di trasformazione separato.



#### Extra

Alcune funzionalità aggiuntive che si trovano nel menu di Part Design:

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Pignone](PartDesign_Sprocket/it.md): crea un profilo del pignone, che può essere estruso.

-   <img alt="" src=images/PartDesign_InvoluteGear.svg  style="width:32px;"> [Ingranaggio evolvente](PartDesign_InvoluteGear/it.md): crea un profilo ad evolvente d\'ingranaggio, che può essere estruso.

-   <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> [Procedura guidata per alberi](PartDesign_WizardShaft/it.md): genera un albero da una tabella di valori e consente di analizzare forze e momenti. L\'albero è realizzato con uno schizzo ruotato che può essere modificato.



### Elementi del menu contestuale 

-   [Soppressa](PartDesign_Suppressed/it.md): casella di controllo per disabilitare una funzione specifica senza eliminarla. {{Version/it|1.0}}

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [Imposta punta](PartDesign_MoveTip/it.md): ridefinisce la punta, che è la caratteristica esposta all\'esterno del corpo.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Sposta oggetto in altro corpo](PartDesign_MoveFeature/it.md): sposta lo schizzo, la geometria di riferimento o la funzione selezionata in un altro corpo.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Sposta l\'oggetto dopo un altro oggetto](PartDesign_MoveFeatureInTree/it.md): consente il riordino del corpo dell\'albero spostando lo schizzo selezionato, la geometria di riferimento o la funzione in un\'altra posizione nell\'elenco delle funzioni.



#### Elementi condivisi con l\'ambiente Part 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;">[Aspetto](Std_SetAppearance/it.md): determina l\'aspetto dell\'intera parte (trasparenza del colore ecc.).

-   <img alt="" src=images/Part_ColorPerFace.svg  style="width:32px;"> [Colore per faccia](Part_ColorPerFace/it.md): assegna i colori alle singole facce degli oggetti.



### Strumenti obsoleti 

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;"> [Migrazione](PartDesign_Migrate/it.md): migra i file dalle versioni di FreeCAD precedenti alla 0.17 alla versione 0.17. Questo strumento non è disponibile nella {{VersionPlus/it|1.0}}.



## Preferenze

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferenze](PartDesign_Preferences/it.md): preferenze disponibili negli strumenti PartDesign.
-   [Ottimizzare l\'installazione](Fine-tuning/it.md): alcuni parametri extra per ottimizzare il comportamento di PartDesign.



## Tutorial

-   [Come usare FreeCAD](http://help-freecad-jpg87.fr/), un sito web che descrive il flusso di lavoro per la progettazione meccanica.
-   [Creare una parte semplice con PartDesign](Creating_a_simple_part_with_PartDesign/it.md)
-   [Esercitazione di base PartDesign 019](Basic_Part_Design_Tutorial_019/it.md)
-   [PartDesign Tutorial per i supporti dei cuscinetti I](PartDesign_Bearingholder_Tutorial_I/it.md) (da aggiornare)
-   [PartDesign Tutorial per i supporti dei cuscinetti II](PartDesign_Bearingholder_Tutorial_II/it.md) (da aggiornare)



## Esempi

Per alcune idee su cosa si può ottenere con gli strumenti di Part Design, dare un\'occhiata a: [Esempi di PartDesign](PartDesign_Examples/it.md).

<img alt="" src=images/PartDesign_ExampleSphere-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleTorus-01.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExamplePad-09.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-05.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSpring-04.png  style="width:80px;">



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [PartDesign](Category_PartDesign.md) > PartDesign Workbench/it
