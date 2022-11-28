# <img alt="L\'icona di TechDraw" src=images/Workbench_TechDraw.svg  style="width   *64px;"> TechDraw Workbench/it

## Introduzione

L\'[Ambiente TechDraw](TechDraw_Workbench/it.md) <img alt="" src=images/Workbench_TechDraw.svg  style="width   *24px;"> serve per produrre disegni tecnici di base derivati dai modelli 3D creati con un altro ambiente di lavoro come [Part](Part_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md), o [Arch](Arch_Workbench/it.md), o importati da altre applicazioni. Ogni disegno è una pagina, che può contenere varie viste di oggetti disegnabili come Part   *   *Features, PartDesign   *   *Bodies, App   *   *Part groups, e gruppi Document Object. I disegni risultanti possono essere utilizzati per la documentazione, le istruzioni di costruzione, i contratti, i permessi, ecc.

Alla pagina possono essere aggiunte dimensioni, sezioni, aree tratteggiate, annotazioni e simboli [SVG](SVG/it.md), e la pagina può essere ulteriormente esportata in diversi formati come [DXF](DXF/it.md), [SVG](SVG/it.md), e [PDF](PDF/it.md).

TechDraw è stato ufficialmente incluso in FreeCAD a partire dalla versione 0.17; è destinato a sostituire l\'[ambiente Drawing](Drawing_Workbench/it.md) non più supportato. L\'ambiente Drawing è ancora fornito nella v0.20, ma non sarà disponibile nelle versioni future ({{VersionPlus/it|1.0}}). Per restare al passo con i piani e gli sviluppi di TechDraw, visita la [Roadmap di TechDraw](TechDraw_Roadmap/it.md).

Se il tuo obiettivo primario è la produzione di disegni 2D complessi, e di file [ DXF](DXF/it.md), e non si ha bisogno di modelli 3D, FreeCAD potrebbe non essere la scelta giusta per te. Dovresti invece prendere in considerazione un programma software dedicato al disegno tecnico, come [LibreCAD](https   *//en.wikipedia.org/wiki/LibreCAD) o [QCad](https   *//en.wikipedia.org/wiki/QCad).


{{TOCright}}

<img alt="" src=images/TechDraw_Workbench_Example.png  style="width   *600px;">

## Pagine

Questi sono gli strumenti per crere gli oggetti Pagine.

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width   *32px;"> [Nuovo disegno standard](TechDraw_PageDefault/it.md)   * aggiunge una nuova pagina utilizzando il [modello](TechDraw_Templates/it.md) predefinito.

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width   *32px;"> [Nuovo disegno da modello](TechDraw_PageTemplate/it.md)   * aggiunge una nuova pagina utilizzando un [modello](TechDraw_Templates/it.md) selezionato.

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width   *32px;"> [Ridisegna la pagina](TechDraw_RedrawPage/it.md)   * forza un aggiornamento della pagina selezionata. {{Version/it|0.19}}

-   <img alt="" src=images/TechDraw_PrintAll.svg  style="width   *32px;"> [Stampa tutte le pagine](TechDraw_PrintAll.md)   * stampa tutte le pagine di un documento. {{Version/it|1.0}}

## Viste

Questi sono gli strumenti per crere gli oggetti Viste.

-   <img alt="" src=images/TechDraw_View.svg  style="width   *32px;"> [Vista di oggetto](TechDraw_View/it.md)   * aggiunge una vista in proiezione 2D di un oggetto.

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width   *32px;"> [Vista attiva](TechDraw_ActiveView/it.md)   * inserisce una vista della vista 3D attiva. {{Version/it|0.19}}

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width   *32px;"> [Gruppo di proiezioni](TechDraw_ProjectionGroup/it.md)   * richiama una finestra di dialogo per creare viste multiple di un oggetto da diverse direzioni.

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Insert Section Views   *


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width   *32px;"> [Vista di sezione](TechDraw_SectionView/it.md)   * aggiunge una vista in sezione trasversale di una vista esistente.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ComplexSection.svg  style="width   *32px;"> [Inserisci vista di sezione complessa](TechDraw_ComplexSection/it.md)   * inserisce una sezione trasversale di una vista esistente basata su un profilo. {{Version/it|1.0}}


</div>

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width   *32px;"> [Dettaglio](TechDraw_DetailView/it.md)   * aggiunge una vista di dettaglio di una porzione di una vista esistente.

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width   *32px;"> [Vista di Draft](TechDraw_DraftView/it.md)   * aggiunge una vista di [Draft](Draft_Workbench/it.md) di un oggetto.

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width   *32px;"> [Vista di Arch](TechDraw_ArchView/it.md)   * aggiunge una vista di un oggetto [Piano di sezione](Arch_SectionPlane/it.md) di [Arch](Arch_Workbench/it.md).

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width   *32px;"> [Vista di foglio di calcolo](TechDraw_SpreadsheetView/it.md)   * inserisce in un disegno una vista di un [foglio di calcolo](Spreadsheet_Workbench/it.md) selezionato.

-   <img alt="" src=images/TechDraw_MoveView.svg  style="width   *32px;"> [Sposta vista](TechDraw_MoveView.md)   * sposta una vista e le sue dipendenze in una pagina diversa. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ShareView.svg  style="width   *32px;"> [Condividi vista](TechDraw_ShareView.md)   * condivide una vista tra più pagine. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ProjectShape.svg  style="width   *32px;"> [Proietta le forme](TechDraw_ProjectShape.md)   * crea proiezioni di forme nella [Vista 3D](3D_view/it.md). {{Version/it|0.20}}

## Sovrapposizioni

Questi sono strumenti per modificare l\'ordine di sovrapposizione che controlla la profondità apparente delle visualizzazioni su una pagina.

-   <img alt="" src=images/TechDraw_StackTop.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Modifica l\'ordine di sovrapposizione   *

   ** <img alt="" src=images/TechDraw_StackTop.svg  style="width   *32px;"> [Sposta la vista in cima alla sovrapposizione](TechDraw_StackTop/it.md)   * sposta le viste in cima all\'ordine di sovrapposizione. {{Version/it|1.0}}

   ** <img alt="" src=images/TechDraw_StackBottom.svg  style="width   *32px;"> [Sposta vista in basso alla sovrapposizione](TechDraw_StackBottom/it.md)   * sposta le viste in fondo all\'ordine di sovrapposizione. {{Version/it|1.0}}

   ** <img alt="" src=images/TechDraw_StackUp.svg  style="width   *32px;"> [Sposta la vista in alto di un livello](TechDraw_StackUp/it.md)   * sposta le viste in alto di un livello nell\'ordine di sovrapposizione. {{Version/it|1.0}}

   ** <img alt="" src=images/TechDraw_StackDown.svg  style="width   *32px;"> [Sposta la vista in basso di un livello](TechDraw_StackDown/it.md)   * sposta le viste in basso di un livello nell\'ordine di sovrapposizione. {{Version/it|1.0}}

## Clip

Questi sono strumenti per creare e gestire gli oggetti Clip (ritagli di viste).

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width   *32px;"> [Gruppo di clip](TechDraw_ClipGroup/it.md)   * inserisce un gruppo di clip in una pagina.

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width   *32px;"> [Aggiunge una vista al gruppo clip](TechDraw_ClipGroupAdd/it.md)   * aggiunge una vista esistente a un gruppo di clip.

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width   *32px;"> [Rimuovi la vista dal gruppo clip](TechDraw_ClipGroupRemove/it.md)   * rimuove una vista da un gruppo di clip.

## Aspetto

Si tratta di strumenti per modificare l\'aspetto delle pagine e della vista.

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width   *32px;"> [Tratteggio da modello](TechDraw_Hatch/it.md)   * applica a una faccia un modello di tratteggio preso da un file.

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width   *32px;"> [Tratteggio geometrico](TechDraw_GeometricHatch/it.md)   * tratteggia una faccia usando uno specifico Autodesk PAT.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width   *32px;"> [Simbolo SVG](TechDraw_Symbol/it.md)   * inserisce un simbolo [SVG](SVG/it.md) in una pagina.

-   <img alt="" src=images/TechDraw_Image.svg  style="width   *32px;"> [Immagine bitmap](TechDraw_Image/it.md)   * inserisce un\'immagine [bitmap](bitmap/it.md) PNG o JPG in una pagina.

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width   *32px;"> [Attiva o disattiva la cornice](TechDraw_ToggleFrame/it.md)   * mostra o nasconde le cornici e le etichette che circondano una vista.

## Dimensioni

Questi sono strumenti per creare e lavorare con gli oggetti Dimension.

Le dimensioni lineari possono essere basate su due punti, su una linea o su due linee.

-   <img alt="" src=images/TechDraw_LengthDimension.svg  style="width   *32px;"> [Inserisce una quota di lunghezza](TechDraw_LengthDimension/it.md)   * aggiunge una quota di lunghezza.

-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width   *32px;"> [Quota orizzontale](TechDraw_HorizontalDimension/it.md)   * aggiunge una quota orizzontale di lunghezza.

-   <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width   *32px;"> [Quota verticale](TechDraw_VerticalDimension/it.md)   * aggiunge una quota verticale.

-   <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width   *32px;"> [Raggio](TechDraw_RadiusDimension/it.md)   * aggiunge una quota radiale ad un cerchio o ad un arco.

-   <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width   *32px;"> [Diametro](TechDraw_DiameterDimension/it.md)   * aggiunge una quota diametrale ad un cerchio o ad un arco.

-   <img alt="" src=images/TechDraw_AngleDimension.svg  style="width   *32px;"> [Angolo](TechDraw_AngleDimension/it.md)   * aggiunge una quota angolare tra due bordi diritti.

-   <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width   *32px;"> [Angolo da 3 punti](TechDraw_3PtAngleDimension/it.md)   * aggiunge una quota angolare usando tre vertici.

-   <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Inserisci le linee di estensione   *

   ** <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width   *32px;"> [Estensione orizzontale](TechDraw_HorizontalExtentDimension/it.md)   * aggiunge una quota di estensione orizzontale. {{Version/it|0.19}}

   ** <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width   *32px;"> [Estensione verticale](TechDraw_VerticalExtentDimension/it.md)   * aggiunge una quota di estensione verticale. {{Version/it|0.19}}

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width   *32px;"> [Link alla geometria 3D](TechDraw_LinkDimension/it.md)   * collega una quota esistente alla geometria 3D.

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width   *32px;"> [Pallinatura](TechDraw_Balloon/it.md)   * aggiunge una pallinatura a una pagina. {{Version/it|0.19}}

-   <img alt="" src=images/TechDraw_LandmarkDimension.svg  style="width   *32px;"> [Quota da punti di riferimento](TechDraw_LandmarkDimension/it.md)   * aggiunge una quota basata su punti di riferimento. {{Version/it|0.19}}

## Annotazioni

Gli strumenti di annotazione servono per \"commentare\" un disegno con informazioni aggiuntive.

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width   *32px;"> [Annotazione](TechDraw_Annotation/it.md)   * aggiunge un blocco di testo normale da utilizzare come annotazione.

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width   *32px;"> [Linea guida](TechDraw_LeaderLine/it.md)   * aggiunge una linea di annotazione a una vista. {{Version/it|0.19}}

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width   *32px;"> [Blocco di testo](TechDraw_RichTextAnnotation/it.md)   * aggiunge un blocco di annotazione rich text a una [Linea guida](TechDraw_LeaderLine/it.md) o una vista. {{Version/it|0.19}}

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Aggiungi vertici cosmetici   *

   ** <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width   *32px;"> [Vertice cosmetico](TechDraw_CosmeticVertex/it.md)   * Lo strumento Vertice cosmetico aggiunge un vertice che non fa parte della geometria originale. {{Version/it|0.19}}

   ** <img alt="" src=images/TechDraw_Midpoints.svg  style="width   *32px;"> [Punti mediani](TechDraw_Midpoints/it.md)   * Lo strumento Punti mediani aggiunge dei Vertici cosmetici nei punti medi di uno o più bordi. {{Version/it|0.19}}

   ** <img alt="" src=images/TechDraw_Quadrants.svg  style="width   *32px;"> [Quadrante](TechDraw_Quadrants/it.md)   * Lo strumento Quadrante aggiunge dei Vertici cosmetici nei punti quarti di uno o più bordi circolari. {{Version/it|0.19}}

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Aggiungi linee assiali   *

   ** <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width   *32px;"> [Linea a centro faccia](TechDraw_FaceCenterLine/it.md)   * Lo strumento Linea a centro faccia aggiunge una linea centrale alle facce selezionate. {{Version/it|0.19}}

   ** <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width   *32px;"> [Linea centrale a 2 linee](TechDraw_2LineCenterLine/it.md)   * Lo strumento Linea a centro linee aggiunge una linea centrale tra 2 bordi. {{Version/it|0.19}}

   ** <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width   *32px;"> [Linea centrale a 2 punti](TechDraw_2PointCenterLine/it.md)   * Lo strumento Linea a centro punti aggiunge una linea centrale tra 2 punti. {{Version/it|0.19}}

-   <img alt="" src=images/TechDraw_2PointCosmeticLine.svg  style="width   *32px;"> [Linea Cosmetica tra due punti](TechDraw_2PointCosmeticLine/it.md)   * aggiunge una linea cosmetica che collega 2 vertici. {{Version/it|0.19}}

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width   *32px;"> [Rimuovi oggetto cosmetico](TechDraw_CosmeticEraser/it.md)   * Lo strumento Rimuovi oggetto cosmetico rimuove gli oggetti cosmetici da una pagina. {{Version/it|0.19}}

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width   *32px;"> [Aspetto delle linee](TechDraw_DecorateLine/it.md)   * Lo strumento DecorateLine modifica l\'aspetto dei bordi. {{Version/it|0.19}}

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width   *32px;"> [Mostra/nascondi i bordi invisibili](TechDraw_ShowAll/it.md)   * Lo strumento mostra o nasconde i bordi impostati invisibili in una vista. {{Version/it|0.19}}

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width   *32px;"> [Informazioni di saldatura](TechDraw_WeldSymbol/it.md)   * Lo strumento Informazioni di saldatura aggiunge le specifiche di saldatura a una linea guida esistente. {{Version/it|0.19}}

-   <img alt="" src=images/TechDraw_SurfaceFinishSymbol.svg  style="width   *32px;"> [Aggiunge Simbolo di Finitura Superficiale](TechDraw_SurfaceFinishSymbol/it.md)   * aggiunge un simbolo di finitura superficiale a una pagina. {{Version/it|1.0}}

## Estensioni

Questi sono strumenti per migliorare i tuoi disegni TechDraw.

### Attributi e modifiche 

-   <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width   *32px;"> [Seleziona attributi di linea, spaziatura in cascata e distanza delta](TechDraw_ExtensionSelectLineAttributes/it.md)   * seleziona gli attributi (stile, larghezza e colore) per le nuove linee cosmetiche e linee di centro e specifica la spaziatura in cascata e distanza delta. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionChangeLineAttributes.svg  style="width   *32px;"> [Cambia attributi linea](TechDraw_ExtensionChangeLineAttributes.md)   * cambia gli attributi (stile, larghezza e colore) delle linee cosmetiche e delle linee centrali. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Modifica la lunghezza delle linee cosmetiche o delle linee assiali   *

   ** <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width   *32px;"> [Estende Linea](TechDraw_ExtensionExtensionExtendLine/it.md)   * estende una linea cosmetica o una linea centrale a entrambe le estremità. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionShortenLine.svg  style="width   *32px;"> [Accorcia Linea](TechDraw_ExtensionShortenLine/it.md)   * accorcia una linea cosmetica o una linea centrale a entrambe le estremità. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionLockUnlockView.svg  style="width   *32px;"> [Blocca/sblocca Vista](TechDraw_ExtensionLockUnlockView/it.md)   * blocca o sblocca la posizione di una vista. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionPositionSectionView.svg  style="width   *32px;"> [Posiziona Vista di Sezione](TechDraw_ExtensionPositionSectionView/it.md)   * allinea ortogonalmente una vista di sezione alla sua vista sorgente. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Allinea le quote   *

   ** <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width   *32px;"> [Allinea Orizzontalmente una Catena di Quote](TechDraw_ExtensionPosHorizChainDimension/it.md)   * allinea le quote orizzontali per creare una quotatura a catena. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionPosVertChainDimension.svg  style="width   *32px;"> [Allinea Verticalmente una Catena di Quote](TechDraw_ExtensionPosVertChainDimension/it.md)   * allinea le quote verticali per creare una quotatura a catena. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionPosObliqueChainDimension.svg  style="width   *32px;"> [Allinea in Obliquo una Catena di Quote](TechDraw_ExtensionPosObliqueChainDimension/it.md)   * allinea le quote oblique per creare una quotatura a catena. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Distribuisci uniformemente le quote   *

   ** <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width   *32px;"> [Distanzia Quote Orizzontali](TechDraw_ExtensionCascadeHorizDimension/it.md)   * distanzia uniformemente le quote orizzontali. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionCascadeVertDimension.svg  style="width   *32px;"> [Distanzia Quote Verticali](TechDraw_ExtensionCascadeVertDimension/it.md)   * distanzia uniformemente le quote verticali. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionCascadeObliqueDimension.svg  style="width   *32px;"> [Distanzia Quote Oblique](TechDraw_ExtensionCascadeObliqueDimension/it.md)   * distanzia uniformemente le quote oblique. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionAreaAnnotation.svg  style="width   *32px;"> [Calcola l\'area delle facce selezionate](TechDraw_ExtensionAreaAnnotation/it.md)   * calcola l\'area delle facce selezionate e inserisce un\'annotazione dell\'area. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCustomizeFormat.svg  style="width   *32px;"> [Personalizza formato etichetta](TechDraw_ExtensionCustomizeFormat/it.md)   * personalizza la formattazione di un etichetta o di una quota. È possibile aggiungere simboli GD&T e altri caratteri speciali. {{Version/it|0.20}}

### Linee di centro e filettature 

-   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Aggiungi linee assiali   *

   ** <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width   *32px;"> [Aggiunge linee di Centro del Cerchio](TechDraw_ExtensionCircleCenterLines/it.md)   * aggiunge linee di centro a cerchi e archi. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionHoleCircle.svg  style="width   *32px;"> [Aggiunge Linee di Centro del Cerchio dei Bulloni](TechDraw_ExtensionHoleCircle/it.md)   * aggiunge le linee di centro ad una serie circolare di cerchi. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Aggiungi filetti cosmetici   *

   ** <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width   *32px;"> [Aggiunge Vista Laterale Filettatura Cosmetica Foro](TechDraw_ExtensionThreadHoleSide/it.md)   * aggiunge una filettatura cosmetica alla vista laterale di un foro. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width   *32px;"> [Aggiunge Vista Inferiore Filettatura Cosmetica Foro](TechDraw_ExtensionThreadHoleBottom/it.md)   * aggiunge una filettatura cosmetica alla vista superiore o inferiore dei fori. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width   *32px;"> [Aggiunge Vista Laterale Filettatura Cosmetica Bullone](TechDraw_ExtensionThreadBoltSide/it.md)   * aggiunge una filettatura cosmetica alla vista laterale di un bullone/vite/barra. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width   *32px;"> [Aggiunge Vista Inferiore Filettatura Cosmetica Bullone](TechDraw_ExtensionThreadBoltBottom/it.md)   * aggiunge una filettatura cosmetica alla vista superiore o inferiore di bulloni/viti/barre. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width   *32px;"> [Aggiunge Vertici di Intersezione Cosmetici](TechDraw_ExtensionVertexAtIntersection/it.md)   * aggiunge vertici cosmetici all\'intersezione dei bordi selezionati. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Aggiungi cerchi o archi cosmetici   *

   ** <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width   *32px;"> [Aggiunge Cerchio Cosmetico](TechDraw_ExtensionDrawCosmCircle/it.md)   * aggiunge un cerchio cosmetico basato su due vertici. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionDrawCosmArc.svg  style="width   *32px;"> [Aggiunge Arco Cosmetico](TechDraw_ExtensionDrawCosmArc/it.md)   * aggiunge un arco cosmetico in senso antiorario basato su tre vertici. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle3Points.svg  style="width   *32px;"> [Aggiunge un Cerchio Cosmetico per 3 Punti](TechDraw_ExtensionDrawCosmCircle3Points/it.md)   * aggiunge un cerchio cosmetico basato su tre vertici. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Aggiungi linee cosmetiche parallele o perpendicolari   *

   ** <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width   *32px;"> [Aggiunge Linea Parallela Cosmetica](TechDraw_ExtensionLineParallel/it.md)   * aggiunge una linea cosmetica parallela a un\'altra linea attraverso un vertice. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionLinePerpendicular.svg  style="width   *32px;"> [Aggiunge Linea Perpendicolare Cosmetica](TechDraw_ExtensionLinePerpendicular/it.md)   * aggiunge una linea cosmetica perpendicolare a un\'altra linea attraverso un vertice. {{Version/it|0.20}}

### Quote

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Crea quote concatenate   *

   ** <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width   *32px;"> [Crea una Catena Orizzontale di Quote](TechDraw_ExtensionCreateHorizChainDimension/it.md)   * crea una sequenza di quote orizzontali allineate. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionCreateVertChainDimension.svg  style="width   *32px;"> [Crea una Catena Verticale di Quote](TechDraw_ExtensionCreateVertChainDimension/it.md)   * crea una sequenza di quote verticali allineate. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionCreateObliqueChainDimension.svg  style="width   *32px;"> [Crea una Catena Obliqua di Quote](TechDraw_ExtensionCreateObliqueChainDimension/it.md)   * crea una sequenza di quote oblique allineate. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Crea quote coordinate   *

   ** <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width   *32px;"> [Crea Quote Coordinate Orizzontali](TechDraw_ExtensionCreateHorizCoordDimension/it.md)   * crea più quote orizzontali equidistanti a partire dalla stessa linea di base. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionCreateVertCoordDimension.svg  style="width   *32px;"> [Crea Quote Coordinate Verticali](TechDraw_ExtensionCreateVertCoordDimension/it.md)   * crea più quote verticali equidistanti a partire dalla stessa linea di base. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimension.svg  style="width   *32px;"> [Crea Quote Coordinate Oblique](TechDraw_ExtensionCreateObliqueCoordDimension/it.md)   * crea più quote oblique equidistanti a partire dalla stessa linea di base. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Crea quote di smusso   *

   ** <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width   *32px;"> [Crea Quota Smusso Orizzontale](TechDraw_ExtensionCreateHorizChamferDimension.md)   * crea una quota orizzontale e una quota angolare per uno smusso. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width   *32px;"> [Crea Quota Smusso Verticale](TechDraw_ExtensionCreateVertChamferDimension/it.md)   * crea una quota verticale e una quota angolare per uno smusso. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCreateLengthArc.svg  style="width   *32px;"> [Crea Quota Lunghezza Arco](TechDraw_ExtensionCreateLengthArc/it.md)   * crea una quota lunghezza arco. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Inserisci prefisso   *

   ** <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width   *32px;"> [Inserisce il Prefisso \'⌀\'](TechDraw_ExtensionInsertDiameter/it.md)   * inserisce un simbolo \'⌀\' all\'inizio del testo della quota. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionInsertSquare.svg  style="width   *32px;"> [Inserisce il Prefisso \'〼\'](TechDraw_ExtensionInsertSquare/it.md)   * inserisce un simbolo \'〼\' all\'inizio del testo della quota. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionRemovePrefixChar.svg  style="width   *32px;"> [Rimuove Prefisso](TechDraw_ExtensionRemovePrefixChar/it.md)   * rimuove tutti i simboli all\'inizio del testo della quota. {{Version/it|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Cambia le posizioni decimali   *

   ** <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width   *32px;"> [Aumenta Posizioni Decimali](TechDraw_ExtensionIncreaseDecimal/it.md)   * aumenta il numero di posizioni decimali del testo della quota. {{Version/it|0.20}}

   ** <img alt="" src=images/TechDraw_ExtensionDecreaseDecimal.svg  style="width   *32px;"> [Diminuisce Posizioni Decimali](TechDraw_ExtensionDecreaseDecimal/it.md)   * riduce il numero di posizioni decimali del testo della quota. {{Version/it|0.20}}

## Esportazione

Questi sono gli strumenti per esportare le pagine in altre applicazioni.

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width   *32px;"> [Esporta pagina in SVG](TechDraw_ExportPageSVG/it.md)   * salva la pagina corrente come file [SVG](SVG/it.md).

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width   *32px;"> [Esporta Pagina in DXF](TechDraw_ExportPageDXF/it.md)   * salva la pagina corrente come file [DXF](DXF/it.md).

## Ulteriori funzioni 

-   [Gruppi di linee](TechDraw_LineGroup/it.md)   * si possono assegnare valori di default a vari tipi di linee.
-   [Modelli di squadrature](TechDraw_Templates/it.md)   * i modelli predefiniti per le pagine di disegno di TechDraw.
-   [Tipi di tratteggio](TechDraw_Hatching/it.md)   * spiegazione delle diverse tecniche di tratteggio.
-   [Dimensionamento e tolleranza geometrica](TechDraw_Geometric_dimensioning_and_tolerancing/it.md)   * spiegazione su come realizzare la quotatura geometrica e la tolleranza.

## Preferenze

-   <img alt="" src=images/Preferences-techdraw.svg  style="width   *32px;"> [Preferenze di TechDraw](TechDraw_Preferences/it.md)   * le preferenze per i valori predefiniti della pagina di disegno come l\'angolo di proiezione, i colori, le dimensioni del testo e gli stili di linea.

## Scripting


<div class="mw-translate-fuzzy">

Gli strumenti TechDraw possono essere utilizzati nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando due API.

-   [API TechDraw](TechDraw_API/it.md)
-   [API TechDrawGui](TechDrawGui_API/it.md)


</div>

## Limitazioni

-   I disegni di TechDraw e le relative API non sono intercambiabili con i disegni di [Drawing](Drawing_Workbench/it.md) e le relative API. È possibile convertire le pagine di Drawing in pagine TechDraw utilizzando uno script Python (`moveViews.py`).
-   Nello stesso documento di FreeCAD è possibile avere sia pagine di TechDraw che pagine di Drawing, poiché ciascuna pagina è completamente indipendente l\'una dall\'altra.
-   Ci sono alcune piccole differenze nello specificare i testi modificabili nei modelli [SVG](SVG/it.md) rispetto al modulo Drawing. In TechDraw il ridimensionamento del documento SVG influisce sulla posizione dei campi di testo modificabili. Per maggiori dettagli vedere la discussione sul forum [TechDraw templates scale](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=24981&p=196271#p196271).
-   Non tagliare, copiare e incollare oggetti TechDraw nella [Vista ad Albero](Tree_view/it.md) poiché generalmente non funziona bene.
-   Non trascinare oggetti TechDraw nella [Vista ad Albero](Tree_view/it.md) con il mouse.

## Tutorial

-   [Tutorial base di TechDraw](Basic_TechDraw_Tutorial/it.md)   * introduzione alla creazione di disegni con TechDraw.
-   [Come creare dei modelli TechDraw personalizzati](TechDraw_TemplateHowTo/it.md)   * istruzioni per creare un nuovo modello di pagina in Inkscape per l\'utilizzo con TechDraw.
-   [TechDraw Generatore di Modelli](TechDraw_TemplateGenerator/it.md)   * istruzioni per creare una macro per generare un template di base.

   *   L\'aggiunta di \"poche\" righe di codice genera uno strumento come [Macro TemplateHelper](Macro_TemplateHelper/it.md).

-   [Misura degli angoli sui fori](Measurement_Of_Angles_On_Holes/it.md)   * istruzioni per l\'aggiunta delle linee d\'asse e delle successive rappresentazioni degli angoli sui fori.
-   [Informazioni pratiche su TechDraw](TechDraw_HowTo_Page/it.md)   * istruzioni per diverse impostazioni come i segni di centratura, ecc.
-   [TechDraw Tutorial Pitch Circle](TechDraw_Pitch_Circle_Tutorial.md)   * istruzioni per aggiungere un pitch circle.

Video tutorial di sliptonic

-   TechDraw Workbench [Part 1 (Basics)](https   *//www.youtube.com/watch?v=7LbOmSGW9F0), [Part 2 (Dimensions)](https   *//www.youtube.com/watch?v=z3w84RfvqaE), [Part 3 (Multiview)](https   *//www.youtube.com/watch?v=uNjXg-m38aI)
-   TechDraw Workbench [Part 4 (Section and Detail)](https   *//www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Customizing Templates)](https   *//www.youtube.com/watch?v=kcmdJ7xa7gg)





{{TechDraw_Tools_navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > TechDraw Workbench/it
