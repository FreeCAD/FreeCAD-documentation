# Topological naming problem/it
## Introduzione


{{TOCright}}

Il [problema di denominazione topologica](topological_naming_problem/it.md) in FreeCAD si riferisce al problema di una forma che cambia il suo nome interno dopo l\'esecuzione di un\'operazione di modellazione (pad, taglio, unione, smusso, raccordo, ecc.). Questo si riflette sulle altre funzioni parametriche che dipendono da quella forma e ha come conseguenze che le interrompe o le calcola in modo errato. Questo problema interessa tutti gli oggetti di FreeCAD, ma è particolarmente importante quando si costruiscono solidi con <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/it.md) e quando si dimensionano questi solidi con <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/it.md).

-   In <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/it.md), se una funzione è supportata su una faccia (o bordo o vertice), la funzione può interrompersi se il solido sottostante cambia dimensione o orientamento, in quanto la faccia originale (o il bordo o vertice) può essere rinominata internamente.
-   In <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/it.md), se una dimensione misura la lunghezza di un bordo proiettato, la dimensione potrebbe interrompersi se il modello 3D viene modificato, poiché modificando il bordo misurato i vertici possono essere rinominati.

Il problema di denominazione topologica è un problema complesso nella modellazione CAD che deriva dal modo in cui le routine interne di FreeCAD gestiscono gli aggiornamenti delle forme geometriche create con il [kernel OCCT](OpenCASCADE/it.md). A partire da FreeCAD 0.18 ci sono sforzi in corso per migliorare la gestione di base delle forme al fine di ridurre o eliminare tali problemi.

Il problema di denominazione topologica influisce molto spesso e confonde i nuovi utenti di FreeCAD. In PartDesign, l\'utente è invitato a seguire le migliori pratiche discusse nella pagina [Editazione delle funzioni](feature_editing/it.md). Si consiglia vivamente l\'uso di oggetti di riferimento come i [piani](PartDesign_Plane/it.md) ed i [sistemi di coordinate locali](PartDesign_CoordinateSystem/it.md) per produrre modelli che non sono facilmente soggetti a tali errori topologici. In TechDraw, si consiglia all\'utente di aggiungere le quote solo quando il modello 3D è completo e non sarà ulteriormente modificato.

## Esempio

1\. In <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/it.md), creare un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Corpo](PartDesign_Body/it.md), poi usare <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Nuovo schizzo](PartDesign_NewSketch/it.md) e selezionare il piano XY per disegnare lo schizzo di base; quindi eseguire un <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [Pad](PartDesign_Pad/it.md) per creare un primo solido.

<img alt="" src=images/FreeCAD_topological_problem_01_solid.png  style="width:" height="400px;">

2\. Selezionare la faccia superiore del solido precedente, quindi usare <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Nuovo schizzo](PartDesign_NewSketch/it.md) per disegnare un altro schizzo; quindi eseguire un secondo pad.

   
  <img alt="" src=images/FreeCAD_topological_problem_02_solid_sketch_2.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_03_solid_2.png  style="width:" height="400px;">
   

3\. Selezionare la faccia superiore dell\'estrusione precedente e creare nuovamente uno schizzo e un pad.

<img alt="" src=images/FreeCAD_topological_problem_04_solid_3.png  style="width:" height="400px;">

4\. Ora, fare doppio clic sul secondo schizzo e modificarlo in modo che la sua lunghezza sia lungo la direzione X; facendo questo si rigenera il secondo pad. Il terzo schizzo e il pad rimangono nello stesso posto.

   
  <img alt="" src=images/FreeCAD_topological_problem_05_solid_sketch_2.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_06_solid_2.png  style="width:" height="400px;">
   

<img alt="" src=images/FreeCAD_topological_problem_07_solid_3.png  style="width:" height="400px;">

5\. A questo punto, fare nuovamente doppio clic sul secondo schizzo e regolarne i punti in modo che una parte di esso sia fuori dai limiti definiti dal primo pad. In questo modo, il secondo pad viene ricalcolato correttamente, tuttavia, guardando nella [vista ad albero](Tree_view/it.md), nel terzo pad viene indicato un errore.

   
  <img alt="" src=images/FreeCAD_topological_problem_08_solid_sketch_2.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_09_solid_2.png  style="width:" height="400px;">
   

![](images/FreeCAD_topological_problem_12_broken_tree.png )

6\. Rendendo visibile il terzo schizzo e pad, è chiaro che il calcolo del nuovo solido non è stato eseguito correttamente. Il terzo schizzo, invece di essere supportato dalla faccia superiore del secondo pad, appare in un posto strano, con la sua normale orientata verso la direzione X. Ciò si traduce in un pad non valido, in quanto questo pad sarebbe scollegato dal resto del <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Corpo](PartDesign_Body/it.md), che non è consentito.

Il problema sembra essere che quando il secondo schizzo è stato modificato, la faccia superiore del secondo pad è stata rinominata da `Face13` a `Face14`. Il terzo schizzo è collegato a `Face13` come era in origine, ma poiché questa faccia è ora sul lato (e non più in alto), lo schizzo segue il suo orientamento e ora è posizionato in modo errato.

   
  <img alt="" src=images/FreeCAD_topological_problem_10_solid_2_sketch_3.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_11_solid_2_faces.png  style="width:" height="400px;">
   

7\. Per risolvere il problema, il terzo schizzo deve essere nuovamente associato alla faccia superiore. Selezionare lo schizzo, fare clic sui puntini di sospensione (tre punti) accanto alla proprietà **Map Mode** e scegliere di nuovo la faccia superiore del secondo pad. Quindi lo schizzo si sposta in cima al solido esistente e il terzo pad viene generato senza problemi.

![](images/FreeCAD_topological_problem_13_remap_sketch_2.png )

   
  <img alt="" src=images/FreeCAD_topological_problem_14_solid_2_sketch_3.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_15_solid_3.png  style="width:" height="400px;">
   

La rimappatura di uno schizzo in questo modo può essere eseguita ogni volta che si verifica un errore di denominazione topologica, ma questo può essere noioso se il modello è complicato e vi sono molti schizzi che devono essere modificati.

## Soluzione

![](images/FreeCAD_topological_problem_16_dependency_graph.png )

Il [Grafico delle dipendenze](Std_DependencyGraph/it.md) è uno strumento utile per osservare le relazioni tra i diversi corpi nel documento. L\'utilizzo del flusso di lavoro di modellazione originale rivela la relazione diretta esistente tra gli schizzi e i pad. Come una catena, è facile vedere che questa dipendenza diretta è soggetta a problemi di denominazione topologica se uno qualsiasi dei collegamenti nella sequenza cambia.

Come spiegato nella pagina [Editazione delle funzioni](feature_editing/it.md), una soluzione a questo problema consiste nel supportare gli schizzi non sulle facce ma sui piani di riferimento che sono sfalsati rispetto ai piani principali di Origine del [Corpo](PartDesign_Body/it.md) di PartDesign

1\. Selezionare l\'origine del [Corpo](PartDesign_Body/it.md) di PartDesign e accertarsi che sia visibile. Quindi selezionare il piano XY e fare clic su [Piano di riferimento](PartDesign_Plane/it.md). Nella finestra di dialogo Offset di associazione, assegnargli un offset nella direzione Z in modo che il piano di riferimento sia complanare con la faccia superiore del primo pad.

2\. Ripetere il processo ma questa volta aggiungere uno scostamento maggiore in modo che il secondo piano di riferimento sia complanare con la faccia superiore del secondo pad.




   
  <img alt="" src=images/FreeCAD_topological_problem_17_datum_plane_1.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_18_datum_plane_2.png  style="width:" height="400px;">
   

3\. Selezionare il secondo schizzo, fare clic sui puntini di sospensione accanto alla proprietà **Map Mode**, quindi selezionare il primo piano di riferimento. Il piano di riferimento è già sfalsato rispetto al piano XY del corpo, quindi per lo schizzo non è richiesto un ulteriore spostamento Z.

4\. Ripetere il processo con il terzo schizzo e selezionare il secondo piano di riferimento come supporto. Di nuovo, non è necessario alcun ulteriore spostamento in Z.

5\. Il grafico delle dipendenze ora mostra che gli schizzi ed i pad sono supportati dai piani di riferimento. Questo modello è più stabile in quanto tutti gli schizzi possono essere modificati essenzialmente indipendentemente l\'uno dall\'altro.

![](images/FreeCAD_topological_problem_19_dependency_graph_datum_planes.png )

6\. Fare doppio clic sul secondo schizzo e modificare la forma. Il secondo pad dovrebbe aggiornarsi immediatamente senza causare problemi topologici con il terzo schizzo e il terzo pad.

<img alt="" src=images/FreeCAD_topological_problem_20_independent_solid_2.png  style="width:" height="400px;">

7\. In effetti, ogni schizzo può essere modificato senza interferire con i pad degli altri. Fino a quando i pad hanno una lunghezza di estrusione sufficiente, in modo che si tocchino e formino un solido contiguo, l\'intero corpo rimane valido.

<img alt="" src=images/FreeCAD_topological_problem_21_independent_solids_all.png  style="width:" height="400px;">

## Note finali 

L\'aggiunta di oggetti di riferimento implica più lavoro per l\'utente, ma alla fine produce modelli più stabili che sono meno soggetti al problema di denominazione topologica.

Naturalmente, gli oggetti di riferimento possono essere creati prima che vengano disegnati gli schizzi e vengano prodotti i pad. Questo può essere utile per visualizzare la forma e le dimensioni approssimative del corpo finale.

I piani di riferimento possono anche essere basati su altri piani di riferimento. Ciò crea una catena di dipendenze che potrebbe anche portare a problemi topologici; tuttavia, poiché i piani di riferimento sono oggetti molto semplici, il rischio di avere questi problemi è inferiore rispetto a quando viene utilizzata la faccia di un oggetto solido come supporto.

Gli oggetti di riferimento, [punti](PartDesign_Point/it.md), [linee](PartDesign_Line/it.md), [piani](PartDesign_Plane/it.md), ed i [sistemi di coordinate](PartDesign_CoordinateSystem/it.md), possono anche essere utili come geometrie di riferimento, ovvero come ausili visivi per mostrare le funzioni principali del modello, anche se nessuno schizzo è direttamente collegato ad essi.

## Link


<div class="mw-translate-fuzzy">

-   [PartDesign Raccordo - Denominazione topologica](PartDesign_Fillet#Topological_naming/it.md)
-   [Denominazione topologica, il mio punto di vista](https://forum.freecadweb.org/viewtopic.php?t=27278): una possibile soluzione, di realthunder.
-   \[\[Topological\_Naming\_Project/it\|Progetto di denominazione topologica

\]\]: idea per risolvere il problema, di ickby.

-   [Script di dati topologici](Topological_data_scripting/it.md)
-   \[\[Feature\_editing/it\|Editazione delle funzioni

\]\]: consigli alternativi per tecniche di modellazione stabili.


</div>

## Video

-   [Perché i miei modelli FreeCAD si rompono? - \"Problema di denominazione topologica\"](https://youtu.be/6p2vqEEmWq4): Una spiegazione video dei problemi sottostanti al [Problema di denominazione topologica](Topological_naming_problem/it.md)
-   [FreeCAD è sostanzialmente danneggiato! - E adesso\... Aiutami a decidere\...](https://www.youtube.com/watch?v=QSsVFu929jo): Un video di Maker Tales


 {{TechDraw Tools navi}} {{PartDesign Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [TechDraw](Category_TechDraw.md) > [PartDesign](Category_PartDesign.md) > [Part](Category_Part.md) > Topological naming problem/it
