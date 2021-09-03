 


{{Manual:TOC/ro}}

In limbajul computerului, cuvântul [rendering](https://en.wikipedia.org/wiki/Rendering_%28computer_graphics%29) este utilizat pentru a descrie o imagine frumoasă produsă de către un model 3D. Desigur, am putea spune că ceea ce vedem într-o vizualizarea 3D FreeCAD este deja ceva plăcut. Cu toate acestea, oricine a văzut un film recent de la Hollywood, știe că este posibil să se producă imagini cu un computer aproape că nu pot fi deosebite de o fotografie.

Desigur, producerea de imagini foto realiste necesită o mulțime de lucruri, în plus față de o aplicație 3D care oferă instrumente specifice în acest scop, precum controale precise pentru materiale și iluminat. Deoarece FreeCAD este o aplicație orientată mai mult spre modelarea tehnică, nu conține niciun fel de instrumente avansate de randare.

+Fortunately, lumea open source oferă numeroase aplicații pentru a produce imagini realiste. Cea mai faimoasă este probabil [Blender](http://www.blender.org), care este foarte popular și utilizat pe scară largă în industria cinematografică și de jocuri. Modelele 3D pot fi exportate cu ușurință și cu fidelitate din FreeCAD și importate în Blender, unde puteți adăuga materiale realiste și iluminare și puteți produce imagini finale sau chiar animații.


<div class="mw-translate-fuzzy">

Alte instrumente open source de randare sunt create pentru a fi folosite în alte aplicații și vor avea grijă să facă calcule complexe pentru a produce imagini realiste. Prin intermediul lui [Raytracing Workbench](Raytracing_Workbench.md), FreeCAD poate utiliza două dintre aceste instrumente de randare: [POV-Ray](https://en.wikipedia.org/wiki/POV-Ray) și [Luxrender](https://en.wikipedia.org/wiki/LuxRender). POV-Ray este un proiect foarte vechi și este considerat clasic [raytracing](https://en.wikipedia.org/wiki/Ray_tracing_%28graphics%29) engine, pe când Luxrender este mult mai recent, și este catalogat ca fiind un instrumente de randare [unbiased](https://en.wikipedia.org/wiki/Unbiased_rendering). Analiza SWOT arată că zmbele au punctele forte și punctele slabe, în funcție de tipul de imagine pe care vreți să o realizați. Cea mai bună modalitate de a le cunoaște este să examinați exemplele de pe site-urile ambelor motoare.


</div>

### Instalare

Înainte de a putea utiliza Raytracing Workbench în FreeCAD, una dintre aceste două aplicații de randare trebuie instalată pe sistemul dvs.This is usually very straightforward. They both provide installers for many platforms or are usually included in the software repositories of most Linux distributions.

Odată POV-Ray ori Luxrender este instalat, trebuie să setăm calea spre executabilul lor principal în preferințele FreeCAD. Acest lucru este de obicei necesar numai în Windows și Mac. Pe Linux, FreeCAD o va alege din locațiile standard. Locația executabililor de tip povray sau luxrender poate fi găsită prin căutarea în sistemul dvs. pentru fișiere numite povray (sau povray.exe pe Windows) și luxrender (sau luxrender.exe pe Windows).

![](images/Exercise_raytracing_01.jpg )

În acest ecran de preferințe putem seta dimensiunea dorită a imaginii pe care dorim să o producem.

### Randarea cu PovRay {#randarea_cu_povray}

Vom folosi tabela pe care am modelat-o în capitolul [traditional modeling](Manual:_Modeling_Traditional,_CSG_way.md) pentru a produce randări cu PovRay și Luxrender.


<div class="mw-translate-fuzzy">

-   Start by loading the table.FCStd file that we modelled earlier or from the link at the bottom of this chapter.
-   Press the small down arrow next to the <img alt="" src=images/Raytracing_New.png  style="width:16px;"> [New Povray project](Raytracing_New.md) button, and choose the **RadiosityNormal** template
-   A warning message might appear telling you that the current 3D view is not in perspective mode and the rendering will therefore differ. Correct this by choosing **No**, choosing menu **View-\>Perspective view** and choosing the RadiosityNormal template again.
-   You can also try other templates after you create a new project, simply by editing its **Template** property.
-   Un nou proiect a fost acum creat:


</div>

![](images/Exercise_raytracing_02.jpg )


<div class="mw-translate-fuzzy">

-   The new project has adopted the point of view of the 3D view as it was at the moment we pressed the button. We can change the view, and update the view position stored in the Povray project anytime, by pressing the <img alt="" src=images/Raytracing_ResetCamera.png  style="width:16px;"> [Reset camera](Raytracing_ResetCamera.md) button.
-   Atelierul de Raytracing funcționează în același mod ca [Drawing Workbench](Drawing_Workbench.md): Odată ce a fost creat un folder pentru proiect, trebuie să adăugăm **Views** a obiectelor noastre la el.

Acum putem face acest lucru prin selectarea tuturor obiectelor care compun masa și apăsați pe butonul <img alt="" src=images/Raytracing_InsertPart.png  style="width:16px;"> [Insert part](Raytracing_InsertPart.md) :


</div>

![](images/Exercise_raytracing_03.jpg )


<div class="mw-translate-fuzzy">

-   The views have taken the color and transparency values from their original parts, but you can change that in the properties of each individual view if you wish.
-   We are now ready to produce our first Povray render. Press the <img alt="" src=images/Raytracing_Render.png  style="width:16px;"> [Render](Raytracing_Render.md) button.
-   Note for windows users: when receiving (in Povray) a warning saying \"I/O restrictions prohibit write access \...\"
    -   open Povray
    -   choose \"Options \> Script I/O Restrictions\" and make sure it is set to \"No Restrictions\"
    -   retry render
-   You will be asked to give a file name and path for the .png image that will be saved by Povray.
-   Povray will then open and calculate the image.
-   După ce faceți acest lucru, dați clic pe imagine pentru a închide fereastra Povray. Imaginea rezultată va fi încărcată în FreeCAD:


</div>

![](images/Exercise_raytracing_04.jpg )

### Randarea cu LuxRender {#randarea_cu_luxrender}


<div class="mw-translate-fuzzy">

-   Rendering cu Luxrender funcționează aproape în același mod. Putem lăsa fișierul nostru deschis și să creați un nou proiect Luxrender în același fișier sau să îl reîncărcați pentru a începe de la zero.
-   Press the little down arrow next to the <img alt="" src=images/Raytracing_Lux.png  style="width:16px;"> [New Luxrender project](Raytracing_Lux.md) button and choose the **LuxOutdoor** template.
-   Select all the components of the table. If you still have the Povray project in your document, be sure to also select the Luxrender project itself, so the views created in the next step won\'t go in the wrong project by mistake.
-   Press the <img alt="" src=images/Raytracing_InsertPart.png  style="width:16px;"> [Insert part](Raytracing_InsertPart.md) button.
-   Select the Luxrender project, and press the <img alt="" src=images/Raytracing_Render.png  style="width:16px;"> [Render](Raytracing_Render.md) button.
-   Luxrender works differently to Povray. When you start the render, the Luxrender application will open and immediately start rendering:


</div>

![](images/Exercise_raytracing_05.jpg )

-   If you leave that window open, Luxrender will continue calculating and rendering forever, progressively refining the image. It is up to you to decide when the image has reached a sufficient quality for your needs, and stop the render.
-   There are also many controls to play with, on the left panel. All these controls will change the aspect of the image being rendered on the fly, without stopping the rendering.
-   Atunci când ajungeți la concluzia că avem o calitate suficient de bună, apăsați**Render-\>stop**, și apoi **File-\>Export to image-\>Tonemapped low dynamic range** pentru a salva imaginea randată îîntr-un fișier png .


<div class="mw-translate-fuzzy">

Puteți extinde foarte mult posibilitățile de randare ale FreeCAD, creând noi șabloane pentru Povray sau Luxrender. Acest lucru este explicat în [Raytracing Workbench](Raytracing_Workbench.md) documentation.


</div>

**Fişiere de descărcat**

-   Modelul de tabel: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/table.FCStd>
-   Fișierul produs pe durat aacestui exercițiu se află la: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/render.FCStd>

**De citit în plus**


<div class="mw-translate-fuzzy">

-   [The Raytracing Workbench](Raytracing_Workbench.md)
-   [Blender](http://www.blender.org)
-   [POV-Ray](http://www.povray.org)
-   [Luxrender](http://www.luxrender.net)


</div>




{{Raytracing Tools navi}} 

[Category:Tutorials{{\#translation:}}](Category:Tutorials.md)
