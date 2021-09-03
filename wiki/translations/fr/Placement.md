

## Description

**Placement** (positionnement en français) est la manière dont FreeCAD spécifie l\'emplacement et la position (orientation) d\'un objet dans l\'espace. Le placement peut être spécifié sous plusieurs formes et manipulé via un [script](Python_scripting_tutorial/fr#Vecteurs_et_placements.md), l\'[Éditeur de propriétés](Property_editor/fr.md) ou en sélectionnant **Edition → Positionnement...** pour ouvrir le [Panneau des tâches de placement](Std_Placement/fr.md).

### L\'accès aux propriétés de Placement 

Les attributs de la fonction Placement d\'un objet peuvent être accessibles et modifiables de 3 façons :

![Panneau de l\'éditeur de propriétés](images/PlacementPropertiesv10-800x800.png ) 

![Script Placement avec y/p/r sa Matrice et son [API](images/Placement_API/fr.md).](PlacePyConv10.png ) 

![Panneau des tâches de placement](images/PlacementDialogv10.png ) 

## Formes de Placement 

Le placement est stocké en interne comme une position, et une rotation (axe de rotation et l\'angle d\'inclinaison sont transformé en un [quaternion](https://fr.wikipedia.org/wiki/Quaternions_et_rotation_dans_l'espace)). Bien qu\'il existe plusieurs modes de spécifications pour une rotation, par exemple avec un centre de rotation. De même, si un axe de rotation (1,1,1) est spécifié, il est normalisé et stocké dans le quaternion et apparaissant comme (0,58, 0,58, 0,58).

### Angle, Axes et Position 

**Placement = \[Angle, Axis, Position\]**

**Placement** : fixe la position de l\'objet dans l\'espace et décrit son orientation avec rotation autour d\'un axe donné.

**Angle = r** : est un scalaire qui indique les angles de rotation de l\'objet sur l**\'axe donné**. La saisie se fait en degrés, mais en interne la valeur est convertie et stockée en radians.

**Axis = (ax,ay,az)** est un vecteur décrivant l\'axe de rotation (voir la note sur l\'axe de rotation). Les exemples sont:

   (1,0,0)       ==> sur l'axe **X**
   (0,1,0)       ==> sur l'axe **Y**
   (0,0,1)       ==> sur l'axe **Z**
   (0.71,0.71,0) ==> sur l'alignement **y=x**

Notez qu\'il est également possible de translater (déplacer) un objet le long de cet axe de rotation (mouvement axial) en entrant la distance à déplacer dans la boîte de sélection {{SpinBox|Axial: 0.0mm}} et en cliquant sur **Apply axial**. (Une façon d'envisager un mouvement axial consiste à penser à un avion avec une hélice en train de tourner sur son nez. L'hélice tourne autour d'un axe de rotation tandis que l'avion se déplace le long du même axe.) Les valeurs du vecteur peuvent être considérées comme la quantité relative de mouvement qui sera appliquée dans cette direction. Par exemple, dans le cas y = x (0.71,0.71,0), la valeur contenue dans le spinbox Axial est appliquée de la même manière aux directions X et Y, mais aucun mouvement ne se produit dans la direction Z.

**Position = (x,y,z)** est un vecteur décrivant le point à partir duquel la géométrie de l\'objet sera calculée (en fait, une \"origine locale\" de l\'objet). Notez que dans les scripts, Placement.Base est utilisé pour désigner le composant Position d\'un emplacement. L\'éditeur de propriétés appelle cette valeur **Position** et le panneau des tâches Placement l\'appelle **Translation**.

### Position avec Yaw, Pitch et Roll 

![Panneau des tâches de placement: {{ComboBox|Euler angles}} sélectionné](images/PlacementDialogv10b.png )  **Placement = \[Position, Yaw-Pitch-Roll\]**

La deuxième forme de **Placement** fixe l\'emplacement d\'un objet dans l\'espace avec une **Position** (comme dans la première forme), mais décrit son orientation en utilisant [Angles de lacet, de tangage et de roulis (Yaw, Pitch et Roll)](https://fr.wikipedia.org/wiki/Axes_de_rotation_d%27un_a%C3%A9ronef). Ces angles sont parfois appelés [angles d\'Euler](https://fr.wikipedia.org/wiki/Angles_d%27Euler) ou angles de Tait-Bryan. Yaw, Pitch and Roll sont des termes courants de l\'aviation pour l\'orientation (ou l\'attitude) d\'un corps.

**Position = (x,y,z)** est le Vecteur décrivant le point à partir duquel la géométrie de l\'objet sera calculée (\"l\'origine locale\" de l\'objet).

**Yaw-Pitch-Roll = (y,p,r)** est un tuple qui spécifie la rotation de l\'objet. Les valeurs de y, p, r indiquent les angles de rotation autour des axes z, y, et x (voir note).  
```python
>>> App.getDocument("Sans_nom").Cylinder.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(10,20,30), App.Vector(0,0,0))
```

App.Rotation(10,20,30) = Euler Angle

**Yaw** = 10 degrés (**Z**)

**Pitch** = 20 degrés (**Y**)

**Roll** = 30 degrés (**X**)

![](images/Tache_Placement_Lacet_fr_Mini.gif )**Yaw** est une rotation autour de l**\'axe Z**, rotation de gauche à droite sur l\'axe Z. (Lacet)
(L\'angle yaw est représenté par **Psi ψ**). 

![](images/Tache_Placement_Tangage_fr_Mini.gif )**Pitch** est la rotation sur l**\'axe Y**, cabré ou piqué. (Tangage)
(L\'angle Pitch est représenté par **Phi φ**). 

![](images/Tache_Placement_Roulis_fr_Mini.gif )**Roll** est la rotation sur l**\'axe X**, tangage latéral de gauche à droite. (Roulis)
(L\'angle Roll est représenté par **Thêta θ**). 

### Matrix

**Placement = Matrix**

La troisième forme de **Placement**, décrit la position de l\'objet et l\'orientation avec une matrice de transformation affine de 4 x 4 ([Transformation Affine](http://fr.wikipedia.org/w/index.php?title=Application_affine&action=submit)).

**Matrice** =

  ((r11,r12,r13,t1),
   (r21,r22,r23,t2),
   (r31,r32,r33,t3),
   (0,0,0,1)) , spécifie la rotation et la translation. 




## Boîte de dialogue Placement 

La boîte de dialogue placement est accessible par le menu **Edition**. Il est utilisé pour faire pivoter et positionner les objets avec précision. Il est également utilisé lorsque nous avons besoin de créer une esquisse sur un plan \"non standard\" ou changer l\'orientation d\'une esquisse dans un nouveau plan.

La section **Translation** déplace l\'objet dans l\'espace. La section **\'Center** permet d\'ajuster l\'axe de rotation qui ne passe pas par le point de référence de l\'objet. La section **Rotation** ajuste l\'angle(s) de rotation et la méthode de spécification de ces angles.

Toutefois, si les éléments de chaque section s'appliquent généralement à l'objet de cette section, certains éléments d'une section peuvent en affecter les éléments. Par exemple, si vous cliquez sur le bouton Points sélectionnés dans la section **Centre** avec 2 points sélectionnés dans la vue 3D, vous remplissez non seulement les boîtes de sélection \'\'\' Centre \'\'\' avec les coordonnées du point médian entre ces 2 points sélectionnés, mais crée également un axe personnalisé le long de la ligne définie par ces 2 points sélectionnés dans la section \'\' \'Rotation\' \'\'. Dans un autre exemple, placer une valeur dans le spinbox Axial et cliquer sur le bouton Appliquer axial dans la section **Translation** translate (déplace) l\'objet le long de l\'axe défini dans la section **Rotation**. La case à cocher **Appliquer des modifications incrémentielles au positionnement de l\'objet** est utile lorsque les translations / rotations doivent être effectuées par rapport à la position / attitude actuelle de l\'objet, plutôt qu\'à la position / attitude d\'origine. En cochant cette case, les champs de saisie du dialogue sont remis à zéro, mais l\'orientation de l\'objet et son emplacement ne sont pas modifiés. Les entrées suivantes modifient l\'orientation / l\'emplacement, mais sont appliquées à partir de la position actuelle de l\'objet. Activer cette case à cocher est également utile lorsque vous utilisez le bouton Points sélectionnés car cela peut parfois empêcher des modifications de placement indésirables.

PS: depuis la version 0.17 introduit un nouvel objet Part, cet objet a son emplacement et l'objet Placement créé dans l'objet Part est incrémenté du Placement. {{Version | 0.17}} Pour obtenir le placement de pièce, utilisez ce code 
```python
import Draft, Part
sel = FreeCADGui.Selection.getSelection()
print sel[0].Placement
print sel[0].getGlobalPlacement()   # return the GlobalPlacement
print sel[0].getParentGeoFeatureGroup() # return the GeoFeatureGroup, ex:  Body or a Part.
print  "____________________"
```

Le bouton **Points sélectionnés** est utilisé pour renseigner les repères dans les boîtes de sélection des coordonnées \'\'\' Centre \'\'\'et (lorsque 2 ou 3 points sont sélectionnés) pour créer en outre un axe de rotation personnalisé (défini par l\'utilisateur) la section **Rotation**. Un point peut être un sommet, mais il peut également s\'agir de n\'importe quel point le long d\'un bord ou d\'une face. Lorsque vous sélectionnez un bord ou une face, tout le bord ou la face est sélectionné, mais FreeCAD se souvient également du point sur cette face ou ce bord sur lequel le pointeur de la souris survolait lorsque cette arête ou cette face était sélectionnée. Ce sont les coordonnées de ce point qui sont utilisées dans la boîte de dialogue Placement lorsque vous cliquez sur le bouton **Points sélectionnés**. Vous pensez peut-être que ce n\'est pas une façon très précise de sélectionner un point et que vous avez raison, mais dans de nombreux cas, il suffit que le point sélectionné soit garanti sur ce bord ou cette face. Dans les cas où vous devez désigner précisément un point à utiliser, vous devez sélectionner un sommet. S\'il n\'y a pas de sommet à l\'emplacement souhaité, envisagez d\'en créer un, par exemple dans une esquisse temporaire attachée à cette face ou à ce bord, en utilisant éventuellement un objet Draft Workbench, tel qu\'une ligne ou un point, etc.

Considérons d'abord le cas simple de la sélection d'un point. Le flux de travail consiste d\'abord à sélectionner le point souhaité, puis à cliquer sur le bouton **Points sélectionnés**. Les coordonnées du point sélectionné seront utilisées pour renseigner les spinboxes X, Y et Z dans la section **Centre**. Désormais, toute rotation effectuée sur l\'objet concerne ce centre de rotation.

Considérons maintenant le cas de la sélection de 2 points. Vous sélectionneriez les 2 points souhaités, puis cliquez sur le bouton **Points sélectionnés**. Les coordonnées du point médian entre les 2 points sélectionnés sont placées dans les boîtes de défilement X, Y et Z dans la section **Centre**. Désormais, toute rotation effectuée sur l\'objet concerne ce centre de rotation. Mais en plus de la configuration de la section **Centre**, un axe personnalisé (défini par l\'utilisateur) est également ajouté à l\'élément **Axis** de la section **Rotation**. (Remarque: si vous étiez en mode de rotation Euler, le mode passe en rotation avec un mode axe et le nouvel axe personnalisé est sélectionné comme axe de rotation actuel.) Désormais, toute rotation effectuée à l\'aide du nouvel axe personnalisé correspond à cet axe. de rotation. En prime, la distance est mesurée entre les 2 points sélectionnés et cette information est donnée dans la vue Rapport. (Remarque: maintenez la touche Maj enfoncée tout en cliquant sur le bouton **Points sélectionnés** pour copier la mesure de distance dans le presse-papiers.) En saisissant cette distance dans le spinbox Axial de la section **Traduction**, le bouton **Appliquer axial** vous permet de translater (déplacer) l\'objet de sorte que le premier point sélectionné occupe maintenant les coordonnées occupées par le deuxième point sélectionné (au moment où le bouton **Points sélectionnés** a été cliqué).

Considérons maintenant le cas de la sélection de 3 points. Vous sélectionneriez les 3 points désirés, puis cliquez sur le bouton **Points sélectionnés**. Les coordonnées du premier point sélectionné (l\'ordre de sélection est très important ici) sont placées dans les boîtes de sélection X, Y et Z de la section **Center**. Depuis que 3 points définissent un plan, FreeCAD peut en tirer parti et utiliser ces 3 points pour créer un nouvel axe de rotation personnalisé (défini par l\'utilisateur) qui est normal (perpendiculaire) à ce plan défini. Comme avec 2 points sélectionnés, la distance entre les points est également affichée dans la vue Rapport, mais cette fois, il s'agit de la distance entre les 2e et 3e points sélectionnés. (Remarque: maintenez la touche Maj enfoncée tout en cliquant sur le bouton \'\' \'Points sélectionnés\' \'\' - Maj + clic - pour copier la mesure de l\'angle dans le presse-papiers.) De plus, l\'angle entre les deuxième et troisième points est également mesuré et affiché dans la vue du rapport. En entrant cet angle dans la zone de sélection **Angle** de la section \'\'\'\' Rotation \'\'\', nous pouvons faire pivoter l\'objet de manière très précise, de sorte que le deuxième point sélectionné est maintenant aligné sur les coordonnées occupées par le troisième point sélectionné. . (Remarque: vous voudrez peut-être augmenter le nombre de chiffres utilisés dans le menu Edition -\> Préférences -\> Général -\> Unités -\> Nombre de décimales (si vous souhaitez plus de précision).)

## Exemples

Rotations autour d\'un seul axe:

<img alt="Avant Rotation" src=images/RotationAboutZBefore.png  style="width:600px;"> Avant Rotation (top view) 

<img alt="Après Rotation sur l\'axe Z" src=images/RotationAboutZAfter.png  style="width:600px;"> Après Rotation sur l\'axe Z (top view) 

<img alt="Après Rotation sur l\'axe y=x" src=images/RotationAboutYXAfter.png  style="width:600px;"> Après Rotation sur l\'axe y=x (right view) 

Rotation avec point central décalé :

<img alt="Avant Rotation" src=images/RotationOffsetBefore.png  style="width:600px;"> Avant Rotation (top view) 

<img alt="After Rotation about Z" src=images/RotationOffsetAfter.png  style="width:600px;"> Après Rotation sur l\'axe Z (top view) 

Rotation en utilisant Euler angles:

<img alt="Before Rotation" src=images/RotationEulerBefore.png  style="width:600px;"> Avant Rotation 

<img alt="After Rotation" src=images/RotationEulerAfter.png  style="width:600px;"> Après Rotation 

## Placement.Base Définition d\'un shape 

La fonction placement n\'est pas le seul moyen de positionnement d\'une forme dans l\'espace. Notez la console Python dans cette image :

![2 Shapes avec le même Placement](images/2Placements800.png )

Les deux cubes ont la même valeur de Placement, mais sont à des emplacements différents ! C\'est parce que les 2 formes sont définies par des sommets différents (courbes et formes plus complexes). Pour les 2 formes dans l\'illustration ci-dessus :

 >>> ev = App.ActiveDocument.Extrude.Shape.Vertexes
 >>> for v in ev: print v.X,",",v.Y,",",v.Z
 ... 
 30.0,30.0,0.0
 30.0,30.0,10.0
 40.0,30.0,0.0
 40.0,30.0,10.0
 40.0,40.0,0.0
 40.0,40.0,10.0
 30.0,40.0,0.0
 30.0,40.0,10.0
 >>> e1v = App.ActiveDocument.Extrude001.Shape.Vertexes
 >>> for v in e1v: print v.X,",",v.Y,",",v.Z
 ... 
 0.0,10.0,0.0
 0.0,10.0,10.0
 10.0,10.0,0.0
 10.0,10.0,10.0
 10.0,0.0,0.0
 10.0,0.0,10.0
 0.0,0.0,0.0
 0.0,0.0,10.0
 >>> 
 

Les Vecteurs définissants le shape utilisent l\'attribut Placement.Base comme origine. Donc, si vous voulez déplacer une forme de 10 unités le long de l\'axe **X**, vous pouvez ajouter 10 à la coordonnées **X** de tous les sommets ou vous pouvez régler le Placement.Base à (10,0,0).

## Utiliser \"Center\" pour contrôler l\'Axe de Rotation 

Par défaut, l\'axe de rotation l\'axe x/y/z. C\'est une ligne parallèle à l\'axe sélectionné, passant par le point de référence (Placement.Base) de l\'objet qui doit être pivoté. Ceux ci peuvent être modifiés en utilisant les champs dans la boîte de dialogue Placement ou, dans les scripts, en utilisant le paramètre FreeCAD.Placement.

Par exemple, supposons que nous ayons un cube (ci-dessous) positionné aux coordonnées (20,20,10).

![Avant Rotation](images/LocalZBefore2.png ) Nous voulons faire tourner le cube autour de son axe vertical (c\'est à dire local Z), tout en gardant la même position. Nous pouvons facilement y parvenir en spécifiant une valeur de centre égale aux coordonnées du point central du cube (25,25,15). ![Après Rotation](images/LocalZAfter2.png )

Dans un script ,nous aurons : 
```python
import FreeCAD
obj = App.ActiveDocument.Box                       # our box
rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1),45)   # 45° about Z
#rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,1),45)   # 45° about X and 45° about Z
#rot = FreeCAD.Rotation(10,20,30)                   # here example with Euler angle Yaw = 10 degrees (Z), Pitch = 20 degrees (Y), Roll = 30 degrees (X) 
centre = FreeCAD.Vector(25,25,15)                  # central point of box 
pos = obj.Placement.Base                           # position point of box
newplace = FreeCAD.Placement(pos,rot,centre)       # make a new Placement object
obj.Placement = newplace                           # spin the box
``` Même script avec le fichier exemple [RotateCoG2.fcstd](http://forum.freecadweb.org/download/file.php?id=1651) (la discussion sur le [forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=3950#p31052)) 
```python
import FreeCAD
obj = App.ActiveDocument.Extrude                    # our box
rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1),45)    # 45 about Z
#rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,1),45)    # 45° about X and 45° about Z
#rot = FreeCAD.Rotation(10,20,30)                    # here example with Euler angle Yaw = 10 degrees (Z), Pitch = 20 degrees (Y), Roll = 30 degrees (X) 
centre = FreeCAD.Vector(25,25,0)                    # "centre" of rotation (where local Z cuts XY)
pos = obj.Placement.Base                            # original placement of obj
newplace = FreeCAD.Placement(pos,rot,centre)        # make a new Placement object
obj.Placement = newplace                            # spin the box
```

## Utilisation du placement dans les expressions 

Dans les expressions, il est possible d\'utiliser les composants du placement par exemple pour accéder au composant x de l\'objet nommé \"Cube\": 
```python
<<Cube>>.Placement.Base.x
```

Vous pouvez également utiliser tout le Placement dans une seule expression: Faites un clic droit sur la propriété Placement dans l\'éditeur de propriétés, sélectionnez \"show all\" puis des propriétés supplémentaires s\'afficheront. Si vous cliquez à nouveau avec le bouton droit sur Placement, le menu contextuel comprendra Expression, sélectionnez Expression puis la boîte de dialogue Expression s\'ouvrira et tout ce que vous tapez ira dans la propriété Placement plutôt que dans ses propriétés enfants.

Pour rendre le placement de \"Sketch\" égal à celui de \"Cylinder\", vous devez entrer de cette manière pour Sketch l\'expression 
```python
<<Cube>>.Placement
``` ![Définition du Placement entier dans une seule expression](images/PlacementInExpression.png )

## Remarques

-   Les propriétés de Placement de l\'onglet Données sont désactivées pour les objets qui sont attachés à un autre objet. Le décalage de rattachement doit être modifié à la place.
-   Axis et Angle peuvent également être exprimés en un [quaternion](http://fr.wikipedia.org/wiki/Quaternions_et_rotation_dans_l%27espace).
-   Le point de référence d\'un objet (FreeCAD.Placement.Base) varie en fonction de l\'objet. Quelques exemples d\'objets courants :

  Objet                                   Point de référence
  --------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Part.Box                                gauche (minx), face (miny), base (minz) vertex
  Part.Sphere                             centre de la sphère (centre de la limite du cube)
  Part.Cylinder                           centre de la base de la face
  Part.Cone                               centre de la base de la face (ou apex si le rayon de base du est 0)
  Part.Torus                              centre du tore
  Fonctionnalités dérivées d\'esquisses   la fonction hérite de la position de l\'esquisse sous-jacente. Les esquisses commencent toujours par Position = (0,0,0). Cette position correspond à l\'origine dans l\'esquisse.

## Limitations

-   Le placement relatif des objets sera éventuellement traité dans l\'atelier Assembly.

## En savoir plus 

-   Ce tutoriel : [Aéroplane](Aeroplane/fr.md) traite largement des mécanismes de modifications de position d\'un objet.



