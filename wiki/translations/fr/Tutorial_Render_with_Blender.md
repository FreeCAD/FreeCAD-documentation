---
- TutorialInfo   */fr
   Topic   *Rendering
   Level   *Intermédiaire
   Time   *60 minutes
   Author   *[https   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=21943 vocx]
   FCVersion   *0.18 ou ultérieure
   Files   *none
---

# Tutorial Render with Blender/fr





## Introduction

Ce tutoriel montre comment produire une image rendue dans [Blender](https   *//www.blender.org/), à partir d\'une pièce ou d\'un assemblage créé avec FreeCAD. Il suppose que l\'utilisateur a déjà créé la pièce dans FreeCAD, ou l\'a importée dedans. Ensuite, cette partie est exportée vers Blender pour le rendu.

Il produit un rendu avec Blender 2.80 avec les moteurs de rendu EEVEE et Cycles. Il montre diverses commandes [Python](Python/fr.md) qui peuvent être utilisées pour effectuer des actions plus rapidement à la fois dans FreeCAD et Blender.

Une description similaire de ce processus est décrite dans une série de vidéos, [Render Solidworks and FreeCAD Models in Blender](https   *//www.youtube.com/watch?v=U7e6-Wfv2b0) par Joko Engineering.

## FreeCAD

1\. Créez un assemblage en utilisant des corps de l\'[atelier Part](Part_Workbench/fr.md) ou [atelier PartDesign](PartDesign_Workbench/fr.md), ou de tout autre atelier produisant des objets solides, par exemple, l\'[atelier Arch](Arch_Workbench/fr.md). Attribuez des couleurs ou des matériaux aux corps individuels qui composent l\'assemblage, en correspondant approximativement à la couleur souhaitée dans votre rendu.

<img alt="" src=images/01_T03_FreeCAD_Blender_model.png  style="width   *600px;">



*align=center|Assemblage de trois corps créés dans FreeCAD avec des couleurs ou des matériaux choisis.*

2\. Si votre modèle est très détaillé, assurez-vous que la valeur {{PropertyView/fr|Deviation}} du corps est défini sur une valeur basse comprise entre `0.1` et `00.1` voire moins. Plus cette valeur est basse, plus le maillage exporté sera détaillé et donc meilleure sera la qualité du rendu.

![](images/02_T03_FreeCAD_Blender_deviation.png )



*align=center|Propriété de déviation des corps créés dans FreeCAD. L'écart doit être faible pour pouvoir exporter les pièces avec une bonne résolution.*

3\. Sélectionnez `Part`, puis **Fichier → Exporter**, ou appuyez sur **Ctrl** + **E**, et exportez-le sous `Wavefront OBJ`.

Alternativement, l\'exportation peut être effectuée depuis la console [Python](Python/fr.md). Définissez une liste d\'objets à exporter et utilisez la fonction d\'exportation avec un nom de fichier.


```python
import importOBJ
objs = FreeCAD.ActiveDocument.getObjectsByLabel("Part")[0]

importOBJ.export(objs, "/home/user/assembly.obj")
```


**Remarque   ***

lors de l\'exportation vers OBJ, deux fichiers sont créés; le premier contient les informations du maillage lui-même, `assembly.obj`; le second contient la définition des matériaux, qui dans la plupart des cas est juste la couleur, `assembly.mtl`.


**Remarque 2   ***

si le fichier OBJ résultant semble vide, vous devrez peut-être exporter les corps individuels. Dans ce cas, sélectionnez chacun des corps sous la pièce et répétez l\'exportation.


```python
import importOBJ
objs = [FreeCAD.ActiveDocument.getObjectsByLabel("Body.base")[0],
FreeCAD.ActiveDocument.getObjectsByLabel("Body.bolt")[0],
FreeCAD.ActiveDocument.getObjectsByLabel("Body.bolt.big")[0]]

importOBJ.export(objs, "/home/user/assembly.obj")
```

## Blender

### Préparez le modèle 

4\. Ouvrez Blender. Changez le panneau `Timeline` dans une `console Python` (**Shift**+**F4**). Cela vous aidera à saisir des commandes et à voir les résultats. Vous pouvez diviser ce panneau, pour garder la console d\'un côté, et faire de l\'autre division un panneau `Info`; cela vous permettra de voir le code des actions en cliquant sur l\'interface.

Assurez-vous que vous utilisez le moteur de rendu EEVEE. Dans le panneau `Properties`, allez dans `Render`, et pour `Render Engine` sélectionnez `Eevee`.


```python
bpy.context.scene.render.engine = 'BLENDER_EEVEE'
```

5\. Importez le fichier de modèle à partir du menu, **Fichier → Importer → Wavefront (.obj)**.

Alternativement, l\'importation peut être effectuée à partir de la `console Python`.


```python
obj_file = "/home/user/assembly.obj"
bpy.ops.import_scene.obj(filepath=obj_file)
```

6\. Modifiez l\'échelle.

Si les corps semblent très grands, vous devrez peut-être changer les unités pour que les objets apparaissent à la bonne échelle.

Dans le panneau `Properties`, allez dans `Scene`, `Units`, et sélectionnez le `Unit System`, `Unit Scale`, et `Length`.

Pour les petites pièces, vous pouvez conserver la longueur à `Millimeters` et l\'échelle à `0.001`. Pour les pièces plus volumineuses, par exemple le modèle d\'un bâtiment, vous devrez peut-être définir ces valeurs sur `Meters` et `0.001`. Essayez d\'autres valeurs d\'échelle si nécessaire.

Cela peut également être défini depuis la `console Python`.


```python
bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'
# or bpy.context.scene.unit_settings.length_unit = 'METERS'
bpy.context.scene.unit_settings.scale_length = 0.001
```


**Remarque   ***

changer l\'échelle et les unités de la scène n\'est nécessaire que si vous souhaitez travailler avec des objets à leurs dimensions réelles. Si vous souhaitez simplement rendre votre scène rapidement, vous pouvez omettre tout ajustement.

6.1. Si vous effectuez un zoom arrière et que la vue coupe les pièces importées, vous devrez peut-être ajuster les valeurs des vignettes de la vue.

Appuyez sur **N** pour afficher le panneau auxiliaire; Accédez à la section `View` et définissez `End` sur une valeur élevée, par exemple `1E6 mm` ou `1000 m`.

6.2. Si vous le souhaitez, ajustez également la taille de la grille; allez à `Overlays`, puis `Guides`, et définissez `Scale` de la grille sur `0.001`.

7\. Réglez la rotation des objets.

Une fois importés, les objets peuvent apparaître pivotés autour de l\'un des axes, par exemple à 90 degrés autour de l\'axe X. Appuyez sur **N** pour afficher le panneau auxiliaire; sélectionnez un objet, accédez à la section `Transform` et définissez `Rotation` sur `0°` dans chaque champ. Faites ceci pour chaque objet.

Cela peut être automatisé par un petit script qui définit simplement la rotation de chaque corps importé à zéro, à l\'exception des objets à l\'intérieur du tuple `fixed_objs`. Cela peut être utile si vous importez des objets dans une scène existante où d\'autres objets sont déjà dans leurs bonnes positions.


```python
fixed_objs = ('Camera', 'Cube', 'Light')

for obj in bpy.data.objects   *
    if any(s for s in fixed_objs if s in obj.name)   *
        print('%s %s  [[No change]]' % (obj.name, obj.rotation_euler))
        continue
    else   *
        obj.rotation_euler = (0, 0, 0)
        print('%s %s  ... rotated' % (obj.name, obj.rotation_euler))
```

![](images/03_T03_FreeCAD_Blender_imported_assembly.png )



*align=center|Assemblage créé dans FreeCAD importé dans Blender; le modèle a été tourné et les unités de la scène ont été ajustées pour correspondre aux objets importés.*

### Préparez la caméra de la scène 

8\. Réglez la caméra dans la bonne position.

Ajustez la fenêtre pour regarder le modèle dans l\'orientation souhaitée, puis appuyez sur **Ctrl**+**Alt**+**0** (pavé numérique), ou utilisez le menu **Affichage → Aligner la vue → Aligner la caméra active sur la vue**.

8.1. Si vous ne voyez rien dans la vue de la caméra, vous devrez peut-être ajuster le découpage. En sélectionnant la caméra dans `Outliner`, allez dans le panneau `Properties`, puis `Object Data`, puis `Lens`, puis définissez `Clip End` à une valeur élevée, par exemple `1E3 mm` ou `1000 m`.


```python
bpy.context.object.data.clip_end = 1e+03
```

Si vous pouvez voir l\'objet à travers la vue de la caméra, vous pouvez maintenant rendre rapidement le modèle en appuyant sur **F12**, ce qui ouvrira `Image Editor` avec le résultat. Appuyez sur **Echap** pour quitter et revenir à `3D Viewport`.

<img alt="" src=images/04_T03_FreeCAD_Blender_first_render.png  style="width   *600px;">



*align=center|Premier rendu de l'assemblage dans Blender, avec la caméra avec un découpage correct mais sans éclairage*

Vous pouvez basculer entre la vue caméra et la fenêtre 3D en appuyant sur **0** dans le pavé numérique; appuyer sur **F12** rendra la vue de la caméra à tout moment.

8.2. Si la caméra semble très petite dans la fenêtre 3D, allez dans le panneau `Properties`, puis `Object Data`, puis `Viewport Display`, et définissez une valeur plus grande pour le `Size`, par exemple, `20 mm`. Cochez également la case `Limits` pour voir la distance de coupure de la caméra.


```python
bpy.context.object.data.display_size = 20
bpy.context.object.data.show_limits = True
```

### Préparez la caméra de la scène 

9\. Sélectionnez la lumière dans `Outliner`, allez dans le panneau `Properties`, puis `Object Data`, puis appuyez sur `Sun`, et réglez le `Strength` à `5.0`.


```python
bpy.context.object.data.type = 'SUN'
bpy.context.object.data.energy = 5
```

Cela transformera la lumière en une lampe solaire. Ce type de lampe émet un nombre infini de rayons lumineux parallèles qui arrivent tous sur la scène avec un angle fixe.

Vous pouvez positionner la lampe solaire n\'importe où dans la fenêtre au-dessus de votre modèle afin de définir la direction des rayons de lumière. Pour une lampe solaire, peu importe à quelle distance ou près vous placez la lampe, seulement la direction des rayons, qui est définie par la rotation de l\'objet `Light`.


```python
bpy.context.active_object.location = (150, 100, 100)
bpy.context.active_object.rotation_euler = (0.6, 0.05, 1.88)
```

Appuyez à nouveau sur **F12** pour voir un rendu préliminaire du modèle.

<img alt="" src=images/05_T03_FreeCAD_Blender_render_sun_lamp.png  style="width   *600px;">



*align=center|Rendu de l'assemblage dans Blender avec une lampe solaire ajoutée qui émet des rayons lumineux parallèles avec un angle fixe*

### Plus de configuration   * sol, éclairage global, reflets et ombres douces 

10\. Ajoutez un plan d\'étage. Appuyez sur **Shift**+**A** puis choisissez `Mesh`, `Plane`, et donnez-lui des dimensions environ 10 fois plus grandes que votre modèle. Cet objet maillé servira de plan de sol ou de dessus de table sur lequel le modèle se trouve. Déplacez également le plan un peu vers le bas afin qu\'il n\'intersecte pas le modèle; `-1 mm` sous l\'objet suffit.


```python
bpy.ops.mesh.primitive_plane_add(size=1500, view_align=False, enter_editmode=False, location=(0, 0, -1))
```

11\. Réglez l\'illumination de l\'environnement. Dans le panneau `Properties`, accédez à `World` et définissez `Color` sur une valeur bleu-gris clair, `RGB (0.358, 0.512, 0.527)} } et définissez {{incode|Strength` sur `0.3`.

12. Définissez les reflets et les ombres. Le moteur de rendu EEVEE de Blender produit des rendus rapides en désactivant la plupart des effets au départ. Afin d'obtenir de meilleures images, certaines options doivent être activées.

Allez dans le panneau `Properties`, puis `Render` et cochez `Screen Space Reflections`. Dans la section `Shadows`, cochez également `Soft Shadows`.

```python
bpy.context.scene.eevee.use_ssr = True
bpy.context.scene.eevee.use_soft_shadows = True
```

=== Définir les matériaux des objets ===

13. Transformez le panneau `Python Console` en un panneau `Shader Editor` (**Shift**+**F3**).

13.1. Sélectionnez le plan de masse, allez dans le panneau `Properties`, puis `Material`, et cliquez sur `New`. Dans `Shader Editor` un nœud `Principled BSDF` devrait apparaître. Donnez-lui une Couleur de base `Base Color` `RGB (0.318, 0.267, 0.187)`, tournez le curseur `Metallic` sur `0.000`, et la Rugosité {{ incode|Roughness}} à `1.000`.

![](images/06_T03_FreeCAD_Blender_Principled_shader.png )



*align=center|le Principled BSDF shader utilisé dans Blender pour simuler une variété de matériaux allant des métaux brillants aux solides rugueux et opaques.*

13.2. Sélectionnez chacune des parties du modèle et ajustez le nœud de matériau `Principled BSDF` respectif. Pour les pièces métalliques, placez la propriété `Metallic` à fond sur `1.000`. Ajustez la valeur de `Roughness` entre `0.2` et `0.7`. Plus le `0.000` est proche de `Roughness`, plus il apparaîtra réfléchissant (semblable à un miroir).

Pour les non-métaux, comme les plastiques, le bois et les textiles, placez le curseur `Metallic` à fond sur `0.000`, et ajustez la valeur de `Roughness` entre `0.4` et `1.0`.

En général, les métaux sont naturellement lisses et donc leur valeur de rugosité est faible, ce qui les rend très réfléchissants (brillants). D\'autres matériaux sont microscopiquement rugueux et ne réfléchissent donc pas autant de lumière, ce qui les rend opaques.

14\. Testez différentes combinaisons de matériaux jusqu\'à ce qu\'elles semblent acceptables. Appuyez sur **Z** puis sur **8** (pavé numérique) pour passer en mode `Rendered`; dans ce mode, le moteur de rendu EEVEE montre en temps réel dans la fenêtre 3D à quoi ressemblera l\'image finale. Utilisez **Z** pour ouvrir le menu à secteurs et revenir en mode `Solid` (**Z** **6**), ou accédez à `LookDev` mode (**Z** **2**), un mode qui ajoute différents types d\'éclairage à la scène pour tester l\'apparence des matériaux.

Appuyez sur **F12** pour rendre la vue à travers la caméra et vérifier la qualité de l\'image.

### Rendu et sauvegarde 

15\. Si votre modèle semble raisonnablement bien avec le moteur de rendu EEVEE, vous pouvez déjà enregistrer l\'image en allant dans **Image → Enregistrer sous** ou en appuyant sur **Shift**+**S** dans le {{Incode|Image Editor}}.

<img alt="" src=images/07_T03_FreeCAD_Blender_EEVEE_render.png  style="width   *600px;">



*align=center|Assemblage rendu produit avec Blender EEVEE; tous les matériaux utilisent le shader BSDF Principled; une seule lampe solaire est utilisée, avec un peu de lumière ambiante.*

16\. Si vous souhaitez améliorer la qualité de l\'image, essayez le moteur de rendu Cycles.

Allez dans le panneau `Properties`, puis `Render`, et pour `Render Engine` sélectionnez `Cycles`. Avec le moteur de rendu Cycles, Blender affine l\'image progressivement jusqu\'à ce qu\'un certain nombre d\'itérations se soient écoulées. Chaque fois que la fenêtre change, le recalcul redémarre.


```python
bpy.context.scene.render.engine = 'CYCLES'
```

16.1. Ajustez la fréquence d\'échantillonnage. Allez dans le panneau `Properties`, puis `Render`, puis dans la section `Sampling` sélectionnez un nombre approprié pour `Render` et `Viewport`.

Pour le `Viewport`, un petit nombre d\'échantillons, compris entre `32` et `128`, suffit généralement pour obtenir un bon aperçu de l\'image. Pour l\'image finale, définissez `Render` sur un nombre plus élevé, de `128` à `2000`, selon la complexité et la quantité de détails sur la scène.

Appuyez sur **F12** pour rendre la vue finale à travers la caméra. Selon votre carte graphique (GPU), le rendu de l\'image devrait prendre plusieurs secondes, ou minutes, avec Cycles qu\'avec EEVEE, mais la qualité de l\'image devrait être meilleure.

17\. Lorsque vous êtes satisfait de la qualité du rendu, dans `Image Editor` allez dans **Image → Enregistrer sous** ou appuyez sur **Shift**+**S**.

<img alt="" src=images/08_T03_FreeCAD_Blender_Cycles_render.png  style="width   *600px;">



*align=center|Assemblage rendu produit avec Blender Cycles; toutes les options, matériaux et lumières utilisés avec EEVEE ont été conservés pour être utilisés avec Cycles.*

### Rendu depuis la ligne de commande 

18\. Si la scène est complètement terminée, vous souhaiterez peut-être effectuer le rendu depuis l\'extérieur de Blender, depuis la ligne de commande du système d\'exploitation. Cela peut être utile pour effectuer le rendu par lots de différentes scènes dans un système distant. EEVEE et Cycles sont pris en charge.


{{Code|lang=sh|code=
blender -b assembly.blend -E BLENDER_EEVEE -o //assembly_EEVEE_#### -t 3 -F PNG -x 1 -f 1
}}


{{Code|lang=sh|code=
blender -b assembly.blend -E CYCLES -o //assembly_CYCLES_#### -t 3 -F PNG -x 1 -f 1
}}

Ceci spécifie que le rendu doit avoir lieu en arrière-plan avec `-b`; le moteur de rendu est choisi avec `-E`; le nom du fichier de sortie est sélectionné avec `-o`; la double barre oblique `//` indique un chemin relatif au fichier d\'entrée; le signe dièse `#` est utilisé pour indiquer le numéro de la trame, complété avec des zéros si nécessaire, par exemple, `0001`; le nombre de threads CPU utilisés dans le rendu est choisi avec `-t 3`; le format du fichier de sortie est indiqué par `-F`, et l\'option `-x 1` ajoute automatiquement l\'extension au nom; la dernière option est `-f 1` qui indique que seule la première image sera rendue, ce qui est le cas normal pour une scène statique; pour les animations, utilisez le commutateur `-a` pour produire une image pour chaque image, qui peut ensuite être assemblée pour produire un fichier vidéo.

## Importation du plugin 

La création du maillage Wavefront intermédiaire (.obj) puis son importation dans Blender fonctionnera dans la plupart des situations. Cependant, il existe également la possibilité d\'importer le fichier FreeCAD (.FCStd) directement dans Blender au moyen d\'un plugin.

-   [io\_import\_fcstd.py](https   *//gist.github.com/yorikvanhavre/e873d51c8f0e307e333fe595c429ba87), version originale pour Blender 2.79
-   [Importateur FreeCAD .FCStd pour Blender 2.80](https   *//gist.github.com/yorikvanhavre/680156f59e2b42df8f5f5391cae2660b)

Ceci est un plugin Blender; pour que cela fonctionne, Blender doit pouvoir importer FreeCAD en tant que module depuis la `Python Console`. 
```python
import FreeCAD
```

Ceci n\'est possible que si Blender et FreeCAD sont compilés avec la même version `pythonX.Y` (majeure et mineure). Par exemple, si Blender est compilé avec Python 3.7, FreeCAD doit également être compilé avec une version Python 3.7. Si FreeCAD est compilé avec une autre version, par exemple Python 2.7.15 ou Python 3.6.7, le plugin ne fonctionnera pas. Le numéro de version micro (troisième numéro) n\'a pas d\'importance, c\'est-à-dire que le plugin devrait fonctionner si un logiciel est compilé avec Python 3.7.5 et l\'autre avec Python 3.7.8.

De plus, le module Python précompilé FreeCAD, `FreeCAD.so` sous Linux et `FreeCAD.pyd` sous Windows, doit être dans le chemin Python utilisé par Blender pour importer des modules. Ce chemin peut être configuré de différentes manières, en fonction du système d\'exploitation et de la distribution Python.

Dans Blender, vous pouvez voir tous les chemins recherchés en inspectant la variable `sys.path`. Le module FreeCAD doit être trouvé dans l\'un de ces répertoires. 
```python
import sys
print(sys.path)```

-   Une copie ou un lien symbolique dans l\'un de ces répertoires pourrait être créé pointant vers le module FreeCAD.


```python
ln -s /usr/lib/freecad/lib/FreeCAD.so $HOME/.config/blender/2.80/scripts/addons

ln -s /usr/lib/freecad/lib/FreeCAD.so $HOME/.local/lib/python3.7/site-packages
```

-   Une autre possibilité est d\'ajouter le module directement dans le chemin à l\'intérieur de Blender.


```python
import sys
sys.path.append("/usr/lib/freecad/lib/FreeCAD.so")
```

## Remarques finales 

EEVEE n\'est pas un moteur de rendu physiquement précis, mais sa principale force est qu\'il s\'agit d\'un moteur en temps réel, ce qui lui permet de produire des rendus rapides directement dans la fenêtre 3D. Dans de nombreux cas, ces images ont une qualité suffisante pour la production finale, ce qui signifie qu\'il est possible d\'obtenir un bon résultat en très peu de temps. Dans les cas où des interactions lumineuses complexes sont souhaitées (réflexions, réfractions, lumière volumétrique et caustiques), EEVEE est plus limité et nécessite certaines options et astuces pour contourner certaines de ces limitations.

D\'autre part, Cycles est un véritable moteur de rendu par lancer de rayons, ce qui signifie qu\'il est plus précis pour calculer les trajets de lumière dans une scène. Cycles est le rendu recommandé lorsque la meilleure qualité est souhaitée (résultats photoréalistes), au prix d\'un temps de rendu plus long.

Les deux moteurs de rendu peuvent être utilisés pour tirer parti des avantages de chacun. Dans de nombreux cas, la scène peut être rapidement préparée et testée avec EEVEE pour obtenir des rendus préliminaires; Ensuite, la même scène peut être utilisée avec des modifications mineures avec Cycles afin de produire un rendu final de meilleure qualité. En particulier, lorsqu\'une scène configurée avec EEVEE sera utilisée avec Cycles, la valeur et la position des lumières peuvent devoir être ajustées car les deux moteurs de rendu traitent la lumière de différentes manières.

L\'obtention de bons résultats dépend fortement des options de rendu, des matériaux et de l\'éclairage. Le shader de matériau `Principled BSDF` est une solution générique qui fonctionne bien dans de nombreux cas, cependant, pour produire des résultats vraiment photoréalistes, l\'utilisation de textures et de textures normales, ainsi que d\'un éclairage soigné de la scène est toujours très importante .  {{Raytracing Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Raytracing](Category_Raytracing.md) > Tutorial Render with Blender/fr
