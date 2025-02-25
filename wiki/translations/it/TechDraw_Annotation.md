---
 GuiCommand:
   Name: TechDraw Annotation
   Name/it: TechDraw Annotazione
   MenuLocation: TechDraw , Annotazioni , Inserisci annotazione
   Workbenches: TechDraw_Workbench/it
   SeeAlso: TechDraw_RichTextAnnotation/it
---

# TechDraw Annotation/it



## Descrizione

Lo strumento **TechDraw Annotazione** aggiunge un blocco di testo ad una pagina di disegno.

<img alt="" src=images/AnnotationSample.png  style="width:250px;"> 
*Annotazione nella pagina di disegno*



## Utilizzo

1.  Se nel documento sono presenti più pagine di disegno: facoltativamente attivare la pagina desiderata selezionandola nella [Vista ad albero](Tree_view/it.md).
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_Annotation.svg" width=16px> [Inserisci annotazione](TechDraw_Annotation/it.md)**.
    -   Selezionare l\'opzione **TechDraw → Annotazioni → <img src="images/TechDraw_Annotation.svg" width=16px> Inserisci annotazione** dal menu.
3.  Se nel documento sono presenti più pagine di disegno e non si ha ancora attivato una pagina, si apre la finestra di dialogo **Scelta pagina**:
    1.  Selezionare la pagina desiderata.
    2.  Premere il pulsante **OK**.
4.  Sulla pagina viene visualizzato un blocco di testo contenente *Default Text*.
5.  Utilizzare l\'[Editor delle proprietà](Property_editor/it.md) per modificare il testo.
6.  Facoltativamente trascinare l\'annotazione in una posizione diversa.

![](images/UpdateAnnotation.png ) 
*Modifica dell'annotazione tramite l'Editor delle proprietà*



## Note

-   Alcuni caratteri interferiscono con la rappresentazione interna del testo dell\'annotazione. Nello specifico, queste sono le virgolette doppie `"`, i simboli minori di `<` e maggiori di `>`; questi devono essere sostituiti da caratteri di escape HTML, ` &amp;quot;`, `&amp;lt;` e `&amp;gt;` rispettivamente. Vedere [Codifiche dei caratteri. in HTML](https://en.wikipedia.org/wiki/Character_encodings_in_HTML#HTML_character_references) per i dettagli.



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

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Il nuovo strumento Annotazione può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


```python
anno = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewAnnotation','TestAnno')
anno.Text = ['Different Text']
anno.TextStyle = 'Bold'
rc = page.addView(anno)
```





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Annotation/it
