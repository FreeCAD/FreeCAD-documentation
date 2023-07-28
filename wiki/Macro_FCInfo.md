# Macro FCInfo
{{Macro
|Name=Macro FCInfo
|Icon=FCInfo.png
|Description=Gives information about the selected shape and can display a conversion of length, inclination (degrees, radians, grades, percent), area, volume and weight in different units (metric and imperial). The macro now also works for the elements of a sketch in edit mode.
<br />French Version [https://gist.githubusercontent.com/mario52a/6afc64081c4eb8be3b93/raw/ddfd2254616b8f3127e0d930abe0b322fa99ee6a/FCInfo_fr_Ver_1-27-rmu_Docked.FCMacro Version française]
|Author=Mario52
|Version=1.27
|Date=2023/06/30
|FCVersion=All
|SeeAlso=[Arch Survey|<img src=images/Arch_Survey.svg style="width:24px"> [Arch Survey](Arch_Survey.md)<br /> [Macro_SimpleProperties|<img src=images/Macro_SimpleProperties.png style="width:24px"> [Macro SimpleProperties](Macro_SimpleProperties.md)<br /> [<img src=images/Macro_FCInfoGlass.png style="width:24px"> [Macro FCInfoGlass](Macro_FCInfoGlass.md)
}}

## Description

Gives information about the selected shape and can display a conversion of length, inclination (degrees, radians, grades, percent), area, volume and weight in different units (metric and imperial). The macro now also works for the elements of a sketch in edit mode.

 

<img alt="" src=images/Macro_FCInfo_00_en.png  style="width:480px;"> 
*FCInfo*

## Use

Select an object or launch the application and select an object, and a series of informations appear. His calculations based on unity of FreeCAD, which is the **mm** to each new selection, the length unit always comes back on **mm** and angle on **decimal degrees**. <img alt="window" src=images/Macro_FCInfo_06.png  style="width:900px;">




### Sector 1: Document 

![FCInfo Document](images/Macro_FCInfo_Document_00.png )

-   Document name
-   Label and internal name of the object
-   Internal Name of the object
-   Sub element name and type of the object
-   Type of the object

### Sector 2: Coordinates click mouse 

![FCInfo Coordinate](images/Macro_FCInfo_Coordinate_click_mouse_00.png )

-   Coordinates X,Y and Z click to mouse
-   The **button** creates point, axis, plane, copy vector axis from **FreeCAD.Vector(-24.0, 240.0, 7.0)**

### Sector 3: Color on point 

![FCInfo Color_on_point](images/Macro_FCInfo_Color_on_point_00.png )

-   Color on point clicked.
    -   value 0.0 to 1.0

-   Line Edit display the color value in different formats: {{LineEdit|"3435973887" , "#cccccc" , "0xcccccc" , "204,204,204" , "(0.8,0.8,0.8)"}}
    -   **3435973887** : Mode RVBA Int unsigned (format in FreeCAD preferences) Alpha = 255
    -   **#cccccc** : Mode RVB Hexadecimal (Qt: `setStyleSheet("color : #cccccc")`)
    -   **0xcccccc** : Mode RVB Hexadecimal (Python: `hex(0xcccccc`)
    -   \"**204,204,204** \" : RVB decim: Mode RVB (Qt: `setStyleSheet(u"QLineEdit {"background-color: rgb(204, 204, 204)};")`)
    -   **(0.8,0.8,0.8)** : RVB float: Mode RVB format float de 0.0 à 1.0
    -   (The number of decimals depend of the option *\"x (Decimals)\"*)

-    {{CheckBox|Sub.Objet}}: Change the color of the selected object or subobject. If this box is activated {{CheckBox|TRUE|Sub.Objet}} the face or sub Object selected is modified or duplicated. If it is not activated (default) the object is modified (color) or duplicated

-    **Coul. Obj**: Change the color of the shape or the face depend of the choice. In case object Mesh or Points the complete object is colored.

-    **Dupl. Obj**: Duplicates the face or the object depend to the chosen option. In the case of a Mesh object or Points the complete object is colored. Duplicate a Mesh object keeps the original and creates a solid shape. Duplicate a Points object keeps the original and creates a copy.

-    {{SpinBox|0}}: Degree of transparency of the selected face or object depend on the option chosen **0 = opaque** , **100 = transparent**

### Sector 4: Units 

![FCInfo Units](images/Macro_FCInfo_Units_00.png )

-    {{ComboBox|mm}}: If the object is a face perimeter, length of the object is displayed. Unit size can be selected :
    km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.

-   Length of the object : Length of the object or perimeter of the face {{LineEdit|10.0 mm}}.

-   If the object is a circle, a second lineEdit **Radius :** is opened and display the radius and diameter of circle {{LineEdit|2.0 mm (dia. 4.0 mm)}}.

-   Perimeter of the shape (12). Perimeter of the object and number of subObject (Edges) contained in the object {{LineEdit|120.0 mm}}.

### Sector 5: Inclination 

![FCInfo Inclination](images/Macro_FCInfo_Inclination_00.png )

-   **Inclination of the object** can be displayed in:
    -   decimal degree, ex: {{LineEdit|174.831872611°}}
    -   degree minute seconde, ex: {{LineEdit|174° 49' 54.741401''}}
    -   radian, ex: {{LineEdit|3.05139181449 rad}}
    -   grade, ex: {{LineEdit|194.257636235 gon}}
    -   pourcent, ex: 30° = {{LineEdit|57.74%}}
-   **Inclinations in planes XY, YZ, ZX** and their coordinates
-   **Direction object**, {{LineEdit|Vector (0.0, 0.0, -10.0)}} give the direction of object. The calculate is : coord_1 - coord_2 = direction (or reverse)
    -   
        **Direction**
        
        this button create a line in direction of the object.
-   **ValueAt(0)**, {{LineEdit|Vector (0.0, 0.0, 10.0)}} returns the 3D vector corresponding to a parameter value.
    -   
        **ValueAt(0)**
        
        this button create a line in ValueAt direction of the object.
-   **NormalAt(0,0)**, {{LineEdit|Vector (0.0, 0.0, 1.0)}} returns the 3D vector corresponding to a parameter value.
    -   
        **NormalAt(0,0)**
        
        this button create a line in NormalAt direction of the object.

### Sector 6: Surface and Volume 

![FCInfo Surface and Volume](images/Macro_FCInfo_Surface_and_Volume_00.png )

-   Surface of the form displayed, unit size can be selected. {{LineEdit|600.0 mm2}}
-   Surface of the face displayed, unit size can be selected. {{LineEdit|0.0 mm2}}
-   Volume of the form displayed, unit size can be selected. {{LineEdit|1000.0 mm3}}
-   Unit , choice your unit.
-   The {{ComboBox|gram}} unit mass can be chosen :
    ton,quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
    lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct.
-   Weight of the form displayed, unit mass can be selected. {{LineEdit|2.7 g}}
-   Density of the material in **kg by dm3** {{LineEdit|2.7000 kg (by dm3)}}
-   Material {{ComboBox|Metal Nickel (Ni),8.27,10.0,adapt Price}}
    -   In beginning the macro search the file **FCInfo_material.txt**, if the file not exist, one file FCInfo_material.txt is created.
    -   The file is created with 10 types of material saved in this format.
        -   **Title of material , Density on dm3 , Price on dm3 , text info on choice**
        -   *(4 fields separate by coma)*
        -   Liquid Water (H2o),1,10.0,adapt Price
        -   Mater Beton,2.4,10.0,adapt Price
        -   Metal Aluminium (Al),2.7,10.0,adapt Price
        -   Metal Copper (Cu),8.96,10.0,adapt Price
        -   Metal Gold (Au),19.3,10.0,Gratis
        -   Metal Iron (Fe),7.87,10.0,adapt Price
        -   Metal Lead (Pb),11.35,10.0,adapt Price
        -   Metal Magnesium (Mg),1.43,10.0,adapt Price
        -   Metal Nickel (Ni),8.27,10.0,adapt Price
        -   Metal Pewter (Sn),7.29,10.0,adapt Price
        -   Metal Platinum (Pt),21.45,10.0,adapt Price
        -   Metal Silver (Ag),10.5,10.0,adapt Price
        -   Metal Sodium (Na),0.97,10.0,adapt Price
        -   Metal Titanium (Ti),4.4,10.0,adapt Price
        -   Metal Zinc (Zn),7.1,10.0,adapt Price
        -   Wood Beechwood,0.8,10.0,adapt Price
        -   Wood MDF,0.75,10.0,adapt Price
        -   Wood Mahogany,0.6,10.0,adapt Price
        -   Wood Oak,0.7,10.0,adapt Price
        -   Wood White pine,0.4,10.0,adapt Price
-   New material or editing {{LineEdit|Metal Nickel (Ni),8.27,10.0,adapt Price}}
    -   you can modify or edit one new material in this format:

    -   **Title, Density on dm3, Price on dm3, text info on choice**

    -   *(4 fields separate by coma)*

    -   *you can also edit the file in your favorite editor respecting the specific format*

    -   you can save the file in a path desired with the variable : **seTMaterialSavePathName**

    -   *by default the file is created in the macro path*

    -   
        **Delete 1/17**
        
        : delete the field displayed

    -   
        **Save**
        
        : save the modification or the new material

### Sector 7: Cost 

![FCInfo Cost](images/Macro_FCInfo_Cost_00.png )

-   Cost total : cost total of the object selected


{{LineEdit|0.027 Eu}}

-   Price (kg/dm3) : price of the material selected (*Metal Aluminium (Al),2.7,***10.0***,adapt Price*)


{{SpinBox|10,0000 Eu (by Kg)}}

### Sector 8: BoundBox 

![FCInfo BoundBox](images/Macro_FCInfo_BoundBox_00.png )

-   BoundBox gives extreme dimensions of the shape.
    -   maximum X length : {{LineEdit|10.0 mm}}

    -   maximum Y length : {{LineEdit|10.0 mm}}

    -   maximum Z length : {{LineEdit|10.0 mm}}

    -   diagonal length : {{LineEdit|17.3205 mm}}

    -   
        **Tracing**
        
        : create 6 rectangles to dimensions of boundbox

    -   
        **Volume**
        
        : create volume to dimensions of boundbox

    -   
        {{CheckBox|Text Dim.}}
        
        : create the dimension of the triangle *(boundbox)*

    -   If the {{CheckBox|TRUE|Text Dim.}} is checked, the spinbox dimension of text {{SpinBox|3,000}} is operational for give your value *(3.0 by default)*

### Sector 9: Center of: 

![FCInfo Center of\...](images/Macro_FCInfo_Center_of_00.png )

-   Center of the shape and these coordinates XYZ
-   Center of mass and these coordinates XYZ
-   The **buttons** creates on point, axis, plane, copy vector axis form **FreeCAD.Vector(-24.0, 240.0, 7.0)** *(see Sector 13)*

### Sector 10: Inertia 

![FCInfo Inertia](images/Macro_FCInfo_Inertia_00.png )

-   Moment of inertia and these coordinates length and weigth
-   The button creates on point, axis, plane, copy vector axis form **FreeCAD.Vector(-24.0, 240.0, 7.0)** *(see Sector 13)*
    -   action line 1 : {{LineEdit|x1}}, {{LineEdit|y1}}, {{LineEdit|z1}}, {{LineEdit|0.0}}
    -   action line 2 : {{LineEdit|x2}}, {{LineEdit|y2}}, {{LineEdit|z2}}, {{LineEdit|0.0}}
    -   action line 3 : {{LineEdit|x3}}, {{LineEdit|y3}}, {{LineEdit|z3}}, {{LineEdit|0.0}}
    -   action 4 diagonal : {{LineEdit|x1}}, {{LineEdit|y2}}, {{LineEdit|z3}}

same for length and weigth

-   Determinant 1 : {{LineEdit|4629629629629.633}} computes the determinant of the matrix, in [scientific value](https://en.wikipedia.org/wiki/Scientific_notation)
-   Determinant 2 : {{LineEdit|4629629629629.6328125}} computes the determinant of the matrix, in decimal value

### Sector 11: Vertexes and details 

![FCInfo Disabled](images/Macro_FCInfo_Disabled_module_00.png )

-    {{CheckBox|Disabled module}}CheckBox for search or not all details of the object. If it is not checked, only the principal value is displayed.

-   Vertexes and details of the shape (compt_Edge), (compt_Faces), (compt_Vector of the Face)
    max 200 lines in the table, if there are more than 200 lines it appears **(!+ 200)** and the number of lines
    If the object is complicated with many objects, the time is long and the search is repeated with every mouse click. The write function in the spreadSheet included, decreases the display time for this it is disabled by default
    (full details can save be the **Save** button in a file in CSV format and can be viewed the file in spreadsheet with the **Read** or by an external spreadsheet as [LibreOffice](https://www.libreoffice.org/) [OpenOffice](http://openoffice.apache.org/downloads.html) or other)

### Sector 12: SpreadSheet 

![FCInfo SpreedSheet](images/Macro_FCInfo_SpreedSheet_00.png )

-    **Read**: read the data in a spreadsheet saved **.FCInfo** or txt, asc, csv

-    **Save**: save the data in disk in the form selected below **.FCInfo** or txt, asc, csv

-    {{RadioButton|TRUE|Tabulation}}: the separator is Tabulation (by default)

-    {{RadioButton|Comma}}: the separator is Comma

-    {{RadioButton|Semicolon}}: the separator is Semicolon

-    {{RadioButton|Space}}: the separator is Space

Option for save or read the spreadsheet with different separator, Tabulation, Comma, Semicolon, Space
The Tabulation are the separator for the FreeCAD \[Spreadsheet_Workbench\|Spreadsheet workbench\]
The number of this four separator are calculate for help if unknown
The COMMA are the old (01.16 and before) separator of the FCInfo macro
Now for compatibility with the FreeCAD spreadsheet and since 01.17 version the TABULATION is the separator by default
If you want to convert your old FCInfo spreadsheet : Open it in FCInfo and save it with the Tabulation option checked

### Sector 13: Main 

![FCInfo Main](images/Macro_FCInfo_Main_00.png )

-    {{CheckBox|Info}}: if this CheckBox is checked, the informations are displayed in the report view window

-    {{CheckBox|Point}}: if checked, one point is created in the coordinate displayed form : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    {{CheckBox|Axis}}: if checked, one axis is created in the coordinate displayed form : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    {{CheckBox|Plane}}: if checked, one axis plane is created in the coordinate displayed form : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    {{RadioButton|Clip-B0}}: None clipBoard

-    {{RadioButton|Clip-B1}}: If checked the coordinate are copy in the clipBoard Form : **FreeCAD.Vector(X.0, Y.0, Z.0)** FreeCAD model

-    {{RadioButton|Clip-B2}}: If checked the coordinate are copy in the clipBoard Form : **X, Y, Z** with Comma separator

-    {{RadioButton|Clip-B3}}: If checked the coordinate are copy in the clipBoard Form : **X Y Z** as is with Space separator

-    {{CheckBox|Left/Right}}: if this CheckBox is not checked, the window macro are displayed to right (default). If it is checked the window macro are displayed to left.
    If the option is 1 mode fly *(User parameter:BaseApp/Preferences/Macros/FCMmacros/FCInfo/**seTPositionFlyRightLeft**)* this button is not visible .

-    {{SpinBox|4 (Decimales)}}: give the number of decimal displayed

-    {{SpinBox|12 (Dim. texte)}}: give the dimensionof text in the macro

-    **Ref**: refresh the display of data in report view

-    **Exit**: exit properly the macro

Once launched macro, the macro remains active and the window remains visible. To exit the macro by pressing **Exit**. If you leave by the cross, the macro remains in memory and the data appears in the \"report view\" of FreeCAD, you must restart FreeCAD for quit it.


<center>

Image:Macro_FCInfo_04.png\|Docked to right, Image:Macro FCInfo 05.png\|or left with Combo view and reachable by a tab, or not docked, to the choice.


</center>




## Options

### The unit used 

#### Length unit: 

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.

#### Angle degrees : 

1.  **decimal degree**, ex: 174.831872611°
2.  degree minute seconde, ex: 174° 49\' 54.741401\'\'
3.  radian, ex: 3.05139181449 rad
4.  grade, ex: 194.257636235 gon
5.  pourcent ex: 30° = 57.74%

Understanding of angles in FCInfo display.




<center>



Image:Macro FCInfo 02.png\|Understanding of angles in FCInfo display Image:Macro FCInfo 03.gif\|Understanding of angles in pourcent in FCInfo display
click twice to see the animation (the image must be in full screen)




</center>






#### Weight unit : 

ton, quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct

#### FCInfo Configuration 

-   Location : **Tools \> Edit parameter \> \*User parameter:BaseApp/Preferences/Macros/FCMmacros/FCInfo/**
-   **switchNotInfoOnBeginning** **\#** SetBool {{true}} or \[{{false}}\]
    -   Display or not this text information on run macro
        -   \[{{false}}\] = display this information

        -   
            {{true}}
            
            = this Information is Not displayed On Beginning
-   **switchVersionSearch** **\#** SetBool {{true}} or \[{{false}}\]
    -   Search if one new version exist on run macro
-   **switchWarning** **\#** SetBool {{true}} or \[{{false}}\]
    -   Display or not display the window warning in case not good selection
-   **switchCreatePoint** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the Create point checkBox
-   **switchCreateAxis** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the Create axis checkBox
-   **switchCreatePlane** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the Create plane checkBox
-   **switchDisplayInfoObject** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the info checkBox
-   **switchClearDisplayReportView** **\#** SetBool {{true}} or \[{{false}}\]
    -   if switchClearDisplayReportView is {{true}} the ReportView is cleared
-   **seTWidgetPosition** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the Widget Position Left/Right checkBox
    -   if seTWidgetPosition \[{{false}}\] : if seTPositionFlyRightLeft = 2 = docked to Right
    -   if seTWidgetPosition {{true}} : if seTPositionFlyRightLeft = 3 = docked to Left
    -   if it is 1 the window macro is not docked
-   **switchBoundBoxCreateText** **\#** SetBool {{true}} or \[{{false}}\]
    -   Create the text dimension of the BoundBox
-   **seTBoundBoxTextHeigth** **\#** seTBoundBoxTextHeigth = 3.0
    -   Give the Heigth of the text dimension (independent of the seTTextHeigthValue)
-   **seTBoundBoxTextArround** **\#** seTBoundBoxTextArround = 3
    -   Give the arround of the text dimensions (independent of the seTDecimalValue)
-   **seTMemoClipBoard** **\#** SetInt \[0\], 1, 2, 3
    -   Give one value \[0\], 1, 2, 3 clipBoard
        -   \[0\] = desactivate the clipBoard
        -   1 = the data string is memorised to : FreeCAD.Vector( X, Y, Z )
        -   2 = the data string is memorised to : X, Y, Z
        -   3 = the data string is memorised to : X Y Z
-   **seTTextHeigthValue** **\#** SetInt 11
    -   Give one text heigth value of the macro
-   **seTDecimalValue** **\#** SetInt 4
    -   Give the number of decimal displayed
    -   If the number is -1 the total decimal value is displayed)
-   **seTMaterialCurrentIndex** **\#** SetInt 0
    -   Set the index of the ComboBox
-   **seTMaterialFileName** **\#** SetString FCInfo_material.txt
    -   Name of the material file
-   **seTMaterialSavePathName** **\#** SetString C:\\\...\\Macro\\FCInfo_material.txt
    -   Path name of the material file
-   **seTMaterialPrice** **\#** SetFloat
    -   Material price by Kg
-   **seTMaterialSuffixDevise** **\#** SetString
    -   Devise money
-   **seTMaterialSuffixCost** **\#** seTMaterialSuffixCost
    -   Suffix Devise cost
-   **seTMaterialCost** **\#** SetFloat
    -   Material cost
-   **seTDensiteValue** **\#** SetFloat 1.0
    -   Give the densite value
-   **seTDensiteDecimalNumber** **\#** SetInt 4
    -   Give the number of decimal for the densite value
-   **seTDensiteSingleStep** **\#** SetFloat 1.0
    -   Give the step for one click, by default 1.0 (possible 0.01 or \...)
-   **seTDensiteSuffixChain** **\#** SetString kg (by dm3)
    -   Choice your suffix string
-   **seTPositionFlyRightLeft** **\#** SetInt 2
    -   Choice your position, Fly, \[Right\], Left
        -   1 = the macro window is fly (not docked)
        -   \[2\] = the macro window is positioned to Right
        -   3 or other = the macro window is positioned to Left
-   **seTIndexUnitWeight** **\#** SetInt
    -   Set unit Weight index
-   **seTUnitSymbolMicro** **\#** U
    -   Set Symbol Micro
-   **seTUnitSymbolCube** **\#** 3
    -   Set Symbol Cube
-   **seTUnitSymbolCarre** **\#** 2
    -   Set Symbol Square
-   **seTIndexUnitLength** **\#** SetInt
    -   Set unit Length index
-   **setBSplineToByArcValue** **\#** SetFloat 0.00001
    -   Set unit for cut the BSpline for seack the radius on point given
-   **setMeshTopologyValue** **\#** SetFloat 0.1
    -   Set unit for create the Mesh to Shape
-   **switchBSplineCreateCircleConstructorAxis** **\#**SetBool {{true}} or \[{{false}}\]
    -   Display the axis of the circles (arcs) for create the BSpline
-   **switchBSplineCreateCircleConstructor** **\#**SetBool {{true}} or \[{{false}}\]
    -   Display the circles cretors for create the BSpline
-   **switchCreateLineDiVatNatOnClick** **\#**SetBool {{true}} or \[{{false}}\]
    -   Create the Line info on point (0,0,0) or on point mouse clicked (x,y,z) if it is {{true}}
    -   If it is {{true}} one \'\*\' is displayed in front of text. EX: \'\*Direction\'

## Script

Copy the contents of the macro in a file named \"FCInfo.FCMacro\"

-   Windows: the form is usually **\" drive:\\Users\\your_user_name\\AppData\\Roaming\\FreeCAD\\ \"**
-   Ubuntu: the form is usually **\" /home/your_user_name/.FreeCAD \"**.

Or, directly in the interface of FreeCAD
The icon must be in the same directory as the macro.
Download image positioning on the icon <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> and then drag the mouse right click \"save as\" (do not change the name)
**PS: the code is too long to be contained in the wiki page (for the time being the wiki pages accept only 64 KB) the macro code has been placed in the forum**
Download the macro file on gist **docked to right**


{{CodeDownload|https://gist.github.com/mario52a/8d40ab6c018c2bde678f|last version Macro_FCInfo}}

(Or **[on the forum.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=47748#p47748)** )
**PS:** this macro uses **getSelection()** and the list of object begin to 1 ex: for a box **Edge1 to Edge12** and the code in the console start at 0 ex: for a box **Edge\[0\] to Edge\[11\]**
This is normal, the counting on arrays/lists inside OpenCascade always starts at **1 and not at 0**.

### Limitations

Always leave the button **Exit**. If one exits the program without going through the button **Exit**, the program remains in memory and continues to run and the display will remain in the \"view report\". You must leave FreeCAD to erase it from memory.
Only the first 200 elements of the object are visible in the table. If there are more than 200 items in the object, a signal will be displayed by **(! +200)**. The complete list of data is visible in the file saved by the button **Save**.

If the window macro is invisible after the run, see the bottom window :

![](images/Macro_FCInfo_08.png )

![](images/FCInfo_begin_00.gif ) 

project:
~~read the file directly in a table.~~ done
~~matches the \"Edges\" and their coordinates~~ done
~~Association of a substance to its density~~
~~inclination on the element rather than the global object~~ done
~~inlay right in the interface of FreeCAD~~ done

## Version

ver 1.27 2023/06/30 optimize the styleSheet, correct the left/right position and restore view after edition sketcher  
```python
            self.PB_00_Decrement.setStyleSheet("background-color: white; border:2px solid rgb(215, 10, 22);")      # bord white and red
``` replaced by  
```python
            self.PB_00_Decrement.setStyleSheet("QPushButton {background-color: white; border:2px solid rgb(215, 10, 22)};")      # bord white and red
```

-   ver 1.26c 2022/04/19 upgrade BSpline error with Gear Bspline=Line

-   ver 1.26b 20/02/2022 upgrade for detect BSpline in SubObject

-   ver 1.26 06/02/2022 add info on Mesh and Points objects, decode colours, duplicate object or subObject, memorize the latest path and other preferences options

-   ver 1.25e 18/12/2021 add info detailed to BSpline (ToByArcs) and info \"sel\[0\].TypeId\"
-   ver 1.25d 12/12/2021 \-\--
-   ver 1.25c 12/12/2021 correct \"strAround((\" by \"str(Around(\" and other little \...
-   ver 1.25b 11/12/2021 correction error in change/modify new material and reorganization
-   ver 1.25 10/12/2021 PySide2 and add comboBox materials
-   ver 1.24 02/12/2021 add [adjustedGlobalPlacement](https://forum.freecadweb.org/viewtopic.php?f=22&t=59852) modified by edwilliams16 for placement with Body, boundbox tracing
-   ver 1.23cb 25/11/2021 delete **\"import Sketcher \* \"** create conflict with \"**open(OpenName, \"r\")**\" ??

Adding  
```python
FreeCAD.ActiveDocument.openTransaction(u"FCInfo")    # memorise les actions (avec annuler restore)
FreeCAD.ActiveDocument.commitTransaction()           # restore les actions  (avec annuler restore)
#FreeCAD.ActiveDocument.abortTransaction()            # abandonne les actions(avec annuler restore)
```

-   ver 1.25d, 13/12/2021 little correction material field uncomment the \"\'try\...Except\" !!!
-   ver 1.25c, 12/12/2021 little correction new material
-   ver 1.23b, 20/11/2021 little correction, add text info in beginning run macro, and ordinal the text code
-   ver 1.23 , 19/11/2021 include icon in macro, number decimal displayed, text height, configure options in the Preference FC, correct info for elements of sketch in edit mode.
-   ver 1.22 , 12/11/2020 : now the macro is totally uninstalled i use :

 
```python
try:
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)    # destroy
        self.window.deleteLater()                                     # destroy
        self.window.destroy()                                         # destroy
except Exception:
        None
```

[How do i exit from FreeCAD instead of Python?](https://forum.freecadweb.org/viewtopic.php?f=22&t=48013#p411508)

instead: 
```python
self.window.hide()
``` and i adding the possibility display or not the \"Error Message\" window \"False\" by default, if you wand activate the warning window go to :  
```python
FreeCAD >Menu >Tools >Edit parameters... >BaseApp/Preferences/Macros/FCMmacros/FCInfo > switchWarning
```

-   ver 1.21-3.01 , 07/11/2019 \# 07/11/2019 ver \"01.21-3-rmu\" replace character micro = \"U\", square = \"2\", cube = \"3\", degrees = \" deg\" see \"<https://forum.freecadweb.org/viewtopic.php?f=3&t=6005&start=70#p345819>\"
-   ver 1.21-2.01 (1.21-rmu) 11/06/2019 rmu replace all characters over 127 in ex: \"°\" in chr(176)) #degree
-   ver 1.21.01 (1.21-rmu) 30/05/2019 rmu change fixed positions to qt layouts grid.addWidget() by rmu75 see the rmu75 fork \"<https://gist.github.com/rmu75/b165147bd1c2f2659c014103793ae1d8>\"
-   ver 1.21 , 16/04/2019 optimization for Py 3\... Qt 5\... FreeCAD 0.15 to 0.19 release
-   ver 1.20 , 29/01/2018 optimization
-   ver 1.19 , 20/01/2018 create checkBox for use detection all elements of the object if wanted or not , the macro is faster. Optimisation
-   ver 1.18 , 19/12/2017 \...
-   ver 1.17c , 14/12/2017 create plane with coordinate give in one project in other project and replace \"FCInfo\" by \"\_\_title\_\_\"
-   ver 1.17b , 13/12/2017 little correction replace FCTreeView to FCInfo
-   ver 1.17 , 12/12/2017 add upgrade Moment of inertia mm and kg by pinq [FCMacro and moment of inertia of assembly](https://forum.freecadweb.org/viewtopic.php?t=23888), and create plane, axis, point, and add options separator for spreadsheet
-   ver 1.16 , 21/06/2017 add control height police (here PointSize 8) and checkbox for position the window to right or left
-   ver 1.15 , 19/12/2015 suppression PyQt4 option [see](http://forum.freecadweb.org/viewtopic.php?f=12&t=13541) , add checkBox for editing infos in report view
-   ver 1.14 , 04/08/2014 replace PyQt4 and PySide and correct tooltip not displayed cause on PySide and add fg
-   ver 1.13 , 27/07/2014 replace FCInfo_en_Ver_1-12_Docked.FCMacro to FCInfo_en_Ver_1-13_Docked.FCMacro accept PyQt4 and PySide
-   ver 1.12 , 10/03/2014 adding tooltip
-   ver 1.11 , 04/03/2014 adding µm, nm, pm, fm, µg, ng, pg, pourcent, fixed of grandeur carat ~~\"cd\"~~ in **\"ct\"**, display of the label and internal name, fixed calculation of angles XY YZ ZX could give an error on a compound shape, window dockable in FreeCAD
-   ver 1.10.b , 19/11/2013 buttons outside the scrollbar and the dimensions of the window blocking

(ver 1.10 , 18/11/2013 create scrollbar)
\*ver 1.08.b , 10/11/2013 translation units in English, error correction to display the area of the faces listed in the table and replacement of the\"**print**\" by \"**App.Console.PrintMessage**\"
~~ver 1.09 , 04/11/2013 works perfectly on Windows and Linux (cause of errors on Linux the characters : ² ³ ° \"ordinal not in range(128)\")~~
In a Linux distribution and in the case of an error of **\"ordinal not in range (128)\"** an alternative version exists on this page [Macro_FCInfo_Alternate_Linux](Macro_FCInfo_Alternate_Linux.md)
\*ver 1.08 , 24/10/2013 correction of high top \"Faces\" and \"Edges\" displaying 100 objects (in the saved file)
\*ver 1.07 , 11/10/2013 matches the \"Faces\" and their coordinates.
\*ver 1.06 , 22/09/2013 matches the \"Edges\" and their coordinates, inclination on the element rather than the global object
\*ver 1.05 , 17/09/2013 added an icon for the spreadsheet, conversion barrel fr, affichage des dimensions overall instead of coordinates.
\*ver 1.04 , 11/09/2013: read the file directly in a table.
\*ver 1.03 , 09/09/2013: clearer display in view report and replacement by \"typeObject = sel\[0\].Shape.ShapeType\"
\*ver 1.02 , 7/09/2013 : small updates
\*ver 1.00 , 6/09/2013

## Links

See Also: <img alt="Arch Survey" src=images/Arch_Survey.svg  style="width:36px;"> [Arch Survey](Arch_Survey.md)

You can share your comments on the forum [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)
Here another post of [FCInfo Macro](http://forum.freecadweb.org/viewtopic.php?f=8&t=6005)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FCInfo
