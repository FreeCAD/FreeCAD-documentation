# Assembly2 Workbench/fr
**L'atelier Assembly2 est obsolète. Son auteur ne le maintient plus, il se peut donc qu'il ne fonctionne pas avec les versions 0.17 et supérieures de FreeCAD. Les informations contenues dans cette page ne sont pas maintenues ; elles sont juste conservées à des fins historiques.**


{{Message|Pour une alternative, voir [A2plus](A2plus_Workbench/fr.md). Cet atelier est un fork d'Assembly2, mais il n'est pas compatible avec lui. Si vous avez des modèles plus anciens que vous devez ouvrir, vous devriez rester avec FreeCAD 0.16 et Assembly2. Les modèles plus récents doivent être créés entièrement et ouverts avec A2plus.<br/>

Pour d'autres options, voir [Assembly3](Assembly3_Workbench/fr.md) ou [Assembly4](Assembly4_Workbench/fr.md). Ces ateliers sont également inspirés de Assembly2 mais ne sont pas compatibles avec lui non plus.}}



## Introduction

[Assembly2](Assembly2_Workbench/fr.md) est un atelier d\'assemblage pour FreeCAD v0.15 qui permet d\'importer des pièces à partir de fichiers externes.

Comme indiqué par son auteur [sur le forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=16591), il n\'est plus maintenu depuis 2016, il peut donc avoir des problèmes avec FreeCAD 0.17 et supérieur. Le plus récent et activement maintenu [atelier A2plus](A2plus_Workbench/fr.md) est une bonne alternative.

![](images/Assembly2_example.jpg )



## Utilisation

Flux de travail prévu :

-   Chaque pièce de l\'assemblage est conçue dans son propre fichier FreeCAD.
-   Un fichier FreeCAD d\'assemblage distinct est créé
-   Les pièces sont importées dans ce fichier d\'assemblage à l\'aide de l\'atelier d\'assemblage 2
-   Des contraintes spatiales sont ensuite ajoutées pour assembler les pièces importées.

Fonctions

-   Contrainte de bord circulaire
-   Contrainte axiale
-   Contrainte plane
-   Importation de pièces
-   Mise à jour des pièces déjà importées

Restrictions

-   Le solveur de contraintes est pauvre et peut échouer ou prendre trop de temps pour les assemblages compliqués.
-   L\'annulation et d\'autres fonctions similaires ne sont pas prises en charge



## Références

-   Auteur : hamish
-   Page d\'accueil : [Assembly2](https://github.com/hamish2014/FreeCAD_assembly2)
-   Code source sur github : [Assembly2](https://github.com/hamish2014/FreeCAD_assembly2)



## Outils

Barre d\'outils

![](images/Assembly2-menu-orizz.png )

Menu déroulant

![](images/Assembly2-menu-vert.png )

-   <img alt="" src=images/Assembly2_ImportPart.png  style="width:32px;"> Importer une pièce d\'un autre document FreeCAD
-   <img alt="" src=images/Assembly2_UpdatePart.png  style="width:32px;"> Mettre à jour les pièces importées dans l\'assemblage
-   <img alt="" src=images/Assembly2_Move.png  style="width:32px;"> Déplacer
-   <img alt="" src=images/Assembly2_CircularEdgeConstraint.png  style="width:32px;"> Ajouter une contrainte d\'arête circulaire
-   <img alt="" src=images/Assembly2_PlaneConstraint.png  style="width:32px;"> Ajouter une contrainte de plan
-   <img alt="" src=images/Assembly2_AxialConstraint.png  style="width:32px;"> Ajouter une contrainte axiale
-   <img alt="" src=images/Assembly2_AngularConstraint.png  style="width:32px;"> Créer une contrainte angulaire entre deux plans
-   <img alt="" src=images/Assembly2_SphericalSurfaceConstraint.png  style="width:32px;"> Ajouter une contrainte de surface sphérique
-   <img alt="" src=images/Assembly2_DOFAnimation.png  style="width:32px;"> Animer les degrés de liberté
-   <img alt="" src=images/Assembly2_Assembly2Constraint.png  style="width:32px;"> Résoudre la contrainte Assembly2
-   <img alt="" src=images/Assembly2_Mux.png  style="width:32px;"> Combine l\'assemblage en un seul objet (à utiliser pour créer un dessin de l\'assemblage, et ainsi de suite\...)
-   <img alt="" src=images/Assembly2_ListParts.png  style="width:32px;"> Crée une liste de pièces à partir des objets importés avec l\'atelier assembly2.
-   <img alt="" src=images/Assembly2_Ceck.png  style="width:32px;"> Assemblage Ceck pour le chevauchement/interférence des pièces.

Autre

-   <img alt="" src=images/Assembly2_BoltMultipleCircularEdges.png  style="width:32px;"> Boulon à arêtes circulaires multiples
-   <img alt="" src=images/Assembly2_FlipConstraint.png  style="width:32px;"> Contrainte de retournement
-   <img alt="" src=images/Assembly2_LockRotation.png  style="width:32px;"> Verrouillage de la rotation
-   <img alt="" src=images/Assembly2_Preferences.png  style="width:32px;"> Préférences
-   <img alt="" src=images/Assembly2_Assembly2.png  style="width:32px;"> Icône WB de Assembly2

## Installation



### Installation automatique 

Cet atelier peut être installé à partir du [Gestionnaire des extensions](Std_AddonMgr/fr.md).



### Depuis GitHub 

Pour utiliser cet atelier, clonez ce dépôt git sous votre répertoire FreeCAD Mod, et installez les bibliothèques Python pyside et numpy. Sur un système Linux basé sur Debian tel qu\'Ubuntu, l\'installation peut se faire par BASH comme suit


```python
sudo apt-get install git python-numpy python-pyside
mkdir ~/.FreeCAD/Mod
cd ~/.FreeCAD/Mod
git clone https://github.com/hamish2014/FreeCAD_assembly2.git
```

Dans FreeCAD, vous aurez maintenant une nouvelle entrée de workbench appelée \"Assembly 2\". Une fois installé, utilisez git pour mettre à jour vers la dernière version via BASH comme suit


```python
cd ~/.FreeCAD/Mod/FreeCAD_assembly2
git pull
rm *.pyc
```

Sinon, sur un système Ubuntu, le PPA freecad-community peut être utilisé :


```python
Add ppa:freecad-community/ppa to your software sources
sudo apt-get update
sudo apt-get install freecad-extras-assembly2
```

Dans Windows

-   Téléchargez le dépôt git sous forme de ZIP.
-   En supposant que FreeCAD est installé dans \"C:\\PortableApps\\FreeCAD 0_15\", allez dans \"C:\\PortableApps\\FreeCAD 0_15\\Mod\" dans l\'explorateur Windows.
-   Créez un nouveau répertoire nommé \"assembly2\".
-   Dézippez le répertoire téléchargé dans \"C:\\PortableApps\\FreeCAD 0_15\\Mod\\assembly2\".

FreeCAD dispose désormais d\'une nouvelle entrée d\'atelier appelée \"Assembly 2\".

Pyside et Numpy sont intégrés dans les dev-Snapshots de FreeCAD 0.15, donc ces paquets Python n\'ont pas besoin d\'être installés individuellement.

Pour mettre à jour la dernière version, supprimez le dossier assembly2 et téléchargez à nouveau le dépôt git.



## Liens

-   Wiki de l\'atelier :
-   Wiki de FreeCAD :
-   Forum de FreeCAD : <http://forum.freecadweb.org/viewtopic.php?f=10&t=8577>
-   Tutoriels :
-   Vidéos : [vidéo 1](https://www.youtube.com/watch?v=dhaYJKDk4GI), [vidéo 2](http://youtu.be/ufhyUxQkeC0),
-   Fichiers :
-   Signaler les bugs : veuillez signaler les bogues à <https://github.com/hamish2014/FreeCAD_assembly2/issues>



## Autres liens intéressants 

-   [Animation](http://www.freecadweb.org/wiki/index.php?title=Sandbox:Animation) : cet atelier peut être utilisé pour créer des séquences d\'images.
-   [ExplodedAnimation](http://www.freecadweb.org/wiki/index.php?title=Sandbox:ExplodedAnimation) : atelier de FreeCAD permettant de créer des vues éclatées et des animations d\'assemblages.
-   [Ateliers externes](External_workbenches/fr.md)



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Assembly2 Workbench/fr
