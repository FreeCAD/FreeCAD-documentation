---
- GuiCommand:/fr
   Name:PartDesign AdditiveHelix
   Name/fr:PartDesign Hélice additive
   MenuLocation:Part Design → Créer une fonction additive → Hélice additive
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.19
   SeeAlso:[PartDesign Hélice soustractive](PartDesign_SubtractiveHelix/fr.md)
---

# PartDesign AdditiveHelix/fr

## Description

L\'outil **Hélice additive** crée un solide en balayant une esquisse ou un objet 2D sélectionné le long d\'une hélice.

<img alt="" src=images/PartDesign_AdditiveHelix_example_overview.png  style="width:650px;">

*Le profil (B) est balayé autour de l\'axe (A) afin de produire l\'hélice solide (C)*



## Utilisation

1.  Sélectionnez l\'esquisse à balayer en hélice. Il est également possible d\'utiliser une face sur le solide existant.
2.  Appuyez sur le bouton **<img src="images/PartDesign_AdditiveHelix.svg" width=16px> [Hélice additive](PartDesign_AdditiveHelix/fr.md)**.
3.  Définissez les paramètres de l\'hélice (voir la section suivante).
4.  Inspectez l\'hélice dans la fenêtre de vue pour vous assurer que les paramètres n\'entraînent pas une hélice auto-sécante.
5.  Appuyez sur **OK**.

## Options

Lors de la création d\'une hélice additive, la boîte de dialogue **Paramètres de l\'hélice** propose plusieurs paramètres spécifiant comment l\'esquisse doit être balayée.

![](images/PartDesign_AdditiveHelix_taskpanel.png )



### Axe

Cette option spécifie l\'axe autour duquel l\'esquisse doit être balayée.

-   **Axe normal à l\'esquisse** : sélectionne comme axe la normale de l\'esquisse qui passe par l\'origine de l\'esquisse. {{Version/fr|0.20}}
-   **Axe d\'esquisse vertical** : sélectionne l\'axe vertical de l\'esquisse. C\'est la valeur par défaut pour les nouvelles hélices.
-   **Axe d\'esquisse horizontal** : sélectionne l\'axe horizontal de l\'esquisse.
-   **Ligne de construction** : sélectionne une ligne de construction contenue dans l\'esquisse utilisée par l\'hélice. La liste déroulante contiendra une entrée pour chaque ligne de construction. La première ligne de construction créée dans l\'esquisse sera intitulée *Ligne de construction 1*.
-   **Axes de base (X/Y/Z)** : sélectionne l\'axe X, Y ou Z de l\'origine du corps;
-   **Sélectionnez une référence\...** : permet de sélectionner dans la vue 3D une arête sur le corps ou une [ligne de référence](PartDesign_Line/fr.md).

### Mode

Ceci contrôle les paramètres qui seront utilisés pour définir l\'hélice. Les choix autorisés sont :

-   **Pas-Hauteur-Angle** : définition via la hauteur par tour et la hauteur totale
-   **Pas-Tours-Angle** : définition via la hauteur par tour et le nombre de tours
-   **Hauteur-Tours-Angles** : définition via la hauteur totale et le nombre de tours
-   **Hauteur-Tours-Croissance** {{Version/fr|0.20}} : définition via la hauteur totale, le nombre de tours et la croissance du rayon hélicoïdal. Ainsi, une hauteur de zéro conduit à une trajectoire en forme de spirale. Une hauteur et une croissance de zéro, conduit à une trajectoire en forme de cercle.



### Pas

La distance entre les tours dans l\'hélice.



### Hauteur

La hauteur de l\'hélice (centre-centre).



### Tours

Le nombre de tours dans l\'hélice. Définit par le rapport hauteur/pas.



### Angle du cône 

Angle du cône qui forme une coque autour de l\'hélice. Plage autorisée : \[-89°, +89°\].



### Pas à gauche 

Si coché, le sens de rotation de l\'hélice est inversé, passant par défaut du sens des aiguilles d\'une montre au sens inverse.



### Inversé

Si coché, la direction de l\'axe de l\'hélice est inversée par rapport à la valeur par défaut.



### Mise à jour de la vue 

Si coché, l\'hélice sera affichée dans la vue et la mise à jour sera automatique à chaque modification des paramètres.



## Préférences

-   Une hélice additive qui n\'intersecte pas le corps sera visible dans l\'aperçu si **Outils → Éditer paramètres.... → BaseApp → Préférences → Mod → PartDesign → AdditiveHelixPreview** est réglé sur `True`. La valeur par défaut de cette préférence est `False`. {{Version/fr|0.20}}



## Propriétés

-    **Pitch**: distance axiale entre deux spires.

-    **Height**: longueur totale de l\'hélice (sans tenir compte de l\'étendue du profil)

-    **Turns**: nombre de tours (ne doit pas être un nombre entier)

-    **Left Handed**: voir [Gaucher](#Gaucher.md).

-    **Reversed**: vrai ou faux. Voir [Inversé](#Invers.C3.A9.md).

-    **Angle**: rapport avec lequel le rayon de l\'hélice augmente le long de l\'axe. Plage admissible : \[-89°, +89°\].

-    **Reference axis**: axe de l\'hélice

-    **Mode**: mode d\'entrée de l\'hélice (hauteur de pas, tours de pas, hauteur de tours)

-    **Outside**: non utilisé (utilisé dans l\'hélice soustractive)

-    **Has Been Edited**: si faux, l\'outil proposera une valeur initiale pour le pas basée sur la boîte englobante du profil, de sorte que l\'auto-intersection soit évitée.

-    **Refine**: vrai ou faux. Si la valeur est vraie, nettoie le solide des arêtes résiduelles laissées par les fonctions. Voir [Part Affiner la forme](Part_RefineShape/fr.md) pour plus de détails.

-    **Profile**: soit une esquisse contenant un contour fermé, soit une face.

-    **Midplane**: non utilisé.

-    **Up to face**: non utilisé.

-    **Allow multiple face**: non utilisé.



## Exemples

![Exemple d\'hélice utilisant une [B-spline](images/Sketcher_CreateBSpline/fr.md) dans l\'esquisse](PartDesign_AdditiveHelix_example_bspline.png )

![Exemple d\'hélice où l\'axe de l\'hélice est normal au plan de l\'esquisse, ce qui donne un effet de \"protrusion avec torsion\".](images/PartDesign_AdditiveHelix_example_twisting_pad.png )





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveHelix/fr
