---
- GuiCommand:
   Name: Draft Label
   Name/it: Etichetta
   MenuLocation: Annotazione - Etichetta
   Workbenches: [Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut: **D** **L**
   Version: 0.17
   SeeAlso: [Testo](Draft_Text/it.md), [Forma da testo](Draft_ShapeString/it.md)
---

# Draft Label/it



## Descrizione

Il comando <img alt="" src=images/Draft_Label.svg  style="width:24px;"> **Etichetta** crea un testo su più righe con una linea guida a 2 segmenti e una freccia.

Se un oggetto o un sottoelemento (faccia, bordo o vertice) viene selezionato all\'avvio del comando, il testo può visualizzare uno o due attributi dell\'elemento selezionato, tra cui posizione, lunghezza, area, volume e materiale. Il testo sarà quindi collegato a detti attributi e si aggiornerà se i loro valori cambiano.

Per inserire un elemento di testo senza una freccia usare invece il comando [Testo](Draft_Text/it.md).

<img alt="" src=images/Draft_Label_example.jpg  style="width:400px;"> 
*Varie etichette con diversi orientamenti, frecce ed informazioni*



## Utilizzo

Vedere anche: [Barra di Draft](Draft_Tray/it.md), [Aggancio](Draft_Snap/it.md) e [Vincolare](Draft_Constrain/it.md).

1.  Facoltativamente selezionare un oggetto o un sottoelemento (vertice, bordo o faccia) di cui si desidera visualizzare gli attributi.
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Label.svg" width=16px> [Etichetta](Draft_Label/it.md)**.
    -   Selezionare l\'opzione **Annotazione → <img src="images/Draft_Label.svg" width=16px> Etichetta** dal menu.
    -   Usare la scorciatoia da tastiera: **D** poi **L**.
3.  Si apre il pannello attività **Etichetta**. Vedere [Opzioni](#Options.md) per maggiori informazioni.
4.  Se si ha selezionato un elemento: selezionare un\'opzione dall\'elenco a discesa **Tipo di etichetta**. Vedere [Tipi di etichette](#Tipi_di_etichette.md) di seguito.
5.  Scegliere il primo punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**. Questo punto indica il bersaglio (punta della freccia). Questo può essere ovunque, non deve essere su un elemento.
6.  Scegliere il secondo punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**. Questo punto indica l\'inizio del segmento orizzontale o verticale della direttrice.
7.  Scegliere il terzo punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**. Questo punto indica il punto base del testo.



## Opzioni

Le scorciatoie da tastiera a carattere singolo disponibili nel pannello delle attività possono essere modificate. Vedere [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md). Le scorciatoie menzionate qui sono le scorciatoie predefinite.

-   Per inserire manualmente le coordinate, inserire le componenti X, Y e Z e premere **Enter** dopo ognuna di esse. Oppure si può premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando si hanno i valori desiderati. Si consiglia di spostare il puntatore fuori dalla [Vista 3D](3D_view/it.md) prima di inserire le coordinate.
-   Premere **R** o fare clic sulla casella di controllo **Relativo** per attivare o disattivare la modalità relativa. Se la modalità relativa è attiva, le coordinate sono relative all\'ultimo punto, se disponibile, altrimenti sono relative all\'origine del sistema di coordinate.
-   Premere **G** o fare clic sulla casella di controllo **Globale** per attivare o disattivare la modalità globale. Se la modalità globale è attiva, le coordinate sono relative al sistema di coordinate globale, altrimenti sono relative al sistema di coordinate [piano di lavoro](Draft_SelectPlane/it.md). {{Version/it|0.20}}
-   Premere **S** per attivare o disattivare [Aggancia](Draft_Snap/it.md).
-   Premere **Esc** o il pulsante **Chiudi** per interrompere il comando.



## Tipi di etichette 

Sono disponibili i seguenti tipi di etichette:

-    {{Value|Custom}}: visualizza il contenuto di **Custom Text**.

-    {{Value|Name}}: visualizza il nome interno dell\'oggetto target. Il nome interno viene assegnato quando viene creato un oggetto e rimane fisso per tutta l\'esistenza dell\'oggetto.

-    {{Value|Label}}: visualizza l\'etichetta dell\'oggetto target. L\'etichetta di un oggetto può essere modificata dall\'utente.

-    {{Value|Position}}: visualizza le coordinate del punto base dell\'oggetto target, del vertice target o del centro di massa del sottoelemento target, se applicabile.

-    {{Value|Length}}: visualizza la lunghezza dell\'oggetto o del sottoelemento di destinazione, se applicabile.

-    {{Value|Area}}: visualizza l\'area dell\'oggetto o sottoelemento di destinazione, se applicabile.

-    {{Value|Volume}}: visualizza il volume dell\'oggetto target, se applicabile.

-    {{Value|Tag}}: visualizza l\'attributo `Tag` dell\'oggetto target, se applicabile. Gli oggetti creati con [Arch Workbench](Arch_Workbench.md) possono avere questo attributo.

-    {{Value|Material}}: visualizza l\'etichetta del materiale dell\'oggetto target, se applicabile.

-    {{Value|Label + Position}}
    

-    {{Value|Label + Length}}
    

-    {{Value|Label + Area}}
    

-    {{Value|Label + Volume}}
    

-    {{Value|Label + Material}}
    



## Note

-   La direzione del secondo segmento della direttrice determina l\'allineamento del testo. Se il segmento è orizzontale e punta a destra il testo è allineato a sinistra e viceversa. Se il secondo segmento va verticalmente verso l\'alto, il testo è allineato a sinistra. Se va verticalmente verso il basso, il testo è allineato a destra.
-   Le Etichette create o salvate con [FreeCAD versione 0.21](Release_notes_0.21/it.md) non sono compatibili con le versioni precedenti.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Draft Etichetta deriva da un oggetto [App FeaturePython](App_FeaturePython/it.md) e ne eredita tutte le proprietà. Le seguenti proprietà sono aggiuntive se non diversamente specificato.



### Dati


{{TitleProperty|Label}}

-    **Custom Text|StringList**: specifica il contenuto del testo se **Label Type** è {{Value|Custom}}. Ciascun elemento nell\'elenco rappresenta una nuova riga di testo.

-    **Label Type|Enumeration**: specifica il tipo di informazioni visualizzate dall\'etichetta. Vedi [Tipi di etichette](#Tipi_di_etichette.md).

-    **Placement|Placement**: specifica la posizione del testo nella [Vista 3D](3D_view/it.md) e, a meno che **Straight Direction** sia {{Value|Custom}}, anche di il primo segmento della direttrice, che è il segmento in cui è allegato il testo. Vedere [Posizionamento](Placement/it.md).

-    **Text|StringList**: (read-only) specifica il contenuto del testo che viene effettivamente visualizzato. Ciascun elemento nell\'elenco rappresenta una nuova riga di testo.


{{TitleProperty|Leader}}

-    **Points|VectorList**: specifica i punti della direttrice.

-    **Straight Direction|Enumeration**: specifica la direzione del primo segmento della direttrice: {{Value|Custom}}, {{Value|Horizontal}} o {{Value|Vertical}}.

-    **Straight Distance|Distance**: specifica la lunghezza del primo segmento della direttrice. Utilizzato solo se **Straight Direction** è {{Value|Horizontal}} o {{Value|Vertical}}. Se la distanza è positiva, la direttrice inizia dal lato destro del testo e il testo si allinea a destra. Altrimenti la direttrice inizia dal lato sinistro del testo e il testo si allinea a sinistra.


{{TitleProperty|Target}}

-    **Target|LinkSub**: specifica l\'oggetto e il sottoelemento facoltativo a cui è collegata l\'etichetta.

-    **Target Point|Vector**: specifica la posizione della punta della direttrice, ovvero dove è attaccata la freccia.



### Vista


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifica lo stile di annotazione applicato all\'etichetta. Vedere [Stile delle annotazioni](Draft_AnnotationStyleEditor/it.md).

-    **Scale Multiplier|Float**: specifica il fattore di scala generale applicato all\'etichetta.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifica come viene visualizzato il testo. Se è {{value|World}} il testo verrà visualizzato su un piano definito dal **Placement** dell\'etichetta. Se è {{value|Screen}} il testo sarà sempre rivolto verso lo schermo. Questa è una proprietà ereditata. Le opzioni menzionate sono le opzioni rinominate ({{Version/it|0.21}}).


{{TitleProperty|Graphics}}

-    **Arrow Size|Length**: specifica la dimensione del simbolo visualizzato sulla punta della direttrice.

-    **Arrow Type|Enumeration**: specifica il tipo di simbolo visualizzato sulla punta della direttrice, che può essere {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} o {{value|Tick-2}}.

-    **Frame|Enumeration**: specifica quale tipo di cornice viene disegnata attorno al testo. Le opzioni correnti sono {{value|None}} o {{value|Rectangle}}.

-    **Line|Bool**: specifica se visualizzare la linea guida. Se è `False` vengono visualizzati solo la freccia e il testo.

-    **Line Color|Color**: specifica il colore della direttrice e della freccia. Viene utilizzato anche per la cornice ({{Version/it|0.20}}).

-    **Line Width|Float**: specifica la larghezza della direttrice. Viene utilizzato anche per la cornice ({{Version/it|0.20}}).


{{TitleProperty|Text}}

-    **Font Name|Font**: specifica il font utilizzato per disegnare il testo. Può essere un nome di font, come {{value|Arial}}, uno stile predefinito come {{value|sans}}, {{value|serif}} o {{value|mono}}, una famiglia come {{value|Arial,Helvetica,sans}}, o un nome con uno stile come {{value|Arial:Bold}}. Se il carattere specificato non viene trovato nel sistema, viene utilizzato un carattere predefinito. {{Version/it|0.21}}

-    **Font Size|Length**: specifica la dimensione del carattere. Il testo può essere invisibile nella [Vista 3D](3D_view/it.md) se questo valore è molto piccolo. {{Version/it|0.21}}

-    **Justification|Enumeration**: specifica l\'allineamento orizzontale del testo: {{value|Left}}, {{value|Center}} o {{value|Right}}. Utilizzato solo se **Straight Direction** è {{Value|Custom}}. Altrimenti l\'allineamento orizzontale si basa sul segno (positivo o negativo) di **Straight Distance**.

-    **Interlinea|Float**: specifica il fattore applicato all\'altezza di riga predefinita del testo.

-    **Max Chars|Integer**: specifica il numero massimo di caratteri su ogni riga del testo.

-    **Text Alignment|Enumeration**: specifica l\'allineamento verticale del testo: {{value|Top}}, {{value|Middle}} o {{value|Bottom}}.

-    **Text Color|Color**: specifica il colore del testo.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare un\'Etichetta Draft usare il metodo `make_label` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makeLabel`.


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



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Label/it
