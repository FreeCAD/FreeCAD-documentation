---
 GuiCommand:
   Name: FCGear CycloidRack
   Name/fr: FCGear Crémaillère cycloïde
   MenuLocation: Gear , Cycloid Rack
   Workbenches: FCGear_Workbench/fr
   Shortcut: Aucun
   Version: 1.0
   SeeAlso: FCGear_CycloidGear/fr
---

# FCGear CycloidRack/fr

## Description

<img alt="" src=images/FCGear_CycloidRack-01.png  style="width:200px;">



*Crémaillères cycloïdes de gauche à droite : engrenage droit, engrenage hélicoïdal, engrenage hélicoïdal double*

## Utilisation

1.  Passez à l\' <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur **[<img src=images/FCGear_CycloidRack.svg style="width:16px"> [Cycloid Rack](FCGear_CycloidRack/fr.md)** dans la barre d\'outils.
    -   Sélectionnez **Gear → [<img src=images/FCGear_CycloidRack.svg style="width:16px"> Cycloid Rack** dans le menu.
3.  Modifiez le paramètre de l\'engrenage en fonction des conditions requises (voir [Propriétés](#Propri.C3.A9t.C3.A9s.md)).

## Propriétés

Un objet FCGear CycloidRack est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :


{{Properties_Title|accuracy}}

-    **numpoints|Integer**: valeur par défaut à {{value|15}}. Nombre de points pour la spline.


{{Properties_Title|base}}

-    **add_endings|bool**: si {{True}} (valeur par défaut), alors la longueur totale de la crémaillère est dents \* pas. Si {{False}}, alors la crémaillère commence par un front de dent.

-    **height|Length**: valeur par défaut à {{value|5 mm}}. Valeur de la largeur de l\'engrenage.

-    **teeth|Integer**: valeur par défaut à {{value|15}}. Nombre de dents.

-    **thickness|Length**: valeur par défaut à {{value|5 mm}}. Epaisseur de la partie non découpée de la crémaillère.


{{Properties_Title|computed}}

-    **transverse_pitch|Length**: (en lecture seule) le pas dans le plan transversal.


{{Properties_Title|cycloid}}

-    **inner_diameter|Float**: valeur par défaut à {{value|7.5}}. Diamètre du cercle de roulement de l\'hypocycloïde, normalisé par **module**. (voir [Remarques](FCGear_CycloidGear/fr#Remarques.md)).

-    **outer_diameter|Float**: valeur par défaut à {{value|7.5}}. Diamètre du cercle de roulement de l\'épicycloïde, normalisé par **module**. (voir [Remarques](FCGear_CycloidGear/fr#Remarques.md)).


{{Properties_Title|fillets}}

-    **head_fillet|Float**: valeur par défaut à {{value|0}}.

-    **root_fillet|Float**: valeur par défaut à {{value|0}}.


{{Properties_Title|helical}}

-    **beta|Angle**: valeur par défaut à {{value|0 °}}. Avec l\'angle d\'hélice β, un engrenage hélicoïdal est créé (valeur positive → sens de rotation à droite, valeur négative → sens de rotation à gauche).

-    **double_helix|Bool**: valeur par défaut à {{false}}. {{true}} crée un engrenage à double hélice (voir [Remarques](FCGear_CycloidGear/fr#Remarques.md)).


{{Properties_Title|involute}}

-    **module|Length**: valeur par défaut à {{value|1 mm}}. Pour les crémaillères, le module est égal au pas et donc à la distance entre les points correspondants sur les dents adjacentes (voir [Remarques](FCGear_CycloidGear/fr#Remarques.md)).


{{Properties_Title|precision}}

-    **simplified|Bool**: valeur par défaut à {{false}}. Si {{true}}, la crémaillère est dessinée avec un nombre constant de dents pour éviter le renommage topologique.


{{Properties_Title|tolerance}}

-    **clearance|Float**: valeur par défaut à {{value|0.25}}. (voir [Remarques](FCGear_CycloidGear/fr#Remarques.md)).

-    **head|Float**: valeur par défaut à {{value|0}}. Longueur supplémentaire de la pointe des dents, normalisée par **module**.


{{Properties_Title|version}}

-    **version|String**:

## Remarques

Voir [FCGear CycloidGear](FCGear_CycloidGear/fr#Remarques.md).

## Formules utiles 

Voir [FCGear CycloidGear](FCGear_CycloidGear/fr#Formules_utiles.md).

## Script



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear CycloidRack/fr
