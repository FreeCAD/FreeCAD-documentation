---
 GuiCommand:
   Name: Arch Component
‏‎‏‎   Name/it: Componente
   MenuLocation: Arch , Utilità , Componente
   Workbenches: Arch_Workbench/it
   Shortcut: **C** **M**
---

# Arch Component/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Crea un componente [Arch](Arch_Workbench/it.md) non parametrico basato su un oggetto [Part](Part_Workbench/it.md). Questo dà all\'oggetto \"basato su Part\" gli stessi attributi e proprietà degli altri oggetti Arch, e permette di specificare come deve essere esportato in IFC impostando la sua proprietà **Ifc Type**.


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un oggetto basato su [Part](Part_Workbench/it.md).
2.  Invocare Componente utilizzando uno di questi metodi:
    -   Premere il pulsante **<img src="images/Arch_Component.svg" width=16px>** nella barra degli strumenti.
    -   Usare la scorciatoia da tastiera **C** **M**.
    -   Usare la voce **Arch** → **Utilità** → **<img src="images/Arch_Component.svg" width=16px> [Componente](Arch_Component/it.md)** del menu principale.


</div>



## Proprietà


<div class="mw-translate-fuzzy">

L\'oggetto Componente di Arch è anche una base condivisa da tutti gli altri oggetti Arch (**<img src="images/Arch_Wall.svg" width=16px> [Muro](Arch_Wall/it.md)**, **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)**, ecc). Pertanto alcune delle sue proprietà e comportamenti sono comuni a tutti gli oggetti Arch (tranne gli strumenti che non producono oggetti solidi, come **<img src="images/Arch_SectionPlane.svg" width=16px> [Piano di sezione](Arch_SectionPlane/it.md)** or **<img src="images/Arch_Axis.svg" width=16px> [Assi](Arch_Axis/it.md)**):


</div>



### Dati


{{TitleProperty|Component}}

-    **Additions|LinkList**: I componenti Arch hanno una proprietà di addizione, che può contenere dei riferimenti a un numero qualsiasi di altre [Forme](Part_Workbench/it.md) basate su oggetti. La forma di queste addizioni viene unita alla forma base del componente, per produrre la forma finale. Vedere le [Note](#Note.md).

-    **Axis|Link**: un asse o un sistema di assi opzionale su cui questo oggetto deve essere duplicato.


<div class="mw-translate-fuzzy">

-   **Base shape**: I Componenti di Arch sono sempre basati su una [Forma](Part_Workbench/it.md) o basati su un oggetto base. Alcuni tipi di oggetti Arch usano semplicemente la forma base così come è, altri (per esempio (**<img src="images/Arch_Wall.svg" width=16px> [Muro](Arch_Wall/it.md)**) eseguono alcune operazioni aggiuntive, ad esempio un\'estrusione. Per alcuni tipi, avere un oggetto base non è obbligatorio, es. (**<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)**)


</div>


<div class="mw-translate-fuzzy">

-   **Clone Of**: Qualsiasi componente Arch può essere un clone di un altro componente Arch dello stesso tipo (un muro può essere solo un clone di un altro muro, ecc.). L\'unica eccezione è il componente Arch generico (come quello prodotto da questo comando), che può essere clone di qualsiasi altro tipo (muro, struttura, finestra, ecc.). Ciò consente di utilizzare un componente Arch generico per sovrascrivere il tipo di un altro.


</div>


<div class="mw-translate-fuzzy">

-   **Hi Res**: un componente Arch può utilizzare la forma di un altro oggetto come versione a risoluzione maggiore della sua. Per questo, è necessario impostare sia la proprietà Alta risoluzione sia la modalità di visualizzazione Alta risoluzione. Ciò consente, ad esempio, di creare un muro semplice e quindi di modellare ogni mattone che compone il muro, ad esempio con **<img src="images/Part_Box.svg" width=16px> [Box](Part_Box/it.md)**. Quindi, usa un composto di quei mattoni come versione ad alta risoluzione del muro. La forma del muro non viene modificata aggiungendo un oggetto Hi-Res. Cambia solo la sua rappresentazione nella [vista 3D](3D_view/it.md), e adotta la rappresentazione nella versione ad alta risoluzione anziché la sua.


</div>

-    **Horizontal Area|Area**: l\'area della proiezione di questo oggetto sul piano XY (sola lettura).


<div class="mw-translate-fuzzy">

-   **Material**: Tutti i componenti Arch hanno una proprietà materiale, che può contenere un [Materiale](Arch_SetMaterial/it.md) o un [Multi-materiale](Arch_MultiMaterial/it.md) (non tutti i tipi di oggetto Arch supportano l\'uso dei Muti-materiali). Le proprietà DiffuseColor e Transparency del materiale allegato definiscono il colore della forma e la trasparenza del componente Arch. Il materiale viene importato ed esportato in [IFC](Arch_IFC/it.md), [OBJ](Arch_OBJ/it.md) e [DAE](Arch_DAE/it.md).


</div>

-    **Move Base|Bool**: specifica se lo spostamento di questo oggetto sposta invece la sua base.


<div class="mw-translate-fuzzy">

-   **Move with Host**: Quando un componente è incorporato in un altro (ad esempio una finestra all\'interno di un muro), impostando questa proprietà su True l\'oggetto si muove o ruota insieme al suo oggetto ospite quando l\'oggetto ospite viene spostato o ruotato usando i comandi **<img src="images/Draft_Move.svg" width=16px> [Sposta](Draft_Move/it.md)** o **<img src="images/Draft_Rotate.svg" width=16px> [Ruota](Draft_Rotate/it.md)** di Draft.


</div>

-    **Perimeter Length|Length**: La lunghezza del perimetro dell\'area orizzontale (sola lettura).

-    **Standard Code|String**: un codice standard opzionale (OmniClass, ecc\...) per questo componente.


<div class="mw-translate-fuzzy">

-   **Subtractions**: I componenti Arch hanno una proprietà sottrazione, che può contenere dei riferimenti a un numero qualsiasi di altre [Forme](Part_Workbench/it.md) basate su oggetti. La forma di questi oggetti viene sottratta alla forma base del componente, per produrre la forma finale.


</div>

-    **Vertical Area|Area**: l\'area di tutte le facce verticali di questo oggetto (sola lettura).


{{TitleProperty|IFC}}

-    **Ifc Data|Map|Hidden**:

-    **Ifc Properties|Map|Hidden**:


<div class="mw-translate-fuzzy">

-   **Role**: Ogni componente Arch, oltre alla funzione definita dal tipo (muro, finestra, ecc.), Ha anche una proprietà Ruolo, che può definire ulteriormente quale tipo di funzione svolge. Ad esempio, una **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)** può avere un ruolo di trave o di colonna. I componenti generici di Arch (come sonp prodotti da questo comando) possono avere qualsiasi ruolo disponibile nell\'intero ambiente Arch. Il ruolo è ciò che viene utilizzato per definire il tipo di oggetto IFC da esportare quando viene [esportato in IFC](Arch_IFC/it.md).


</div>


{{TitleProperty|IFC Attributes}}

-    **Description|String**: Tutti i componenti Arch hanno un campo Descrizione, che può contenere qualsiasi testo. Questo è utilizzato quando si [esporta in IFC](Arch_IFC/it.md).

-    **Global Id|String**:

-    **Object Type|String**:

-    **Predefined Type|Enumeration**:

-    **Tag|Enumeration**: La proprietà Tag è un altro campo di testo, che può essere utilizzato per fornire un\'ulteriore identità personalizzata agli oggetti.



## Note

-   Il posizionamento del componente Arch viene applicato dopo che le addizioni e le sottrazioni sono state eseguite, quindi queste vengono eseguite rispetto all\'oggetto di base nella sua posizione di base. Poi il risultato viene spostato nella posizione definita dal Posizionamento.


<div class="mw-translate-fuzzy">

-   Gli oggetti possono essere aggiunti o rimossi negli elenchi delle Addizioni e Sottrazioni di un componente selezionando sia l\'oggetto che il componente e utilizzando i comandi **<img src="images/Arch_Add.svg" width=16px> [Aggiungi componente](Arch_Add/it.md)** o **<img src="images/Arch_Remove.svg" width=16px> [Rimuovi componente](Arch_Remove/it.md)**, o dal pannello delle azioni facendo doppio clic sul componente nella [Vista ad albero](Tree_view/it.md). Il pannello delle azioni consente inoltre di verificare quale oggetto fa parte di questi elenchi.


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Component/it
