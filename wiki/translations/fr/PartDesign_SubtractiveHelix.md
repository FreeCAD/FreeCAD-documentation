---
- GuiCommand:/fr
   Name:PartDesign SubtractiveHelix
   Name/fr:PartDesign Hélice soustractive
   MenuLocation:Conception de pièces → Créer une fonction soustractive → Hélice soustractive
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.19
   SeeAlso:[PartDesign Hélice additive](PartDesign_AdditiveHelix/fr.md)
---

# PartDesign SubtractiveHelix/fr

## Description

L\'outil **Hélice soustractive** modifie un solide en balayant une esquisse ou un objet 2D sélectionné le long d\'une trajectoire d\'hélice et le soustrayant au matériau.

![](images/PartDesign_SubtractiveHelix_example_overview.png )

*Le profil (B) est balayé autour de l\'axe (A) pour réaliser la rainure hélicoïdale (C) dans la pièce préexistante*

## Utilisation

1.  Sélectionnez l\'esquisse à balayer en hélice. Une face sur le solide existant peut également être utilisée.
2.  Appuyez sur le bouton **<img src="images/PartDesign_SubtractiveHelix.svg" width=24px> [Hélice soustractive ](PartDesign_SubtractiveHelix/fr.md)**.
3.  Définissez les paramètres de l\'hélice (voir la section suivante).
4.  Inspectez l\'hélice dans la fenêtre de vue pour vous assurer que les paramètres n\'entraînent pas une hélice auto-sécante.
5.  Appuyez sur **OK**.

## Options

Lors de la création d\'une hélice soustractive, la boîte de dialogue **Paramètres de l\'hélice** propose plusieurs paramètres spécifiant comment l\'esquisse doit être balayée.

![](images/PartDesign_SubtractiveHelix_taskpanel.png )

### Axe

Cette option spécifie l\'axe autour duquel l\'esquisse doit être balayée.

-   **Normal sketch axis**: sélectionne la normale de l\'esquisse qui passe par l\'origine de l\'esquisse comme axe. {{Version/fr|0.20}}
-   **Axe d\'esquisse vertical**: sélectionne l\'axe vertical de l\'esquisse.
-   **Axe d\'esquisse horizontal** : sélectionne l\'axe horizontal de l\'esquisse.
-   **Ligne de construction** : sélectionne une ligne de construction contenue dans l\'esquisse utilisée par l\'hélice. La liste déroulante contiendra une entrée pour chaque ligne de construction. La première ligne de construction créée dans l\'esquisse sera intitulée *Ligne de construction 1*.
-   **Axes de base (X/Y/Z)** : sélectionne l\'axe X, Y ou Z de l\'origine du corps ;
-   **Sélectionnez une référence\...** : permet de sélectionner dans la vue 3D une arête sur le corps ou une [ligne de référence](PartDesign_Line/fr.md).

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

### Gaucher

Si coché, le sens de rotation de l\'hélice est inversé, passant par défaut du sens des aiguilles d\'une montre au sens inverse.

### Inversé

Si coché, la direction de l\'axe de l\'hélice est inversée par rapport à la valeur par défaut.

### Supprimer l\'extérieur du profil 

Si coché, le résultat sera l\'intersection du profil balayé et du corps préexistant.

### Réactualiser la vue 

Si coché, l\'hélice sera affichée dans la vue et la mise à jour sera automatique à chaque modification des paramètres.

## Préférences

-   Une hélice soustractive qui n\'intersecte pas le corps sera visible dans l\'aperçu si **Outils → Éditer paramètres.... → BaseApp → Préférences → Mod → PartDesign → SubtractiveHelixPreview** est réglé sur `True`. La valeur par défaut de cette préférence est `False`. {{Version/fr|0.20}}

## Propriétés

-    **Pitch**: La distance axiale entre deux spires.

-    **Height**: La longueur totale de l\'hélice (sans tenir compte de l\'étendue du profil)

-    **Turns**: Le nombre de tours (ne doit pas être un nombre entier)

-    **Left Handed**: Voir [Gaucher](#Gaucher.md).

-    **Reversed**: Vrai ou faux. Voir [Inversé](#Invers.C3.A9.md).

-    **Angle**: Le rapport avec lequel le rayon de l\'hélice augmente le long de l\'axe. Plage admissible: \[-89°, +89°\].

-    **Reference axis**: L\'axe de l\'hélice

-    **Mode**: Le mode d\'entrée de l\'hélice (hauteur de pas, tours de pas, hauteur de tours)

-    **Outside**: Si vrai, le résultat sera l\'intersection du profil balayé et du corps préexistant.

-    **Has Been Edited**: Si faux, l\'outil proposera une valeur initiale pour le pas basée sur la boîte englobante du profil, de sorte que l\'auto-intersection soit évitée.

-    **Refine**: Vrai ou faux. Si la valeur est vraie, nettoie le solide des arêtes résiduelles laissées par les fonctions. Voir [Part Affiner la forme](Part_RefineShape/fr.md) pour plus de détails.

-    **Profile**: Soit une esquisse contenant un contour fermé, soit une face.

-    **Midplane**: Non utilisé.

-    **Up to face**: Non utilisé.

-    **Allow multiple face**: Non utilisé.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveHelix/fr
