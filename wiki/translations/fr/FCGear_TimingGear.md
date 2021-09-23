---
- GuiCommand:/fr
   Name:FCGear TimingGear
   Name/fr:FCGear TimingGear
   MenuLocation:FCGear → Create a Timing gear
   Workbenches:[FCGear](FCGear_Workbench/fr.md)
   Version:v0.16
---

# FCGear TimingGear/fr

## Description

Le but des engrenages de distribution est de permettre à l\'arbre à cames et au vilebrequin de faire tourner la chaîne de distribution. Le vilebrequin tourne pour déplacer les pistons de haut en bas à l\'intérieur des cylindres. L\'arbre à cames tourne pour permettre aux soupapes d\'admission et d\'échappement des cylindres de s\'ouvrir et de se fermer. Ces composants sont importants pour le bon calage du moteur.

Les engrenages de distribution sont connectés à une courroie de distribution ou une chaîne de distribution.

:   ![](images/Timing-Gear_example.png )
:   
    *Au-dessus: engrenage de distribution*
    

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Lancez la commande d\'une de ces manières:
    -   Appuyez sur le bouton <img alt="" src=images/FCGear_TimingGear.svg  style="width:22px;"> [Create a Timing gear](FCGear_WormGear/fr.md) dans la barre d\'outils.
    -   Utilisez le **Gear Menu → Timing gear**.
3.  Modifier le paramètre d\'engrenage selon les conditions requises (voir **Propriétés → Données** ci-dessous).

## Propriétés

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Placement}}: [Placement](Placement/fr.md) est l\'emplacement et l\'orientation d\'un objet dans l\'espace.

-    {{PropertyData/fr|Label}}: nom d\'utilisateur de l\'objet dans [vue en arborescence](tree_view/fr.md).


{{Properties_Title|computed}}

-    {{PropertyData/fr|h}}: Hauteur radiale des dents (non modifiable, calculée automatiquement).

-    {{PropertyData/fr|offset}}: X-Offset du point médian du deuxième arc (non modifiable, calculé automatiquement).

-    {{PropertyData/fr|pitch}}: Pas de vitesse (non modifiable, calculé automatiquement).

-    {{PropertyData/fr|r0}}: Le rayon du premier arc (non modifiable, calculé automatiquement).

-    {{PropertyData/fr|r1}}: Le rayon du deuxième arc (non modifiable, calculé automatiquement).

-    {{PropertyData/fr|rs}}: Le rayon du troisième arc (non modifiable, calculé automatiquement).

-    {{PropertyData/fr|u}}: Différence radiale entre le pas... diamètre et la tête d\'engrenage (non modifiable, calculée automatiquement).


{{Properties_Title|gear_parameter}}

-    {{PropertyData/fr|height}}: La valeur par défaut est 5,00 mm. Valeur de la largeur de l\'engrenage.

-    {{PropertyData/fr|teeth}}: La valeur par défaut est 20. Nombre de dents.

-    {{PropertyData/fr|type}}: La valeur par défaut est gt2. Type d\'engrenage de distribution - pas de profil pour les courroies de distribution (voir également les informations dans **Remarques**).

### Vue

La description des paramètres de l\'onglet **View** se trouve dans l\'[Éditeur de propriétés](Property_editor/fr.md) dans **Exemple de propriétés d'un objet PartDesign**.

## Remarques

-    **type**: Le pas des courroies de distribution (distance du centre de la dent au centre de la dent des dents consécutives) est spécifié en types. GT2 a un pas de 2 mm, GT3 de 3 mm, GT5 de 5 mm etc\...

## Limitations

Les limitations ne sont pas encore connues.

## Formules utiles 

-    **addendum diameter**= **pitch diameter** + 2 \* **module**

-    **belt length**= 2 \* **axle base** + **belt tooth pitch** : 2 \* **(teeth 1 + 2)** + **belt tooth pitch²** : 4 \* pi² \* **axle base** \* **(teeth 1 - 2)²**

-    **axel base**= **belt length** : 4 - **belt tooth pitch** : 8 \* **(teeth 1+2)** + ¼ \* sqrt \[**belt length** - ½ \* **belt tooth pitch** \* **(teeth 1+2)²** - 2 \* **belt tooth pitch²** \* **(teeth 1+2)²** : pi²\]




[Category:Addons](Category:Addons.md) [Category:FCGear](Category:FCGear.md) [Category:External Command Reference](Category:External_Command_Reference.md)

---
[documentation index](../README.md) > [Addons](Category:Addons.md) > FCGear TimingGear/fr
