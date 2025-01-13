# Macro CenterOfMass/fr
{{Macro/fr
|Name=Macro CenterOfMass
|Description=Calculer et montrer le centre de masse de plusieurs solides. 
|Author=Schupins, SyProLei
|Version=0.8.0
|Date=2024-12-17
|FCVersion=0.19 et supérieure
}}

## Description

Donne la masse totale et l\'emplacement du centre de masse des objets sélectionnés. Différentes densités peuvent être choisies pour chaque objet.


{{Codeextralink|https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/CenterOfMass.FCMacro}}

<img alt="" src=images/CenterOfMass_exemple.png  style="width:600px;">



## Utilisation

1.  Sélectionner un ou plusieurs solides.
2.  Lancez la macro.
3.  Vous aurez une fenêtre listant les solides. Vous pouvez spécifier la densité de votre matériau dans différents systèmes d\'unités ou choisir parmi les matériaux prédéfinis.



### Options disponibles 

-   Colorier les solides en fonction de leur densité.
-   Afficher l\'emplacement du centre de masse.
-   Exporter et importer des *masses*, des *matériaux* et des *densités* (même s\'il ne s\'agit pas d\'un fichier **.csv** de la macro, mais les colonnes doivent être nommées en conformité).
-   Sauvegarder les densités dans le document (les supprimer à nouveau lorsque l\'on règle le matériau à{{ComboBox|default}}).
-   Vous pouvez modifier certaines préférences dans **Outils → Modifier les paramètres → Préférences → Macros**.

## Script

Vous pouvez télécharger la macro depuis GitHub : [Macro CenterOfMass.FCMacro](https://github.com/FreeCAD/FreeCAD-macros/blob/master/Information/CenterOfMass.FCMacro)

Vous pouvez utiliser ce fichier de l\'icône comme une icône de la barre d\'outils : ![](images/Macro_CenterOfMass.svg )



## Lien

La discussion sur le forum : [Macro to compute center of mass](https://forum.freecad.org/viewtopic.php?f=24&t=31883)

## Version

Version / Date de merge

0.8.0 / 2025-01-06 : merci à farahats9 pour sa contribution

-   Nouveau : afficher le volume et la surface
-   Nouveau : calcul des moments d\'inertie
-   Correction : la macro fonctionne maintenant avec l\'exemple d\'assemblage dans FreeCAD 1.0
-   Correction : sélection automatique du matériau pour les solides s\'il est déjà assigné par le nouveau système de matériaux.
-   Modifications mineures de l\'interface utilisateur

0.7.6 / 2024-08-01 : préparation à la version majeure de FreeCAD

-   Correction : faire fonctionner l\'exemple d\'assemblage 0.22.0dev.
-   Correction : importation d\'une nomenclature contenant un matériau personnalisé
-   Correction : support des nouveaux jeux de paramètres de matériaux
-   Correction : icônes modifiées ou manquantes, vérification des versions

0.7.3 / 2023-09-11 :

-   Nouveau : ajout de boutons pour copier dans le presse-papier
-   Nouveau : icône de graphiques vectoriels évolutifs
-   Correction : compatibilité avec les versions de FreeCAD et le web

0.7.0 / 2023-02-13 :

-   Nouveau : barre de recherche pour les solides
-   Nouveau : fonction d\'importation retravaillée pour améliorer l\'importation de nomenclatures externes avec une meilleure tolérance d\'entrée. La légende \"poids\" doit être changée en \"masse\" si vous voulez importer la masse d\'un ancien fichier d\'exportation de la macro.
-   Nouveau : la masse peut être mise à zéro pour exclure le solide du calcul et de la visualisation.
-   Correction : comportement de la rotation de la valeur par défaut et \"Appliquer à tous\"
-   Correction : préservation de la couleur originale des solides lorsque le bouton \"Nouveau\" est pressé.

0.6.0 / 2022-08-27 :

-   Nouveau : les masses sont éditables (une fonctionnalité très demandée)
-   Nouveauté : mise en évidence du solide sur lequel vous travaillez
-   Nouveau : pas d\'entrées dupliquées lorsque le conteneur et le contenu sont sélectionnés simultanément
-   Nouveau : les camemberts affichent la relation de densité dans la boîte combo.
-   Nouveau : lisibilité du texte sur les combo-boxes colorées avec la conformité WCAG21 1.4.6 Contrast (Enhanced).
-   Correction : une partie utilisée comme conteneur pour des maillages (par exemple .stl) est reconnue correctement.
-   Correction : corrections pour la gestion des erreurs et de la langue, l\'édition des matériaux, l\'ajustement de la taille des combo-boxes et de l\'interface graphique.

0.5.8 / 2022-05-31 :

-   Réinsertion : boîte de délimitation
-   Nouveau : réglage pour colorer les sphères
-   Nouveau : paramètre pour changer les cartes de couleur
-   GUI réorganisée : calcul de mise à jour ajouté, Densité totale ajoutée
-   Correction : les boîtes de messages ne pouvaient pas être utilisées lorsque FreeCAD n\'était pas exécuté sur l\'écran principal dans une configuration multi-moniteur.
-   Correction : plus d\'une maille n\'était pas calculée correctement

0.5.0 / 2022-04-07 : réécriture complète par s-quirin (projet SyProLei à l\'Université de la Sarre)

-   Nouveau : base de code, Exigences augmentées à Qt5.12+ et Python3 (FreeCAD 0.19).
-   Nouveau : affichage de la masse de chaque solide.
-   Nouveau : fenêtre de démarrage ancrée ou flottante (peut être définie dans l\'éditeur de paramètres).
-   Nouveau : la sélection correspond à l\'arborescence ou est triée par nom (peut être défini dans l\'éditeur de paramètres).
-   Nouveau : option pour sauvegarder les densités dans le document.
-   Amélioré : l\'aspect et la convivialité du Gui similaire à FreeCAD.
-   Amélioration : palette de couleurs échelonnée (du vert au rouge) pour colorer les formes.
-   Amélioration : visualisation du déplacement du centre de masse sur la géométrie.
-   Amélioration : suivi interne des unités.
-   Correction : gestion des groupes et des objets de groupe.
-   Correction : gestion de App::Link.
-   Correction : remplacement d\'une classe Qt obsolète.

0.4.1 / 2019-05-25 : dernière mise à jour avec les anciennes exigences et l\'interface graphique disponible dans le dépôt officiel.

0.1.2 / 2018-11-10 : version initiale de chupins fusionnée dans le dépôt officiel.



---
⏵ [documentation index](../README.md) > Macro CenterOfMass/fr
