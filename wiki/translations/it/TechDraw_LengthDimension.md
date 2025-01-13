---
 GuiCommand:
   Name: TechDraw LengthDimension
   Name/it: TechDraw Quota Allineata
   MenuLocation: TechDraw , Quotatura , Inserisci Quota Allineata
   Workbenches: TechDraw_Workbench/it
   SeeAlso: TechDraw_HorizontalDimension/it, TechDraw_VerticalDimension/it
---

# TechDraw LengthDimension/it



## Descrizione

Lo strumento **TechDraw Quota Allineata** aggiunge una quota lineare a una Vista. La quota può essere la distanza tra due punti, la lunghezza di un bordo dritto, la distanza perpendicolare tra due bordi o la distanza perpendicolare tra un punto e un bordo.

<img alt="" src=images/TechDraw_Dimension_Length_example.png  style="width:220px;"> 
*Quotatura allineata della distanza presa da due punti*



## Utilizzo

1.  Selezionare i punti e/o i bordi che definiscono la misurazione. La geometria può essere selezionata nella [Vista 3D](3D_view/it.md) (prime due opzioni) o nel disegno (tutte le opzioni):
    -   Selezionare due punti.
    -   Selezionare un singolo bordo dritto.
    -   Selezionare due bordi. Se entrambi i bordi sono diritti devono essere paralleli. Ciò produrrà una quotatura perpendicolare se un punto finale di uno dei bordi ha una proiezione perpendicolare sull\'altro bordo (il punto risultante deve trovarsi sul bordo effettivo). Se sono possibili più soluzioni, viene utilizzato il punto finale più vicino al punto proiettato. Se non esiste una proiezione perpendicolare valida, la quotatura sarà la distanza tra i punti finali più vicini dei bordi.
    -   Selezionare un punto e un bordo. Ciò produrrà una quotatura perpendicolare. In {{VersionMinus/it|0.21}} la quotatura sarà perpendicolare solo se il punto ha una proiezione perpendicolare sul bordo effettivo. Altrimenti la quotatura sarà la distanza tra il punto e il punto finale più vicino del bordo.
2.  Se si ha selezionato la geometria nella vista 3D: aggiungere la vista TechDraw corretta alla selezione selezionandola nella [Vista ad albero](Tree_view/it.md).
3.  Esistono diversi modi per richiamare lo strumento:
    -   
        {{Version/it|1.0}}
        
        : Se la [preferenza](TechDraw_Preferences/it#Dimensions.md) degli **Strumenti di quotatura** è impostata su {{Value|Strumento singolo}} (predefinito): premere la freccia giù a destra del pulsante **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** e selezionare il pulsante **[[Image:TechDraw_LengthDimension.svg|16px] ] Inserisci Quota Allineata** dal menu a discesa.

    -   Se questa preferenza ha un valore diverso (e in {{VersionMinus/it|0.21}}): premere il pulsante **<img src="images/TechDraw_LengthDimension.svg" width=16px> [Inserisci Quota Allineata](TechDraw_LengthDimension/it.md)** .

    -   Selezionare l\'opzione **TechDraw → Quotatura → <img src="images/TechDraw_LengthDimension.svg" width=16px> Inserisci Quota Allineata** dal menu.
4.  Una quota viene aggiunta alla vista.
5.  La quota può essere trascinata nella posizione desiderata.
6.  Se necessario, aggiungere tolleranze come descritto in [questa pagina](TechDraw_Geometric_dimensioning_and_tolerancing/it#Tolleranze.md).



### Visualizzazione quotatura 3D 

La quota mostrerà inizialmente la misura prevista (cioè come mostrato nel disegno). Se necessario, e se la quota è basata su riferimenti 3D, può essere convertita nella misurazione 3D effettiva modificando la proprietà **Measure Type** in {{Value|True}}. Per basare una quota su riferimenti 3D, selezionare la geometria dalla [vista 3D](3D_view/it.md) al momento della creazione oppure utilizzare lo strumento <img alt="" src=images/TechDraw_DimensionRepair.svg  style="width:16px;"> [TechDraw Ripara quota](TechDraw_DimensionRepair/it.md) per aggiornare le quote esistenti.



### Cambiare le proprietà 

Per modificare le proprietà di un oggetto quota fare doppio clic su di esso nel disegno o nella [Vista ad albero](Tree_view/it.md). Si aprirà la [Finestra di dialogo Quota](#Finestra_di_dialogo_Quota.md).



## Finestra di dialogo Quota 

![](images/TechDraw_DimensionDialog.png )

La finestra di dialogo della quotatura offre le seguenti impostazioni:



### Tolleranza

-   **Teoricamente esatta**: Se selezionato, la quota viene specificata come teoricamente esatta. In quanto tale, non dovrà avere alcuna tolleranza. La quota verrà visualizzata con una cornice attorno al valore: <img alt="" src=images/TechDraw_theoretically_exact.png  style="width:100px;">

-   **Tolleranza simmetrica**: Se selezionato, lo scostamento superiore e lo scostamento inferiore sono uguali e il valore negativo dello scostamento superiore viene utilizzato come scostamento inferiore. La visualizzazione sarà <img alt="" src=images/TechDraw_equal-tolerance.png  style="width:100px;">, altrimenti sarà <img alt="" src=images/TechDraw_Non-equal-tolerance.png  style="width:80px;">.

-   **Scostamento superiore**: Di quanto la dimensione può essere più grande.

-   **Scostamento inferiore**: Di quanto la dimensione può essere più piccola.



### Formattazione

-   **Specificatore di formato**: come verrà formattato il valore della quota. Per impostazione predefinita lo specificatore è {{Value|%.xf}} dove {{Value|x}} è il numero di decimali. Per la sintassi della formattazione vedere [questa pagina di Wikipedia](https://en.wikipedia.org/wiki/Printf_format_string). Esiste anche un formato aggiuntivo {{Value|%w}} che stampa il numero specificato di cifre dopo il separatore decimale e rimuove gli zeri finali. Ad esempio, {{Value|%.2w}} significa che verranno stampati al massimo 2 decimali e gli eventuali zeri finali verranno troncati.

-   **Testo arbitrario**: se selezionato, il valore della quota viene sostituito dal contenuto del campo **Specificatore di formato**.

-   **Specificatore formato Scostamento superiore**: come verrà formattato il valore dello scostamento superiore. Per impostazione predefinita lo specificatore è {{Value|%.xf}} dove {{Value|x}} è il numero di decimali. Per la sintassi della formattazione vedere [questa pagina di Wikipedia](https://en.wikipedia.org/wiki/Printf_format_string).

-   **Specificatore formato Scostamento inferiore**: come verrà formattato il valore dello scostamento inferiore. Per impostazione predefinita lo specificatore è {{Value|%.xf}} dove {{Value|x}} è il numero di decimali. Per la sintassi della formattazione vedere [questa pagina di Wikipedia](https://en.wikipedia.org/wiki/Printf_format_string).

-   **Testo tolleranza arbitraria**: Se selezionato, gli scostamenti vengono sostituiti dal contenuto dei campi **Specificatore formato Scostamento superiore** **Specificatore formato Scostamento inferiore**.



### Stile di Visualizzazione 

-   **Capovolgi le punte delle frecce**: Inverte la direzione delle frecce della linea di misura. Per impostazione predefinita si trovano all\'interno della linea/arco di misura e puntano verso l\'esterno.

-   **Colore**: Il colore delle linee e del testo.

-   **Dimensione del carattere**: la dimensione del testo della quota.

-   **Stile di disegno**: Lo standard (e il suo stile) secondo il quale viene disegnata la quota. Vedere la proprietà [**Standard e Stile**](#Vista.md) per i dettagli.



### Linee

-   **Sovrascrivi angoli**: Se selezionato, gli angoli usuali per la linea di misura e le linee di riferimento verranno sovrascritti dai valori specificati.

-   **Angolo della linea di misura**: Sovrascrive il valore dell\'angolo tra linea di misura e l\'asse X della vista (in gradi).

-   **Usa predefinito**: imposta l\'angolo della linea di misura sull\'angolo usuale.

-   **Usa selezione**: imposta l\'angolo della linea di misura in modo che corrisponda all\'angolo del bordo selezionato (o 2 vertici) nella vista.

-   **Angolo linea di riferimento**: Sovrascrive il valore dell\'angolo tra le linee di riferimento e l\'asse X della vista (in gradi).

-   **Usa predefinito**: imposta l\'angolo della linea di riferimento sull\'angolo usuale.

-   **Usa selezione**: imposta l\'angolo della linea di riferimento in modo che corrisponda all\'angolo del bordo selezionato (o 2 vertici) nella vista.



## Limitazioni

Gli oggetti dimensione sono vulnerabili ai problemi di \"[denominazione topologica](Topological_naming_problem/it.md)\". Ciò significa che se si modifica la geometria 3D, le facce e i bordi del modello possono essere rinominati internamente. Se una quota è collegata a un bordo che viene poi modificato, la dimensione potrebbe interrompersi. In generale, non è possibile mantenere sincronizzate le dimensioni 2D proiettate con gli oggetti 3D reali.

Pertanto, si consiglia di aggiungere le dimensioni verso la fine del processo di creazione del modello, quando il modello non viene più modificato.



### Soluzione

Se si desidera mantenere una vista di TechDraw con dimensioni che non si interrompono, è necessario dimensionare un oggetto che non cambierà piùː

-   Creare una copia non parametrica dell\'oggetto che si desidera proiettare con [Part Copia Semplice](Part_SimpleCopy/it.md).
-   Selezionare questa copia, quindi usare [vista](TechDraw_View/it.md), e aggiungere le dimensioni desiderate.
-   Se il modello 3D originale viene modificato, le modifiche non avranno effetto sulla copia semplice, né sulle dimensioni nella vista di TechDraw.

Vedere [Quota da punti di riferimento](TechDraw_LandmarkDimension/it.md) per un altro approccio per aggirare il problema della denominazione topologica.



## Note

-   **Selezione dei bordi**. I bordi possono essere difficili da selezionare. Si può regolare l\'area di selezione per i bordi modificando la [Preferenza Edge Fuzz](TechDraw_Preferences/it#Avanzate.md).
-   **Numero di decimali**. Le dimensioni utilizzano l\'impostazione delle posizioni decimali globali per impostazione predefinita. Questo può essere modificato tramite le [preferenze](TechDraw_Preferences/it#Dimensioni.md) o modificando la proprietà FormatSpec.
-   **Qualsiasi oggetto**. Le viste possono contenere più oggetti 3D come Sorgente. Le quote possono essere applicate alla geometria da qualsiasi oggetto nella vista (ad es. Da Object1.Vertex0 a Object2.Vertex3).



## Proprietà



### Dati


{{Properties_Title|Base}}

-    **References 2D|LinkSubList**: gli oggetti vista del disegno 2D su cui si basa la misurazione. Utilizzato se **Measure Type** è {{Value|Projected}}.

-    **References 3D|LinkSubList**: gli oggetti 3D su cui si basa la misurazione. Utilizzato se **Measure Type** è {{Value|True}}.

-    **Type|Enumeration**: lunghezza, raggio, diametro, ecc. Normalmente non manipolato dall\'utente finale.

-    **Measure Type|Enumeration**: come viene eseguita la misurazione.

:   

    :   Vero - basata sulla geometria 3D.
    :   Proiettato - basata sulla geometria 2D della Vista del disegno.

-    **Theoretical Exact|Bool**: specifica una quota teoricamente esatta (o di base).

:   

    :   
        `False`
        
        \- una quota comune per impostazione predefinita, possibilmente con tolleranze.

    :   
        `True`
        
        \- un valore teorico. Come tale non è soggetta ad alcuna tolleranza. La quota verrà visualizzata da una cornice attorno al valore: <img alt="" src=images/TechDraw_theoretically_exact.png  style="width:100px;">

-    **Equal Tolerance|Bool**: se lo Scostamento superiore ed inferiore sono uguali. Quindi il valore negativo dello Scostamento superiore viene utilizzato come Scostamento inferiore.

:   

    :   
        `True`
        
        \- il valore negato di **Over Tolerance** viene utilizzato come **Under Tolerance**. La visualizzazione sarà <img alt="" src=images/TechDraw_equal-tolerance.png  style="width:100px;">

    :   
        `False`
        
        \- viene preso in considerazione **Under Tolerance**. La visualizzazione sarà <img alt="" src=images/TechDraw_Non-equal-tolerance.png  style="width:80px;">

-    **Over Tolerance|QuantityConstraint**: l\'importo in base al quale la dimensione può essere più grande.

-    **Under Tolerance|QuantityConstraint**: la quantità di cui la dimensione può essere più piccola.

-    **Inverted|Bool**: indica se la quota rappresenta un valore normale o invertito.

:   

    :   
        `False`
        
        \- viene utilizzato il valore ordinario. Per la lunghezza è un numero positivo, per l\'angolo il valore obliquo (0° - 180°).

    :   
        `True`
        
        \- viene utilizzato il valore invertito. Per la lunghezza un numero negativo, per l\'angolo il valore del riflesso (180° - 360°).

-    **X|Distance**: posizione orizzontale del testo della quota rispetto alla vista.

-    **Y|Distance**: posizione verticale del testo della quota rispetto alla vista.

-    **Lock Position|Bool|Hidden**: blocca la posizione del testo della quota quando `True`.

-    **Rotation|Angolo|Hidden**: sola lettura.

-    **Scale Type|Enumeration|Hidden**: sola lettura.

-    **Scale|FloatConstant|Hidden**: sola lettura.

-    **Caption|String|Hidden**: non utilizzato.


{{Properties_Title|Format}}

-    **Format Spec|String**: come verrà formattato il valore della quota. Vedere [Formattazione](#Formattazione.md).

-    **Format Spec Over Tolerance|String**: come **Format Spec**, ma per Scostamenti superiori.

-    **Format Spec Under Tolerance|String**: come **Format Spec**, ma per Scostamenti inferiori.

-    **Arbitrary|Bool**: indica se la quota viene sostituita dal contenuto del campo **Format Spec**.

:   

    :   
        `False`
        
        \- il contenuto di **Format Spec** viene utilizzato per formattare il valore dimensionale effettivo.

    :   
        `True`
        
        \- il contenuto della **Format Spec** verrà visualizzato come testo invece del valore della quota.

-    **Arbitrary Tolerances|Bool**: come **Arbitrary**, ma per la tolleranza.


{{Properties_Title|Override}}

-    **Angle Override|Bool**: indica se la direzione delle linee di misura e di riferimento viene sovrascritta.

:   

    :   
        `False`
        
        \- le direzioni vengono calcolate come al solito.

    :   
        `True`
        
        \- le direzioni vengono sovrascritte dai valori delle proprietà LineAngle e ExtensionAngle.

-    **Line Angle|Angle**: angolo della linea di misura con l\'asse X della vista (in gradi).

-    **Extension Angle|Angle**: angolo delle linee di riferimento con l\'asse X della vista (in gradi).


{{Properties_Title|References}}

-    **Saved Geometry|TopoShapeList|Hidden**: geometria di riferimento. {{Version/it|0.21}}



### Vista


{{TitleProperty|Base}}

-    **Keep Label|Bool**: non utilizzato.

-    **Stack Order|Integer**: sovrapposto o sovrapposto rispetto ad altri oggetti di disegno. {{Version/it|0.21}}


{{Properties_Title|Dimension Format}}

-    **Arrowsize|Length**: la dimensione delle frecce di quotatura. {{Version/it|0.21}}

-    **Color|Color**: colore per linee e testo.

-    **Flip Arrowheads|Bool**: per impostazione predefinita il valore *dentro* la linea/arco di quota indica che le frecce puntano *verso l\'esterno*. Se posizionate *all\'esterno* della linea/arco di quota, le frecce puntano *verso l\'interno* della linea/arco di quota.

:   

    :   
        `False`
        
        \- Lascia che la direzione delle frecce venga selezionata automaticamente in base alla regola sopra.

    :   
        `True`
        
        \- Ignora la direzione scelta automaticamente e forza quella opposta.

-    **Font|Font**: il nome del carattere da utilizzare per il testo della quota.

-    **Fontsize|Length**: dimensione del testo della quota.

-    **Gap Factor ASME|Float**: regola la distanza tra i punti di quota e l\'inizio delle linee di riferimento. Lo spazio è questo valore moltiplicato per la larghezza della linea. {{Version/it|0.21}}

-    **Gap Factor ISO|Float**: regola lo spazio tra i punti di quota e l\'inizio delle linee di riferimento. Lo spazio è questo valore moltiplicato per la larghezza della linea. {{Version/it|0.21}}

-    **Line Spacing Factor|Float**: regola lo spazio tra il testo della quota e la linea di misura. Lo spazio è questo valore moltiplicato per la larghezza della linea. {{Version/it|0.21}}

-    **Line Width|Lenght**: spessore della linea di misura.

-    **Rendering Extent|Enumeration**: proprietà piuttosto universale che specifica quanto spazio può occupare il disegno della quota:

:   

    :   Nessuno - non vengono disegnate linee o frecce, viene visualizzato solo il semplice valore della quota.
    :   Minimo - per lunghezze e angoli viene disegnata una direttrice che collega il valore dimensionale e la *linea di riferimento virtuale* del punto finale. La linea di riferimento stessa non viene aggiunta.
    :   I diametri vengono renderizzati seguendo l\'estensione Confinata, i raggi seguendo l\'estensione Ridotta.
    :   Confinato - per lunghezze e angoli viene disegnata una linea doppia (o arco) che collega le *linee di riferimento virtuali* del punto iniziale e finale, sebbene le linee di riferimento stesse non vengano aggiunte.
    :   I diametri vengono disegnati con una direttrice dal valore dimensionale al punto più vicino sul cerchio, i raggi come con l\'estensione Ridotta.
    :   Ridotto - per lunghezze e angoli viene tracciata una linea a singola intestazione che collega il valore dimensionale e la *linea di riferimento* del punto finale insieme alla linea di riferimento stessa.
    :   I diametri sono disegnati con una direttrice dal centro al punto più vicino sul cerchio, i raggi con una direttrice dal valore dimensionale al punto dell\'arco più vicino.
    :   Normale - il valore predefinito. Per lunghezze e angoli viene disegnata una linea doppia (o arco) che collega le \"linee di riferimento\" del punto iniziale e finale, così come le linee di riferimento stesse.
    :   I diametri sono disegnati come linee doppie che colpiscono il centro e collegano i punti più vicini e più lontani sul cerchio.
    :   I raggi vengono disegnati come una direttrice dal centro al punto dell\'arco più vicino.
    :   Expanded - Solo i diametri supportano questo valore, visualizzandoli in modo simile alla lunghezza orizzontale o verticale. Gli altri tipi di quota vengono visualizzati come con l\'estensione Normale.

-    **Standard And Style|Enumeration**: specifica lo standard (e il relativo stile) in base al quale viene disegnata la quota:

:   

    :   <img alt="Differenze tra gli standard supportati" src=images/TechDraw_Dimension_standardization.png  style="width:500px;">

    :   Orientato ISO - disegnato secondo lo standard ISO 129-1, il testo viene ruotato per essere parallelo alla tangente della linea di misura.

    :   Riferimenti ISO - disegnato in conformità alla norma ISO 129-1, il testo è sempre orizzontale, sopra la linea di estensione più breve possibile.

    :   ASME Inline - disegnato secondo lo standard ASME Y14.5M, il testo è orizzontale, inserito in un\'interruzione all\'interno della linea o dell\'arco di misura.

    :   Riferimenti ASME - disegnato in conformità con ASME Y14.5M, il testo è orizzontale, la breve linea di estensione è attaccata al centro verticale di un lato.



## Script


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Quota allineata può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


```python
dim1 = FreeCAD.ActiveDocument.addObject("TechDraw::DrawViewDimension", "Dimension")
dim1.Type = "Distance"
dim1.References2D=[(view1, "Edge1")]
page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LengthDimension/it
