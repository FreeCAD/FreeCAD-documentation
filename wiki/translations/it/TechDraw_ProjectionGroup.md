---
- GuiCommand:
   Name:TechDraw_ProjectionGroup
   Name/it:Gruppo di proiezioni
   MenuLocation:TechDraw - Gruppo di proiezioni
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


<div class="mw-translate-fuzzy">

1.  Selezionare uno o più oggetti, \"Corpo\" o \"Parte\", nella finestra 3D o nella vista ad albero. Se nel documento ci sono più pagine di disegno, è anche necessario selezionare la pagina desiderata nella struttura.
2.  Premere il pulsante **<img src="images/TechDraw_ProjectionGroup.svg" width=16px> [Gruppo di proiezioni](TechDraw_ProjectionGroup/it.md)**.
3.  Si apre una finestra in cui è possibile selezionare quali viste devono apparire, la scala del gruppo e altri parametri:


</div>

![](images/TaskProjGroup.png )


<div class="mw-translate-fuzzy">



*Finestra di dialogo delle azioni del gruppo di proiezioni. Il campo centrale indica la direzione corrente della vista con le percentuali degli assi x, y e z.*


</div>



## Proprietà

### Data


{{TitleProperty|Base}}

-    **Source|LinkList**: Links to the drawable objects to be depicted.

-    **XSource|XLinkList**: Links to the drawable objects in an external file.

-    **Anchor|Link**: The central view in the group. Normally the Front view.

-    **ProjectionType|Enumeration**: {{Value|First Angle}} or {{Value|Third Angle}}.

For the other properties in this group see [TechDraw View](TechDraw_View#Properties.md).


{{TitleProperty|Collection}}

-    **Views|LinkList**: Links to the views in this ProjectionGroup.


{{TitleProperty|Distribute}}

-    **Auto Distribute|Bool**: If `True`, space out individual views automatically. Use `False` to position manually.

-    **spacing X|Length**: Horizontal space between views when automatically positioned. Note that Scale and the size of other views in the group also influence the spacing.

-    **spacing Y|Length**: Vertical space between views when automatically positioned.

### View


{{TitleProperty|Base}}

See [TechDraw View](TechDraw_View#Properties.md).

## Notes

Le Proiezioni ereditano nel loro complesso X, Y, ScaleType, Scale e Rotation dalla vista di base.

Le singole viste all\'interno del gruppo ereditano tutte le proprietà della vista della parte, ma l\'oggetto ProjectionGroup controlla la scala di tutti i suoi membri viste.

La proprietà RotationVector delle singole viste all\'interno del gruppo è obsoleta a partire dalla versione 0.19. Utilizzare invece XDirection.

Notare che la casella centrale visualizza la direzione di proiezione corrente della vista principale. Non può essere utilizzata per cambiare la direzione.



## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>

A Projection Group can be created with [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
import FreeCAD as App

doc = App.ActiveDocument
cyl = doc.addObject("Part::Cylinder", "Cylinder")
doc.recompute()

page = doc.addObject("TechDraw::DrawPage", "Page")
template = doc.addObject("TechDraw::DrawSVGTemplate", "Template")
template.Template = App.getResourceDir() + "Mod/TechDraw/Templates/A4_LandscapeTD.svg"
page.Template = template

# Toggle the visibility of the page to ensure its width and height are updated (hack):
page.Visibility = False
page.Visibility = True

group = doc.addObject("TechDraw::DrawProjGroup", "ProjGroup")
page.addView(group)
group.Source = [cyl]
group.ProjectionType = "Third Angle"

front_view = group.addProjection("Front") # First projection will become the Anchor.
group.Anchor.Direction = (0, 1, 0)
group.Anchor.RotationVector = (1, 0, 0)

left_view = group.addProjection("Left")
top_view = group.addProjection("Top")

group.X = page.PageWidth / 2
group.Y = page.PageHeight / 2

doc.recompute()
```


<div class="mw-translate-fuzzy">

Nota di programmazione: Il Gruppo di proiezioni deve sempre essere aggiunto alla Pagina (ad esempio page.addView(group) prima di aggiungere delle proiezioni al Gruppo. Ciò consente al Gruppo di proiezioni di utilizzare i valori dei parametri predefiniti derivati dalla pagina genitore.


</div>


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ProjectionGroup/it
