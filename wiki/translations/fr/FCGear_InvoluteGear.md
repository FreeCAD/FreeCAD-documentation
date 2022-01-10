---
- GuiCommand:/fr
   Name:FCGear InvoluteGear
   Name/fr:FCGear InvoluteGear
   MenuLocation:FCGear → Create an Involute gear
   Workbenches:[FCGear](FCGear_Workbench/fr.md)
   Shortcut:Aucun
   Version:v0.16
   SeeAlso:[FCGear Engrenage cycloïde](FCGear_CycloideGear/fr.md)
---

# FCGear InvoluteGear/fr

## Description

En raison du rapport d\'engrènement favorable et de la production relativement simple, l\'engrenage à développante est la forme de dent la plus courante en génie mécanique. Les roues dentées se trouvent partout où le mouvement et la force doivent être transférés d\'une pièce à l\'autre. Par exemple, ils peuvent être trouvés dans des machines, des voitures, des montres ou des appareils électroménagers. Le mouvement est souvent transféré directement d\'une roue dentée à l\'autre, mais parfois aussi via une chaîne. De plus, le sens de rotation peut être modifié. Il est également possible de changer un mouvement radial en un mouvement linéaire via un engrenage à crémaillère (<img alt="" src=images/FCGear_InvoluteRack.svg  style="width:22px;"> [FCGear Engrenage à crémaillère](FCGear_InvoluteRack/fr.md)).

![](images/Involute-Gear_example.png ) 
*De gauche à droite: Engrenage droit, engrenage hélicoïdal, engrenage double hélicoïdal*

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Lancez la commande d\'une de ces manières :
    -   Appuyez sur le bouton <img alt="" src=images/FCGear_InvoluteGear.svg  style="width:22px;"> [Create an Involute gear](FCGear_InvoluteGear/fr.md) dans la barre d\'outils.
    -   Utilisez **Gear Menu → Involute gear**.
3.  Modifiez le paramètre de démultiplication aux conditions requises (voir **Propriétés → Données** ci-dessous).

## Propriétés

### Données


{{Properties_Title|Base}}

-    **Placement**: [Placement](Placement/fr.md) est l\'emplacement et l\'orientation d\'un objet dans l\'espace.

-    **Label**: nom d\'utilisateur de l\'objet dans [vue en arborescence](Tree_view/fr.md).


{{Properties_Title|computed}}

(Toutes les propriétés de ce groupe sont calculées automatiquement et donc en lecture seule)

-    **da**: Diamètre extérieur, mesuré à l\'addendum (la pointe des dents).

-    **df**: Diamètre de la racine, mesuré au pied des dents.

-    **dw**: Diamètre du pas de travail.

-    **transverse_pitch**: Pas dans le plan de rotation.


{{Properties_Title|gear_parameter}}

-    **beta**: avec l\'angle d\'hélice β, un engrenage hélicoïdal est créé: valeur positive → sens de rotation à droite, valeur négative → sens de rotation à gauche (voir aussi les informations dans **Remarques**).

-    **clearance**: valeur par défaut est 0,25 (voir aussi les informations dans **Remarques**).

-    **double_gear**: {{Emphasis | True}} crée un engrenage à double hélice (voir aussi les informations dans **Remarques**).

-    **head**: valeur par défaut est 0,00. Cette valeur est utilisée pour modifier la hauteur des dents.

-    **height**: valeur de la largeur de l\'engrenage.

-    **module**: module est le rapport du diamètre de référence de l\'engrenage divisé par le nombre de dents (voir aussi les informations dans **Remarques**).

-    **properties_from_tool**: si l\'angle d\'hélice β est donné et que **properties_from-tool** est activé, les paramètres d\'engrenage sont recalculés en interne pour l\'engrenage tourné.

-    **shift**: valeur par défaut est 0,00, génère un décalage de profil positif et négatif (voir aussi les informations dans **Remarques**).

-    **teeth**: nombre de dents (voir aussi les informations dans **Remarques**).

-    **undercut**: **True** modifie le profil de la racine de la dent (voir aussi les informations dans **Remarques**).


{{Properties_Title|involute_parameter}}

-    **pressure_angle**: valeur par défaut 20° (voir aussi les informations dans les **Remarques**).


{{Properties_Title|precision}}

.

-    **numpoints**: La valeur par défaut est 6, changement du profil de la développante. Changer la valeur peut conduire à des résultats inattendus.

-    **simple**: **True** génère un affichage simplifié (sans dents et seulement un cylindre en diamètre primitif).


{{Properties_Title|tolerance}}

-    **backslash**: valeur par défaut est 0.00. Le contrecoup, également appelé claquement ou jeu, est la distance entre les dents d\'une paire d\'engrenages.

-    **reversed_backslash**: **True** diminution du jeu ou **False** augmentation du jeu (voir aussi les informations dans les **Remarques**).

### Vue

La description des paramètres de l\'onglet **View** se trouve dans l\'[Éditeur de propriétés](Property_editor/fr.md) dans **Exemple de propriétés d'un objet PartDesign**.

## Remarques

-    **beta**: lorsque **beta** est modifié, le **diamètre primitif** change également. La formule suivante illustre l\'interaction des paramètres: d = m \* Z / cos beta (Z = nombre de dents, d = diamètre primitif, m = module). Cela signifie pour l\'engrenage droit: cos beta = 0 et pour l\'engrenage hélicoïdal: cos beta\> 0. Cependant un angle d\'hélice inférieur à 10° n\'a guère d\'avantages par rapport aux dents droites.

-    **clearance**: sur une paire d\'engrenages, le jeu est la distance entre l\'extrémité de la dent du premier engrenage et la racine de la dent du deuxième engrenage.

-    **double_gear**: pour utiliser le double engrenage hélicoïdal, l\'angle d\'hélice β (**beta**) pour l\'engrenage hélicoïdal doit d\'abord être entré.

-    **module**: en utilisant les directives ISO (Organisation internationale de normalisation), la taille du module est désignée comme l\'unité représentant la taille des dents des engrenages. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Si vous multipliez Module par Pi, vous pouvez obtenir Pitch (p) (le pas). Le pas est la distance entre les points correspondants sur les dents adjacentes.

-    **shift**: le décalage de profil n\'est pas simplement utilisé pour empêcher la contre-dépouille. Il peut être utilisé pour régler la distance centrale entre deux vitesses. Si une correction positive est appliquée, de manière à éviter la contre-dépouille dans un pignon, l\'épaisseur de la dent en haut est plus fine.

-    **teeth**: Si le nombre de dents est modifié, le diamètre primitif change également (**dw**).

-    **undercut**: Undercut est utilisé lorsque le nombre de dents d\'un engrenage est trop petit. Dans le cas contraire, l\'accouplement coupera dans la racine de la dent. La contre-dépouille affaiblit non seulement la dent avec une taille de guêpe, mais supprime également une partie de la développante utile adjacente au cercle de base.

-    **pressure_angle**: 20° est une valeur standard ici. L\'angle de pression est défini comme l\'angle entre la ligne d\'action (tangente commune aux cercles de base) et une perpendiculaire à la ligne de centre. Ainsi, pour les engrenages standard, les engrenages à angle de pression de 14,5° ont des cercles de base beaucoup plus proches des racines des dents que les engrenages à 20°. C\'est pour cette raison que les engrenages de 14,5° rencontrent des problèmes de sous-coupe plus importants que les engrenages de 20°. Important. l\'angle de pression change avec un changement de profil. ne modifiez le paramètre que si une connaissance suffisante de la géométrie de l\'engrenage est disponible.

-    **reversed_backslash**: s\'il y a plusieurs vitesses, faites attention à la vitesse pour laquelle le paramètre est réglé.

## Formules utiles 

### Engrenages droits standards 

Le terme \"standard\" désigne ici les engrenages droits sans coefficient de décalage de profil ($x$).

+----------+-------------------------------------------------+----------------------------------------+---------------------------------------------+
| Symbole  | Terme                                           | Formule                                | Paramètre FCGear                            |
+==========+=================================================+========================================+=============================================+
| $m$      | *Module*                                        | \-                                     | $\texttt{module}$                           |
+----------+-------------------------------------------------+----------------------------------------+---------------------------------------------+
| $z$      | *Nombre de dents*                               | \-                                     | $\texttt{teeth}$                            |
+----------+-------------------------------------------------+----------------------------------------+---------------------------------------------+
| $\alpha$ | *Angle de pression*                             | \-                                     | $\texttt{pressure} {\_} \texttt{parameter}$ |
|          |                                                 | Typiquement, $\alpha = 20^\circ$       |                                             |
+----------+-------------------------------------------------+----------------------------------------+---------------------------------------------+
| d        | *Diamètre de référence* ou *Diamètre primitif*. | $z \cdot m$                            | \-                                          |
+----------+-------------------------------------------------+----------------------------------------+---------------------------------------------+
| $h^*_a$  | *Coefficient de l\'addendum*                    | \-                                     | $h^*_a = 1 + \texttt{ head}$                |
|          |                                                 | Typiquement, $h^*_a = 1$               |                                             |
+----------+-------------------------------------------------+----------------------------------------+---------------------------------------------+
| $h^*_f$  | *Dedendum Coefficient*                          | \-                                     | $h^*_f = 1 + \texttt{ clearance}$           |
|          |                                                 | Typiquement, $h^*_f = 1.25$            |                                             |
+----------+-------------------------------------------------+----------------------------------------+---------------------------------------------+
| $h_a$    | *Addendum*                                      | $h_a = h^*_a \cdot m$                  | \-                                          |
+----------+-------------------------------------------------+----------------------------------------+---------------------------------------------+
| $h_f$    | *Dedendum*                                      | $h_f = h^*_f \cdot m$                  | \-                                          |
+----------+-------------------------------------------------+----------------------------------------+---------------------------------------------+
| $h$      | *Hauteur des dents* or *Profondeur des dents*   | $h = h_a + h_f$                        | \-                                          |
|          |                                                 | Typically, $h = 2.25 \cdot m$          |                                             |
+----------+-------------------------------------------------+----------------------------------------+---------------------------------------------+
| $x$      | *Coefficient de décalage du profil*             | \-                                     | $\texttt{shift}$                            |
|          |                                                 | Pour les engrenages standards, $x = 0$ |                                             |
+----------+-------------------------------------------------+----------------------------------------+---------------------------------------------+

: style=\"text-align: left;\" \| Formules de base communes aux engrenages cylindriques standard internes et externes

+---------+---------------------------+----------------------------------------+
| Symbole | Terme                     | Formule                                |
+=========+===========================+========================================+
| $d_a$   | *Diamètre aux extrémités* | $d_a = d + 2 \cdot h_a$                |
|         |                           | Typiquement, $d_a = (z + 2) \cdot m$   |
+---------+---------------------------+----------------------------------------+
| $d_f$   | *Diamètre du coeur*       | $d_f = d - 2 \cdot h_f$                |
|         |                           | Typiquement, $d_f = (z - 2.5) \cdot m$ |
+---------+---------------------------+----------------------------------------+

: style=\"text-align: left;\" \| Formules de base spécifiques aux engrenages cylindriques externes standard

+---------+---------------------------+----------------------------------------+
| Symbole | Terme                     | Formule                                |
+=========+===========================+========================================+
| $d_a$   | *Diamètre aux extrémités* | $d_a = d - 2 \cdot h_a$                |
|         |                           | Typiquement, $d_a = (z - 2) \cdot m$   |
+---------+---------------------------+----------------------------------------+
| $d_f$   | *Diamètre du coeur*       | $d_f = d + 2 \cdot h_f$                |
|         |                           | Typiquement, $d_f = (z + 2.5) \cdot m$ |
+---------+---------------------------+----------------------------------------+

: style=\"text-align: left;\" \| Formules de base spécifiques aux engrenages cylindriques standard internes

+---------+---------------------------------+---------------------------------+
| Symbole | Terme                           | Formule                         |
+=========+=================================+=================================+
| $a$     | *Distance du centre*            | $d = \frac{d_1 + d_2}{2}$       |
+---------+---------------------------------+---------------------------------+
| $c$     | *Dégagement extrémité et coeur* | $c_1 = h_{f2} - h_{a1}$         |
|         |                                 | $c_2 = h_{f1} - h_{a2}$         |
|         |                                 | Typiquement, $c = 0.25 \cdot m$ |
+---------+---------------------------------+---------------------------------+

: style=\"text-align: left;\" \| Formules de base spécifiques à une paire d\'engrenages cylindriques standard externes

-   **Engrenage hélicoïdal et double hélice**
    -   
        **pitch diameter (dw)**
        
        = **module** \* **teeth** : **cos beta**

    -   
        **axle base**
        
        = **(pitch diameter (dw) 1 + 2)** : 2

    -   
        **addendum diameter**
        
        = **pitch diameter (dw)** + 2 \* **module**

    -   
        **module**
        
        = **pitch diameter (dw)** \* **cos beta** : **teeth**

## Script

Utilisez la puissance de Python pour automatiser la modélisation de votre engrenage: 
```python
import FreeCAD as App
import freecad.gears.commands
gear = freecad.gears.commands.CreateInvoluteGear.create()
gear.teeth = 20
gear.beta = 20
gear.height = 10
gear.double_helix = True
App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")
```




_ _ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > FCGear InvoluteGear/fr
