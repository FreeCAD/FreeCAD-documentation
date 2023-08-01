---
- GuiCommand:
   Name:OpenSCAD_AddOpenSCADElement
   Name/fr:OpenSCAD Ajout d'un élément OpenSCAD
   MenuLocation:OpenSCAD - Ajouter un élément OpenSCAD
   Workbenches:[OpenSCAD](OpenSCAD_Workbench/fr.md)
---

# OpenSCAD AddOpenSCADElement/fr

## Description

Ajoute un élément OpenSCAD en entrant le code OpenSCAD dans le panneau des tâches et en exécutant le binaire OpenSCAD (nécessite OpenSCAD).

Lorsque **mesh** est sélectionné, **[OpenSCAD](http://www.openscad.org/)** retourne un **maillage**.

Chaque fois que vous appuyez sur **Ajouter**, le code [OpenSCAD](http://www.openscad.org/) est exécuté, et les éléments sont importés.

Si OpenSCAD est exécuté avec succès, ses messages sont affichés comme des avertissements dans la fenêtre de rapport. Ce sera le cas si le chemin vers les fichiers importés, inclus et utilisés est brisé. En cas de résultats non désirés, il est fortement recommandé de jeter un coup d\'oeil aux fenêtres de rapport, car il peut y avoir beaucoup d\'autres résultats, créés par l\'importateur. Si OpenSCAD échoue, ses messages seront enregistrés comme des erreurs.

Les bibliothèques devraient être accessibles comme d\'habitude, tandis que l\'exemple peut être joint comme indiqué ci-dessous.


```python
include <../examples/example001.scad>;
```

comprendrait les premiers exemples également connus sous le nom d\'icône OpenSCAD.

## Installation de OpenSCAD dans FreeCAD 

**Remarque :** OpenSCAD doit être installé sur votre ordinateur avant que FreeCAD ne dispose de cette fonctionnalité
Installez OpenSCAD de la manière appropriée pour votre système d\'exploitation. Voir [le site Web d\'OpenSCAD](https://www.openscad.org/) pour plus d\'informations.

FreeCAD doit savoir où trouver l\'exécutable OpenSCAD :

-   Basculez vers l\'<img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [atelier OpenSCAD](OpenSCAD_Workbench/fr.md) via 
**Menu des ateliers → OpenSCAD**
-   Ouvrez la boîte de dialogue des préférences **Edition → Préférences**
-   Cliquez sur \"OpenSCAD\" dans le plan de gauche
-   Cliquez sur le bouton **...** de **Réglages généraux → Réglages généraux de OpenSCAD → Exécutable OpenSCAD** pour parcourir le répertoire ou entrer le chemin (par exemple, les distributions Linux basées sur Ubuntu `/usr/bin/openscad`) directement dans l\'entrée de ligne à droite du bouton
-   Fermez et redémarrez FreeCAD

:   **Résultat :** une nouvelle icône OpenSCAD apparaîtra dans la barre d\'outils et dans le menu OpenSCAD, dans l\'atelier FreeCAD OpenSCAD.

Remarque: Il est également possible d\'ajouter un autre paramètre facultatif qui contrôle les côtés maximum d\'un polygone avant qu\'il ne soit considéré comme un cercle (fn).

À partir de FreeCAD {{VersionPlus/fr|0.14}}, FreeCAD recherchera l\'exécutable OpenSCAD si le paramètre mentionné ci-dessus est vide.





{{OpenSCAD_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD AddOpenSCADElement/fr
