---
- GuiCommand:/it
   Name:TechDraw WeldingSymbol
   Name/it:Informazioni di saldatura
   Icon:techdraw-weldsymbol.svg
   MenuLocation:TechDraw → Informazioni di saldatura
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Linea guida](TechDraw_LeaderLine/it.md)
   Version:0.19
---

# TechDraw WeldSymbol/it


</div>

## Descrizione

Lo strumento Simbolo saldatura aggiunge le specifiche di saldatura a una linea guida esistente.

<img alt="" src=images/TechDraw_WeldingSymbol_example.png  style="width:330px;"> 
*Specifiche di saldatura aggiunte a una linea guida*

## Utilizzo

1.  Selezionare una [linea guida](TechDraw_LeaderLine/it.md). esistente.
2.  Premere il pulsante **<img src="images/TechDraw_WeldSymbol.svg" width=16px> Informazioni di saldatura**.
3.  Si apre una finestra di dialogo Azioni. Essa consente di inserire o selezionare singoli simboli di saldatura e il testo di accompagnamento da aggiungere alla linea guida.
4.  Per uscire dalla finestra di dialogo e salvare le modifiche, premere il pulsante **OK**. Per uscire dalla finestra di dialogo senza salvare, premere il pulsante **Annulla**.
5.  Dopo aver creato il simbolo di saldatura, è possibile modificarlo facendo doppio clic sul Welding Symbol nell\'albero.

## Proprietà

### Simbolo di saldatura 

-    **All Around**: mostra il simbolo All Around (cerchio) in corrispondenza del nodo nella linea guida.

-    **Field Weld**: mostra il simbolo Field Weld (flag) sul nodo nella linea guida.

-    **Alternate Weld**: scosta il simbolo inferiore per indicare saldature alternate.

-    **Tail Text**: testo da mostrare alla fine della linea guida.

### Tessere dei simboli 

Ogni singolo simbolo (\"lato freccia\" e \"altro lato\") è rappresentato da un oggetto \"tessera\". Un simbolo di saldatura è associato a 1 o 2 tessere. Ognuna di esse ha le seguenti proprietà:

-    **Tile Parent**: Il simbolo della saldatura principale

-    **Tile Row**: Riga della tessera. 0 significa sopra la linea, -1 sotto la linea. **Nota:** Se si cambia la riga di una tessera, si deve anche cambiare la tessera per il secondo lato! In questo modo si possono capovolgere i lati.

-    **Tile Column**: Colonna della tessra. Al momento è sempre 0, quindi la proprietà non è modificabile.

-    **Symbol File**: Directory e nome file del file svg per il simbolo.

-    **Symbol Included**: Nome della directory e del file SVG del simbolo effettivamente incluso. (È una directory temporanea.)

-    **Left Text**: Testo da visualizzare a sinistra del simbolo svg.

-    **Center Text**: Testo da visualizzare sopra o sotto il simbolo svg.

-    **Right Text**: Testo da visualizzare a destra del simbolo svg.

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Simbolo saldatura può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
symbolName = "DrawWeldSymbol001")
symbolType = "TechDraw::DrawWeldSymbol"
App.activeDocument().addObject(symbolType, symbolName)
App.activeDocument().Page.addView(App.activeDocument().DrawWeldSymbol001)
App.activeDocument().DrawWeldSymbol001.Leader = myLeader
App.activeDocument().DrawWeldSymbol001.AllAround = True
App.activeDocument().DrawWeldSymbol001.FieldWeld = True
App.activeDocument().DrawWeldSymbol001.AlternatingWeld = True
App.activeDocument().DrawWeldSymbol001.TailText = "process text"

tileName = "DrawTileWeld001"
tileType = "TechDraw::DrawTileWeld"
App.activeDocument().addObject(tileType, tileName)
App.activeDocument().DrawTileWeld001.TileParent = App.activeDocument().DrawWeldSymbol001
App.activeDocument().DrawTileWeld001.TileRow = 0
App.activeDocument().DrawTileWeld001.TileColumn = 0
App.activeDocument().DrawTileWeld001.SymbolFile = fullPathToMySvgFile
App.activeDocument().DrawTileWeld001.LeftText = "left text"
App.activeDocument().DrawTileWeld001.RightText = "right text"
App.activeDocument().DrawTileWeld001.CenterText = "center text"
```

## Svg Symbol Tiles 


<div class="mw-translate-fuzzy">

## Tessere dei simboli SVG 

-   I singoli simboli sono formati da file Svg di 64x64 pixel. È possibile creare simboli aggiuntivi in un programma SVG come [Inkscape](https://en.wikipedia.org/wiki/Inkscape) usando uno dei simboli forniti da FreeCAD come modello.

<img alt="" src=images/Techdraw-WeldingSymbolLayoutArrow.svg  style="width:128px;"> <img alt="" src=images/Techdraw-WeldingSymbolLayoutOther.svg  style="width:128px;">


</div>

<img alt="" src=images/Techdraw-WeldingSymbolLayoutArrow.svg  style="width:128px;"> <img alt="" src=images/Techdraw-WeldingSymbolLayoutOther.svg  style="width:128px;">


<div class="mw-translate-fuzzy">

\* I singoli simboli sono formati da file Svg 64x64 (nominali) pixel. Le tessere hanno in realtà un \"bordo\" di 4px. Il bordo assicura che la linea guida e il simbolo corrispondano.

-   Il simbolo è disegnato in nero su uno sfondo trasparente. Lo spessore del tratto è di 0,5 mm.
-   La linea guida passa sotto i simboli dal lato freccia e sopra i simboli per \"l\'altro\" lato.
-   Non esiste uno standard di denominazione particolare se non quello di aggiungere \"Su o Giù\" alla freccia o ad altri simboli laterali.


</div>

## Note

-   Si può modificare il Simbolo di saldatura facendo doppio clic su di esso nella vista ad albero. Il doppio clic nell\'area grafica non è ancora supportato.
-   Esiste un [parametro preferenza](TechDraw_Preferences/it.md) per la directory dei simboli di saldatura predefinita. Si possono aggiungere dei simboli in una directory personale.


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw WeldSymbol/it
