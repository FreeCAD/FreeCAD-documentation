# TechDraw Symbol/it
---
- GuiCommand:/it   Name:TechDraw_Symbol   Name/it:Simbolo SVG   Workbenches:[MenuLocation:TechDraw → Simbolo SVG   Shortcut:   SeeAlso:[[TechDraw Templates/it|Modelli di squadrature](TechDraw_Workbench/it___TechDraw]].md), [SVG di Draft](Draft_SVG/it.md)---


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Simbolo inserisce un file [SVG](SVG/it.md) nella pagina. Questo simbolo può essere qualsiasi cosa che aiuti ad annotare il disegno, e che non ha bisogno di essere ulteriormente modificato.


</div>

<img alt="" src=images/TechDraw_SymbolSVG_sample.png  style="width:250px;">


<div class="mw-translate-fuzzy">



*Rosa dei venti aggiunta alla pagina di disegno; questo simbolo è disponibile installando la macro SymbolsLibrary con Addon Manager*


</div>



## Uso


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/TechDraw_Symbol.svg" width=16px> [Simbolo SVG](TechDraw_Symbol/it.md)
**
2.  Si apre una finestra di dialogo.
3.  Selezionare un percorso e il nome file.
4.  Premere **OK**


</div>



## Note

-    **Scale Type**per i simboli è sempre impostata su *Personalizzato* al momento della creazione. Questo è per comodità, poiché i simboli sono quasi sempre ridimensionati in modo diverso dal resto degli oggetti nella pagina.

## Properties

See also [TechDraw View](TechDraw_View#Properties.md).


{{TitleProperty|Drawing view}}

-    **Editable Texts**: List of editable texts, if any.



## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Simbolo SVG può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
sym = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewSymbol','TestSymbol')
rc = page.addView(anno)
f = open(unicode(symbolFileSpec,'utf-8'),'r')
svg = f.read()
f.close()
sym.Symbol = svg
rc = page.addView(sym)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Symbol/it
