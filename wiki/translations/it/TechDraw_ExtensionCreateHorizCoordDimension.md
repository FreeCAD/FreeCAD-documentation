---
 GuiCommand:
   Name: TechDraw ExtensionCreateHorizCoordDimension
   Name/it: TechDraw Quote in Parallelo Orizzontali
   MenuLocation: TechDraw , Estensioni: Quotatura , Crea Quote in Parallelo Orizzontali
   Workbenches: TechDraw_Workbench/it
   Shortcut: 
   Version: 0.20
   SeeAlso: TechDraw_ExtensionCreateVertCoordDimension, TechDraw_ExtensionCreateObliqueCoordDimension/it
---

# TechDraw ExtensionCreateHorizCoordDimension/it



## Descrizione

Lo strumento **TechDraw Crea Quote in Parallelo Orizzontali** crea quote in parallelo orizzontali: più quote equidistanti a partire dalla stessa linea di base.

<img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimensionExample.png  style="width:400px;"> 
*A destra le quote create*



## Utilizzo

1.  Facoltativamente, specificare la spaziatura in parallelo con lo strumento <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width:16px;"> [TechDraw Seleziona attributi linea](TechDraw_ExtensionSelectLineAttributes/it.md).
2.  Selezionare tre o più vertici.
3.  L\'ordine di selezione dei primi due vertici determina la posizione della linea di base. Se il vertice selezionato per primo è a sinistra del secondo, la linea di base viene creata sul vertice più a sinistra, altrimenti viene creata sul vertice più a destra.
4.  Esistono diversi modi per richiamare lo strumento:
    -   
        {{Version/it|1.0}}
        
        : Se la [preferenza](TechDraw_Preferences/it#Dimensions.md) degli **Strumenti di quotatura** è impostata su {{Value|Strumento singolo}} (predefinito): premere la freccia giù a destra del pulsante **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** e selezionare il pulsante **<img src="images/TechDraw_ExtensionCreateHorizCoordDimension.svg" width=16px> Crea Quote in Parallelo Orizzontali** dal menu a discesa.

    -   Se questa preferenza ha un valore diverso (e in {{VersionMinus/it|0.21}}): premere il pulsante **<img src="images/TechDraw_ExtensionCreateHorizCoordDimension.svg" width=16px> [Crea Quote in Parallelo Orizzontali](TechDraw_ExtensionCreateHorizCoordDimension/it.md)**.

    -   Selezionare l\'opzione **TechDraw → Estensioni: Quotatura → <img src="images/TechDraw_ExtensionCreateHorizCoordDimension.svg" width=16px> Crea Quote in Parallelo Orizzontali** dal menu.
5.  Vengono create le quote in parallelo con testi di quota centrati.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionCreateHorizCoordDimension/it
