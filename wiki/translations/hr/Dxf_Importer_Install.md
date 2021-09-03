


<div class="mw-translate-fuzzy">


{{TutorialInfo/hr|Topic=SampleClass|Level=Medium user|Time=15 minutes|Author=[Mario52](User:Mario52.md)|FCVersion=All}}


</div>

### Description

This page explains step by step the margin to follow to install the package Draft-dxf-import yorikvanhavre for you to upload files in DXF format FreeCAD and import DWG files using the teighafileconverter utility. This installation was made in the Windows Vista environment, but the principle of the system is the same for linux

### First step: 

identify the macros folder FreeCAD

**1 :** open FreeCAD


<div class="mw-collapsible mw-collapsed toccolours">

If you have a version from 0.15 you can use the automatic update DXF package (expand to see)


<div class="mw-collapsible-content">

<img alt="Automatic DXF install" src=images/Dxf_Importer_Install_01b.png  style="width:640px;"> 


</div>


</div>

**2 :** click **Menu \> Macro \> Macros** or the click the bottom <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> \"Open a dialog to let you execute a macro Recorded\"

![open FreeCAD](images/Dxf_Importer_Install_01.png ) 

**3 :** one dialog box open

**4 :** copy the address of \"Macro destination\" (here **C:\\Users\\d\\AppData\\Roaming\\FreeCAD\\**) In Ubuntu, this is normally **/home/your\_user\_name/.FreeCAD**

![Open a dialog to let you execute a macro Recorded](images/Dxf_Importer_Install_02.png ) 

**5 :** paste the address into your browser and confirm

![paste the address into your browser](images/Dxf_Importer_Install_03.png ) 

**6 :** leave open the explorer

![](images/Dxf_Importer_Install_04.png ) 

**7 :** Close FreeCAD

### Second step: 

Download the files

**8 :** download files on the page <https://github.com/yorikvanhavre/Draft-dxf-importer>

**9 :** and click the icon button **Download ZIP** for the default version.


<div class="mw-collapsible mw-collapsed toccolours">

(or choice for your development version see down page) (expand to see)


<div class="mw-collapsible-content">

<img alt="Automatic DXF install" src=images/Dxf_Importer_Install_05b.png  style="width:640px;"> 


</div>


</div>

![download files](images/Dxf_Importer_Install_05.png ) 

**10 :** you must extract the file to a temporary directory (here **c:\\tmp**)

![extract the file](images/Dxf_Importer_Install_06.png ) 

**11 :** the decompresser creates a new folder named \"**Draft-dxf-import-master**\"

![decompresser creates a new folder](images/Dxf_Importer_Install_07.png ) 

**12 :** the files are in this folder select all the files and \"Cut\"

![select all the files and Cut](images/Dxf_Importer_Install_08.png ) 

**13 :** paste the files in the folder FreeCAD macros in the explorer open (step 6) (**C:\\Users\\d\\AppData\\Roaming\\FreeCAD\\**)

In Ubuntu, this is normally **/home/your\_user\_name/.FreeCAD**

![paste the files in the folder](images/Dxf_Importer_Install_09.png ) 

**14 :** Open FreeCAD click the button <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> , the necessary files in DXF format are present, close the window \"Execute macro

![open FreeCAD](images/Dxf_Importer_Install_15.png ) 

**15 :** load your DXF file

![load your DXF file](images/Dxf_Importer_Install_10.png ) 

**16 :** DXF file can be used

![DXF file can be used](images/Dxf_Importer_Install_11.png ) 

**VERSIONS**

This repository contains several versions of the DXF importer. The default version, that you download when you press the \"download ZIP\" button above, is always the version needed by the current stable version of FreeCAD.

If you use another version of FreeCAD, for example a development version or an older version, you might also need another verison of this DXF library. You can find out which version of the DXF library is needed by your version of FreeCAD, by entering the following code in the FreeCAD python console: 
```python
import importDXF
print importDXF.CURRENTDXFLIB
```

### Third step: 

Download Teigha converter for use DWG files

**17 :** teighafileconverter download on [teighafileconverter page](http://www.opendesign.com/guestfiles/teighafileconverter)

![download Teigha](images/Dxf_Importer_Install_12.png ) 

**18 :** choose the version that suits your Qt and OS

![choose the version](images/Dxf_Importer_Install_13.png ) 

**19 :** and install it on your system ![install it on your system](images/Dxf_Importer_Install_14.png ) 

**20 :** open FreeCAD and click the button <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> \"Open a dialog to let you execute a macro Recorded\"

**21 :** close the macros window

**22 :** and activate the Draft workbench

![activate the Draft workbebch](images/Dxf_Importer_Install_16.png ) 

**23 :** now let\'s get into the options page DXF / DWG click \"Menu \> Edit \> Preferences\"

![Menu \> Preferences](images/Dxf_Importer_Install_17.png ) 

**24 :** select \"Draft \> DXF / DWG options\" tab

**25 :** In the DWG format option section, click the 3 points **\...** ![Draft \> DXF / DWG options](images/Dxf_Importer_Install_18.png ) 

**26 :** to give way Teigha converter that FreeCAD will use to convert DWG to DXF

**27 :** enter in the directory here in Window here \"**C:/Program Files/ODA/Teigha File Converter 4.00.1/**\" and select TeighaFileConverter.exe and confirm

![DWG format option](images/Dxf_Importer_Install_19.png ) 

**28 :** the operation is completed click the **OK** you can test a DWG file

![directory Teigha File Converter 4.00.1](images/Dxf_Importer_Install_20.png ) 

### Fourth step: 

Using Teigha. Teigha is a full program and you can use it without FreeCAD

![directory Teigha File Converter 4.00.1](images/Dxf_Importer_Install_21.png ) 

**1 :** Imput folder: folder path or are the DXF or DWG files to convert

**2 :** Output folder: path to the destination folder for the converted files

**3 :** Recurse folder:

**4 :** Audit:

**5 :** Input files filter: filter for only DXF, DWG or DXF and DWG

**6 :** Output release: the file will be converted to the format and the selected version

**7 :** Start: launches the process

### Links

Video tutorial [FreeCAD Tutorial 24 - DXF/DWG Import](https://www.youtube.com/watch?v=wHxTWuDhc3M)
