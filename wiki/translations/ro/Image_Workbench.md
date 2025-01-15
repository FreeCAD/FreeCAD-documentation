# Image Workbench/ro
**The '''Image Workbench''' is no longer included after version 0.20.<br>
Its functionality has been integrated in [Std Base](Std_Base.md). See [Std Import](Std_Import.md) and [Std ViewLoadImage](Std_ViewLoadImage.md).**

<img alt="Image workbench icon" src=images/Workbench_Image.svg  style="width:128px;">






## Introducere




Atelierul Imagine [Image Workbench](Image_Workbench.md) gestionează diferite tipuri de [bitmap images](http://en.wikipedia.org/wiki/Raster_graphics) și vă permite să le deschideți în FreeCAD.



## Instrumente


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Image-import.svg  style="width:32px;"> [Open](Image_Open.md): open an image on a new viewport.
-   <img alt="" src=images/Image-import-to-plane.svg  style="width:32px;"> [Import to plane](Image_CreateImagePlane.md): import an image to a plane in the 3D view.
-   <img alt="" src=images/Image-scale.svg  style="width:32px;"> [Scaling](Image_Scaling.md): scale an image imported to a plane.


</div>



## Funcționalități

-   Atelierul Imagine vă permite de asemenea să importați o imagine într-un plan spațial 3D al FreeCAD cu [Image Import](Image_CreateImagePlane/ro.md), cu al doilea buton al atelierului Imagine.
-   Imaginea importată poate fi atașată la o schiță a uneia dintre cele trei planuri (XY / XZ / YZ) cu ​​offset pozitiv sau negativ.
-   Această funcție este disponibilă numai dacă ați deschis un document FreeCAD.
-   The image can be moved in 3D-space by editing the placement in the [Property editor](Property_editor.md).
-   The major use is tracing over the image, in order to generate a new part while using the image as a template.
-   The image is imported with 1 pixel = 1mm.

 * The recommendation is to have the imported image at a reasonable resolution.

-   Imaginea poate fi scalată prin editarea valorilor \"XSize\" și \"YSize\" în[Property editor](Property_editor.md).
-   Imaginea poate fi mutată prin editarea valorilor X/Y/Z-în [Property editor](Property_editor.md).
-   Imaginea poate fi rotită în jurul unei axe utilizând [Property editor](Property_editor.md).

## Workflow


<div class="mw-translate-fuzzy">

## Flux de lucru 

O utilizare importantă a acestui atelier de lucru este urmărirea imaginii, cu ajutorul instrumentelor [ Draft](Draft_Workbench.md) sau [ Sketcher](Sketcher_Workbench.md), pentru a genera un corp solid bazat pe contururile imaginii.


</div>

**Tip:**
Urmărirea cu elemente de schiță peste o imagine funcționează cel mai bine dacă imaginea are o mică (negativă) decalare față de planul de schiță.
Puteți seta o decalare de -0,1 mm la import sau mai târziu, prin editarea destinației de plasare a imaginii.

Decalajul imaginii poate fi setat în timpul importului sau poate fi modificat mai târziu prin proprietățile sale.


<div class="mw-translate-fuzzy">


{{docnav/ro|Raytracing Workbench/ro|Draft Workbench/ro}}


</div>


{{Image Tools navi

}}



---
⏵ [documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete%20Workbenches.md) > [Image](Category_Image.md) > Image Workbench/ro
