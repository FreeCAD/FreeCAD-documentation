---
- GuiCommand:/it
   Name:TechDraw_ArchView
   Name/it:Vista di Arch
   MenuLocation:TechDraw → Vista di Arch
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Arch](Arch_Workbench/it.md), [Piano di sezione di Arch](Arch_SectionPlane/it.md)
---

# TechDraw ArchView/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Vista di Arch inserisce una vista di un **<img src="images/Arch_SectionPlane.svg" width=16px> [Piano di sezione di Arch](Arch_SectionPlane/it.md)** in una [pagina di TechDraw](TechDraw_PageDefault/it.md).


</div>

![](images/TechDraw_Arch_example.jpg )

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una Sezione di Arch nella finestra 3D o nella vista a albero.
2.  Se nel documento ci sono più pagine di disegno, è necessario selezionare anche la pagina desiderata nella struttura.
3.  Premere il pulsante **<img src="images/TechDraw_ArchView.svg" width=24px> [Vista di Arch](TechDraw_ArchView/it.md)
**
4.  Nella pagina appare una vista degli oggetti visti dal piano di sezione.


</div>

### Limitazioni


<div class="mw-translate-fuzzy">

Poiché la Vista di Arch è resa all\'interno del modulo [Arch](Arch_Workbench/it.md), TechDraw ha un controllo limitato sul suo aspetto. Potrebbe essere necessario apportare delle modifiche all\'interno di Arch per ottenere la rappresentazione desiderata.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

-   La Vista di Arch è resa dall\'ambiente [Arch](Arch_Workbench/it.md), allo stesso modo di come avveniva in [Drawing](Drawing_Workbench/it.md). Vedere le note.
-   [Dimensioni](Draft_Snap_Dimensions/it.md), [Testi](Draft_Text/it.md) e qualsiasi altro oggetto 2D (Sketch o Draft) considerato dal piano di sezione viene reso \"così com\'è\" (senza nessuna intersezione o linee nascoste) sopra la geometria solida.
-   Il volume degli [Spazi](Arch_Space/it.md) non viene reso, viene resa solo l\'etichetta.
-   Le linee di taglio, le linee proiettate (se Mostra proprietà nascosta è impostata su Vero) e le linee 2D di cui sopra possono essere rese con larghezze di linea diverse. Questo può essere configurato nelle preferenze di Arch.
-   La Vista di Arch ha due modalità di rendering: Wireframe, che utilizza gli algoritmi OpenCasCade di [Drawing](Drawing_Workbench/it.md), è veloce e produce solo linee (non è possibile riempire la faccia) e Solid, che si basa sull\'[algoritmo di Painter](https://en.wikipedia.org/wiki/Painter%27s_algorithm), ed è in grado di riprodurre facce riempite con il colore della loro forma. Tuttavia, è molto più lento e può fallire in molte situazioni. L\'immagine sotto mostra la differenza tra le due modalità di rendering:


</div>

![](images/TechDraw_Arch_rendering.jpg )


<div class="mw-translate-fuzzy">

-   Per le [Tubazioni](Arch_Pipe/it.md) sono rese solo le linee di base, ma non il volume dei tubi:


</div>

![](images/TechDraw_Arch_piping.jpg )

## Proprietà


<div class="mw-translate-fuzzy">

-    **Source**: L\'oggetto piano di sezione da visualizzare.

-    **All On**: Se gli oggetti nascosti devono essere mostrati o meno. Se False, vengono visualizzati solo gli oggetti visibili nella vista 3D.

-    **Render Mode**: La modalità di rendering da utilizzare, Solido o Wireframe.

-    **Show Hidden**: Se la geometria nascosta (la parte della geometria che si trova dietro il piano di sezione) viene mostrata o meno. Verrà eseguito il rendering in linea tratteggiata, che può essere configurato nelle preferenze di Arch.

-    **Show Fill**: Se le aree tagliate devono essere riempite con un colore grigio o no.

-    **Line Width**: La larghezza delle linee principali. La larghezza delle linee di taglio e delle linee 2D proiettate possono essere configurate nelle preferenze di Arch.

-    **Font Size**: La dimensione di tutti i testi che appaiono in questa vista.


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento New Arch può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewArch','TestArch')
dv.Source = mySectionPlane
rc = page.addView(dv)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ArchView/it
