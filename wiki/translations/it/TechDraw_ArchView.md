---
 GuiCommand:
   Name: TechDraw_ArchView
   Name/it: TechDraw Vista di Arch
   MenuLocation: TechDraw , Viste da altri ambienti di lavoro , Inserisci Oggetto ambiente BIM
   Workbenches: TechDraw_Workbench/it, BIM_Workbench/it
   SeeAlso:  Arch SectionPlane/it
---

# TechDraw ArchView/it



## Descrizione

Lo strumento **TechDraw Vista di Arch** inserisce una Vista di Arch, una vista di un <img alt="" src=images/Arch_SectionPlane.svg  style="width:16px;"> [Piano di sezione Arch](Arch_SectionPlane/it.md), su una [Pagina TechDraw](TechDraw_PageDefault/it.md).


{{Version/it|1.0}}

: lo strumento [TechDraw Vista](TechDraw_View.md) può anche creare una vista di Arch.

<img alt="" src=images/TechDraw_Arch_example.jpg  style="width:500px;">



## Utilizzo

1.  Selezionare un piano di sezione di Arch nella [Vista 3D](3D_view/it.md) o nella [Vista albero](Tree_view/it.md).
2.  Se nel documento sono presenti più pagine di disegno: facoltativamente aggiungere la pagina desiderata alla selezione selezionandola nella [Vista ad albero](Tree_view/it.md).
    -   Selezionare l\'opzione **TechDraw → Viste da altri ambienti di lavoro → <img src="images/TechDraw_ArchView.svg" width=16px> Inserisci oggetto Ambiente BIM** dal menu.
3.  Se nel documento sono presenti più pagine di disegno e se nessuna pagina è visualizzata nell\'[Area della vista principale](Main_view_area/it.md) e non si ha ancora selezionato una pagina, si apre la finestra di dialogo **Scelta pagina**:
    1.  Selezionare la pagina desiderata.
    2.  Premere il pulsante **OK**.



## Opzioni

-   La Vista di Arch è renderizzata dall\'[Ambiente BIM](BIM_Workbench/it.md).
-   [Quotature Draft](Draft_Snap_Dimensions/it.md), [Testi Draft](Draft_Text/it.md) e qualsiasi altro oggetto 2D (Sketch o Draft) considerato dal piano di sezione viene reso \"così com\'è\" (senza intersezioni o linee nascoste) sopra la geometria solida
-   Il volume di [Arch Spazio](Arch_Space/it.md) non viene renderizzato, verrà renderizzata solo l\'etichetta
-   Le linee di taglio, le linee proiettate (se la proprietà Mostra nascosto è impostata su True) e le linee 2D sopra possono essere renderizzate con larghezze di linea diverse. Questo può essere configurato nelle preferenze di Arch.
-   Vista di Arch ha due modalità di rendering:
    -   Wireframe, che utilizza gli algoritmi OpenCasCade di [TechDraw](TechDraw_Workbench/it.md), è veloce e produce solo linee (non è possibile il riempimento della faccia)
    -   Solido, che si basa sull\'[Painter\'s algorithm](https://en.wikipedia.org/wiki/Painter%27s_algorithm) ed è in grado di rendere i volti riempiti con il colore della loro forma. Tuttavia, è molto più lento e può fallire in molte situazioni.

:   L\'immagine seguente illustra la differenza tra le due modalità di rendering:





:   ![](images/TechDraw_Arch_rendering.jpg )

-   Per le [Tubazioni Arch](Arch_Pipe/it.md) sono renderizzate solo le linee di base, ma non il volume dei tubi:

:   ![](images/TechDraw_Arch_piping.jpg )



## Note

La Vista di Arch viene renderizzata all\'interno dell\'ambiente [BIM](BIM_Workbench/it.md), pertanto TechDraw ha un controllo limitato sul suo aspetto. Potrebbe essere necessario apportare modifiche all\'interno di Arch per ottenere la rappresentazione desiderata.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Una Vista Arch, formalmente un oggetto {{Incode|TechDraw::DrawViewArch}}, ha le [proprietà](TechDraw_View#Properties_Part_View.md) comuni a tutti i tipi di Vista. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Arch view}}

-    **Source|Link**: l\'oggetto piano di sezione da visualizzare.

-    **All On|Bool**: se gli oggetti nascosti devono essere mostrati o meno. Se `False`, viene eseguito il rendering solo degli oggetti visibili nella vista 3D.

-    **Render Mode|Enumeration**: la modalità di rendering da utilizzare, {{Value|Solid}} o {{Value|Wireframe}}.

-    **Fill Spaces|Bool**: Se `True`, gli Spazi Arch vengono visualizzati come un\'area colorata.

-    **Show Hidden|Bool**: se la geometria nascosta (la parte della geometria che si trova dietro il piano di sezione) viene mostrata o meno. Verrà visualizzato in una linea tratteggiata, che può essere configurata nelle preferenze di Arch.

-    **Show Fill|Bool**: se le aree tagliate devono essere riempite con un colore grigio o meno.

-    **Line Width|Float|Float**: la larghezza delle linee principali. I rapporti delle linee di taglio e delle larghezze delle linee proiettate/2D possono essere configurati nelle preferenze di Arch.

-    **Font Size|Float**: la dimensione di tutti i testi che appaiono in questa vista.

-    **Cut Line Width|Float**: larghezza delle linee di taglio in questa vista.

-    **Join Arch|Bool**: Se `True`, i muri e le strutture verranno fusi dal materiale.

-    **Line Spacing|Float**: la spaziatura tra le righe da utilizzare per i testi su più righe. {{Version/it|1.0}}


{{TitleProperty|Drawing view}}

-    **Symbol|String|Hidden**: il codice SVG che definisce questo simbolo.

-    **Editable Texts|StringList**: valori di sostituzione per le stringhe modificabili in questo simbolo.

-    **Owner|Link**: feature a cui è associato questo simbolo. {{Version/it|1.0}}



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Vista di Arch può essere utilizzato nelle [macro](Macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewArch','TestArch')
dv.Source = mySectionPlane
rc = page.addView(dv)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ArchView/it
