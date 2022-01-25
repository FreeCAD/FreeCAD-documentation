# Manual:Using spreadsheets/de
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC/de}}

FreeCAD features another interesting workbench to explore: the [Spreadsheet Workbench](Spreadsheet_Workbench.md). This workbench allows you to create [spreadsheets](https://en.wikipedia.org/wiki/Spreadsheet) such as those made with [Excel](https://en.wikipedia.org/wiki/Microsoft_Excel) or [Calc from LibreOffice](https://en.wikipedia.org/wiki/LibreOffice_Calc) directly in FreeCAD. These spreadsheets can then be populated with data extracted from your model, and can also perform a series of calculations between values. Spreadsheets can be exported as CSV files, which can be imported in any other spreadsheet application.

In FreeCAD, however, spreadsheets have an additional utility: Their cells can receive a name, and can then be referenced by any field supported by the [expressions engine](Expressions.md). This turns spreadsheets into powerful control structures, where the values inserted in specific cells can drive dimensions of the model. There is only one thing to keep in mind, as FreeCAD prohibits circular dependencies between objects, the same spreadsheet cannot be used to set a property of an object and at the same time retrieve a property value from the same object. That would mean the spreadsheet and the object depend on one other.

In the following example, we will create a couple of objects, retrieve some of their properties in a spreadsheet, then use the spreadsheet to directly drive properties of other objects.

### Leseeigenschaften

-   Start by switching to the [Part Workbench](Part_Workbench.md), and create a couple of objects: a <img alt="" src=images/Part_Box.svg  style="width:16px;"> [box](Part_Box.md), a <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> [cylinder](Part_Cylinder.md) and a <img alt="" src=images/Part_Sphere.svg  style="width:16px;"> [sphere](Part_Sphere.md).
-   Edit their **Placement** property (or use the <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Draft Move](Draft_Move.md) tool) to place them a little apart, so we can better see the effects of what we\'ll do:

![](images/Exercise_spreadsheet_01.jpg )

-   Now, let\'s extract some information about these objects. Switch to the [Spreadsheet Workbench](Spreadsheet_Workbench.md)
-   Press the <img alt="" src=images/Spreadsheet_Create.png  style="width:16px;"> **New Spreadsheet** button
-   Double-click the new Spreadsheet object in the tree view. The spreadsheet editor opens:

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

The [Spreadsheet Workbench](Spreadsheet_Workbench.md) page will describe in more detail all the possible operations and functions available in spreadsheets.

### Schreibeigenschaften

Another very interesting use of the Spreadsheet Workbench in FreeCAD is to do the contrary of what we have been doing until now: Instead of reading the values of properties of 3D objects, we can also assign values to these objects. Remember, however, one of the fundamental rules of FreeCAD: Circular dependencies are forbidden. We can therefore not use the same spreadsheet to read **and** write values to a 3D object. That would make the object depend on the spreadsheet, which would also depend on the object. Instead, we will create another spreadsheet.

-   We can now close the spreadsheet tab (under the 3D view). This is not mandatory, there is no problem in keeping several spreadsheet windows open.
-   Press the <img alt="" src=images/Spreadsheet_Create.png  style="width:16px;"> **New Spreadsheet** button again
-   Change the name of the new spreadsheet to something more meaningful, such as **Input** (do this by right-clicking the new spreadsheet object, and choosing **Rename**).
-   Double-click the Input spreadsheet to open the spreadsheet editor.
-   In cell A1, let\'s put a descriptive text, for example: \"Cube dimensions\"
-   In cell B1, write **=5mm** (using the = sign makes sure the value is interpreted as a unit value, not a text).
-   Now to be able to use this value outside the spreadsheet, we need to give a name, or alias, to the B1 cell. Right-click the cell, click **Properties** and select the **Alias** tab. Give it a name, such as **cubedims**:

![](images/Exercise_spreadsheet_05.jpg )

-   Press **OK**, then close the spreadsheet tab
-   Select the cube object
-   In the properties editor, click the little <img alt="" src=images/Bound-expression-unset.png  style="width:16px;"> **expression** icon at the right side of the **Length** field. This will open the [expressions editor](Expressions.md), where you can write **Spreadsheet001.cubedims**. Repeat this for Height and Width:

![](images/Exercise_spreadsheet_06.jpg )

You might wonder why we had to use \"Spreadsheet001\" instead of \"Input\" in the expression above. This is because each object, in a FreeCAD document, has an **internal name**, which is unique in the document, and a **label**, which is what appears in the tree view. If you uncheck the relevant option in the preferences window, FreeCAD will allow you to give the same label to more than one object. This is why all operations that must identify an object uniquely, will use the internal name instead of the label, which could designate more than one object. The easiest way to know the internal name of an object is by keeping the **selection panel** (menu bar View → Panels) open, it will always indicate the internal name of a selected object:

![](images/Exercise_spreadsheet_07.jpg )

By using cell aliases in spreadsheets, we are able to use a spreadsheet to store \"master values\" in a FreeCAD document. This can be used, for example, to have a model of a piece of certain dimensions, and to store these dimensions in a spreadsheet. It then becomes very easy to produce another model with different dimensions, it is just a matter of opening the file and changing a couple of dimensions in the spreadsheet.

Finally, note that the constraints inside a sketch can also receive the value of a spreadsheet cell:

![](images/Exercise_spreadsheet_08.jpg )

You can also give aliases to dimensional constraints (horizontal, vertical or distance) in a sketch (you can then use that value from outside the sketch as well):

![](images/Exercise_spreadsheet_09.jpg )

**Download**

-   The file produced in this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/spreadsheet.FCStd>

**Mehr lesen**


<div class="mw-translate-fuzzy">

-   [Der Arbeitsbereich Kalkulationstabellen](Spreadsheet_Workbench/de.md)
-   [Der Ausdrucksantrieb](Expressions/de.md)


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Using spreadsheets/de
