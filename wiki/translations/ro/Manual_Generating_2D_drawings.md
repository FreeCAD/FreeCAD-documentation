# Manual:Generating 2D drawings/ro
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

Când modelul Dvs. nu poate fi imprimat 3D sau frezat direct de maşină, de exemplu, când este prea mare (cum ar fi o clădire) sau părţile cer să fie asamblate manual când sunt gata, de obicei trebuie să-i explicaţi unei alte persoane cum să procedeze. În domeniile tehnice (inginerie, arhitectură etc.) se folosesc în mod curent desene, care sunt înmânate unei persoane însărcinate cu asamblarea produsului final şi ele îi arată cum să procedeze.


</div>


<div class="mw-translate-fuzzy">

Exemplele tipice sunt [instrucţiunile de montare ale Ikea](http://www.ikea.com/ms/en_US/customer_service/assembly_instructions.html), [reprezentările arhitecturale](https://en.wikipedia.org/wiki/Architectural_drawing) sau [desenele schematice](https://en.wikipedia.org/wiki/Blueprint). De obicei, aceste desene conţin nu numai reprezentarea grafică propriu-zisă, ci şi numeroase alte adăugiri, precum texte, dimensiuni, numere, simboluri etc. care-i ajută pe alţii să înţeleagă ce trebuie făcut şi cum anume.


</div>


<div class="mw-translate-fuzzy">

În FreeCAD, atelierul destinat pentru crearea acestui tip de reprezentări grafice este [Desenare](TechDraw_Workbench.md).


</div>

The TechDraw Workbench allows you to create sheets, which can be blank or use a pre-made [template](TechDraw_Templates.md) to already have a series of items on the sheet, such as borders and a title. On these sheets, you can then place views of the 3D objects you modeled previously, and configure how these views will appear on the sheet. You can also place all kinds of annotations on the sheet, such as dimensions, texts, and other symbols commonly used in technical drawings.

Odată desenate, schemele pot fi listate la imprimantă sau exportate în formatele [SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics), PDF sau [DXF](https://en.wikipedia.org/wiki/AutoCAD_DXF).


<div class="mw-translate-fuzzy">

Pe parcursul următorului exerciţiu, vom vedea cum se realizează un desen simplu, precum cel al modelului de scaun aflat în [Biblioteca FreeCAD](https://github.com/FreeCAD/FreeCAD-library) mergând pe calea (Furniture -\> Chairs -\> IkeaChair). Biblioteca FreeCAD poate fi adăugată ușor la instalarea FreeCAD (raportați-vă la capitolul acestui manual [installing](Manual_Installing.md) ), sau puteți descărca pur și simplu modelul din pagina web a bibliotecii sau prin intermediul link-ului direct furnizat în partea de jos a acestui capitol.


</div>

![](images/Exercise_TechDraw_01.png )


<div class="mw-translate-fuzzy">

-   Încărcați fișierul IkeaChair din bibliotecă. Puteți alege între versiunea .FCStd, care va încărca istoricul complet de modelare, sau versiunea .step, care va crea un singur obiect, fără istorie. Deoarece nu va mai trebui să mai modelați, este mai bine să alegem versiunea .step, deoarece va fi mai ușor de manipulat.


</div>

![](images/Parts_library.jpg )


<div class="mw-translate-fuzzy">

-   Comutați pe [Drawing Workbench](Drawing_Workbench.md)
-   Apăsați mica săgeată alăturată butonului <img alt="" src=images/Drawing_Landscape_A3.png  style="width:16px;"> [New Drawing Page](Drawing_Landscape_A3.md) button.
-   Selectați șablonul **A4 Portrait / ISO7200** . O nouă filă se va deschide în fereastra FreeCAD, afișând noua pagină.
-   In vederea arborescentă (sau în tab-ul model), selectați modelul scaunului.
-   Apăsați butonul <img alt="" src=images/Drawing_View.png  style="width:16px;"> [Insert view](Drawing_View.md) .
-   Un obiect vedere va fi creat pe pagina noastră. Dați vederii următarele proprietăți:
    -   X: 100
    -   Y: 150
    -   Scale: 0.1
    -   Rotation: 270
-   Acum avem o vedere frumoasă (care este proiecția implicită) a scaunului nostru:

![](images/Exercise_drawing_02.jpg )


</div>

![](images/Exercise_drawing_02.jpg )


<div class="mw-translate-fuzzy">

-   Repetați operația de două ori, pentru a crea încă două vederi. Vom stabili valorile lor X și Y, care indică poziția vederii pe pagină și direcția acestora, pentru a crea orientări diferite de vizualizare. Dați fiecărei vizualizări noi următoarele proprietăți:
    -   View001 (front view): X: 100, Y: 130, Scale: 0.1, Rotation: 90, Direction: (-1,0,0)
    -   View002 (side view): X: 180, Y: 130, Scale: 0.1, Rotation: 90, Direction: (0,-1,0)
-   După aceasta, obținem următoarea pagină:

![](images/Exercise_drawing_03.jpg )


</div>

![](images/Exercise_TechDraw_04.png )


<div class="mw-translate-fuzzy">

-   Putem schimba aspectul vederilor noastre dacă vrem, de exemplu, putem ridica proprietatea **Width Line** la 0.5.


</div>

-   We can tweak the aspect of our views if we want, for example, we can change their **Line Width** property (under the View tab in the Combo View) to 0.5.


<div class="mw-translate-fuzzy">

Vom plasa cote și indicații pe desenul nostru. Există două moduri de a adăuga cotelor unui model, unul este plasarea cotelor în interiorul modelului 3D, folosind <img alt="" src=images/Draft_Dimension.png  style="width:16px;"> [Dimension](Draft_Dimension.md) instrumentul [Draft Workbench](Draft_Workbench/ro.md), și apoi plasați o vedere a acestor cote pe foaia noastră cu instrumetnul <img alt="" src=images/Drawing_DraftView.png  style="width:16px;"> [Draft View](Drawing_DraftView.md) (care pot fi utilizate cu o singură cotă sau cu un grup care conține cote), sau putem face lucruri direct pe foaia Desen, folosind [Drawing Dimensioning Workbench](https://github.com/hamish2014/FreeCAD_drawing_dimensioning), care este instalabil din [FreeCAD addons](https://github.com/FreeCAD/FreeCAD-addons). Vom folosi aici această metodă din urmă.


</div>


<div class="mw-translate-fuzzy">

-   Comutați pe [Drawing Dimensioning Workbench](https://github.com/hamish2014/FreeCAD_drawing_dimensioning)
-   Apăsați butonul **Add Linear Dimension** . Nodurile disponibile sunt evidențiate în verde pe pagina desenului:


</div>

![](images/Exercise_TechDraw_05.png )


<div class="mw-translate-fuzzy">

-   Instrumentul Dimensiune liniară, ca și în cazul majorității celorlalte instrumente de cotare a desenului, nu va ieși după ce ați terminat, permițându-vă să plasați mai multe dimensiuni. Când ați terminat, faceți clic pur și simplu pe butonul **Close** în Task panel.
-   Repetați operația, până când sunt plasate toate dimensiunile pe care doriți să le indicați. Faceți un minut pentru a căuta diferitele opțiuni propuse în panoul de sarcini Dimensiunile liniare. De exemplu, prin decuplarea opțiunii **auto place text**, veți putea plasa textul cotei în altă parte, ca în imaginea de mai jos:


</div>

![](images/Exercise_TechDraw_07.png )

-   We will now place the two callouts shown in the image above, using the <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [TechDraw Balloon](TechDraw_Balloon.md) tool.

![](images/Exercise_TechDraw_06.png )

1.  Looking at the Page in the [3D view](3D_view.md) window, select the View to which the Balloon will be attached, as shown in the image above.
2.  Press the <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> Balloon button.
3.  The cursor is now displayed as a balloon icon. Click on the page to place the balloon origin at the desired position.
4.  The balloon bubble may be dragged to the desired position.
5.  Change the balloon properties by double-clicking the balloon label or the balloon object in the [tree view](Tree_view.md). This will open the Balloon Task dialog. Set the Value field to the desired text and change the Symbol drop-down menu selection to **None**
6.  Press **OK**
7.  Repeat the operation for the second callout.

-   We will now fill in the sheet title block.
    -   Make sure that the View frames, labels, and vertices are visible. If not, hit the <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> Toggle button.
    -   Edit the text in each section of the sheet title block by clicking on the small green square on the left side of the text.


<div class="mw-translate-fuzzy">

Pagina noastră poate fi acum exportată în SVG pentru a fi utilizată în continuare în aplicații grafice cum ar fi [inkscape](http://www.inkscape.org), sau spre DXF selectând meniul **File -\> Export**. Atelierul Drawing Dimensioning workbench (Atelierul de cotare a desenului) are, de asemenea, propriul instrument de **DXF export**, care acceptă, de asemenea, adnotările adăugate în acest atelier. Formatul DXF este recunoscut în aproape toate aplicațiile CAD 2D existente. Paginile de desenare pot fi printate sau exportate direct în format PDF.


</div>

**Fişiere de descărcat**


<div class="mw-translate-fuzzy">

-   Modelul de scaun: <https://github.com/FreeCAD/FreeCAD-library/blob/master/Furniture/Chairs/IkeaLikeChair.step>
-   Fişierul creat pe parcursul acestui exerciţiu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/drawing.FCStd>
-   Fila SVG produsă de acest fişier: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/drawing.svg>


</div>

**De citit în plus**


<div class="mw-translate-fuzzy">

-   [Atelierul Desenare](TechDraw_Workbench/ro.md)
-   [The Drawing Dimensioning Workbench](https://github.com/hamish2014/FreeCAD_drawing_dimensioning)
-   [Biblioteca FreeCAD](https://github.com/FreeCAD/FreeCAD-library)
-   [Inkscape](http://www.inkscape.org)


</div>

**Watch tutorials**

-   [Sliptonic\'s TechDraw playlist](https://www.youtube.com/watch?v=7LbOmSGW9F0&list=PLEuOia-QxyFKQnmM1U9yVo7eNrK_Mcln8)
-   [Symbols and Views](https://www.youtube.com/watch?v=cggBR1Ghq7k)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Generating 2D drawings/ro
