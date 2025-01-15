---
 GuiCommand:
   Name: Arch Axis
   Name/it: Assi
   MenuLocation: Arch , Strumenti per assi , Asse
   Workbenches: Arch_Workbench/it
   Shortcut: **A** **X**
   SeeAlso: Arch_AxisSystem/it, Arch_Grid/it
---

# Arch Axis/it


</div>



## Descrizione

Lo strumento <img alt="" src=images/Arch_Axis.svg  style="width:16px;"> Assi permette di posizionare una serie di assi nel documento corrente. La distanza e l\'angolo tra gli assi è personalizzabile, così come lo stile di numerazione. Gli assi servono principalmente da riferimento per bloccare gli oggetti, ma possono anche essere utilizzati in combinazione con dei <img alt="" src=images/Arch_AxisSystem.svg  style="width:16px;"> [Sistemi di assi](Arch_AxisSystem/it.md), e possono anche essere referenziati da altri oggetti Arch per creare schiere parametriche, ad esempio di travi o colonne. Al posto degli assi si può anche usare una <img alt="" src=images/Arch_Grid.svg  style="width:16px;"> [Griglia](Arch_Grid/it.md).

<img alt="" src=images/Arch_Axis_example.jpg  style="width:600px;"> 
*Due assi posizionati perpendicolarmente tra loro per creare una griglia
*



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Arch_Axis.svg" width=16px> Assi
**, oppure premere i tasti **A** e **X**
2.  [Spostare](Draft_Move/it.md) o [ruotare](Draft_Rotate/it.md) il sistema di assi nella posizione desiderata
3.  Attivare la modalità di modifica facendo doppio clic sul sistema di assi nella vista ad albero per regolare le impostazioni quali il numero di assi, le distanze e gli angoli tra gli assi.


</div>



## Opzioni

-   Ogni asse di un sistema di assi ha una propria distanza e un proprio angolo rispetto all\'asse precedente. Questo permette di creare sistemi molto complessi, quali sistemi non ortogonali, sistemi polari o qualsiasi tipo di sistema non uniforme.
-   Facendo doppio clic sull\'asse nella vista ad albero è possibile modificare le distanze, gli angoli e le etichette di ciascun asse.
-   La lunghezza degli assi, le dimensioni delle bolle e gli stili di numerazione sono personalizzabili direttamente tramite le proprietà del sistema di assi.
-   Ogni asse può anche visualizzare un\'etichetta, che è modificabile tramite la finestra di dialogo del pannello azioni.



## Proprietà

-    {{PropertyData/it|Length}}: La lunghezza degli assi

-    **Limit**: Se maggiore di zero, ciascun asse verrà rappresentato come due linee della lunghezza specificata anziché una linea continua {{Version/it|0.20}}

-    {{PropertyView/it|Bubble Size}}: La dimensione dei cerchi di numerazione degli assi

-    {{PropertyView/it|Numeration style}}: Lo stile di numerazione degli assi: 1,2,3, A, B, C, ecc.

-    {{PropertyView/it|Bubble Position}}: Dove la bolla è posizionata sull\'asse: al punto iniziale, endpoint, entrambi o nessuno.

-    {{PropertyView/it|Font Name}}: Un font per disegnare il numero della bolla e/o le etichette

-    {{PropertyView/it|Font Size}}: Solo la dimensione del testo dell\'etichetta (il testo della bolla è controllato dalla dimensione della bolla)

-    {{PropertyView/it|Show Labels}}: Attiva/disattiva la visualizzazione dei testi delle etichette



## Utilizzare come segno di sezione 

Impostando la proprietà **Bubble Position** su **Arrow left/right** o **Bar left/right**, l\'asse visualizzerà una freccia o una barra piena invece della bolla, quindi può essere utilizzato come segno di sezione. {{Version/it|0.20}}



## Script


**Vedere anche:**

[API di Arch](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Assi può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


```python
Axes = makeAxis(num=5, size=1000, name="Axes")
```

-   Crea un oggetto `Axes` con un dato numero (`num`) di assi e un intervallo `size` tra ciascun asse.

Esempio:


```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Arch Axis/it
