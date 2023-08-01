---
- GuiCommand:/fr
   Name:FCGear InvoluteGear
   Name/fr:FCGear Engrenage à développante
   MenuLocation:Gear → Involute Gear
   Workbenches:[FCGear](FCGear_Workbench/fr.md)
   Shortcut:Aucun
   Version:v0.16
   SeeAlso:[FCGear Engrenage cycloïde](FCGear_CycloideGear/fr.md)
---

# FCGear InvoluteGear/fr

## Description

En raison du rapport d\'engrènement favorable et de la production relativement simple, l\'engrenage à développante est la forme de dent la plus courante en génie mécanique. Les roues dentées se trouvent partout où le mouvement et la force doivent être transférés d\'une pièce à l\'autre. Par exemple, ils peuvent être trouvés dans des machines, des voitures, des montres ou des appareils électroménagers. Le mouvement est souvent transféré directement d\'une roue dentée à l\'autre, mais parfois aussi via une chaîne. De plus, le sens de rotation peut être modifié. Il est également possible de changer un mouvement radial en un mouvement linéaire via un [FCGear Engrenage à crémaillère](FCGear_InvoluteRack/fr.md).

![](images/Involute-Gear_example.png ) 
*De gauche à droite: Engrenage droit, engrenage hélicoïdal, engrenage double hélicoïdal*

## Utilisation

1.  Passez à l\'<img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur **[<img src=images/FCGear_InvoluteGear.svg style="width:16px"> [Involute Gear](FCGear_InvoluteGear/fr.md)** dans la barre d\'outils.
    -   Sélectionnez l\'option **Gear → [<img src=images/FCGear_InvoluteGear.svg style="width:16px"> Involute Gear** dans le menu.
3.  Modifiez le paramètre de l\'engrenage en fonction des conditions requises (voir [Propriétés](#Propri.C3.A9t.C3.A9s.md)).

## Propriétés

Un objet FCGear InvoluteGear est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|accuracy}}

-    **numpoints|Integer**: valeur par défaut à {{Value|6}}. Changement du profil de la développante. La modification de la valeur peut conduire à des résultats inattendus.

-    **simple|Bool**: valeur par défaut à {{False}}. {{True}} génère un affichage simplifié (sans dents et seulement un cylindre en diamètre primitif).


{{Properties_Title|base}}

-    **height|Length**: valeur par défaut à {{Value|5 mm}}. Valeur de la largeur de l\'engrenage.

-    **module|Length**: valeur par défaut à {{Value|1 mm}}. Module est le rapport du diamètre de référence de l\'engrenage divisé par le nombre de dents (voir [Remarques](#Remarques.md)).

-    **teeth|Integer**: valeur par défaut à {{Value|15}}. Nombre de dents (voir [Remarques](#Remarques.md)).


{{Properties_Title|computed}}

-    **angular_backlash|Angle**: (lecture seule)

-    **da|Length**: (lecture seule) diamètre extérieur, mesuré à l\'addendum (la pointe des dents).

-    **df|Length**: (lecture seule) diamètre de la racine, mesuré au pied des dents.

-    **dw|Length**: (lecture seule) diamètre du pas de travail.

-    **transverse_pitch|Length**: (lecture seule) pas dans le plan de rotation.


{{Properties_Title|fillets}}

-    **head_fillet|Float**: valeur par défaut à {{Value|0 mm}}.

-    **root_fillet|Float**: valeur par défaut à {{Value|0 mm}}.

-    **undercut|Bool**: valeur par défaut à {{False}}. {{True}} modifie le profil de la racine de la dent (voir [Remarques](#Remarques.md)).


{{Properties_Title|helical}}

-    **beta|Angle**: valeur par défaut à {{Value|0 °}}. Avec l\'angle d\'hélice β, un engrenage hélicoïdal est créé - valeur positive → sens de rotation à droite, valeur négative → sens de rotation à gauche (voir [Remarques](#Remarques.md)).

-    **double_helix|Bool**: valeur par défaut à {{False}}, {{True}} crée un engrenage à double hélice (voir [Remarques](#Remarques.md)).

-    **properties_from_tool|Bool**: valeur par défaut à {{False}}. Si {{True}} et **beta** est différent de zéro, les paramètres de l\'engrenage sont recalculés en interne pour l\'engrenage tourné.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: valeur par défaut à {{Value|20 °}} (voir [Remarques](#Remarques.md)).

-    **shift|Float**: valeur par défaut à {{Value|0}}. Génère un décalage de profil positif et négatif (voir [Remarques](#Remarques.md)).


{{Properties_Title|tolerance}}

-    **backlash|Length**: valeur par défaut à {{Value|0}}. Le jeu, également appelé lash ou play, est la distance entre les dents d\'une paire d\'engrenages.

-    **clearance|Float**: valeur par défaut à {{Value|0.25}} (voir [Remarques](#Remarques.md)).

-    **head|Float**: valeur par défaut à {{Value|0}}. Cette valeur est utilisée pour modifier la hauteur de la dent.

-    **reversed_backlash|Bool**: {{True}} diminution du jeu, {{False}} (valeur par défaut) augmentation du jeu. (voir [Remarques](#Remarques.md)).


{{Properties_Title|version}}

-    **version|String**:

## Remarques

-    **beta**: lorsque **beta** est modifié, le **diamètre primitif** change également. La formule suivante illustre l\'interaction des paramètres: d = m \* Z / cos beta (Z = nombre de dents, d = diamètre primitif, m = module). Cela signifie pour l\'engrenage droit: cos beta = 0 et pour l\'engrenage hélicoïdal: cos beta\> 0. Cependant un angle d\'hélice inférieur à 10° n\'a guère d\'avantages par rapport aux dents droites.

-    **clearance**: sur une paire d\'engrenages, le jeu est la distance entre l\'extrémité de la dent du premier engrenage et la racine de la dent du deuxième engrenage.

-    **double_gear**: pour utiliser le double engrenage hélicoïdal, l\'angle d\'hélice β (**beta**) pour l\'engrenage hélicoïdal doit d\'abord être entré.

-    **module**: en utilisant les directives ISO (Organisation internationale de normalisation), la taille du module est désignée comme l\'unité représentant la taille des dents des engrenages. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Si vous multipliez Module par Pi, vous pouvez obtenir Pitch (p) (le pas). Le pas est la distance entre les points correspondants sur les dents adjacentes.

-    **shift**: le décalage de profil n\'est pas simplement utilisé pour empêcher la contre-dépouille. Il peut être utilisé pour régler la distance centrale entre deux vitesses. Si une correction positive est appliquée, de manière à éviter la contre-dépouille dans un pignon, l\'épaisseur de la dent en haut est plus fine.

-    **teeth**: si le nombre de dents est modifié, le diamètre primitif change également (**dw**).

-    **undercut**: undercut est utilisé lorsque le nombre de dents d\'un engrenage est trop petit. Dans le cas contraire, l\'accouplement coupera dans la racine de la dent. La contre-dépouille affaiblit non seulement la dent avec une taille de guêpe, mais supprime également une partie de la développante utile adjacente au cercle de base.

-    **pressure_angle**: 20° est une valeur standard ici. L\'angle de pression est défini comme l\'angle entre la ligne d\'action (tangente commune aux cercles de base) et une perpendiculaire à la ligne de centre. Ainsi, pour les engrenages standard, les engrenages à angle de pression de 14,5° ont des cercles de base beaucoup plus proches des racines des dents que les engrenages à 20°. C\'est pour cette raison que les engrenages de 14,5° rencontrent des problèmes de sous-coupe plus importants que les engrenages de 20°. Important. l\'angle de pression change avec un changement de profil. ne modifiez le paramètre que si une connaissance suffisante de la géométrie de l\'engrenage est disponible.

-    **reversed_backlash**: s\'il y a plusieurs vitesses, faites attention à la vitesse pour laquelle le paramètre est réglé.

## Limitations

Un profil de dent en 2D, obtenu en fixant la valeur de **height** à zéro, ne peut pas être utilisé avec des caractéristiques nécessitant une forme en 2D. Par exemple, les fonctions [PartDesign Protrusion](PartDesign_Pad/fr.md) et [PartDesign Hélice additive](PartDesign_AdditiveHelix/fr.md) n\'acceptent pas un tel profil comme base. Pour les détails techniques, veuillez vous reporter à la question connexe [issue on GitHub](https://github.com/looooo/freecad.gears/issues/97).

## Formules utiles 

### Engrenages droits standards 

Le terme \"standard\" désigne ici les engrenages droits sans coefficient de décalage de profil ($x$).

+++++
| Symbole  | Terme                                           | Formule                                | Paramètre FCGear                            |
+==========+=================================================+========================================+=============================================+
| $m$      | *Module*                                        | \-                                     | $\texttt{module}$                           |
+++++
| $z$      | *Nombre de dents*                               | \-                                     | $\texttt{teeth}$                            |
+++++
| $\alpha$ | *Angle de pression*                             | \-                                     | $\texttt{pressure} {\_} \texttt{parameter}$ |
|          |                                                 | Typiquement, $\alpha = 20^\circ$       |                                             |
+++++
| d        | *Diamètre de référence* ou *Diamètre primitif*. | $z \cdot m$                            | \-                                          |
+++++
| $h^*_a$  | *Coefficient de l\'addendum*                    | \-                                     | $h^*_a = 1 + \texttt{ head}$                |
|          |                                                 | Typiquement, $h^*_a = 1$               |                                             |
+++++
| $h^*_f$  | *Coefficient du dedendum*                       | \-                                     | $h^*_f = 1 + \texttt{ clearance}$           |
|          |                                                 | Typiquement, $h^*_f = 1.25$            |                                             |
+++++
| $h_a$    | *Addendum*                                      | $h_a = h^*_a \cdot m$                  | \-                                          |
+++++
| $h_f$    | *Dedendum*                                      | $h_f = h^*_f \cdot m$                  | \-                                          |
+++++
| $h$      | *Hauteur des dents* or *Profondeur des dents*   | $h = h_a + h_f$                        | \-                                          |
|          |                                                 | Typically, $h = 2.25 \cdot m$          |                                             |
+++++
| $x$      | *Coefficient de décalage du profil*             | \-                                     | $\texttt{shift}$                            |
|          |                                                 | Pour les engrenages standards, $x = 0$ |                                             |
+++++

: style=\"text-align: left;\" \| Formules de base communes aux engrenages cylindriques standard internes et externes

++++
| Symbole | Terme                 | Formule                                |
+=========+=======================+========================================+
| $d_a$   | *Diamètre de la tête* | $d_a = d + 2 \cdot h_a$                |
|         |                       | Typiquement, $d_a = (z + 2) \cdot m$   |
++++
| $d_f$   | *Diamètre de base*    | $d_f = d - 2 \cdot h_f$                |
|         |                       | Typiquement, $d_f = (z - 2.5) \cdot m$ |
++++

: style=\"text-align: left;\" \| Formules de base spécifiques aux engrenages cylindriques externes standard

++++
| Symbole | Terme                 | Formule                                |
+=========+=======================+========================================+
| $d_a$   | *Diamètre de la tête* | $d_a = d - 2 \cdot h_a$                |
|         |                       | Typiquement, $d_a = (z - 2) \cdot m$   |
++++
| $d_f$   | *Diamètre de base*    | $d_f = d + 2 \cdot h_f$                |
|         |                       | Typiquement, $d_f = (z + 2.5) \cdot m$ |
++++

: style=\"text-align: left;\" \| Formules de base spécifiques aux engrenages cylindriques standard internes

++++
| Symbole | Terme                                 | Formule                         |
+=========+=======================================+=================================+
| $a$     | *Distance entre centres*              | $d = \frac{d_1 + d_2}{2}$       |
++++
| $c$     | *Dégagement de la tête et de la base* | $c_1 = h_{f2} - h_{a1}$         |
|         |                                       | $c_2 = h_{f1} - h_{a2}$         |
|         |                                       | Typiquement, $c = 0.25 \cdot m$ |
++++

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



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear InvoluteGear/fr
