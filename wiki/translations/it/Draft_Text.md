---
- GuiCommand:/it
   Name:Draft Text
   Name/it:Testo
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Testo
   Shortcut:**T** **E**
   SeeAlso:[Etichetta](Draft_Label/it.md), [Forma da testo](Draft_ShapeString/it.md)
   Version:0.7
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_Text.svg  style="width:16px;"> Testo inserisce una casella di testo su più righe in un determinato punto. Usa [il tipo di linea e il colore](Draft_Linestyle/it.md) impostati nella [barra di Draft](Draft_Tray/it.md).


</div>


<div class="mw-translate-fuzzy">

Per creare un\'etichetta di testo con una linea guida e una freccia usare [Etichetta](Draft_Label/it.md). Per creare testo solido o lettere 3D usare [Forma da testo](Draft_ShapeString/it.md) con [Estrusione](Part_Extrude/it.md) di Part.


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Text_example.png  style="width:400px;"> 
*Per posizionare una casella di testo basta un singolo punto*


</div>

## Utilizzo

See also: [Draft Tray](Draft_Tray.md) and [Draft Snap](Draft_Snap.md).


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_Text.svg" width=16px> [Testo](Draft_Text/it.md)**, o premere i tasti **T** e poi **E**.
2.  Selezionare un punto nella vista 3D, oppure digitare le sue [coordinate ](Draft_Coordinates/it.md) e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [Inserisci punto](Draft_AddPoint/it.md)**.
3.  Immettere il testo desiderato, premendo **Invio** tra ogni riga.
4.  Premere due volte **Invio** per completare l\'operazione.


</div>

## Opzioni

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** per ciascun componente X, Y e Z. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [Inserisci punto](Draft_AddPoint/it.md)** quando si hanno i valori desiderati per inserire il punto.
-   Tenere premuto **Ctrl** mentre si digita il testo per forzare [l\'aggancio](Draft_Snap.md) del proprio punto alla posizione di aggancio più vicina, indipendentemente dalla distanza.
-   Premere**Invio** o **↓ freccia in giù** per inserire una nuova riga di testo.
-   Premere **↑ freccia in su** per modificare la riga di testo precedente.
-   Premere due volte **Invio** o **↓ freccia in giù** per finire di editare il testo.
-   Premere il tasto **Esc** o il pulsante {{button|Chiudi}} per interrompere il comando corrente.


</div>

## Notes


<div class="mw-translate-fuzzy">

**Attenzione:** I testi creati con la [versione 0.18](Release_notes_0.18/it.md) non sono retrocompatibili, quindi eseguire il backup del proprio lavoro se si prova ad aprire con versioni precedenti i file creati con la 0.18.


</div>

## Proprietà

See also: [Property editor](Property_editor.md).

A Draft Text object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated.

### Data


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

### Dati

-    **Text**: specifica il contenuto del blocco di testo come un elenco di stringhe; ogni elemento dell\'elenco separato da una virgola indica una nuova riga.

-    **Position**: specifica il punto base della prima riga del blocco di testo.

-    **Angle**: specifica la rotazione della linea di base della prima riga del blocco di testo.

-    **Axis**: specifica l\'asse da utilizzare per la rotazione.


</div>

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the text. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the text.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|3D text}} the text will be displayed in a plane defined by its **Placement**. If it is {{value|2D text}} the text will always face the camera. This is an inherited property.


{{TitleProperty|Graphics}}

-    **Line Color|Color**: not used.

-    **Line Width|Float**: not used.


{{TitleProperty|Text}}


<div class="mw-translate-fuzzy">

### Vista

-    **Display Mode**: se è \"3D text\" il testo è allineato agli assi della scena, inizialmente situati sul piano XY; se è \"2D text\", il testo è sempre rivolto verso la fotocamera.

-    **Font Name**: specifica il carattere da utilizzare per disegnare il testo. Può essere il nome di un carattere, ad esempio \"Arial\", uno stile predefinito come \"sans\", \"serif\" o \"mono\", una famiglia come \"Arial,Helvetica,sans\" o un nome con uno stile come \"Arial:Bold\". Se nel sistema non trova il font specificato, ne utilizza uno generico.

-    **Font Size**: specifica la dimensione delle lettere. Se l\'oggetto testo viene creato nella vista ad albero ma non è visibile alcun testo, aumentare la dimensione del testo fino a renderlo visibile.

-    **Justification**: specifica se il testo è allineato a sinistra, a destra o al centro del punto base.

-    **Line Spacing**: specifica lo spazio tra le righe di testo.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Testo può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
text = make_text(string, placement=None, screen=False)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `Text`, nel `point` definito da un `FreeCAD.Vector`.

-    `stringlist`è una stringa o un elenco di stringhe; se si tratta di una lista, ogni elemento viene visualizzato nella sua propria riga.

-   Se `screen` è `True`, il testo è sempre rivolto verso la direzione della vista della telecamera, altrimenti si allinea con gli assi della scena e giace sul piano XY.


</div>


<div class="mw-translate-fuzzy">

Le proprietà di visualizzazione di `Text` possono essere cambiate sovrascrivendo i suoi attributi; per esempio, sovrascrivendo `ViewObject.FontSize` con le nuove dimensioni in millimetri.


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

t1 = "This is a sample text"
p1 = App.Vector(0, 0, 0)

t2 = ["First line", "second line"]
p2 = App.Vector(1000, 1000, 0)

text1 = Draft.make_text(t1, p1)
text2 = Draft.make_text(t2, p2)
text1.ViewObject.FontSize = 200
text2.ViewObject.FontSize = 200

zaxis = App.Vector(0, 0, 1)

t3 = ["Upside", "down"]
p3 = App.Vector(-1000, -500, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 180))
text3 = Draft.make_text(t3, place3)
text3.ViewObject.FontSize = 200

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
