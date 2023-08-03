---
 TutorialInfo:r
   Topic:  Plans / Dessins
   Level:  Débutant
   Time:  15 minutes
   Author: http://freecadweb.org/wiki/index.php?title=User:Drei Drei
   FCVersion: 0.16 ou au dessus
   Files: 
---

# Drawing tutorial/fr

 **Le développement de [atelier Drawing](Drawing_Workbench/fr.md) s'est arrêté dans FreeCAD 0.16, et le nouvel [atelier TechDraw](TechDraw_Workbench/fr.md) visant à le remplacer a été introduit en v0.17. Les deux ateliers sont toujours fournis dans la version 0.17, mais l'atelier de dessin peut être supprimé dans les versions ultérieures.**



### Introduction

Ce tutoriel est destiné à présenter au lecteur le travail de base de l\'[atelier Drawing](Drawing_Workbench/fr.md), ainsi que la plupart des outils disponibles pour créer des plans.

<img alt="" src=images/Drawing_tutorial_result.png  style="width:480px;">

### Exigences

-   FreeCAD version 0.16 ou supérieure
-   Le lecteur doit avoir les connaissances de base pour utiliser les ateliers Pièces et Conception de Pièces
-   Le lecteur a terminé le [ Tutoriel Planche à Dessin](Draft_tutorial/fr.md)

### Procédure

#### Préparations

Pour réduire le temps nécessaire à ce tutoriel, il est obligatoire de regrouper des éléments similaires dans **Vue Arborescente** pour appliquer des opérations en même temps à plusieurs éléments.

##### Regroupement d\' Éléments 

1.  Dans la **Vue Arborescente**, cliquez avec le bouton droit de la souris sur le nom du document. Dans ce cas **Sans nom** .
2.  Sélectionnez **Créer un groupe**. Vous pouvez modifier le nom du groupe en double-cliquant sur le **Vue Arborescente**.
3.  Sélectionnez les éléments que vous souhaitez ajouter et **le glisser** dans le groupe

Créez les groupes suivants:

-   Draft_objects
-   Draft_dimensions
-   Draft_annotations_text

#### Exemples de Dessin 

Les modèles sont la base de la création des dessins, vous pouvez utiliser les modèles fournis ou créer les vôtres.

1.  Sélectionnez le menu déroulant à côté de ![ 32px](images/_Drawing_Landscape_A3.png ) [Nouveau Dessin A3 Paysage](Drawing_Landscape_A3/fr.md)
2.  Sélectionnez **A4 Paysage**

Nous avons maintenant un dossier intitulé *\'Page\'* dans vue Arborescente **. Cet objet contiendra tout ce qui concerne le**Dessin\'\'\'.

#### Projections

Les projections sont définies comme la représentation visuelle d\'un objet sur un plan spécifique. Elles déterminent les propriétés de l\'objet visible selon cette orientation spécifique.

##### Projections orthographiques 

Celles-ci sont utilisées dans l\'atelier Ingénierie (en cours de développement)pour spécifier les propriétés d\'un objet qui sera usiné. Il existe deux normes communes: les projections **Troisième Angle** et **Premier Angle**.

Pour ce tutoriel, ces projections ne sont pas utilisées car nos objets n\'ont qu\'une représentation significative dans le plan XY

1.  Sélectionnez l\'objet que vous souhaitez projeter dans le dessin.
2.  Sélectionnez ![ 32px](images/_Drawing_Orthoviews.png ) [ Vues Orthogonales](Drawing_Orthoviews/fr.md)
3.  Sélectionnez le type de **projection** que vous souhaitez utiliser
4.  Sélectionnez la vue que vous souhaitez ajouter

Dans les onglets **Général** et **Axonométrique**, vous pouvez spécifier **emplacement**, **échelle** et **séparation** de chaque vue.

##### Autres projections partielles 

Il est possible de créer des vues personnalisées de l\'objet.

1.  Sélectionnez l\'objet que vous souhaitez projeter dans le dessin.
2.  Sélectionnez ![ 32px](images/_Drawing_View.png ) [ Insérer une vue](Drawing_View/fr.md)
3.  Dans l\'onglet **Données**, éditez la **Direction** de **Shape View** en modifiant les valeurs pour les axes **X**, **Y** et **Z** . Par défaut, les valeurs sont **(0, 0, 1)**

Vous pouvez également modifier l\' **Échelle** et la **rotation** de la **Vue** dans l\'onglet **Données**. La même chose peut être faite pour les **Projections Orthographiques**.

##### Projections Planche à Dessin 

La manière préférée d\'ajouter des éléments créés dans l\' **Atelier Planche à Dessin** c\'est avec un outil contenu dans l\' **Atelier Planche à Dessin** conçu spécifiquement pour cela. Avec cette procédure, il est possible d\'importer **Dimensions**, **Annotations**, **Shapestrings** et tout autre élément créé dans l\'Atelier **Planche à Dessin**.

1.  Passez à Atelier **Planche à Dessin**
2.  Sélectionnez le **groupe** ou **éléments** que vous souhaitez projeter. Dans ce cas, **Draft_dimensions**
3.  Sélectionnez ![](images/_Draft_PutOnSheet.png ) [Dessin](Draft_Drawing/fr.md)
4.  Modifier les coordonnées **X** \'et **Y** vers **(140, 100)**
5.  Réglez l\'échelle à 0,5

Répétez pour chaque groupe et définissez les valeurs à celles indiquées ci-dessus.

#### Exportation de votre travail 

FreeCAD prend en charge l\'exportation de fichiers SVG et PDF en fonction de vos **Dessins**

##### SVG

1.  Sélectionnez ![ 32px](images/_Drawing_Save.png ) [ Enregistrer la feuille](Drawing_Save/fr.md)
2.  Spécifiez le chemin d\'accès et le nom du fichier exporté

##### PDF

1.  Dans le menu **Fichier**, sélectionnez **Exporter PDF \...**
2.  Spécifiez le chemin d\'accès et le nom du fichier exporté

Nous avons terminé le travail de base pour l\'[atelier Drawing](Drawing_Workbench/fr.md).



## Lecture recommandée 

-   Pour savoir comment créer des modèles personnalisés, voir [Modèle de dessin ](Drawing_Template_HowTo/fr.md)
-   Pour plus d\'informations sur les outils disponibles, consultez la page [Atelier Drawing](Drawing_Workbench/fr.md).


{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing tutorial/fr
