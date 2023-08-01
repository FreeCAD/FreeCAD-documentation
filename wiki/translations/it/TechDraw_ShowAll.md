---
- GuiCommand:
   Name:TechDraw ShowAll
   Name/it:Mostra tutto
   MenuLocation:TechDraw → Mostra tutto
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Cambia aspetto delle linee](TechDraw_DecorateLine/it.md)
   Version:0.19
---

# TechDraw ShowAll/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Mostra tutto mostra o nasconde le linee invisibili in una vista. Notare che \"invisibile\" è uno stato cosmetico, da non confondere con le linee nascoste che sono costrutti geometrici.


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una vista in una pagina o nella struttura.
2.  Premere il pulsante **<img src="images/TechDraw_ShowAll.svg" width=16px> [Mostra tutto](TechDraw_ShowAll/it.md)**.
3.  Lo stato delle linee invisibili nella vista viene invertito.


</div>

## Notes

-   To make invisible lines permanently visible use <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [TechDraw DecorateLine](TechDraw_DecorateLine.md).



## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

L\'effetto dello strumento Mostra può essere replicato nelle [macro](macros/it.md) o nella console [Python](Python/it.md).


</div>


```python
v = App.ActiveDocument.View
vvo = v.ViewObject
vvo.ShowAllEdges = True
App.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ShowAll/it
