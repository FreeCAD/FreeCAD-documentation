---
- GuiCommand:/it
   Name:Draft Text
   Name/it:Testo
   MenuLocation:Drafting → Testo
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut:**T** **E**
   Version:0.7
   SeeAlso:[Etichetta](Draft_Label/it.md), [Forma da testo](Draft_ShapeString/it.md)
---

# Draft Text/it



## Descrizione

Il comando <img alt="" src=images/Draft_Text.svg  style="width:24px;"> **Testo** crea un testo su più righe in un dato punto.

Per creare un elemento di testo con una freccia usare invece il comando [Etichetta](Draft_Label/it.md).

<img alt="" src=images/Draft_Text_example.png  style="width:400px;"> 
*Singolo punto richiesto per posizionare il testo*



## Utilizzo

Vedi anche: [Barra di Draft](Draft_Tray/it.md) e [Aggancio](Draft_Snap/it.md).

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Text.svg" width=16px> [Testo](Draft_Text/it.md)**.
    -   Selezionare l\'opzione **Annotazione → <img src="images/Draft_Text.svg" width=16px> Testo** dal menu.
    -   Usare la scorciatoia da tastiera: **T** poi **E**.
2.  Si apre il pannello delle attività **Text**. Vedere [Opzioni](#Options.md) per maggiori informazioni.
3.  Scegliere un punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
4.  Inserire il testo desiderato, premere **Enter** per iniziare una nuova riga.
5.  Premere **Enter** due volte o premere il pulsante **<img src="images/Button_valid.svg" width=16px> Crea testo** per terminare il comando.



## Opzioni

Le scorciatoie da tastiera a carattere singolo disponibili nel pannello delle attività possono essere modificate. Vedere [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md). Le scorciatoie menzionate qui sono le scorciatoie predefinite.

-   Per inserire manualmente le coordinate, inserire le componenti X, Y e Z e premere **Enter** dopo ognuna di esse. Oppure si può premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando ha i valori desiderati. Si consiglia di spostare il puntatore fuori dalla [Vista 3D](3D_view/it.md) prima di inserire le coordinate.
-   Premere **G** o fare clic sulla casella di controllo **Globale** per attivare o disattivare la modalità globale. Se la modalità globale è attiva, le coordinate sono relative al sistema di coordinate globale, altrimenti sono relative al sistema di coordinate [piano di lavoro](Draft_SelectPlane/it.md). {{Version/it|0.20}}
-   Premere **T** o fare clic sulla casella di controllo **Continua** per attivare o disattivare la modalità continua. Se la modalità continua è attiva, il comando si riavvierà al termine, consentendo di continuare a creare testi. Il collegamento non funziona nel secondo pannello delle attività. Questa opzione non è disponibile nel primo pannello delle attività in FreeCAD versione 0.19 e precedenti.
-   Premere **S** per attivare o disattivare [Aggancia](Draft_Snap/it.md).
-   Premere **Esc** o il pulsante **Chiudi** per interrompere il comando.



## Note

-   Un Testo può essere modificato facendo doppio clic su di esso nella [Vista albero](Tree_view/it.md). {{Version/it|0.20}}
-   I Testi creati o salvati con [FreeCAD versione 1.0](Release_notes_1.0/it.md) non sono compatibili con le versioni precedenti.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Draft Testo deriva da un oggetto [App FeaturePython](App_FeaturePython/it.md) e ne eredita tutte le proprietà. Le seguenti proprietà sono aggiuntive se non diversamente specificato.



### Dati


{{TitleProperty|Base}}

-    **Placement|Placement**: specifica la posizione del testo nella [Vista 3D](3D_view/it.md). Vedere [Posizionamento](Placement/it.md).

-    **Text|StringList**: specifica il contenuto del testo. Ciascun elemento nell\'elenco rappresenta una nuova riga di testo.



### Vista


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifica lo stile di annotazione applicato al testo. Vedere [Stile delle annotazioni](Draft_AnnotationStyleEditor/it.md).

-    **Scale Multiplier|Float**: specifica il fattore di scala generale applicato al testo.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifica come viene visualizzato il testo. Se è {{value|World}} il testo verrà visualizzato su un piano definito dal suo **Placement**. Se è {{value|Screen}} il testo sarà sempre rivolto verso lo schermo. Questa è una proprietà ereditata. Le opzioni menzionate sono le opzioni rinominate ({{Version/it|1.0}}).


{{TitleProperty|Graphics}}

-    **Line Color|Color**: not used.

-    **Line Width|Float**: not used.


{{TitleProperty|Text}}

-    **Font Name|Font**: specifica il font utilizzato per disegnare il testo. Può essere un nome di font, come {{value|Arial}}, uno stile predefinito come {{value|sans}}, {{value|serif}} o {{value|mono}}, una famiglia come {{value|Arial,Helvetica,sans}}, o un nome con uno stile come {{value|Arial:Bold}}. Se il carattere specificato non viene trovato nel sistema, viene utilizzato un carattere predefinito.

-    **Font Size|Length**: specifica la dimensione delle lettere. Il testo può essere invisibile nella [Vista 3D](3D_view/it.md) se questo valore è molto piccolo.

-    **Justification|Enumeration**: specifica se l\'allineamento del testo: {{value|Left}}, {{value|Center}} o {{value|Right}}.

-    **Line Spacing|Float**: specifica il fattore applicato all\'altezza di riga predefinita del testo.

-    **Text Color|Color**: specifica il colore del testo.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare un Draft Testo usare il metodo `make_text` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makeText`.


```python
text = make_text(string, placement=None, screen=False)
```

-   Crea un oggetto `text`, in `placement`, che può essere un `FreeCAD.Placement`, ma anche un `FreeCAD.Rotation` o un { {incode\|FreeCAD.Vector}}.

-    `stringa`è una stringa o un elenco di stringhe. Se si tratta di un elenco, ogni elemento viene visualizzato su una propria riga.

-   Se `screen` è `True`, il testo è sempre rivolto verso la telecamera, altrimenti viene visualizzato in un piano definito dal suo **Placement**.

Le proprietà di visualizzazione di `text` possono essere cambiate sovrascrivendo i suoi attributi; per esempio, sovrascrivendo `ViewObject.FontSize` con le nuove dimensioni in millimetri.

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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Text/it
