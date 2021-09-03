---
- GuiCommand:/it
   Name:Draft Dimension
   Name/it:Quota
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Quota   Shortcut:**D** **I**
   SeeAlso:[Inverti la direzione delle quote](Draft_FlipDimension/it.md), [TechDraw](TechDraw_Workbench/it.md)
   Version:0.8
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [Quota](Draft_Dimension/it.md) crea un oggetto che misura e visualizza la distanza tra due punti; un terzo punto specifica la posizione della linea di quota.


</div>


<div class="mw-translate-fuzzy">

Lo strumento può misurare bordi o linee direttamente collegate a corpi solidi; se il corpo cambia, la dimensione si aggiorna automaticamente. Lo strumento può anche misurare un diametro o raggio di curvatura come quelli prodotti da [Arco](Draft_Arc/it.md), o dalle operazioni [Raccordo di Part](Part_Fillet/it.md), [Raccordo di Schizzo](Sketcher_CreateFillet/it.md) e [Raccordo di PartDesign](PartDesign_Fillet/it.md).


</div>


<div class="mw-translate-fuzzy">

La dimensione risultante viene posizionata nella vista 3D ed è considerata un oggetto Draft. Questo oggetto può essere visualizzato in una pagina di [TechDraw](TechDraw_Workbench/it.md) utilizzando gli strumenti [Vista Draft](TechDraw_NewDraft/it.md) o [Vista Arch](TechDraw_NewArch/it.md). In alternativa, TechDraw ha i propri strumenti per visualizzare le dimensioni, ad esempio [Lunghezza](TechDraw_Dimension_Length/it.md) e [Raggio](TechDraw_Dimension_Radius/it.md); però, questi strumenti sono pensati per preparare disegni tecnici, quindi creano le quote solo nella pagina di disegno e non nella vista 3D.


</div>

<img alt="" src=images/Screenshot_Draft_Dimension.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


*Dimensione definita da tre punti.*


</div>


<div class="mw-translate-fuzzy">

## Utilizzo


</div>

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

### Usage linear dimension 


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_Dimension.svg" width=16px> [Quota](Draft_Dimension/it.md)**, o premere i tasti **D** e poi **I**.
2.  Selezionare un primo punto nella vista 3D, oppure digitare le sue [coordinate ](Draft_Coordinates/it.md) e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [Inserisci punto](Draft_AddPoint/it.md)**.
3.  Selezionare un secondo punto nella vista 3D, oppure digitare le sue [coordinate ](Draft_Coordinates/it.md) e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [Inserisci punto](Draft_AddPoint/it.md)**. I primi due punti definiscono la distanza misurata.
4.  Selezionare un terzo punto nella vista 3D, oppure digitare le sue [coordinate ](Draft_Coordinates/it.md) e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [Inserisci punto](Draft_AddPoint/it.md)**. Il punto finale definisce la posizione della linea di misura.


</div>

### Usage radial dimension 

1.  Optionally select a circular edge in the [3D view](3D_view.md).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
3.  The **Dimension** task panel opens. See [Options](#Options.md) for more information.
4.  If you have not yet selected an edge do one of the following:
    -   Press **E** or the **<img src="images/view-select.svg" width=16px> select edge** button and select a circular edge in the [3D view](3D_view.md).
    -   Hold down the **Alt** key, select a circular edge in the [3D view](3D_view.md) and release the **Alt** key.
5.  To position the dimension line do one of the following:
    -   For a diameter dimension:
        -   Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
    -   For a radial dimension:
        -   Hold down the **Shift** key and pick a point in the [3D view](3D_view.md).

### Usage angular dimension 

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
2.  The **Dimension** task panel opens. See [Options](#Options.md) for more information.
3.  Hold down the **Alt** key, select two straight edges in the [3D view](3D_view.md) and release the **Alt** key.
4.  To position the dimension arc pick a point in the [3D view](3D_view.md).
5.  Depending on the edges and the picked point the displayed angle will be the acute (sharp) or obtuse (blunt) angle between the edges, or the angle of one of the edges with the horizontal. In some cases you may have to first add auxiliary geometry ([Draft Lines](Draft_Line.md) for example) to get a particular angle.


<div class="mw-translate-fuzzy">

## Opzioni


</div>

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Premere il tasto **X**, o **Y** o **Z** dopo un punto per vincolare il punto successivo su un dato asse.
-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** per ciascun componente X, Y e Z.. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [Inserisci punto](Draft_AddPoint/it.md)** quando si hanno i valori desiderati per inserire il punto.
-   Premere il tasto **R** oppure fare clic sulla casella di controllo per attivare la modalità \"relativo\". Se la modalità relativo è attiva, le coordinate del punto successivo sono relative all\'ultimo; in caso contrario, sono assolute, prese dall\'origine (0,0,0).
-   Premere il tasto **T** oppure fare clic sulla casella di controllo per attivare la modalità \"continua\". Se la modalità continua è attiva, lo strumento Quota si riavvia dopo aver terminato la quota in costruzione, e consente di disegnare una nuova quota senza premere nuovamente il pulsante dello strumento; le dimensioni successive iniziano dal punto finale della dimensione precedente e condividono la stessa linea base.
-   Tenere premuto **Ctrl** mentre si disegna per forzare [l\'aggancio](Draft_Snap.md) del proprio punto alla posizione di aggancio più vicina, indipendentemente dalla distanza.
-   Tenere premuto **Maiusc** mentre si disegna per [vincolare](Draft_Constrain.md) il prossimo punto in orizzontale o in verticale rispetto all\'ultimo, e per passare tra le modalità di diametro e raggio.
-   Premere il tasto **Esc** o il pulsante {{button|Chiudi}} per interrompere il comando corrente, e finire le dimensioni \"continue\"; le dimensioni già posizionate rimangono.


</div>

## Convert

### Usage

1.  Select one or more [Std MeasureDistance](Std_MeasureDistance.md) objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
3.  Each selected object is replaced by a non-parametric linear Draft Dimension.

## Notes


<div class="mw-translate-fuzzy">

La Dimensione può essere modificata facendo doppio clic sull\'elemento nella vista ad albero o premendo il pulsante **<img src="images/Draft_Edit.svg" width=16px> [Modifica](Draft_Edit/it.md)**. Quindi si può spostare i punti in una nuova posizione.


</div>

## Proprietà

See also: [Property editor](Property_editor.md).

A Draft Dimension object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated:

### Data linear and radial dimension 


{{TitleProperty|Dimension}}


<div class="mw-translate-fuzzy">

### Dati

-    **Start**: specifica il punto iniziale della distanza da misurare.

-    **End**: specifica il punto finale della distanza da misurare.

-    **Dimline**: specifica un punto attraverso il quale la linea di quota deve passare.

-    **Distance**: (sola lettura) indica la lunghezza misurata.

-    **Diameter**: se è `True` visualizza una dimensione diametro; altrimenti visualizza una dimensione raggio; questa proprietà funziona solo se la quota è collegata ad un arco circolare.


</div>


{{TitleProperty|Linear/radial dimension}}

-    **Direction|Vector**: specifies the direction of the measurement.

-    **Distance|Length**: (read-only) specifies the value of the measurement.

-    **End|VectorDistance**: specifies the end point of the measurement.

-    **Start|VectorDistance**: specifies the start point of the measurement.


{{TitleProperty|Radial dimension}}

-    **Diameter|Bool**: specifies if a radial dimension is displayed as a diameter dimension. If it changed the symbol used in **Override** must be updated manually (from {{Value|Ø}} to {{Value|R}} or vice versa). Not used for linear dimensions.

### Data angular dimension 


{{TitleProperty|Angular dimension}}

-    **Angle|Angle**: (read-only) specifies the value of the measurement.

-    **Center|VectorDistance**: specifies the center of the measurement.

-    **First Angle|Angle**: specifies the start angle of the measurement.

-    **Last Angle|Angle**: specifies the end angle of the measurement.


{{TitleProperty|Dimension}}

-    **Dimline|VectorDistance**: specifies the point through which the dimension arc passes.

-    **Linked Geometry|LinkSubList|hidden**: not used.

-    **Normal|Vector|hidden**: specifies the normal of the plane of the dimension.

-    **Support|Link|hidden**: not used.

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the dimension. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the dimension.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|2D text}} the text will be displayed in a plane defined by the **Normal** of the measurement. If it is {{value|3D text}} the text will always face the camera. Note that these values are switched compared to [Draft Texts](Draft_Text.md). This is an inherited property.


{{TitleProperty|Graphics}}


<div class="mw-translate-fuzzy">

### Vista

-    **Ext Lines**: specifica la lunghezza massima delle linee di estensione che vanno dai punti di misurazione alla linea di quota.

-    **Ext Overshoot**: specifica la lunghezza aggiuntiva delle linee di estensione oltre la linea di quota.

-    **Dim Overshoot**: specifica la lunghezza aggiuntiva aggiunta alla linea di quota.

-    **Arrow Size**: specifica la dimensione del simbolo visualizzato alle estremità della linea di quota.

-    **Arrow Type**: specifica il tipo di simbolo visualizzato alle estremità della linea di quota, che può essere \"Dot\", \"Circle\", \"Arrow\", o \"Tick\".

-    **Flip Arrows**: specifica se capovolgere l\'orientamento dei simboli alle estremità della linea di quota; funziona solo se i simboli sono frecce.

-    **Font Name**: specifica il carattere da utilizzare per disegnare il testo. Può essere il nome di un carattere, ad esempio \"Arial\", uno stile predefinito come \"sans\", \"serif\" o \"mono\", una famiglia come \"Arial,Helvetica,sans\" o un nome con uno stile come \"Arial:Bold\". Se nel sistema non trova il font specificato, ne utilizza uno generico.

-    **Font Size**: specifica la dimensione delle lettere. Se l\'oggetto testo viene creato nella vista ad albero ma non è visibile alcun testo, aumentare la dimensione del testo fino a renderlo visibile.

-    **Flip Text**: specifica se capovolgere l\'orientamento del testo che indica la misura.

-    **Text Position**: specifica la posizione del testo in coordinate assolute, riferito all\'origine (0,0,0); lasciare questa proprietà al valore predefinito (0,0,0) per visualizzare il testo accanto alla linea di quota.

-    **Text Spacing**: specifica lo spazio tra il testo e la linea di quota.

-    **Override**: specifica un testo personalizzato da visualizzare al posto della misura effettiva. Usare la stringa `$dim` all\'interno del testo per visualizzare il valore della misura.

-    **Decimals**: specifica il numero di posizioni decimali da visualizzare nella misura.

-    **Show Unit**: se è `True` l\'unità viene visualizzata accanto al valore numerico della misura.

-    **Unit Override**: specifica un\'unità in cui esprimere la misura, per esempio, \"km\", \"m\", \"cm\", \"mm\", \"mi\", \"ft\", \"in\"; lasciare vuota questa proprietà per utilizzare le unità predefinite. {{Version/it|0.17}}


</div>


{{TitleProperty|Text}}

-    **Flip Text|Bool**: specifies whether to flip the orientation of the text.

-    **Font Name|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead.

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small.

-    **Override|String**: specifies a custom text to display instead of the actual measurement. Use the string {{value|$dim}} inside the text to include the measurement.

-    **Text Position|VectorDistance**: specifies the position of the text in absolute coordinates. {{Value|[0, 0, 0]}} will display the text in its default position near the dimension line or arc.

-    **Text Spacing|Length**: specifies the space between the text and the dimension line or arc.


{{TitleProperty|Units}}

-    **Decimals|Integer**: specifies the number of decimal places to display for the measurement. Not used for angular dimensions.

-    **Show Unit|Bool**: specifies whether to display the unit next to the numerical value of the measurement. Not used for angular dimensions.

-    **Unit Override|String**: specifies the unit in which to express the measurement, for example, {{value|km}}, {{value|m}}, {{value|cm}}, {{value|mm}}, {{value|mi}}, {{value|ft}}, {{value|in}} or {{value|arch}} for arch units. Leave this blank to use the default unit. Not used for angular dimensions.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[API Draft](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Dimension può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
dimension = make_dimension(p1, p2, p3=None, p4=None)```


<div class="mw-translate-fuzzy">

Esistono vari modi per richiamare questa funzione, a seconda degli argomenti passati:


</div>


```python
dimension = make_dimension(p1, p2, p3=None)
dimension = make_dimension(object, i1, i2, p4=None)
dimension = make_dimension(object, i1, mode, p4=None)
```


<div class="mw-translate-fuzzy">

-   Crea una `Dimension` lineare misurando la distanza tra i punti `p1` e `p2`.
-   Crea una `Dimension` lineare collegata a un `object`, misurando la distanza tra i suoi vertici indicizzati `i1` e `i2`.
-   Crea una `Dimension` circolare collegata a un `object`, con l\'indice `i1` del bordo curvo da misurare, e `mode` che può essere un `"radius"` o un `"diameter"` per specificare il tipo di dimensione.
    -   
        `p3`
        
        nel primo caso, e `p4` negli altri due, specifica un punto facoltativo attraverso il quale deve passare la linea di quota.

    -   Tutti i punti sono definiti dai loro `FreeCAD.Vector`.


</div>


<div class="mw-translate-fuzzy">

Per creare una quota angolare utilizzare la seguente funzione:


</div>


```python
dimension = make_angular_dimension(center, angles, p3, normal=None)
dimension = make_angular_dimension(center, [angle1, angle2], p3, normal=None)
```


<div class="mw-translate-fuzzy">

-   Crea una `Dimension` angolare da un punto `center`, una lista `angles` con due elementi, e il punto `p3` attraverso il quale deve passare l\'arco.
    -   Se `angle1 > angle2`, l\'angolo visualizzato è la differenza `angle1 - angle2`; altrimenti, viene visualizzato l\'angolo di implementazione, `360 - (angle2 - angle1)`.
    -   Gli angoli dovrebbero essere dati in radianti; per convertire gli angoli espressi in gradi si può usare la funzione `math.radians()`.


</div>


<div class="mw-translate-fuzzy">

Le proprietà di visualizzazione di `Dimension` possono essere cambiate sovrascrivendo i suoi attributi; per esempio, sovrascrivendo `ViewObject.FontSize` con le nuove dimensioni in millimetri.


</div>

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


<div class="mw-translate-fuzzy">





</div>


 
