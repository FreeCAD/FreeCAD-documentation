---
- GuiCommand:/it
   Name:TechDraw_PageDefault
   Name/it:Nuovo disegno standard
   MenuLocation:TechDraw → Nuovo disegno standard
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Nuovo disegno da modello](TechDraw_PageTemplate/it.md), [Modelli di squadrature](TechDraw_Templates/it.md)
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Nuovo disegno standard crea una nuova pagina utilizzando il file modello specificato nelle [Preferenze](TechDraw_Preferences/it.md).


</div>

<img alt="" src=images/A4_LandscapeTD.svg  style="width:400px;"> 
*Modello predefinito fornito con TechDraw: pagina A4 con orientamento orizzontale, con i campi di testo modificabili*

## Utilizzo


<div class="mw-translate-fuzzy">

-   Premere il pulsante **<img src="images/TechDraw_PageDefault.svg" width=16px> [Nuovo disegno standard](TechDraw_PageDefault.md)**. (Deve esistere un documento attivo.)


</div>

## Note


<div class="mw-translate-fuzzy">

-   Se una pagina è contrassegnata come \"non tenere aggiornata\" tramite la Proprietà KeepUpdated o dalle impostazione nelle Preferenze, le modifiche apportate nel modello 3D vengono ignorate. Si potrebbero notare delle anomalie nell\'aspetto della Pagina (geometria mancante, valori di Dimensione mancanti, ecc.). Questi errori possono essere corretti aggiornando la Pagina.

La pagina ha questa icona <img alt="" src=images/TechDraw_Tree_Page_Unsync.png  style="width:32px;"> nell\'albero mentre l\'aggiornamento è sospeso. Questa impostazione influisce anche sul processo di avvio. Se la pagina è contrassegnata come \"non tenere aggiornata\", all\'avvio del programma essa non viene disegnata.


</div>

Se il modello predefinito non è specificato nel file di configurazione utente `user.cfg`, lo strumento prova 
```python
$INSTALL_DIR/Mod/TechDraw/Templates/A4_LandscapeTD.svg
```

Dove `$INSTALL_DIR` è la directory in cui è stato installato FreeCAD, per esempio 
```python
/usr/share/freecad/Mod/TechDraw/Templates/A4_LandscapeTD.svg
```

## Proprietà


<div class="mw-translate-fuzzy">

-    **Projection Type**: tipo predefinito di proiezione da usare (primo o terzo angolo) per questa pagina.

-    **KeepUpdated**: se false, la pagina non viene aggiornata con le modifiche al modello 3D. Utile per i disegni complicati o lenti. Vedere le note.

-    **Template**: un link alla pagina dei [Modelli di squadrature](TechDraw_Templates/it.md).

-    **Views**: un elenco di collegamenti alle viste su questa pagina.

-    **Scale**: scala predefinita da usare per le viste in questa pagina.


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento New Default può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
template = FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
template.Template = templateFileSpec
page.Template = FreeCAD.ActiveDocument.Template
```

-   Crea una nuova pagina nel documento corrente

### Campi di testo modificabili {#campi_di_testo_modificabili}


<div class="mw-translate-fuzzy">


**Per ulteriori informazioni sulla creazione di modelli vedere anche:**

[Modelli di squadrature](TechDraw_Templates/it.md).


</div>

Una volta creata una nuova pagina, il suo attributo `Template` contiene un dizionario `EditableTexts` con il nome dei campi modificabili (chiavi) e i loro valori testuali. Copiare questo dizionario in una variabile, apportare le modifiche, quindi riassegnare il dizionario all\'attributo `EditableTexts` per vedere le modifiche.


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
