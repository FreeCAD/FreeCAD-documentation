---
 GuiCommand:
   Name: Std Measure
   Name/fr: Std Mesurer
   MenuLocation: Outils , Mesurer
   Workbenches: Tous
   Version: 1.0
   SeeAlso: Draft_Dimension/fr
---

# Std Measure/fr

## Description

La commande **Std Mesurer** donne accès à l\'outil de mesures unifiées. Elle remplace plusieurs anciennes commandes de mesure, offrant ainsi une fonctionnalité de mesure polyvalente.



## Utilisation

1.  Vous pouvez présélectionner les entités à mesurer.
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Std_Measure.svg" width=16px> [Mesurer](Std_Measure/fr.md)
**
    -   Sélectionnez l\'option **Outils → <img src="images/Std_Measure.svg" width=16px> Mesurer** du menu.
3.  Le panneau des tâches **Mesure** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
4.  Si aucune entité géométrique n\'a été présélectionnée, effectuez l\'une des opérations suivantes :
    -   Sélectionnez les entités géométriques tout en laissant le *Mode* à *Automatique* pour que le mode soit automatiquement déterminé en fonction de la sélection.
    -   Choisissez un *Mode* autre que *Automatique* et sélectionnez ensuite les entités géométriques (un nouveau clic sur celles-ci les désélectionnera) :
        -   *Distance* : distance la plus courte entre les entités sélectionnées. Si des arêtes circulaires sont sélectionnées, la distance entre les centres des cercles est mesurée,
        -   *Distance libre* : distance entre deux points librement sélectionnés (appartenant à des entités différentes telles que des arêtes, des faces).
        -   *Angle* : angle entre les entités sélectionnées,
        -   *Longueur* : longueur de l\'arête sélectionnée,
        -   *Position* : coordonnées du sommet sélectionné,
        -   *Surface* : surface de la face sélectionnée,
        -   *Rayon* : rayon de l\'arête circulaire sélectionnée,
        -   *Centre d\'inertie* : centre d\'inertie de l\'arête, de la face ou du solide sélectionné (uniquement si présélectionné dans l\'arborescence).
5.  Le résultat de la mesure sera affiché dans le champ *Résultat* et sur une infobulle affichée dans la [vue 3D](3D_view/fr.md). Cette infobulle comprendra également une icône indiquant le type de mesure. Les infobulles peuvent être personnalisées dans le [réglage des préférences](Preferences_Editor/fr.md). Elles peuvent être déplacées dans la vue 3D en les faisant glisser à l\'aide d\'un curseur.
6.  Appuyez sur le bouton **Réinitialiser** pour supprimer la mesure ou sur le bouton **Enregistrer** pour la conserver. Les mesures sauvegardées sont placées dans un [groupe](Std_Group/fr.md) de mesures dans la [vue en arborescence](Tree_view/fr.md).
7.  Appuyez sur **Échap** ou sur le bouton **Fermer** pour terminer la commande.

## Options

1.  
    {{Version/fr|1.1}}: vous pouvez appuyez sur le bouton **<img src="images/Preferences-system.svg" width=x16px> <img src="images/Toolbar_flyout_arrow.svg" width=x16px>** pour changer les paramètres :

    -   *Sauvegarde automatique* : si la case est cochée, la dernière mesure est sauvegardée lors du démarrage d\'une nouvelle mesure (maintenir **Maj** peut temporairement désactiver ce comportement),
    -   *Sélection additive* : si la case est cochée, cliquer sur des entités géométriques successives les ajoute en tant que sélections pour la même mesure, sinon **Ctrl** doit être pressé pour le faire.

-   Pour les modes *Distance* et *Distance libre*, la case à cocher **Afficher les delta** est affichée. Si cette case est cochée, la propriété **Show Delta** de la mesure est définie à `True` et 3 mesures projetées supplémentaires sont affichées dans la [vue 3D](3D_view/fr.md).



## Propriétés



### Données


{{TitleProperty|Measurement}}

-    **Element1|LinkSub**: premier élément de la mesure.

-    **Element2|LinkSub**: deuxième élément de la mesure.

-    **Distance|Distance**: distance entre les deux éléments.

-    **Distance X|Distance**: distance dans la direction X (uniquement pour les mesures *Distance* et *Distance libre*).

-    **Distance Y|Distance**: distance dans la direction Y (idem).

-    **Distance Z|Distance**: distance dans la direction Z (idem).

-    **Position1|Vector|Hidden**: position du premier point mesuré (en lecture seule).

-    **Position2|Vector|Hidden**: position du deuxième point mesuré (en lecture seule).



### Vue


{{TitleProperty|Appearance}}

-    **Font Size|Integer**: taille de la police pour l\'infobulle de la cote sauvegardée.

-    **Line Color|Color**: couleur de la ligne de la cote affichée dans la vue 3D.

-    **Show Delta|Bool**: si `True`, les mesures de distance projetées sont affichées dans la vue 3D. (Uniquement pour les mesures *Distance* et *Distance libre*).

-    **Text Background Color|Color**: couleur de l\'arrière-plan de l\'infobulle de la cote.

-    **Text Color|Color**: couleur du texte et du symbole de l\'infobulle de la cote.



## Remarques

-   Cette commande est le résultat d\'un [projet GSoC de 2023 (En)](Unified_Measurement_Facility.md).





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std Measure/fr
