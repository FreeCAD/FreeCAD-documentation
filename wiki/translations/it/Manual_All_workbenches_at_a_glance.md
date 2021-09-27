# Manual:All workbenches at a glance/it
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC/it}}

Per i nuovi utenti di FreeCAD una delle maggiori difficoltà è quella di sapere in quale ambiente di lavoro trovare uno strumento specifico. La tabella sottostante fornisce una panoramica degli ambienti più importanti e dei loro strumenti. Per un elenco più completo fare riferimento alla pagina della documentazione di FreeCAD per ciascun [ ambiente](Workbenches/it.md).

Quattro ambienti sono inoltre progettati per lavorare in coppia, e uno di loro è completamente incluso nell\'altro: Architettura contiene tutti gli strumenti di Draft, e PartDesign tutti gli strumenti di Sketcher. Tuttavia, per chiarezza, qui sono separati.

### Parte

L\'ambiente Parte fornisce gli strumenti di base per lavorare con le parti solide: primitive, come cubi e sfere, e operazioni geometriche semplici e operazioni booleane. Essendo il punto di ancoraggio principale con [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology), l\'ambiente Parte fornisce le fondamenta del sistema di geometria di FreeCAD, e quasi tutti gli altri ambienti producono della geometria basata su Part.


<div class="mw-translate-fuzzy">

  Tool                                                                                                                           Descrizione                                                                Tool                                                                                                                               Descrizione
  ------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------
  <img alt="" src=images/Part_Box.png  style="width:32px;"> _                                                 Disegna un cono
  <img alt="" src=images/Part_Cylinder.png  style="width:32px;"> _                                          Disegna una sfera
  <img alt="" src=images/Part_Torus.png  style="width:32px;"> _   Crea varie altre primitive geometriche parametriche
  <img alt="" src=images/Part_Shapebuilder.png  style="width:32px;"> _                                            Unisce (fonde) due oggetti
  <img alt="" src=images/Part_Common.png  style="width:32px;"> _                                                  Taglia (sottrae) un oggetto da un altro
  <img alt="" src=images/Part_JoinConnect.png  style="width:32px;"> _                             Incorpora un oggetto con pareti in un altro oggetto analogo
  <img alt="" src=images/Part_JoinCutout.png  style="width:32px;"> _                                     Estrude le facce piane di un oggetto
  <img alt="" src=images/Part_Fillet.png  style="width:32px;"> _                                 Crea un solido ruotando un altro oggetto (non solido) attorno ad un asse
  <img alt="" src=images/Part_Section.png  style="width:32px;"> _                      Crea più sezioni trasversali lungo un oggetto
  <img alt="" src=images/Part_Chamfer.png  style="width:32px;"> _                                       Specchia l\'oggetto selezionato in un determinato piano di specchio
  <img alt="" src=images/Part_RuledSurface.png  style="width:32px;"> _                                             Spazza uno o più profili lungo un percorso
  <img alt="" src=images/Part_Loft.png  style="width:32px;"> _                                         Crea una copia in scala dell\'oggetto originale
  <img alt="" src=images/Part_Thickness.png  style="width:32px;"> [Spessore](Part_Thickness/it.md)                          Assegna uno spessore alle facce di una forma                                                                                                                                                                  


</div>

### Draft

L\'ambiente Draft fornisce gli strumenti per fare disegni di base CAD 2D: linee, cerchi, ecc \... e una serie di utili strumenti generici come spostare, ruotare o scalare. Esso fornisce inoltre diversi aiuti di disegno, come la griglia e l\'aggancio. Esso è pensato principalmente per disegnare le linee guida per gli oggetti di Arch, ma serve anche come \"coltellino svizzero\" di FreeCAD.


<div class="mw-translate-fuzzy">

  Tool                                                                                                                         Descrizione                                                        Tool                                                                                                                     Descrizione
  ---------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------
  <img alt="" src=images/Draft_Line.png  style="width:32px;"> _                                    Disegna una linea composta da più segmenti (polilinea)
  <img alt="" src=images/Draft_Circle.png  style="width:32px;"> _                                       Disegna un arco da centro, raggio, angolo iniziale e angolo finale
  <img alt="" src=images/Draft_Ellipse.png  style="width:32px;">_                       Disegna un poligono regolare da un centro e un raggio
  <img alt="" src=images/Draft_Rectangle.png  style="width:32px;"> _                                   Disegna un testo di annotazione multi-linea
  <img alt="" src=images/Draft_Dimension.png  style="width:32px;"> _                        Disegna una B-Spline da una serie di punti
  <img alt="" src=images/Draft_Point.png  style="width:32px;"> _     Inserisce in un dato punto nel documento corrente una forma composta che riproduce una stringa di testo
  <img alt="" src=images/Draft_Facebinder.png  style="width:32px;"> _             Disegna una curva di Bezier da una serie di punti
  <img alt="" src=images/Draft_Move.png  style="width:32px;"> _                             Ruota gli oggetti di un certo angolo attorno ad un punto
  <img alt="" src=images/Draft_Offset.png  style="width:32px;"> _                  Tronca, estende o estrude un oggetto
  <img alt="" src=images/Draft_Upgrade.png  style="width:32px;"> _                Converte o separa gli oggetti in un oggetto di livello inferiore
  <img alt="" src=images/Draft_Scale.png  style="width:32px;"> _   Crea un oggetto 2D ottenuto dalla proiezione di un altro oggetto
  <img alt="" src=images/Draft_Draft2Sketch.png  style="width:32px;"> _                              Crea una serie polare o rettangolare da un oggetto
  <img alt="" src=images/Draft_PathArray.png  style="width:32px;"> _                                Crea copie collegate di oggetti
  <img alt="" src=images/Draft_Mirror.png  style="width:32px;"> [Specchia](Draft_Mirror/it.md)                              Specchia oggetti rispetto a una linea                                                                                                                                                       


</div>

### Sketcher

L\'ambiente Sketcher contiene gli strumenti per costruire e modificare gli oggetti 2D complessi, chiamati schizzi. La geometria all\'interno di questi disegni può essere posizionata con precisione e relazionata usando i vincoli. Gli schizzi sono destinati principalmente ad essere i mattoni della geometria di PartDesign, ma in FreeCAD sono utili ovunque.


<div class="mw-translate-fuzzy">

  Tool                                                                                                                                                                 Descrizione                                                                                                                                                                Tool                                                                                                                                                           Descrizione
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/Sketcher_CreatePoint.png  style="width:32px;"> _                                                          Disegna un segmento da 2 punti
  <img alt="" src=images/Sketcher_Arc.png  style="width:32px;"> _                     Disegna un arco da due punti finali e un altro punto sulla circonferenza
  <img alt="" src=images/Sketcher_Circle.png  style="width:32px;"> _         Disegna un cerchio da tre punti sulla circonferenza
  <img alt="" src=images/Sketcher_CreateEllipse.png  style="width:32px;"> _   Disegna un\'ellisse da diametro maggiore (2 punti) e punto su raggio minore
  <img alt="" src=images/Sketcher_CreateArcOfEllipse.png  style="width:32px;"> _                              Disegna una linea fatta di molteplici segmenti di linea. Sono disponibili diverse modalità di disegno
  <img alt="" src=images/Sketcher_CreateRectangle.png  style="width:32px;"> _                              Disegna un triangolo regolare inscritto in un cerchio di geometria di costruzione
  <img alt="" src=images/Sketcher_CreateSquare.png  style="width:32px;"> _                              Disegna un pentagono regolare inscritto in un cerchio di geometria di costruzione
  <img alt="" src=images/Sketcher_CreateHexagon.png  style="width:32px;"> _                               Disegna un ettagono regolare inscritto in un cerchio di geometria di costruzione
  <img alt="" src=images/Sketcher_CreateOctagon.png  style="width:32px;"> _                                              Disegna un\'asola selezionando il centro di un semicerchio e un punto finale dell\'altro semicerchio
  <img alt="" src=images/Sketcher_CreateFillet.png  style="width:32px;"> _                                                   Tronca una linea, un cerchio o un arco in un dato punto cliccato
  <img alt="" src=images/Sketcher_External.png  style="width:32px;"> _                Commuta un elemento da/in modalità di costruzione. Un oggetto costruzione non è utilizzato in un\'operazione di geometria 3D ed è visibile solo durante la modifica dello schizzo che lo contiene
  <img alt="" src=images/Constraint_PointOnPoint.png  style="width:32px;"> _             Sovrappone un punto su un altro oggetto come una linea, un arco o un asse.
  <img alt="" src=images/Constraint_Vertical.png  style="width:32px;"> _                           Vincola le linee selezionate o gli elementi di una polilinea ad avere un orientamento orizzontale. Prima di applicare questo vincolo si può selezionare più di un oggetto.
  <img alt="" src=images/Constraint_Parallel.png  style="width:32px;"> _               Vincola due linee perpendicolari tra loro, o vincola una linea perpendicolare ad un punto finale di un arco.
  <img alt="" src=images/Constraint_Tangent.png  style="width:32px;"> _                         Vincoli due entità selezionate uguali fra loro. Se usato su cerchi o archi vengono posti uguali i loro raggi.
  <img alt="" src=images/Constraint_Symmetric.png  style="width:32px;"> _                                    Vincola l\'elemento selezionato impostando le distanze verticale e orizzontale rispetto all\'origine, bloccando in tal modo la posizione di tale elemento
  <img alt="" src=images/Constraint_HorizontalDistance.png  style="width:32px;"> _         Fissa la distanza verticale tra due punti o tra i punti finali della linea. Se viene selezionato un solo elemento, la distanza è impostata dall\'origine.
  <img alt="" src=images/Constraint_Length.png  style="width:32px;"> _                                            Definisce il raggio di un arco o cerchio selezionato vincolando il raggio.
  <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> _                           Vincola due linee ad obbedire ad una legge di rifrazione per simulare il passaggio della luce attraverso un\'interfaccia
  <img alt="" src=images/Constraint_InternalAlignment.png  style="width:32px;"> _                                          Mappa uno schizzo sulla faccia di un solido selezionata in precedenza
  <img alt="" src=images/Sketcher_MergeSketch.png  style="width:32px;"> _                                     Riflette gli elementi selezionati in uno schizzo


</div>

### Part Design 

L\'ambiente Part Design contiene strumenti avanzati per costruire parti solide. Esso contiene inoltre tutti gli strumenti di Sketcher. Dato che può produrre solo forme solide (la regola numero uno di Parte Design), è il principale ambiente da utilizzare nella progettazione di pezzi (parti) da produrre come manufatti o stampare in 3D, poiché si ottengono sempre oggetti stampabili.


<div class="mw-translate-fuzzy">

  Tool                                                                                                                                       Descrizione                                                                               Tool                                                                                                                                                    Descrizione
  ------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/PartDesign_Pad.png  style="width:32px;"> _                                            Crea una tasca da uno schizzo selezionato. Il disegno deve essere mappato sulla faccia di un oggetto solido esistente
  <img alt="" src=images/PartDesign_Revolution.png  style="width:32px;"> _                                              Crea una gola rivoluzionando uno schizzo attorno ad un asse
  <img alt="" src=images/PartDesign_Fillet.png  style="width:32px;"> _                                         Smussa i bordi di un oggetto
  <img alt="" src=images/PartDesign_Draft.png  style="width:32px;"> _                                  Specchia le funzioni su un piano o una faccia
  <img alt="" src=images/PartDesign_LinearPattern.png  style="width:32px;"> _                    Crea una schiera polare di funzioni
  <img alt="" src=images/PartDesign_Scaled.png  style="width:32px;"> _   Permette di creare una schiera con una qualsiasi combinazione delle altre trasformazioni
  <img alt="" src=images/PartDesign_WizardShaft.png  style="width:32px;"> _            Consente di creare diversi tipi di ingranaggi


</div>

### Arch

L\'ambiente Arch contiene gli strumenti per lavorare con i progetti [BIM](https://en.wikipedia.org/wiki/Building_information_modeling) (ingegneria civile e architettura). Esso contiene inoltre tutti gli strumenti dell\'ambiente Draft. Arch è usato principalmente per creare oggetti BIM o dare gli attributi BIM agli oggetti costruiti con altri ambienti, al fine di esportarli in [IFC](https://en.wikipedia.org/wiki/Industry_Foundation_Classes).


<div class="mw-translate-fuzzy">

  Tool                                                                                                  Descrizione                                                           Tool                                                                                                                     Descrizione
  ----------------------------------------------------------------------------------------------------- --------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------
  <img alt="" src=images/Arch_Wall.png  style="width:32px;"> _                   Crea un elemento strutturale da zero o utilizzando un oggetto selezionato come base
  <img alt="" src=images/Arch_Rebar.png  style="width:32px;"> _                                   Crea un piano includendo gli oggetti selezionati
  <img alt="" src=images/Arch_Building.png  style="width:32px;"> _                                       Crea un sito includendo gli oggetti selezionati
  <img alt="" src=images/Arch_Window.png  style="width:32px;"> _   Aggiunge un oggetto piano di sezione al documento
  <img alt="" src=images/Arch_Axis.png  style="width:32px;"> _                                      Crea una falda del tetto da una faccia selezionata
  <img alt="" src=images/Arch_Space.png  style="width:32px;"> _                                Crea un oggetto scala nel documento
  <img alt="" src=images/Arch_Panel.png  style="width:32px;"> _                                  Crea un oggetto telaio da uno schema selezionato
  <img alt="" src=images/Arch_Equipment.png  style="width:32px;"> _             Attribuisce un materiale agli oggetti selezionati
  <img alt="" src=images/Arch_Schedule.png  style="width:32px;"> _               Taglia un oggetto con un piano
  <img alt="" src=images/Arch_Add.png  style="width:32px;"> _                              Sottrae o rimuove oggetti da un componente
  <img alt="" src=images/Arch_Survey.png  style="width:32px;"> [Ispeziona](Arch_Survey/it.md)         Entra o esce dalla modalità di ispezione                                                                                                                                                       


</div>

### Drawing


<div class="mw-translate-fuzzy">

L\'ambiente Drawing (Disegno) gestisce la creazione e la manipolazione dei fogli con i disegni 2D, utilizzati per visualizzare le viste in 2D del modello 3D. Questi fogli possono poi essere esportati in applicazioni 2D in formato SVG o DXF, in un file PDF o stampati.


</div>

The Drawing Workbench handles the creation and manipulation of 2D drawing sheets, used for displaying views of your 3D work in 2D. These sheets can then be exported to 2D applications in SVG or DXF formats, to a PDF file or printed.

  Tool                                                                                                                          Descrizione                                                                           Tool                                                                                                                        Descrizione
  ----------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------
  <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> _                                Inserisce una vista dell\'oggetto selezionato nel foglio di disegno attivo
  <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> _                              Aggiunge un inserto nel foglio di disegno corrente
  <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> _   Crea automaticamente le viste ortogonali di un oggetto sul foglio di disegno corrente
  <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> _        Inserisce nel foglio di disegno corrente una speciale Vista di Draft dell\'oggetto selezionato
  <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Salva](Drawing_Save/it.md)                                  Salva il foglio corrente in un file in formato SVG                                                                                                                                                                

### Altri ambienti incorporati 

Quanto sopra riassume i più importanti strumenti di FreeCAD, ma sono disponibili molti altri ambienti di lavoro, tra i quali:


<div class="mw-translate-fuzzy">

-   L\'ambiente [Mesh](Mesh_Workbench/it.md) permette di lavorare con le [mesh poligonali](https://en.wikipedia.org/wiki/Polygon_mesh). Anche se le mesh (maglie) non sono il tipo di geometria preferito con cui lavorare in FreeCAD, a causa della loro mancanza di precisione e di supporto per le curve, le mesh sono ancora molto usate, e sono pienamente supportate in FreeCAD. L\'ambiente Mesh offre anche una serie di strumenti \"da Part a Mesh\" e \"da Mesh a Part\".
-   L\'ambiente [Raytracing](Raytracing_Workbench/it.md) offre strumenti per interfacciarsi con i renderer esterni come POV-Ray o LuxRender. Proprio da dentro FreeCAD, questo ambiente permette di produrre rendering di alta qualità dai modelli.
-   L\'ambiente [Spreadsheet](Spreadsheet_Workbench.md) permette di creare e manipolare i dati dei fogli di calcolo, che possono essere estratti dai modelli FreeCAD. Le celle del foglio possono anche essere usate da riferimento per molti settori (campi di inserimento dati) di FreeCAD, e questo permette di usarle come base di dati.
-   L\'ambiente [FEM](FEM_Workbench.md) si occupa di [Finite Elements Analysis](https://en.wikipedia.org/wiki/Finite_element_method), e consente di effettuare i calcoli pre e post-elaborazione FEA e di visualizzare i risultati graficamente.


</div>

### Ambienti esterni 

Esistono anche numerosi altri ambienti molto utili, prodotti dai membri della comunità FreeCAD. Anche se non sono inclusi in una installazione standard di FreeCAD, sono facili da installare come plug-in. Essi sono tutti referenziati nel repositorio [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons). Tra i più sviluppati ci sono:


<div class="mw-translate-fuzzy">

-   L\'ambiente [Drawing Dimensioning](https://github.com/hamish2014/FreeCAD_drawing_dimensioning) offre molti nuovi strumenti per lavorare direttamente su fogli di disegno (Drawing) e permette di aggiungere quote, annotazioni e altri simboli tecnici con un grande controllo sul loro aspetto.
-   L\'ambiente [Fasteners](https://github.com/shaise/FreeCAD_FastenersWB) offre una vasta gamma di oggetti dispositivi di fissaggio pronti per l\'uso come viti, bulloni, barre, rondelle e dadi. Sono disponibili molte opzioni e impostazioni.
-   L\'ambiente [Assembly2](https://github.com/hamish2014/FreeCAD_assembly2) offre una serie di strumenti per montare e lavorare con gli [assemblaggi](https://en.wikipedia.org/wiki/Assembly_modelling).


</div>

**Approfondimenti**


<div class="mw-translate-fuzzy">

-   [La lista completa degli ambienti](Workbenches/it.md)
-   [Ambiente Parte](Part_Workbench/it.md)
-   [Ambiente Draft](Draft_Workbench/it.md)
-   [Ambienti Schizzo e Part Design](PartDesign_Workbench/it.md)
-   [Ambiente Arch](Arch_Workbench/it.md)
-   [Ambiente Drawing](Drawing_Workbench/it.md)
-   [Ambiente FEM](FEM_Workbench/it.md)
-   [Il repository FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons)


</div>


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > Manual:All workbenches at a glance/it
