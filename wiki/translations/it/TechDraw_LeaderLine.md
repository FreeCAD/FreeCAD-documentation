---
- GuiCommand:/it
   Name:TechDraw LeaderLine
   Name/it:Linea guida
   MenuLocation:TechDraw → Aggiungi linee → Linea guida
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   Version:0.19
   SeeAlso:[Blocco di testo](TechDraw_RichTextAnnotation/it.md), [Simbolo di saldatura](TechDraw_WeldSymbol/it.md), [Gruppi di linee](TechDraw_LineGroup/it.md)
---

# TechDraw LeaderLine/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Linea guida aggiunge una linea a una vista. Altri oggetti di annotazione, come un [Blocco di testo](TechDraw_RichTextAnnotation/it.md), possono essere collegati alla linea guida per formare annotazioni complesse.


</div>

![](images/TechDraw_LeaderLine_sample.png )


<div class="mw-translate-fuzzy">



*Linea guida aggiunta a View001*


</div>




<div class="mw-translate-fuzzy">

## Utilizzo


</div>


<div class="mw-translate-fuzzy">

1.  Selezionare una vista.
2.  Premere il pulsante **<img src="images/TechDraw_LeaderLine.svg" width=16px> Linea guida**. Si apre una finestra di dialogo che consente di disegnare la linea guida e di assegnare simboli di fine linea.
3.  Cliccare su **seleziona punti** e quindi fare clic nella pagina per definire il punto iniziale della linea.
4.  Muovere il mouse e fare clic su un altro punto per creare una linea.
5.  ora è possibile
    1.  terminare il disegno facendo doppio clic o premendo **Salva i punti**,
    2.  oppure aggiungere ulteriori punti per definire più segmenti di linea.
6.  Per terminare la creazione, premere **OK** per chiudere la finestra di dialogo.


</div>

## Usage edit 


<div class="mw-translate-fuzzy">

1.  Selezionare la Linea guida nella struttura del documento e fare doppio clic su di essa.
2.  Si apre una finestra di dialogo in cui è possibile modificare l\'aspetto.
3.  Per modificare i punti, fare clic su **Modifica punti** e i punti della linea diventano visibili nel disegno.
4.  Trascinare i punti nel posto desiderato e terminare la modifica facendo clic su **Salva modifiche**.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Note

-   È possibile modificare una linea guida facendo doppio clic su di essa nella vista ad albero. Il doppio clic nell\'area grafica non è ancora supportato. I segmenti di linea possono essere modificati premendo **Modifica punti**. Per uscire dalla modifica del punto, premere **Salva modifiche** o **Annulla modifiche**.
-   Se non è stato definito alcun punto durante la creazione della linea guida, verrà posizionata una linea corta al centro della vista. Successivamente non è possibile aggiungere ulteriori punti.
-   Per impostazione predefinita, l\'opzione **Leader Line Auto Horizontal** delle [preferenze](TechDraw_Preferences/it.md) è attivata. Pertanto l\'ultimo segmento di linea sarà orizzontale. Quindi, se c\'è un solo un segmento, si ottiene una linea orizzontale, indipendentemente da dove si è posto il secondo punto.
-   si può disattivare la funzione orizzontale automatica per le linee guida esistenti modificando la proprietà **Auto Horizontal**.


</div>



## Proprietà

### Data


{{Properties_Title|Base}}

-    **Start Symbol|Enumeration**: The symbol at the start of the leaderline. Options: <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Filled Arrow, <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Open Arrow, <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Tick, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Dot, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Open Circle, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Fork, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Filled Triangle, None.

-    **End Symbol|Enumeration**: The symbol at the end of the leaderline. Idem.

-    **X|Distance**: The X coordinate of the leaderline relative to the View.

-    **Y|Distance**: The Y coordinate of the leaderline relative to the View.


{{Properties_Title|Leader}}

-    **Leader Parent|Link**: The View the leaderline is attached to.

-    **Way Points|VectorList**: The points of the leaderline.

-    **Scalable|Bool**: Specifies if the leaderline scales with **Leader Parent**.

-    **Auto Horizontal|Bool**: Specifies if the last leaderline segment is forced to be horizontal.

### View


{{TitleProperty|Base}}

-    **Keep Label|Bool**: Not used.

-    **Stack Order|Integer**: Over or underlap relative to other drawing objects. <small>(v0.21)</small> 


{{TitleProperty|Line Format}}

-    **Color|Color**: The color of the leaderline.

-    **Line Style|Enumeration**: The style of the leaderline. Options: NoLine, <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continuous, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Dash, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Dot, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> DashDot, <img alt="Length" src=images/DashDotDot-line.svg  style="width:20px;"> DashDotDot.

-    **Line Width|Length**: The width of the leaderline.



## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Linea guida può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


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


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LeaderLine/it
