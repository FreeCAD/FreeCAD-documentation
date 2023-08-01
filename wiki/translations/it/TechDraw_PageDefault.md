---
- GuiCommand:
   Name: TechDraw_PageDefault
   Name/it: Nuovo disegno standard
   MenuLocation: TechDraw - Nuovo disegno standard
   Workbenches: [TechDraw](TechDraw_Workbench/it.md)
   SeeAlso: [Nuovo disegno da modello](TechDraw_PageTemplate/it.md), [Modelli di squadrature](TechDraw_Templates/it.md)
---

# TechDraw PageDefault/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Nuovo disegno standard crea una nuova pagina utilizzando il file modello specificato nelle [Preferenze](TechDraw_Preferences/it.md).


</div>

<img alt="" src=images/A4_LandscapeTD.svg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Modello predefinito fornito con TechDraw: pagina A4 con orientamento orizzontale, con i campi di testo modificabili*


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

-   Premere il pulsante **<img src="images/TechDraw_PageDefault.svg" width=16px> [Nuovo disegno standard](TechDraw_PageDefault.md)**. (Deve esistere un documento attivo.)


</div>



## Note


<div class="mw-translate-fuzzy">

-   Se una pagina è contrassegnata come \"non tenere aggiornata\" tramite la Proprietà KeepUpdated o dalle impostazione nelle Preferenze, le modifiche apportate nel modello 3D vengono ignorate. Si potrebbero notare delle anomalie nell\'aspetto della Pagina (geometria mancante, valori di Dimensione mancanti, ecc.). Questi errori possono essere corretti aggiornando la Pagina.

La pagina ha questa icona <img alt="" src=images/TechDraw_Tree_Page_Unsync.png  style="width:32px;"> nell\'albero mentre l\'aggiornamento è sospeso. Questa impostazione influisce anche sul processo di avvio. Se la pagina è contrassegnata come \"non tenere aggiornata\", all\'avvio del programma essa non viene disegnata.


</div>


<div class="mw-translate-fuzzy">

Se il modello predefinito non è specificato nel file di configurazione utente `user.cfg`, lo strumento prova


</div>


:   
    
```python
    $INSTALL_DIR/Mod/TechDraw/Templates/A4_LandscapeTD.svg
    
```
    


<div class="mw-translate-fuzzy">

Dove `$INSTALL_DIR` è la directory in cui è stato installato FreeCAD, per esempio


</div>


:   
    
```python
    /usr/share/freecad/Mod/TechDraw/Templates/A4_LandscapeTD.svg
    
```
    



## Proprietà

### Data


{{TitleProperty|Base}}

-    **Projection Type**: Default projection type (First or Third Angle) for this Page.


{{TitleProperty|Page}}


<div class="mw-translate-fuzzy">

-    **Projection Type**: tipo predefinito di proiezione da usare (primo o terzo angolo) per questa pagina.

-    **KeepUpdated**: se false, la pagina non viene aggiornata con le modifiche al modello 3D. Utile per i disegni complicati o lenti. Vedere le note.

-    **Template**: un link alla pagina dei [Modelli di squadrature](TechDraw_Templates/it.md).

-    **Views**: un elenco di collegamenti alle viste su questa pagina.

-    **Scale**: scala predefinita da usare per le viste in questa pagina.


</div>

### View


{{TitleProperty|Grid}}

-    **Show Grid**: Show a grid over this Page. <small>(v0.20)</small> 

-    **Grid Spacing**: Distance between grid lines. <small>(v0.20)</small> 



## Script

See [TechDraw PageTemplate](TechDraw_PageTemplate#Scripting.md).


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageDefault/it
