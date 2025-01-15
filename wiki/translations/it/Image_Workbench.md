# Image Workbench/it
**L''''Ambiente Image''' non è più incluso dopo la versione 0.20.<br>
La sua funzionalità è stata integrata in [Menu di base](Std_Base/it.md). Vedere [Importa](Std_Import/it.md) e [Std ViewLoadImage](Std_ViewLoadImage.md).**

<img alt="L\'icona dell\'ambiente Image" src=images/Workbench_Image.svg  style="width:128px;">






## Introduzione

L\'[Ambiente Image](Image_Workbench/it.md) <img alt="" src=images/Workbench_Image.svg  style="width:24px;"> gestisce diversi tipi di immagini [bitmap](bitmap/it.md), e permette di aprirle in FreeCAD.



## Strumenti

-   <img alt="" src=images/Image_Open.svg  style="width:32px;"> [Apri\...](Image_Open/it.md): apre un\'immagine in una nuova finestra.
-   <img alt="" src=images/Image_CreateImagePlane.svg  style="width:32px;"> [Importa immagine\...](Image_CreateImagePlane/it.md): importa un\'immagine su un piano nella vista 3D.
-   <img alt="" src=images/Image_Scaling.svg  style="width:32px;"> [Scala](Image_Scaling/it.md): ridimensiona un\'immagine importata su un piano.



## Funzioni

-   Come avviene con uno [Schizzo](Sketcher_Workbench/it.md), un\'immagine importata può essere collegata a uno dei piani principali XY, XZ o YZ e viene fornito un offset positivo o negativo.
-   L\'immagine viene importata con una relazione di 1 pixel in 1 millimetro.
-   La raccomandazione è di importare un\'immagine con una risoluzione ragionevole.



## Flusso di lavoro 

Un uso importante di questo ambiente è il tracciamento sull\'immagine, con gli strumenti di [Draft](Draft_Workbench/it.md) o [Sketcher](Sketcher_Workbench/it.md), per generare un corpo solido basato sui contorni dell\'immagine.

Tracciare su un\'immagine funziona meglio se l\'immagine ha un piccolo offset negativo, ad esempio di -0,1 mm, dal piano di lavoro. Ciò significa che l\'immagine è leggermente dietro al piano in cui si disegna la geometria 2D, in modo da non disegnare sull\'immagine stessa.

L\'offset dell\'immagine può essere impostato durante l\'importazione o modificato successivamente attraverso le sue proprietà.





{{Image Tools navi

}}



---
⏵ [documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete%20Workbenches.md) > [Image](Category_Image.md) > Image Workbench/it
