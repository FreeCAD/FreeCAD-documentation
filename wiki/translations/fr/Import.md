---
- TutorialInfo   */fr
   Topic   *Atelier Arch
   Level   *Avancé
   Time   *120 minutes
   Author   *Pablo Gil
   FCVersion   *0.19.x
   Files   *
}}

## Introduction

La recherche d\'une copie de travail d\'IfcOpenShell-python sous OSX/macOS pour importer/exporter des fichiers IFC a été si difficile que je partage ce tutoriel au cas où cela aiderait plus de gens. Mon système est OSX 10.11.6, 64 bits avec Python 2.7.11, cela pourrait fonctionner pour vous si vous avez également OSX car ils sont souvent 64 bits mais peuvent différer du mien. La procédure peut être très similaire si vous exécutez Linux ou Windows, mais elle présente probablement quelques différences.

## Conditions

-   [IfcOpenShell](IfcOpenShell/fr.md)
-   FreeCAD v0.19 ou ultérieur

## Étapes

1\. Téléchargez ou clonez le projet GitHub complet sur <https   *//github.com/IfcOpenShell/IfcOpenShell> (ce sera toujours la version la plus récente)

   *   
    `git clone https   *//github.com/IfcOpenShell/IfcOpenShell
---

# Import/Export IFC - compiling IfcOpenShell/fr

     

2\. Depuis un terminal, accédez au dossier **/nix/** et lancez le script. Sous OSX, il est exécuté avec   * 
```python
cd nix/
./build-all.sh
``` Il faudra entre 30 et 120 minutes pour tout compiler. Ce n\'est pas la façon la plus intelligente de compiler [IfcOpenShell](IfcOpenShell/fr.md) mais ce simple script compilera toutes les dépendances, les versions de Python, etc.

3\. Une fois terminé (je ne me souviens pas maintenant mais il sera imprimé quelque chose comme \"Built IfcOpenShell\...\" et il reviendra à votre invite), vous aurez un nouveau dossier **/IfcOpenShell/build/** plein de fichiers et de dossiers. D\'après mon expérience personnelle, il y a deux semaines, le script nix \"build-all.sh\" ne s\'est pas terminé avec succès, mais après l\'avoir essayé hier avec les dernières mises à jour, cela a bien fonctionné, donc je suppose que vous pourriez rencontrer quelque chose de similaire au cas où le développement irait plus loin\... Alors maintenant, vous avez tout ce dont vous avez besoin, mais vous devez faire un travail manuel pour le faire fonctionner   *

4\. Ouvrez FreeCAD et ouvrez la [Console Python](Python_console/fr.md) et la [Vue rapport](Report_view/fr.md). Ensuite, écrivez dans la console Python ce qui suit   * 
```python
import sys
print sys.path
``` Vous obtiendrez une longue ligne avec tous les chemins que FreeCAD lit. Vous pourrez peut-être installer IfcOpenShell dans n\'importe lequel d\'entre eux, mais je vous suggère de le placer dans l\'un d\'entre eux où vous trouverez un **/site-packages/** après un **/Python/** ou **/python-something/**. Dans mon cas, c\'était **/Library/Python/2.7/site-packages**. (Remarque   * vous trouverez des chemins dans le répertoire de votre application mais je vous suggère de ne pas les utiliser car IfcOpenShell ne sera disponible que pour cette application)

5\. Une fois localisé où vous voulez/devez l\'installer, allez-y avec votre navigateur de fichiers (Finder sous OSX). Autrement dit, allez dans le dossier **/site-packages/**

   *   
    {{incode|cd site-packages/`
    

6\. Ouvrez une nouvelle fenêtre de navigateur de fichiers et accédez à votre projet GitHub téléchargé   * **/IfcOpenShell/src/ifcopenshell-python/** et copiez le dossier complet **/ifcopenshell/**

7\. Collez-le dans le dossier **/site-packages/** . Maintenant, vous devriez avoir quelque chose comme   * 
```python
/site-packages/ifcopenshell/__init__.py
/site-packages/ifcopenshell/entity_instance.py
/site-packages/ifcopenshell/file.py
/site-packages/ifcopenshell/geom/app.py
/site-packages/ifcopenshell/geom/main.py
/site-packages/ifcopenshell/geom/occ_utils.py
/site-packages/ifcopenshell/geom/__init__.py
/site-packages/ifcopenshell/guid.py
```

8\. Maintenant, nous devons choisir les fichiers dans le dossier /build/, ils sont   * 
```python
_ifcopenshell_wrapper.so
ifcopenshell_wrapper.py
``` mais comme nous avons tout compilé, vous devrez choisir celui qui correspond à votre version FreeCAD Python. Vérifiez-le facilement en lisant la première ligne de votre vue FreeCAD [Console Python](Python_console/fr.md). Dans mon cas, c\'était Python 2.7.11.

9\. Maintenant, copions les fichiers à l\'endroit où ils correspondent à votre version de Python. Dans mon cas, c\'était   * 
```python
/IfcOpenShell/build/Darwin/x86_64/build/ifcopenshell/[b]python-2.7[/b].10/ifcwrap/
```

10\. Collez-les dans **/site-packages/ifcopenshell/**

11\. Vérifiez que tout est en place   * 
```python
/site-packages/ifcopenshell/__init__.py                  (1)
/site-packages/ifcopenshell/entity_instance.py           (1)
/site-packages/ifcopenshell/_ifcopenshell_wrapper.so     (2)
/site-packages/ifcopenshell/file.py                      (1)
/site-packages/ifcopenshell/geom/__init__.py             (1)
/site-packages/ifcopenshell/geom/app.py                  (1)
/site-packages/ifcopenshell/geom/main.py                 (1)
/site-packages/ifcopenshell/geom/occ_utils.py            (1)
/site-packages/ifcopenshell/guid.py                      (1)
/site-packages/ifcopenshell/ifcopenshell_wrapper.py      (2)
```

\(1\) depuis le projet GitHub
(2) depuis le dossier /build/

28/5000 12. Fermez et rouvrez FreeCAD

## Test

Maintenant qu\'il est installé, vérifions si tout fonctionne comme prévu   *

12.1 dans la console Python, écrivez   * 
```python
import ifcopenshell
from ifcopenshell import geom
``` s\'il ne génère aucune erreur, cela signifie qu\'il est peut-être correctement installé

12.2 Accédez au [manuel FreeCAD de Yorik](Manual   *BIM_modeling/fr.md), accédez à la partie inférieure de la page et téléchargez les fichiers suivants pour tester   * 
```python
house.FCStd
house.ifc
```

12.3 Ouvrez **house.FCStd**, sélectionnez l\'objet racine \"Building\" et exportez-le (**File → Export**) en définissant le type de fichier sur \"Industry Foundation Classes (\*.ifc)\". Appuyez sur **Save** et si cela fonctionne et que cela ne génère pas d\'erreur dans la [Vue rapport](Report_view/fr.md), cela fonctionne.

12.4 Test final, importez **house.ifc** dans un nouveau fichier alors ouvrez un nouveau fichier et importez ce fichier\... cela prendra un certain temps.

13\. Profitez du BIM avec FreeCAD!

## Réflexions finales 

Mon opinion est que FreeCAD lui-même devrait avoir des versions précompilées d\'IfcOpenShell fournies avec la distribution, car le construire par vous-même est une douleur totale et l\'utilisateur moyen ne le fera pas (ils ne savent pas comment compiler, gérer GitHub, etc.), mais enfin, peut-être dans le futur.

J\'espère que cela vous aidera.

Tchao!

## Liens

-   Fil du forum en relation [discussion](http   *//forum.freecadweb.org/viewtopic.php?f=23&t=17536)
-   [IfcOpenShell](IfcOpenShell/fr.md)


{{Userdocnavi

}}

[Category   *BIM](Category_BIM.md) [Category   *Arch](Category_Arch.md) [Category   *3rd Party](Category_3rd_Party.md) [Category   *File_Formats](Category_File_Formats.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [BIM](Category_BIM.md) > [Arch](Category_Arch.md) > [3rd Party](Category_3rd Party.md) > [File_Formats](Category_File_Formats.md) > Import/Export IFC - compiling IfcOpenShell/fr
