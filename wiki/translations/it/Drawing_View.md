---
- GuiCommand:/it
   Name:Drawing View
   Name/it:Inserisci vista
   Workbenches:[Disegno](Drawing_Workbench/it.md), Completo
   MenuLocation:Disegno → Inserisci Vista
   Shortcut:Nessuno
   SeeAlso:[Disegno A3](Drawing_Landscape_A3/it.md)
---

# Drawing View/it

Questo strumento crea una nuova vista dell\'oggetto selezionato e la posiziona nel foglio di disegno attivo.

<img alt="Un foglio di disegno con due proiezioni, frontale e dall\'alto, e una vista isometrica." src=images/Drawing_Views_fr.png  style="width:500px;">

### Utilizzo

Selezionare un oggetto nella vista 3D o nella struttura del progetto, quindi fare clic sullo strumento *Inserisci vista* del disegno. Per impostazione predefinita, viene inserita una vista dall\'alto in scala 1:1 (scala reale), posizionata in alto a sinistra della pagina. Se la vista è troppo piccola o troppo grande per la pagina, può risultare non visibile.

Nell\'albero del progetto viene aggiunto un oggetto **View** sotto l\'oggetto **Page**. Per le viste successive, viene aggiunto al nome un numero a tre cifre. Fare clic sulla freccia davanti all\'oggetto Page per dispiegarla e visualizzarne il contenuto.

Se nella struttura ad albero del progetto viene selezionato solo l\'oggetto, la vista viene aggiunta alla prima pagina del progetto. Quando il progetto è composto da più pagine si deve selezionare l\'oggetto e la pagina in cui deve essere aggiunto, poi fare clic sull\'icona per aggiungere la vista alla pagina selezionata.

### Modificare una vista esistente 

Dispiegare l\'oggetto Page nella struttura del Progetto, quindi selezionare la vista da modificare. I suoi parametri possono essere modificati nella scheda Dati della finestra Proprietà di visualizzazione.

<img alt="" src=images/Drawing_View_Properties.png‎ ) ![Vista isometrica con « smooth lines visibility » disattivata](images/Drawing_View_Iso.png‎  style="width:150px;"> <img alt="Vista isometrica con « smooth lines visibility » attivata" src=images/Drawing_View_Iso_SmoothLines.png‎‎  style="width:150px;">

-   **Label** : cambia l\'etichetta della vista nella struttura del progetto. È anche possibile fare clic su Vista nella struttura e fare clic destro → Rinomina, oppure premere {{KEY/it|F2}}.
-   **Rotation** : ruota la vista. Ad esempio, una vista isometrica richiede una rotazione di 60 gradi (vedere anche il sottostante parametro Direction)
-   **Scale** : imposta la scala di visualizzazione.
-   **X** : imposta in millimetri la posizione orizzontale della vista nella pagina.
-   **Y** : imposta in millimetri la posizione verticale della vista nella pagina. Notare che le coordinate (0,0) si trovano in alto a sinistra della pagina, quindi maggiore è il numero e più la vista viene spostata in basso.
-   **Direction** : cambia la direzione della vista. Questo viene determinato dal valori xyz che definiscono un vettore normale alla pagina. La vista dall\'alto è (0,0,1), e isometrica è (1,1,1). I valori possono anche essere negativi.
-   **Show Hidden Lines** : commuta la visibilità delle nascosta linee selezionando *True* (vero) o *False* (falso).
-   **Show Smooth Lines** : attiva o disattiva la lisciatura delle linee selezionando *True* (vero) o *False* (falso). Le linee morbide sono anche chiamate bordi di tangenza. Si tratta di linee di demarcazione tra due superfici tangenti.

### Disegnare automaticamente una vista 

Per generare automaticamente un foglio di disegno con viste standard, utilizzare la [Macro vista automatica](Macro_Automatic_drawing/it.md). 

### Altro

Per commutare la vista 3D tra ortogonale e prospettica selezionare [Vista in prospettivo](Std_PerspectiveCamera/it.md) o [Vista ortografica](Std_OrthographicCamera/it.md)


{{docnav/it
|[Nuovo disegno A3 orizzontale](Drawing_Landscape_A3/it.md)
|[Annotazione](Drawing_Annotation/it.md)
|[Drawing](Drawing_Workbench/it.md)
|IconL=Drawing_Landscape_A3.png
|IconC=Workbench_Drawing.svg
|IconR=Drawing_Annotation.png
}}


{{Drawing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing View/it
