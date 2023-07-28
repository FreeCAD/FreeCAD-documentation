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


<div class="mw-translate-fuzzy">

Lo strumento Nuova pagina da modello crea una nuova pagina utilizzando il file di un modello selezionato in una finestra di dialogo.


</div>


<div class="mw-translate-fuzzy">

La directory di partenza per il dialogo può essere specificata nelle [Preferenze di TechDraw](TechDraw_Preferences/it.md)


</div>

<img alt="" src=images/A4_Landscape_ISO7200_Pep.svg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Uno dei modelli che viene fornito con TechDraw: A4 ISO 7200_Pep, pagina con orientamento orizzontale, e con campi di testo modificabili*


</div>



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

A Page based on a selected template can be created with [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
import FreeCAD as App
from PySide import QtGui

doc = App.ActiveDocument
default_dir = App.getResourceDir() + "Mod/TechDraw/Templates"
param = App.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
template_dir = param.GetString("TemplateDir", default_dir)

template_file = QtGui.QFileDialog.getOpenFileName(QtGui.QApplication.activeWindow(),
                                                  "Select a Template File", 
                                                  template_dir,
                                                  "Template (*.svg)")
                                                  
page = doc.addObject("TechDraw::DrawPage", "Page")
template = doc.addObject("TechDraw::DrawSVGTemplate", "Template")
template.Template = template_file[0]
page.Template = template

doc.recompute()
```



### Campi di testo modificabili 


<div class="mw-translate-fuzzy">


**Per ulteriori informazioni sulla creazione di modelli vedere anche:**

[Modelli di squadrature](TechDraw_Templates/it.md).


</div>

Once a new page has been created, its `Template` attribute holds an `EditableTexts` dictionary with the name of the editable fields (keys) and their textual values. Copy this dictionary to a variable, make changes, and then re-assign the dictionary to the `EditableTexts` attribute to see the changes.


```python
page = FreeCAD.ActiveDocument.Page
texts = page.Template.EditableTexts

for key, value in texts.items():
    print("{0} = {1}".format(key, value))

texts["FC-Title"] = "The title of my page"
page.Template.EditableTexts = texts
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageTemplate/it
