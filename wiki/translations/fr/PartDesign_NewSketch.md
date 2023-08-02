---
- GuiCommand:
   Name: PartDesign NewSketch
   Name/fr: PartDesign Esquisse
   MenuLocation: Esquisse -> Créer une esquisse
   Workbenches: PartDesign_Workbench/fr
   Version: 0.17
   SeeAlso: Sketcher_NewSketch/fr
---

# PartDesign NewSketch/fr

## Description

Cet outil crée une nouvelle esquisse. Il crée un nouveau [PartDesign Corps](PartDesign_Body/fr.md) destiné à contenir l\'esquisse s\'il n\'en existe aucun et ouvre automatiquement l\'[atelier Sketcher](Sketcher_Workbench/fr.md) après sa création.

Lors de la création de modèles à l\'aide de l\'[atelier PartDesign](PartDesign_Workbench/fr.md), cet outil doit être préféré à l\'outil **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketcher Esquisse](Sketcher_NewSketch/fr.md)** situé dans l\'[atelier Sketcher](Sketcher_Workbench/fr.md).



## Utilisation

1.  Appuyez sur le bouton **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Créer une esquisse](PartDesign_NewSketch/fr.md)** de la barre d\'outils PartDesign.
2.  Dans le panneau des tâches, la boîte de dialogue **Sélectionner une fonction** s\'ouvre. Sélectionnez l\'un des plans dans la liste ou depuis la vue 3D, qui peut être réorientée pour une meilleure visibilité.
3.  Appuyez sur **OK**.
4.  L\'interface bascule automatiquement vers l\'atelier Sketcher et l\'esquisse peut être modifiée. Une fois l\'esquisse terminée, l\'interface retourne dans l\'atelier PartDesign et la vue 3D est restaurée selon l\'orientation de la vue avant la création de l\'esquisse.
5.  Vous pouvez également sélectionner un plan ou une face sur le corps actif existant avant de créer l\'esquisse, auquel cas l\'esquisse est créée instantanément.

## Options

-   Pour modifier le rattachement d\'une esquisse existante, modifiez sa propriété **Map Mode** (voir [Propriétés](#Propriétés.md).)

-   La boîte de dialogue *Sélectionner une fonction* définit les caractéristiques de la nouvelle esquisse

:   

    :   <img alt="" src=images/PartDesign.CreateSketch.SelectFeatureDialog.jpeg  style="width:300px;">
    :   Boîte de dialogue *Sélectionner une fonction*. Ces paramètres créent une esquisse sur le plan XY et permettent des références croisées à partir d\'autres éléments du même corps

Paramètres de la boîte de dialogue

-   Système de coordonnées : définit l\'orientation du plan d\'esquisse
-   Autoriser les fonctionnalités utilisées : *à définir*

:   Autoriser les options de fonctionnalités externes

-   À partir d\'autres corps de la même pièce : tous les éléments utilisés dans le même corps peuvent être référencés
-   De différentes pièces ou fonctions indépendantes : *à définir*
-   Faire une copie indépendante : tous les autres éléments seront des copies séparées, c\'est-à-dire qu\'ils ne changeront pas lorsque l\'original sera modifié.
-   Faire une copie dépendante : les éléments seront des copies, mais une dépendance aux éléments d\'origine est conservée. Ceci utilise essentiellement une [PartDesign Forme liée](PartDesign_ShapeBinder/fr.md)
-   Créer une référence croisée : les éléments liés ne seront pas des copies mais pointent vers les éléments d\'origine, par ex. une esquisse principale. Toutes les modifications sont reflétées dans cette esquisse.

Pour référencer des éléments dans l\'[atelier Sketcher](Sketcher_Workbench/fr.md), utilisez les deux fonctions **<img src="images/Sketcher_External.svg" width=16px> [Sketcher Géométrie externe](Sketcher_External/fr.md)** et **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> [Sketcher Copie carbone](Sketcher_CarbonCopy/fr.md)**. En général, il est recommandé d\'utiliser d\'autres esquisses comme source pour les références plutôt que des faces ou des arêtes car elles sont moins affectées par le problème de dénomination topologique.



## Propriétés

-    **Map Mode**: mode de liaison de l\'esquisse à un autre objet, généralement un plan ou une face, mais pouvant être constitué d\'autres types d\'objets. Cliquez une fois dans le champ pour afficher un bouton **...** et appuyez dessus pour ouvrir la boîte de dialogue de [Part Ancrage](Part_EditAttachment/fr.md). Si défini à Désactivé, la propriété Placement est activée.

-    **Placement**: contrôle l\'orientation de l\'esquisse dans l\'espace 3D, voir [placement](Std_Placement/fr.md). Désactivé si l\'esquisse est liée via la propriété Map Mode.








{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign NewSketch/fr
