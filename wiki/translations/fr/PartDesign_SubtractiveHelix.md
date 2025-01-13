---
 GuiCommand:
   Name: PartDesign SubtractiveHelix
   Name/fr: PartDesign Hélice soustractive
   MenuLocation: PartDesign , Créer une fonction soustractive , Hélice soustractive
   Workbenches: PartDesign_Workbench/fr
   Version: 0.19
   SeeAlso: PartDesign_AdditiveHelix/fr
---

# PartDesign SubtractiveHelix/fr

## Description

L\'outil **Hélice soustractive** modifie un solide en balayant une esquisse ou un objet 2D sélectionné le long d\'une trajectoire d\'hélice et le soustrayant au matériau.

![](images/PartDesign_SubtractiveHelix_example_overview.png )

*Le profil (B) est balayé autour de l\'axe (A) pour réaliser la rainure hélicoïdale (C) dans la pièce préexistante*



## Utilisation

1.  Sélectionnez l\'esquisse à balayer en hélice. Il est également possible d\'utiliser une face sur le solide existant.
2.  Appuyez sur le bouton **<img src="images/PartDesign_SubtractiveHelix.svg" width=24px> [Hélice soustractive ](PartDesign_SubtractiveHelix/fr.md)**.
3.  Définissez les paramètres de l\'hélice (voir la section suivante).
4.  Inspectez l\'hélice dans la fenêtre de vue pour vous assurer que les paramètres n\'entraînent pas une hélice auto-sécante.
5.  Appuyez sur **OK**.

## Options

Lors de la création d\'une hélice soustractive, la boîte de dialogue **Paramètres de l\'hélice** propose plusieurs paramètres spécifiant comment l\'esquisse doit être balayée.

![](images/PartDesign_SubtractiveHelix_taskpanel.png )



### Axe

Cette option spécifie l\'axe autour duquel l\'esquisse doit être balayée.

-   **Axe normal à l\'esquisse** : sélectionne la normale de l\'esquisse qui passe par l\'origine de l\'esquisse comme axe. {{Version/fr|0.20}}
-   **Axe vertical de l\'esquisse** : sélectionne l\'axe vertical de l\'esquisse.
-   **Axe horizontal de l\'esquisse** : sélectionne l\'axe horizontal de l\'esquisse.
-   **Ligne de construction** : sélectionne une ligne de construction contenue dans l\'esquisse utilisée par l\'hélice. La liste déroulante contiendra une entrée pour chaque ligne de construction. La première ligne de construction créée dans l\'esquisse sera intitulée *Ligne de construction 1*.
-   **Axes (X/Y/Z)** : sélectionne l\'axe X, Y ou Z de l\'origine du corps ;
-   **Sélectionner une référence\...** : permet de sélectionner dans la vue 3D une arête sur le corps ou une [ligne de référence](PartDesign_Line/fr.md).

### Mode

Ceci contrôle les paramètres qui seront utilisés pour définir l\'hélice. Les choix sont :

-   **Pas-Hauteur-Angle** : définition via la hauteur par tour et la hauteur totale.
-   **Pas-Tours-Angle** : définition par la hauteur par tour et le nombre de tours.
-   **Hauteur-Tours-Angles** : définition par la hauteur totale et le nombre de tours.
-   **Hauteur-Tours-Croissance** {{Version/fr|0.20}} : définition via la hauteur totale, le nombre de tours et la croissance du rayon de l\'hélice. Ainsi une Hauteur de zéro conduit à une trajectoire en forme de spirale. Une Hauteur et une Croissance de zéro conduit à une trajectoire en forme de cercle.



### Pas

La distance entre les tours dans l\'hélice.



### Hauteur

La hauteur de l\'hélice (centre-centre).



### Tours

Le nombre de tours dans l\'hélice. Définit par le rapport hauteur/pas.



### Angle du cône 

Angle du cône qui forme une coque autour de l\'hélice. Plage autorisée : \[-89°, +89°\].



### Pas à gauche 

Si cette case est cochée, le sens de rotation de l\'hélice est inversé, passant par défaut du sens horaire par défaut au sens antihoraire.



### Inversé

Si la case est cochée, la direction de l\'axe de l\'hélice est inversée par rapport à la valeur par défaut.



### Supprimer l\'extérieur du profil 

Si la case est cochée, le résultat sera l\'intersection du profil balayé et du corps préexistant.



### Mettre à jour la vue 

Si la case est cochée, l\'hélice sera affichée dans la vue et la mise à jour sera automatique à chaque modification des paramètres.



## Préférences

-   Une hélice soustractive qui n\'intersecte pas le corps sera visible dans l\'aperçu si **Outils → Éditer paramètres.... → BaseApp → Préférences → Mod → PartDesign → SubtractiveHelixPreview** est réglé sur `True`. La valeur par défaut de cette préférence est `False`. {{Version/fr|0.20}}



## Propriétés

-    **Pitch**: distance axiale entre deux spires.

-    **Height**: longueur totale de l\'hélice (sans tenir compte de l\'étendue du profil)

-    **Turns**: nombre de tours (ne doit pas être un nombre entier)

-    **Left Handed**: voir [Pas à gauche](#Pas_à_gauche.md).

-    **Reversed**: vrai ou faux. Voir [Inversé](#Invers.C3.A9.md).

-    **Angle**: rapport avec lequel le rayon de l\'hélice augmente le long de l\'axe. Plage admissible: \[-89°, +89°\].

-    **Reference axis**: axe de l\'hélice

-    **Mode**: mode d\'entrée de l\'hélice (hauteur de pas, tours de pas, hauteur de tours)

-    **Outside**: si vrai, le résultat sera l\'intersection du profil balayé et du corps préexistant.

-    **Has Been Edited**: si faux, l\'outil proposera une valeur initiale pour le pas basée sur la boîte englobante du profil, de sorte que l\'auto-intersection soit évitée.

-    **Refine**: vrai ou faux. Si la valeur est vraie, nettoie le solide des arêtes résiduelles laissées par les fonctions. Voir [Part Affiner la forme](Part_RefineShape/fr.md) pour plus de détails.

-    **Profile**: soit une esquisse contenant un contour fermé, soit une face.

-    **Midplane**: non utilisé.

-    **Up to face**: non utilisé.

-    **Allow multiple face**: non utilisé.



## Remarques

-   Une <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:16px;"> [PartDesign Forme liée](PartDesign_ShapeBinder/fr.md) ne peut pas être utilisée pour le profil.
-   Lors de l\'utilisation d\'une <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:16px;"> [PartDesign Sous forme liée](PartDesign_SubShapeBinder/fr.md) pour le profil, la sélection de la liaison dans la [vue en arborescence](Tree_view/fr.md) échouera, mais la face de la liaison devra être sélectionnée dans la [vue 3D](3D_view/fr.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveHelix/fr
