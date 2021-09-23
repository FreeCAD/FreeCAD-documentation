---
- GuiCommand:/it   Name:TechDraw_Dimension_Length   Name/it:Lunghezza   Workbenches:[MenuLocation:TechDraw → Lunghezza   Shortcut:   SeeAlso:[[TechDraw Dimension Horizontal/it|Dimensione orizzontale](TechDraw_Workbench/it___TechDraw]].md), [Dimensione verticale](TechDraw_Dimension_Vertical/it.md)---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Lunghezza aggiunge una dimensione lineare ad una vista. La dimensione può essere la distanza tra due vertici, la lunghezza di uno spigolo o la distanza tra 2 spigoli. La distanza indicata all\'inizio è la distanza proiettata (vale a dire, come mostrata nel disegno), ma utilizzando lo strumento **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Link alla dimensione](TechDraw_Dimension_Link/it.md)** essa può essere modificata con la distanza 3D effettiva.


</div>

<img alt="" src=images/TechDraw_Dimension_Length_example.png  style="width:220px;"> 
*Dimensione della lunghezza presa da due nodi arbitrari della vista*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare i punti o i bordi che definiscono la misura.
2.  Premere il pulsante **<img src="images/TechDraw_Dimension_Length.svg" width=20px> [Lunghezza](TechDraw_Dimension_Length/it.md)
**
3.  Alla vista viene aggiunta una dimensione. La dimensione può essere trascinata nella posizione desiderata.


</div>

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the dimension dialog:

## Dimension dialog 

The dimension dialog offers the following settings:

![](images/TechDraw_DimensionDialog.png )

### Tolerancing

-   **Theoretically Exact**: If checked, is specifies the dimension as theoretically exact dimension. As such, it shall not bear any tolerances. The dimension will be displayed by a frame around the value: <img alt="" src=images/TechDraw_theoretically_exact.png  style="width:100px;">

-   **Equal Tolerance**: If checked, the over- and undertolerance are equal and the negated value of the overtolerance is used as undertolerance. The display will be <img alt="" src=images/TechDraw_equal-tolerance.png  style="width:100px;">, otherwise it will be <img alt="" src=images/TechDraw_Non-equal-tolerance.png  style="width:80px;">.

-   **Overtolerance**: The amount by which the dimension may be larger.

-   **Undertolerance**: The amount by which the dimension may be smaller.

### Formatting

-   **Format Specifier**: How the dimension value will be formatted. By default the specifier is *%.xf* whereby *x* is the number of decimals. For the formatting syntax see [this Wikipedia page](https://en.wikipedia.org/wiki/Printf_format_string).

-   **Arbitrary Text**: If checked, the dimension is replaced by the content of the **Format Specifier** field.

-   **OverTolerance Format Specifier**: How the overtolerance value will be formatted. By default the specifier is *%.xf* whereby *x* is the number of decimals. For the formatting syntax see [this Wikipedia page](https://en.wikipedia.org/wiki/Printf_format_string).

-   **UnderTolerance Format Specifier**: How the undertolerance value will be formatted. By default the specifier is *%.xf* whereby *x* is the number of decimals. For the formatting syntax see [this Wikipedia page](https://en.wikipedia.org/wiki/Printf_format_string).

-   **Arbitrary Tolerance Text**: If checked, the tolerances are replaced by the content of the **OverTolerance Format Specifier** **UnderTolerance Format Specifier** fields.

### Display Style 

-   **Flip Arrowheads**: Flips the direction in which the dimension line arrows are pointing. By default they are inside the dimension line/arc and pointing outwards.

-   **Color**: The color for lines and text.

-   **Font Size**: The dimension text size.

-   **Drawing Style**: The standard (and its style) according to which the dimension is drawn. See the property [**Standard And Style**](#View.md) for details.

## Proprietà

### Dati


{{Properties_Title|Base}}

-    **X**: posizione orizzontale del testo della quota rispetto alla vista.

-    **Y**: posizione verticale del testo della quota rispetto alla vista.

-    **Type**: lunghezza, raggio, diametro, ecc. Normalmente non viene manipolato dall\'utente finale.

-    **MeasureType**: `True` - basato sulla geometria 3D o \"Proiettato\" - basato sul disegno. Normalmente non manipolato direttamente dall\'utente finale.

-    **TheoreticalExact**: specifica una dimensione teoricamente esatta (o di base).

:   

    :   
        `False`
        
        \- una dimensione comune di default, accetta le tolleranze.

    :   
        `True`
        
        \- un valore teorico. In quanto tale, non accetta alcuna tolleranza. Contrassegnata da una cornice attorno al valore.

-    **OverTolerance**: scostamento superiore rispetto alla dimensione mostrata.

-    **UnderTolerance**: scostamento inferiore rispetto alla dimensione mostrata.

-    **Inverted**: Indica se la dimensione rappresenta un valore normale o invertito.

:   

    :   
        `False`
        
        \- viene utilizzato il valore ordinario. Per la lunghezza è un numero positivo, per un angolo è il valore dell\'inclinazione (0° - 180°).

    :   
        `True`
        
        \- viene utilizzato il valore invertito. Per la lunghezza è un numero negativo, per un angolo è il valore riflesso (180° - 360°).


{{Properties_Title|Format}}

-    **FormatSpec**: consente di aggiungere u testo aggiuntivo al testo della dimensione.

:   

    :   il valore della dimensione sostituisce la parte del testo %.2f (o qualsiasi altro identificatore di formato valido - vedere [printf](https://en.wikipedia.org/wiki/Printf_format_string)).

-    **Arbitrary**: specifica se trattare **FormatSpec** come modello o testo reale.

:   

    :   
        `False`
        
        \- sostituisce l\'identificatore di formato con il valore dimensionale effettivo.

    :   
        `True`
        
        \- ignora il valore dimensionale e visualizza esattamente **FormatSpec** come valore.

### Vista


{{Properties_Title|Base}}

-    **Visibility**: imposta se la dimensione è visibile. `True` - visibile, `False` - nascosta.


{{Properties_Title|Dim Format}}

-    **Font**: il nome del carattere da utilizzare per il testo della quota.

-    **FontSize**: dimensione del testo in mm.

-    **LineWidth**: spessore della linea di dimensione.

-    **Color**: colore per linee e testo.

-    **StandardAndStyle**: specifica lo standard (e lo stile di esso) in base al quale viene disegnata la dimensione:

:   

    :   ISO Oriented - disegnata secondo ISO 129.1 (standard internazionale), il testo viene ruotato per essere parallelo alla tangente della linea di quota.
    :   ISO Referencing - disegnata secondo ISO-129.1, il testo è sempre orizzontale, sopra la linea di riferimento più breve possibile.
    :   ASME Inlined - disegnata secondo ASME Y14.5M (standard USA), il testo è orizzontale, inserito in un\'interruzione all\'interno della linea di quota o dell\'arco.
    :   ASME Referencing - disegnata secondo ASME Y14.5M, il testo è orizzontale, una breve linea di riferimento è attaccata al centro verticale di un lato.

-    **RenderingExtent**: proprietà piuttosto universale che specifica quanto spazio può occupare il disegno quotato:

:   

    :   None - non vengono disegnate linee o frecce, viene visualizzato solo il valore della quota.
    :   Minimal - per lunghezze e angoli viene disegnata una linea a testa singola che collega il valore dimensionale e la *linea di estensione virtuale* del punto finale. La linea di estensione non viene aggiunta.
    :   I diametri vengono visualizzati secondo l\'estensione Confined, i raggi secondo l\'estensione Reduced.
    :   Confined - per lunghezze e angoli viene disegnata una linea a due punte (o arco) che collega le *linee di estensione virtuali* dei punti iniziale e finale, sebbene le linee di estensione stesse non vengano aggiunte.
    :   I diametri sono disegnati con una linea singola minima dal valore dimensionale al punto più vicino sul cerchio, i raggi come con l\'estensione Reduced.
    :   Reduced - per lunghezze e angoli viene disegnata una linea a testa singola che collega il valore dimensionale e la *linea di estensione* del punto finale con la linea di estensione stessa.
    :   I diametri sono disegnati con una linea singola dal centro al punto più vicino sul cerchio, i raggi con una linea singola minima dal valore dimensionale al punto dell\'arco più vicino.
    :   Normal - il valore predefinito. Per lunghezze e angoli viene disegnata una linea a due punte (o arco) che collega le *linee di estensione* dei punti iniziale e finale, sono anche disegnate le linee di estensione.
    :   I diametri sono disegnati come linee a due punte che colpiscono il centro e collegano i punti più vicini e più lontani sul cerchio.
    :   I raggi sono disegnati come un\'unica linea di testa dal centro al punto di arco più vicino.
    :   Expanded - solo i diametri supportano questo valore, rendendoli in una lunghezza orizzontale o verticale. Gli altri tipi di dimensione vengono visualizzati come con l\'estensione Normal.

-    **FlipArrowheads**: di default, con il valore *inside* le frecce puntano *verso l\'esterno* della linea o arco di quotatura. Con *outside* le frecce puntano *verso l\'interno* della linea o arco di quotatura.

:   

    :   
        `False`
        
        \- lascia che la direzione delle frecce sia selezionata automaticamente secondo la regola pecedente.

    :   
        `True`
        
        \- ignora la direzione scelta automaticamente e forza quella opposta.

## Limitazioni


<div class="mw-translate-fuzzy">

Gli oggetti dimensione sono vulnerabili ai problemi di \"[denominazione topologica](topological_naming_problem/it.md)\". Ciò significa che se si modifica la geometria 3D, le facce e i bordi del modello possono essere rinominati internamente; se una quota è collegata a un bordo che viene poi modificato, la dimensione potrebbe interrompersi. In generale, non è possibile mantenere sincronizzate le dimensioni 2D proiettate con gli oggetti 3D reali.


</div>

Pertanto, si consiglia di aggiungere le dimensioni verso la fine del processo di creazione del modello, quando il modello non viene più modificato.

### Soluzione

Se si desidera mantenere una vista di TechDraw con dimensioni che non si interrompono, è necessario dimensionare un oggetto che non cambierà più.

-   Selezionare l\'oggetto che si vuole proiettare, quindi passare a <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/it.md) e usare **Part → <img src="images/Part_SimpleCopy.svg" width=16px> [Crea una copia semplice](Part_SimpleCopy/it.md)**. Questo crea un singolo oggetto che non è parametrico, quindi non è più modificabile.
-   Selezionare questa copia, quindi usare [Nuova vista](TechDraw_NewView/it.md), e aggiungere le dimensioni desiderate.
-   Se il modello 3D originale viene modificato, le modifiche non avranno effetto sulla copia semplice, né sulle dimensioni nella vista di TechDraw.


<div class="mw-translate-fuzzy">

Vedere [Dimensione da punti di riferimento](TechDraw_Dimension_Landmark/it.md) per un altro approccio per aggirare il problema della denominazione topologica.


</div>

## Script


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


<div class="mw-translate-fuzzy">

Lo strumento Dimensione orizzontale può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Distance"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```

## Note

-   **Selezione dei bordi**. I bordi possono essere difficili da selezionare. Si può regolare l\'area di selezione per i bordi usando il parametro \"/Mod/TechDraw/General/EdgeFuzz\" (vedere [Parametri standard](Std_DlgParameter/it.md)). Questo è un numero senza dimensioni. Il valore predefinito è 10.0. I valori nell\'intervallo 20-30 rendono notevolmente più semplice la selezione dei bordi. I numeri più grandi causano sovrapposizioni con altri elementi di disegno.
-   **Numero di decimali**. Le dimensioni utilizzano l\'impostazione delle posizioni decimali globali per impostazione predefinita. Questo può essere modificato tramite le [preferenze](TechDraw_Preferences/it#Dimensioni.md) o modificando la proprietà FormatSpec.
-   **Qualsiasi oggetto**. Le viste possono contenere più oggetti 3D come Sorgente. Le quote possono essere applicate alla geometria da qualsiasi oggetto nella vista (ad es. Da Object1.Vertex0 a Object2.Vertex3).


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}} 
