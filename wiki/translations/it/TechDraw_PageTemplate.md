---
- GuiCommand:/it
   Name:TechDraw_PageTemplate
   Name/it:Nuovo disegno da modello
   MenuLocation:TechDraw → Nuovo disegno da modello
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Nuova pagina standard](TechDraw_PageDefault/it.md), [Modelli di squadrature](TechDraw_Templates/it.md)
---

# TechDraw PageTemplate/it


</div>

## Descrizione

Lo strumento Nuova pagina da modello crea una nuova pagina utilizzando il file di un modello selezionato in una finestra di dialogo.


<div class="mw-translate-fuzzy">

La directory di partenza per il dialogo può essere specificata nelle [Preferenze di TechDraw](TechDraw_Preferences/it.md)


</div>

<img alt="" src=images/A4_Landscape_ISO7200_Pep.svg  style="width:400px;">



*Uno dei modelli che viene fornito con TechDraw: A4 ISO 7200_Pep, pagina con orientamento orizzontale, e con campi di testo modificabili*

## Utilizzo


<div class="mw-translate-fuzzy">

-   Premere il pulsante **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Nuovo disegno da modello](TechDraw_PageTemplate/it.md)**.


</div>

## Proprietà

See [TechDraw PageDefault](TechDraw_PageDefault#Properties.md).

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Nuovo disegno da modello può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
templateFileSpec = QtGui.QFileDialog.getOpenFileName(self.baseWidget,
                                                     dialogCaption, 
                                                     dialogDir,
                                                     dialogFilter)
page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
template = FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
template.Template = templateFileSpec
page.Template = FreeCAD.ActiveDocument.Template
```

-   Crea una nuova pagina nel documento corrente

### Campi di testo modificabili 


<div class="mw-translate-fuzzy">


**Per ulteriori informazioni sulla creazione di modelli vedere anche:**

[Modelli di squadrature](TechDraw_Templates/it.md).


</div>

Per modificare a livello di programmazione i campi di testo editabili in un modello di pagina vedere le informazioni in [Nuova pagina standard](TechDraw_PageDefault/it.md).


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageTemplate/it
