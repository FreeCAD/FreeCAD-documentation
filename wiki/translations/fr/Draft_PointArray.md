---
 GuiCommand:
   Name: Draft PointArray
   Name/fr: Draft Réseau de points
   MenuLocation: Modification , Outils pour les réseaux ,  Réseau de points
   Workbenches: Draft_Workbench/fr, Arch_Workbench/fr
   Version: 0.18
   SeeAlso: Draft_OrthoArray/fr, Draft_PolarArray/fr, Draft_CircularArray/fr, Draft_PathArray/fr, Draft_PathLinkArray/fr, Draft_PointLinkArray/fr
---

# Draft PointArray/fr

## Description

La commande <img alt="" src=images/Draft_PointArray.svg  style="width:24px;"> **Draft Réseau de points** crée un réseau régulier à partir d\'un objet de base sélectionné en plaçant des copies aux points d\'un objet ponctuel. Utilisez la commande [Draft Réseau lié selon une courbe](Draft_PointLinkArray/fr.md) pour créer un réseau lié [Link](App_Link/fr.md) plus efficace. À l\'exception du type de réseau créé, réseau de liens ou réseau régulier, la commande [Draft Réseau lié selon une courbe](Draft_PointLinkArray/fr.md) est identique à cette commande.

L\'objet de base peut être un objet 2D créé avec l\'[atelier Draft](Draft_Workbench/fr.md) ou l\'[atelier Sketcher](Sketcher_Workbench/fr.md), mais aussi un objet 3D tel que ceux créés avec l\'[atelier Part](Part_Workbench/fr.md), l\'[atelier PartDesign](PartDesign_Workbench/fr.md) ou l\'[atelier Arch](Arch_Workbench/fr.md).

L\'objet Point peut être n\'importe quel objet ayant une forme et des sommets (y compris un [Std Part](Std_Part/fr.md) contenant un ou plusieurs de ces objets), ainsi qu\'un [maillage](Mesh_Workbench/fr.md) et un [nuage de point](Points_Workbench/fr.md). Les points en double dans l\'objet point sont filtrés. {{Version/fr|0.21}}

Dans {{VersionMinus|0.20}}, seuls trois types d\'objets Point sont pris en charge ; voir [Objet Point version 0.20 et inférieure](#Objet_Point_version_0.20_et_inf.C3.A9rieure.md).

<img alt="" src=images/Draft_PointArray_Example.png  style="width:400px;"> 
*Un réseau Draft de points*



## Utilisation

1.  Sélectionnez l\'objet que vous souhaitez mettre en réseau.
2.  Ajoutez l\'objet [composé de points](#Compos.C3.A9_de_points.md) à la sélection.
3.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_PointArray.svg" width=16px> [Réseau de points](Draft_PointArray/fr.md)**.
    -   Sélectionnez l\'option **Modification → Outils pour les réseaux → <img src="images/Draft_PointArray.svg" width=16px> Réseau de points** dans le menu.
4.  Le réseau est créé.
5.  Vous pouvez éventuellement modifier les [propriétés](#Propri.C3.A9t.C3.A9s.md) du réseau dans l\'[Éditeur de propriétés](Property_editor/fr.md).



## Objet Point version 0.20 et inférieure 

Voici les objets Point pris en charge dans {{VersionMinus/fr|0.20}} et la manière dont ils peuvent être créés :

-   [Part Composé](Part_Compound/fr.md) : créez un ou plusieurs [Draft Points](Draft_Point/fr.md) ou [Part Points](Part_Point/fr.md). Sélectionnez-les et lancez la commande [Part Composé](Part_Compound/fr.md).
-   Draft Bloc : créez un ou plusieurs [Draft Points](Draft_Point/fr.md) ou [Part Points](Part_Point/fr.md). Sélectionnez-les et lancez la commande [Draft Agréger](Draft_Upgrade/fr.md).
-   [Sketcher Esquisse](Sketcher_NewSketch/fr.md) : créez une [Esquisse](Sketcher_NewSketch/fr.md) et ajoutez un ou plusieurs [Sketcher Points](Sketcher_CreatePoint/fr.md) à l\'esquisse.



## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Réseau de points est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés (à l\'exception de certaines propriétés Vue qui ne sont pas héritées par les réseaux Link). Les propriétés suivantes sont supplémentaires, sauf indication contraire :



### Données


{{TitleProperty|Link}}

Les propriétés de ce groupe ne sont disponibles que pour les réseaux de liens. Voir [Std Créer un lien](Std_LinkMake/fr#Propri.C3.A9t.C3.A9s.md) pour plus d\'informations.

-    **Scale|Float**
    

-    **Scale Vector|Vector|Hidden**
    

-    **Scale List|VectorList**
    

-    **Visibility List|BoolList|Hidden**
    

-    **Placement List|PlacementList|Hidden**
    

-    **Element List|LinkList|Hidden**
    

-    **_ Link Touched|Bool|Hidden**
    

-    **_ Child Cache|LinkList|Hidden**
    

-    **Colored Elements|LinkSubHidden|Hidden**
    

-    **Link Transform|Bool**
    


{{TitleProperty|Objects}}

-    **Base|Link**: spécifie l\'objet à dupliquer dans le réseau.

-    **Count|Integer**: (en lecture seule) spécifie le nombre d\'éléments dans le réseau. Ce nombre est déterminé par le nombre de points dans l\'objet **Point**.

-    **Expand Array|Bool**: spécifie s\'il faut développer le réseau dans la [Vue en arborescence](Tree_view/fr.md) pour permettre la sélection de ses éléments individuels. Disponible uniquement pour les réseaux de type Link.

-    **Extra Placement|Placement**: spécifie un [placement](Placement.md), une translation et une rotation supplémentaires pour chaque élément du réseau.

-    **Point Object|Link**: spécifie l\'objet composé dont les points sont utilisés pour positionner les éléments du réseau. L\'objet doit avoir une propriété **Links**, **Components** ou **Geometry** et contenir au moins un élément avec les propriétés **X**, **Y**, et **Z**.



### Vue


{{TitleProperty|Link}}

Les propriétés de ce groupe, à l\'exception de la propriété héritée, ne sont disponibles que pour les réseaux liens (Link). Voir [Std Créer un lien](Std_LinkMake/fr#Propri.C3.A9t.C3.A9s.md) pour plus d\'informations.

-    **Draw Style|Enumeration**
    

-    **Line Width|FloatConstraint**
    

-    **Override Material|Bool**
    

-    **Point Size|FloatConstraint**
    

-    **Selectable|Bool**: il s\'agit d\'une propriété héritée qui apparaît dans le groupe Sélection pour d\'autres réseaux.

-    **Shape Material|Material**
    


{{TitleProperty|Base}}

Les propriétés de ce groupe, à l\'exception de la propriété héritée, ne sont disponibles que pour les réseaux liens (Link). Voir [Std Créer un lien](Std_LinkMake/fr#Propri.C3.A9t.C3.A9s.md) pour plus d\'informations.

-    **Child View Provider|PersistentObject|Hidden**
    

-    **Material List|MaterialList|Hidden**
    

-    **Override Color List|ColorList|Hidden**
    

-    **Override Material List|BoolList|Hidden**
    

-    **Proxy|PythonObject|Hidden**: il s\'agit d\'une propriété héritée.


{{TitleProperty|Display Options}}

Les propriétés de ce groupe sont des propriétés héritées. Voir [Part Feature](Part_Feature/fr#Propri.C3.A9t.C3.A9s.md) pour plus d\'informations.

-    **Bounding Box|Bool**: cette propriété n\'est pas héritée par les réseaux de liens (Link).

-    **Display Mode|Enumeration**: pour les réseaux de liens, il peut s\'agir de {{value|Link}} ou {{value|ChildView}}. Pour les autres réseaux, il peut s\'agir de : {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} ou {{value|Points}}

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: non utilisé.

-    **Pattern Size|Float**: non utilisé.


{{TitleProperty|Object style}}

Les propriétés de ce groupe ne sont pas héritées par les réseaux de liens.



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Pour créer un réseau de points, utilisez la méthode `make_point_array` ({{Version/fr|0.19}}) de l\'atelier Draft. Cette méthode remplace la méthode dépréciée `makePointArray`.


```python
point_array = make_point_array(base_object, point_object, extra=None, use_link=True)
```

-    `base_object`est l\'objet à mettre en réseau. Il peut également s\'agir du `Label` (chaîne de caractères) d\'un objet du document courant.

-    `point_object`est l\'objet contenant les points. Il peut également s\'agir du `Label` (chaîne de caractères) d\'un objet du document courant. Il doit avoir une propriété `Geometry`, `Links`, ou `Components` contenant des points.

-    `extra`est un `App.Placement`, un `App.Vector` ou un `App.Rotation` qui déplace chaque élément.

-   Si `use_link` est `True`, les éléments créés sont des [App Links](App_Link/fr.md) au lieu de copies ordinaires.

Exemple:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon = Draft.make_polygon(3, radius=500.0)

p1 = Draft.make_point(App.Vector(1500, 0, 0))
p2 = Draft.make_point(App.Vector(2500, 0, 0))
p3 = Draft.make_point(App.Vector(2000, 1000, 0))

compound = doc.addObject("Part::Compound", "Compound")
compound.Links = [p1, p2, p3]

point_array = Draft.make_point_array(polygon, compound)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PointArray/fr
