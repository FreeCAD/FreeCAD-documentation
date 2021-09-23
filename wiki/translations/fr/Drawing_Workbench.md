# Drawing Workbench/fr
**Le développement de l'[atelier Mise en plan](Drawing_Workbench/fr.md) s'est arrêté, et un nouvel atelier [Techdraw](TechDraw_Workbench/fr.md) visant à le remplacer sera introduit dans la version 0.17. Les deux ateliers seront fournis dans la version v0.17, mais l'atelier Mise en plan peut être supprimé dans les versions ultérieures.**

<img alt="Icône de l\'atelier Drawing" src=images/Workbench_Drawing.svg  style="width:128px;">

## Introduction

L\'atelier Mise en plan vous permet de mettre votre travail 3D sur papier. C\'est-à-dire, mettre des vues de vos modèles dans une fenêtre 2D et insérer cette fenêtre dans un dessin, par exemple une feuille avec une bordure, un titre et votre logo et enfin imprimer cette feuille.


{{TOCright}}

<img alt="" src=images/Drawing_extraction.png  style="width:600px;">

## Outils

Ces outils permettent de créer, configurer et exporter des mises en plan 2D

-   <img alt="" src=images/Drawing_New.png  style="width:32px;"> [Ouvrir un fichier vectoriel SVG](Drawing_Open_SVG/fr.md): Ouvre une feuille de dessin précédemment sauvegardée au format de fichier SVG

-   <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [Nouvelle feuille A3 paysage](Drawing_Landscape_A3/fr.md): Créé une nouvelle feuille à partir du gabarit A3 par défaut de FreeCAD

-   <img alt="" src=images/Drawing_View.png  style="width:32px;"> [Insérer une vue](Drawing_View/fr.md): Insère une vue de l\'objet sélectionné dans la feuille active

-   <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> [Annotation](Drawing_Annotation/fr.md): Ajoute une annotation dans la feuille de dessin courante.

-   <img alt="" src=images/Drawing_Clip.png  style="width:32px;"> [Clip](Drawing_Clip/fr.md): Ajoute un groupe de clip dans la feuille de dessin courante

-   <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> [Ouverture du navigateur internet](Drawing_Openbrowser/fr.md): Ouvre un aperçu de la feuille courante dans le navigateur.

-   <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Vue Orthogonale](Drawing_Orthoviews/fr.md): Crée automatiquement des vues orthogonales d\'un objet sur la feuille de dessin courante.

-   <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> [Symbol](Drawing_Symbol/fr.md): Ajoute le contenu d\'un fichier SVG en tant que symbole dans la feuille de dessin en cours.

-   <img alt="" src=images/Drawing_DraftView.png  style="width:32px;"> [Draft View](Draft_Drawing/fr.md): Insère une vue Brouillon spécial de l\'objet sélectionné dans la feuille de dessin en cours.

-   <img alt="" src=images/Drawing_SpreadsheetView.png  style="width:32px;"> [Spreadsheet View](Drawing_SpreadsheetView/fr.md): Insère une vue d\'une feuille de calcul sélectionnée dans la feuille de dessin en cours.

-   <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Exporter la feuille](Drawing_Save/fr.md): Exporte la feuille dans un fichier au format SVG

-   [Project Shape](Drawing_ProjectShape/fr.md): Crée une projection de l\'objet sélectionné (Source) dans la vue 3D.

-    **Note:**L\'atelier [Draft](Draft_Workbench/fr.md) a son propre [atelier de dessin](Draft_Drawing/fr.md) qui place les objets du projet sur papier. Il a quelques fonctionnalités supplémentaires sur les outils de dessin standards et prend en charge les objets spécifiques tels que [les dimensions](Draft_Dimension/fr.md).

## Flux de travail 

Le document contient un objet de forme 3D à partir duquel nous voulons produire un dessin. Une \"Page\" est donc créée. Une page est instanciée à partir d\'un modèle, par exemple, le modèle \"A3\_Landscape\". Le modèle est un document [SVG](SVG/fr.md) qui peut contenir un cadre de page, un logo et d\'autres éléments.

Dans cette page peuvent être insérées une ou plusieurs vues. Chaque vue a une position sur la page (Propriétés X,Y), une échelle (Propriété d\'échelle) et des propriétés additionnelles. Chaque fois que la page, la vue ou l\'objet référencé subit une modification, la page est régénérée et l\'affichage mis à jour.

## Script

Pour l\'instant la méthodologie de travail par l\'interface graphique est sévèrement limitée, l\'API de script est plus intéressante.

Voir la page [Drawing API exemples](Drawing_API_example/fr.md) pour une description des fonctions utilisées pour la création des pages et vues du dessin.

Ici un script qui permet de remplir facilement le [cartouche](Macro_CartoucheFC/fr.md) de la feuille originelle A3\_Landscape de FreeCAD.

## Modèles

FreeCAD est livré avec un jeu de modèles par défaut, vous pouvez en trouver d\'autres sur la page des [Modèles de feuille](Drawing_templates/fr.md).

## Extension Module de dessin 

Quelques notes sur le module de dessin sont ajoutés à la page [Documentation sur le module dessin](Drawing_Documentation/fr.md) [(en)](Drawing_Documentation.md). Il aide à comprendre rapidement le fonctionne du module de dessin, ce qui permet aux programmeurs de commencer rapidement sa programmation.

## Tutoriels

-   [Drawing tutoriel](Drawing_tutorial/fr.md)

## Liens externes 

-   [Introduction au dessin mécanique sur Youtube - par Normal Universe](https://www.youtube.com/watch?v=1Hm5Zyjmjac)





{{Drawing Tools navi

}} 

[Category:Obsolete Workbenches](Category:Obsolete_Workbenches.md)

---
[documentation index](../README.md) > Drawing Workbench/fr
