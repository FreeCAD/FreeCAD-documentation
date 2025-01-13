# Macro Parametric Curve FP/fr
{{Macro/fr
|Name=Macro Parametric_Curve_FP
|Icon=Parametric_Curve_FP.svg
|Description=Amélioration de la Macro 3D Parametric Curve mais avec de nouvelles fonctionnalités. Créer un objet Feature Python, l'intégration de feuilles de calcul et de JSON, des paramètres étendus. <br/>Prend en charge les mêmes paramètres a, b, c, mais peut également avoir autant de paramètres d sous la forme de d1, d2, d3, d4, etc. que vous le souhaitez.<br/>Prend également en charge l'enregistrement des formules dans un fichier texte au format JSON et la prise en charge de l'intégration dans une feuille de calcul de la formule en cours.<br/>La documentation complète peut être trouvée [https://github.com/mwganson/Parametric_Curve_FP Documentation complète sur Github Parametric_Curve_FP].  
|Author=TheMarkster
|Version=2023.05.06
|Date=2023-05-06
|FCVersion=Toutes en Python 3
|Download=[https://wiki.freecadweb.org/images/5/59/Parametric_Curve_FP.svg Icône de la barre d'outils]
|SeeAlso=[Macro 3D Parametric Curve](Macro_3D_Parametric_Curve/fr.md)
|Links=[https://github.com/mwganson/Parametric_Curve_FP Documentation complète sur Github]
}}

## Description

Cette macro est une mise à jour de la [macro 3D Parametric Curve](Macro_3D_Parametric_Curve/fr.md) de Gomez Lucio, puis modifiée par Laurent Despeyroux le 9 février 2015. La macro a été mise à jour en un objet paramétrique Feature Python. Elle supporte les mêmes paramètres a, b, c, mais peut aussi avoir autant de paramètres d sous forme de d1, d2, d3, d4, etc. que vous le souhaitez. Si vous souhaitez référencer un [jeu de variables](Std_VarSet/fr.md) ou un [objet DynamicData dd](DynamicData_Workbench/fr.md) dans une formule, vous pouvez utiliser la commande {{Incode|fc(expr)}} pour le faire. Par exemple, s\'il existe une valeur flottante dans un objet dd nommé my_float et que vous souhaitez la référencer dans la formule pour le paramètre b, entrez pour b : {{Incode|fc(dd.my_float)}} ou si vous souhaitez l\'utiliser de manière plus complexe : b : {{Incode|fc(dd.my_float) * a + pi}} comme autre exemple.

Il prend également en charge l\'enregistrement des formules dans un fichier texte au format JSON et l\'intégration de la formule en cours dans une feuille de calcul. La documentation complète est disponible sur github [Parametric_Curve_FP](https://github.com/mwganson/Parametric_Curve_FP).

<img alt="" src=images/Parametric_Curve_FP_SCR.png  style="width:600px;"> 
*Capture d'écran de Parametric_Curve_FP*



### Légende


{{Codeextralink|https://gist.github.com/mwganson/473920ad317fb2dc3e37638112874e2a/raw/afbd008f86b7084a879665f6570629b7d321f286/Parametric_Curve_FP.FCMacro|Parametric_Curve_FP.FCMacro}}

Icône de la barre d\'outils ![](images/Parametric_Curve_FP.svg )

### Script

**Macro Parametric_Curve_FP.FCMacro**


{{CodeDownload|https://gist.github.com/mwganson/473920ad317fb2dc3e37638112874e2a|Parametric_Curve_FP.FCMacro}}



---
⏵ [documentation index](../README.md) > Macro Parametric Curve FP/fr
