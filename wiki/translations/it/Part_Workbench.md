# <img alt="L\'icona dell\'ambiente Part" src=images/Workbench_Part.svg  style="width:64px;"> Part Workbench/it






## Introduzione

L**\'Ambiente Part** <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> fornisce un flusso di lavoro tradizionale [geometria solida costruttiva](Constructive_solid_geometry/it.md) (CSG). In questo flusso di lavoro ogni oggetto è un solido indipendente. L\'ambiente Part può creare questi oggetti da [schizzi](Sketcher_Workbench/it.md) definiti parametricamente utilizzando strumenti come [Estrusione](Part_Extrude/it.md), [Rivoluzione](Part_Revolve/it.md), [Loft](Part_Loft/it.md), ecc. Inoltre, è possibile creare dei solidi con primitive di base come [Cubo](Part_Box/it.md), [Cilindro](Part_Cylinder/it.md), ecc. Questi oggetti possono essere combinati, tramite [Operazioni booleane](Part_Boolean/it.md), per creare solidi più complessi.

L\'ambiente Part può anche creare oggetti che non sono solidi, come facce, gusci e oggetti con solo bordi o vertici. Fornisce inoltre una varietà di strumenti generici per la manipolazione della geometria, la convalida della geometria e la creazione di copie.

L\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [Ambiente PartDesign](PartDesign_Workbench/it.md) utilizza un flusso di lavoro alternativo per la creazione di solidi. Per una discussione dettagliata dell\'ambiente Part e dell\'ambiente Part Design vedere [Part e Part Design](Part_and_PartDesign/it.md).

![](images/Part_Workbench_Example.jpg )



## Gli strumenti 



### Barra degli strumenti Solidi 

-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cubo](Part_Box/it.md): Crea un cubo.

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cilindro](Part_Cylinder/it.md): Crea un cilindro.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sfera](Part_Sphere/it.md): Crea una sfera.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cono](Part_Cone/it.md): Crea un cono.

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Toro](Part_Torus/it.md): Crea un toro.

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Tubo](Part_Tube/it.md): Crea un tubo.

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Crea primitive\...](Part_Primitives/it.md): uno strumento per creare una delle seguenti primitive:

  - <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Piano](Part_Plane/it.md): crea un piano.

  - <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cubo](Part_Box/it.md): crea un cubo. Questo oggetto può anche essere creato con lo strumento [Cubo](Part_Box/it.md).

  - <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cilindro](Part_Cylinder/it.md): crea un cilindro. Questo oggetto può anche essere creato con lo strumento [Cilindro](Part_Cylinder/it.md).

  - <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cono](Part_Cone/it.md): crea un cono. Questo oggetto può anche essere creato con lo strumento [Cono](Part_Cone/it.md).

  - <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sfera](Part_Sphere/it.md): crea una sfera. Questo oggetto può anche essere creato con lo strumento [Sfera](Part_Sphere/it.md).

  - <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellissoide](Part_Ellipsoid/it.md): crea un ellissoide.

  - <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Toro](Part_Torus/it.md): crea un toro. Questo oggetto può anche essere creato con lo strumento [Toro](Part_Torus/it.md).

  - <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prisma](Part_Prism/it.md): crea un prisma.

  - <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Cuneo](Part_Wedge/it.md) crea un cuneo.

  - <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Elica](Part_Helix/it.md): crea un\'elica.

  - <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spirale](Part_Spiral/it.md): crea una spirale.

  - <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Cerchio](Part_Circle/it.md): crea un arco circolare.

  - <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellisse](Part_Ellipse/it.md): crea un arco ellittico.

  - <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Punto](Part_Point/it.md): crea un punto.

  - <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Linea](Part_Line/it.md): crea una linea.

  - <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Poligono regolare](Part_RegularPolygon/it.md): crea un poligono regolare.

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Crea una forma\...](Part_Builder/it.md): Crea forme partendo da varie primitive.



### Barra degli strumenti Strumenti Part 

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Crea schizzo](Sketcher_NewSketch/it.md): crea un nuovo schizzo e apre la finestra [Dialogo Schizzo](Sketcher_Dialog/it.md) per modificarlo.

-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Estrudi](Part_Extrude/it.md): Estrude facce planari.

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Rivoluziona](Part_Revolve/it.md): Crea un solido tramite la rivoluzione di un oggetto (non solido) attorno ad un asse.

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Specchia](Part_Mirror/it.md): Riflette l\'oggetto selezionato rispetto ad un asse stabilito.

-   <img alt="" src=images/Part_Scale.svg  style="width:32px;"> [Scala](Part_Scale/it.md): Ridimensiona una o più forme. {{Version/it|1.0}}

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Raccorda](Part_Fillet/it.md): Raccorda (arrotonda) i bordi di un oggetto.

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Smussa](Part_Chamfer/it.md): Smussa i bordi di un oggetto.

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Crea faccia](Part_MakeFace/it.md): Crea una faccia da un insieme di linee (contorni).

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Superficie rigata](Part_RuledSurface/it.md): Crea una superficie rigata.

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Loft](Part_Loft/it.md): Loft da un profilo all\'altro.

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Sweep](Part_Sweep/it.md): fa scorrere uno o più profili lungo un percorso.

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Seziona](Part_Section/it.md): Crea una sezione intersecando un oggetto con un piano di sezione.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Sezioni\...](Part_CrossSections/it.md): Crea una o più sezioni trasversali attraverso un oggetto.

-   <img alt="" src=images/Part_Offset.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Offset:

  - <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [Offset 3D](Part_Offset/it.md): Crea una forma parallela ad una data distanza dall\'originale.

  - <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [Offset 2D](Part_Offset2D/it.md): Crea un contorno parallelo ad una certa distanza dall\'originale, ingrandisce o contrae una faccia piana.

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Spessore](Part_Thickness/it.md): Svuota un solido.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Proiezione su superficie](Part_ProjectionOnSurface/it.md): Proietta un logo, un testo o qualsiasi faccia, polilinea o bordo su una superficie.

-   <img alt="" src=images/Part_ColorPerFace.svg  style="width:32px;"> [Colore per faccia](Part_ColorPerFace/it.md): assegna i colori alle singole facce degli oggetti.



### Barra degli strumenti Boolean 

-   <img alt="" src=images/Part_Compound.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Composto:

  - <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Crea un composto](Part_Compound/it.md): Crea un composto dagli oggetti selezionati.

  - <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Esplodi composto](Part_ExplodeCompound/it.md): Divide i composti.

  - <img alt="" src=images/Part_Compound‏‎Filter.svg  style="width:32px;"> [Filtra composto](Part_CompoundFilter/it.md): Estrae i singoli pezzi di un composto.

-   <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Operazione booleana](Part_Boolean/it.md): Esegue operazioni booleane su due oggetti.

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Sottrai](Part_Cut/it.md): Sottrae un oggetto da un altro.

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Unisci](Part_Fuse/it.md): Unisce (fonde) due o più oggetti.

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Interseca](Part_Common/it.md): Estrae la parte comune (intersezione) di due oggetti.

-   <img alt="" src=images/Part_JoinConnect.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Giunzione:

  - <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Congiungi oggetti](Part_JoinConnect/it.md): Congiunge le facce interne di oggetti con pareti (es. tubi).

  - <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Incorpora oggetto](Part_JoinEmbed/it.md): Incorpora un oggetto con pareti in un altro oggetto con pareti.

  - <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Ritaglio per l\'oggetto](Part_JoinCutout/it.md): Crea un ritaglio nella parete di un oggetto per un altro oggetto con pareti.

-   <img alt="" src=images/Part_BooleanFragments.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Suddivisione:

  - <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Frammenti booleani](Part_BooleanFragments/it.md): Crea qualsiasi pezzo ottenendolo da operazioni booleane.

  - <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Affetta in parti](Part_SliceApart/it.md): Taglia e divide un oggetto intersecandolo con altri oggetti.

  - <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Affetta in composto](Part_Slice/it.md): Taglia un oggetto intersecandolo con altri oggetti.

  - <img alt="" src=images/Part_XOR.svg  style="width:32px;"> [XOR booleano](Part_XOR/it.md): Rimuove lo spazio condiviso da un numero pari di oggetti.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Controlla la geometria](Part_CheckGeometry/it.md): Controlla se la geometria degli oggetti selezionati contiene degli errori.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Elimina funzioni](Part_Defeaturing/it.md): Rimuove le funzioni da un oggetto.



### Altri strumenti 

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Importa file CAD\...](Part_Import/it.md): Importazione da file \*.IGES, \*.STEP, o \*.BREP.

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Esporta file CAD\...](Part_Export/it.md): Esportazione in file \*.IGES, \*.STEP, o \*.BREP.

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [Box di selezione](Part_BoxSelection/it.md): Seleziona le facce da un\'area rettangolare.

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Crea forma da mesh](Part_ShapeFromMesh/it.md): Crea forme (shapes) da oggetti mesh.

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Crea oggetto punti da geometria](Part_PointsFromMesh/it.md): Crea oggetti punti a partire da oggetti geometrici.

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;">[Converti in solido](Part_MakeSolid/it.md): Crea solidi a partire da oggetti forma (shape).

-   <img alt="" src=images/Part_ReverseShape.svg  style="width:32px;"> [Inverti le forme](Part_ReverseShape/it.md): Crea copie parametriche degli oggetti selezionati con normali delle facce invertite.

-   Creare una copia:

  - <img alt="" src=images/Part_SimpleCopy‎.svg  style="width:32px;"> [Crea una copia semplice](Part_SimpleCopy/it.md): Crea copie non parametriche di oggetti.

  - <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Crea una copia modificata](Part_TransformedCopy/it.md): Crea copie non parametriche di oggetti. È destinato agli oggetti nidificati in contenitori.

  - <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Crea una copia di un elemento](Part_ElementCopy/it.md): Crea copie non parametriche di sottoelementi: vertici, bordi e facce.

  - <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Affina una forma](Part_RefineShape/it.md): Crea copie parametriche con una forma raffinata da oggetti selezionati. Rimuove i bordi non necessari dalle facce planari e cilindriche.

-   <img alt="" src=images/Part_EditAttachment.svg  style="width:32px;"> [Associazione\...](Part_EditAttachment/it.md): Associa un oggetto ad uno o più altri oggetti.



## Strumenti obsoleti 



### Misura

Lo strumento <img alt="" src=images/Std_Measure.svg  style="width:32px;"> [Misurare](Std_Measure/it.md) sostituisce gli strumenti elencati di seguito. {{Version/it|1.0}}

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Misura lineare](Part_Measure_Linear/it.md) Crea una misura lineare. Non disponibile nella {{VersionPlus/it|1.0}}.

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Misura angolare](Part_Measure_Angular/it.md): Crea una misura angolare. Non disponibile nella {{VersionPlus/it|1.0}}.

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Aggiorna misure](Part_Measure_Refresh/it.md): Aggiorna tutte le misure. Non disponibile nella {{VersionPlus/it|1.0}}.

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Cancella Tutto](Part_Measure_Clear_All/it.md): Cancella tutte le misure. Non disponibile nella {{VersionPlus/it|1.0}}.

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Attiva o Disattiva tutte le misure](Part_Measure_Toggle_All/it.md) e [Attiva o Disattiva Vista Tutte le Misure](View_Measure_Toggle_All/it.md): Mostra o nasconde tutte le misure. Non disponibile nella <small>(v1.0)</small> .

-   <img alt="" src=images/Part_Measure_Toggle_3D.svg  style="width:32px;"> [Attiva o Disattiva le misure 3D](Part_Measure_Toggle_3D/it.md): Mostra o nasconde le misure 3D. Non disponibile nella <small>(v1.0)</small> .

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Attiva o Disattiva le misure Delta](Part_Measure_Toggle_Delta/it.md): Mostra o nasconde le misure delta. Non disponibile nella <small>(v1.0)</small> .



## Preferenze

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferenze](PartDesign_Preferences/it.md): Preferenze per l\'Ambiente Part.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preferenze di Importa e esporta](Import_Export_Preferences/it.md): preferenze per l\'importazione e l\'esportazione in diversi formati di file.
-   [Ottimizzazione](Fine-tuning/it#Part_Workbench.md): Alcuni parametri extra per mettere a punto il comportamento di Part.



## Script

Vedere [Script di Part](Part_scripting/it.md)



## Tutorial

-   [Importare da STL o OBJ](Import_from_STL_or_OBJ/it.md) : come importare file STL/OBJ in FreeCAD
-   [Esportare in STL o OBJ](Export_to_STL_or_OBJ/it.md) : come esportare file STL/OBJ da FreeCAD
-   [Tutorial Sfera traforata](Whiffle_Ball_tutorial/it.md) : come usare il modulo Part



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Category_Part.md) > Part Workbench/it
