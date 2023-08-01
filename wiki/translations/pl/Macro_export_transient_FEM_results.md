# Macro export transient FEM results/pl
{{Macro
|Name=export transient FEM results
|Description=Export multiple FEM results from a transient analysis for post-processing in ParaView.
|Download=[https://drive.google.com/file/d/1MSBxLPlQ-TwzF-sFkgOeFb48zij5_scp/view?usp=sharing Macro file (3 kB)]<br/>[https://drive.google.com/file/d/1m3RiJ-JM7QSJ6YDhZnafHIbyL92V6sYU/view?usp=sharing Example file without results (200 kB)]<br/>[https://drive.google.com/file/d/157aIdVpIyfpVW9WxL-ReGz0FIsQebH_q/view?usp=sharing Example file with results (10 MB)]<br/>[https://drive.google.com/file/d/1g-QOJtl3G5KaY2bSrw03NNQ8mnfBi03T/view?usp=sharing All example files, including the vtk-export folder (21 MB)]
|Author=Luftschraube
|Version=0.1
|Date=2019-08-30
|FCVersion=All
}}

## Description

This macro exports multiple FEM result objects from a transient analysis to the VTK format and generates a PVU file which can be used to load the results directly into ParaView for post-processing.

## Background

A transient analysis in FreeCAD ends up with a bunch of FEM result objects, one for each timestamp. The individual results can be investigated directly in FreeCAD and be post-processed using [pipelines](FEM_PostPipelineFromResult.md). However, the possibilities within FreeCAD are still limited, especially for transient analyses. A better tool for post-processing and visualisation is ParaView. You can export single FEM result objects from FreeCAD as a .vtk or .vtu file, which can then be opened with ParaView. Unfortunately, the FEM workbench doesn\'t support the export of multiple .vtk files at one time (yet). That\'s where this macro comes into play.

## How to use (experienced users) 

Run the macro on a FreeCAD project that includes several FEM result objects from a transient analysis. Besides the .FCStd file, a new folder \'vtk-export\' will be created, containing the individual results (.vtu files), and a .pvu file that can be opened from ParaView.

## How to use (step-by-step with example) 

As an example, the bending of a aluminium/steel bimetal strip is used. A step-by-step guide to create the sample file is given [here](Transient_FEM_analysis.md), or you can download the file from the [downloads section](#Downloads.md) of this page. Save the FCMacro file in the FreeCAD macro folder, which can be found via Edit → Preferences → General → Macro.

With the example file opened, we go to Macro → Macros\..., select \"ExportTransientResults_190830.FCMacro\" (or whatever name you saved it as) and execute it. The macro will now create a subfolder \'vtk-export\' besides the .FCStd file. Depending on the number and size of the result objects, this may take some time. In the Report View (View → Report View), we should see \'Macro finished\', if eveything went fine - or some error messages. (Note: Sometimes messages like \'PropertyFloatList NOT exported to vtk\' appear, but I was able to work with the VTK files anyway\...) In the subfolder \'vtk-export\', we will find .vtu files, one for each result set for each timestamp. Additionally, a .pvd file is created, which tells ParaView which result set belongs to which timestamp.

Now, we open ParaView and go to File → Open\... and open the .pvd file. In the \'Properties\' tab, we click \'Apply\' to load the results. In the \'Information\' tab we will see a list of *Index* and *Value*, corresponding to the timestamps of the results that we just imported. (Of course, it always makes sense to check if the times given here are correct or if something strange happened during the export.) From here, we can use ParaView to play around with the results. Since ParaView offers a lot of possibilities, please refer to the appropriate documentations around the internet.

For demonstrating purposes, let us now visualise the temperature of the bent bimetal strip: In the \'properties\' tab on the left, under \'coloring\' we select temperature, and the image gets color-mapped according to the local temperature. Via the little icon with a heart, we select the color scale \'cool to warm\'. With the recorder-like icons on the top, we can move through all the individual results that were created during the analysis. The \'play\' button will display the individual images in their sequence. However, the individual results are not separated by a constant time interval, so the animation is not proportional in time.

What we need is an interpolation of the results in between the time steps, which is available via Filters → Temporal → Temporal Interpolator. Here we choose again the temperature for coloring. In the \'animation view\' (View → Animation View), we can now switch from \'sequence\' mode to \'real time\' mode. We can also set the start time (default is 0.01 s), the end time, and the duration. While start and end time refer to simulation time, the duration is the actual real time that the animation takes to play completely. With 10 s duration, our 60 s simulation time will be squeezed into 10 s real time.

We go one step further and want to visualise the actual bending of the strip. With the Temporal Interpolator selected, we add Filters → Common → Warp by Vector. Under \'vectors\' we choose \'DisplacementVectors\' and set the \'scale factor\' to 10. When we play the animation now, we can actually see the color-mapped strip bending (exaggerated by a factor of 10).

<img alt="" src=images/Transient_FEM_Bimetal_ParaView_(1).JPG  style="width:700px;"> 

The post-processing we have just done can be saved as a \'state\' in ParaView, which can be opened any time again and even be applied to a different set of results.

## Downloads

-   [Macro file (3 kB)](https://drive.google.com/file/d/1MSBxLPlQ-TwzF-sFkgOeFb48zij5_scp/view?usp=sharing)
-   [Example file without results (200 kB)](https://drive.google.com/file/d/1m3RiJ-JM7QSJ6YDhZnafHIbyL92V6sYU/view?usp=sharing)
-   [Example file with results (10 MB)](https://drive.google.com/file/d/157aIdVpIyfpVW9WxL-ReGz0FIsQebH_q/view?usp=sharing)
-   [All example files, including the vtk-export folder (21 MB)](https://drive.google.com/file/d/1g-QOJtl3G5KaY2bSrw03NNQ8mnfBi03T/view?usp=sharing)

## Script

The ToolBar Icon

**Macro_export_transient_FEM_results.FCMacro**


{{MacroCode|code=
#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Macro to export multiple FEM results objects from a transient analysis for
# post-processing in ParaView.
#
# Created by <Luftschraube> under the GNU Lesser General Public License (LGPL)
#
# Version 0.1 (30.08.2019)
#

import FreeCAD
import Fem
import feminout.importVTKResults
import os
from sys import exit

FreeCAD.Console.PrintMessage(">>>Macro started\n")

#Get the file path and name of the active document 
p = FreeCAD.ActiveDocument.FileName
FilePath = "/".join(p.split("/")[:-1])
FileName = p.split("/")[-1].split(".")[0]
FreeCAD.Console.PrintMessage("File path:" + FilePath + "\n")
FreeCAD.Console.PrintMessage("File name:" + FileName + "\n")
FreeCAD.Console.PrintMessage("\n<<<Macro finished with errors\n")

#Get FEM result objects into a list
FreeCAD.Console.PrintMessage("Looking for result objects...")
FEMResultObjects = []

for obj in App.ActiveDocument.Objects:
    if obj.TypeId == "Fem::FemResultObjectPython":  
        FEMResultObjects.append(obj.Label)
        #FreeCAD.Console.PrintMessage(obj.Label + '\n')

NumberOfResultObjects = len(FEMResultObjects)
FreeCAD.Console.PrintMessage(str(NumberOfResultObjects) + " found\n")

if NumberOfResultObjects > 0:#Export result objects as .vtu file and generate .pvu file
    ExportFolderName = "vtk-export"
    ExportOutputPath = FilePath + "/" + ExportFolderName
    if not os.path.exists(ExportOutputPath):
        os.makedirs(ExportOutputPath)
        FreeCAD.Console.PrintMessage(ExportOutputPath + " has been created\n")
    else:
        FreeCAD.Console.PrintMessage(ExportOutputPath + " already exists\n")PVUFile = open(ExportOutputPath + "/" + FileName + ".pvd","w")
    PVUFile.write("<VTKFile type=\"Collection\" version=\"1.0\" byte_order=\"LittleEndian\" header_type=\"UInt64\">\n\t<Collection>\n")n = 0
    for ExportObject in sorted(FEMResultObjects):
        n = n + 1
        
        #Read and format time stamp (e.g., 12.37 s = 0001237)
        FreeCADResultLabelParts = ExportObject.split("_")
        PreDecimal = FreeCADResultLabelParts[-3]
        PostDecimal = FreeCADResultLabelParts[-2]

        if len(PostDecimal) == 1:
            PostDecimal = PostDecimal + str(0)
        TimeValue = float(PreDecimal) + float(PostDecimal)/100
        TimeString = str(int(round(TimeValue*100,0))).zfill(7)    #For some reason, the VTK exporter expects a list (although only one object is processed at once...) - so build a list with the current object
        ExportObjectList = []
        ExportObjectList.append(FreeCAD.ActiveDocument.getObject(ExportObject))
        FileNameOUT = FileName + "_" + TimeString + ".vtu"
        FilePath = ExportOutputPath + "/" + FileNameOUT
        FreeCAD.Console.PrintMessage(FilePath + " is to be created\n")
        feminout.importVTKResults.export(ExportObjectList,FilePath)    PVUFile.write("\t\t<DataSet timestep=\"" + str(TimeValue) + "\" file=\"" + FileNameOUT + "\"/>\n")#Close the .pvu file
    PVUFile.write("\t</Collection>\n</VTKFile>")
    PVUFile.close()
else:
    FreeCAD.Console.PrintMessage("Nothing to export!")

FreeCAD.Console.PrintMessage('\n<<<Macro finished\n')
}}

## Link

Example [Transient FEM analysis](https://www.freecadweb.org/wiki/Transient_FEM_analysis)

The Forum discussion [Export transient FEM results to vtk/vtu for ParaView](https://forum.freecadweb.org/viewtopic.php?f=22&t=37650)



---
⏵ [documentation index](../README.md) > Macro export transient FEM results/pl
