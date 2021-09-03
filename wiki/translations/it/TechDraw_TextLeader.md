---
- GuiCommand:/it
   Name:TechDraw RichTextAnnotation
   Name/it:Blocco di testo
   MenuLocation:TechDraw → Annotazioni → Blocco di testo
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   Version:0.19
   SeeAlso:[Modelli di squadrature](TechDraw_Templates/it.md), [SVG di Draft](Draft_SVG/it.md), [Linea guida](TechDraw_LeaderLine/it.md)
---


</div>

## Descrizione

Lo strumento Blocco di testo aggiunge un blocco di annotazione formattato a una [Linea guida](TechDraw_LeaderLine/it.md) o ad una vista.

<img alt="" src=images/TechDraw_RichTextBlock_sample.png  style="width:220px;"> 
*Blocco di testo indipendente*

## Utilizzo

1.  Premere il pulsante **<img src="images/TechDraw_RichTextAnnotation.svg" width=16px> [Blocco di testo](TechDraw_RichTextAnnotation/it.md)**.
2.  Si apre una finestra di dialogo delle azioni che consente l\'immissione rapida del testo.
3.  Il pulsante **Avvia l'editor di testo avanzato** apre un editor completo. Premere l\'icona Salva per registrare le modifiche.
4.  Dopo aver creato il blocco, è possibile modificarlo facendo doppio clic su RichTextBlock nella struttura.
5.  Per collegare il blocco a una [Linea guida](TechDraw_LeaderLine/it.md), selezionare la linea prima di avviare lo strumento Blocco di testo.

## Proprietà

-    **X,Y**: la posizione del blocco. Relativa alla fine della linea se collegato a una [Linea guida](TechDraw_LeaderLine/it.md), altrimenti questa è la posizione sulla pagina.

-    **ShowFrame**: disegna un contorno attorno al blocco.

-    **MaxWidth**: limita la dimensione orizzontale del blocco. Il valore di -1 è per larghezza illimitata.

-    **AnnoText**: il testo HTML del blocco.

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Blocco di testo può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
myPage = FreeCAD.ActiveDocument().Page
myBase = FreeCAD.ActiveDocument().View
blockObj = FreeCAD.ActiveDocument.addObject('TechDraw::DrawRichAnno','DrawRichAnno')
FreeCAD.activeDocument().myPage.addView(blockObj)
blockObj.X = 5
blockObj.Y = 5
blockObj.AnnoText = myHTMLText
```

## Note

-   È possibile modificare il Blocco di testo facendo doppio clic su di esso nella vista ad albero. Il doppio clic nell\'area grafica non è ancora supportato.


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
