---
- GuiCommand:/fr
   Name:PartDesign AdditiveHelix
   Name/fr:PartDesign Hélice additive
   MenuLocation:Conception de pièces → Créer une fonction additive → Hélice additive
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.19
   SeeAlso:[PartDesign Hélice soustractive](PartDesign_SubtractiveHelix/fr.md)
---

## Description

L\'outil **Hélice additive** crée un solide en balayant une esquisse ou un objet 2D sélectionné le long d\'une hélice.

![](images/PartDesign_AdditiveHelix_example_overview.png )

*Le profil (B) est balayé autour de l\'axe (A) afin de produire l\'hélice solide (C)*

## Utilisation

1.  Sélectionnez l\'esquisse à balayer en hélice. Une face sur le solide existant peut également être utilisée.
2.  Appuyez sur le bouton **<img src="images/PartDesign_AdditiveHelix.svg" width=16px> [Hélice additive](PartDesign_AdditiveHelix/fr.md)**.
3.  Définissez les paramètres de l\'hélice (voir la section suivante).
4.  Inspectez l\'hélice dans la fenêtre de vue pour vous assurer que les paramètres n\'entraînent pas une hélice auto-sécante.
5.  Appuyez sur **OK**.

## Options

Lors de la création d\'une hélice additive, la boîte de dialogue **Paramètres de l\'hélice** propose plusieurs paramètres spécifiant comment l\'esquisse doit être balayée.

![](images/PartDesign_AdditiveHelix_taskpanel.png )

### Axis

Cette option spécifie l\'axe autour duquel l\'esquisse doit être balayée.

-   **Vertical sketch axis** : sélectionne l\'axe vertical de l\'esquisse.
-   **Horizontal sketch axis** : sélectionne l\'axe horizontal de l\'esquisse.
-   **Construction line** : sélectionne une ligne de construction contenue dans l\'esquisse utilisée par l\'hélice. La liste déroulante contiendra une entrée pour chaque ligne de construction. La première ligne de construction créée dans l\'esquisse sera intitulée *Construction line 1*.
-   **Base (X/Y/Z) axis** : sélectionne l\'axe X, Y ou Z de l\'origine du corps ;
-   **Select reference\...** : permet de sélectionner dans la vue 3D une arête sur le corps ou une [ligne de référence](PartDesign_Line/fr.md).

### Mode

Ceci contrôle les paramètres qui seront utilisés pour définir l\'hélice. Les choix autorisés sont :

-   **Pitch-Height-Angle** : définition via la hauteur par tour et la hauteur totale
-   **Pitch-Turns-Angle** : définition via la hauteur par tour et le nombre de tours
-   **Height-Turns-Angle** : définition via la hauteur totale et le nombre de tours
-   **Height-Turns-Growth** {{Version/fr|0.20}} : définition via la hauteur totale, le nombre de tours et la croissance du rayon hélicoïdal. Ainsi, une hauteur de zéro conduit à un chemin en forme de spirale. Une hauteur et une croissance de zéro, conduit à un chemin en forme de cercle.

### Pitch

La distance entre les tours dans l\'hélice.

### Height

La hauteur de l\'hélice (centre-centre).

### Turns

Le nombre de tours dans l\'hélice. Définit par le rapport hauteur/pas.

### Cone Angle 

Le rapport avec lequel le rayon de l\'hélice augmente le long de l\'axe. Plage autorisée : \[-89°, +89°\].

### Left handed 

Si coché, le sens de rotation de l\'hélice est inversé, passant par défaut du sens des aiguilles d\'une montre au sens inverse.

### Reversed

Si coché, la direction de l\'axe de l\'hélice est inversée par rapport à la valeur par défaut.

### Update view 

Si coché, l\'hélice sera affichée dans la vue et la mise à jour sera automatique à chaque modification des paramètres.

## Préférences

-   Une hélice additive qui n\'intersecte pas le corps sera visible dans l\'aperçu si **Outils → Éditer paramètres.... → BaseApp → Préférences → Mod → PartDesign → AdditiveHelixPreview** est réglé sur `True`. La valeur par défaut de cette préférence est `False`. {{Version/fr|0.20}}

## Propriétés

-    {{PropertyData/fr|Pitch}}: La distance axiale entre deux spires.

-    {{PropertyData/fr|Height}}: La longueur totale de l\'hélice (sans tenir compte de l\'étendue du profil)

-    {{PropertyData/fr|Turns}}: Le nombre de tours (ne doit pas être un nombre entier)

-    {{PropertyData/fr|Left Handed}}:

-    {{PropertyData/fr|Reversed}}: Vrai ou faux. Voir [Reversed](#Reversed.md).

-    {{PropertyData/fr|Angle}}: Le rapport avec lequel le rayon de l\'hélice augmente le long de l\'axe. Plage admissible : \[-89 °, + 89 °\].

-    {{PropertyData/fr|Reference axis}}: L\'axe de l\'hélice

-    {{PropertyData/fr|Mode}}: Le mode d\'entrée de l\'hélice (hauteur de pas, tours de pas, hauteur de tours)

-    {{PropertyData/fr|Outside}}: Non utilisé (utilisé dans l\'hélice soustractive)

-    {{PropertyData/fr|Has Been Edited}}: Si faux, l\'outil proposera une valeur initiale pour le pas basée sur la boîte englobante du profil, de sorte que l\'auto-intersection soit évitée.

-    {{PropertyData/fr|Refine}}: Vrai ou faux. Si la valeur est vraie, nettoie le solide des arêtes résiduelles laissées par les fonctions. Voir [Part Affiner la forme](Part_RefineShape/fr.md) pour plus de détails.

-    {{PropertyData/fr|Profile}}: Soit une esquisse contenant un contour fermé, soit une face.

-    {{PropertyData/fr|Midplane}}: Non utilisé.

-    {{PropertyData/fr|Up to face}}: Non utilisé.

-    {{PropertyData/fr|Allow multiple face}}: Non utilisé.

## Exemples

![Exemple d\'hélice utilisant une [B-spline](images/Sketcher_CreateBSpline/fr.md) dans l\'esquisse](PartDesign_AdditiveHelix_example_bspline.png )

![Exemple d\'hélice où l\'axe de l\'hélice est normal au plan de l\'esquisse, ce qui donne un effet de \"protrusion avec torsion\".](images/PartDesign_AdditiveHelix_example_twisting_pad.png )





{{PartDesign Tools navi

}} 
