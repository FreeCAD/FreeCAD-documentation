---
- TutorialInfo   *   Topic   *Arch Workbench
   Level   *Advanced
   Time   *120 minutes
   Author   *Pablo Gil
   FCVersion   *0.19.x
   Files   *
}}

## Introduction

It was a such a hard investigation on how to get a working copy of IfcOpenShell-python on OSX/macOS in order to import/export IFC files that I\'m sharing this tutorial in case it helps more people. My system is OSX 10.11.6, 64bits with Python 2.7.11, it might work for you if you have also OSX as they are often 64bits but may differ from mine. The procedure might be very similar if you run Linux or Windows but it probably have some differences.

## Requirements

-   [IfcOpenShell](IfcOpenShell.md)
-   FreeCAD v0.19 or higher

## Steps

1\. Download or clone the full GitHub project at <https   *//github.com/IfcOpenShell/IfcOpenShell> (it will always be the newest version)

   *   
    `git clone https   *//github.com/IfcOpenShell/IfcOpenShell
---

# Import/Export IFC - compiling IfcOpenShell/en

     

2\. From a terminal go to **/nix/** folder and launch the script. In OSX it is executed with   * 
```python
cd nix/
./build-all.sh
``` It will take from 30 up to 120 minutes to compile everything. It\'s not the smarter way of compiling [IfcOpenShell](IfcOpenShell.md) but this simple script will compile all dependencies, Python versions, etc.

3\. Once it finishes (I don\'t remember now but it will be printed something like \"Built IfcOpenShell\...\" and it will return to your prompt) you will have a new folder **/IfcOpenShell/build/** full of files and folders. From my personal experience, two weeks ago the nix \"build-all.sh\" script didn\'t finished successfully but after trying it yesterday with the newest updates it worked fine so I guess you might experience something similar in case the development goes further\... So now you have everything you need but you have to do some manual work in order to get it working   *

4\. Open FreeCAD and open the [Python console](Python_console.md) and [Report view](Report_view.md). Then write into the Python console the following   * 
```python
import sys
print sys.path
``` You will get a looooong line with all the paths that FreeCAD reads. You may be able to install IfcOpenShell in any of them but I suggest you to place it inside one where you find a **/site-packages/** after a **/Python/** or **/python-something/**. In my case it was **/Library/Python/2.7/site-packages**. (Note   * you will find paths inside your app directory but I suggest you to not use them because then IfcOpenShell will only be available for this app)

5\. Once located where you want/have to install it, go there with your file browser (Finder in OSX). That is, go inside **/site-packages/** folder

   *   
    {{incode|cd site-packages/`
    

6\. Open a new file browser window and navigate to your downloaded GitHub project   * **/IfcOpenShell/src/ifcopenshell-python/** and copy the full **/ifcopenshell/** folder

7\. Paste it inside **/site-packages/** folder. Now you should have something like   * 
```python
/site-packages/ifcopenshell/__init__.py
/site-packages/ifcopenshell/entity_instance.py
/site-packages/ifcopenshell/file.py
/site-packages/ifcopenshell/geom/app.py
/site-packages/ifcopenshell/geom/main.py
/site-packages/ifcopenshell/geom/occ_utils.py
/site-packages/ifcopenshell/geom/__init__.py
/site-packages/ifcopenshell/guid.py
```

8\. Now we have to pick to files inside the /build/ folder, they are   * 
```python
_ifcopenshell_wrapper.so
ifcopenshell_wrapper.py
``` but as we have compiled everything you will have to pick the one that matches with your FreeCAD Python version. Check it easily reading the first line inside your FreeCAD [Python console](Python_console.md) view. In my case it was Python 2.7.11.

9\. Now go let\'s copy the files inside the place it corresponds to your Python version. In my case it was   * 
```python
/IfcOpenShell/build/Darwin/x86_64/build/ifcopenshell/[b]python-2.7[/b].10/ifcwrap/
```

10\. Paste them inside **/site-packages/ifcopenshell/**

11\. Check everything is in place   * 
```python
/site-packages/ifcopenshell/__init__.py                  (1)
/site-packages/ifcopenshell/entity_instance.py           (1)
/site-packages/ifcopenshell/_ifcopenshell_wrapper.so     (2)
/site-packages/ifcopenshell/file.py                      (1)
/site-packages/ifcopenshell/geom/__init__.py             (1)
/site-packages/ifcopenshell/geom/app.py                  (1)
/site-packages/ifcopenshell/geom/main.py                 (1)
/site-packages/ifcopenshell/geom/occ_utils.py            (1)
/site-packages/ifcopenshell/guid.py                      (1)
/site-packages/ifcopenshell/ifcopenshell_wrapper.py      (2)
```

\(1\) from GitHub project
(2) from /build/ folder

12\. Close and reopen FreeCAD

## Testing

Now that it is installed, let\'s check if everything works as expected   *

12.1 in the Python console write   * 
```python
import ifcopenshell
from ifcopenshell import geom
``` if it doesn\'t throw any error it means it may be correctly installed

12.2 Go to [Yorik\'s FreeCAD manual](Manual_BIM_modeling.md), navigate to the lower part of the page and download the following files to test   * 
```python
house.FCStd
house.ifc
```

12.3 Open **house.FCStd**, select the root \"Building\" object and export it (**File → Export**) setting the File type to \"Industry Foundation Classes (\*.ifc)\". Press **Save** and if it works and it doesn\'t throw an error in the [Report view](Report_view.md) then it\'s working.

12.4 Final test, import **house.ifc** into a new file so open a new file and import that file\... it will take a while.

13\. Enjoy BIM with FreeCAD!

## Final thoughts 

My opinion is that FreeCAD itself should have precompiled versions of IfcOpenShell bundled with the distribution because building it by yourself is a total pain and average user won\'t do it (they don\'t know how to compile, manage GitHub, etc), but well, maybe in the future.

I hope it helps you.

Cheers

## Links

-   Related forum thread [discussion](http   *//forum.freecadweb.org/viewtopic.php?f=23&t=17536)
-   [IfcOpenShell](IfcOpenShell.md)


{{Userdocnavi

}}

[Category   *BIM](Category_BIM.md) [Category   *Arch](Category_Arch.md) [Category   *3rd Party](Category_3rd_Party.md) [Category   *File_Formats](Category_File_Formats.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [BIM](Category_BIM.md) > [Arch](Category_Arch.md) > [3rd Party](Category_3rd Party.md) > [File_Formats](Category_File_Formats.md) > Import/Export IFC - compiling IfcOpenShell/en
