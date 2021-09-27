---
- GuiCommand:/fr
   Name:Part CreatePrimitives
   Name/fr:Part Primitives
   MenuLocation:Pièce → Créer des primitives...
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Générateur de formes](Part_Builder/fr.md)
---

# Part Primitives/fr

## Description

_.

<img alt="" src=images/Part_Primitives_example.png  style="width:800px;"> 
*Formes primitives pouvant être créées avec l'[atelier Part](Part_Workbench/fr.md).*

## Utilisation

Pour créer une primitive, soit

\#\* appuyez sur le bouton **<img src="images/Part_Primitives.svg" width=24px> '''Création de primitives géométriques paramétrées'''** dans la barre d\'outils.

\#\* sélectionnez **Pièce → Créer des primitives...** dans la barre de menu.

1.  Dans la boîte de dialogue qui apparaît, sélectionnez la primitive, définissez ses paramètres et son emplacement, puis appuyez sur **Créer**

La boîte de dialogue reste ouverte afin que vous puissiez ensuite créer d\'autres primitives.

Pour éditer une primitive, il y a 2 façons:

Utilisation de la boîte de dialogue: {{Version/fr|0.19}}

1.  Sélectionnez la primitive dans l\'arborescence et double-cliquez dessus.
2.  La même boîte de dialogue s\'ouvrira qui a également été utilisée pour créer la primitive. Modifiez-y les paramètres et vous obtenez un aperçu en direct de la primitive modifiée.
3.  Pour terminer l\'édition, appuyez sur **OK**.

Utilisation de l\'[Éditeur de propriétés](Property_editor/fr.md):

1.  Sélectionnez la primitive dans l\'arborescence.
2.  Modifiez ses propriétés dans la table Propriétés.

## Primitives géométriques 

Les primitives suivantes peuvent être créées:

-   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Plan](Part_Plane/fr.md): Crée un plan.
-   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> _.
-   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> _.
-   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> _.
-   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> _.
-   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellipsoïde](Part_Ellipsoid/fr.md): Crée un ellipsoïde.
-   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> _.
-   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prisme](Part_Prism/fr.md): Crée un prisme.
-   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Pyramide tronquée](Part_Wedge/fr.md): Crée une pyramide tronquée.
-   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Hélice](Part_Helix/fr.md): Crée une hélice.
-   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spirale](Part_Spiral/fr.md): Crée une spirale.
-   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Cercle](Part_Circle/fr.md): Crée une arête circulaire.
-   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse/fr.md): Crée une arête elliptique.
-   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Point](Part_Point.md): Crée un point (sommet).
-   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Ligne](Part_Line/fr.md): Crée une ligne (bord).
-   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Polygone régulier](Part_RegularPolygon/fr.md): Crée un polygone régulier.

## Script


**Voir aussi:**

[Part scripts](Part_scripting/fr.md)

Testez la création des primitives avec un script. {{Version/fr|0.19}}

Ce peut être lancer à partir de la [Console Python](Python_console/fr.md). 
```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```

Ce script se trouve dans le répertoire d\'installation du programme et peut être examiné pour voir comment les primitives de base sont construites. 
```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```

Il peut également être utilisé comme entrée dans le programme. 
```python
freecad $INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Primitives/fr
