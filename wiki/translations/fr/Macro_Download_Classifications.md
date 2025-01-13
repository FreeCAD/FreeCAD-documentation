# Macro Download Classifications/fr
{{Macro/fr
|Name=Download Classifications
|Description=Télécharge un ensemble de systèmes de classification BIM à utiliser dans FreeCAD
|Author=yorik
|Version=1.0
|Date=2024-12-13
|FCVersion=Toutes
}}

## Description

Cette macro télécharge une série de systèmes de classification BIM à partir de <https://github.com/Moult/IfcClassification> et les place dans le dossier approprié de votre ordinateur afin qu\'ils soient trouvés par l\'outil [BIM Classification](BIM_Classification/fr.md).



## Utilisation

Lancez la macro. Une fois qu\'elle a été exécutée avec succès, les nouveaux systèmes de classification seront disponibles dans l\'outil [BIM Classification](BIM_Classification/fr.md). Une fois la macro exécutée et les systèmes de classification installés, vous pouvez supprimer la macro en toute sécurité.



## Installation

Par le biais du [gestionnaire des extensions](Std_AddonMgr/fr.md).

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
⏵ [documentation index](../README.md) > Macro Download Classifications/fr
