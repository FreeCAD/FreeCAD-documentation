# Release notes 0.15/fr
 FreeCAD 0.15 a été publié le 8 avril 2015. Ceci est un résumé des changements les plus intéressants survenus dans FreeCAD depuis la dernière version. Voir [sur Mantis (en anglais)](http://www.freecadweb.org/tracker/changelog_page.php) pour la liste complète des changements. Les versions plus anciennes : [0.14](Release_notes_0.14/fr.md) - [0.13](Release_notes_0.13/fr.md) - [0.12](Release_notes_0.12/fr.md) - [0.11](Release_notes_0.11/fr.md)

<img alt="" src=images/Spark-Plug-Plane.jpg  style="width:1024px;">


<center>

Spark Plug Plane par r-frank


</center>

## Généralité

### Boîte de recherche dans la Vue Sélection 

La fenêtre de sélection permet aux utilisateurs de faire une recherche dans les objets sélectionné. Maintenant vous avez la possibilité de sélectionner ou désélectionner une seule entité, de zoomer sur une entité et d\'aller sur cette entité dans l\'arborescence.

![](images/FeatureSelectionView.jpg )

### Le support des unités est déployé 

Le nouveau système [d\'unités](Quantity/fr.md) de FreeCAD, introduit dans la version 0.14, est maintenant utilisé dans pratiquement tous les modules de freeCAD, dont [Sketcher](Sketcher_Workbench/fr.md), [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md). Quelques zones ne l\'utilisent toujours pas mais en général vous pouvez maintenant compter sur le système d\'unité tout le long de votre processus de modélisation.

### Améliorations mineures 

-   L\'Import/Export a maintenant sa propre section dans les préférences. Tous les formats de fichiers sont regroupé dans leur propre onglets, ce qui rend plus facile la recherhce des bonnes options aux nouveaux utilisateurs.
-   Les raccourcis clavier personnalisés acceptent maintenant jusqu\'à 4 touches.
-   FreeCAD supporte maintenant [l\'Occulus Rift](http://forum.freecadweb.org/viewtopic.php?f=9&t=7715).
-   Support des barre d\'outils globales personnalisées : En plus d\'ajouter une barre d\'outils avec vos propre outils de n\'importe quels ateliers, il est maintenant possible d\'ajouter une barre d\'outils personnalisé qui restera présente dans tout les ateliers.
-   Nouveau paquets de librairies pour Windows avec la dernière version OCE 0.17.

## Atelier Part 

-   Quelques nouveaux éléments géométrique de base ont été ajouté : Parabole, Arc de Parabole, Hyperbole et Arc d\'hyperbole.

## Ateliers Part Design & Sketcher 

### Ellipses

L\'[Atelier Sketcher](Sketcher_Workbench/fr.md) bénéficie du support des ellipses. Elles peuvent être construites de différentes manière et peuvent être utilisé pour différentes opérations.

![](images/Ellipse-example.png )

### Amélioration de l'outil de sélection 

Le Sketcher bénéficie aussi d\'une série de nouveaux outils pour vous aidez dans le diagnostique, l\'optimisation et la réparation de vos esquisses. Vous pouvez maintenant, par exemple, facilement sélectionner les éléments associé à une contrainte, ou inversement, ou trouver les contraintes conflictuelles ou redondantes.

L\'interface graphique bénéficie aussi de nouveaux panneaux, et montre maintenant la liste des éléments sélectionnables de votre esquisse.

### Fusionner les esquisses 

Il est maintenant possible de fusionner plusieurs esquisses en une.

### Améliorations des propriétés de l\'esquisse 

L\'affichage des propriétés des objets Esquisses a été améliorés et les contraintes dimensionnelles (distances, distances horizontales et verticales) à l'intérieur de l\'esquisse sont éditable directement dans ses propriétés sans avoir à retourner dans le mode édition de l\'esquisse.

### Améliorations mineures 

-   Ajout de plus de polygones régulier dans le sketcher
-   Ajout de novelle contraintes : Contrainte de symétrie perpendiculaire à un axe de symétrie

## Atelier Tableur 

L\'[atelier Tableur](Spreadsheet_Workbench/fr.md) a été entièrement recodé. FreeCAD possède maintenant un éditeur de feuille de calcul de pointe, robuste, riche en caractéristique. Quelques fonctionnalités que l\'on trouvé dans l\'ancienne version de cet atelier ont été supprimés, comme le controlleur de propriété, mais c\'est un problème complexe qui demande plus de temps pour être implémenter proprement. A présent, le nouvel atelier Tableur offre des fonctionnalité bien plus robuste pour extraire des données depuis le modèle.

<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width:640px;">

## Atelier Draft 

### Compatibilité des polices filaire dans Texte Surfacique 

Pour les nostalgique des vieux logiciel CAD, les police filaire (dans lesquels chaque lettre sont faite de simple lignes sans surface) peuvent maintenant être utilisé avec l\'outil [Texte surfacique](Draft_ShapeString/fr.md).

![](images/Stickyfonts.jpg )

### Améliorations mineures 

-   [Lignes](Draft_Line/fr.md) peuvent maintenant être défini par leur longueur et l\'angle selon le plan de travil en cours.
-   Extension de ligne relative pour les [dimensions](Draft_Snap_Dimensions/fr.md).
-   Support des [Ellipses](Sketcher_CreateEllipseByCenter/fr.md).
-   Les objets [Réseaux](Draft_Array/fr.md) peuvent maintenant être fusionnés.

## Atelier Mise en plan 

### Export de la page en DXF 

Le système utilisé pour exporter les pages de dessin au format DXF jusqu\'à présent utilisait un hack très compliqué pour convertir le code SVG en objet FreeCAD puis retour à DXF avec les projets exportateurs. Maintenant, l\'exportation est fait en interne dans le module Dessin, qui donne beaucoup plus rapidement des résultats fiables. Exportation DXF utilise maintenant un système de modèle et similaire aux feuilles SVG. Si votre page de dessin utilise un certain modèle SVG, et un modèle DXF avec le même nom est trouvé au même endroit, il est utilisé pour générer le fichier DXF.

![](images/Drawing-dxf-export.jpg )

Dans le fichier DXF, les différents vues sont placées sous forme de blocs à l\'échelle. Cela permet de restaurer rapidement l\'échelle 1:1

### Améliorations mineures 

-   Il est maintenant possible de réutiliser les paramètres de projection d\'une vue existante lors de la création de nouveaux projets de vues.

## Atelier Architecture 

### Mise à jour de l\'import/export IFC 

FreeCAD deL\' [ importateur IFC](Arch_IFC.md) de FreeCad a reçu beaucoup de travail et d\'essais, et une mise à niveau massive. L\'ancien,importateur basé sur Python, a été désactivé (il est encore utilisable à partir de la console de python, ), et FreeCAD utilise désormais exclusivement et de manière intensive le plus récent,d\'avant garde[Version 5](http://ifcopenshell.org/python.html) ([lire la suite](http://ifcopenshell.org/pythonOCC/example1/) à ce sujet) de [IfcOpenShell](http://ifcopenshell.org/) qui est maintenant disponible sur toutes les plateformes principales (assurez-vous de télécharger la version correspond à la version python utilisé par votre installation de FreeCAD). Nous bénéficions désormais d\'une importation et exportation beaucoup plus rapide et fiable, un code beaucoup plus simple et plus propre (lire: plus facile à étendre), et déjà quelques goodies supplémentaires, comme un meilleur support pour les objets basés sur les courbes et les propriétés IFC.

### Nouvelle fonctionnalité: Couper un objet avec un plan 

Cette nouvelle fonctionnalité, [ Arc Plan de Coupe](Arch_CutPlane.md), permet de couper un objet selon un plan définit par la face d\'un autre objet. Il est possible de couper l\'objet en arrière ou en avant du plan choisit.

![](images/Arch_CutPlane_example.jpg )

### Nouvel outil de toit 

L\'outil [Toit](Arch_Roof.md) a été complètement refait et il est désormais possible de définir des pentes différentes pour chaque côtés du toit, en outre, il est possible de définir une épaisseur de toit, la longueur du débordement.

![](images/RoofExample.png )

### Panneaux

Un nouvel objet [Panneau](Arch_Panel.md) a été ajouté à l\' [Atelier Arch(itecture)](Arch_Workbench.md). Il permet de créer toutes sortes d\'objets en forme de plaques, et sera particulièrement utile pour les constructions de panneaux comme les projets [wikihouse](http://www.wikihouse.cc/) ou [maison contextuelle](http://www.popup-house.com/)

<img alt="" src=images/Arch_Panel_example.jpg  style="width:640px;">

### Fourniture

Le nouvel objet \[Arch Equipment\]\[Équipement Arch(itecture) \]est conçu pour ajouter toutes sortes d\'objets autonomes non-structurels pour vos projets architecturaux, tels que les appareils d\'éclairage, des équipements sanitaires ou des meubles.

### Améliorations mineures 

-   L\' objet Basepoint de [Structure Arch(itecture)peut](Arch_Frame.md) maintenant être réglé sur un sommet spécifique du profil.

## Modules externes 

Il a également été fait un travail très intéressant sur de nouveaux ateliers et macros, qui ne sont pas intégrés dans le code source FreeCAD (encore!), Mais sont faciles à installer sur une installation existante FreeCAD 0,15. Les instructions sont fournies sur les pages liées ci-dessous:

### Assemblage 2 

L\' [Atelier Assemblage 2](https://github.com/hamish2014/FreeCAD_assembly2) fournit des outils pour créer des assemblages multi-pièces, et est une très bonne alternative pour l\'atelier officielle d\'Assemblage encore en cours de développement (voir \[http: // forum .freecadweb.org/viewtopic.php?f=10&t=8577 forum thread\])

![](images/Assembly2_example.jpg )

### Dessin dimensionnement 

L\'[atelier Dessin dimensionnement](https://github.com/hamish2014/FreeCAD_drawing_dimensioning) ajoute de puissants outils d\'annotation et de dimensionnement à l\'atelier de dessin (voir [fil de discussion](http://forum.freecadweb.org/viewtopic.php?f=10&t=8395)).

![](images/Drawing_Dimensioning_example.jpg )

### Caractéristiques de travail 

Les [fonctions de construction macro](https://github.com/Rentlau/WorkFeature) ajoute une large gamme d\'objets utilitaires comme des plans ou des axes d\'alignement, et des outils pour vous aider à positionner et aligner les objets le long de ces objets d\'aide (voir \[http: / forum /forum.freecadweb.org/viewtopic.php?f=22&t=9056 fil de discussion\]).

<img alt="" src=images/WF.png  style="width:640px;">

[Category:News](Category:News.md) [Category:Documentation](Category:Documentation.md) [Category:Releases](Category:Releases.md)
