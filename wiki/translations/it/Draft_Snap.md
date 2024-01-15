# Draft Snap/it
## Descrizione

In <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/it.md) e <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch](Arch_Workbench/it.md) è possibile creare la geometria selezionando i punti nella [Vista 3D](3D_view/it.md) o inserendo le coordinate nel [pannello delle attività](Task_panel/it.md) dei comandi. Un altro modo per selezionare i punti è mediante l\'aggancio (snap). L\'aggancio consente di selezionare punti geometrici precisi o definiti da oggetti esistenti o dalla griglia. Si può ad esempio eseguire l\'aggancio al punto finale di una linea, al centro di un cerchio o all\'intersezione di due bordi.

L\'aggancio è disponibile con la maggior parte dei comandi [Draft](Draft_Workbench/it.md) e [Arch](Arch_Workbench/it.md).

![](images/Draft_Snap_Endpoint_example.png ) 
*Aggancio al punto finale di un bordo*



## Strumenti per l\'aggancio 

Questi strumenti sono disponibili nella barra degli strumenti Snap Draft e nel [Widget Snap Draft](Draft_snap_widget/it.md).

Tenere presente che i bordi circolari non devono essere cerchi completi.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Blocca aggancio](Draft_Snap_Lock/it.md): abilita o disabilita l\'aggancio a livello globale.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Aggancia Punto Finale](Draft_Snap_Endpoint/it.md): aggancia ai punti finali dei bordi.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Aggancia Punto Medio](Draft_Snap_Midpoint/it.md): aggancia al punto medio dei bordi.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Aggancia Centro](Draft_Snap_Center/it.md): aggancia al punto centrale delle facce e dei bordi circolari e al punto **Placement** di [Piani di lavoro proxy di Draft](Draft_WorkingPlaneProxy/it.md) e [Parti di edificio Arch](Arch_BuildingPart/it.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Aggancia Angolo](Draft_Snap_Angle/it.md): aggancia a punti cardinali speciali sui bordi circolari, a multipli di 30° e 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Aggancia Intersezione](Draft_Snap_Intersection/it.md): aggancia all\'intersezione di due bordi.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Aggancia Perpendicolare](Draft_Snap_Perpendicular/it.md): aggancia ai punti perpendicolari sulle facce ({{Version/it|0.21}}) e sui bordi.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Aggancia Estensione](Draft_Snap_Extension/it.md): aggancia a una linea immaginaria che si estende oltre i punti finali dei bordi diritti.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Aggancia Parallelo](Draft_Snap_Parallel/it.md): aggancia a una linea immaginaria parallela ai bordi diritti.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Aggancia Speciale](Draft_Snap_Special/it.md): aggancia a punti speciali definiti dall\'oggetto.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Aggancia Vicino](Draft_Snap_Near/it.md): aggancia al punto più vicino su facce e bordi.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Aggancia Ortogonale](Draft_Snap_Ortho/it.md): aggancia alle linee immaginarie che attraversano il punto precedente a multipli di 45°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Aggancia Griglia](Draft_Snap_Grid/it.md): aggancia alle intersezioni delle linee della griglia.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Aggancia Piano di lavoro](Draft_Snap_WorkingPlane/it.md): proietta i punti di aggancio sul [piano di lavoro](Draft_SelectPlane/it.md) corrente.

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Aggancia Quote](Draft_Snap_Dimensions/it.md): mostra le quote X e Y temporanee.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Attiva/disattiva griglia](Draft_ToggleGrid/it.md): cambia la visibilità della griglia.



## Aggancio avanzato 

-   È possibile ottenere ulteriori punti di aggancio combinando due opzioni di aggancio (snap). Ad esempio, combinando [Draft Aggancia Ortogonale](Draft_Snap_Ortho/it.md) e [Draft Aggancia Estensione](Draft_Snap_Extension/it.md) si ottiene un punto di aggancio all\'intersezione delle loro linee immaginarie.
-   L\'aggancio può essere combinato con [vincoli](Draft_Constrain/it.md).
-   Premere **Q** per inserire un \"punto di attesa\" nella posizione corrente del cursore. È possibile eseguire l\'aggancio agli assi ortogonali dei punti di aggancio e alle intersezioni di questi assi. Se l\'opzione [Draft Aggancia Punto medio](Draft_Snap_Midpoint/it.md) è attiva, si può anche eseguire l\'aggancio al punto medio tra due punti di attesa.
-   Premere **** una o più volte per agganciare un oggetto oscurato da un\'altra geometria. Questo si chiama \"aggancio ciclico\". Tenere presente che si deve spostare leggermente il cursore nella [Vista 3D](3D_view/it.md) dopo aver premuto il tasto.

![](images/Draft_Snap_example_cycling_1.png ) 
*Ciclo di aggancio 1: il rettangolo rosso è stato creato per primo quindi ha priorità di aggancio. Senza il ciclo di aggancio non è possibile eseguire l'aggancio al rettangolo verde dove è sovrapposto al rettangolo rosso.*

![](images/Draft_Snap_example_cycling_2.png ) 
*Ciclo di aggancio 2: dopo aver utilizzato una volta il tasto del ciclo di aggancio il rettangolo verde riceve la priorità di aggancio. Ora è possibile eseguire l'aggancio al punto medio del bordo verde sovrapposto.*



## Note

-   È possibile attivare più opzioni di aggancio (snap) contemporaneamente, ma è consigliabile attivare solo le opzioni di aggancio realmente necessarie. Attivarne troppe può rallentare le cose.
-   Non è una buona idea avere [Draft Aggancio Vicino](Draft_Snap_Near/it.md) permanentemente attivo poiché ha la precedenza su molte altre opzioni di aggancio.



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Quando un comando [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) che richiede l\'immissione di punti è attivo, la distanza massima alla quale [Draft Aggancia Griglia](Draft_Snap_Grid/it.md) rileva le intersezioni delle linee della griglia può essere modificata al volo premendo **P** (tasto aumenta) o **M** (tasto diminuisci). Questa impostazione viene memorizzata: **Strumenti → Modifica parametri... → BaseApp → Preferenze → Mod → Draft → snapRange**. Può anche essere modificato nel pannello delle attività del comando [Draft Seleziona Piano](Draft_SelectPlane/it.md).
-   Per eseguire l\'aggancio solo quando si tiene premuto il tasto **Modificatore aggancio**:
    -   Deseleziona: **Modifica → Preferenze... → Draft → Griglia e aggancio  → Aggancia sempre**.
    -   Il tasto predefinito **Modificatore aggancio**, **Ctrl**, può essere modificato: **Modifica → Preferenze... → Draft → Griglia e aggancio → Modificatore aggancio**.
-   Per mostrare la barra degli strumenti di aggancio Draft solo quando un comando è attivo, selezionare: **Modifica → Preferenze... → Draft → Interfaccia → Mostra solo la barra degli strumenti di aggancio Draft durante i comandi**. {{Version/it|0.22}}
-   I simboli di aggancio possono essere modificati: **Modifica → Preferenze... → Draft → Griglia e aggancio → Stile simbolo di aggancio**.
-   Il colore dei simboli di aggancio e le dimensioni di [Draft Aggancia Quote](Draft_Snap_Dimensions/it.md) possono essere modificati: **Modifica → Preferenze... → Draft → Griglia e aggancio → Colore simbolo di aggancio**.
-   La dimensione dei simboli di snap dipende da: **Modifica → Preferenze... → Visualizzazione → Vista 3D → Dimensione marcatore**. {{Version/it|0.22}}
-   Le scorciatoie da tastiera a carattere singolo menzionate possono essere modificate: **Modifica → Preferenze... → Draft → Interfaccia → Scorciatoie comando**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap/it
