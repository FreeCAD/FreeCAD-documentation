---
 GuiCommand:
   Name: TechDraw PageDefault
   Name/it: TechDraw Pagina predefinita
   MenuLocation: TechDraw , Inserisci Pagina predefinita
   Workbenches: TechDraw_Workbench/it
   SeeAlso: TechDraw_PageTemplate/it, TechDraw_Templates/it
---

# TechDraw PageDefault/it



## Descrizione

Lo strumento **TechDraw Pagina predefinita** crea una nuova Pagina utilizzando il file modello specificato nelle [Preferenze](TechDraw_Preferences/it.md).

<img alt="" src=images/A4_LandscapeTD.svg  style="width:400px;"> 
*Modello predefinito fornito con TechDraw: A4_LandscapeTD.svg*



## Utilizzo

1.  Deve esistere un documento attivo.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_PageDefault.svg" width=16px> [Inserisci Pagina predefinita](TechDraw_PageDefault/it.md)**.
    -   Seleziona l\'opzione **TechDraw → Pagina → <img src="images/TechDraw_PageDefault.svg" width=16px> Inserisci Pagina predefinita** dal menu.



## Note

-   Se una Pagina è contrassegnata come \"non mantenere aggiornata\" tramite la sua proprietà **Keep Updated**, tramite l\'opzione **Toggle Keep Updated** dal menu contestuale della finestra o dall\'impostazione nella Preferenze, ignorerà le modifiche nel modello 3D. Si potrebbero notare anomalie (geometria mancante, valori di dimensione mancanti, ecc.) nell\'aspetto della Pagina. Queste verranno corrette automaticamente una volta aggiornata la pagina con lo strumento [Ridisegna pagina](TechDraw_RedrawPage/it.md). La Pagina avrà questa icona <img alt="" src=images/TechDraw_Tree_Page_Unsync.svg  style="width:24px;"> nella [Vista ad albero](Tree_view/it.md) mentre l\'aggiornamento è sospeso. Questa impostazione influisce anche sul processo di avvio. Se una Pagina è contrassegnata come \"non mantenere aggiornata\" non verrà disegnata all\'avvio del programma.

-   Se il modello predefinito non è specificato nel file di configurazione utente `user.cfg`, lo strumento provaː

:   
    
```python
    $INSTALL_DIR/Mod/TechDraw/Templates/A4_LandscapeTD.svg
    
```
    

ː Dove `$INSTALL_DIR` è la directory in cui è stato installato FreeCAD, per esempioː

:   
    
```python
    /usr/share/freecad/Mod/TechDraw/Templates/A4_LandscapeTD.svg
    
```
    



## Proprietà



### Dati


{{TitleProperty|Base}}

-    **Projection Type**: tipo di proiezione predefinito (Primo o Terzo angolo) per questa Pagina.


{{TitleProperty|Page}}

-    **Keep Updated**: se false, la Pagina non viene aggiornata con le modifiche al modello 3D. Utile per disegni complicati/lenti. Vedere [Note](#Note.md).

-    **Template**: un collegamento all\'oggetto [Template](TechDraw_Templates/it.md) di questa pagina.

-    **Views**: un elenco di collegamenti alle visualizzazioni in questa Pagina.

-    **Scale**: scala predefinita per le visualizzazioni in questa Pagina.

-    **Next Balloon Index**: numerazione automatica per le Pallinature.



### Vista


{{TitleProperty|Grid}}

-    **Show Grid**: Mostra una griglia su questa Pagina.

-    **Grid Spacing**: distanza tra le linee della griglia.



## Script

Vedere [TechDraw PageTemplate](TechDraw_PageTemplate/it#Scripting.md).





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageDefault/it
