---
 GuiCommand:
   Name: Arch Rebar Footing Reinforcement
   Name/it: Armatura di Fondamenta
   MenuLocation: Arch , Strumenti di armatura , Armatura fondamenta<br>3D/BIM , Reinforcement tools , Armatura fondamenta
   Workbenches: Arch_Workbench/it
   SeeAlso: Reinforcement_Workbench/it, Arch_Rebar/it
---

# Reinforcement FootingRebars/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento [Armatura fondamenta](Arch_Rebar_Footing_Reinforcement/it.md) consente all\'utente di creare barre d\'armatura all\'interno di un oggetto [Struttura](Arch_Structure/it.md) di Fondamenta.


</div>


<div class="mw-translate-fuzzy">

Questo comando fa parte dell\'ambiente [Reinforcement](Reinforcement_Workbench/it.md), un [ambiente esterno](External_workbenches/it.md) che si può installare con <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md), tramite il menu **Strumenti → Addon manager → Reinforcement**.


</div>

<img alt="" src=images/Isometric_view_of_Columns_footing.png  style="width:600px;"> 
*Un esempio di armatura di fondamenta per una [Struttura](Arch_Structure/it.md)*

<img alt="" src=images/Front_View_of_Column_footing.png  style="width:600px;"> 
*Vista frontale di un esempio di Armatura di fondamenta*



## Utilizzo

1\. Selezionare la faccia verticale di un oggetto Fondamenta di una **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)** creata in precedenza come mostrato nell\'immagine seguente.

:   <img alt="" src=images/Footing_Face_selected.png  style="width:600px;">


<div class="mw-translate-fuzzy">



*Faccia selezionata per una Struttura Fondamenta di Arch*


</div>


<div class="mw-translate-fuzzy">

2\. Quindi selezionare **[Armatura di fondamenta](Arch_Rebar_Footing_Reinforcement/it.md)** dagli strumenti dell\'armatura.


</div>

3\. Sullo schermo verrà visualizzata una finestra di dialogo relativa all\'armatura di fondamenta, come mostrato di seguito.

:   <img alt="" src=images/Footing_Reinforcement_GUI_.png  style="width:600px;">


<div class="mw-translate-fuzzy">



*Finestra di dialogo per l'armatura di fondamenta*


</div>


<div class="mw-translate-fuzzy">

4\. Selezionare il tipo di armatura desiderato e altri dati di input per l\'armatura in direzione parallela della faccia selezionata nella maglia di rinforzo della fondazione, come mostrato nell\'immagine sottostante.


</div>


:   <img alt="" src=images/Input_Fields_for_Parallel_rebars_in_footing_GUI_Dialog_box.png  style="width:600px;">


<div class="mw-translate-fuzzy">



*Finestra di dialogo per le armature di fondamenta in direzione parallela alla faccia selezionata*


</div>


<div class="mw-translate-fuzzy">

5\. Ora fare clic sul pulsante Avanti o selezionare Armature trasversali nella visualizzazione elenco e inserire i dati desiderati per i dati di input per le armature nella direzione trasversale della faccia selezionata nella maglia di rinforzo della base come mostrato nell\'immagine sottostante.


</div>


:   <img alt="" src=images/GUICrossRebarInputsFooting.png  style="width:600px;">


<div class="mw-translate-fuzzy">



*Finestra di dialogo per l'armatura di fondamenta nella direzione trasversale della faccia selezionata*


</div>


<div class="mw-translate-fuzzy">

6\. Fare clic su Avanti o fare clic su Colonne nella visualizzazione elenco e inserire l\'input desiderato per le colonne nell\'armatura di fondazione. Qui si può scegliere se aggiungere o meno le armature secondarie nelle colonne.


</div>


:   <img alt="" src=images/Columns_input_fields_for_column_footing.png  style="width:600px;">


<div class="mw-translate-fuzzy">



*Finestra di dialogo per i campi di input dei pilastri nell'armatura della fondazione*


</div>


<div class="mw-translate-fuzzy">

7\. Fare clic su next o fare clic su Ties nella visualizzazione elenco e inserire l\'input desiderato per i tiranti nelle colonne dell\'armatura di fondazione.


</div>


:   <img alt="" src=images/Ties_input_fields_for_column_footing.png  style="width:600px;">


<div class="mw-translate-fuzzy">



*Finestra di dialogo per i campi di input dei Tiranti nelle colonne dell'Armatura della fondazione*


</div>


<div class="mw-translate-fuzzy">

8\. Fare clic su next o fare clic su Main rebars nella visualizzazione elenco e inserire l\'input desiderato per le armature principali nelle colonne dell\'armatura di fondazione.


</div>


:   <img alt="" src=images/Main_Rebar_input_fields_for_column_footing.png  style="width:600px;">


<div class="mw-translate-fuzzy">



*Finestra di dialogo per i campi di input delle armature principali nelle colonne dell'armatura di fondazione *


</div>

Nota: i passaggi 9 e 10 sono obbligatori, solo se il controllo delle armature secondarie è abilitato nel passaggio 6.


<div class="mw-translate-fuzzy">

9\. Fare clic su next o su XDir Armatura secondaria nella visualizzazione elenco e inserire l\'input desiderato per le armature secondarie nella direzione X in una colonna nell\'armatura di fondazione.


</div>


:   <img alt="" src=images/X_Direction_secondary_rebar_sinput_fields_for_column_footing_Reinforcement.png  style="width:600px;">


<div class="mw-translate-fuzzy">



*Finestra di dialogo per i campi di input delle armature in direzione X nelle colonne dell'armatura di fondazione*


</div>


<div class="mw-translate-fuzzy">

10\. Fare clic su next o fare clic su YDir Armatura secondaria nella visualizzazione elenco e inserire l\'input desiderato per le armature secondarie nella direzione Y in una colonna nell\'armatura di fondazione.


</div>


:   <img alt="" src=images/Y_Direction_secondary_rebars_input_fields_for_Column_footing_reinforcement.png  style="width:600px;">


<div class="mw-translate-fuzzy">



*Finestra di dialogo per i campi di input delle armature in direzione Y nelle colonne dell'Armatura della fondazione*


</div>

11\. Click **OK** or **Apply** or **Finish** to generate Footing reinforcement.

12\. Click **Cancel** to exit the dialog box.



## Proprietà

**Proprietà per le armature in direzione parallela alla faccia selezionata nell\'armatura di fondamenta:**

-   {{ PropertyData\|Mesh Cover Along}}: Rappresenta l\'allineamento della rete di armatura lungo la faccia superiore e/o inferiore della struttura. Può avere tre valori \"Top\", \"Bottom\" e \"Both\".
-   {{ PropertyData\|Rebar Type}}: Tipo di armatura per le armature parallele di fondazione. Può avere tre valori \'StraightRebar\', \'LShapeRebar\' e \'UShapeRebar\'.
-   {{ PropertyData\|Front Cover}}: La distanza tra l\'armatura parallela e la faccia selezionata.
-   {{ PropertyData\|Left Cover}}: La distanza tra l\'estremità sinistra dell\'armatura parallela e la faccia sinistra della struttura..
-   {{ PropertyData\|Right Cover}}: La distanza tra l\'estremità destra dell\'armatura parallela e la faccia destra della struttura..
-   {{ PropertyData\|Bottom Cover}}: La distanza tra le armature parallele dalla faccia inferiore della struttura.
-   {{ PropertyData\|Top Cover}}: La distanza tra le armature parallele dalla faccia superiore della struttura.
-   {{ PropertyData\|Rear Cover}}: Copriferro posteriore per l\'armatura di fondazione delle armature parallele.
-   {{ PropertyData\|Rounding}}: Un valore di arrotondamento da applicare agli angoli delle barre, espresso in numero di volte il diametro delle barre parallele..
-   {{ PropertyData\|Diameter}}: Diametro delle armature parallele
-   {{ PropertyData\|Amount}}: Contiene il numero di armature parallele.
-   {{ PropertyData\|Spacing}}: Contiene il passo tra le armature parallele.

**Proprietà per le armature in direzione trasversale rispetto alla faccia selezionata per l\'armatura di fondamenta:**

-    **Rebar Type**: Tipo di armatura per le armature trasversali per l\'armatura di fondamenta. Può avere tre valori \'StraightRebar\', \'LShapeRebar\' e \'UShapeRebar\'.

-    **Front Cover**: La distanza tra l\'armatura trasversale e la faccia trasversale (faccia perpendicolare alla faccia selezionata).

-    **Left Cover**: La distanza tra l\'estremità sinistra dell\'armatura trasversale e la faccia sinistra della struttura..

-    **Right Cover**: La distanza tra l\'estremità destra dell\'armatura trasversale e la faccia destra della struttura.

-    **Bottom Cover**: La distanza tra le barre trasversali dalla faccia inferiore della struttura.

-    **Top Cover**: La distanza tra le barre trasversali dalla faccia superiore della struttura.

-    **Rear Cover**: Copriferro posteriore per le barre trasversali dell\'armatura di fondazione.

-    **Rounding**: Un valore di arrotondamento da applicare agli angoli delle barre, espresso in numero di volte il diametro delle barre trasversali.

-    **Diameter**: Diametro delle barre trasversali

-    **Amount**: Contiene il numero delle barre trasversali.

-    **Spacing**: Contiene la distanza tra le barre trasversali.

**Proprietà per i pilastri nell\'armatura di fondamenta:**

-    **Front Cover**: Distanza tra la faccia selezionata e le colonne.

-    **Left Cover**: Distanza tra la faccia sinistra e le colonne.

-    **Right Cover**: Distanza tra la faccia destra e le colonne.

-    **Rear Cover**: Distanza tra la faccia posteriore e le colonne.

-    **Column Width**: Larghezza della colonna.

-    **Column Length**: Lunghezza della colonna.

-    **X direction column amount**: Contiene il numero delle colonne nella direzione x. Se è selezionata l\'opzione per il conteggio nella direzione X.

-    **X direction column spacing**: Contiene il passo tra le colonne nella direzione x. Se è selezionata l\'opzione per il conteggio nella direzione X.

-    **Y direction column amount**: Contiene il numero delle colonne nella direzione y.Se è selezionata l\'opzione per il conteggio nella direzione Y.

-    **Y direction column spacing**: Contiene il passo tra le colonne nella direzione y. Se è selezionata l\'opzione per il conteggio nella direzione Y.

-    **Add Secondary Rebars**: Se selezionato, aggiunge le armature secondarie nelle direzioni x e y nelle colonne.

**Proprietà per i Tiranti nei pilastri dell\'Armatura di fondamenta:**

-    **Top Cover**: Copriferro superiore per i tiranti esterni del basamento dall\'estremità delle armature principali.

-    **Bottom Cover **: Copriferro inferiore dei tiranti dalla parte inferiore delle armature principali nel plinto vicino alla rete.

-    **Diameter**: Diametro dei tiranti.

-    **Bent Angle**: Angolo di piega per i tiranti.

-    **Extension Factor**: Fattore di allungamento per i tiranti con bordo allungato.

-    **Tie Number**: Contiene il numero delle armature o il passo tra i tiranti, se l\'opzione Number è selezionata.

-    **Tie Spacing**: Contiene il passo tra i tiranti, se l\'opzione Spacing è selezionata.

**Proprietà delle armature principali per i Pilastri nell\'armatura di fondamenta:**

-    **Rebar Type**: tipo di armatura per le armature principali del pilastro. Sono necessari due valori diversi per \"StraightRebar\", \"LShapeRebar\".

-    **Hook Orientation**: orientamento del gancio delle armature principali nei pilastri se il tipo di barra principale è LShapeRebar. Sono necessari otto diversi orientamenti per i ganci a L, ad es. \'Top Inside\', \'Top Outside\', \'Bottom Inside\', \'Bottom Outside\', \'Top Left\', \'Top Right\', \'Bottom Left\', \'Bottom Right\'.

-    **Hook Extend Along**: direzione del gancio principale dell\'armatura (LShapeRebar). ha due opzioni \"x-axis\" e \"y-axis\".

-    **Hook Extension**: Specifica la lunghezza del gancio dell\'armatura principale (LShapeRebar).

-    **Rebar Rounding**: Un valore di arrotondamento da applicare agli angoli delle barre, espresso in numero di volte il diametro dell\'armatura principale.

-    **Top Offset**: Offset superiore delle armature principali nel pilastro esterno al plinto della faccia superiore.

-    **Diameter**: Diametro delle armature principali nei pilastri.

**Proprietà per le armature in direzione X nei pilastri dell\'armatura di fondamenta:**

Armature lungo la direzione x tranne le armature principali

-    **Rebar Type**: Tipo di armature di un pilastro nella direzione x. Ha due valori, \'StraightRebar\' e \'LShapeRebar\'.

-    **Hook Orientation**: Orientamento dei ganci dell\'armatura a forma di L. Ci sono otto diversi orientamenti per i ganci a forma di L, ad es. \'Top Inside\', \'Top Outside\', \'Bottom Inside\', \'Bottom Outside\', \'Top Left\', \'Top Right\', \'Bottom Left\', \'Bottom Right\'.

-    **Hook Extension**: Lunghezza del gancio delle armature a L.

-    **Rounding**: Un valore di arrotondamento da applicare agli angoli delle armature a L, espresso in numero di volte il diametro.

-    **Top Offset**: La distanza tra l\'armatura e la faccia superiore della struttura.

-    **Number#Diameter**: Number#Diameter insieme delle armature nella direzione x.

**Proprietà per le armature in direzione Y nei pilastri dell\'armatura di fondamenta:**

Armature lungo la direzione Y tranne le armature principali

-    **Rebar Type**: Tipo di armature in direzione y. Ha due valori, \'StraightRebar\' e \'LShapeRebar\'.

-    **Hook Orientation**: Orientamento dei ganci a L. Ci sono otto diversi orientamenti per i ganci a L, ad es. \'Top Inside\', \'Top Outside\', \'Bottom Inside\', \'Bottom Outside\', \'Top Left\', \'Top Right\', \'Bottom Left\', \'Bottom Right\'.

-    **Hook Extension**: Lunghezza del gancio delle armature a L.

-    **Rounding**: Un valore di arrotondamento da applicare agli angoli delle armature a L, espresso in numero di volte il diametro.

-    **Top Offset**: La distanza tra l\'armatura e la faccia superiore della struttura.

-    **Number#Diameter**: Number#Diameter insieme delle armature in direzione y.



## Script


**See also:**

[API di Arch](Arch_API/it.md), [API di Reinforcement](Reinforcement_API/it.md) and [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).


<div class="mw-translate-fuzzy">

Lo strumento Armatura di Fondamenta può essere utilizzato dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>



### Creare Armatura di Fondamenta 


```python
from FootingReinforcement.FootingReinforcement import makeFootingReinforcement

footingReinforcementGroup = makeFootingReinforcement(
    parallel_rebar_type,
    parallel_front_cover,
    parallel_rear_cover,
    parallel_left_cover,
    parallel_right_cover,
    parallel_top_cover,
    parallel_bottom_cover,
    parallel_diameter,
    parallel_amount_spacing_check,
    parallel_amount_spacing_value,
    cross_rebar_type,
    cross_front_cover,
    cross_rear_cover,
    cross_left_cover,
    cross_right_cover,
    cross_top_cover,
    cross_bottom_cover,
    cross_diameter,
    cross_amount_spacing_check,
    column_front_cover,
    column_left_cover,
    column_right_cover,
    column_rear_cover,
    tie_top_cover,
    tie_bottom_cover,
    tie_bent_angle,
    tie_extension_factor,
    tie_diameter,
    tie_number_spacing_check,
    tie_number_spacing_value,
    column_main_rebar_diameter,
    column_main_rebars_t_offset,
    cross_amount_spacing_value,
    column_width,
    column_length,
    xdir_column_amount_spacing_check = True,
    xdir_column_amount_spacing_value = 1,
    ydir_column_amount_spacing_check = True,
    ydir_column_amount_spacing_value = 1,
    parallel_rounding = 2,
    parallel_l_shape_hook_orintation = "Alternate",
    cross_rounding = 2,
    cross_l_shape_hook_orintation = "Alternate",
    column_main_rebars_type = "StraightRebar",
    column_main_hook_orientation = "Bottom Outside",
    column_main_hook_extend_along = "x-axis",
    column_l_main_rebar_rounding = 2,
    column_main_hook_extension = 40,
    column_sec_rebar_check = False,
    column_sec_rebars_t_offset = (400, 400),
    column_sec_rebars_number_diameter = (
        "1#8mm+1#8mm+1#8mm",
        "1#8mm+1#8mm+1#8mm",
    ),
    column_sec_rebars_type = (
        "StraightRebar",
        "StraightRebar",
    ),
    column_sec_hook_orientation = (
        "Top Inside",
        "Top Inside",
    ),
    column_l_sec_rebar_rounding = (2, 2),
    column_sec_hook_extension = (40, 40),
    mesh_cover_along = "Bottom",
    structure = None,
    facename = None,
)
```

-   Crea un oggetto `footingReinforcementGroup` a partire dalla data `structure`, che è una [Struttura di Arch](Arch_Structure/it.md), e `facename`, che è una faccia di quella struttura.
    -   Se non vengono forniti né `structure` né `facename`, prenderà come input la faccia selezionata dall\'utente.

**Proprietà per le armature in direzione parallela alla faccia selezionata:**.

-    `parallel_rebar_type`: Tipo di armatura per armature parallele nell\'armatura di fondamenta. Può avere tre valori \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\'.

-    `parallel_front_cover`: La distanza tra l\'armatura parallela e la faccia selezionata.

-    `parallel_rear_cover`: Copriferro posteriore delle armature parallele per l\'armatura di fondamenta.

-    `parallel_left_cover`: La distanza tra l\'estremità sinistra dell\'armatura parallela e la faccia sinistra della struttura.

-    `parallel_right_cover`: La distanza tra l\'estremità destra dell\'armatura parallela e la faccia destra della struttura.

-    `parallel_top_cover`: La distanza tra le armature parallele e la faccia superiore della struttura.

-    `parallel_bottom_cover`: La distanza tra le armature parallele e la faccia inferiore della struttura.

-    `parallel_diameter`: Diametro delle armature parallele.

-    `parallel_amount_spacing_check`: Se è impostato su True, il valore di parallel_amount_spacing_value viene utilizzato come numero delle barre d\'armatura, altrimenti il ​​valore di parallel_amount_spacing_value viene utilizzato come passo per le barre d\'armatura parallele.

-    `parallel_amount_spacing_value`: Contiene il numero di barre d\'armatura o il passo tra barre d\'armatura parallele in base al valore di amount_spacing_check.

-    `parallel_rounding`: Un valore di arrotondamento da applicare agli angoli delle barre, espresso in numero di volte il diametro_parallelo.

-    `parallel_l_shape_hook_orintation`: Rappresenta l\'orientamento del gancio dell\'armatura parallela a forma di L se parallel_rebar_type è LShapeRebar. Può avere tre valori \"Left\", \"Right\",\"Alternate\"

**Proprietà per le armature in direzione trasversale rispetto alla faccia selezionata:**.

-    `cross_rebar_type`: Tipo di armatura per le armature trasversali per le armatura di fondazione. Può avere tre valori \'StraightRebar\', \'LShapeRebar\' e \'UShapeRebar\'.

-    `cross_front_cover`: La distanza tra l\'armatura trasversale e la faccia trasversale (faccia perpendicolare alla faccia selezionata).

-    `cross_rear_cover`: Copriferro posteriore per le barre trasversali dell\'armatura di fondazione.

-    `cross_left_cover`: La distanza tra l\'estremità sinistra dell\'armatura trasversale e la faccia sinistra della struttura..

-    `cross_right_cover`: La distanza tra l\'estremità destra dell\'armatura e la faccia destra della struttura rispetto alla faccia trasversale.

-    `cross_top_cover`: La distanza tra le armature trasversali e la faccia superiore della struttura.

-    `cross_bottom_cover`: La distanza tra le armature trasversali e la faccia inferiore della struttura.

-    `cross_diameter`: Diametro delle barre trasversali.

-    `cross_amount_spacing_check`: Se è impostato su True, il valore di cross_amount_spacing_value viene utilizzato come numero delle barre, altrimenti il valore di cross_amount_spacing_value viene utilizzato come passo tra le barre.

-    `cross_amount_spacing_value`: Contiene il numero di barre o la distanza tra le barre in base al valore di cross_amount_spacing_check.

-    `cross_rounding`: Un valore di arrotondamento da applicare agli angoli delle barre, espresso in numero di volte il cross_diameter.

-    `cross_l_shape_hook_orintation`: Rappresenta l\'inclinazione dell\'aggancio della barra a L se il tipo di traversa è LShapeRebar. Può avere tre valori \"Left\", \"Right\" e \"Alternate\"

**Proprietà dei pilastri nell\'armatura di fondamenta:**

-    `column_front_cover`: Distanza tra la faccia selezionata e i pilastri.

-    `column_left_cover`: Distanza tra la faccia sinistra e i pilastri.

-    `column_right_cover`: Distanza tra la faccia destra e i pilastri destri.

-    `column_rear_cover`: Distanza tra la faccia posteriore e i pilastri posteriori.

-    `column_width`: Larghezza dei pilastri.

-    `column_length`: Lunghezza dei pilastri.

-    `xdir_column_amount_spacing_check`: Se è impostato su True, il valore di xdir_column_amount_spacing_value viene utilizzato come numero di colonne, altrimenti il ​​valore di xdir_column_amount_spacing_value viene utilizzato come passo delle colonne nella direzione x.

-    `xdir_column_amount_spacing_value`: Contiene il numero di colonne o il passo tra le colonne nella direzione x in base al valore di xdir_column_amount_spacing_check.

-    `ydir_column_amount_spacing_check`: Se è impostato su True, il valore di ydir_column_amount_spacing_value viene utilizzato come numero di colonne, altrimenti il ​​valore di ydir_column_amount_spacing_value viene utilizzato come passo delle colonne nella direzione y.

-    `ydir_column_amount_spacing_value`: Contiene il numero di colonne o il passo tra le colonne nella direzione y in base al valore di ydir_column_amount_spacing_check.

-    `column_sec_rebar_check`: Se True, aggiunge le armature secondarie in direzione x e y nei pilastri.

**Proprietà dei Tiranti dei pilastri nell\'Armatura di fondamenta:**

-    `tie_top_cover`: Copriferro superiore per i tiranti esterni del basamento dall\'estremità delle armature principali.

-    `tie_bottom_cover`: Copriferro inferiore dei tiranti dalla parte inferiore delle armature principali nel plinto vicino alla rete.

-    `tie_bent_angle`: Angolo di piega per i tiranti.

-    `tie_extension_factor`: Fattore di allugamento per i tiranti con bordo esteso.

-    `tie_diameter`: Diametro dei tiranti.

-    `tie_number_spacing_check`: Se è impostato su True, il valore di tie_number_spacing_value viene utilizzato come numero di tiranti, altrimenti il ​​valore di tie_number_spacing_value viene utilizzato come valore di passo dei tiranti.

-    `tie_number_spacing_value`: Contiene il numero di tiranti o il passo dei tiranti in base al valore di tie_number_spacing_check.

**Proprietà delle armature principali per i Pilastri nell\'armatura di fondamenta:**

-    `column_main_rebar_diameter`: Diametro delle armature principali nei pilastri.

-    `column_main_rebars_t_offset`: Offset superiore delle armature principali nella fondazione esterna del pilastro.

-    `column_main_hook_extend_along`: Direzione del gancio dell\'armatura principale (LShapeRebar). Ha due opzioni \"x-axis\" e \"y-axis\".

-    `column_l_main_rebar_rounding`: Un valore di arrotondamento da applicare agli angoli delle barre, espresso in numero di volte il column_main_rebar_diameter.

-    `column_main_hook_extension`: Specifica la lunghezza del gancio dell\'armatura principale (LShapeRebar).

-    `column_main_rebars_type`: Tipo di armatura per le armature principali del pilastro. Sono possibili due input diversi \'StraightRebar\' e \'LShapeRebar\'. L\'impostazione predefinita è StraightRebar.

-    `column_main_hook_orientation`: Orientamento del gancio delle armature principali dei pilastri se column_main_rebars_type è LShapeRebar. Sono possibili otto diversi orientamenti per i ganci a L, ad es.\'Top Inside\', \'Top Outside\', \'Bottom Inside\', \'Bottom Outside\', \'Top Left\', \'Top Right\', \'Bottom Left\', \'Bottom Right\'.

**Proprietà delle armature secondarie nelle direzioni X e Y per le Armature di fondamenta:**

-    `column_sec_rebars_t_offset`e `sec_rebars_b_offset` sono tuple (xdir_rebars_t_offset, ydir_rebars_t_offset) che definiscono le distanze di offset (o altezza) per le armature secondarie in direzione x e y rispetto alle facce superiori della struttura, rispettivamente.

-    `column_sec_rebars_number_diameter`è una tupla (xdir_rebars_number_diameter, ydir_rebars_number_diameter) che definisce rispettivamente l\'insieme number#diameter delle armature secondarie nella direzione x e nella direzione y.

-    `column_sec_rebars_type`è una tupla (xdir_rebars_type, ydir_rebars_type) che definisce rispettivamente il tipo delle armature secondarie nella direzione x e nella direzione y; può avere `"StraightRebar"` o `"LShapeRebar"` come tipo di armatura.

-    `column_sec_hook_orientation`è una tupla (xdir_hook_orientation, ydir_hook_orientation) che definisce l\'orientamento del gancio a forma di L della direzione x secondaria e della direzione y; può avere `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, `"Top Right"`, `"Top Left"`, `"Bottom Right"` o `"Bottom Left"` come hook_orientation.

-    `column_l_sec_rebar_rounding`è una tupla (l_xdir_rebar_rounding, l_ydir_rebar_rounding) che determina il raggio di piegatura delle barre secondarie a forma di L nella direzione x e nella direzione y, espresso come multiplo del diametro delle barre d\'armatura a L nella direzione x e nella direzione y, rispettivamente.

-    `column_sec_hook_extension`è una tupla (xdir_hook_extension, ydir_hook_extension) che definisce la lunghezza del gancio delle armature secondarie a forma di L nella direzione x e nella direzione y.

**Proprietà comuni per l\'Armatura di Fondamenta**

-    `mesh_cover_along`: Può avere tre valori \"Top\", \"Bottom\" e \"Both\". Rappresenta l\'allineamento della rete dell\'armatura lungo la faccia superiore e/o inferiore della struttura.

-    `structure`: Oggetto struttura Arch. L\'impostazione predefinita è None

-    `facename`: faccia selezionata della struttura. L\'impostazione predefinita è None



### Modifica delle Armature di Fondamenta 


<div class="mw-translate-fuzzy">

È possibile modificare le proprietà dell\'Armatura di Fondamenta con la seguente funzione


</div>


```python
from FootingReinforcement.FootingReinforcement import editFootingReinforcement

footingReinforcementGroup = editFootingReinforcement(
    footingReinforcementGroup,
    parallel_rebar_type,
    parallel_front_cover,
    parallel_rear_cover,
    parallel_left_cover,
    parallel_right_cover,
    parallel_top_cover,
    parallel_bottom_cover,
    parallel_diameter,
    parallel_amount_spacing_check,
    parallel_amount_spacing_value,
    cross_rebar_type,
    cross_front_cover,
    cross_rear_cover,
    cross_left_cover,
    cross_right_cover,
    cross_top_cover,
    cross_bottom_cover,
    cross_diameter,
    cross_amount_spacing_check,
    column_front_cover,
    column_left_cover,
    column_right_cover,
    column_rear_cover,
    tie_top_cover,
    tie_bottom_cover,
    tie_bent_angle,
    tie_extension_factor,
    tie_diameter,
    tie_number_spacing_check,
    tie_number_spacing_value,
    column_main_rebar_diameter,
    column_main_rebars_t_offset,
    cross_amount_spacing_value,
    column_width,
    column_length,
    xdir_column_amount_spacing_check = True,
    xdir_column_amount_spacing_value = 1,
    ydir_column_amount_spacing_check = True,
    ydir_column_amount_spacing_value = 1,
    parallel_rounding = 2,
    parallel_l_shape_hook_orintation = "Alternate",
    cross_rounding = 2,
    cross_l_shape_hook_orintation = "Alternate",
    column_main_rebars_type = "StraightRebar",
    column_main_hook_orientation = "Bottom Outside",
    column_main_hook_extend_along = "x-axis",
    column_l_main_rebar_rounding = 2,
    column_main_hook_extension = 40,
    column_sec_rebar_check = False,
    column_sec_rebars_t_offset = (400, 400),
    column_sec_rebars_number_diameter = (
        "1#8mm+1#8mm+1#8mm",
        "1#8mm+1#8mm+1#8mm",
    ),
    column_sec_rebars_type = (
        "StraightRebar",
        "StraightRebar",
    ),
    column_sec_hook_orientation = (
        "Top Inside",
        "Top Inside",
    ),
    column_l_sec_rebar_rounding = (2, 2),
    column_sec_hook_extension = (40, 40),
    mesh_cover_along = "Bottom",
    structure = None,
    facename = None,
)
```

-    `footingReinforcementGroup`è un oggetto del gruppo `Footing Reinforcement` creato in precedenza.

-   Gli altri parametri sono gli stessi richiesti dalla funzione `makeFootingReinforcement()`.


<div class="mw-translate-fuzzy">





</div>




{{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement FootingRebars/it
