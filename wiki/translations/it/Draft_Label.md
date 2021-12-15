---
- GuiCommand:/it
   Name:Draft Label
   Name/it:Etichetta
   MenuLocation:Draft → Etichetta
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut:**D** **L**
   Version:0.17
   SeeAlso:[Testo](Draft_Text/it.md), [Forma da testo](Draft_ShapeString/it.md)
---

# Draft Label/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Etichetta inserisce una casella di testo su più righe con una linea guida a 2 segmenti e una freccia. Se si seleziona un oggetto o un sottoelemento (faccia, bordo o vertice) all\'avvio del comando, è possibile creare un\'etichetta per visualizzare un determinato attributo dell\'elemento selezionato, tra cui posizione, lunghezza, area, volume o materiale.


</div>

If an object or a sub-element (face, edge or vertex) is selected when starting the command, the text can be made to display one or two attributes of the selected element, including position, length, area, volume and material. The text will then be linked to the attributes and will update if their values change.


<div class="mw-translate-fuzzy">

Per inserire un elemento di testo più semplice senza una freccia usare [Testo](Draft_Text/it.md). Per creare forme di testo solido usare [Forma da testo](Draft_ShapeString/it.md) con [Estrusione](Part_Extrude/it.md).


</div>

<img alt="" src=images/Draft_Label_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Varie etichette con diversi orientamenti, simboli terminali e informazioni*


</div>

## Utilizzo

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_Label.svg" width=16px> [Etichetta](Draft_Label/it.md)**, o premere i tasti **D** e poi **L**.
2.  Selezionare un primo punto nella vista 3D, oppure digitare le sue coordinate e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Aggiungi punto**. Questo punto indica l\'obiettivo (punta della freccia) che può essere ovunque, non è necessario che sia un elemento.
3.  Fare clic su un secondo punto nella vista 3D o digitare una coordinata e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> aggiungi punto**. Questo punto indica l\'inizio di una linea guida orizzontale o verticale.
4.  Fare clic su un terzo punto nella vista 3D o digitare una coordinata e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> aggiungi punto**. Questo punto indica il punto base del testo.


</div>

## Opzioni

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Cliccare su **Label type** per selezionare il tipo di informazioni da visualizzare, incluso \"Custom\", \"Name\", \"Label\", \"Position\", \"Length\", \"Area\", \"Volume\", \"Tag\", e \"Material\". (Vedere le spiegazioni sotto, in [Tipi di etichette](Draft_Label/it#Tipi_di_etichette.md))
-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** per ciascun componente X, Y e Z. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando si hanno i valori desiderati per inserire il punto.
-   Tenere premuto **Ctrl** mentre si posiziona l\'etichetta per forzare lo [snap](Draft_Snap.md) al punto di aggancio più vicino, indipendentemente dalla distanza.
-   Premere il tasto **Esc** o il pulsante **Chiudi** per interrompere il comando corrente.


</div>

## Notes


<div class="mw-translate-fuzzy">


{{emphasis|Nota:}}

la direzione del segmento retto orizzontale, a destra o a sinistra, allinea automaticamente il testo nella direzione opposta. Se la linea guida sale verticalmente, il testo è allineato a sinistra; se scende verticalmente, è allineato a destra.


</div>

## Proprietà

See also: [Property editor](Property_editor.md).

A Draft Label object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated:

### Data


{{TitleProperty|Label}}


<div class="mw-translate-fuzzy">

### Dati

-    **Label Type**: specifica il tipo di informazioni mostrate da questa etichetta (vedere sotto).

-    **Custom Text**: specifica il blocco di testo da visualizzare quando **Label Type** è impostato su \"Custom\", o l\'etichetta non è parametrica. Il testo è dato come una lista di stringhe; ogni elemento dell\'elenco, separato da una virgola, indica una nuova riga di testo.

-    **Text**: (sola lettura) indica il testo effettivo visualizzato dall\'etichetta, secondo **Label Type**.

-    **Target Point**: specifica la posizione della punta della linea guida.

-    **Straight Direction**: specifica la direzione del segmento retto della linea guida, orizzontale o verticale.

-    **Straight Distance**: specifica la lunghezza del segmento retto della linea guida, partendo dal punto base del testo. Se la distanza è positiva, la linea guida inizia dal lato destro del testo e il testo si allinea a destra; altrimenti, la linea guida inizia dal lato sinistro del testo e il testo si allinea a sinistra.

-    **Position**: specifica il punto base della prima riga del blocco di testo; influenza anche come viene disegnata la linea guida.

-    **Angle**: specifica la rotazione della linea di base della prima riga del blocco di testo; influenza anche come viene disegnata la linea guida, poiché non è più orizzontale o verticale.

-    **Axis**: specifica l\'asse da utilizzare per la rotazione.


</div>


{{TitleProperty|Leader}}

-    **Points|VectorList**: specifies the points of the leader.

-    **Straight Direction|Enumeration**: specifies the direction of the first leader segment: {{Value|Custom}}, {{Value|Horizontal}} or {{Value|Vertical}}.

-    **Straight Distance|Distance**: specifies the length of the first leader segment. Only used if **Straight Direction** is {{Value|Horizontal}} or {{Value|Vertical}}. If the distance is positive, the leader starts from the right side of the text and the text aligns to the right. Otherwise the leader starts from the left side of the text and the text aligns to the left.


{{TitleProperty|Target}}

-    **Target|LinkSub**: specifies the object and optional subelement the label is linked to.

-    **Target Point|Vector**: specifies the position of the tip of the leader, which is where the arrow is attached.

#### Tipi di etichette 


<div class="mw-translate-fuzzy">

-    **Custom:**visualizza il contenuto di **Custom Text**.

-    **Name:**visualizza il nome interno dell\'oggetto destinatario; il nome interno viene assegnato all\'oggetto al momento della sua creazione e rimane fisso per tutta l\'esistenza dell\'oggetto.

-    **Label:**visualizza l\'etichetta dell\'oggetto destinatario; l\'etichetta dell\'oggetto può essere modificata dall\'utente in qualsiasi momento.

-    **Position:**visualizza le coordinate del punto base dell\'oggetto, del vertice o del centro di massa del sottoelemento destinatari, se applicabile.

-    **Length:**mostra la lunghezza del sottoelemento di destinazione, se possibile.

-    **Area:**mostra l\'area del sottoelemento di destinazione, se possibile.

-    **Volume:**mostra il volume dell\'oggetto di destinazione, se possibile.

-    **Tag:**mostra l\'attributo `Tag` dell\'oggetto di destinazione, se l\'oggetto di destinazione ha tale proprietà, come nel caso di tutti gli oggetti[Arch](Arch_Workbench/it.md).

-    **Material:**mostra l\'etichetta del materiale dell\'oggetto di destinazione, se l\'oggetto di destinazione ha tale proprietà.


</div>

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the label. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the label.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|3D text}} the text will be displayed in a plane defined by the **Placement** of the label. If it is {{value|2D text}} the text will always face the camera. This is an inherited property.


{{TitleProperty|Graphics}}


<div class="mw-translate-fuzzy">

### Vista

-    **Text Font**: specifica il carattere da utilizzare per disegnare il testo. Può essere il nome di un carattere, ad esempio \"Arial\", uno stile predefinito come \"sans\", \"serif\" o \"mono\", una famiglia come \"Arial,Helvetica,sans\" o un nome con uno stile come \"Arial:Bold\". Se nel sistema non trova il font specificato, ne utilizza uno generico.

-    **Text Size**: specifica la dimensione delle lettere. Se l\'oggetto testo viene creato nella vista ad albero ma non è visibile alcun testo, aumentare la dimensione del testo fino a renderlo visibile.

-    **Text Alignment**: specifica l\'allineamento verticale della linea di base del testo rispetto alla linea guida. Può essere in alto, in mezzo o in basso.

-    **Text Color**: specifica il colore del testo in una tupla RGB (R, G, B).

-    **Line Width**: specifica la larghezza della linea guida.

-    **Line Color**: specifica il colore della linea guida.

-    **Arrow Size**: specifica la dimensione del simbolo visualizzato alla fine della linea guida.

-    **Arrow Type**: specifica il tipo di simbolo visualizzato alla fine della linea guida, che può essere dot, circle, arrow, o tick.

-    **Frame**: se è \"Rectangle\" disegna una cornice attorno al testo.

-    **Line**: se è `True` visualizza la linea guida; altrimenti visualizza solo il testo e il simbolo finale.

-    **Display Mode**: se è \"3D text\" il testo è allineato agli assi della scena, inizialmente situati sul piano XY; se è \"2D text\", il testo è sempre rivolto verso la fotocamera.


</div>


{{TitleProperty|Text}}

-    **Justification|Enumeration**: specifies the horizontal alignment of the text: {{value|Left}}, {{value|Center}} or {{value|Right}}. Only used if **Straight Direction** is {{Value|Custom}}. Otherwise the horizontal alignment is based on the sign (positive or negative) of **Straight Distance**.

-    **Line Spacing|Float**: specifies the factor applied to the default line height of the text.

-    **Max Chars|Integer**: specifies the maximum number of characters on each line of the text.

-    **Text Alignment|Enumeration**: specifies the vertical alignment of the text: {{value|Top}}, {{value|Middle}} or {{value|Bottom}}.

-    **Text Color|Color**: specifies the color of the text.

-    **Text Font|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead.

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Etichetta può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
label = make_label(target_point=App.Vector(0, 0, 0),
                   placement=App.Vector(30, 30, 0),
                   target_object=None, subelements=None,
                   label_type="Custom", custom_text="Label",
                   direction="Horizontal", distance=-10,
                   points=None)
```

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(4000, 1000)
doc.recompute()

p1 = App.Vector(-200, 1000, 0)
place1 = App.Placement(App.Vector(-1000, 1300, 0), App.Rotation())

label1 = Draft.make_label(p1, place1, target_object=rectangle, distance=500, label_type="Label")
label1.ViewObject.TextSize = 200

p2 = App.Vector(-200, 0, 0)
place2 = App.Placement(App.Vector(-1000, -300, 0), App.Rotation())

label2 = Draft.make_label(p2, place2, target_object=rectangle, distance=500, label_type="Custom",
                          custom_text="Beware of the sharp edges")
label2.ViewObject.TextSize = 200

p3 = App.Vector(1000, 1200, 0)
place3 = App.Placement(App.Vector(2000, 1800, 0), App.Rotation())

label3 = Draft.make_label(p3, place3, target_object=rectangle, distance=-500, label_type="Area")
label3.ViewObject.TextSize = 200

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Label/it
