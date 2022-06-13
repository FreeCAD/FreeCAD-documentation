# <img alt="L\'icona dell\'ambiente PartDesign" src=images/Workbench_PartDesign.svg  style="width   *64px;"> PartDesign Workbench/it


{{TOCright}}

## Introduzione

La <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [Ambiente PartDesign](PartDesign_Workbench/it.md) fornisce strumenti avanzati per la modellazione di parti solide complesse. È principalmente focalizzato sulla creazione di parti meccaniche che possono essere fabbricate e assemblate in un prodotto finito. Tuttavia, i solidi creati possono essere utilizzati in generale per qualsiasi altro scopo come [progettazione architettonica](Arch_Workbench/it.md), [analisi degli elementi finiti](FEM_Workbench/it.md), o [lavorazione e stampa 3D](Path_Workbench/it.md).

L\'ambiente PartDesign è intrinsecamente correlato all\'ambiente [Sketcher](Sketcher_Workbench/it.md). L\'utente normalmente crea uno schizzo, quindi usa lo strumento [Estrusione PartDesign](PartDesign_Pad/it.md) per estruderlo e creare un solido di base che in seguito può essere ulteriormente modificato.

Mentre l\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Part](Part_Workbench/it.md) si basa sulla [Geometria solida costruttiva](constructive_solid_geometry/it.md) (CSG) per la costruzione di forme, l\'ambiente PartDesign utilizza la metodologia parametrica di modifica delle funzioni, il che significa che un solido di base viene trasformato in sequenza aggiungendogli delle funzioni fino a ottenere la forma finale. Per una spiegazione più completa di questo processo, si può visitare la pagina di [Editazione delle funzioni](feature_editing/it.md) e poi [Creare una parte semplice con PartDesign](Creating_a_simple_part_with_PartDesign/it.md) per iniziare a creare i solidi.

Una discussione più dettagliata dell\'ambiente Part e dell\'ambiente PartDesign può essere trovata qui   * [Part e PartDesign](Part_and_PartDesign/it.md).

I corpi creati con PartDesign sono spesso soggetti al [Problema di denominazione topologica](topological_naming_problem/it.md) il quale fa rinominare le funzioni interne quando le operazioni parametriche vengono modificate. Questo problema può essere minimizzato seguendo le migliori pratiche descritte nella pagina di [Editazione delle funzioni](feature_editing/it.md) e sfruttando gli oggetti di riferimento come supporto per schizzi e funzioni.

<img alt="" src=images/PartDesign_Example.png  style="width   *500px;">

## Strumenti

Gli strumenti di Part Design si trovano tutti nel menu di **Part Design** e nella barra degli strumenti di PartDesign che appare quando si carica l\'ambiente Part Design.

### Strumenti struttura 

Questi strumenti in realtà non fanno parte di PartDesign. Appartengono al sistema [Standard di Base](Std_Base/it.md). Sono stati sviluppati nella v0.17 con l\'intenzione di essere utili per organizzare un modello e creare [assemblaggi](Assembly/it.md); come tali, sono molto utili quando si lavora con corpi creati con questo ambiente di lavoro.

-   <img alt="" src=images/Std_Part.svg  style="width   *32px;"> [Parte](Std_Part/it.md)   * aggiunge un nuovo contenitore di Parti nel documento attivo e lo rende attivo.

-   <img alt="" src=images/Std_Group.svg  style="width   *32px;"> [Gruppo](Std_Group/it.md)   * aggiunge un contenitore Gruppo nel documento attivo, che consente di organizzare gli oggetti nella [vista ad albero](Tree_view/it.md).

### Strumenti di supporto di Part Design 

-   <img alt="" src=images/PartDesign_Body.svg  style="width   *32px;"> [Crea corpo](PartDesign_Body/it.md)   * crea un oggetto [Corpo](Body/it.md) nel documento attivo e lo rende attivo.

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width   *32px;"> [Crea schizzo](PartDesign_NewSketch/it.md)   * crea un nuovo schizzo su una faccia o un piano selezionati. Se non viene selezionata alcuna faccia mentre viene eseguito questo strumento, all\'utente viene richiesto di selezionare un piano dal pannello Azioni. L\'interfaccia passa quindi all\'ambiente [Sketcher](Sketcher_Workbench/it.md) nella modalità di modifica dello schizzo.

-   <img alt="" src=images/Sketcher_EditSketch.png  style="width   *32px;"> [Edita schizzo](Sketcher_EditSketch/it.md)   * modifica lo schizzo selezionato.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MapSketch.svg‎  style="width   *32px;"> [Mappa schizzo su faccia](Sketcher_MapSketch/it.md)   * mappa uno schizzo su un piano precedentemente selezionato o su una faccia del corpo attivo.


</div>

### Strumenti di modellazione di Part Design 

#### Strumenti di riferimento 

-   <img alt="" src=images/PartDesign_Point.svg  style="width   *32px;"> [Crea un punto di riferimento](PartDesign_Point/it.md)   * crea un punto di riferimento nel corpo attivo.

-   <img alt="" src=images/PartDesign_Line.svg  style="width   *32px;"> [Crea una linea di riferimento](PartDesign_Line/it.md)   * crea una linea di riferimento nel corpo attivo.

-   <img alt="" src=images/PartDesign_Plane.svg  style="width   *32px;"> [Crea un piano di riferimento](PartDesign_Plane/it.md)   * crea un piano di riferimento nel corpo attivo.

-   <img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width   *32px;"> [Sistema di coordinate locali](PartDesign_CoordinateSystem/it.md)   * crea nel corpo attivo un sistema di coordinate locale collegato alla geometria di riferimento.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width   *32px;"> [Crea un Forma legata](PartDesign_ShapeBinder/it.md)   * crea un raccoglitore di forme nel corpo attivo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width   *32px;"> [Crea una Forma legata sotto-oggetti](PartDesign_SubShapeBinder/it.md)   * crea una forma legata di un sottoelemento, come un bordo o una faccia di un altro corpo, mantenendo la posizione relativa di quell\'elemento. {{Version/it|0.19}}


</div>

-   <img alt="" src=images/PartDesign_Clone.svg  style="width   *32px;"> [Crea un clone](PartDesign_Clone/it.md)   * crea un clone del corpo selezionato.

#### Strumenti Additivi 

Questi sono gli strumenti per creare funzioni di base o per aggiungere del materiale a un corpo solido esistente.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width   *32px;"> [Estrusione](PartDesign_Pad/it.md)   * estrude un solido da uno schizzo selezionato.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width   *32px;"> [Rivoluzione](PartDesign_Revolution/it.md)   * crea un solido ruotando uno schizzo attorno ad un asse. Lo schizzo deve avere un profilo chiuso.

-   <img alt="" src=images/PartDesign_Additive_Loft.svg  style="width   *32px;"> [Loft additivo](PartDesign_AdditiveLoft/it.md)   * crea un solido eseguendo una transizione tra due o più schizzi.

-   <img alt="" src=images/PartDesign_Additive_Pipe.svg  style="width   *32px;"> [Sweep additivo](PartDesign_AdditivePipe/it.md)   * crea un solido spostando uno o più schizzi lungo un percorso aperto o chiuso.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width   *32px;"> [Elica additiva](PartDesign_AdditiveHelix/it.md)   * crea un solido facendo scorrere uno schizzo lungo un\'elica. {{Version/it|0.19}}

-   <img alt="" src=images/PartDesign_CompPrimitiveAdditive.png  style="width   *48px;"> [Crea una primitiva additiva](PartDesign_CompPrimitiveAdditive/it.md)   * aggiunge un primitiva additiva al corpo attivo.

   **<img alt="" src=images/PartDesign_AdditiveBox.svg  style="width   *32px;"> [Cubo additivo](PartDesign_AdditiveBox/it.md)   * crea un cubo additivo.

   **<img alt="" src=images/PartDesign_AdditiveCylinder.svg  style="width   *32px;"> [Cilindro additivo](PartDesign_AdditiveCylinder/it.md)   * crea un cilindro additivo.

   **<img alt="" src=images/PartDesign_AdditiveSphere.svg  style="width   *32px;"> [Sfera additiva](PartDesign_AdditiveSphere/it.md)   * crea una sfera additiva.

   **<img alt="" src=images/PartDesign_AdditiveCone.svg  style="width   *32px;"> [Cono additivo](PartDesign_AdditiveCone/it.md)   * crea un cono additivo.

   **<img alt="" src=images/PartDesign_AdditiveEllipsoid.svg  style="width   *32px;"> [Ellissoide additivo](PartDesign_AdditiveEllipsoid/it.md)   * crea un ellissoide additivo.

   **<img alt="" src=images/PartDesign_AdditiveTorus.svg  style="width   *32px;"> [Toro additivo](PartDesign_AdditiveTorus/it.md)   * crea un toro additivo.

   **<img alt="" src=images/PartDesign_AdditivePrism.svg  style="width   *32px;"> [Prisma additivo](PartDesign_AdditivePrism/it.md)   * crea un prisma additivo.

   **<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width   *32px;"> [Cuneo additivo](PartDesign_AdditiveWedge/it.md)   * crea un cuneo additivo.

#### Strumenti sottrattivi 

Questi sono gli strumenti per sottrarre del materiale da un corpo esistente.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width   *32px;"> [Tasca](PartDesign_Pocket/it.md)   * crea una tasca da uno schizzo selezionato.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width   *32px;"> [Foro](PartDesign_Hole/it.md)   * crea una funzione foro da uno schizzo selezionato. Lo schizzo deve contenere uno o più cerchi.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width   *32px;"> [Gola](PartDesign_Groove/it.md)   * crea un solco ruotando uno schizzo attorno ad un asse.

-   <img alt="" src=images/PartDesign_SubtractiveLoft.svg  style="width   *32px;"> [Loft sottattivo](PartDesign_SubtractiveLoft/it.md)   * crea una forma solida effettuando una transizione tra due o più schizzi e la sottrae dal corpo attivo.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width   *32px;"> [Sweep sottrattivo](PartDesign_SubtractivePipe/it.md)   * crea una forma solida spostando uno o più schizzi lungo un percorso aperto o chiuso e la sottrae dal corpo attivo.

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width   *32px;"> [Elica sottrattiva](PartDesign_SubtractiveHelix/it.md)   * crea una forma solida facendo scorrere uno schizzo lungo un\'elica e la sottrae dal corpo attivo. {{Version/it|0.19}}

-   <img alt="" src=images/PartDesign_CompPrimitiveSubtractive.png  style="width   *48px;"> [Crea una primitiva sottrattiva](PartDesign_CompPrimitiveSubtractive/it.md)   * aggiunge una primitiva sottrattiva al corpo attivo.

   **<img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width   *32px;"> [Cubo sottrattivo](PartDesign_SubtractiveBox/it.md)   * aggiunge un cubo sottrattivo al corpo attivo.

   **<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width   *32px;"> [Cilindro sottattivo](PartDesign_SubtractiveCylinder/it.md)   * aggiunge un cilindro sottrattivo al corpo attivo.

   **<img alt="" src=images/PartDesign_SubtractiveSphere.svg  style="width   *32px;"> [Sfera sottattiva](PartDesign_SubtractiveSphere/it.md)   * aggiunge una sfera sottrattiva al corpo attivo.

   **<img alt="" src=images/PartDesign_SubtractiveCone.svg  style="width   *32px;"> [Cono sottrattivo](PartDesign_SubtractiveCone/it.md)   * aggiunge un cono sottrattivo al corpo attivo.

   **<img alt="" src=images/PartDesign_SubtractiveEllipsoid.svg  style="width   *32px;"> [Ellissoide sottrattivo](PartDesign_SubtractiveEllipsoid/it.md)   * aggiunge un ellissoide sottrattivo al corpo attivo.

   **<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width   *32px;"> [Toro sottrattivo](PartDesign_SubtractiveTorus/it.md)   * aggiunge un toro sottrattivo al corpo attivo.

   **<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width   *32px;"> [Prisma sottattivo](PartDesign_SubtractivePrism/it.md)   * aggiunge un prisma sottrattivo al corpo attivo.

   ** <img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width   *32px;"> ‎[Cuneo sottrattivo](PartDesign_SubtractiveWedge/it.md)   * aggiunge un cuneo sottrattivo al corpo attivo.

#### Strumenti di trasformazione 


<div class="mw-translate-fuzzy">

Questi sono gli strumenti per trasformare le funzioni esistenti. Permetteranno di scegliere quali funzioni trasformare.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width   *32px;"> [Specchiato](PartDesign_Mirrored/it.md)   * rispecchia una o più funzioni su un piano o una faccia.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width   *32px;"> [Serie lineare](PartDesign_LinearPattern/it.md)   * crea una serie lineare basata su una o più funzioni.


</div>

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width   *32px;"> [Serie polare](PartDesign_PolarPattern/it.md)   * crea una serie polare di una o più funzioni.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *32px;"> [Multitrasformazione](PartDesign_MultiTransform/it.md)   * crea una serie con qualsiasi combinazione delle altre trasformazioni.


</div>

#### Strumenti di abbellimento 


<div class="mw-translate-fuzzy">

Questi strumenti applicano un trattamento ai bordi o alle facce selezionate.


</div>

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width   *32px;"> [Raccordo](PartDesign_Fillet/it.md)   * raccorda (arrotonda) i bordi del corpo attivo.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width   *32px;"> [Smusso](PartDesign_Chamfer/it.md)   * smussa i bordi del corpo attivo.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width   *32px;"> [Sformo](PartDesign_Draft/it.md)   * applica uno sformo angolare alle facce selezionate nel corpo attivo.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width   *32px;"> [Spessore](PartDesign_Thickness/it.md)   * crea un guscio di dato spessore dal corpo attivo e apre le facce selezionate.


</div>

#### Booleane

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width   *32px;"> [Operazione booleana](PartDesign_Boolean/it.md)   * importa uno o più Corpi o Cloni PartDesign nel corpo attivo e applica un\'operazione booleana.

#### Extra

Alcune funzionalità aggiuntive che si trovano nel menu di Part Design   *

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width   *32px;"> [Migra](PartDesign_Migrate/it.md)   * migra nella versione 0.17 i file creati con versioni precedenti di FreeCAD. Se il file è basato su funzioni PartDesign, la migrazione dovrebbe riuscire. Se il file contiene oggetti Part, PartDesign e Draft misti, molto probabilmente la conversione fallisce.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width   *32px;"> [Procedura guidata per la progettazione delle ruote dentate](PartDesign_Sprocket/it.md)   * crea un profilo della ruota dentata che può essere estruso. <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_InternalExternalGear.svg  style="width   *32px;"> [Ingranaggio evolvente](PartDesign_InvoluteGear/it.md)   * crea un profilo di ingranaggio involuto che può essere estruso.


</div>

-   <img alt="" src=images/PartDesign_WizardShaft.svg  style="width   *32px;"> [Procedura guidata per alberi](PartDesign_WizardShaft/it.md)   * genera un albero da una tabella di valori e consente di analizzare forze e momenti. L\'albero è realizzato con uno schizzo ruotato che può essere modificato.

### Elementi del menu contestuale 

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width   *32px;"> [Imposta punta](PartDesign_MoveTip/it.md)   * ridefinisce la punta, che è la caratteristica esposta all\'esterno del corpo.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width   *32px;"> [Sposta oggetto in altro corpo](PartDesign_MoveFeature/it.md)   * sposta lo schizzo, la geometria di riferimento o la funzione selezionata in un altro corpo.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width   *32px;"> [Sposta l\'oggetto dopo un altro oggetto](PartDesign_MoveFeatureInTree/it.md)   * consente il riordino del corpo dell\'albero spostando lo schizzo selezionato, la geometria di riferimento o la funzione in un\'altra posizione nell\'elenco delle funzioni.

#### Elementi condivisi con l\'ambiente Part 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width   *32px;">[Aspetto](Std_SetAppearance/it.md)   * determina l\'aspetto dell\'intera parte (trasparenza del colore ecc.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width   *32px;"> [Imposta i colori](Part_FaceColors/it.md)   * assegna i colori alle facce delle parti.


<div class="mw-translate-fuzzy">

### Preferenze


</div>

-   <img alt="" src=images/Preferences-part_design.svg  style="width   *32px;"> [Preferenze](PartDesign_Preferences/it.md)   * preferenze disponibili negli strumenti PartDesign.
-   [Ottimizzare l\'installazione](Fine-tuning/it.md)   * alcuni parametri extra per ottimizzare il comportamento di PartDesign.

## Tutorial

-   [Come usare FreeCAD](http   *//help-freecad-jpg87.fr/), un sito web che descrive il flusso di lavoro per la progettazione meccanica.
-   [Creare una parte semplice con PartDesign](Creating_a_simple_part_with_PartDesign/it.md)
-   [Basi di Part Design](Basic_Part_Design_Tutorial/it.md)
-   [PartDesign Tutorial per i supporti dei cuscinetti I](PartDesign_Bearingholder_Tutorial_I/it.md) (da aggiornare)
-   [PartDesign Tutorial per i supporti dei cuscinetti II](PartDesign_Bearingholder_Tutorial_II/it.md) (da aggiornare)





 {{PartDesign_Tools_navi}}

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > PartDesign Workbench/it
