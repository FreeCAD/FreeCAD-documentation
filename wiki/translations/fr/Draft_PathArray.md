---
- GuiCommand:
   Name: Draft PathArray
   Name/fr: Draft Réseau selon une courbe
   MenuLocation: Modification -> Outils pour les réseaux -> Réseau selon une courbe
   Workbenches: Draft_Workbench/fr, Arch_Workbench/fr
   Version: 0.14
   SeeAlso: Draft_OrthoArray/fr, Draft_PolarArray/fr, Draft_CircularArray/fr, Draft_PathLinkArray/fr, Draft_PointArray/fr, Draft_PointLinkArray/fr
---

# Draft PathArray/fr

## Description

La commande <img alt="" src=images/Draft_PathArray.svg  style="width:24px;"> **Draft Réseau selon une courbe** crée un réseau régulier à partir d\'un objet sélectionné en plaçant des copies le long d\'un chemin. Utilisez la commande [Draft Réseau lié selon une courbe](Draft_PathLinkArray/fr.md) pour créer un réseau [Link](App_Link/fr.md) plus efficace à la place. À l\'exception du type de réseau créé, réseau de liens ou réseau régulier, la commande [Draft Réseau lié selon une courbe](Draft_PathLinkArray/fr.md) est identique à cette commande.

Ces deux commandes peuvent être utilisées sur des objets 2D créés avec l\'[atelier Draft](Draft_Workbench/fr.md) ou l\'[atelier Sketcher](Sketcher_Workbench/fr.md), mais aussi sur de nombreux objets 3D tels que ceux créés avec l\'[atelier Part](Part_Workbench/fr.md), l\'[atelier PartDesign](PartDesign_Workbench/fr.md) ou l\'[atelier Arch](Arch_Workbench/fr.md).

<img alt="" src=images/Draft_PathArray_Example.png  style="width:400px;"> 
*Un Draft réseau selon une courbe*



## Utilisation

1.  Sélectionnez l\'objet que vous souhaitez mettre en réseau.
2.  Ajouter l\'objet trajectoire à la sélection. Il est également possible de sélectionner des arêtes à la place. Les arêtes doivent appartenir au même objet et doivent être connectées.
3.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le **<img src="images/Draft_PathArray.svg" width=16px> [Réseau selon une courbe](Draft_PathArray/fr.md)**.
    -   Sélectionnez l\'option **Modification → Outils pour les réseaux → <img src="images/Draft_PathArray.svg" width=16px> Réseau selon une courbe** dans le menu.
4.  Le réseau est créé.
5.  Vous pouvez éventuellement modifier les [propriétés](#Propri.C3.A9t.C3.A9s.md) du réseau dans l\'[Éditeur de propriétés](Property_editor/fr.md).



## Alignement

L\'alignement des éléments d\'un Draft Réseau selon une courbe dépend des propriétés du réseau et de l\'orientation de l\'objet source. La position de l\'objet source est ignorée : pour les besoins du réseau, les valeurs {{Value|x}}, {{Value|y}} et {{Value|z}} sont fixées à {{Value|0}}. Si la propriété **Align** du réseau est définie à `False`, l\'orientation des éléments du réseau est identique à celle de l\'objet source. Si elle a pour valeur `True`, l\'axe X du système de coordonnées local de chaque élément placé est tangent à la trajectoire. Les axes Y et Z des systèmes de coordonnées locaux dépendent de la propriété **Align Mode** du réseau. Les autres propriétés du réseau impliquées dans l\'alignement comprennent **Tangent Vector**, **Force Vertical** et **Vertical Vector**.

<img alt="" src=images/Draft_PathArray_example2.png  style="width:600px;"> 
*3 réseaux basés sur la même courbe non planaire.<br>De gauche à droite : Align est false, Align à true pour Align Mode Original et Align à true pour Align Mode Frenet.*.



### Mode d\'alignement 

Trois modes sont disponibles :

#### Original

Ce mode se rapproche le plus du mode unique **Align Mode** disponible dans la version 0.18. Il s\'appuie sur un vecteur normal fixe. Si le chemin est planaire, ce vecteur est perpendiculaire au plan du chemin, sinon un vecteur par défaut, l\'axe Z positif, est utilisé. À partir de ce vecteur normal et du vecteur tangent local (l\'axe X local), un [produit vectoriel](https://fr.wikipedia.org/wiki/Produit_vectoriel) est calculé. Ce nouveau vecteur est utilisé comme axe Z local. L\'orientation de l\'axe Y local est déterminée à partir des axes X et Z locaux.

#### Frenet

Ce mode utilise le vecteur normal local dérivé de la trajectoire à chaque placement d\'élément. Si ce vecteur ne peut pas être déterminé (par exemple dans le cas d\'un segment droit), un vecteur par défaut, toujours l\'axe Z positif, est utilisé à la place. Avec ce vecteur et le vecteur tangent local, le système de coordonnées local est déterminé en utilisant la même procédure que dans le paragraphe précédent.

#### Tangent

Ce mode est similaire à **Align Mode**. {{Value|Original}} mais offre la possibilité de pré-rotation de l\'objet source en spécifiant un **Tangent Vector**.



### Force Vertical et Vertical Vector 

Ces propriétés ne sont disponibles que si **Align Mode** est {{Value|Original}} ou {{Value|Tangent}}. Si **Force Vertical** est défini sur `True`, le système de coordonnées local est calculé d\'une manière différente. **Vertical Vector** est utilisé comme vecteur normal fixe. Un produit vectoriel est à nouveau calculé à partir de ce vecteur normal et du vecteur tangent local (l\'axe X local). Mais ce vecteur est maintenant utilisé comme l\'axe Y local. L\'orientation de l\'axe Z local est déterminée à partir des axes X et Y locaux.

L\'utilisation de ces propriétés peut être nécessaire si l\'un des bords du chemin est (presque) parallèle à la normale par défaut du chemin.



## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Réseau selon une courbe est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés (à l\'exception de certaines propriétés Vue qui ne sont pas héritées par les réseaux Link). Les propriétés suivantes sont supplémentaires, sauf indication contraire :



### Données


{{TitleProperty|Link}}

Les propriétés de ce groupe ne sont disponibles que pour les réseaux de liens. Voir [Std Créer un lien](Std_LinkMake/fr#Propri.C3.A9t.C3.A9s.md) pour plus d\'informations.

-    **Scale|Float**
    

-    **Scale Vector|Vector|Caché**
    

-    **Scale List|VectorList**
    

-    **Visibility List|BoolList|Caché**
    

-    **Placement List|PlacementList|Caché**
    

-    **Element List|LinkList|Caché**
    

-    **_ Link Touched|Bool|Caché**
    

-    **_ Child Cache|LinkList|Caché**
    

-    **Colored Elements|LinkSubCaché|Caché**
    

-    **Link Transform|Bool**
    


{{TitleProperty|Alignment}}

-    **Align|Bool**: spécifie si les éléments du réseau sont alignés ou non le long du chemin. Si elle vaut `False`, toutes les autres propriétés de ce groupe, à l\'exception de **Extra Translation** ne s\'appliquent pas et sont masquées.

-    **Align Mode|Enumeration**: spécifie le mode d\'alignement, qui peut être {{Value|Original}}, {{Value|Frenet}} ou {{Value|Tangent}}.

-    **End Offset|Length**: spécifie la longueur entre la fin du chemin et la dernière copie. Elle doit être inférieure à la longueur du chemin moins **Start Offset**. {{Version/fr|0.21}}

-    **Extra Translation|VectorDistance**: spécifie un déplacement supplémentaire pour chaque élément le long du chemin.

-    **Force Vertical|Bool**: spécifie s\'il faut remplacer la direction normale par défaut par la valeur de **Vecteur Vertical**. Utilisé uniquement si **Align Mode** est {{Value|Original}} ou {{Value|Tangent}}.

-    **Start Offset|Length**: spécifie la longueur entre le début du chemin et la première copie. Elle doit être inférieure à la longueur du chemin. {{Version/fr|0.21}}

-    **Tangent Vector|Vector**: spécifie le vecteur d\'alignement. Utilisé uniquement si **Align Mode** est {{Value|Tangent}}.

-    **Vertical Vector|Vector**: spécifie le remplacement de la direction normale par défaut. Utilisé uniquement si **Vertical Vector** est `True`.


{{TitleProperty|Objects}}

-    **Base|LinkGlobal**: spécifie l\'objet à dupliquer dans le réseau.

-    **Count|Integer**: spécifie le nombre d\'éléments dans le réseau.

-    **Expand Array|Bool**: indique s\'il faut développer le réseau dans la [Vue en arborescence](Tree_view/fr.md) pour permettre la sélection de ses éléments individuels. Disponible uniquement pour les réseaux de type lien (Link).

-    **Path Object|LinkGlobal**: spécifie l\'objet à utiliser pour le chemin. Il doit contenir {{Value|Edges}} dans sa [Part TopoShape](Part_TopoShape/fr.md).

-    **Path Subelements|LinkSubListGlobal**: spécifie une liste d\'arêtes de **Path Object**. Si elle est renseignée, seules ces arêtes sont utilisées pour le chemin.



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

-    **Child View Provider|PersistentObject|Caché**
    

-    **Material List|MaterialList|Caché**
    

-    **Override Color List|ColorList|Caché**
    

-    **Override Material List|BoolList|Caché**
    

-    **Proxy|PythonObject|Caché**: il s\'agit d\'une propriété héritée.


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

Pour créer un réseau selon une courbe, utilisez la méthode `make_path_array` ({{Version/fr|0.19}}) de l\'atelier Draft. Cette méthode remplace la méthode dépréciée `makePathArray`.


```python
path_array = make_path_array(base_object, path_object,
                             count=4, extra=App.Vector(0, 0, 0), subelements=None,
                             align=False, align_mode="Original", tan_vector=App.Vector(1, 0, 0),
                             force_vertical=False, vertical_vector=App.Vector(0, 0, 1),
                             use_link=True)
```

-    `base_object`est l\'objet à mettre en réseau. Il peut également s\'agir du `Label` (chaîne de caractères) d\'un objet du document courant.

-    `path_object`est l\'objet courbe. Il peut également s\'agir du `Label` (chaîne de caractères) d\'un objet du document courant.

-    `count`est le nombre d\'éléments dans le réseau.

-    `extra`est un vecteur qui déplace chaque élément.

-    `subelements`est une liste d\'arêtes de `path_object`, par exemple `["Bord1", "Bord2"]`. Si elle est renseignée, seules ces arêtes sont utilisées pour le chemin.

-   Si `align` est `True` les éléments sont alignés le long de la courbe en fonction de la valeur de `align_mode`, qui peut être `"Original"`, `"Frenet"` ou `"Tangent"`.

-    `tan_vector`est un vecteur unitaire qui définit la direction tangente locale des éléments le long de la courbe. Il est utilisé lorsque `align_mode` est `"Tangent"`.

-   Si `force_vertical` est `True` `vertical_vector` est utilisé pour la direction Z locale des éléments le long de la courbe. Il est utilisé lorsque `align_mode` est `"Original"` ou `"Tangent"`.

-   Si `use_link` est `True`, les éléments créés sont des [App Links](App_Link/fr.md) au lieu de copies ordinaires.

-    `path_array`est restitué avec l\'objet réseau créé.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(500, -1000, 0)
p2 = App.Vector(1500, 1000, 0)
p3 = App.Vector(3000, 500, 0)
p4 = App.Vector(4500, 100, 0)
spline = Draft.make_bspline([p1, p2, p3, p4])
obj = Draft.make_polygon(3, 500)

path_array = Draft.make_path_array(obj, spline, 6)
doc.recompute()

wire = Draft.make_wire([p1, -p2, -p3, -p4])
path_array2 = Draft.make_path_array(obj, wire, count=3, extra=App.Vector(0, -500, 0), subelements=["Edge2", "Edge3"], align=True, force_vertical=True)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PathArray/fr
