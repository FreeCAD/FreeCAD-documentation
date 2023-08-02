---
- GuiCommand:
   Name: TechDraw Annotation
   Name/it: Annotazione
   MenuLocation: TechDraw -> Annotazioni -> Annotazione
   Workbenches: TechDraw_Workbench/it
   SeeAlso: Draft Text/it, Draft ShapeString/it
---

# TechDraw Annotation/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Annotazione aggiunge un blocco di testo a una pagina di disegno.


</div>

<img alt="" src=images/AnnotationSample.png  style="width:250px;"> 
*Annotazione nella pagina di disegno*



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Se nel documento sono presenti più pagine di disegno, è necessario selezionare la pagina desiderata nella struttura.
2.  Premere il pulsante **<img src="images/TechDraw_Annotation.svg" width=24px> [Annotazione](TechDraw_Annotation/it.md)**.
3.  Nella pagina viene visualizzato un blocco di testo contenente \"Testo predefinito\". Utilizzare l\'editor delle proprietà per modificare il testo. Trascinare l\'annotazione nella posizione desiderata.
4.  Potrebbe essere necessario premere ** <img src="images/Std_Refresh.svg" width=16px> [Aggiorna](Std_Refresh/it.md)** e/o **<img src="images/TechDraw_RedrawPage.svg" width=16px> [Ridisegna la pagina](TechDraw_RedrawPage/it.md)** per far cambiare il testo.


</div>

![](images/UpdateAnnotation.png )


<div class="mw-translate-fuzzy">



*Modifica dell'annotazione tramite l'editor delle proprietà*


</div>



## Note


<div class="mw-translate-fuzzy">


**Note:**

alcuni caratteri interferiscono con la rappresentazione interna del testo dell\'annotazione. Nello specifico, questi sono le doppie virgolette `"`, i simboli minore di `<` e maggiore di `>`; questi caratteri devono essere sostituiti rispettivamente dai caratteri di escape HTML,`&amp;quot;`, `&amp;lt;`, e `&amp;gt;`. Per i dettagli vedere [Character encodings in HTML](https://en.wikipedia.org/wiki/Character_encodings_in_HTML#HTML_character_references).


</div>



## Proprietà

L\'Annotazione eredita tutte proprietà applicabili dalla Vista di base, tranne **Scale**. Al suo posto usa la proprietà **TextSize**.

-    **Text**: Il testo da visualizzare.

-    **Font**: Il nome del font da usare. Annotazione utilizza la migliore combinazione di font installati.

-    **TextColor**: Il colore del testo.

-    **TextSize**: La dimensione del testo in mm.

-    **MaxWidth**: La larghezza massima del blocco di annotazione. -1 Indica nessuna larghezza massima.

-    **LineSpace**: Regolazione dell\'interlinea (%).

-    **TextStyle**: Stile del testo \"Normal\", \"Bold\", \"Italic\", \"Bold-Italic\"



## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Annotazione può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
anno = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewAnnotation','TestAnno')
anno.Text = ['Different Text']
anno.TextStyle = 'Bold'
rc = page.addView(anno)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Annotation/it
