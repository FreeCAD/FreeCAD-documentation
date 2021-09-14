# Raytracing templates/fr



## Introduction

L\'[atelier raytracing](Raytracing_Workbench/fr.md) est livré avec quelques modèles pour Povray et Luxrender, mais vous pouvez facilement créer les vôtres. Tout ce que vous avez à faire est de créer un fichier de scène pour le rendu donné, puis de le modifier manuellement avec un éditeur de texte pour insérer des balises spéciales que FreeCAD reconnaîtra et où il insérera son contenu (données de caméra et d\'objets).

Modèle personnel {{Version/fr|0.18}} peut être placé dans


```python
~/.FreeCAD/data/Mod/Raytracing/Templates
```

## Povray

Les fichiers de raytracing Povray (avec l\'extension .pov) peuvent être créés manuellement à l\'aide d\'un éditeur de texte (povray est principalement conçu pour être utilisé comme langage de script), mais également avec un large éventail d\'applications 3D, telles que [blender](http://www.blender.org). Sur le [website](http://www.povray.org/povray), vous trouverez des informations complémentaires et une liste d\'applications capables de générer des fichiers .pov.

Lorsque vous avez un fichier .pov prêt, vous devez l\'ouvrir avec un éditeur de texte et effectuer deux opérations:

1.  Supprimez les informations de la caméra, car FreeCAD placera ses propres données de caméra. Pour ce faire, localisez un bloc de texte comme ceci: camera {...}, qui décrit les paramètres de l\'appareil photo, puis supprimez-le (ou mettez \"//\" devant chaque ligne pour les commenter. ).
2.  Insérez la ligne suivante quelque part: // RaytracingContent. C\'est ici que FreeCAD insérera son contenu (données de la caméra et des objets). Vous pouvez, par exemple, mettre cette ligne à la fin du fichier.

Notez que FreeCAD ajoutera également des déclarations que vous pourrez utiliser dans votre modèle, après la //RaytracingContent tag. Ceux-ci sont:

-   cam\_location: la location de la camera
-   cam\_look\_at: la location de la cible de la camera
-   cam\_sky: le vecteur supérieur de la camera.
-   cam\_angle: l\'angle de la camera

Si vous souhaitez, par exemple, placer une lampe au-dessus de l\'appareil photo, vous pouvez utiliser ceci: 
```python
light_source {
 cam_location + cam_angle * 100
 color rgb <10, 10, 10>
}
```

## Luxrender

Les fichiers de raytracing Luxrender (avec extension .lxs) peuvent être soit des fichiers uniques, soit un fichier maître .lxs comprenant des fichiers de définition globale (.lxw), de définition du matériau (.lxm) et de définition géométrique (.lxo). Vous pouvez travailler avec les deux styles, mais il est également facile de transformer un groupe de 4 fichiers en un fichier .lxs unique, en copiant le contenu de chaque fichier .lxw, .lxm et .lxo et en le collant à l\'endroit où ce fichier est enregistré qui sera inséré dans le fichier .lxs principal.

Les fichiers de scène Luxrender sont difficiles à produire manuellement, mais avec de nombreuses applications 3D telles que [blender](http://www.blender.org). Sur le [luxrender website](http://www.luxrender.net), vous trouverez plus d'informations et des plugins pour les principales applications 3D disponibles.

Si vous travaillez avec des fichiers .lxw, .lxm et .lxo séparés, sachez que les fichiers .lx exportés par FreeCAD peuvent se trouver à un emplacement différent de celui du fichier modèle et que ces fichiers risquent de ne pas être trouvés par Luxrender au moment du rendu. Dans ce cas, vous devez copier ces fichiers à l\'emplacement de votre fichier final ou modifier leurs chemins dans le fichier .lxs exporté.

Si vous exportez un fichier de scène à partir de blender et souhaitez tout fusionner en un seul fichier, vous devez effectuer une étape avant l\'exportation: par défaut, l\'exportateur luxrender de Blender exporte toute la géométrie du maillage en tant que fichiers .ply séparés. placer la géométrie du maillage directement dans le fichier .lxo. Pour changer ce comportement, vous devez sélectionner chacune de vos mailles dans Blender, aller à l\'onglet \"Maillage\" et définir l\'option \"Exporter sous\" sur \"Maillage luxrender\" pour chacune d\'entre elles.

Une fois votre fichier de scène prêt, pour le transformer en modèle FreeCAD, vous devez suivre les étapes suivantes:

1.  Localisez la position de la caméra, une ligne qui commence par LookAt, et supprimez-la (ou placez un \"\#\" au début de la ligne pour la commenter)
2.  À cet endroit, insérez la ligne suivante: #RaytracingCamera
3.  À un point souhaité, par exemple juste après la fin de la définition des matériaux, avant les informations de géométrie ou tout à la fin, juste avant la dernière ligne WorldEnd, insérez la ligne suivante: #RaytracingContent. C\'est là que FreeCAD va insérer ses propres objets.

Notez que dans luxrender, les objets stockés dans un fichier de scène peuvent définir des matrices de transformation permettant d\'effectuer des opérations de localisation, de rotation ou de mise à l\'échelle. Ces matrices peuvent s\'empiler et affecter tout ce qui vient après, donc, en plaçant votre balise #RaytracingContent à la fin du fichier, vos objets FreeCAD peuvent être affectés par une matrice de transformation placée plus tôt dans le modèle. . Pour vous assurer que cela ne se produira pas, placez votre balise #RaytracingContent avant tout autre objet de géométrie présent dans le modèle. FreeCAD lui-même ne définira aucune de ces matrices de transformation.


{{Raytracing Tools navi/fr}}


{{Userdocnavi/fr}}

