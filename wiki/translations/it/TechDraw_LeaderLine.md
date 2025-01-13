---
 GuiCommand:
   Name: TechDraw LeaderLine
   Name/it: TechDraw Linea guida
   MenuLocation: TechDraw , Aggiungi linee , Linea guida
   Workbenches: TechDraw_Workbench/it
   Version: 0.19
   SeeAlso: TechDraw_RichTextAnnotation/it, TechDraw_WeldSymbol/it
---

# TechDraw LeaderLine/it



## Descrizione

Lo strumento **TechDraw Linea guida** aggiunge una linea a una Vista. Altri oggetti di annotazione, come un [Blocco di testo](TechDraw_RichTextAnnotation/it.md), possono essere collegati alla linea guida per formare annotazioni complesse.

![](images/TechDraw_LeaderLine_sample.png ) 
*Linea guida aggiunta ad una Vista*



## Creazione

1.  Selezionare una vista.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_LeaderLine.svg" width=16px> [Aggiungi linea guida](TechDraw_LeaderLine/it.md)**.
    -   Selezionare l\'opzione **TechDraw → Aggiungi linee → <img src="images/TechDraw_LeaderLine.svg" width=16px> Aggiungi linea guida** dal menu.
3.  Si apre un pannello delle azioni.
4.  Premere il pulsante **Seleziona punti**.
5.  Scegliere il primo punto sulla pagina per definire il punto iniziale della linea.
6.  Scegliere il punto successivo sulla pagina. Tenere premuto **Ctrl** per eseguire l\'aggancio ad angoli multipli di di 22,5°. Facoltativamente, utilizzare un doppio clic anziché un clic singolo per completare l\'immissione dei punti.
7.  Facoltativamente aggiungere più punti.
8.  Se non si ha fatto doppio clic su un punto: premere il pulsante **Salva punti**.
9.  Facoltativamente modificare il **Simbolo Iniziale**, **Simbolo Finale**, **Colore**, **Larghezza** e **Stile** della linea guida. Vedere [Proprietà](#Proprietà.md) per ulteriori informazioni.
10. Premere il pulsante **OK**.



## Modifica

1.  Fare doppio clic su una Linea guida nella [Vista ad albero](Tree_view/it.md).
2.  Si apre un pannello delle azioni.
3.  Per modificare i punti:
    1.  Premere il pulsante **Modifica punti**.
    2.  La Linea guida è contrassegnata da nodi temporanei.
    3.  Trascinare uno o più nodi in una nuova posizione.
    4.  Premere il pulsante **Salva modifiche**.
4.  Facoltativamente modificare il **Simbolo Iniziale**, **Simbolo Finale**, **Colore**, **Larghezza** e **Stile** della linea guida. Vedere [Proprietà](#Proprietà.md) per ulteriori informazioni.
5.  Premere il pulsante **OK**.



## Note

-   Non è possibile aggiungere o rimuovere punti da una Linea guida esistente.
-   Se non sono stati specificati punti al momento della creazione, al centro della vista viene posizionata una breve linea. Non c\'è modo di correggere una linea del genere, dovrebbe essere cancellata.
-   Per impostazione predefinita, la **Linea guida orizzontale automatica** [preferenza](TechDraw_Preferences/it#Annotazione.md) è selezionata. Ciò significa che l\'ultimo segmento di linea delle nuove Linee guida viene disegnato orizzontalmente. Se è presente un solo segmento il risultato sarà una singola linea orizzontale.
-   E\' possibile disattivare questa funzione orizzontale automatica per Le linee guida esistenti modificando la loro proprietà **Auto Horizontal**.



## Proprietà



### Dati


{{Properties_Title|Base}}

-    **Start Symbol|Enumeration**: il simbolo all\'inizio della Linea guida. Opzioni: <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Freccia piena, <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Freccia aperta, <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Tratto, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Punto, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Cerchio aperto, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Biforcazione, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Triangolo pieno, Nessuno.

-    **End Symbol|Enumeration**: il simbolo alla fine della linea guida. Idem.

-    **X|Distance**: la coordinata X della linea guida relativa alla Vista.

-    **Y|Distance**: la coordinata Y della linea guida relativa alla Vista.


{{Properties_Title|Leader}}

-    **Leader Parent|Link**: la vista a cui è associata la Linea guida.

-    **Way Points|VectorList**: i punti della Linea guida.

-    **Scalable|Bool**: specifica se la Linea guida viene ridimensionata con **Leader Parent**.

-    **Auto Horizontal|Bool**: specifica se l\'ultimo segmento della Linea guida deve essere orizzontale.



### Vista


{{TitleProperty|Base}}

-    **Keep Label|Bool**: non utilizzato.

-    **Stack Order|Integer**: sovrapposto o sovrapposto rispetto ad altri oggetti di disegno. {{Version/it|0.21}}


{{TitleProperty|Line Format}}

-    **Color|Color**: il colore della Linea guida.

-    **Stile linea|Enumeration**: lo stile della Linea guida. Opzioni: Nessuna linea, <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continuo, <img alt="" src=images/Dash-line.svg  style="width:20px;"> A tratti, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Punto, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> Tratto punto, <img alt="Length" src=images/DashDotDot-line.svg  style="width:20px;"> Tratto punto punto.

-    **Line Width|Length**: la larghezza della Linea guida.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Linea guida può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


```python
myPage = FreeCAD.ActiveDocument().Page
myBase = FreeCAD.ActiveDocument().View
leaderObj = FreeCAD.ActiveDocument.addObject('TechDraw::DrawLeaderLine','DrawLeaderLine')
FreeCAD.activeDocument().myPage.addView(leaderObj)
FreeCAD.activeDocument().leaderObj.LeaderParent = myBase
#first waypoint is always (0,0,0)  
#rest of waypoints are positions relative to (0,0,0)
leaderObj.WayPoints = [p0,p1,p2]
leaderObj.X = 5
leaderObj.Y = 5
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LeaderLine/it
