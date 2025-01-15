# <img alt="L\'icona di TechDraw" src=images/Workbench_TechDraw.svg  style="width:64px;"> TechDraw Workbench/it



## Introduzione

L\'[Ambiente TechDraw](TechDraw_Workbench/it.md) <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> serve per produrre disegni tecnici di base derivati dai modelli 3D creati con un altro ambiente di lavoro come [Part](Part_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md), o [BIM](BIM_Workbench/it.md), o importati da altre applicazioni. Ogni disegno è una pagina, che può contenere varie viste di oggetti disegnabili come Part::Features, PartDesign::Bodies, App::Part groups, e gruppi Document Object. I disegni risultanti possono essere utilizzati per la documentazione, le istruzioni di costruzione, i contratti, i permessi, ecc.

Alla pagina possono essere aggiunte dimensioni, sezioni, aree tratteggiate, annotazioni e simboli [SVG](SVG/it.md), e la pagina può essere ulteriormente esportata in diversi formati come [DXF](DXF/it.md), [SVG](SVG/it.md), e [PDF](PDF/it.md).

Se il tuo obiettivo primario è la produzione di disegni 2D complessi, e di file [ DXF](DXF/it.md), e non si ha bisogno di modelli 3D, FreeCAD potrebbe non essere la scelta giusta per te. Dovresti invece prendere in considerazione un programma software dedicato al disegno tecnico, come [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD) o [QCad](https://en.wikipedia.org/wiki/QCad).




<img alt="" src=images/TechDraw_Workbench_Example.png  style="width:600px;">



### Aggancio


{{Version/it|1.0}}

: L\'Ambiente TechDraw ha una funzione di aggancio. Può essere utilizzato per allineare automaticamente viste, viste in sezione e quote durante il posizionamento mediante trascinamento con il mouse. Con **Allineamento vista a scatto** abilitato (impostazione predefinita) nelle [preferenze](TechDraw_Preferences/it#Snapping.md), le viste si agganceranno all\'allineamento con altre viste quando abbastanza vicine (impostazione **Fattore di aggancio vista**). Le quote vengono inoltre agganciate ad altre quote parallele e il testo della quota può essere agganciato al centro della linea di quota. L\'aggancio può essere temporaneamente disabilitato tenendo premuto il tasto **Alt**.



## Strumenti



### Pagine

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [Inserisci Pagina predefinita](TechDraw_PageDefault/it.md): aggiunge una nuova pagina utilizzando il [modello](TechDraw_Templates/it.md) predefinito.

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> [Inserisci Pagina usando un modello](TechDraw_PageTemplate/it.md): aggiunge una nuova pagina utilizzando un [modello](TechDraw_Templates/it.md) selezionato.

-   <img alt="" src=images/TechDraw_FillTemplateFields.svg  style="width:32px;"> [Aggiorna campi del modello](TechDraw_FillTemplateFields/it.md): {{Version/it|1.0}}

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width:32px;"> [Ridisegna Pagina](TechDraw_RedrawPage/it.md): forza un aggiornamento della pagina selezionata.

-   <img alt="" src=images/TechDraw_PrintAll.svg  style="width:32px;"> [Stampa tutte le Pagine](TechDraw_PrintAll/it.md): stampa tutte le pagine di un documento. {{Version/it|0.21}}

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width:32px;"> [Esporta pagina in SVG](TechDraw_ExportPageSVG/it.md): salva la pagina corrente come file [SVG](SVG/it.md).

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width:32px;"> [Esporta Pagina in DXF](TechDraw_ExportPageDXF/it.md): salva la pagina corrente come file [DXF](DXF/it.md).



### Viste



#### Viste TechDraw 

-   <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [Inserisci Vista](TechDraw_View/it.md): aggiunge una rappresentazione di uno o più oggetti. {{Version/it|1.0}}: Può creare una singola vista, un [Gruppo di proiezione](TechDraw_ProjectionGroup/it.md), una [Vista di foglio di calcolo](TechDraw_SpreadsheetView/it.md), una [Vista di Arch](TechDraw_ArchView/it.md), un [ Simbolo](TechDraw_Symbol/it.md) o una [Vista immagine](TechDraw_Image/it.md).

-   <img alt="" src=images/TechDraw_BrokenView.svg  style="width:32px;"> [Inserisci Vista interrotta](TechDraw_BrokenView/it.md): aggiunge una vista interrotta di uno o più oggetti. {{Version/it|1.0}}

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Inserisci Vista Sezione semplice](TechDraw_SectionView/it.md): aggiunge una vista in sezione trasversale di una vista esistente.

-   <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:32px;"> [Inserisci Vista Sezione complessa](TechDraw_ComplexSection/it.md): inserisce una sezione trasversale di una vista esistente basata su un profilo. {{Version/it|0.21}}

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [Inserisci Vista dettaglio](TechDraw_DetailView/it.md): aggiunge una vista di dettaglio di una porzione di una vista esistente.

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Inserisci Gruppo di proiezioni](TechDraw_ProjectionGroup/it.md): richiama una finestra di dialogo per creare viste multiple di un oggetto da diverse direzioni. {{Version/it|1.0}}: è possibile utilizzare al suo posto lo strumento [Inserisci Vista](TechDraw_View/it.md).

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width:32px;"> [Inserisci Gruppo di ritaglio](TechDraw_ClipGroup/it.md): inserisce un gruppo di ritaglio.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width:32px;"> [Simbolo SVG](TechDraw_Symbol/it.md): inserisce un simbolo [SVG](SVG/it.md) in una pagina. {{Version/it|1.0}}: è possibile utilizzare al suo posto lo strumento [Inserisci Vista](TechDraw_View/it.md).

-   <img alt="" src=images/TechDraw_Image.svg  style="width:32px;"> [Immagine bitmap](TechDraw_Image/it.md): inserisce un\'immagine [bitmap](bitmap/it.md) PNG o JPG in una pagina. {{Version/it|1.0}}: è possibile utilizzare al suo posto lo strumento [Inserisci Vista](TechDraw_View/it.md).

-   <img alt="" src=images/TechDraw_ShareView.svg  style="width:32px;"> [Condividi vista](TechDraw_ShareView.md): condivide una vista tra più pagine.

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Attiva o disattiva la cornice](TechDraw_ToggleFrame/it.md): mostra o nasconde le cornici e le etichette che circondano una vista.

-   <img alt="" src=images/TechDraw_ProjectShape.svg  style="width:32px;"> [Proietta le forme](TechDraw_ProjectShape.md): crea proiezioni di forme nella [Vista 3D](3D_view/it.md).



#### Viste da altri ambienti di lavoro 

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Inserisci Vista attiva](TechDraw_ActiveView/it.md): inserisce una vista della vista 3D attiva.

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> [Inserisci Vista di Draft](TechDraw_DraftView/it.md): aggiunge una vista di [Draft](Draft_Workbench/it.md) di un oggetto.

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [Inserisci Vista di BIM](TechDraw_ArchView/it.md): aggiunge una vista di un oggetto [Piano di sezione](Arch_SectionPlane/it.md) di [BIM](BIM_Workbench/it.md). {{Version/it|1.0}}: è possibile utilizzare al suo posto lo strumento [Inserisci Vista](TechDraw_View/it.md).

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> [Inserisci Vista di un foglio di calcolo](TechDraw_SpreadsheetView/it.md): inserisce in un disegno una vista di un [foglio di calcolo](Spreadsheet_Workbench/it.md) selezionato. {{Version/it|1.0}}: è possibile utilizzare al suo posto lo strumento [Inserisci Vista](TechDraw_View/it.md).



### Impilamento

Questi sono strumenti per modificare l\'ordine di impilamento che controlla la profondità apparente delle visualizzazioni su una pagina.

-   <img alt="" src=images/TechDraw_StackTop.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Modifica l\'ordine di impilamento:

  - <img alt="" src=images/TechDraw_StackTop.svg  style="width:32px;"> [Sposta la vista in cima alla pila](TechDraw_StackTop/it.md): sposta le viste in cima alla pila di ordinamento. {{Version/it|0.21}}

  - <img alt="" src=images/TechDraw_StackBottom.svg  style="width:32px;"> [Sposta la vista in fondo alla pila](TechDraw_StackBottom/it.md): sposta le viste in fondo alla pila di ordinamento. {{Version/it|0.21}}

  - <img alt="" src=images/TechDraw_StackUp.svg  style="width:32px;"> [Sposta la vista su di un livello](TechDraw_StackUp/it.md): sposta le viste su di un livello lungo la pila di ordinamento. {{Version/it|0.21}}

  - <img alt="" src=images/TechDraw_StackDown.svg  style="width:32px;"> [Sposta la vista giù di un livello](TechDraw_StackDown/it.md): sposta le viste giù di un livello lungo la pila di ordinamento. {{Version/it|0.21}}



### Quotatura

-   <img alt="" src=images/TechDraw_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Quote:

  - <img alt="" src=images/TechDraw_Dimension.svg  style="width:32px;"> [Inserisci Quota](TechDraw_Dimension/it.md): aggiunge una quota contestuale. {{Version/it|1.0}}

  - <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:32px;"> [Inserisci Quota allineata](TechDraw_LengthDimension/it.md): aggiunge una quota allineata.

  - <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:32px;"> [Inserisci Quota orizzontale](TechDraw_HorizontalDimension/it.md): aggiunge una quota orizzontale.

  - <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:32px;"> [Inserisci Quota verticale](TechDraw_VerticalDimension/it.md): aggiunge una quota verticale.

  - <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:32px;"> [Inserisci Quota raggio](TechDraw_RadiusDimension/it.md): aggiunge una quota radiale ad un cerchio o ad un arco.

  - <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:32px;"> [Inserisci Quota diametro](TechDraw_DiameterDimension/it.md): aggiunge una quota diametrale ad un cerchio o ad un arco.

  - <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:32px;"> [Inserisci Quota angolare](TechDraw_AngleDimension/it.md): aggiunge una quota angolare tra due bordi diritti.

  - <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:32px;"> [Inserisci Quota angolare da 3 punti](TechDraw_3PtAngleDimension/it.md): aggiunge una quota angolare usando tre vertici.

  - <img alt="" src=images/TechDraw_AreaDimension.svg  style="width:32px;"> [Inserisci Annotazione Area](TechDraw_AreaDimension/it.md): aggiunge la quota dell\'area di una faccia. {{Version/it|1.0}}

  - <img alt="" src=images/TechDraw_ExtensionCreateLengthArc.svg  style="width:32px;"> [Crea Quota Lunghezza Arco](TechDraw_ExtensionCreateLengthArc/it.md): crea una quota lunghezza arco.

  -  <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width:32px;"> [Inserisci Quota estensione orizzontale](TechDraw_HorizontalExtentDimension/it.md): aggiunge una quota di estensione orizzontale.

  - <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width:32px;"> [Inserisci Quota estensione verticale](TechDraw_VerticalExtentDimension/it.md): aggiunge una quota di estensione verticale.

  -  <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width:32px;"> [Crea Quote in Serie Orizzontale](TechDraw_ExtensionCreateHorizChainDimension/it.md): crea una sequenza di quote orizzontali allineate.

  - <img alt="" src=images/TechDraw_ExtensionCreateVertChainDimension.svg  style="width:32px;"> [Crea Quote in Serie Verticale](TechDraw_ExtensionCreateVertChainDimension/it.md): crea una sequenza di quote verticali allineate.

  - <img alt="" src=images/TechDraw_ExtensionCreateObliqueChainDimension.svg  style="width:32px;"> [Crea Quote in Serie Obliqua](TechDraw_ExtensionCreateObliqueChainDimension/it.md): crea una sequenza di quote oblique allineate.

  - <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width:32px;"> [Crea Quote in Parallelo Orizzontali](TechDraw_ExtensionCreateHorizCoordDimension/it.md): crea più quote orizzontali equidistanti a partire dalla stessa linea di base.

  - <img alt="" src=images/TechDraw_ExtensionCreateVertCoordDimension.svg  style="width:32px;"> [Crea Quote in Parallelo Verticali](TechDraw_ExtensionCreateVertCoordDimension/it.md): crea più quote verticali equidistanti a partire dalla stessa linea di base.

  - <img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimension.svg  style="width:32px;"> [Crea Quote in Parallelo Oblique](TechDraw_ExtensionCreateObliqueCoordDimension/it.md): crea più quote oblique equidistanti a partire dalla stessa linea di base.

  - <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width:32px;"> [Crea Quota Smusso Orizzontale](TechDraw_ExtensionCreateHorizChamferDimension/it.md): crea una quota orizzontale e una quota angolare per uno smusso.

  - <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width:32px;"> [Crea Quota Smusso Verticale](TechDraw_ExtensionCreateVertChamferDimension/it.md): crea una quota verticale e una quota angolare per uno smusso.

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width:32px;"> [Inserisci Pallinatura](TechDraw_Balloon/it.md): aggiunge una \"pallinatura\" annotativa a una pagina.

-   <img alt="" src=images/TechDraw_AxoLengthDimension.svg  style="width:32px;"> [Inserisci quota lunghezza assonometrica](TechDraw_AxoLengthDimension/it.md): aggiunge una quota di lunghezza assonometrica. {{Version/it|0.21}}

-   <img alt="" src=images/TechDraw_LandmarkDimension.svg  style="width:32px;"> [Quota da punti di riferimento - SPERIMENTALE](TechDraw_LandmarkDimension/it.md): aggiunge una quota basata su punti di riferimento.

-   <img alt="" src=images/TechDraw_DimensionRepair.svg  style="width:32px;"> [Ripara quota](TechDraw_DimensionRepair/it.md): può regolare i riferimenti geometrici 2D o 3D di una quota. {{Version/it|0.21}}

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:32px;"> [Collega Quota alla geometria 3D](TechDraw_LinkDimension/it.md): collega una quota esistente alla geometria 3D (deprecata).



### Tratteggio

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Tratteggia una Faccia usando un file immagine](TechDraw_Hatch/it.md): applica a una faccia un modello di tratteggio preso da un file.

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Applica un Tratteggio geometrico a una Faccia](TechDraw_GeometricHatch/it.md): tratteggia una faccia usando uno specifico Autodesk PAT.



### Annotazioni

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Inserisci Annotazione](TechDraw_Annotation/it.md): aggiunge un blocco di testo normale da utilizzare come annotazione.

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width:32px;"> [Aggiungi Linea guida alla vista](TechDraw_LeaderLine/it.md): aggiunge una linea guida a una vista.

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:32px;"> [Inserisci Blocco di testo](TechDraw_RichTextAnnotation/it.md): aggiunge un blocco di annotazione rich text a una linea guida o ad una vista.

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Aggiungi vertici cosmetici:

  - <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:32px;"> [Aggiungi Vertice cosmetico](TechDraw_CosmeticVertex/it.md): aggiunge un vertice che non fa parte della geometria originale.

  - <img alt="" src=images/TechDraw_Midpoints.svg  style="width:32px;"> [Aggiungi Punti mediani](TechDraw_Midpoints/it.md): aggiunge dei Vertici Cosmetici nei punti mediani dei bordi selezionati.

  - <img alt="" src=images/TechDraw_Quadrants.svg  style="width:32px;"> [Aggiungi Vertici Quadrante](TechDraw_Quadrants/it.md): aggiunge dei Vertici Cosmetici nei punti quarti dei bordi (circolari) selezionati.

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Aggiungi Linee centrali:

  - <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:32px;"> [Aggiungi Linea centrale alla faccia](TechDraw_FaceCenterLine/it.md): aggiunge una linea centrale alle facce selezionate.

  - <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:32px;"> [Aggiungi Linea centrale tra 2 linee](TechDraw_2LineCenterLine/it.md): aggiunge una linea centrale tra 2 linee.

  - <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:32px;"> [Aggiungi Linea centrale tra 2 punti](TechDraw_2PointCenterLine/it.md): aggiunge una linea centrale tra 2 punti.

-   <img alt="" src=images/TechDraw_2PointCosmeticLine.svg  style="width:32px;"> [Aggiungi Linea Cosmetica tra due punti](TechDraw_2PointCosmeticLine/it.md): aggiunge una linea cosmetica che collega 2 vertici.

-   <img alt="" src=images/TechDraw_CosmeticCircle.svg  style="width:32px;"> [Aggiungi Cerchio Cosmetico](TechDraw_CosmeticCircle/it.md): aggiunge un cerchio cosmetico. {{Version/it|1.0}}

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:32px;"> [Cambia Aspetto delle linee](TechDraw_DecorateLine/it.md): modifica l\'aspetto delle linee selezionate.

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width:32px;"> [Mostra/nascondi i bordi invisibili](TechDraw_ShowAll/it.md): mostra/nasconde le linee/bordi invisibili in una vista.

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:32px;"> [Aggiungi Informazioni di saldatura](TechDraw_WeldSymbol/it.md): aggiunge le specifiche di saldatura a una linea guida esistente.

-   <img alt="" src=images/TechDraw_SurfaceFinishSymbols.svg  style="width:32px;"> [Aggiungi Simbolo di Finitura Superficiale](TechDraw_SurfaceFinishSymbols/it.md): aggiunge un simbolo di finitura superficiale a una pagina. {{Version/it|0.21}}

-   <img alt="" src=images/TechDraw_HoleShaftFit.svg  style="width:32px;"> [Accoppiamento foro/albero](TechDraw_HoleShaftFit/it.md): aggiunge le tolleranze del foro o dell\'albero utilizzando ISO 286 a una quota. {{Version/it|0.21}}



### Estensioni



#### Attributi e modifiche 

-   <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width:32px;"> [Seleziona attributi di linea, spaziatura in cascata e distanza delta](TechDraw_ExtensionSelectLineAttributes/it.md): seleziona gli attributi (stile, larghezza e colore) per le nuove linee cosmetiche e linee di centro e specifica la spaziatura in cascata e distanza delta.

-   <img alt="" src=images/TechDraw_ExtensionChangeLineAttributes.svg  style="width:32px;"> [Cambia attributi linea](TechDraw_ExtensionChangeLineAttributes/it.md): cambia gli attributi (stile, larghezza e colore) delle linee cosmetiche e delle linee centrali.

-   <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Modifica la lunghezza delle linee cosmetiche o delle linee assiali:

  - <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width:32px;"> [Estendi linea](TechDraw_ExtensionExtendLine/it.md): estende una linea cosmetica o una linea centrale ad entrambe le estremità.

  - <img alt="" src=images/TechDraw_ExtensionShortenLine.svg  style="width:32px;"> [Accorcia linea](TechDraw_ExtensionShortenLine/it.md): accorcia una linea cosmetica o una linea centrale ad entrambe le estremità.

-   <img alt="" src=images/TechDraw_ExtensionLockUnlockView.svg  style="width:32px;"> [Blocca/sblocca Vista](TechDraw_ExtensionLockUnlockView/it.md): blocca o sblocca la posizione di una vista.

-   <img alt="" src=images/TechDraw_ExtensionPositionSectionView.svg  style="width:32px;"> [Allinea Vista di Sezione](TechDraw_ExtensionPositionSectionView/it.md): allinea ortogonalmente una vista di sezione alla sua vista sorgente.

-   <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Allinea le quote:

  - <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width:32px;"> [Allinea in Serie Quote Orizzontali](TechDraw_ExtensionPosHorizChainDimension/it.md): allinea le quote orizzontalmente per creare una quotatura in serie.

  - <img alt="" src=images/TechDraw_ExtensionPosVertChainDimension.svg  style="width:32px;"> [Allinea in Serie Quote Verticali](TechDraw_ExtensionPosVertChainDimension/it.md): allinea le quote verticali per creare una quotatura in serie.

  - <img alt="" src=images/TechDraw_ExtensionPosObliqueChainDimension.svg  style="width:32px;"> [Allinea in Serie Quote Oblique](TechDraw_ExtensionPosObliqueChainDimension/it.md): allinea le quote oblique per creare una quotatura in serie.

-   <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Distribuisci uniformemente le quote:

  - <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width:32px;"> [Distanzia in Parallelo Quote Orizzontali](TechDraw_ExtensionCascadeHorizDimension/it.md): distanzia uniformemente le quote orizzontali.

  - <img alt="" src=images/TechDraw_ExtensionCascadeVertDimension.svg  style="width:32px;"> [Distanzia in Parallelo Quote Verticali](TechDraw_ExtensionCascadeVertDimension/it.md): distanzia uniformemente le quote verticali.

  - <img alt="" src=images/TechDraw_ExtensionCascadeObliqueDimension.svg  style="width:32px;"> [Distanzia in Parallelo Quote Oblique](TechDraw_ExtensionCascadeObliqueDimension/it.md): distanzia uniformemente le quote oblique.

-   <img alt="" src=images/TechDraw_ExtensionAreaAnnotation.svg  style="width:32px;"> [Calcola l\'area delle facce selezionate](TechDraw_ExtensionAreaAnnotation/it.md): calcola l\'area delle facce selezionate e inserisce un\'annotazione dell\'area.

-   <img alt="" src=images/TechDraw_ExtensionArcLengthAnnotation.svg  style="width:32px;"> [Calcola la lunghezza dell\'arco dei bordi selezionati](TechDraw_ExtensionArcLengthAnnotation/it.md): calcola la lunghezza dell\'arco dei bordi selezionati e inserisce un\'annotazione sulla lunghezza dell\'arco. {{Version/it|1.0}}

-   <img alt="" src=images/TechDraw_ExtensionCustomizeFormat.svg  style="width:32px;"> [Personalizza formato etichetta](TechDraw_ExtensionCustomizeFormat/it.md): personalizza la formattazione di un etichetta o di una quota. È possibile aggiungere simboli GD&T e altri caratteri speciali.



#### Linee di centro e filettature 

-   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Aggiungi linee assiali:

  - <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:32px;"> [Aggiungi linee di Centro del Cerchio](TechDraw_ExtensionCircleCenterLines/it.md): aggiunge linee di centro a cerchi e archi.

  - <img alt="" src=images/TechDraw_ExtensionHoleCircle.svg  style="width:32px;"> [Aggiungi Linee di Centro del Cerchio dei Bulloni](TechDraw_ExtensionHoleCircle/it.md): aggiunge le linee di centro ad una serie circolare di cerchi.

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Aggiungi filetti cosmetici:

  - <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:32px;"> [Aggiungi Vista Laterale Filettatura Cosmetica Foro](TechDraw_ExtensionThreadHoleSide/it.md): aggiunge una filettatura cosmetica alla vista laterale di un foro.

  - <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:32px;"> [Aggiungi Vista Inferiore Filettatura Cosmetica Foro](TechDraw_ExtensionThreadHoleBottom/it.md): aggiunge una filettatura cosmetica alla vista superiore o inferiore dei fori.

  - <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:32px;"> [Aggiungi Vista Laterale Filettatura Cosmetica Bullone](TechDraw_ExtensionThreadBoltSide/it.md): aggiunge una filettatura cosmetica alla vista laterale di un bullone/vite/barra.

  - <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:32px;"> [Aggiungi Vista Inferiore Filettatura Cosmetica Bullone](TechDraw_ExtensionThreadBoltBottom/it.md): aggiunge una filettatura cosmetica alla vista superiore o inferiore di bulloni/viti/barre.

-   <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Aggiungi vertici:

ː\* <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width:32px;"> [Aggiungi Vertici di Intersezione Cosmetici](TechDraw_ExtensionVertexAtIntersection/it.md): aggiunge vertici cosmetici all\'intersezione dei bordi selezionati.

  - <img alt="" src=images/TechDraw_CommandAddOffsetVertex.svg  style="width:32px;"> [Aggiungi un vertice di offset](TechDraw_CommandAddOffsetVertex.md): aggiunge un vertice cosmetico ad un offset specificato da un vertice selezionato. {{Version/it|1.0}}

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Aggiungi cerchi o archi cosmetici:

  - <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width:32px;"> [Aggiungi Cerchio Cosmetico](TechDraw_ExtensionDrawCosmCircle/it.md): aggiunge un cerchio cosmetico basato su due vertici.

  - <img alt="" src=images/TechDraw_ExtensionDrawCosmArc.svg  style="width:32px;"> [Aggiungi Arco Cosmetico](TechDraw_ExtensionDrawCosmArc/it.md): aggiunge un arco cosmetico in senso antiorario basato su tre vertici.

  - <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle3Points.svg  style="width:32px;"> [Aggiungie un Cerchio Cosmetico per 3 Punti](TechDraw_ExtensionDrawCosmCircle3Points/it.md): aggiunge un cerchio cosmetico basato su tre vertici.

-   <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Aggiungi linee cosmetiche parallele o perpendicolari:

  - <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width:32px;"> [Aggiungi Linea Parallela Cosmetica](TechDraw_ExtensionLineParallel/it.md): aggiunge una linea cosmetica parallela a un\'altra linea attraverso un vertice.

  - <img alt="" src=images/TechDraw_ExtensionLinePerpendicular.svg  style="width:32px;"> [Aggiungi Linea Perpendicolare Cosmetica](TechDraw_ExtensionLinePerpendicular/it.md): aggiunge una linea cosmetica perpendicolare a un\'altra linea attraverso un vertice.



#### Quote

Molti degli strumenti per le estensioni sono elencati in [Quote](#Quote.md) sopra.

-   <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Inserisci prefisso:

  - <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width:32px;"> [Inserisci il Prefisso \'⌀\'](TechDraw_ExtensionInsertDiameter/it.md): inserisce un simbolo \'⌀\' all\'inizio del testo della quota.

  - <img alt="" src=images/TechDraw_ExtensionInsertSquare.svg  style="width:32px;"> [Inserisci il Prefisso \'□\'](TechDraw_ExtensionInsertSquare/it.md): inserisce un simbolo \'□\' all\'inizio del testo della quota.

  - <img alt="" src=images/TechDraw_ExtensionInsertRepetition.svg  style="width:32px;"> [Inserisci il Prefisso \'n×\'](TechDraw_ExtensionInsertRepetition/it.md): inserisce un conteggio di elementi ripetuti all\'inizio del testo della quota. {{Version/it|1.0}}

  - <img alt="" src=images/TechDraw_ExtensionRemovePrefixChar.svg  style="width:32px;"> [Rimuovi Prefisso](TechDraw_ExtensionRemovePrefixChar/it.md): rimuove tutti i simboli all\'inizio del testo della quota.

-   <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Cambia le posizioni decimali:

  - <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width:32px;"> [Aumenta Posizioni Decimali](TechDraw_ExtensionIncreaseDecimal/it.md): aumenta il numero di posizioni decimali del testo della quota.

  - <img alt="" src=images/TechDraw_ExtensionDecreaseDecimal.svg  style="width:32px;"> [Diminuisce Posizioni Decimali](TechDraw_ExtensionDecreaseDecimal/it.md): riduce il numero di posizioni decimali del testo della quota.



### Varie

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:32px;"> [Rimuovi oggetto cosmetico](TechDraw_CosmeticEraser/it.md): rimuove gli oggetti cosmetici da una pagina.



### Strumenti obsoleti 

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width:32px;"> [Aggiunge una vista al gruppo clip](TechDraw_ClipGroupAdd/it.md): aggiunge una vista esistente a un gruppo di clip. Non disponibile in {{VersionPlus/it|1.0}}.

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width:32px;"> [Rimuovi la vista dal gruppo clip](TechDraw_ClipGroupRemove/it.md): rimuove una vista da un gruppo di clip. Non disponibile in {{VersionPlus/it|1.0}}.

-   <img alt="" src=images/TechDraw_MoveView.svg  style="width:32px;"> [Sposta vista](TechDraw_MoveView.md): sposta una vista e le sue dipendenze in una pagina diversa. Non disponibile in {{VersionPlus/it|1.0}}.



## Ulteriori funzioni 

-   [Gruppi di linee](TechDraw_LineGroup/it.md): si possono assegnare valori di default a vari tipi di linee.
-   [Modelli di squadrature](TechDraw_Templates/it.md): i modelli predefiniti per le pagine di disegno di TechDraw.
-   [Tipi di tratteggio](TechDraw_Hatching/it.md): spiegazione delle diverse tecniche di tratteggio.
-   [Dimensionamento e tolleranza geometrica](TechDraw_Geometric_dimensioning_and_tolerancing/it.md): spiegazione su come realizzare la quotatura geometrica e la tolleranza.



## Preferenze

-   <img alt="" src=images/Preferences-techdraw.svg  style="width:32px;"> [Preferenze di TechDraw](TechDraw_Preferences/it.md): le preferenze per i valori predefiniti della pagina di disegno come l\'angolo di proiezione, i colori, le dimensioni del testo e gli stili di linea.

## Scripting

Gli strumenti TechDraw possono essere utilizzati nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) utilizzando due API. Per maggiori informazioni vedere:

-   [Autogenerated API documentation](https://freecad.github.io/SourceDoc/)
-   [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)
-   [Campi di testo modificabili](TechDraw_PageDefault/it#Campi_di_testo_modificabili.md)



## Limitazioni

-   Non tagliare, copiare e incollare oggetti TechDraw nella [Vista ad albero](Tree_view/it.md) poiché generalmente non funziona bene.
-   Non trascinare gli oggetti TechDraw nella [Vista ad albero](Tree_view/it.md) con il mouse.



## Tutorial

-   [Tutorial base di TechDraw](Basic_TechDraw_Tutorial/it.md): introduzione alla creazione di disegni con TechDraw.
-   [Come creare dei modelli TechDraw personalizzati](TechDraw_TemplateHowTo/it.md): istruzioni per creare un nuovo modello di pagina in Inkscape per l\'utilizzo con TechDraw.
-   [TechDraw Generatore di Modelli](TechDraw_TemplateGenerator/it.md): istruzioni per creare una macro per generare un template di base.

:   L\'aggiunta di \"poche\" righe di codice genera uno strumento come [Macro TemplateHelper](Macro_TemplateHelper/it.md).

-   [Misura degli angoli sui fori](Measurement_Of_Angles_On_Holes/it.md): istruzioni per l\'aggiunta delle linee d\'asse e delle successive rappresentazioni degli angoli sui fori.
-   [Informazioni pratiche su TechDraw](TechDraw_HowTo_Page/it.md): istruzioni per diverse impostazioni come i segni di centratura, ecc.
-   [TechDraw Tutorial Pitch Circle](TechDraw_Pitch_Circle_Tutorial.md): istruzioni per aggiungere un pitch circle.

Video tutorial di sliptonic

-   TechDraw Workbench [Part 1 (Basics)](https://www.youtube.com/watch?v=7LbOmSGW9F0), [Part 2 (Dimensions)](https://www.youtube.com/watch?v=z3w84RfvqaE), [Part 3 (Multiview)](https://www.youtube.com/watch?v=uNjXg-m38aI)
-   TechDraw Workbench [Part 4 (Section and Detail)](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Customizing Templates)](https://www.youtube.com/watch?v=kcmdJ7xa7gg)



## Sviluppo

Vuoi conoscere il futuro di TechDraw Workbench? Visita [la pagina della roadmap di TechDraw](TechDraw_Roadmap/it.md) per saperne di più.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [TechDraw](Category_TechDraw.md) > TechDraw Workbench/it
