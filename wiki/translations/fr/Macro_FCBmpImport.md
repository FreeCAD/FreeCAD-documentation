# Macro FCBmpImport/fr
{{Macro/fr
|Name=Macro FCBmpImport
|Icon=FCBmpImportLogo.svg
|Description=Importe des images BMP monochromes et en niveaux de gris dans FreeCAD sous forme d'esquisses, de solides, de fils, de faces ou de lithophane.
|Author=TheMarkster
|Version=0.2021.09.23
|Date=2021-09-23
|FCVersion=0.18 ou après
|Download=[https://wiki.freecadweb.org/File:FCBmpImportScreenshot.png Icône de la barre d'outils]
|SeeAlso=
|Links=[https://github.com/mwganson/fcbmpimport Documentation complète sur Github]
}}

## Description

Cette macro est utilisée pour importer des images BMP dans FreeCAD comme objets FreeCAD. Les options pour les images monochromes à 1 bit par pixel incluent l\'importation en tant qu\'esquisses, solides, fils, faces ou points. Une image BMP en niveaux de gris peut également être importée comme une lithophane.

Utilisation : Cliquez sur le bouton Open Image et sélectionnez votre image dans la boîte de dialogue d\'ouverture de fichier. Les seuls types d\'images supportés sont les BMP. Celles-ci doivent être monochromes, 1 bit par pixel, sauf si elles sont importées en tant que lithophane, auquel cas les BMP en niveaux de gris sont supportés. Vous pouvez utiliser une image BMP en couleur pour la lithophanie, mais elle sera interprétée en interne comme une échelle de gris lors de l\'importation. Après avoir ouvert l\'image, elle apparaîtra dans le volet d\'aperçu. La croix rouge et bleue représente l\'emplacement de l\'origine par rapport à l\'objet importé. Vous pouvez ajouter des valeurs négatives dans les cases X Offset et Y Offset pour déplacer l\'origine avant d\'effectuer l\'importation. Voir la capture d\'écran ci-dessous où la croix a été déplacée. Sous le bouton Open Image se trouvent les boutons à utiliser pour effectuer l\'importation. Certains de ces boutons font apparaître des boîtes de dialogue pour des options supplémentaires. Par exemple, Solid propose l\'option Lithophane. Avec les importations de fils, vous pouvez choisir de créer des faces à partir des fils. Avec les points, vous pouvez choisir de créer une nouvelle esquisse avec les points ajoutés comme liens vers la géométrie externe.

Il faut noter qu\'il existe de meilleures façons d\'importer des images dans FreeCAD. La meilleure façon est de convertir en SVG et d\'importer comme géométrie dans la plupart des cas. Les images à haute résolution doivent être évitées. Elles auront tendance à produire trop d\'objets pour que FreeCAD soit capable de les gérer. Il est même possible de manquer de mémoire et de faire planter FreeCAD ou même l\'ordinateur entier, alors assurez-vous de sauvegarder tout ce sur quoi vous travaillez. Le processus peut être assez lent selon la résolution et la complexité de l\'image. Il existe un bouton d\'abandon que vous pouvez utiliser. Si vous voyez des messages d\'erreur, allez-y et abandonnez l\'importation. Prenons le cas d\'une image de résolution relativement faible de 120 x 120. Cela représente tout de même 14 400 pixels ! L\'algorithme passe d\'une ligne matricielle à l\'autre, ce qui fait qu\'il y aurait 120 lignes. Lorsque les pixels adjacents d\'une ligne sont tous de la même couleur, ils sont combinés en un seul objet et, lors de l\'importation sous la forme d\'un solide fusionné, ils sont encore combinés à mesure que de nouvelles lignes sont ajoutées. La barre de progression est fonctionnelle tant que c\'est la macro qui travaille, mais lorsque la macro se termine et donne à FreeCAD l\'objet, FreeCAD peut parfois prendre beaucoup de temps pour le digérer et le rendre et peut sembler ne pas répondre. Soyez patient.

Les meilleures images sont celles qui présentent des angles nets de 90 degrés, tous horizontaux et verticaux, sans diagonales ni courbes. Ces images peuvent être importées sous forme de croquis et extrudées dans l\'atelier de fabrication de pièces. Les images comportant des courbes et des diagonales auront tendance à être très pixélisées. C\'est la nature même du format BMP. Même les images à haute résolution seront pixellisées si vous faites un zoom suffisant. Certaines des importations seront, franchement, assez laides. C\'est la principale raison pour laquelle les importations SVG sont préférables.

La macro offre également d\'autres outils pour l\'édition des fils. Il s\'agit principalement de traiter les fils importés, qui sont des fils de l\'atelier de dessin. Les points de ces objets peuvent être édités avec la macro. Voir la documentation sur github pour plus de détails.

Le bouton Select Objects permet de sélectionner des sous-objets qui partagent les mêmes limites de boundbox sur l\'un des axes. Par exemple, si vous souhaitez sélectionner toutes les faces ayant la même coordonnée Z sur le plan XY, sélectionnez l\'une des faces, cliquez sur le bouton Sélectionner les objets, sélectionnez Z dans la boîte de dialogue et attendez que toutes les faces de l\'objet correspondant à ce critère soient ajoutées au mécanisme de sélection de FreeCAD. Cela fonctionne également pour les arêtes et les sommets. Cette fonctionnalité a été ajoutée pour faciliter la sélection de toutes les faces d\'une poche 3D dans l\'atelier Path mais elle peut être utile à d\'autres fins.

La documentation complète se trouve sur github : [FCBmpImport](https://github.com/mwganson/fcbmpimport).

<img alt="" src=images/FCBmpImportScreenshot.png  style="width:600px;"> 
*Copie d'écran de FCBmpImport‎*

## Légende


{{Codeextralink|https://gist.githubusercontent.com/mwganson/ea7aa4dcb79d7492caa24e8970967174/raw/1fe247b5b93e5084866a69754854d9caedca1f09/FCBmpImport.FCMacro|FCBmpImport.FCMacro}}

Icône de la barre d\'outils ![](images/FCBmpImportLogo.svg )

## Script

**Macro FCBmpImport.FCMacro**


{{CodeDownload|https://gist.github.com/mwganson/ea7aa4dcb79d7492caa24e8970967174|FCBmpImport.FCMacro}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Macro FCBmpImport/fr
