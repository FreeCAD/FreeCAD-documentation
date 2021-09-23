# MIBA/fr
## Introduction

Miba est un moyen d\'intégrer des informations sur l\'espace 3D dans une image 2D. Ainsi, il est souvent possible d\'utiliser l\'image 2D au lieu d\'un visualiseur 3D. Grâce aux informations Miba, vous êtes en mesure de calculer la position d\'un emplacement 3D dans l\'image 2D. Cela vous permet de décorer l\'image ultérieurement avec des informations 3D arbitraires. Vous pouvez prendre l\'image dans un premier état (conception) et l\'utiliser plus tard (p. ex. production). Vous n\'avez pas besoin de connaître le type de données 3D ou les positions lorsque vous prenez la photo. L\'image est donc complètement séparée des données 3D.

Un cahier des charges détaillé, vous pouvez trouver ici: [MIBA](http://miba.juergen-riegel.net/)

## Miba dans FreeCAD 

Si vous choisissez un format de fichier qui possède une capacité de commentaire (JPG et PNG), vous pouvez choisir d\'écrire un commentaire ou d\'insérer les informations MIBA dans les champs de commentaire (par défaut) :

<img alt="" src=images/Save_picture.png  style="width:600px;">

## Faire des photos Miba avec un script 


```python
import Part,PartGui

# loading test part
Part.open("C:/Documents and Settings/jriegel/My Documents/Projects/FreeCAD/data/Blade.stp")

OutDir = "c:/temp/"
Gui.ActiveDocument.ActiveView.setAnimationEnabled(False)

# creating images with different Views, Cameras and sizes
for p in ["PerspectiveCamera", "OrthographicCamera"]:
    Gui.SendMsgToActiveView(p)
    for f in ["ViewAxo", "ViewFront", "ViewTop"]:
        Gui.SendMsgToActiveView(f)
        for x, y in [[500, 500], [1000, 3000], [3000, 1000], [3000, 3000], [8000, 8000]]:
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + "Blade_" + p + "_" + f + "_" + str(x) + "_" + str(y) + ".jpg", x, y, "White")
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + "Blade_" + p + "_" + f + "_" + str(x) + "_" + str(y) + ".png", x, y, "Transparent")

# close active document
App.closeDocument(App.ActiveDocument.Name)
```

[Category:User\_Documentation](Category:User_Documentation.md)

---
[documentation index](../README.md) > [User_Documentation](Category:User_Documentation.md) > MIBA/fr
