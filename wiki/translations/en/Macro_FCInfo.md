# Macro FCInfo/en
{{Macro
|Name=Macro FCInfo
|Icon=FCInfo.png
|Description=Gives a series of information on the form.<br />FRench Version [https://gist.githubusercontent.com/mario52a/6afc64081c4eb8be3b93/raw/c1dd823886fe2e75dc5c6dd490157c259051b651/FCInfo_fr_Ver_1-22-rmu_Docked.FCMacro]
|Author=Mario52
|Version=1.22
|Date=2020/11/12
|FCVersion=All
|Download=Download the [https://forum.freecadweb.org/download/file.php?id=50755 Macro_FCInfo_Icon] package and paste it in the same directory of the macro
|SeeAlso=<img src=images/Arch_Survey.svg style="width:Arch Survey|24px"> [Arch Survey](Arch_Survey.md)<br />[Macro SimpleProperties](Macro_SimpleProperties.md)
}}

## Description

Gives a series of informations about the selected shape and can display a conversion of length, inclination (degrees, radians, grades, pourcent) shape, surface, volume and the weight of the form in the density selected in different units of quantities international and Anglo-Saxon.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/8d40ab6c018c2bde678f/raw/4ff055ff5eb117f75beea5843efca4791990cf62/FCInfo_en_Ver_1-22-rmu_Docked.FCMacro}}

<img alt="" src=images/Macro_FCInfo_00_en.png  style="width:480px;"> 
*FCInfo*

## Utilisation

Select an object or launch the application and select an object, and a series of informations appear. His calculations based on unity of FreeCAD, which is the **mm** to each new selection, the length unit always comes back on **mm** and angle on **decimal degrees**. <img alt="upper window" src=images/Macro_FCInfo_06.png  style="width:200px;"><img alt="lower window" src=images/Macro_FCInfo_07.png  style="width:200px;">




**Sector 1: Document**

-   Document name
-   Label of the object
-   Internal Name of the object
-   Sub element name of the object
-   Type of the object

**Sector 2: Coordinates click mouse**

-   Coordinates X,Y and Z click to mouse
-   The button create on point, axis, plane, copy vector axis form **FreeCAD.Vector(-24.0, 240.0, 7.0)**

**Sector 3: Value**

-   Length of the object if the object is a face perimeter is displayed unit size can be selected :
    km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique. If the object is circle one second lineEdit is open ans display the radius of circle.
-   Perimeter of the shape

**Sector 4: Vertexes and details**

-   CheckBox for for search or not all details of the object if is not checked only the principal value are displayed.
-   Vertexes and details of the shape (compt\_Edge), (compt\_Faces), (compt\_Vector of the Face)
    max 200 lines in the table, if there are more than 200 lines it appears (!+ 200) and the number of lines
    (full details can save be the **Save** button in a file in CSV format and can be viewed the file in spreadsheet with the **Read** or by an external spreadsheet as [LibreOffice](https://www.libreoffice.org/) [OpenOffice](http://openoffice.apache.org/downloads.html) or other)

**Sector 5: Inclination**

-   Inclinations of the object can be displayed in:
-   **decimal degree**, ex: 174.831872611°
-   **degree minute seconde**, ex: 174° 49\' 54.741401\'\'
-   **radian**, ex: 3.05139181449 rad
-   **grade**, ex: 194.257636235 gon
-   **pourcent** ex: 30° = 57.74%
-   Inclinations in planes XY, YZ, ZX and their coordinates
-   **Direction object**, give the direction of object the calculate is : coord\_1 - coord\_2 = direction (or reverse)
    -   
        **Line**
        
        this button create a line in direction of the object
-   **ValueAt**, returns the 3D vector corresponding to a parameter value.

**Sector 6: Surface and Volume**

-   Surface of the form displayed unit size can be selected
-   Surface of the face displayed unit size can be selected
-   Volume of the form displayed unit size can be selected
-   density of the material in **kg by dm3**
    (the \"spinBox\" is set to **7,5** kg, average density of steel. If you want a different default value, change the value of the density, line 204)
-   The **gram** buttom unit mass can be chosen :
    ton,quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
    lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct
-   weight of the form displayed unit mass can be selected

**Sector 7: BoundBox**

-   BoundBox extreme dimensions of the shape

**Sector 8: Center of:**

-   Center of the shape and these coordinates XYZ
-   Center of mass and these coordinates XYZ
-   The button create on point, axis, plane, copy vector axis form **FreeCAD.Vector(-24.0, 240.0, 7.0)**

**Sector 9: Inertia**

-   Moment of inertia and these coordinates length and weigth
-   The button create on point, axis, plane, copy vector axis form **FreeCAD.Vector(-24.0, 240.0, 7.0)**
    -   action line 1 : x1, y1, z1
    -   action line 2 : x2, y2, z2
    -   action line 3 : x3, y3, z3
    -   action 4 diagonal : x1, y2, z3

same for length and weigth

-   Determinant 1 : computes the determinant of the matrix scientific value
-   Determinant 2 : computes the determinant of the matrix decimal value

**Section 10: SpreadSheet**

-    **Read**: read the data in a spreadsheet saved **.FCInfo** or txt, asc, csv

-    **Save**: save the data in disk in the form selected below **.FCInfo** or txt, asc, csv

-    **Tabulation**: the separator is Tabulation

-    **Comma**: the separator is Comma

-    **Semicolon**: the separator is Semicolon

-    **Space**: the separator is Space

Option for save or read the spreadSheet with different separator, Tabulation, Comma, Semicolon, Space
The Tabulation are the separator for the FreeCAD spreadSheet module
The number of this four separator are calculate for help if unknown
The COMMA are the old (01.16 and before) separator of the FCInfo macro
Now for compatibility with the FreeCAD spreadSheet and since 01.17 version the TABULATION is the separator by default
If you want to convert your old FCInfo spreadsheet : Open it in FCInfo and save it with the Tabulation option checked

**Section 11: Main**

-    **CheckBox Clip Board**: if checked the coordinates are saved in clipBoard form : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    **CheckBox Point**: if checked one point is created in the coordinate displayed form : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    **CheckBox Axis **: if checked one axis is created in the coordinate displayed form : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    **CheckBox Plane**: if checked one axis plane is created in the coordinate displayed form : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    **Ref**: Refresh the display of data in report view

-    **Exit**: Exit the macro (you must restart from the tool bar button or menu \"View → Panels → FCInfo\"

-    **CheckBox****1** : If this CheckBox is checked the informations are displayed in the report view window

-    **CheckBox****2** : If this CheckBox is not checked the window macro are displayed to right (default). If it is checked the window macro are displayed to left

Once launched macro, the macro remains active and the window remains visible. To exit the macro by pressing **Exit**. If you leave by the cross, the macro remains in memory and the data appears in the \"report view\" of FreeCAD.


<center>

Image:Macro\_FCInfo\_04.png\|Docked to rigth, Image:Macro FCInfo 05.png\|or left with Combo view and reachable by a tab, or not docked to the choice.


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

Image:Macro FCInfo 02.png\|Understanding of angles in FCInfo display Image:Macro FCInfo 03.gif\|Understanding of angles in poucent in FCInfo display
click twice to see the animation (the image must be in full screen)


</center>




#### Weight unit : 

ton, quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct
the \"spinBox\" is set to **7,5** kg, average density of steel. If you want a different default value, change the value of the density, line 208


```python
 global densite       ; densite       = 7.5  # (steel = 7.5 kg par dm3)
```

A file can be created by the button **Save**. The file is written as a file [csv](https://fr.wikipedia.org/wiki/Comma-separated_values) in this way, the data can be studied in a spreadsheet in FreeCAD or Openoffice, LibreOffice\...

## Script

Copy the contents of the macro in a file named \"FCInfo.FCMacro\"

-   Windows: the form is usually **\" drive:\\Users\\your\_user\_name\\AppData\\Roaming\\FreeCAD\\ \"**
-   Ubuntu: the form is usually **\" /home/your\_user\_name/.FreeCAD \"**.

Or, directly in the interface of FreeCAD
The icon must be in the same directory as the macro.
Download image positioning on the icon <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> and then drag the mouse right click \"save as\" (do not change the name)
**PS: too long to be contained in the wiki page (for the time being the wiki pages accept only 64 KB) the macro code has been placed in the forum**


<div class="toccolours mw-collapsible mw-collapsed">

There is also FCInfo\_Alternate\_Linux for only for FreeCAD version 0.13\... and PyQt4


<div class="mw-collapsible-content">

There is also a [Macro\_FCInfo\_Alternate\_Linux](http://www.freecadweb.org/wiki/index.php?title=Macro_FCInfo_Alternate_Linux) here the code is changed (due to the character display error : **² ³ ° μ** ordinal not in range (128)\") which posed problems in certain configurations the functions are the same
Example : 
```python
global uniteSs       ; uniteSs       = u"mm²"
global uniteVs       ; uniteVs       = u"mm³"
global uniteAs       ; uniteAs       = u"°"
``` remplacés par 
```python
global uniteSs       ; uniteSs       = "mm"+iso8859(unichr(178))
global uniteVs       ; uniteVs       = "mm"+iso8859(unichr(179))
global uniteAs       ; uniteAs       = iso8859(unichr(176))
``` **Files saved with this version is incompatible with the other version (docked or not)**


</div>


</div>

Download the icon file [Macro\_FCInfo\_Icon](https://forum.freecadweb.org/download/file.php?id=50755) unzip and copy the icon in the same directory of the macro

Dwnload the macro file on gist **docked to right**


{{CodeDownload|https://gist.github.com/mario52a/8d40ab6c018c2bde678f|last version Macro_FCInfo and the icons at the end of the page}}

(Or **[On the forum.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=47748#p47748)** )
**PS:** this macro uses **getSelection()** and the list of object begin to 1 ex: for a box **Edge1 to Edge12** and the code in the console start at 0 ex: for a box **Edge\[0\] to Edge\[11\]**
This is normal the counting on arrays/lists inside OpenCascade always starts at **1 and not at 0**

### Limitations

Always leave the button **Exit**. If one exits the program without going through the button **Exit** the program remains in memory and continues to run and the display will remain in the \"view report\". You must leave FreeCAD to erase it from memory.
Only the first 200 elements of the object are visible in the table if there are more than 200 items in the object a signal will be displayed by \"\'(! +200)\" \'. The complete list of data is visible in the file saved by the button **Save**.
If the window macro is invisible after the run , see the bottom window :

![](images/Macro_FCInfo_08.png )

![](images/FCInfo_begin_00.gif ) 

project:
~~read the file directly in a table.~~ done
~~matches the \"Edges\" and their coordinates~~ done
Association of a substance to its density
~~inclination on the element rather than the global object~~ done
~~inlay right in the interface of FreeCAD~~ done

## Version

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
-   ver 1.21-2.01 (1.21-rmu) 11/06/2019 rmu replace all characters over 127 in ex: \"°\" in chr(176)) \#degree
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
-   ver 1.13 , 27/07/2014 replace FCInfo\_en\_Ver\_1-12\_Docked.FCMacro to FCInfo\_en\_Ver\_1-13\_Docked.FCMacro accept PyQt4 and PySide
-   ver 1.12 , 10/03/2014 adding tooltip
-   ver 1.11 , 04/03/2014 adding µm, nm, pm, fm, µg, ng, pg, pourcent, fixed of grandeur carat ~~\"cd\"~~ in **\"ct\"**, display of the label and internal name, fixed calculation of angles XY YZ ZX could give an error on a compound shape, window dockable in FreeCAD
-   ver 1.10.b , 19/11/2013 buttons outside the scrollbar and the dimensions of the window blocking

(ver 1.10 , 18/11/2013 create scrollbar)
\*ver 1.08.b , 10/11/2013 translation units in English, error correction to display the area of the faces listed in the table and replacement of the\"**print**\" by \"**App.Console.PrintMessage**\"
~~ver 1.09 , 04/11/2013 works perfectly on Windows and Linux (cause of errors on Linux the characters : ² ³ ° \"ordinal not in range(128)\")~~
In a Linux distribution and in the case of an error of **\"ordinal not in range (128)\"** an alternative version exists on this page [Macro\_FCInfo\_Alternate\_Linux](Macro_FCInfo_Alternate_Linux.md)
\*ver 1.08 , 24/10/2013 correction of high top \"Faces\" and \"Edges\" displaying 100 objects (in the saved file)
\*ver 1.07 , 11/10/2013 matches the \"Faces\" and their coordinates.
\*ver 1.06 , 22/09/2013 matches the \"Edges\" and their coordinates, inclination on the element rather than the global object
\*ver 1.05 , 17/09/2013 added an icon for the spreadsheet, conversion barrel fr, affichage des dimensions overall instead of coordinates.
\*ver 1.04 , 11/09/2013: read the file directly in a table.
\*ver 1.03 , 09/09/2013: clearer display in view report and replacement by \"typeObject = sel\[0\].Shape.ShapeType\"
\*ver 1.02 , 7/09/2013 : small updates
\*ver 1.00 , 6/09/2013

## Links

SeeAlso [Arch Survey](Arch_Survey.md) <img alt="Arch Survey" src=images/Arch_Survey.svg  style="width:36px;">

You can share your comments on the forum [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)
Here another post of [FCInfo Macro](http://forum.freecadweb.org/viewtopic.php?f=8&t=6005)

---
[documentation index](../README.md) > Macro FCInfo/en
