---
- GuiCommand:/it
   Name:PartDesign Fillet
   Name/it:Raccordo
   Workbenches:[PartDesign](PartDesign_Workbench/it.md)
   MenuLocation:PartDesign → Raccordo
   SeeAlso:[PartDesign Smusso](PartDesign_Chamfer.md), [Part Raccordo](Part_Fillet.md)
---


</div>

## Descrizione

Questo strumento crea dei raccordi (arrotondamenti) sui bordi selezionati di un oggetto. Nella struttura del progetto viene creata una nuova voce **Fillet** (Raccordo), seguita da un numero sequenziale se nel documento esistono già altri raccordi.

## Utilizzo

-   Selezionare uno o più bordi di un oggetto, quindi avviare lo strumento facendo clic sulla sua icona o tramite il menu.
-   Nei **Parametri Raccordo** della finestra delle opzioni, impostare il raggio di raccordo inserendo il valore, o facendo clic sulle frecce su / giù. Il raccordo applicato viene mostrato in tempo reale.
-   Se si desidera aggiungere più bordi o facce, fare clic prima sul pulsante **Aggiungi** e quindi selezionare il bordo o la faccia.
-   Se si desidera rimuovere bordi o facce
    -   selezionare il bordo o la faccia nell\'elenco della finestra di dialogo e premere il tasto **Canc**. *Nota*: poiché deve esserci almeno un bordo per la funzione, l\'ultimo bordo o faccia rimanente nell\'elenco non può essere rimosso.
    -   oppure fare clic sul pulsante **Rimuovi**. Tutti i bordi e le facce precedentemente selezionati vengono evidenziati in viola. Selezionare il bordo o la faccia da rimuovere.
-   Premere **OK** per convalidare.
-   Per una catena di spigoli tangenti l\'uno all\'altro, può essere selezionato un bordo singolo, il raccordo si propaga lungo la catena.
-   Per modificare il raccordo dopo che la funzione è stata convalidata, fare doppio clic sull\'etichetta del Raccordo nella struttura del progetto, oppure fare clic destro su di esso e selezionare **Modifica Raccordo**.

## Raccordo di PartDesign e Raccordo di Part 

Il <img alt="" src=images/PartDesign_Fillet.svg  style="width:24px;"> [Raccordo di PartDesign](PartDesign_Fillet/it.md) non deve essere confuso con il **<img alt="" src=images/Part_Fillet.svg  style="width:24px;"> [Raccordo di Part](Part_Fillet/it.md)**. Sebbene condividano lo stesso nome, non sono uguali e non vengono utilizzati allo stesso modo.

Ecco come differiscono l\'uno dall\'altro:

-   Il raccordo di PartDesign è *Parametrico*. Dopo aver applicato un raccordo, è possibile modificarne il raggio; ciò non è possibile con il raccordo di Parte.
-   Il raccordo di PartDesign crea una voce Raccordo separata (seguita da un numero sequenziale se sono già presenti raccordi) nella struttura del progetto. Il raccordo di Parte diventa il genitore dell\'oggetto a cui è stato applicato.
-   Il raccordo di PartDesign offre un\'anteprima in tempo reale del raccordo applicato all\'oggetto prima di convalidare la funzione.
-   Il raccordo di Parte supporta i raggi variabili (con un raggio iniziale e un raggio finale). Il raccordo di PartDesign no.

## Problemi noti 

Raccordi, smussi e altre funzionalità che operano su corpi solidi dipendono dal kernel OpenCASCADE Technology (OCCT) sottostante utilizzato da FreeCAD. Occasionalmente il kernel OCCT ha difficoltà nel gestire gli spigoli coincidenti, dove si incontrano due facce. In questo caso, FreeCAD potrebbe bloccarsi senza una spiegazione.

Se eseguito dal terminale, FreeCAD può generare un registro come questo dopo l\'arresto anomalo:


{{code|code=
#1  0x7fff63d660ba in BRep_Tool::Curve(TopoDS_Edge const&, TopLoc_Location&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x2a
#2  0x7fff63d69546 in BRep_Tool::Curve(TopoDS_Edge const&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x46
#3  0x7fff71f4fef5 in ChFi3d_Builder::PerformIntersectionAtEnd(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x3b05
#4  0x7fff71f58307 in ChFi3d_Builder::PerformOneCorner(int, bool) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x1097
#5  0x7fff71ef6218 in ChFi3d_Builder::PerformFilletOnVertex(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x4e8
#6  0x7fff71ef71d1 in ChFi3d_Builder::Compute() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0xe31
#7  0x7fff720ad7c3 in BRepFilletAPI_MakeChamfer::Build() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x33
#8  0x7fff723be48e in PartDesign::Chamfer::execute() from /usr/lib/freecad-daily/lib/_PartDesign.so+0x60e
...
}}

Questo output fa riferimento a funzioni situate in `libTKBRep.so`, `libTKFillet.so`, ecc., che sono librerie OCCT. Se si verifica questo tipo di arresto anomalo, potrebbe essere necessario segnalare e risolvere il problema in OCCT anziché in FreeCAD.

Per maggiori informazioni vedere le discussioni del forum :

-   [Bug Chamfer bigger than 2mm crashes freecad](https://forum.freecadweb.org/viewtopic.php?p=263818#p263818)
-   [Segfault when using part desigin fillet](https://forum.freecadweb.org/viewtopic.php?p=264827#p264827)

L\'utente è anche responsabile dell\'integrità del proprio modello. A seconda del modello, potrebbe essere impossibile eseguire un raccordo o uno smusso se il corpo non è abbastanza grande da supportare tale operazione. Ad esempio, non è possibile creare un raccordo da 10 mm se un bordo è separato di soli 5 mm dalla superficie successiva. In questo caso, il raggio massimo per un raccordo è 5 mm; tentare di usare un valore più grande può dare come risultato una forma che non può essere calcolata o anche un crash. Se l\'utilizzo del limite esatto di 5 mm non funziona, potrebbe essere possibile utilizzare un\'approssimazione molto ravvicinata, come 4.9999 mm, per ottenere lo stesso risultato visibile.

### Topological naming 


<div class="mw-translate-fuzzy">

### Denominazione topologica 

I numeri che rappresentano i nomi dei bordi non sono completamente stabili, pertanto è consigliabile terminare il lavoro di modellazione principale del corpo solido prima di applicare funzioni come raccordi e smussi, altrimenti i bordi potrebbero cambiare nome e i bordi raccordati diventerebbero probabilmente non validi.


</div>

Ulteriori informazioni nella pagina dedicata al [problema di denominazione topologica](topological_naming_problem/it.md).

## Script


<div class="mw-translate-fuzzy">

Lo strumento Fillet può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
Box = Box.makeFillet(3,[Box.Edges[0]]) # 1 Fillet
Box = Box.makeFillet(3,[Box.Edges[1],Box.Edges[2],Box.Edges[3],Box.Edges[4]]) # for several Fillets
```

-   3 = valore del raggio
-   Box.Edges\[2\] = lo spigolo con il suo numero identificativo


<div class="mw-translate-fuzzy">

Esempio:


</div>


```python
import PartDesign
from FreeCAD import Base

Box = Part.makeBox(10,10,10)
Box = Box.makeFillet(3,[Box.Edges[0]]) # pour 1 Fillet
Box = Box.makeFillet(3,[Box.Edges[1],Box.Edges[2],Box.Edges[3],Box.Edges[4]]) # for several Fillets
Part.show(Box)
```


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}} 
