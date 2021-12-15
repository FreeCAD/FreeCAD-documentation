---
- GuiCommand:/it
   Name:TechDraw Balloon
   Name/it:Pallinatura
   MenuLocation:TechDraw → Pallinatura
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   Version:0.19
   SeeAlso:[Annotazione](TechDraw_Annotation/it.md)
---

# TechDraw Balloon/it


</div>

## Descrizione

Lo strumento Pallinatura aggiunge le bolle con una linea guida in un disegno.

<img alt="" src=images/Techdraw_balloon.png  style="width:600px;">

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare la vista a cui si vuole attaccare una bolla.
2.  Premere il pulsante **<img src="images/TechDraw_Balloon.svg" width=16px> [Pallinatura](TechDraw_Balloon/it.md)**.
3.  Il cursore assume un\'icona a forma di fumetto. Fare clic sulla pagina per fissare l\'origine della bolla nella posizione desiderata.
4.  La bolla può essere trascinata nella posizione desiderata. Usare Ctrl e trascina per spostare la bolla e la freccia.
5.  È possibile modificare le proprietà della bolla facendo doppio clic sulla sua etichetta del palloncino o sull\'oggetto bolla nell\'albero. Questo apre la finestra di dialogo Azioni bolla:


</div>

To move the bubble of a Balloon, press and hold the left mouse button on its center and drag the mouse.

To change the properties of a Balloon double-click it on the page or in the [Tree view](Tree_view.md). This will open the Balloon task panel.

**Note:** The position of a Balloon is relative to its Source View and uses the same scale factor.

## Utilizzo dei separatori 

Quando si utilizza una forma rettangolare, si possono aggiungere i separatori utilizzando \"\|\" nel testo. Ad esempio \"AAA\|TEST\|111\" restituisce:


<div class="mw-translate-fuzzy">

![300 px](images/balloon_separator.png )


</div>

## Proprietà

### Data


<div class="mw-translate-fuzzy">

### Dati

-    **Text**: testo da visualizzare.

-    **Source View**: vista sorgente per la bolla.

-    **Origin X**: posizione x dell\'origine della bolla.

-    **Origin Y**: posizione y dell\'origine della bolla.

-    **End Type**: simbolo di fine linea della bolla. Opzioni: <img alt="" src=images/Arrownone.svg  style="width:20px;"> Nessuno, <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Freccia piena, <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Freccia aperta, <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Barra, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Dot, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Cerchio aperto, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Biforcazione, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Triangolo pieno

-    **Shape**: forma della bolla. Opzioni: <img alt="" src=images/Circular.svg  style="width:20px;"> Cerchio, Nessuna, <img alt="" src=images/Triangle.svg  style="width:20px;"> Triangolo, <img alt="" src=images/Inspection.svg  style="width:20px;"> Ispezione, <img alt="" src=images/Hexagon.svg  style="width:20px;"> Esagono, <img alt="" src=images/TechDraw_Square.svg  style="width:20px;"> Quadrato, <img alt="" src=images/Rectangle.svg  style="width:20px;"> Rettangolo

-    **Shape Scale**: fattore di scala per la **Shape**.

-    **Text Wrap**: lunghezza dell\'involucro del testo; -1 significa che il testo non verrà mai racchiuso e il risultato è in ogni caso una riga singola.

-    **Kink Length**: distanza tra la **forma** e la piega della linea guida.

-    **X**: posizione orizzontale della bolla rispetto alla vista.

-    **Y**: posizione verticale della bolla rispetto alla vista.


</div>

### View


<div class="mw-translate-fuzzy">

### Vista

-    **Color**: colore del testo della bolla.

-    **Font**: il nome del carattere da utilizzare per la bolla.

-    **Fontsize**: dimensione del testo in mm.

-    **Line Width**: larghezza della linea della bolla.


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Pallinatura può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
bal1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewBalloon','Balloon')
rc = page.addView(bal1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Balloon/it
