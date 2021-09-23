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
2.  Appuyez sur le bouton **<img src="images/PartDesign_SubtractiveHelix.svg" width=24px> [Balayer une esquisse sélectionnée le long d'une hélice et la soustraire au corps](PartDesign_SubtractiveHelix/fr.md)**.
3.  Définissez les paramètres de l\'hélice (voir la section suivante).
4.  Inspectez l\'hélice dans la fenêtre de vue pour vous assurer que les paramètres n\'entraînent pas une hélice auto-sécante.
5.  Appuyez sur **OK**.

## Options

Lors de la création d\'une hélice soustractive, la boîte de dialogue **Paramètres de l\'hélice** propose plusieurs paramètres spécifiant comment l\'esquisse doit être balayée.

![](images/PartDesign_SubtractiveHelix_taskpanel.png )

### Axis

Cette option spécifie l\'axe autour duquel l\'esquisse doit être balayée.

-   **Vertical sketch axis** : sélectionne l\'axe vertical de l\'esquisse.
-   **Horizontal sketch axis** : sélectionne l\'axe horizontal de l\'esquisse.
-   **Construction line** : sélectionne une ligne de construction contenue dans l\'esquisse utilisée par l\'hélice. La liste déroulante contiendra une entrée pour chaque ligne de construction. La première ligne de construction créée dans l\'esquisse sera intitulée *Construction line 1*.
-   **Base (X/Y/Z) axis** : sélectionne l\'axe X, Y ou Z de l\'origine du corps ;
-   **Select reference\...** : permet de sélectionner dans la vue 3D une arête sur le corps ou une [ligne de référence](PartDesign_Line/fr.md).

### Mode

Ceci contrôle les paramètres qui seront utilisés pour définir l\'hélice. Les choix sont :

-   **Pitch-Height-Angle** : définition via la hauteur par tour et la hauteur totale.
-   **Pitch-Turns-Angle**: définition par la hauteur par tour et le nombre de tours.
-   **Height-Turns-Angle**: définition par la hauteur totale et le nombre de tours.
-   **Height-Turns-Growth** {{Version/fr|0.20}} : définition via la hauteur totale, le nombre de tours et la croissance du rayon de l\'hélice. Ainsi une Hauteur de zéro conduit à un parcours en forme de spirale. Une Hauteur et une Croissance de zéro à conduit à un chemin en forme de cercle.

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

### Remove outside of profile 

Si coché, le résultat sera l\'intersection du profil balayé et du corps préexistant.

### Update view 

Si coché, l\'hélice sera affichée dans la vue et la mise à jour sera automatique à chaque modification des paramètres.

## Préférences

-   Une hélice soustractive qui n\'intersecte pas le corps sera visible dans l\'aperçu si **Outils → Éditer paramètres.... → BaseApp → Préférences → Mod → PartDesign → SubtractiveHelixPreview** est réglé sur `True`. La valeur par défaut de cette préférence est `False`. {{Version/fr|0.20}}

## Propriétés

-    {{PropertyData/fr|Pitch}}: La distance axiale entre deux spires.

-    {{PropertyData/fr|Height}}: La longueur totale de l\'hélice (sans tenir compte de l\'étendue du profil)

-    {{PropertyData/fr|Turns}}: Le nombre de tours (ne doit pas être un nombre entier)

-    {{PropertyData/fr|Left Handed}}:

-    {{PropertyData/fr|Reversed}}: Vrai ou faux. Voir [Reversed](#Reversed.md).

-    {{PropertyData/fr|Angle}}: Le rapport avec lequel le rayon de l\'hélice augmente le long de l\'axe. Plage admissible: \[-89°, +89°\].

-    {{PropertyData/fr|Reference axis}}: L\'axe de l\'hélice

-    {{PropertyData/fr|Mode}}: Le mode d\'entrée de l\'hélice (hauteur de pas, tours de pas, hauteur de tours)

-    {{PropertyData/fr|Outside}}: Si vrai, le résultat sera l\'intersection du profil balayé et du corps préexistant.

-    {{PropertyData/fr|Has Been Edited}}: Si faux, l\'outil proposera une valeur initiale pour le pas basée sur la boîte englobante du profil, de sorte que l\'auto-intersection soit évitée.

-    {{PropertyData/fr|Refine}}: Vrai ou faux. Si la valeur est vraie, nettoie le solide des arêtes résiduelles laissées par les fonctions. Voir [Part Affiner la forme](Part_RefineShape/fr.md) pour plus de détails.

-    {{PropertyData/fr|Profile}}: Soit une esquisse contenant un contour fermé, soit une face.

-    {{PropertyData/fr|Midplane}}: Non utilisé.

-    {{PropertyData/fr|Up to face}}: Non utilisé.

-    {{PropertyData/fr|Allow multiple face}}: Non utilisé.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveHelix/fr
