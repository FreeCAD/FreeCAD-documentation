---
 GuiCommand:
   Name: BIM Project
   Name/fr: BIM Projet
   MenuLocation: 3D/BIM , Projet
   Workbenches: BIM_Workbench/fr
   Shortcut: 
   SeeAlso: 
---

# BIM Project/fr

## Description

L\'outil **BIM Projet** crée un projet d\'[IFC natif](NativeIFC/fr.md) dans le document en cours. En IFC, un projet (IfcProject) est l\'objet racine de tous les contenus du modèle. Il est obligatoire d\'en avoir un dans chaque fichier IFC.

Il n\'est pas nécessaire de créer un projet pour exporter un modèle FreeCAD en IFC, car un projet par défaut sera ajouté chaque fois que vous exporterez un fichier IFC. Cependant, lorsque vous travaillez avec [NativeIFC](NativeIFC/fr.md), un fichier IFC est attaché au modèle, et toute la géométrie et les propriétés de ce modèle et de ses composants proviennent du fichier IFC attaché. Le projet est l\'endroit où le fichier IFC est attaché au document.

Généralement, vous créez un projet BIM pour y joindre un fichier IFC. Lors de la création du projet, le fichier IFC joint est vide et n\'est pas enregistré. La prochaine fois que vous enregistrerez le fichier FreeCAD, il vous sera également demandé d\'enregistrer le fichier IFC.

Si vous distribuez le fichier FreeCAD, tous les fichiers IFC attachés doivent être distribués ensemble, sinon FreeCAD ne pourra pas extraire la géométrie. Cependant, si la propriété **shape mode** de tous les objets contenus dans un projet est réglée sur **Shape**, alors le fichier FreeCAD peut être distribué sans le fichier IFC qui l\'accompagne et s\'ouvrira toujours correctement sur d\'autres ordinateurs. Les objets IFC, cependant, ne seront plus éditables.

Lors de l\'insertion d\'un fichier IFC, un objet projet est créé, qui contient tout le contenu du fichier. Comme tous les objets NativeIFC, le projet peut être développé en double-cliquant dessus dans l\'arborescence.



## Utilisation

1.  Assurez-vous d\'avoir un document FreeCAD ouvert.
2.  Appuyez sur le bouton **<img src="images/BIM_Project.svg" width=16px> [Projet](BIM_Project/fr.md)**.
3.  Vous pouvez verrouiller le document en appuyant sur le bouton **<img src="images/IFC.svg" width=16px> [Verrouiller en IFC](NativeIFC/fr#Modes_verrouillé_et_déverrouillé.md)**.



## Modes verrouillé et déverrouillé 

Dans l\'[atelier BIM](BIM_Workbench/fr.md), la barre d\'état comporte un bouton **<img src="images/IFC.svg" width=16px> [Verrouiller en IFC](Mode_verrouillé.md)** qui permet de basculer entre les modes **verrouillé** et **déverrouillé**. En mode déverrouillé, vous pouvez avoir plusieurs [projets](BIM_Project/fr.md) dans votre document FreeCAD, ainsi que des éléments IFC et non-IFC.

En mode verrouillé, les données attachées à votre objet de projet sont directement attachées au document FreeCAD. Le document FreeCAD agit comme une réplique fidèle, ou un rendu, du document IFC. L\'élément de projet est donc supprimé. Vous ne pouvez avoir qu\'un seul projet dans votre document FreeCAD, et vous ne pouvez plus avoir d\'objets non-IFC (tout nouvel objet est instantanément converti en IFC).



## Ajouter des objets à un projet 

Les objets sont ajoutés à un projet simplement en les faisant glisser et en les déposant sur le projet dans l\'arborescence. Ces objets seront convertis en IFC et pourraient perdre certains de leurs anciens comportements paramétriques lorsque ceux-ci ne sont pas pris en charge par l\'IFC.



## Différence

Lorsque le projet contient des modifications non enregistrées, un point rouge apparaît sur l\'icône de l\'arbre. En cliquant avec le bouton droit de la souris sur le projet et en choisissant **IFC → Différence**, une fenêtre de dialogue s\'ouvrira pour afficher une [différence](https://fr.wikipedia.org/wiki/Diff) de ce qui a été modifié dans le fichier IFC joint. C\'est un bon moyen de s\'assurer que ce que vous avez modifié correspond bien à ce que vous vouliez.



## Enregistrer

Les fichiers IFC attachés à un projet sont automatiquement enregistrés chaque fois que vous enregistrez le fichier FreeCAD. Ils peuvent également être sauvegardés manuellement à tout moment en cliquant avec le bouton droit de la souris sur le projet et en choisissant **IFC → Enregistrer**.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Project/fr
