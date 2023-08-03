---
 GuiCommand:
   Name: Draft Ellipse
   Name/it: Ellisse
   MenuLocation: Drafting , Ellisse
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   Shortcut: **E** **L**
   Version: 0.7
---

# Draft Ellipse/it



## Descrizione

Il comando <img alt="" src=images/Draft_Ellipse.svg  style="width:24px;"> **Ellisse** crea un\'ellisse nel [piano di lavoro](Draft_SelectPlane/it.md) corrente da due punti che definiscono un rettangolo in cui si adatterà l\'ellisse.

Un Draft Ellisse può essere trasformata in un arco ellittico impostando le sue proprietà **First Angle** e **Last Angle** su valori diversi.

<img alt="" src=images/Draft_ellipse_example.jpg  style="width:400px;"> 
*Ellisse definita dagli angoli di un rettangolo*



## Utilizzo

Vedere anche: [Barra di Draft](Draft_Tray/it.md), [Aggancio](Draft_Snap/it.md) e [Vincolare](Draft_Constrain/it.md).

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Ellipse.svg" width=16px> [Ellisse](Draft_Ellipse/it.md)**.
    -   Selezionare l\'opzione **Drafting → <img src="images/Draft_Ellipse.svg" width=16px> Ellisse** dal menu.
    -   Usare la scorciatoia da tastiera: **E** poi **L**.
2.  Si apre il pannello delle attività **Ellisse**. Vedere [Opzioni](#Options.md) per maggiori informazioni.
3.  Scegliere il primo punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
4.  Scegliere il secondo punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**. Questo punto non deve essere vincolato all\'asse X, Y o Z.



## Opzioni

Le scorciatoie da tastiera a carattere singolo disponibili nel pannello delle attività possono essere modificate. Vedere [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md). Le scorciatoie menzionate qui sono le scorciatoie predefinite.

-   Per inserire manualmente le coordinate, inserire le componenti X, Y e Z e premere **Enter** dopo ognuna di esse. Oppure si può premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando ha i valori desiderati. Si consiglia di spostare il puntatore fuori dalla [Vista 3D](3D_view/it.md) prima di inserire le coordinate.
-   Premere **R** o fare clic sulla casella di controllo **Relativo** per attivare o disattivare la modalità relativa. Se la modalità relativa è attiva, le coordinate del secondo punto sono relative al primo punto, altrimenti sono relative all\'origine del sistema di coordinate.
-   Premere **G** o fare clic sulla casella di controllo **Globale** per attivare o disattivare la modalità globale. Se la modalità globale è attiva, le coordinate sono relative al sistema di coordinate globale, altrimenti sono relative al sistema di coordinate [piano di lavoro](Draft_SelectPlane/it.md). {{Version/it|0.20}}
-   Premere **L** o fare clic sulla casella di controllo **Riempimento** per attivare o disattivare la modalità riempimento. Se la modalità riempimento è attiva, l\'ellisse creata avrà **Make Face** impostato su `True` e avrà una faccia piena.
-   Premere **T** o fai clic sulla casella di controllo **Continua** per attivare o disattivare la modalità continua. Se la modalità continua è attiva, il comando verrà riavviato al termine, consentendo di continuare a creare ellissi.
-   Premere **S** per attivare o disattivare [Aggancia](Draft_Snap/it.md).
-   Premere **Esc** o il pulsante **Chiudi** per interrompere il comando.



## Note

-   Un\'Ellisse può essere modificata con il comando [Modifica](Draft_Edit/it.md).



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Per modificare il numero di decimali utilizzati per l\'inserimento delle coordinate: **Modifica → Preferenze... → Generale → Unità → Impostazioni unità → Numero di cifre decimali**.
-   Per modificare il valore iniziale della modalità riempimento: **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti Draft → Riempi gli oggetti con le facce quando possibile**. La modifica della modalità di riempimento in un pannello delle attività sovrascriverà questa preferenza per la sessione corrente di FreeCAD.
-   Se l\'opzione **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti di Draft → Usa le primitive di Part quando disponibili** è selezionata, il comando creerà una [Part Ellisse](Part_Ellipse/it.md) invece di una Draft Ellisse.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Draft Ellisse è derivato da un [Part Part2DObject](Part_Part2DObject/it.md) e ne eredita tutte le proprietà. Ha anche le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Draft}}

-    **Area|Area**: (sola lettura) specifica l\'area della faccia dell\'ellisse. Il valore sarà {{value|0.0}} se **Make Face** se `False` o la faccia non può essere creata.

-    **First Angle|Angle**: specifica l\'angolo del primo punto dell\'ellisse, normalmente {{value|0&#176;}}.

-    **Last Angle|Angle**: specifica l\'angolo dell\'ultimo punto dell\'ellisse, normalmente {{value|0&#176;}}.

-    **Major Radius|Length**: specifica il raggio maggiore dell\'ellisse.

-    **Make Face|Bool**: specifica se l\'ellisse crea o meno una faccia. Se è `True` viene creata una faccia, altrimenti solo il perimetro è considerato parte dell\'oggetto. Questa proprietà funziona solo se la forma è un\'ellisse completa.

-    **Minor Radius|Length**: specifica il raggio minore dell\'ellisse.



### Vista


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifica la [Campitura](Draft_Pattern/it.md) con cui riempire la faccia dell\'ellisse. Questa proprietà funziona solo se **Make Face** è `True` e se **Display Mode** è {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifica la dimensione della [Campitura](Draft_Pattern/it.md).



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare una Draft Ellisse usare il metodo `make_ellipse` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makeEllipse`.


```python
ellipse = make_ellipse(majradius, minradius, placement=None, face=True, support=None)
```

-   Crea un oggetto `ellipse` dai dati di (`majradius`) e (`minradius`) in millimetri.
    -   Il valore più grande viene utilizzato per il raggio maggiore (asse X) se non viene fornito nessun altro posizionamento.
-   Se `placement` è `None` l\'ellisse viene creata all\'origine.
-   Se `face` è `True`, l\'ellisse crea una faccia, cioè appare riempita.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

ellipse1 = Draft.make_ellipse(3000, 200)
ellipse2 = Draft.make_ellipse(700, 1000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

ellipse3 = Draft.make_ellipse(700, 1000, placement=place3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Ellipse/it
