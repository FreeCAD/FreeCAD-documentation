---
- GuiCommand:/it
   Name:Draft_ShapeString
   Name/it:Forma da testo
   MenuLocation:Drafting → Forma da testo
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut:
   Version:0.14
   SeeAlso:[Testo](Draft_Text/it.md), [Etichetta](Draft_Label/it.md) [Estrusione](Part_Extrude/it.md)
---

# Draft ShapeString/it



## Descrizione

Il comando <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;"> **Forma da testo** crea una forma composta che rappresenta una stringa di testo. Questa forma può essere utilizzata per creare lettere 3D con il comando [Part Estrusione](Part_Extrude/it.md).

Il comando Forma da testo non è destinato alle annotazioni di testo standard. Il comando [Testo](Draft_Text/it.md) o il comando [Etichetta](Draft_Label/it.md) dovrebbe essere utilizzato a tale scopo.

![](images/Draft_ShapeString_Example400.png ) 
*Per posizionare una Forma da testo basta un singolo punto*



## Utilizzo

Per gli utenti Windows: leggere prima il paragrafo [Selezione file font su Windows](#Selezione_file_font_su_Windows.md).

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_ShapeString.svg" width=16px> [Forma da testo](Draft_ShapeString/it.md)**.
    -   Selezionare l\'opzione **Drafting → <img src="images/Draft_ShapeString.svg" width=16px> Forma da testo** dal menu.
2.  Si apre il pannello attività **Forma da testo**.
3.  Fare clic su un punto nella [Vista 3D](3D_view/it.md) o digitare le coordinate.
4.  Facoltativamente, premere il pulsante **Reimposta punto** per reimpostare il punto all\'origine.
5.  Inserire una **Stringa**.
6.  Specificare l\'**Altezza**.
7.  Per selezionare un carattere, eseguire una delle seguenti operazioni:
    -   Inserire un percorso file nella casella di input **Font file**.
    -   Premere il pulsante **...** e selezionare un file.
8.  Premere il pulsante **OK** per terminare il comando.



## Opzioni

-   Premer **Esc** o il pulsante **Annulla** per interrompere il comando.



## Note

-   Una Forma da testo può essere modificata facendo doppio clic su di essa nella [Vista ad albero](Tree_view/it.md). {{Version/it|0.20}}
-   I font supportati includono TrueType (**.ttf**), OpenType (**.otf**) e Type 1 (**.pfb**).
-   Il comando è limitato al testo LTR (da sinistra a destra). Pertanto al momento il testo RTL (da destra a sinistra + dall\'alto verso il basso) non è supportato.
-   Altezze del testo molto piccole possono causare forme dei caratteri deformate a causa della perdita di dettagli nel ridimensionamento.
-   Molti font genereranno geometrie problematiche. Questo perché i contorni dei caratteri possono sovrapporsi, avere piccoli spazi e avere direzioni diverse all\'interno di un glifo. Queste condizioni sono considerate errori nelle poliline utilizzate per definire le facce.
-   Forma da testo può anche essere creato con [Macro Fonts Win10 PYMP](Macro_Fonts_Win10_PYMP/it.md).
-   Per creare Forme da testo disposte in modo circolare utilizzare il [Macro FCCircularText](Macro_FCCircularText/it.md).



## Selezione file font su Windows 

In Windows l\'accesso alla cartella dei caratteri predefinita è limitato. Ciò influisce sulla selezione del file di carattere per Forma da testo. Esistono tre casi in FreeCAD in cui è possibile specificare un file di font per Forma da testo: nel pannello attività Forma da testo, quando si modifica la proprietà **Font File** di una Forma da testo e quando si specifica il file di font predefinito in [Preferenze per l\'ambiente Draft](Draft_Preferences/it#Testi_e_quotature.md).

Non è possibile premere il pulsante **...** e quindi selezionare un file dalla cartella predefinita dei font di Windows quando si utilizza la finestra di dialogo dei file nativi. Ci sono una serie di soluzioni alternative:

-   Assicurarsi che **DontUseNativeFontDialog** sia impostato su {{True}}, che è il valore predefinito per questa preferenza. Questo chiamerà una finestra di dialogo file diversa, non nativa, solo quando si preme il pulsante **...** nel pannello attività Forma da testo. Con questa finestra di dialogo è possibile accedere alla cartella predefinita dei font di Windows.
-   Cambiare **DontUseNativeDialog** in {{True}}. Ciò indica a FreeCAD di utilizzare sempre la finestra di dialogo dei file non nativi.
-   Specificare il file del carattere nella casella di immissione. Ovviamente è possibile digitare il percorso completo o copiare e incollare il percorso da Esplora file di Windows. Ma c\'è anche un altro modo per entrare nella cartella. Se si inserisce {{Value|C:\}} apparirà un elenco a tendina. Selezionare {{Value|Windows}} da quell\'elenco e aggiungere {{Value|\F}}. Selezionare {{Value|Fonts}} dal nuovo elenco a discesa. Infine aggiungere {{Value|\}} e le prime lettere del file del font, quindi selezionalo dall\'elenco a discesa.
-   Creare una cartella personalizzata contenente i file dei font.

Vedere il paragrafo [Preferenze](#Preferenze.md) di seguito per la posizione delle preferenze citate.



## Tutorial

-   [Tutorial Forma da testo - ShapeString](Draft_ShapeString_tutorial/it.md): come estrudere un testo, posizionarlo nello spazio 3D e creare un\'incisione in un altro corpo.
-   [How to use ShapeStrings in PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623)



## Preferenze

Vedere anche: [Impostare le Preferenze](Preferences_Editor/it.md), [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md) e [Modifica parametri](Std_DlgParameter/it.md).

-   Il file di font predefinito può essere modificato nelle preferenze: **Modifica → Preferenze... → Draft → Testi e quotature → Font predefinito per Forma da testo**.
-   Per utenti Windows:
    -   Impostare **Strumenti → Modifica parametri... → BaseApp → Preferences → Dialog → DontUseNativeFontDialog** su {{True}} per utilizzare la finestra di dialogo del file non nativo quando si seleziona un file di carattere dal pannello delle attività Forma da testo.
    -   In alternativa, impostare **Strumenti → Modifica parametri... → BaseApp → Preferences → Dialog → DontUseNativeDialog** su {{True}} per utilizzare sempre la finestra di dialogo del file non nativo.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Forma da testo è derivato da un [Part Part2DObject](Part_Part2DObject/it.md) e ne eredita tutte le proprietà. Ha anche le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Draft}}

-    **Font File|File**: specifica il percorso del file di font utilizzato per disegnare il testo.

-    **Size|Length**: specifica l\'altezza generale del testo.

-    **String|String**: specifica la stringa di testo da visualizzare. A differenza di un [Draft Testo](Draft_Text/it.md), un Draft Forma da testo può visualizzare solo una singola riga di testo.

-    **Tracking|Length**: specifica la spaziatura aggiuntiva tra i caratteri del testo.



### Vista


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifica la [Campitura](Draft_Pattern/it.md) con cui riempire le facce del testo. Questa proprietà funziona solo se **Display Mode** è {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifica la dimensione della [Campitura](Draft_Pattern/it.md).



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare una Draft Forma da testo usare il metodo `make_shapestring` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makeShapeString`.


```python
shapestring = make_shapestring(String, FontFile, Size=100, Tracking=0)
```

-   Crea una forma composta `shapestring` usando la `String` specificata e il percorso completo di un `FontFile` supportato.

-    `Size`è l\'altezza in millimetri del testo risultante.

-    `Tracking`è la spaziatura aggiuntiva tra i caratteri, in millimetri.

Il posizionamento di `ShapeString` può essere cambiato sovrascrivendo il suo attributo `Placement`, o sovrascrivendo singolarmente i suoi attributi `Placement.Base` e `Placement.Rotation`.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

font1 = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
font2 = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
font3 = "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf"

S1 = Draft.make_shapestring("This is a sample text", font1, 200)

S2 = Draft.make_shapestring("Inclined text", font2, 200, 10)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(-1000, 500, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 45))
S2.Placement = place2

S3 = Draft.make_shapestring("Upside-down text", font3, 200, 10)
S3.Placement.Base = App.Vector(0, -1000, 0)
S3.Placement.Rotation = App.Rotation(zaxis, 180)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ShapeString/it
