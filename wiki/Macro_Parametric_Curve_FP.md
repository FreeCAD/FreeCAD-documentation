# Macro Parametric Curve FP
{{Macro
|Name=Macro Parametric_Curve_FP
|Icon=Parametric_Curve_FP.svg
|Description=Update of Macro 3D Parametric Curve, but with new features. Creates a Feature Python object, offers spreadsheet and JSON integration, expanded parameters.<br/>It has support for the same a, b, c parameters, but also can have as many d parameters in the form of d1, d2, d3, d4, etc. as you like.<br/>It also supports saving formulas to a text file in JSON format and support for Spreadsheet integration of the current formula.<br/>Full documentation can be found [https://github.com/mwganson/Parametric_Curve_FP Full Documentation on Github Parametric_Curve_FP] on github. 
|Author=TheMarkster
|Version=2023.05.06
|Date=2023-05-06
|FCVersion=All Python 3
|Download=[https://wiki.freecadweb.org/images/5/59/Parametric_Curve_FP.svg ToolBar Icon]
|SeeAlso=[Macro 3D Parametric Curve](Macro_3D_Parametric_Curve.md) <img src="images/Macro_3D_Parametric_Curve.png" width=24px>
|Links=[https://github.com/mwganson/Parametric_Curve_FP Full Documentation on Github]
}}

## Description

This macro is an update to the [Macro 3D Parametric Curve](Macro_3D_Parametric_Curve.md) by Gomez Lucio and later Modified by Laurent Despeyroux on 9th feb 2015. The macro has been updated to a parametric Feature Python object. It has support for the same a, b, c parameters, but also can have as many d parameters in the form of d1, d2, d3, d4, etc. as you like. If you want to reference a [VarSet](Std_VarSet.md) or [DynamicData dd object](DynamicData_Workbench.md) in a formula you can use the {{Incode|fc(expr)}} command to do this. For example, if there is a float value in a dd object named my_float and you wish to reference it in the formula for the b parameter, enter for b: {{Incode|fc(dd.my_float)}} or if you want to use it in a more complex way: b: {{Incode|fc(dd.my_float) * a + pi}} as another example.

It also supports saving formulas to a text file in JSON format and support for Spreadsheet integration of the current formula. Full documentation can be found [Parametric_Curve_FP](https://github.com/mwganson/Parametric_Curve_FP) on github.

 <img alt="" src=images/Parametric_Curve_FP_SCR.png  style="width:600px;">  
*Parametric_Curve_FP screenshot‎*

### Legend


{{Codeextralink|https://gist.github.com/mwganson/473920ad317fb2dc3e37638112874e2a/raw/afbd008f86b7084a879665f6570629b7d321f286/Parametric_Curve_FP.FCMacro|Parametric_Curve_FP.FCMacro}}

ToolBar Icon  ![](images/Parametric_Curve_FP.svg )

### Script

**Macro Parametric_Curve_FP.FCMacro**


{{CodeDownload|https://gist.github.com/mwganson/473920ad317fb2dc3e37638112874e2a|Parametric_Curve_FP.FCMacro}}



---
⏵ [documentation index](../README.md) > Macro Parametric Curve FP
