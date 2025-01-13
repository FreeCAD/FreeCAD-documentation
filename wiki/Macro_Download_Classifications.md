# Macro Download Classifications
{{Macro
|Name=Download Classifications
|Description=Downloads a package of BIM classification systems for use in FreeCAD
|Author=yorik
|Version=1.0
|Date=2024-12-13
|FCVersion=All
}}

## Description

This macro downloads a series of BIM classification systems from <https://github.com/Moult/IfcClassification> and places them in the appropriate folder on your computer so they are found by the [BIM Classification](BIM_Classification.md) tool.

## Usage

Run the macro. After it has run successfully, the new classification systems will be available in the [BIM Classification](BIM_Classification.md) tool. After the macro has run and the classification systems are installed, you can safely delete the macro.

## Install

Through the [Addon manager](Std_AddonMgr.md).

## Code

 **Macro_Download_Classifications.FCMacro**


{{MacroCode|code=
import os
import FreeCAD
import requests
import json

target = os.path.join(FreeCAD.getUserAppDataDir(), "BIM", "Classification")
apireq = "https://api.github.com/repos/Moult/IfcClassification/contents/xml"

r = requests.get(apireq)
if r.ok:
    j = json.loads(r.content)
    print("Installing to", target", ...")
    for f in j:
        df = requests.get(f["download_url"])
        with open(os.path.join(target, f["name"]), 'wb') as tf:
            tf.write(df.content)
            print("Downloaded", f["name"])
else:
    print("error getting repo contents")
}}



---
⏵ [documentation index](../README.md) > Macro Download Classifications
