---
- GuiCommand:/it
   Name:TechDraw_SectionView
   Name/it:Vista di sezione
   MenuLocation:TechDraw → Vista di sezione
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Vista](TechDraw_View/it.md), [Gruppo di proiezioni](TechDraw_ProjectionGroup/it.md)
---

# TechDraw SectionView/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Vista di sezione crea una vista in sezione trasversale basata sulla vista di una parte esistente.


</div>

<img alt="" src=images/TechDraw_Section_example.png  style="width:250px;"> 
*Sezione di una vista già posizionata, che mostra i fori interni e la superficie di taglio ombreggiata*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una vista di una parte nella finestra o nella struttura 3D.
2.  Se nel documento sono presenti più pagine di disegno, è necessario selezionare anche la pagina desiderata nella struttura.
3.  Premere il pulsante **<img src="images/TechDraw_SectionView.svg" width=16px> [Vista di sezione](TechDraw_SectionView/it.md)**.
4.  Si apre una finestra di dialogo che aiuta a calcolare le varie proprietà della sezione. La finestra di dialogo calcola ragionevoli punti di partenza per SectionNormal e Direzione della vista, ma per esigenze speciali questi possono essere modificati dopo la creazione.
5.  Se si commette un errore o si cambia idea durante l\'impostazione dei parametri della sezione, premere il pulsante **Reset** e si può ricominciare da capo.


</div>

![](images/TechDraw_Section_Taskview.png ) 
*La scheda Azioni per definire il taglio in sezione di una vista*

## Properties Section View 

See also [TechDraw View](TechDraw_View#Properties.md).

### Dati


{{TitleProperty|Cut Operation}}

-    **Fuse Before Cut|Bool**: Fuse the source shapes before performing the section cut.

-    **Trim After Cut|Bool**: Additionally trim the resulting shape after the section cut to remove any unwanted pieces.


{{TitleProperty|Cut Surface Format}}


<div class="mw-translate-fuzzy">

#### Formato della superficie della sezione 

-    **Cut Surface Display**: Aspetto della superficie tagliata. Opzioni:

    -   *Hide* Nasconde la superficie tagliata, visualizza solo il contorno.
    -   *Color*: Colora la superficie tagliata usando l\'impostazione di **Colore della superficie tagliata** nelle [preferenze di TechDraw](TechDraw_Preferences/it.md).
    -   *SvgHatch*: Tratteggia la sezione tagliata usando un [tratteggio](TechDraw_Hatch/it.md)
    -   *PatHatch*: Tratteggia la sezione tagliata usando un [tratteggio geometrico](TechDraw_GeometricHatch/it.md)

-    **File Hatch Pattern**: Percorso completo del file di modello di tratteggio SVG.

-    **File Geom Pattern**: Percorso completo per il file del modello PAT.

-    **Svg Included**: Percorso completo del file di modello di tratteggio SVG incluso.

-    **Pat Included**: Percorso completo del file del modello PAT incluso.

-    **Name Geom Pattern**: Nome del modello PAT da utilizzare (ignorato per il parametro *SvgHatch* di **Cut Surface Display**).


</div>


{{TitleProperty|Section}}


<div class="mw-translate-fuzzy">

#### Sezione

-    **Base View**: la vista della parte su cui si basa questa Vista in sezione.

-    **Section Normal**: un vettore che descrive la direzione normale al piano di taglio.

-    **Section Origin**: un vettore che descrive un punto sul piano di taglio. Tipicamente il baricentro della parte originale.

-    **Fuse Before Cut**: fondere le forme sorgente prima di eseguire il taglio di sezione.


</div>

### Vista


{{TitleProperty|Cut Surface}}


<div class="mw-translate-fuzzy">

#### Superficie della sezione 

-    **Cut Surface Color**: tinta unita per l\'evidenziazione della superficie. Usato se **Cut Surface Display** è impostata su *Color*.


</div>


{{TitleProperty|Surface Hatch}}


<div class="mw-translate-fuzzy">

#### Tratteggio della superficie 

-    **Hatch Color**: Colore per le linee di tratteggio della superficie.

-    **Weight Pattern**: Spessore di linea per le linee di tratteggio della superficie.


</div>

## Properties Base View 


<div class="mw-translate-fuzzy">

Una vista in sezione eredita tutte le proprietà applicabili della vista specificata come **BaseView**. Nelle proprietà della vista è possibile modificare l\'aspetto della linea di sezione:


</div>


<div class="mw-translate-fuzzy">

-    **Section Line Color**: colore per la linea di sezione.

-    **Section Line Style**: stile per la linea di sezione.


</div>

Le impostazioni predefinite per questi parametri sono impostate tramite le impostazioni **Linea di sezione** e **Stile linea di sezione** nelle [preferenze di TechDraw](TechDraw_Preferences/it.md).

## Note


<div class="mw-translate-fuzzy">

-   **Section Line Format**: sono supportati sia il tradizionale formato della linea di sezione (come illustrato sopra), sia il \"metodo della freccia di riferimento\". Questa opzione è controllata dall\'impostazione della Preferenza \"Mod/TechDraw/Format/SectionFormat\" (vedere [Modifica parametri](Std_DlgParameter/it.md)). 0 per linea tradizionale, 1 per metodo freccia di riferimento.
-   **CutSurfaceDisplay**: la superficie tagliata può essere nascosta, colorata in tinta unita, tratteggiata utilizzando un modello Svg (impostazione predefinita) o tratteggiata utilizzando un modello PAT. Vedere [Tipi di tratteggio](TechDraw_Hatching/it.md).
-   **FuseBeforeCut**: l\'operazione di sezione a volte non riesce a tagliare le forme di origine. Se FuseBeforeCut è true, le forme di origine vengono unite in un\'unica forma prima di tentare l\'operazione di sezione. In caso di problemi con l\'operazione di sezione, provare a invertire questo valore.


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Vista di sezione può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
doc = FreeCAD.ActiveDocument
box = doc.Box
page = doc.Page

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = box
view.Direction = (0.0, 0.0, 1.0)

section = doc.addObject("TechDraw::DrawViewSection", "Section")
page.addView(section)
section.Source = box
section.BaseView = view
section.Direction = (0.0, 1.0, 0.0)
section.SectionNormal = (-1.0, 0.0, 0.0)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SectionView/it
