---
- GuiCommand:/it
   Name:TechDraw_ProjectionGroup
   Name/it:Gruppo di proiezioni
   MenuLocation:TechDraw → Gruppo di proiezioni
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   Shortcut:
   SeeAlso:[Vista](TechDraw_View/it.md), [Vista di sezione](TechDraw_SectionView/it.md)
   Version:
---

# TechDraw ProjectionGroup/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:24px;"> [Gruppo di proiezioni](TechDraw_ProjectionGroup/it.md) crea una [proiezione multivista](https://en.wikipedia.org/wiki/Multiview_projection) di uno o più oggetti 3D. È anche possibile includere le viste isometriche dei 4 angoli anteriori.


</div>


<div class="mw-translate-fuzzy">

Se si desidera produrre una sola vista, non conviene utilizzare Gruppo di proiezioni, meglio usare invece [Vista](TechDraw_View/it.md). Se non si desidera utilizzare il tradizionale modo di visualizzazione [primo](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#First-angle_projection) o [terzo angolo di proiezione](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#Third-angle_projection), è possibile utilizzare diverse volte \"Vista\" al posto di \"Gruppo di proiezioni\".


</div>

<img alt="" src=images/TechDraw_ProjGroup_example.png  style="width:400px;"> 
*Tre viste ortogonali e una vista isometrica di un oggetto solido*

## Utilizzo

1.  Selezionare uno o più oggetti, \"Corpo\" o \"Parte\", nella finestra 3D o nella vista ad albero. Se nel documento ci sono più pagine di disegno, è anche necessario selezionare la pagina desiderata nella struttura.
2.  Premere il pulsante **<img src="images/TechDraw_ProjectionGroup.svg" width=16px> [Gruppo di proiezioni](TechDraw_ProjectionGroup/it.md)**.
3.  Si apre una finestra in cui è possibile selezionare quali viste devono apparire, la scala del gruppo e altri parametri:

![](images/TaskProjGroup.png )


<div class="mw-translate-fuzzy">


*Finestra di dialogo delle azioni del gruppo di proiezioni. Il campo centrale indica la direzione corrente della vista con le percentuali degli assi x, y e z.*


</div>

Dopo aver creato un gruppo di proiezioni è possibile spostare il gruppo nel suo complesso trascinando la vista centrale. È inoltre possibile spostare le singole viste mediante trascinamento.

## Proprietà

-    **Anchor**: la vista centrale del gruppo. Normalmente è la vista frontale.

-    **ProjectionType**: \"Primo angolo\" o \"Terzo angolo\".

-    **AutoDistribute**: se è True (vero), spazia automaticamente le singole viste. Utilizzare false per posizionarle manualmente.

-    **spacingX**: lo spazio orizzontale tra le viste quando esse sono posizionate automaticamente.

-    **spacingY**: lo spazio verticale tra le viste quando esse sono posizionate automaticamente.

Le Proiezioni ereditano nel loro complesso X, Y, ScaleType, Scale e Rotation dalla vista di base.

Le singole viste all\'interno del gruppo ereditano tutte le proprietà della vista della parte, ma l\'oggetto ProjectionGroup controlla la scala di tutti i suoi membri viste.

La proprietà RotationVector delle singole viste all\'interno del gruppo è obsoleta a partire dalla versione 0.19. Utilizzare invece XDirection.

Notare che la casella centrale visualizza la direzione di proiezione corrente della vista principale. Non può essere utilizzata per cambiare la direzione.

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Proiezioni può essere usato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md). Uno script completo è disponibile nel codice sorgente in \"source-dir/src/Mod/TechDraw/TDTest/DProjGroupTest.py\".


</div>


```python
    #make a page
    print("making a page")
    page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
    FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
    FreeCAD.ActiveDocument.Template.Template = templateFileSpec
    FreeCAD.ActiveDocument.Page.Template = FreeCAD.ActiveDocument.Template

    #make projection group
    group = FreeCAD.ActiveDocument.addObject('TechDraw::DrawProjGroup','ProjGroup')
    rc = page.addView(group)
    group.Source = [fusion]

    #add Front(Anchor) view
    frontView = group.addProjection("Front")               ##need an Anchor

    #update group
    group.Anchor.Direction = FreeCAD.Vector(0,0,1)
    group.Anchor.RotationVector = FreeCAD.Vector(1,0,0)

    #add more projections
    leftView = group.addProjection("Left")
    topView = group.addProjection("Top")
    rightView = group.addProjection("Right")
    rearView = group.addProjection("Rear")
    BottomView = group.addProjection("Bottom")

    #remove a view from projection group
    iv = group.removeProjection("Left")

```


<div class="mw-translate-fuzzy">

Nota di programmazione: Il Gruppo di proiezioni deve sempre essere aggiunto alla Pagina (ad esempio page.addView(group) prima di aggiungere delle proiezioni al Gruppo. Ciò consente al Gruppo di proiezioni di utilizzare i valori dei parametri predefiniti derivati dalla pagina genitore.


</div>


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ProjectionGroup/it
