---
 GuiCommand:
   Name: FCGear BevelGear
   Name/fr: FCGear Engrenage conique
   MenuLocation: Gear , Bevel Gear
   Workbenches: FCGear_Workbench/fr
   Version: v0.16
---

# FCGear BevelGear/fr



## Description

L\'outil <img alt="" src=images/FCGear_BevelGear.svg  style="width:24px;"> [FCGear Engrenage conique](FCGear_BevelGear/fr.md) crée un engrenage conique de base, un objet solide qui doit être amélioré pour obtenir la forme finale correcte dans les étapes suivantes.

Les engrenages coniques ne sont pas utilisés aussi souvent que les autres types d\'engrenages, en partie à cause du bruit qu\'ils génèrent. Mais ils sont encore utilisés dans certains secteurs, tels que les emballages alimentaires et les aliments en conserve, les équipements de jardin et de pelouse, les machines telles que les perceuses et les broyeurs, les systèmes de compression pour le marché du gaz et du pétrole et les vannes de régulation de débit.

Les engrenages coniques en spirale ont des dents incurvées pour fournir un engagement plus doux et un plus grand contact dent sur dent par rapport à un engrenage conique droit. Cela réduit les vibrations et le bruit. Ils peuvent être utilisés à des vitesses élevées et sont généralement utilisés dans les transmissions de motos et de vélos.

![](images/Bevel-Gear_example.png ) 
*De gauche à droite : engrenage droit, engrenage en spirale*



## Utilisation

1.  Passez à l\' <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur **[<img src=images/FCGear_BevelGear.svg style="width:16px"> [Bevel Gear](FCGear_BevelGear/fr.md)** dans la barre d\'outils.
    -   Sélectionnez l\'option **Gear → [<img src=images/FCGear_BevelGear.svg style="width:16px"> Bevel Gear** dans le menu.
3.  Un objet BevelGear est créé selon les paramètres par défaut.
4.  Modifiez le paramètre de l\'engrenage en fonction des conditions requises (voir [Propriétés](#Propri.C3.A9t.C3.A9s.md)).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet FCGear BevelGear est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Base}}

-    **height|Length**: valeur par défaut à {{Value|5}}. Valeur de la largeur de l\'engrenage conique, mesurée à partir du cercle primitif.

-    **module|Length**: valeur par défaut à {{Value|1}}. Module est le rapport du diamètre primitif de l\'engrenage divisé par le nombre de dents (voir [Remarques](#Remarques.md)).

-    **reset_origin|Bool**: si {{True}} (par défaut), l\'origine de l\'engrenage est au centre du cercle primitif (bas de l\'engrenage). (voir [Remarques](#Remarques.md)).

-   : Si {{False}}, l\'origine de l\'engrenage se trouve à l\'extrémité du cône primitif.

-    **teeth|Integer**: valeur par défaut à {{Value|15}}. Nombre de dents.


{{Properties_Title|computed}}

-    **angular_backlash|Angle**: (lecture seule)

-    **dw|Length**: (lecture seule) diamètre du pas de travail.


{{Properties_Title|helical}}

-    **beta|Angle**: valeur par défaut à {{Value|0 °}}. Avec l\'angle d\'hélice β, un engrenage conique hélicoïdal est créé - valeur positive → sens de rotation à droite, valeur négative → sens de rotation à gauche.


{{Properties_Title|involute}}

-    **pitch_angle|Angle**: valeur par défaut à {{Value|45 °}}. Angle de conicité du cône primitif.


{{Properties_Title|involute_parameter}}

-    **pressure_angle|Angle**: valeur par défaut à {{Value|20 °}} (voir [Remarques](#Remarques.md)).


{{Properties_Title|precision}}

-    **numpoints|Integer**: valeur par défaut à {{Value|6}}, Modification du profil de la développante. Changer la valeur peut conduire à des résultats inattendus.


{{Properties_Title|tolerance}}

-    **backlash|Length**: valeur par défaut à {{Value|0}}. Le jeu, également appelé lash ou play, est la distance entre les dents d\'une paire d\'engrenages.

-    **clearance|Float**: valeur par défaut à {{Value|0.1}} (voir [Remarques](#Remarques.md)).


{{Properties_Title|version}}

-    **version|String**:



## Remarques

-   Les engrenages coniques sont assez complexes, car leurs propriétés dépendent non seulement du rapport de transmission, mais aussi de l\'angle entre les axes de l\'engrenage. L\'engrenage conique par défaut est construit pour des axes perpendiculaires et un rapport de 1:1.

-    **pitch angle**: l\'angle de conicité du cône est égal à la moitié de l\'angle entre les axes de l\'engrenage pour un rapport de 1:1, c\'est-à-dire 45° pour des axes perpendiculaires. Les angles primitifs pour d\'autres combinaisons de rapports et d\'angles entre les axes peuvent être déterminés géométriquement dans une [esquisse](Sketcher_Workbench/fr.md).

-    **clearance**: sur une paire d\'engrenages, le jeu est la distance entre l\'extrémité de la dent du premier engrenage et la racine de la dent du deuxième engrenage.

-    **module**: en utilisant les directives ISO (Organisation internationale de normalisation), la taille du module est désignée comme l\'unité représentant la taille des dents des engrenages. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Si vous multipliez Module par Pi, vous pouvez obtenir Pitch (p) (le pas). Le pas est la distance entre les points correspondants sur les dents adjacentes.

-    **pressure_angle**: ne modifier le paramètre que si l\'on dispose d\'une connaissance suffisante de la géométrie de l\'engrenage.

-    **reset_origin**: il est recommandé de régler le paramètre sur **false** pour que l\'origine de l\'engrenage se trouve à l\'extrémité du cône primitif. De cette manière, nous pouvons étendre la roue conique au-delà du plan du cercle primitif en utilisant la propriété du module.

-   Le point faible de cet outil est qu\'il construit la géométrie du diamètre primitif vers l\'extrémité et ignore le fait qu\'il existe également une géométrie dans la direction opposée. C\'est pourquoi nous devons déterminer la section transversale de l\'engrenage au niveau du cercle primitif appartenant au module choisi pour définir la géométrie de coupe et ensuite utiliser un engrenage conique étendu (mis à l\'échelle à partir de la pointe) à couper. (voir *réinitialiser l\'origine* ci-dessus)



## Formules utiles 

-    **pitch diameter**= **module** \* **teeth**

-    **addendum diameter**= **pitch diameter** + 2 \* **module** \* **cos angle du cône de référence**

-    **tip angle 1**= **(dents 1 + 2)** \* **(cos reference angle de cône 1)** : **(dents 2 - 2)** \* **(sin angle de cône de référence 1)**

-    **tip angle 2**= **(teeth 2 + 2)** \* **(cos reference angle de cône 2)** : **(teeth 1 - 2)** \* **(sin angle de cône de référence 2)**

-    **angle du cône de référence 1**= **(teeth 1)**: **(teeth 2)**

-    **angle du cône de référence 2**= **(teeth 2)**: **(teeth 1)**

-    **angle total de l'axe**= **angle du cône de référence 1** + **angle du cône de référence 2**

Angle du cône de référence substantiel \[TECH.\]



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External%20Command%20Reference.md) > FCGear BevelGear/fr
