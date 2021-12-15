---
- GuiCommand:/it
   Name:Image CreateImagePlane
   Name/it:Piano immagine
   Icon:Image CreateImagePlane.svg
   MenuLocation:Barre degli strumenti → Crea un'immagine planare nello spazio 3D
   Workbenches:[Image](Image_Workbench/it.md)
   SeeAlso:[Apri immagine](Image_Open/it.md), [Scala immagine](Image_Scaling/it.md)
---

# Image CreateImagePlane/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento [Piano immagine](Image_CreateImagePlane/it.md) importa una immagine [bitmap](bitmap/it.md) e la posiziona su uno dei piani XY, YZ o XZ.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Image_CreateImagePlane.svg" width=16px> [Piano immagine](Image_CreateImagePlane/it.md)**.
2.  Selezionare l\'immagine desiderata.
3.  Scegliere il piano in cui posizionare l\'immagine, assegnare un valore di offset e premiere **OK**.


</div>

L\'oggetto ImagePlane risultante utilizza il rapporto 1 pixel = 1 millimetro; affinché l\'immagine sia visualizzata correttamente, deve avere una risoluzione sufficiente.


<div class="mw-translate-fuzzy">

Quando si importa l\'immagine, è possibile aggiungere un offset di `-0,1 mm` per posizionare l\'immagine leggermente dietro al piano di lavoro; questo rende più facile tracciare (disegnare sopra) l\'immagine con gli strumenti di [Draft](Draft_Workbench/it.md) o [Sketcher](Sketcher_Workbench/it.md).


</div>


<div class="mw-translate-fuzzy">

Se inizialmente non viene assegnato alcuno scostamento all\'immagine, la sua posizione può ancora essere regolata nelle [proprietà](property_editor/it.md).


</div>

## Proprietà


{{Properties Title|Base}}


<div class="mw-translate-fuzzy">


{{Properties Title|Base}}

-    **Position**: specifica le coordinate del punto base del piano dell\'immagine.

-    **Angle**: specifica l\'angolo di rotazione del piano dell\'immagine.

-    **Axis**: specifica l\'asse utilizzato per l\'angolo di rotazione.


</div>


{{Properties Title|Image Plane}}


<div class="mw-translate-fuzzy">


{{Properties Title|Image Plane}}

-    **XSize**: specifica la larghezza del piano dell\'immagine.

-    **YSize**: specifica l\'altezza del piano dell\'immagine.

-    **Image Plane**: specifica l\'immagine da usare per questo piano.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Image Tools navi

}}

---
[documentation index](../README.md) > [Image](Image_Workbench.md) > Image CreateImagePlane/it
