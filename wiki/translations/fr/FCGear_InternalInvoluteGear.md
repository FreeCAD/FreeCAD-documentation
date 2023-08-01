---
- GuiCommand:/fr
   Name:FCGear InternalInvoluteGear
   Name/fr:FCGear Engrenage à développante interne
   MenuLocation:Gear → Internal Involute Gear
   Workbenches:[FCGear](FCGear_Workbench/fr.md)
   Shortcut:Aucun
   Version:1.0
   SeeAlso:[FCGear Engrenage à développante](FCGear_InvoluteGear/fr.md)
---

# FCGear InternalInvoluteGear/fr

## Description

<img alt="" src=images/FCGear_InternalInvoluteGear-01.png  style="width:300px;">



*Engrenages à développante interne, de gauche à droite : engrenage droit, engrenage hélicoïdal, engrenage hélicoïdal double*

## Utilisation

1.  Passez à l\' <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur **[<img src=images/FCGear_InternalInvoluteGear.svg style="width:16px"> [Internal Involute Gear](FCGear_InternalInvoluteGear/fr.md)** dans la barre d\'outils.
    -   Sélectionnez l\'option **Gear → [<img src=images/FCGear_InternalInvoluteGear.svg style="width:16px"> Internal Involute Gear** dans le menu.
3.  Modifiez le paramètre de l\'engrenage en fonction des conditions requises (voir [Propriétés](#Propri.C3.A9t.C3.A9s.md)).

## Propriétés

Un objet FCGear InternalInvoluteGear est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|accuracy}}

-    **numpoints|Integer**: valeur par défaut à {{value|6}}. Changement du profil de la développante. La modification de la valeur peut entraîner des résultats inattendus.


{{Properties_Title|base}}

-    **height|Length**: valeur par défaut à {{value|5 mm}}. Valeur de la largeur de l\'engrenage.

-    **module|Length**: valeur par défaut à {{value|1 mm}}. Le module est le rapport du diamètre de référence de l\'engrenage divisé par le nombre de dents (voir [Remarques](FCGear_InvoluteGear/fr#Remarques.md)).

-    **teeth|Integer**: valeur par défaut est {{value|15}}. Nombre de dents (voir [Remarques](FCGear_InvoluteGear/fr#Remarques.md)).

-    **thickness|Length**: valeur par défaut est {{value|5 mm}}. Epaisseur de la partie extérieure non découpée de l\'engrenage.


{{Properties_Title|computed}}

-    **angular_backlash|Angle**: (lecture seule)

-    **da|Length**: (lecture seule) diamètre intérieur, mesuré à l\'addendum (la pointe des dents).

-    **df|Length**: (lecture seule) diamètre de la racine, mesuré au pied des dents.

-    **dw|Length**: (lecture seule) diamètre du pas de travail.

-    **outside_diameter|Length**: (lecture seule) diamètre extérieur.

-    **transverse_pitch|Length**: (lecture seule) pas dans le plan de rotation.


{{Properties_Title|fillets}}

-    **head_fillet|Float**: valeur par défaut à {{value|0 mm}}.

-    **root_fillet|Float**: valeur par défaut à {{value|0 mm}}.


{{Properties_Title|helical}}

-    **beta|Angle**: valeur par défaut à {{value|0 °}}. Avec l\'angle d\'hélice β, un engrenage hélicoïdal est créé - valeur positive → sens de rotation à droite, valeur négative → sens de rotation à gauche (voir [Remarques](FCGear_InvoluteGear/fr#Remarques.md)).

-    **double_helix|Bool**: valeur par défaut à {{false}}. {{true}} crée un engrenage à double hélice (voir [Remarques](FCGear_InvoluteGear/fr#Remarques.md)).

-    **properties_from_tool|Bool**: valeur par défaut à {{false}}. Si {{true}} et **beta** est différent de zéro, les paramètres de l\'engrenage sont recalculés en interne pour l\'engrenage tourné.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: valeur par défaut à {{value|20 °}}. (voir [Remarques](FCGear_InvoluteGear/fr#Remarques.md)).

-    **shift|Float**: valeur par défaut à {{value|0}}. Génère un décalage de profil positif et négatif (voir [Remarques](FCGear_InvoluteGear/fr#Remarques.md)).


{{Properties_Title|precision}}

-    **simple|Bool**: valeur par défaut à {{false}}. {{true}} génère un affichage simplifié (sans dents et seulement un cylindre en diamètre de pas).


{{Properties_Title|tolerance}}

-    **backlash|Length**: valeur par défaut à {{value|0 mm}}. Le jeu, également appelé lash ou play, est la distance entre les dents d\'une paire d\'engrenages.

-    **clearance|Float**: valeur par défaut à {{value|0.25}} (voir [Remarques](FCGear_InvoluteGear/fr#Remarques.md)).

-    **head|Float**: valeur par défaut à {{value|-0.4 mm}}. Cette valeur est utilisée pour modifier la hauteur des dents.

-    **reversed_backlash|Bool**: {{true}} diminution du jeu ou {{false}} augmentation du jeu (par défaut) (voir [Remarques](FCGear_InvoluteGear/fr#Remarques.md)).


{{Properties_Title|version}}

-    **version|String**:

## Remarques

Voir [FCGear InvoluteGear](FCGear_InvoluteGear/fr#Remarques.md).

## Formules utiles 

Voir [FCGear InvoluteGear](FCGear_InvoluteGear/fr#Formules_utiles.md).

## Script



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear InternalInvoluteGear/fr
