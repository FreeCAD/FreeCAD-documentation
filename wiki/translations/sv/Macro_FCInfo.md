# Macro FCInfo/sv
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


<div class="mw-translate-fuzzy">

## Beskrivning

Ger en serie information om den valda formen och kan visa en konvertering av längd, lutning (grader, radianer, grader, hällande) form, yta, volym och vikt av formuläret i densiteten vald i olika kvantiteter internationella och Anglo -Saxiska.


</div>


{{Codeextralink|https://gist.githubusercontent.com/mario52a/8d40ab6c018c2bde678f/raw/93362d69fe505714b80655756b2a3ba752767975/FCInfo_en_Ver_1-27-rmu_Docked.FCMacro}}

<img alt="" src=images/Macro_FCInfo_00_en.png  style="width:480px;"> 
*FCInfo*

## Use


<div class="mw-translate-fuzzy">

## Utnyttjande

Välj ett objekt eller starta programmet och välj ett objekt och en serie information visas. Hans beräkningar baserade på FreeCADs enhet, som är **mm** för varje nytt val, kommer längdsenheten alltid tillbaka på **mm** och vinkel på **decimalgrader**. <img alt="upper window" src=images/Macro_FCInfo_06.png  style="width:200px;"><img alt="lower window" src=images/Macro_FCInfo_07.png  style="width:200px;">


</div>


<div class="mw-translate-fuzzy">




**Sektor 1: Dokument**

-   Dokument namn
-   Etikett för objektet
-   Objektets interna namn
-   Subelementets namn på objektet
-   Typ av objektet


</div>

### Sector 1: Document 

![FCInfo Document](images/Macro_FCInfo_Document_00.png )

-   Document name
-   Label and internal name of the object
-   Internal Name of the object
-   Sub element name and type of the object
-   Type of the object




<div class="mw-translate-fuzzy">

**Sektor 2: Koordinater klicka på musen**

-   Koordinater X, Y och Z klickar på musen
-   Knappen skapas på punkt, axel, plan, kopiera vektoraxelformat **FreeCAD.Vector (-24.0, 240.0, 7.0)**


</div>

![FCInfo Coordinate](images/Macro_FCInfo_Coordinate_click_mouse_00.png )

-   Coordinates X,Y and Z click to mouse
-   The **button** creates point, axis, plane, copy vector axis from **FreeCAD.Vector(-24.0, 240.0, 7.0)**

### Sector 3: Color on point 

![FCInfo Color_on_point](images/Macro_FCInfo_Color_on_point_00.png )


<div class="mw-translate-fuzzy">

**Sektor 2: Koordinater klicka på musen**

-   Koordinater X, Y och Z klickar på musen
-   Knappen skapas på punkt, axel, plan, kopiera vektoraxelformat **FreeCAD.Vector (-24.0, 240.0, 7.0)**


</div>

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


<div class="mw-translate-fuzzy">

Alternativ för att spara eller läsa spreadSheet med olika separator, Tabulation, Comma, Semicolon, Space
Tabellen är separatorn för FreeCAD spreadSheet-modulen
Numret på den här fyra separatorn beräknas för hjälp om det är okänt
Kommunen är den gamla (01.16 och tidigare) separatorn av FCInfo makro
Nu för kompatibilitet med FreeCAD spreadSheet och sedan 01.17 versionen är tabellen separator som standard
Om du vill konvertera ditt gamla FCInfo-kalkylblad: Öppna det i FCInfo och spara det med Tabuleringsalternativet markerat


</div>

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


<div class="mw-translate-fuzzy">

När makroen är lanserad, förblir makroen aktiv och fönstret är synligt. För att lämna makroet genom att trycka på **Exit**. Om du lämnar vid korset kvarstår makrot i minnet och data visas i \"Rapportvy\" av FreeCAD.


</div>


<div class="mw-translate-fuzzy">


<center>

Image:Macro_FCInfo_04.png\|Dockad till höger, Image:Macro FCInfo 05.png\|eller vänster med kombinationsvy och nås med en flik, eller inte dockad till valet.


</center>





</div>

## Options




<div class="mw-translate-fuzzy">

## Alternativ

### Den enhet som används 

#### Längd enhet: 

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.


</div>

#### Length unit: 

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.

#### Angle degrees : 


<div class="mw-translate-fuzzy">

#### Vinkelgrader :

1.  **decimal degree**, ex: 174.831872611°
2.  degree minute seconde, ex: 174° 49\' 54.741401\'\'
3.  radian, ex: 3.05139181449 rad
4.  grade, ex: 194.257636235 gon
5.  pourcent ex: 30° = 57.74%


</div>


<div class="mw-translate-fuzzy">

Förståelse av vinklar i FCInfo-displayen.


<center>

Image:Macro FCInfo 02.png\|Förståelse av vinklar i FCInfo-displayen Image:Macro FCInfo 03.gif\|Förståelse av vinklar i poucent i FCInfo-skärm
klicka två gånger för att se animationen (bilden måste vara i helskärm)


</center>





</div>


<center>

Image:Macro FCInfo 02.png\|Understanding of angles in FCInfo display Image:Macro FCInfo 03.gif\|Understanding of angles in pourcent in FCInfo display
click twice to see the animation (the image must be in full screen)


</center>




#### Weight unit : 


<div class="mw-translate-fuzzy">

#### Viktenhet :

ton, quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct
\"spinboxen\" är inställd på **7,5** kg, medeltäthet av stål. Om du vill ha ett annat standardvärde, ändra värdet på densiteten, linje 208


</div>

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




<div class="mw-translate-fuzzy">

## Script

Kopiera innehållet i makroet i en fil med namnet \"FCInfo.FCMacro\"

-   Windows: formen är vanligtvis **\" drive:\\Users\\your_user_name\\AppData\\Roaming\\FreeCAD\\ \"**
-   Ubuntu: formen är vanligtvis **\" /home/your_user_name/.FreeCAD \"**.

Eller direkt i gränssnittet till FreeCAD
Ikonen måste vara i samma katalog som makroen.
Ladda ner bildpositionering på ikonen <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> och dra sedan musen med högerklicka \"spara som\" (ändra inte namnet)


</div>

Copy the contents of the macro in a file named \"FCInfo.FCMacro\"

-   Windows: the form is usually **\" drive:\\Users\\your_user_name\\AppData\\Roaming\\FreeCAD\\ \"**
-   Ubuntu: the form is usually **\" /home/your_user_name/.FreeCAD \"**.

Or, directly in the interface of FreeCAD
The icon must be in the same directory as the macro.
Download image positioning on the icon <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> and then drag the mouse right click \"save as\" (do not change the name)


<div class="mw-translate-fuzzy">

**PS: för länge att finnas på wikisidan (för tillfället wiki sidorna accepterar endast 64 KB) makrokoden har placerats i forumet**


</div>


<div class="mw-translate-fuzzy">

Hämta makrofilen på **docked to right**


</div>


<div class="mw-translate-fuzzy">


{{CodeDownload|https://gist.github.com/mario52a/8d40ab6c018c2bde678f|senaste versionen Macro_FCInfo och ikonerna i slutet av sidan}}


</div>


<div class="mw-translate-fuzzy">

(Eller **[On the forum.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=47748#p47748)** )
**PS:** detta makro använder **getSelection ()** och listan över objekt börjar till 1 ex: för en ruta **Edge1 till Edge12** och koden i konsolen börjar vid 0 ex: for a box **Edge\[0\] to Edge\[11\]**
Detta är normalt att räkna på arrayer / listor i OpenCascade börjar alltid på **1 och inte på 0**


</div>

### Limitations


<div class="mw-translate-fuzzy">

### Begränsningar

Lämna alltid knappen **Exit**. Om man lämnar programmet utan att gå igenom knappen **Exit**, förblir programmet i minnet och fortsätter att springa och displayen kommer att vara kvar i \"visningsrapporten\". Du måste lämna FreeCAD för att radera det från minnet.
Endast de första 200 elementen i objektet är synliga i tabellen om det finns mer än 200 objekt i objektet kommer en signal att visas med **(! +200)**. Den fullständiga listan med data är synlig i filen som sparas med knappen **Save**.


</div>


<div class="mw-translate-fuzzy">

Om fönstret makro är osynligt efter körningen, se nedre fönstret:


</div>

![](images/Macro_FCInfo_08.png )

![](images/FCInfo_begin_00.gif ) 


<div class="mw-translate-fuzzy">

projekt:
~~läs filen direkt i en tabell.~~ gjort
~~matchar \"Edges\" och deras koordinater~~ gjort
Sammansättning av ett ämne för dens densitet
~~lutning på elementet snarare än det globala objektet~~ gjort
~~inlägg direkt i gränssnittet till FreeCAD~~ gjort


</div>

## Version

ver 1.27 2023/06/30 optimize the styleSheet, correct the left/right position and restore view after edition sketcher 
```python
            self.PB_00_Decrement.setStyleSheet("background-color: white; border:2px solid rgb(215, 10, 22);")      # bord white and red
``` replaced by 
```python
            self.PB_00_Decrement.setStyleSheet("QPushButton {background-color: white; border:2px solid rgb(215, 10, 22)};")      # bord white and red
```


<div class="mw-translate-fuzzy">

-   ver 1.22 , 12/11/2020 : now the macro is totally uninstalled i use :


</div>

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
-   Ver 1.20, 29/01/2018 optimering
-   ver 1.19, 20/01/2018 skapa checkbox för att upptäcka alla element i objektet om det är önskat eller inte, makroet är snabbare. Optimering
-   ver 1.18, 19/12/2017 \...
-   ver 1.17c, 14/12/2017 skapa plan med koordinat ge i ett projekt i annat projekt och ersätt \"FCInfo\" med \"\_\_title\_\_\"
-   Ver 1.17b, 13/12/2017 liten korrigering ersätter FCTreeView till FCInfo
-   ver 1.17, 12/12/2017 lägg till uppgradering Moment of inertia mm och kg av pinq [FCMacro och tröghetsmoment](https://forum.freecadweb.org/viewtopic.php?t=23888) och skapa plan, axel, punkt och lägg till alternativ separator för kalkylblad
-   ver 1.16, 21/06/2017 lägg till kontrollhöjds polis (här PointSize 8) och kryssrutan för att placera fönstret åt höger eller vänster
-   ver 1.15, 19/12/2015 suppression PyQt4 alternativ [se](http://forum.freecadweb.org/viewtopic.php?f=12&t=13541), lägg till checkbox för att redigera infos i rapportvy
-   ver 1.14, 04/08/2014 ersätt PyQt4 och PySide och korrigera verktygstips inte visad orsak på PySide och lägg till fg
-   ver 1.13, 27/07/2014 ersätt FCInfo_en_Ver_1-12_Docked.FCMacro till FCInfo_en_Ver_1-13_Docked.FCMacro acceptera PyQt4 och PySide
-   ver 1.12, 10/03/2014 lägger till verktygstips
-   ver 1.11, 04/03/2014 Lägga till μm, nm, pm, fm, μg, ng, pg, hällande, fast av storhet karat ~~\"cd\"~~ i \'\' \'\"ct\" , visning av etiketten och internt namn, fast beräkning av vinklar XY YZ ZX kan ge ett fel på en sammansatt form, fönstret dockbart i FreeCAD
-   Ver 1.10.b, 19/11/2013 knappar utanför rullningsfältet och dimensionerna i fönstret blockerar

(ver 1.10, 18/11/2013 skapa rullningsfältet)
\* ver 1.08.b, 10/11/2013 översättningsenheter på engelska, felkorrigering för att visa området för ansikten som anges i tabellen och ersättning av **print** **App.Console .PrintMessage**
~~ver 1.09, 04/11/2013 fungerar perfekt på Windows och Linux (orsak till fel på Linux karaktärerna: ² ³ ° ordinal inte inom intervallet (128) \")~~
I en Linux-distribution och i händelse av ett fel på ordinär inte inom intervallet (128) finns det en alternativ version på den här sidan [Macro_FCInfo_Alternate_Linux](Macro_FCInfo_Alternate_Linux/sv.md)
\* Ver 1.08, 24/10/2013 korrigering av högsta \"Faces\" och \"Edges\" som visar 100 objekt (i den sparade filen)
\* ver 1.07, 11/10/2013 matchar \"Faces\" och deras koordinater.
\* ver 1.06, 22/09/2013 matchar \"Edges\" och deras koordinater, lutning på elementet snarare än det globala objektet
\* ver 1.05, 17/09/2013 lade till en ikon för kalkylbladet, konverteringskärlet fr, affichage des dimensions overall istället för koordinater.
\* ver 1.04, 11/09/2013: läs filen direkt i en tabell.
\* ver 1.03, 09/09/2013: tydligare visning i rapport och ersättning med \"typeObject = sel \[0\] .Shape.ShapeType\"
\* ver 1.02, 7/09/2013: små uppdateringar
\* ver 1.00, 6/09/2013



<div class="mw-translate-fuzzy">

## Länkar

Se även [Arch Survey](Arch_Survey/sv.md) <img alt="Arch Survey" src=images/Arch_Survey.png  style="width:36px;">


</div>

See Also: <img alt="Arch Survey" src=images/Arch_Survey.svg  style="width:36px;"> [Arch Survey](Arch_Survey.md)

Du kan dela dina kommentarer på forumet [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)
Här ett annat inlägg av [FCInfo Macro](http://forum.freecadweb.org/viewtopic.php?f=8&t=6005)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FCInfo/sv
