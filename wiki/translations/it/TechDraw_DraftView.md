---
- GuiCommand:/it
   Name:TechDraw_DraftView
   Name/it:Vista di Draft
   MenuLocation:TechDraw → Vista di Draft
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Draft](Draft_Workbench/it.md), [Vista di Arch](TechDraw_ArchView/it.md)
---

# TechDraw DraftView/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/TechDraw_DraftView.svg  style="width:24px;"> _, le viste create con questo strumento sono gestite da <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/it.md), e appositamente progettato per mostrare oggetti 2D. Vedere le note.


</div>

![](images/TechDraw_DraftView_example.png ) 
*Elementi di Draft, cerchi e schiere, importati in una pagina di disegno TechDraw*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un oggetto Draft nella finestra 3D o nella vista a albero.
2.  Se nel documento ci sono più pagine di disegno, è necessario selezionare anche la pagina desiderata nella struttura.
3.  Premere il pulsante **<img src="images/TechDraw_DraftView.svg" width=16px> [Vista di Draft](TechDraw_DraftView/it.md)
**
4.  Nella pagina viene aggiunta una vista di un oggetto di Draft.


</div>

### Limitazioni


<div class="mw-translate-fuzzy">

Poiché la Vista di Draft è resa all\'interno del modulo [Draft](Draft_Workbench/it.md), TechDraw ha un controllo limitato sul suo aspetto. Potrebbe essere necessario apportare delle modifiche all\'interno di Draft per ottenere la rappresentazione desiderata.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

-   La creazione di una vista di Draft di un gruppo gestisce in modo ricorsivo tutti gli oggetti trovati in quel gruppo e nei suoi sottogruppi. La vista viene aggiornata automaticamente quando i contenuti del gruppo cambiano.
-   Non è prevista la rimozione delle linee nascoste. Ogni faccia trovata negli oggetti gestiti viene semplicemente proiettata lungo il vettore Direzione, quando le facce si sovrappongono non viene intrapresa nessuna azione specifica.
-   La vista di Draft supporta anche tutti gli oggetti Draft che non sono basati su parti, come dimensioni e testi
-   Colore, larghezza e tipo di linea possono essere specificati nelle proprietà. I tipi di linea possono essere perfezionati dando direttamente un valore [stroke-dasharray](https://www.w3.org/TR/SVG/painting.html#StrokeProperties), ad esempio 3,5.
-   Le facce proiettate vengono riempite con il colore della faccia.


</div>

## Proprietà


<div class="mw-translate-fuzzy">

-    **Source**: L\'oggetto di Draft da visualizzare

-    **LineWidth**: La larghezza delle linee, indipendentemente dalla scala

-    **FontSize**: Le dimensioni di tutti i testi che compaiono in questa vista (i testi e le dimensioni)

-    **Direction**: La direzione di proiezione da usare

-    **Color**: Il colore delle linee

-    **LineStyle**: Lo stile di linea da utilizzare per questa vista. Può essere Solid, Dashed, Dashdot, Dot o un modello linea SVG come 0.20,0.20

-    **LineSpacing**: Interlinea per testi multilinea


</div>


<div class="mw-translate-fuzzy">

Nota: Vista di Draft eredita tutte le proprietà della Vista di base applicabili.


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento New Draft può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDraft','TestDraft')
dv.Source = myDraftbject
rc = page.addView(dv)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DraftView/it
