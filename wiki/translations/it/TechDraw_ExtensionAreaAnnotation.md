---
 GuiCommand:
   Name: TechDraw ExtensionAreaAnnotation
   Name/it: TechDraw Annotazione calcolo Area
   MenuLocation: TechDraw , Estensioni: Attributi/Modifiche , Calcola l'area delle facce selezionate
   Workbenches: TechDraw_Workbench/it
   Shortcut: 
   Version: 0.20
   SeeAlso: TechDraw_AreaDimension
---

# TechDraw ExtensionAreaAnnotation/it



## Descrizione

Lo strumento **TechDraw Annotazione calcolo Area** calcola l\'area delle facce selezionate e inserisce un\'annotazione dell\'area.

<img alt="" src=images/TechDraw_ExtensionAreaAnnotationExample.png  style="width:400px;"> 
*A destra l'annotazione dell'area inserita*



## Utilizzo

1.  Selezionare uno o più facce.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_ExtensionAreaAnnotation.svg" width=16px> [Calcola l'area delle facce selezionate](TechDraw_ExtensionAreaAnnotation/it.md)**.
    -   Seleziona l\'opzione **TechDraw → Estensioni: Attributi/Modifiche → <img src="images/TechDraw_ExtensionAreaAnnotation.svg" width=16px> Calcola l'area delle facce selezionate** dal menu.
3.  Viene calcolata l\'area totale delle facce e viene inserita un\'annotazione dell\'area.



## Limitazioni

-    {{VersionMinus/it|0.21}}: lo strumento non può gestire facce con bordi curvi.

-   I fori (isole) nella faccia selezionata vengono ignorati. Questo [post sul forum](https://forum.freecad.org/viewtopic.php?p=783325#p783325) mostra una soluzione alternativa. E\' possibile anche utilizzare [TechDraw Quotatura Area](TechDraw_AreaDimension/it.md) ma si deve poi impostare correttamente la proprietà **References 3D** della quota creata.

-   L\'area calcolata non è collegata dinamicamente alla faccia. Se cambia l\'area della faccia il testo non viene aggiornato.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionAreaAnnotation/it
