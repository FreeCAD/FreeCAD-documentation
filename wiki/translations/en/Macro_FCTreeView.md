# Macro FCTreeView/en
 {{Macro
|Name=Macro FCTreeView
|Icon=Macro_FCTreeView.png
|Description={{ColoredText|#ff0000|#ffffff|New version GUI modifyed for the HD dpi (QGridLayout) run only FC version 0.18 and more (PySide2 Qt5)}} <br/> <br/>Macro for list all objects in the project in one list without hierarchy, options sort by name, label, visibility, group, by length option search by name, label .... without case sensitive or with case sensitive and select all objects displayed in the macro window. <br/> <br/>For the precedent version see [https://gist.githubusercontent.com/mario52a/67517ef758ff20005d0a6adcfd8c9190/raw/0a92d7f591a0a179f84b2fc417046723b4d7b0e6/Macro_FCTreeView.FCMacro Macro_FCTreeView.FCMacro] and install it manually.
|Author=Mario52
|Version=00.09
|Date=2020-09-24
|FCVersion=0.18 and below
|Download=[https://forum.freecadweb.org/download/file.php?id=70498 Macro FCTreeView Icon package] unzip the .zip file and copy the icon in your macro directory.
}}

## Description

Macro for list all objects in the project in one list without hierarchy, options sort by name, label, visibility, group, by length option search by name, label \.... without case sensitive or with case sensitive and select all objects displayed in the macro window. {{Codeextralink|https://gist.githubusercontent.com/mario52a/67517ef758ff20005d0a6adcfd8c9190/raw/59bc2028978c82744c83c6b138ab3ef30e0bf6f3/Macro_FCTreeView.FCMacro}}

## How To Use 

![Macro FCTreeView](images/FCTreeView.gif ) 

### Section **Window** 

The title display the option, number and type object(s) displayed

-   **O** = Objects
-   **N** = Name
-   **L** = Label
-   **T** = Total
-   **G** = Group
-   **S** = Single
-   **V** = Visible
-   **H** = Hidden

If one object are selected : the Placement Base, Rotation and Center of mass is displayed (if available !) ![Icon used for the Name of object](images/Macro_FCTreeView_00.png ) Icon used for the Name of object (the scrollbar is colored blue)

![Icon used for the Label of object](images/Macro_FCTreeView_05.png ) Icon used for the Label of object (the scrollbar is colored blue clear)

![Icon used for visualise if the object is status Visible (mouse click for Hidden)](images/Macro_FCTreeView_01.png ) Icon used for visualise if the object is status Visible (mouse click for Hidden) (the scrollbar is colored green)

![Icon used for visualise if the object is status Hidden (mouse click for Visible)](images/Macro_FCTreeView_02.png ) Icon used for visualise if the object is status Hidden (mouse click for Visible) (the scrollbar is colored red)

![Icon used for the Name contains objects (or folder Group)](images/Macro_FCTreeView_17.png ) Icon used for the Name contains objects (or folder Group)

![Icon used for inform the object in a group the number objects is displayed in top group](images/Macro_FCTreeView_03.png ) Icon used for inform the object in a group the number objects is displayed in top group (the scrollbar is colored red clear)

![Icon used for displayed the single object (not group)](images/Macro_FCTreeView_04.png ) Icon used for displayed the single object (not group)

### Section **Sort by :** 


**<img src=images/Macro_FCTreeView_10.png style="width:18px"> Name**

Icon used for flip/flop normal/reverse the data listing sort by Name


**<img src=images/Macro_FCTreeView_11.png style="width:18px"> Label**

Icon used for flip/flop normal/reverse the data listing sort by Label


**<img src=images/Macro_FCTreeView_12.png style="width:18px"> Visible**

Icon used for flip/flop normal/reverse the data listing sort by Visibile/Hidden


**<img src=images/Macro_FCTreeView_13.png style="width:18px"> Group**

Icon used for flip/flop normal/reverse the data listing sort by Group/Single object


**<img src=images/Macro_FCTreeView_19.png style="width:18px"> Length**

If this check Box is checked the sort is created by length with the button clicked (Name, Label \...)

### Section **Global** 


**<img src=images/Macro_FCTreeView_21.png style="width:18px"> Split**

flip/flop Split the Name list


**<img src=images/Macro_FCTreeView_22.png style="width:18px"> Split**

flip/flop Split the Name and Label list


**<img src=images/Macro_FCTreeView_14.png style="width:18px"> Expend**

flip/flop the data listing Fold/Expend


**<img src=images/Macro_FCTreeView_15.png style="width:18px"> Expend**

flip/flop the data listing Expend/Fold


**<img src=images/Macro_FCTreeView_06.png style="width:18px"> Visibility**

flip/flop normal/Visibility


**<img src=images/Macro_FCTreeView_07.png style="width:18px"> Group**

flip/flop normal/Group


**<img src=images/Macro_FCTreeView_16.png style="width:18px"> Reload**

reload the data in the project


**<img src=images/Macro_FCTreeView_18.png style="width:18px"> Original**

return in original organisation after operation visibility/Hidden


**<img src=images/Macro_FCTreeView_01.png style="width:18px"> All Visible**

visualise if the object is status Visible


**<img src=images/Macro_FCTreeView_02.png style="width:18px"> All Hidden**

visualise if the object is status Hidden

### Section **Search** 


**<img src=images/Macro_FCTreeView_20.png style="width:18px"> Clear**

Clear the search line edit

#### The radioButton options **Search**: 

-   **(\"NLwc\")** : Search by Name and Label **W**ithout respecting the sensitive **C**ase

-   **(\"Nsc\")** : Search by Name and respecting the **S**ensitive **C**ase

-   **(\"Lwc\")** : Search by Label **W**ithout respecting the sensitive **C**ase

-   **(\"NLsc\")** : Search by Name and Label and respecting the **S**ensitive **C**ase

-   **(\"NLwsc\")** : Search by Name and Label in Word and respecting the **S**ensitive **C**ase (same panel selection of FreeCAD)

-   **(Nu)** : Search by numeric value (radius, length, angle \.....) see version section


**<img src=images/Macro_FCTreeView_23.png style="width:18px"> Select**

flip/flop for Selected all object(s) displayed in the window


**<img src=images/Macro_FCTreeView_24.png style="width:18px"> Unselected**

flip/flop Unselected all object(s)


**<img src=images/Macro_FCTreeView_25.png style="width:18px"> S Sheet**

access in Spreadsheet options

### The SpreadSheet options: 

![Macro FCTreeView](images/TreeView_SpeadSheet.gif ) 

![](images/Macro_FCTreeView_001.png )

![](images/Macro_FCTreeView_002.png )

-   CheckBox options for select the data to save in spreadsheet


**<img src=images/Macro_FCTreeView_28.png style="width:18px"> Select**

: Select all checkBox option to save


**<img src=images/Macro_FCTreeView_29.png style="width:18px"> Select**

: unSelect all checkBox option to save

![](images/Macro_FCTreeView_003.png )

-   **Value** : alone the value is saved in the cell
    -   Ex : 10.00 ![](images/Macro_FCTreeView_30.png )
-   **Val Gr** : the value and the unit are saved in unique cell
    -   Ex : 10.00 mm ![](images/Macro_FCTreeView_31.png )
-   **Val Gr Ph** : the value, the unit and the physic data is saved in unique cell
    -   Ex : 10.00 mm Length ![](images/Macro_FCTreeView_32.png )
-   **Split** : if the Split checkBox is checked, the data is cut saved in separate cell
    -   Ex : 10.00 \| mm \| length ![](images/Macro_FCTreeView_33.png )

![](images/Macro_FCTreeView_004.png )

-   Combobox **mm** : select the unit length desired. The value is convert in the selected unit. The units length available are:
    -   km, hm, dam, m, dm, cm, **mm**, um, nm, pm, fm, in, lk, ft, yd, rd, ch, fur, mi, lea, nmi
-   Combobox **gram** : select the unit weight desired. The value is convert in the selected unit. The units weight available are:
    -   t, q, kg, hg, dag, **g**, dg, cg, mg, µg, ng, pg, fg, gr, dr, oz, oz t, lb, t lb, st, qtr, cwt, tonneau fr, ct
-   Spinbox **Densite** : give the density by dm3 of the material used (Default : 1.0000)
-   Spinbox **Round** : give the round value desired (Default : 3)

![](images/Macro_FCTreeView_005.png )

-   Combobox **Name spreadSheet** : List the spreadsheet in the document
-   Line edit **Name spreadSheet** : Display the actual spreadsheet or give the name for the new spreadsheet

![](images/Macro_FCTreeView_006.png )


**<img src=images/Macro_FCTreeView_28.png style="width:18px"> Select**

select all checkbox options


**<img src=images/Macro_FCTreeView_29.png style="width:18px"> Unselect**

unselected all checkbox options


**<img src=images/Macro_FCTreeView_27.png style="width:18px"> Save**

save the data in Spreadsheet displayed. if no spreadsheet is active the spreadsheet named **FCSpreadSheet** is created


**<img src=images/Macro_FCTreeView_26.png style="width:18px"> Quit**

quit the Spreadsheet options

### Icons

The icon must be copied into the same directory as the macro [Macro\_FCTreeView\_Icon](https://forum.freecadweb.org/download/file.php?id=70498)

![Icon used for the Name of object](images/Macro_FCTreeView_00.png ) ![Icon used for visualise if the object is status Visible (mouse click for Hidden)](images/Macro_FCTreeView_01.png ) ![Icon used for visualise if the object is status Hidden (mouse click for Visible)](images/Macro_FCTreeView_02.png ) ![Icon used for inform the object in a group the number objects is displayed in top group](images/Macro_FCTreeView_03.png ) ![Icon used for displayed the single object (not group)](images/Macro_FCTreeView_04.png ) ![Icon used for the Label of object](images/Macro_FCTreeView_05.png ) ![Icon used for flip/flop normal/Visibility](images/Macro_FCTreeView_06.png ) ![Icon used for flip/flop normal/Group](images/Macro_FCTreeView_07.png ) ![Icon used for Reverse the data listing (momentarily not used)](images/Macro_FCTreeView_08.png ) ![Icon used for quit Macro FCTreeView (momentarily not used)](images/Macro_FCTreeView_09.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Name](images/Macro_FCTreeView_10.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Label](images/Macro_FCTreeView_11.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Visibility/Hidden](images/Macro_FCTreeView_12.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Grout/Single object](images/Macro_FCTreeView_13.png ) ![Icon used for flip/flop the data listing Fold/Expend](images/Macro_FCTreeView_14.png ) ![Icon used for flip/flop the data listing Expend/Fold](images/Macro_FCTreeView_15.png ) ![Icon used for reload the data in the project](images/Macro_FCTreeView_16.png ) ![Icon used for the Name contains objects (or folder Group)](images/Macro_FCTreeView_17.png ) ![Icon used for return in original organisation after operation visibility/Hidden](images/Macro_FCTreeView_18.png ) ![If this check Box is checked the sort is created by length with the button clicked (Name, Label \...)](images/Macro_FCTreeView_19.png ) ![Icon used for Clear the search line edit](images/Macro_FCTreeView_20.png ) ![Icon used for flip/flop Split the Name list](images/Macro_FCTreeView_21.png ) ![Icon used for flip/flop Split the Name and Label list](images/Macro_FCTreeView_22.png ) ![Icon used for Selected all object(s) displayed in the window](images/Macro_FCTreeView_23.png ) ![Icon used for Unselected all object(s)](images/Macro_FCTreeView_24.png ) ![Icon used for access in Spreadsheet options](images/Macro_FCTreeView_25.png ) ![Icon used for quit the Spreadsheet options](images/Macro_FCTreeView_26.png ) ![Icon used for save the data in Spreadsheet](images/Macro_FCTreeView_27.png ) ![Icon used for select all checkbox options](images/Macro_FCTreeView_28.png ) ![Icon used for unselected all checkbox options](images/Macro_FCTreeView_29.png ) ![Icon used for save the value data in Spreadsheet](images/Macro_FCTreeView_30.png ) ![Icon used for save the value and Unit data in Spreadsheet](images/Macro_FCTreeView_31.png ) ![Icon used for save the value, Unit and type data in Spreadsheet](images/Macro_FCTreeView_32.png ) ![Icon used for split the value, Unit and type in cell separate in Spreadsheet](images/Macro_FCTreeView_33.png )

## Script

For prevent many instance the clic on ToolBar button are effect flip/flop (hide/visible)

The macro is located in right dock for change it modify the value line number 133 **testing = 0** (or change it with the mouse as a widget normal)

The icon ToolBar ![Macro FCTreeView](images/Macro_FCTreeView.png )

**Macro\_FCTreeView.FCMacro**


{{CodeDownload|https://gist.github.com/mario52a/67517ef758ff20005d0a6adcfd8c9190|Macro_FCTreeView.FCMacro}}

## To do 

~~Docked the macro~~

## Version

ver 00.09 (2020-09-24) : correct the \"**freeze**\" macro after call the **assembly4 workbench** i try activate \"**Class SelObserver**\" and it work ???


```python
class SelObserver:
    def addSelection(self, document, object, element, position):  # Selection
        global sourisPass
        global listeSorted
        global ui

        None
```

ver 00.08 (2020-02-25) : upgrade with Layout

ver 00.07 (06/05/2018) : modify procedure for search the last cell used

ver 00.06 (13/12/2017) : correct little bug line del line num 1881 \"del listeSortedBis\[doublon\]\[4:\] \# supprime le fond inutile\" thanks renatorivo

ver 00.05 (27/11/2017) : add creation spreadsheet and many option for him

ver 00.04 (29-09-2017) : add search by numeric value (length, radius\....)

values researched :


```python
global impost                 ; impost = ["Angle","Angle0","Angle1","Angle2","Angle3","ChamferSize","Circumradius","Columns","Degree",
                                          "FilletRadius","FirstAngle","Growth","Height","LastAngle","Length","Length2","MajorRadius",
                                          "MinorRadius","Pitch","Polygon","Radius","Radius1","Radius2","Radius3","Rows","Size","Width",
                                          "X","X1","X2","Xmax","Xmin","X2max","X2min",
                                          "Y","Y1","Y2","Ymax","Ymin","Y2max","Y2min",
                                          "Z","Z1","Z2","Zmax","Zmin","Z2max","Z2min"]
```

ver 00.03 (23/09/2017) : add search by type object

ver 00.02 (11/09/2017) : modify for docked and prevent many instance the clic on button are effect flip/flop (macro hide/visible)

ver 00.01 (08/09/2017) :
