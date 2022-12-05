---
- GuiCommand:Addon/fr
   Name:BIM IfcProperties
   Name/fr:BIM Propriétés IFC
   Workbenches:<img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench/fr.md)
   Addon:BIM
   MenuLocation:Manage → IFC Properties
   SeeAlso:[BIM Elements IFC](BIM_IfcElements/fr.md),[BIM Quantité IFC](BIM_IfcQuantities/fr.md)
---

# BIM IfcProperties/fr

## Description

<img alt="" src=images/BIM_ifcproperties_screenshot.png  style="width:1024px;">

Le gestionnaire de propriétés IFC vous permet de modifier les propriétés IFC d\'un objet sélectionné, de nombreux objets sélectionnés ou de tous les objets du document. Les propriétés IFC sont des informations attachées à des objets individuels. Ils ne peuvent être rattachés qu\'à [Objets BIM](BIM_Workbench/fr.md) donc tout objet non-BIM doit d\'abord être converti en objet BIM en utilisant le menu **3D/BIM -\> Create component** avant de pouvoir recevoir des Propriétés IFC.

Les propriétés IFC peuvent être personnalisées, c\'est-à-dire que vous pouvez définir votre propre nom et valeur pour elles, ou suivre un schéma prédéfini défini par la norme IFC. Ces propriétés sont définies dans **Property sets** et sont généralement disponibles pour les types IFC les plus courants. Par exemple, le jeu de propriétés **Pset_BeamCommon** est conçu pour être attaché aux poutres. Les jeux de propriétés prédéfinis contiennent généralement des propriétés habituelles définies par le schéma IFC pour un type particulier. Par exemple, Pset_WallCommon, qui doit être attaché aux murs, contient des propriétés qui définissent si le mur est porteur ou est extérieur ou intérieur.

Vous pouvez créer vos propres propriétés et jeux de propriétés et les attribuer à n\'importe quel objet. Il n\'y a aucune exigence dans le schéma IFC pour ajouter des Psets prédéfinis pour les types courants ou toute restriction pour ajouter des propriétés personnalisées. Il s\'agit d\'une décision laissée aux utilisateurs. Habituellement, lorsque vous travaillez en équipe, ces choses sont décidées en même temps que d\'autres exigences BIM pour vous assurer que tous les modèles BIM produits répondent aux mêmes exigences.

### Définir vos propres jeux de propriétés 

Les ensembles de propriétés disponibles prédéfinis dans la norme IFC sont stockés dans un fichier csv [fichier csv fourni avec FreeCAD](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Arch/Presets/pset_definitions.csv). Vous pouvez également ajouter un fichier csv personnalisé avec vos propres jeux de propriétés. Ce fichier doit être nommé CustomPsets.csv et être placé dans \$USERAPPDATA/BIM.

Le dossier \$USERAPPDATA dépend de votre plate-forme/système d\'exploitation (généralement \$HOME/.FreeCAD sur linux/mac, /users/YOUR USER/Application Data/roaming/FreeCAD sur Windows) et peut également être trouvé en tapant dans une console Python sous FreeCAD:

FreeCAD.getUserAppDataDir()

Dans le fichier CSV, chaque ligne représente un ensemble de propriétés différent, commençant par le nom de l\'ensemble et un nombre quelconque de paires Name;Type, définissant un nom de propriété et son [type](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Arch/Presets/ifc_types_IFC4.json). Par exemple:

Pset_FreeCAD;Name;IfcLabel;Version;IfcReal

définirait un ensemble de propriétés nommé \"FreeCAD\" (le préfixe Pset\_ n\'est pas obligatoire mais est une pratique courante) qui contient deux propriétés: une appelée \"Name\" qui est un IfcLabel (un morceau de texte) et une autre appelée \"Version\" qui est un IfcReal (une valeur numérique avec des décimales).



---
![](images/Right_arrow.png) [documentation index](../README.md) > BIM IfcProperties/fr
