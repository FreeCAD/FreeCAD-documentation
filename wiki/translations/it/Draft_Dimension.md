---
- GuiCommand:
   Name: Draft Dimension
   Name/it: Quota
   MenuLocation: Draft -> Quota
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   Shortcut: **D** **I**
   Version: 0.8
   SeeAlso: Draft_FlipDimension/it
---

# Draft Dimension/it



## Descrizione

Il comando <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> **Quota** [crea](#Creazione.md) una [quota lineare](#Utilizzo_della_quota_lineare.md), una [quota radiale](#Usage_radial_dimension.md) o una [quota angolare](#Usage_angular_dimension.md). Il comando può essere utilizzato anche per [convertire](#Convert.md) oggetti [Misura distanza](Std_MeasureDistance/it.md).

Le quote lineari basate sui bordi e le quote radiali sono parametriche. Ciò significa che si aggiorneranno se il bordo misurato viene modificato. I bordi misurati possono appartenere a oggetti Draft ma anche a corpi solidi. Le quote angolari non sono parametriche.

Le Quote di Draft possono essere visualizzate su una pagina [TechDraw](TechDraw_Workbench/it.md) utilizzando i comandi [TechDraw DraftView](TechDraw_DraftView/it.md) o [TechDraw ArchView](TechDraw_ArchView/it.md). In alternativa, [TechDraw](TechDraw_Workbench/it.md) offre i propri comandi di quotatura. Ma questi creano quote che vengono visualizzate solo sulla pagina di disegno e non nella [Vista 3D](3D_view/it.md).

<img alt="" src=images/Screenshot_Draft_Dimension.jpg  style="width:400px;"> 
*Quota lineare definita da tre punti*



## Creazione

Vedere anche: [Barra di Draft](Draft_Tray/it.md), [Aggancio](Draft_Snap/it.md) e [Vincolare](Draft_Constrain/it.md).



### Utilizzo della quota lineare 

1.  Facoltativamente, selezionare un bordo dritto nella [Vista 3D](3D_view/it.md).
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Dimension.svg" width=16px> [Quota](Draft_Dimension/it.md)**.
    -   Selezionare l\'opzione **Annotazione → <img src="images/Draft_Dimension.svg" width=16px> Quota** dal menu.
    -   Usare la scorciatoia da tastiera: **D** poi **I**.
3.  Si apre il pannello attività **Quota**. Vedere [Opzioni](#Opzioni.md) per maggiori informazioni.
4.  Se non si ha ancora selezionato un bordo, eseguire una delle seguenti operazioni:
    -   Premere **E** o il pulsante **<img src="images/view-select.svg" width=16px> Seleziona bordo** e seleziona un bordo dritto nella [Vista 3D](3D_view/it.md).
    -   Tenere premuto il tasto **Alt**, selezionare un bordo dritto nella [Vista 3D](3D_view/it.md) e rilasciare il tasto **Alt**.
    -   Definire la distanza misurata selezionando i punti:
        -   Scegliere un primo punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
        -   Scegliere un secondo punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
5.  Per posizionare la linea di quota, eseguire una delle seguenti operazioni:
    -   Per una quota allineata:
        -   Scegliere un punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
    -   Per una quota orizzontale:
        -   Spostare il puntatore sopra o sotto il bordo o i punti.
        -   Tenere premuto il tasto **Shift**, muovere il puntatore e scegliere un punto nella [Vista 3D](3D_view/it.md).
    -   Per una quota verticale:
        -   Spostare il puntatore a sinistra o a destra del bordo o dei punti.
        -   Tenere premuto il tasto **Shift**, muovere il puntatore e scegliere un punto nella [Vista 3D](3D_view/it.md).



### Utilizzo della quota radiale 

1.  Facoltativamente, selezionare un bordo circolare nella [Vista 3D](3D_view/it.md).
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Dimension.svg" width=16px> [Quota](Draft_Dimension/it.md)**.
    -   Selezionare l\'opzione **Annotazione → <img src="images/Draft_Dimension.svg" width=16px> Quota** dal menu.
    -   Usare la scorciatoia da tastiera: **D** poi **I**.
3.  Si apre il pannello attività **Quota**. Vedere [Opzioni](#Opzioni.md) per maggiori informazioni.
4.  Se non si ha ancora selezionato un bordo, eseguire una delle seguenti operazioni:
    -   Premere **E** o il pulsante **<img src="images/view-select.svg" width=16px> Seleziona bordo** e selezionare un bordo circolare nella [Vista 3D](3D_view/it.md).
    -   Tenere premuto il tasto **Alt**, selezionare un bordo circolare nella [Vista 3D](3D_view/it.md) e rilasciare il tasto **Alt**.
5.  Per posizionare la linea di quota, eseguire una delle seguenti operazioni:
    -   Per quotare un diametro:
        -   Scegliere un punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
    -   Per quotare un raggio:
        -   Tenere premuto il tasto **Shift** e scegliere un punto nella [Vista 3D](3D_view/it.md).



### Utilizzo della quota angolare 

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Dimension.svg" width=16px> [Quota](Draft_Dimension/it.md)**.
    -   Selezionare l\'opzione **Annotazione → <img src="images/Draft_Dimension.svg" width=16px> Quota** dal menu.
    -   Usare la scorciatoia da tastiera: **D** poi **I**.
2.  Si apre il pannello attività **Quota**. Vedere [Opzioni](#Opzioni.md) per maggiori informazioni.
3.  Effettuare una delle seguenti operazioni:
    -   Premere **E** o il pulsante **<img src="images/view-select.svg" width=16px> Seleziona bordo** e selezionare un primo bordo dritto nella [Vista 3D](3D_view/it.md) . Ripetere l\'operazione per selezionare un secondo bordo dritto.
    -   Tenere premuto il tasto **Alt**, selezionare due bordi dritti nella [Vista 3D](3D_view/it.md) e rilasciare il tasto **Alt**.
4.  Per posizionare l\'arco di quota selezionare un punto nella [Vista 3D](3D_view/it.md).
5.  L\'angolo visualizzato dipende dai bordi e dal punto selezionato.



### Opzioni

Le scorciatoie da tastiera a carattere singolo disponibili nel pannello delle attività possono essere modificate. Vedere [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md). Le scorciatoie menzionate qui sono le scorciatoie predefinite.

-   Per inserire manualmente le coordinate, inserire le componenti X, Y e Z e premere **Enter** dopo ognuna di esse. Oppure si può premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando ha i valori desiderati. Si consiglia di spostare il puntatore fuori dalla [Vista 3D](3D_view/it.md) prima di inserire le coordinate.
-   Premee **R** o fare clic sulla casella di controllo **Relativo** per attivare o disattivare la modalità relativa. Se la modalità relativa è attiva, le coordinate sono relative all\'ultimo punto, se disponibile, altrimenti sono relative all\'origine del sistema di coordinate.
-   Premere **G** o fare clic sulla casella di controllo **Globale** per attivare o disattivare la modalità globale. Se la modalità globale è attiva, le coordinate sono relative al sistema di coordinate globale, altrimenti sono relative al sistema di coordinate [piano di lavoro](Draft_SelectPlane/it.md). {{Version/it|0.20}}
-   Premere **T** o fare clic sulla casella di controllo **Continua** per attivare o disattivare la modalità continua. Questa modalità funziona solo per quote lineari. Se la modalità continua è attiva, il comando si riavvierà al termine, consentendo di continuare a creare quote. Tutte le quote successive inizieranno dal punto finale della quota precedente e utilizzeranno la stessa linea di base della prima quota. Si noti che la selezione del bordo non è possibile per le quote successive.
-   Premee **S** per attivare o disattivare [Aggancia](Draft_Snap/it.md).
-   Premere **Esc** o il pulsante **Chiudi** per terminare il comando.



## Conversione



### Utilizzo

1.  Selezionare uno o più oggetti [Misura la distanza](Std_MeasureDistance/it.md).
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Dimension.svg" width=16px> [Quota](Draft_Dimension/it.md)**.
    -   Selezionare l\'opzione **Annotazione → <img src="images/Draft_Dimension.svg" width=16px> Quota** dal menu.
    -   Usare la scorciatoia da tastiera: **D** poi **I**.
3.  Ciascun oggetto selezionato viene sostituito da una Quota Draft lineare non parametrica.



## Note

-   Le Quote Draft lineari e radiali possono essere modificate con il comando [Modifica](Draft_Edit/it.md).
-   Le Quote Draft create o salvate con [FreeCAD versione 0.21](Release_notes_0.21/it.md) non sono compatibili con le versioni precedenti.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Draft Quota deriva da un oggetto [App FeaturePython](App_FeaturePython/it.md) e ne eredita tutte le proprietà. Le seguenti proprietà sono aggiuntive se non diversamente specificato.



### Dati quote lineari e radiali 


{{TitleProperty|Dimension}}

-    **Dimline|VectorDistance**: specifica il punto attraverso il quale passa la linea di quota.

-    **Linked Geometry|LinkSubList**: specifica l\'oggetto e i suoi sottoelementi a cui è collegata la quota.

-    **Normal|Vector**: specifica la normale del piano del testo.

-    **Support|Link|hidden**: specifica l\'oggetto misurato.


{{TitleProperty|Linear/radial dimension}}

-    **Direction|Vector**: specifica la direzione della misura.

-    **Distance|Length**: (sola lettura) specifica il valore della misura.

-    **End|VectorDistance**: specifica il punto finale della misura.

-    **Start|VectorDistance**: specifica il punto iniziale della misura.


{{TitleProperty|Radial dimension}}

-    **Diameter|Bool**: specifica se una quota radiale viene visualizzata come quota diametro. Se è cambiato il simbolo utilizzato in **Override** deve essere aggiornato manualmente (da {{Value|Ø}} a {{Value|R}} o viceversa). Non utilizzato per quote lineari.



### Dati quote angolari 


{{TitleProperty|Angular dimension}}

-    **Angle|Angle**: (sola lettura) specifica il valore della misura.

-    **Center|VectorDistance**: specifica il centro della misura.

-    **First Angle|Angle**: specifica l\'angolo iniziale della misurazione.

-    **Last Angle|Angle**: specifica l\'angolo finale della misura.


{{TitleProperty|Dimension}}

-    **Dimline|VectorDistance**: specifica il punto attraverso il quale passa l\'arco di quota.

-    **Linked Geometry|LinkSubList|hidden**: non utilizzato.

-    **Normal|Vector|hidden**: specifica la normale del piano della quota.

-    **Support|Link|hidden**: non utilizzato.



### Vista


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifica lo stile di annotazione applicato alla quota. Vedere [Stile delle annotazioni](Draft_AnnotationStyleEditor/it.md).

-    **Scale Multiplier|Float**: specifica il fattore di scala generale applicato alla quota.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifica come viene visualizzato il testo. Se è {{value|World}} il testo verrà visualizzato su un piano definito dal **Normal** della misura. Se è {{value|Screen}} il testo sarà sempre rivolto verso lo schermo. Questa è una proprietà ereditata. Le opzioni menzionate sono le opzioni rinominate ({{Version/it|0.21}}).


{{TitleProperty|Graphics}}

-    **Arrow Size|Length**: specifica la dimensione dei simboli visualizzati alle estremità della linea di quota o dell\'arco.

-    **Arrow Type|Enumeration**: specifica il tipo di simbolo visualizzato alle estremità della linea di quota o dell\'arco, che può essere {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} o {{value|Tick-2}}.

-    **Dim Overshoot|Distance**: specifica la lunghezza aggiuntiva aggiunta alla linea di quota. Non utilizzato per quote angolari.

-    **Ext Lines|Distance**: specifica la lunghezza delle linee di estensione che vanno dalla linea di quota ai punti misurati. Usare {{Value|0}} per linee di estensione complete. Un valore negativo definisce lo spazio tra le estremità delle linee di estensione e i punti misurati. Un valore positivo definisce la lunghezza massima delle linee di estensione. Utilizzato solo per quote lineari.

-    **Ext Overshoot|Distance**: specifica la lunghezza aggiuntiva delle linee di estensione oltre la linea di quota. Non utilizzato per quote angolari.

-    **Flip Arrows|Bool**: specifica se invertire l\'orientamento dei simboli alle estremità della linea di quota o dell\'arco. Funziona solo se i simboli sono frecce.

-    **Line Color|Color**: specifica il colore della linea o dell\'arco di quota e delle frecce.

-    **Line Width|Float**: specifica la larghezza delle linee o dell\'arco appartenenti alla quota.

-    **Show Line|Bool**: specifica se visualizzare la linea di quota. Non influisce sulla visualizzazione delle linee di estensione e degli overshoot. Non utilizzato per quote angolari.


{{TitleProperty|Text}}

-    **Flip Text|Bool**: specifica se invertire l\'orientamento del testo.

-    **Font Name|Font**: specifica il font utilizzato per disegnare il testo. Può essere un nome di font, come {{value|Arial}}, uno stile predefinito come {{value|sans}}, {{value|serif}} o {{value|mono}}, una famiglia come {{value|Arial,Helvetica,sans}}, o un nome con uno stile come {{value|Arial:Bold}}. Se il carattere specificato non viene trovato nel sistema, viene utilizzato un carattere predefinito.

-    **Font Size|Length**: specifica la dimensione del testo. Il testo può essere invisibile nella [Vista 3D](3D_view/it.md) se questo valore è molto piccolo.

-    **Override|String**: specifica un testo personalizzato da visualizzare al posto della misura effettiva. Usare la stringa {{value|$dim}} all\'interno del testo per includere la misura.

-    **Text Color|Color**: specifica il colore del testo. {{Version/it|0.21}}

-    **Text Position|VectorDistance**: specifica la posizione del testo in coordinate assolute. {{Value|[0, 0, 0]}} visualizzerà il testo nella sua posizione predefinita vicino alla linea di quota o all\'arco.

-    **Text Spacing|Length**: specifica lo spazio tra il testo e la linea o l\'arco di quota.


{{TitleProperty|Units}}

-    **Decimals|Integer**: specifica il numero di posizioni decimali da visualizzare per la misura.

-    **Show Unit|Bool**: specifica se visualizzare l\'unità accanto al valore numerico della misura. Non utilizzato per quote angolari.

-    **Unit Override|String**: specifica l\'unità in cui esprimere la misura, ad esempio {{value|km}}, {{value|m}}, {{value|cm}}, {{value|mm}}, {{value|mi}}, {{value|ft}}, {{value|in}} o {{value|arch}} per unità arco. Lasciare vuoto questo campo per utilizzare l\'unità predefinita. Non utilizzato per quote angolari.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare una Quota Draft utilizzare il metodo `make_dimension` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makeDimension`.


```python
dimension = make_dimension(p1, p2, p3=None, p4=None)```

Esistono vari modi per richiamare questo metodo, a seconda degli argomenti passati:


```python
dimension = make_dimension(p1, p2, p3=None)
dimension = make_dimension(object, i1, i2, p4=None)
dimension = make_dimension(object, i1, mode, p4=None)
```

-   Crea una `dimension` lineare misurando la distanza tra i punti `p1` e `p2`.
-   Crea una `dimension` lineare collegata a un `object`, misurando la distanza tra i suoi vertici indicizzati `i1` e `i2`.
-   Crea una `dimension` circolare collegata a un `object`, con l\'indice `i1` del bordo curvo da misurare, e `mode` che può essere un `"radius"` o un `"diameter"` per specificare il tipo di dimensione.
    -   
        `p3`
        
        nel primo caso, e `p4` negli altri due, specifica un punto facoltativo attraverso il quale deve passare la linea di quota.

    -   Tutti i punti sono definiti dai loro `FreeCAD.Vector`.

Per creare una quota angolare utilizzare il seguente metodo:


```python
dimension = make_angular_dimension(center, angles, p3, normal=None)
dimension = make_angular_dimension(center, [angle1, angle2], p3, normal=None)
```

-   Crea una `dimension` angolare da un punto `center`, una lista `angles` con due elementi, e il punto `p3` attraverso il quale deve passare l\'arco.
    -   Se `angle1 > angle2`, l\'angolo visualizzato è la differenza `angle1 - angle2`; altrimenti, viene visualizzato l\'angolo di implementazione, `360 - (angle2 - angle1)`.
    -   Gli angoli dovrebbero essere dati in gradi.

Le proprietà di visualizzazione di `dimension` possono essere cambiate sovrascrivendo i suoi attributi; per esempio, sovrascrivendo `ViewObject.FontSize` con le nuove dimensioni in millimetri.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(-2500, 0, 0)
dimension1 = Draft.make_dimension(p1, p2, p3)
dimension1.ViewObject.FontSize = 200

polygon = Draft.make_polygon(3, radius=1000)
doc.recompute()

p4 = App.Vector(-2000, 1500, 0)
dimension2 = Draft.make_dimension(polygon, 1, 2, p4)
dimension2.ViewObject.FontSize = 200

center = App.Vector(2000, 0, 0)
p5 = App.Vector(3000, 1000, 0)
angle1 = 45
angle2 = 10
dimension3 = Draft.make_angular_dimension(center, [angle1, angle2], p5)
dimension3.ViewObject.FontSize = 200

dimension4 = Draft.make_angular_dimension(center, [angle2, angle1], p5*1.2)
dimension4.ViewObject.FontSize = 200

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Dimension/it
