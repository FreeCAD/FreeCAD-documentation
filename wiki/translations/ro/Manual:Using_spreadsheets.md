 


{{Manual:TOC/ro}}


<div class="mw-translate-fuzzy">

FreeCAD oferă un alt atelier de lucru interesant pentru a explora: [Spreadsheet Workbench](Spreadsheet_Workbench.md). Acest atelier vă permite să creați [spreadsheets](https://en.wikipedia.org/wiki/Spreadsheet) ca cele realizate cu [Excel](https://en.wikipedia.org/wiki/Microsoft_Excel) sau

[LibreOffice](https://en.wikipedia.org/wiki/OpenOffice.org_Calc) direct în FreeCAD. Aceste foi de calcul pot fi apoi populate cu date extrase din modelul dvs. și pot efectua, de asemenea, o serie de calcule între valori. Foile de calcul pot fi exportate ca fișiere CSV, care pot fi apoi importate în orice altă aplicație de calcul tabelar.


</div>

Cu toate acestea, în FreeCAD, foile de calcul au o utilitate suplimentară: Celulele lor pot primi un nume și pot fi menționate de orice domeniu susținut de [expressions engine](Expressions.md). Aceste foi de calcul se transformă în structuri de control puternice, unde valorile introduse în celule specifice pot modifica dimensiunile modelului. Nu trebuie să țineți minte doar că, deoarece FreeCAD interzice dependența circulară între obiecte, aceeași foaie de lucru nu poate fi utilizată pentru a defini o proprietate a unui obiect și, în același timp, pentru a recupera o valoarea de proprietate a aceluiași obiect. Asta ar însemna că foaia de calcul și obiectul depind unul de celălalt.

În următorul exemplu, vom crea câteva obiecte, vom prelua unele dintre proprietățile lor dintr-o foaie de calcul și apoi vom folosi foaia de lucru pentru a modifica proprietățile altor obiecte.

### Lectura Proprietăților 


<div class="mw-translate-fuzzy">

-   Începeți prin comutarea pe [Part Workbench](Part_Workbench.md), și crearea câtorva obiecte: <img alt="" src=images/Part_Box.png  style="width:16px;"> [box](Part_Box.md), <img alt="" src=images/Part_Cylinder.png  style="width:16px;"> [cylinder](Part_Cylinder.md) și <img alt="" src=images/Part_Sphere.png  style="width:16px;"> [sphere](Part_Sphere.md).
-   Editați proprietatea de **Placement** (sau utilizați <img alt="" src=images/Draft_Move.png  style="width:16px;"> [Draft Move](Draft_Move.md) tool) pentru a le puțin mai departe, astfel încât să putem vedea efectele a ceea ce vom face:


</div>

![](images/Exercise_spreadsheet_01.jpg )


<div class="mw-translate-fuzzy">

-   Now, let\'s extract some information about these objects. Switch to the [Spreadsheet Workbench](Spreadsheet_Workbench.md)
-   Press the <img alt="" src=images/Spreadsheet_Create.png  style="width:16px;"> **New Spreadsheet** button
-   Double-click the new Spreadsheet object in the tree view. The spreadsheet editor opens:


</div>

![](images/Exercise_spreadsheet_02.jpg )

The spreadsheet editor of FreeCAD, although it is not as complete and powerful as the more complete spreadsheet applications we listed above, has nevertheless most of the basic tools and functions that are commonly used, such as the possibility to change the aspect of the cells (size, color, alignment), join and split cells, use formulas such as **=2+2**, or reference other cells with **=B1**.

In FreeCAD, on top of these common features, there is a new interesting one: The possibility to reference not only other cells, but other objects from the document, and retrieve values from their properties. For example, let\'s retrieve a couple of properties from the 3 objects we created above. Properties are what we can see in the properties editor window, under the **Data** tab, when an object is selected.

-   Let\'s start by entering a couple of texts in the cells A1, A2 and A3, so we remember what is what later on, for example **Cube Length**, **Cylinder Radius** and **Sphere Radius**. To enter text, just write in the \"Contents\" field above the spreadsheet, or double-click a cell.
-   Now let\'s retrieve the actual length of our cube. In cell B1, type **=Cube.Length**. You will notice that the spreadsheet has an autocompletion mechanism, which is actually the same as the expression editor we used in the previous chapter.
-   Do the same for cell B2 (**=Cylinder.Radius**) and B3 (**=Sphere.Radius**).

![](images/Exercise_spreadsheet_03.jpg )

-   Although these results are expressed with their units, the values can be manipulated as any number, try for example entering in cell C1: **=B1\*2**.
-   We can now change one of these values in the properties editor, and the change will be immediately reflected in the spreadsheet. For example, let\'s change the length of our cube to **20mm**:

![](images/Exercise_spreadsheet_04.jpg )


<div class="mw-translate-fuzzy">

The [Spreadsheet Workbench](Spreadsheet_Workbench.md) page will describe in more detail all the possible operations and functions available in spreadsheets.


</div>

### Scrierea proprietăților 

O altă utilizare foarte interesantă a Atelierul foi de calcul (Spreadsheet) în FreeCAD este de a face exact opusul a ceea ce am făcut până acum: n loc să citim valorile proprietăților obiectelor 3D, putem atribui valori acestor obiecte. Amintiți-vă, totuși, una dintre regulile fundamentale ale FreeCAD: dependențele circulare sunt interzise. Noi nu putem folosi aceeași foaie de calcul pentru a citi **and** scrie valorile la un obiect 3D. Acest lucru ar face ca obiectul să depindă de foaia de calcul, care depinde, de asemenea, de obiect. În schimb, vom crea o altă foaie de calcul.


<div class="mw-translate-fuzzy">

-   We can now close the spreadsheet tab (under the 3D view). This is not mandatory, there is no problem in keeping several spreadsheet windows open.
-   Press the <img alt="" src=images/Spreadsheet_Create.png  style="width:16px;"> **New Spreadsheet** button again
-   Change the name of the new spreadsheet to something more meaningful, such as **Input** (do this by right-clicking the new spreadsheet object, and choosing **Rename**).
-   Double-click the Input spreadsheet to open the spreadsheet editor.
-   In cell A1, let\'s put a descriptive text, for example: \"Cube dimensions\"
-   In cell B1, write **=5mm** (using the = sign makes sure the value is interpreted as a unit value, not a text).
-   Now to be able to use this value outside the spreadsheet, we need to give a name, or alias, to the B1 cell. Right-click the cells, click **Properties** and select the **Alias** tab. Give it a name, such as **cubedims**:


</div>

![](images/Exercise_spreadsheet_05.jpg )

-   Press **OK**, then close the spreadsheet tab
-   Select the cube object
-   In the properties editor, click the little <img alt="" src=images/Bound-expression-unset.png  style="width:16px;"> **expression** icon at the right side of the **Length** field. This will open the [expressions editor](Expressions.md), where you can write **Spreadsheet001.cubedims**. Repeat this for Height and Width:

![](images/Exercise_spreadsheet_06.jpg )


<div class="mw-translate-fuzzy">

You might wonder why we had to use \"Spreadsheet001\" instead of \"Input\" in the expression above. This is because each object, in a FreeCAD document, has an **internal name**, which is unique in the document, and a **label**, which is what appears in the tree view. If you uncheck the relevant option in the preferences window, FreeCAD will allow you to give the same label to more than one object. This is why all operations that must identify an object uniquely, will use the internal name instead of the label, which could designate more than one object. The easiest way to know the internal name of an object is by keeping the **selection panel** (menu Edit-\>Panels) open, it will always indicate the internal name of a selected object:


</div>

![](images/Exercise_spreadsheet_07.jpg )

By using cell aliases in spreadsheets, we are able to use a spreadsheet to store \"master values\" in a FreeCAD document. This can be used, for example, to have a model of a piece of certain dimensions, and to store these dimensions in a spreadsheet. It then becomes very easy to produce another model with different dimensions, it is just a matter of opening the file and changing a couple of dimensions in the spreadsheet.

În cele din urmă, rețineți că constrângerile dintr-o schiță pot primi, de asemenea, valoarea unei celule de foaie de calcul tabelar:

![](images/Exercise_spreadsheet_08.jpg )

Puteți, de asemenea, să dați aliasuri constrângerilor dimensionale (orizontale, verticale sau distanțe) într-o schiță (puteți utiliza și această valoare din afara schiței):

![](images/Exercise_spreadsheet_09.jpg )

**Fişiere de descărcat**

-   Fișierul produs în cadrul acestui exercițiu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/spreadsheet.FCStd>

**De citit în plus**


<div class="mw-translate-fuzzy">

-   [The Spreadsheet Workbench](Spreadsheet_Workbench.md)
-   [The Expressions engine](Expressions.md)


</div>




[Category:Tutorials/ro](Category:Tutorials/ro.md)
