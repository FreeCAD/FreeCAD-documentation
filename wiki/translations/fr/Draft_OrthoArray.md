---
- GuiCommand:/fr
   Name:Draft OrthoArray
   Name/fr:Draft Réseau orthogonal
   MenuLocation:Modification → Outils de réseau → Réseau
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Draft Réseau polaire](Draft_PolarArray/fr.md), [Draft Réseau circulaire](Draft_CircularArray/fr.md), [Draft Réseau selon une courbe](Draft_PathArray/fr.md), [Draft Réseau lié selon une courbe](Draft_PathLinkArray/fr.md), [Draft Réseau de points](Draft_PointArray/fr.md), [Draft Réseau lié selon des points](Draft_PointLinkArray/fr.md)
---

# Draft OrthoArray/fr

## Description

La commande <img alt="" src=images/Draft_OrthoArray.svg  style="width:24px;"> **Draft Réseau orthogonal** crée un réseau orthogonal (3 axes) à partir d\'un objet sélectionné. La commande peut éventuellement créer un réseau de liens [Link](App_Link/fr.md), plus efficace qu\'un réseau normal.

Cette commande peut être utilisée sur des objets 2D créés avec l\'[atelier Draft](Draft_Workbench/fr.md) ou l\'[atelier Sketcher](Sketcher_Workbench/fr.md), mais aussi sur de nombreux objets 3D tels que ceux créés avec l\'[atelier Part](Part_Workbench/fr.md), l\'[atelier PartDesign](PartDesign_Workbench/fr.md) ou l\'[atelier Arch](Arch_Workbench/fr.md).

<img alt="" src=images/Draft_Array_example.png  style="width:300px;"> 
*Un Draft réseau orthogonal*

## Utilisation

1.  Sélectionner un objet au choix.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_OrthoArray.svg" width=16px> [Réseau](Draft_OrthoArray/fr.md)**.
    -   Sélectionnez l\'option **Modification → Outils de réseau → <img src="images/Draft_OrthoArray.svg" width=16px> Réseau** dans le menu.
3.  Le panneau de tâches **Réseau orthogonal** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
4.  Si vous n\'avez pas encore sélectionné d\'objet : sélectionnez un objet.
5.  Saisissez les paramètres requis dans le panneau des tâches.
6.  Pour terminer la commande, effectuez l\'une des opérations suivantes :
    -   Cliquez dans la [Vue 3D](3D_view/fr.md).
    -   Appuyez sur **Entrée**.
    -   Appuyez sur le bouton **OK**.

## Options

-   Entrez le **Nombre d'éléments** pour les directions X, Y et Z. Ce nombre doit être au moins {{Value|1}} pour chaque direction. Ce nombre doit être au moins {{Value|1}} pour chaque direction.
-   Entrez dans le champ **Intervalles en X** pour spécifier le déplacement des éléments dans la direction X. Pour un réseau rectangulaire, les intervalles Y et Z doivent être spécifiés. Pour un réseau rectangulaire, les valeurs Y et Z doivent être {{Value|0}}.
-   Entrez dans le champ **Intervalles en Y** pour spécifier le déplacement des éléments dans la direction Y. Pour un tableau rectangulaire, les valeurs X et Z doivent être {{Value|0}}. Pour un réseau rectangulaire, les valeurs X et Z doivent être {{Value|0}}.
-   Entrez dans le champ **Intervalles en Z** pour spécifier le déplacement des éléments dans la direction Z. Pour un tableau rectangulaire, les valeurs X et Z doivent être {{Value|0}}. Pour un réseau rectangulaire, les valeurs X et Y doivent être {{Value|0}}.
-   Appuyez sur le bouton **Réinitialiser X, Y ou Z** pour réinitialiser le déplacement dans la direction donnée aux valeurs par défaut.
-   Si la case **Union** est cochée, les éléments qui se chevauchent dans le réseau sont fusionnés. Cela ne fonctionne pas pour les réseaux de liens.
-   Si la case **Lier un réseau** est cochée, un réseau de liens est créé au lieu d\'un réseau normal. Un réseau de liens est plus efficace car ses éléments sont des objets [App Link](App_Link/fr.md).
-   Appuyez sur **Echap** ou sur le bouton **Annuler** pour annuler la commande en cours.

## Remarques

-   Un Draft Réseau orthogonal peut être transformé en un [Draft Réseau polaire](Draft_PolarArray/fr.md) ou un [Draft Réseau circulaire](Draft_CircularArray/fr.md) en modifiant sa propriété **Array Type**.
-   Un réseau de liens ne peut pas être transformé en un réseau normal ou vice versa. Le type de réseau doit être décidé au moment de la création.

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour modifier le nombre de décimales utilisées pour la saisie des coordonnées : **Edition → Préférences... → Général → Unités → Systèmes d'unités → Nombre de décimales**.

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

La commande Draft Réseau orthogonal, la commande [Draft Réseau polaire](Draft_PolarArray/fr.md) et la commande [Draft Réseau circulaire](Draft_CircularArray/fr.md) créent le même objet. Cet objet est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés (à l\'exception de certaines propriétés Vue qui ne sont pas héritées par les réseaux liens Link). Les propriétés suivantes sont supplémentaires, sauf indication contraire :

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
    


{{TitleProperty|Circular array}}

Les propriétés de ce groupe sont cachées pour les réseaux orthogonaux et les réseaux polaires.

-    **Number Circles|Integer**: spécifie le nombre de couches circulaires. Doit être au moins {{Value|2}}.

-    **Radial Distance|Distance**: spécifie la distance entre les couches circulaires.

-    **Symmetry|Integer**: spécifie le nombre de lignes de symétrie. Ce nombre modifie la répartition des éléments dans le réseau.

-    **Tangential Distance|Distance**: spécifie la distance entre les éléments d\'une même couche circulaire. Elle doit être supérieure à zéro.


{{TitleProperty|Objects}}

-    **Array Type|Enumeration**: spécifie le type de réseau, qui peut être {{value|ortho}}, {{value|polar}} ou {{value|circular}}.

-    **Axis Reference|LinkGlobal**: spécifie l\'objet et le bord à utiliser à la place des propriétés **Axis** et **Center**. Non utilisé pour les réseaux orthogonaux.

-    **Base|Link**: spécifie l\'objet à dupliquer dans le réseau.

-    **Count|Integer**: (en lecture seule) spécifie le nombre total d\'éléments dans le réseau. Uniquement disponible pour les réseaux Link.

-    **Expand Array|Bool**: spécifie s\'il faut développer le réseau dans la vue [Tree view](Tree_view.md) pour permettre la sélection de ses éléments individuels. Disponible uniquement pour les réseaux de type Link.

-    **Fuse|Bool**: spécifie si les éléments qui se chevauchent dans le réseau sont fusionnés ou non. Non utilisé pour les réseaux de type Link.


{{TitleProperty|Orthogonal array}}

Les propriétés de ce groupe sont masquées pour les réseaux circulaires et les réseaux polaires.

-    **Interval X|VectorDistance**: spécifie l\'intervalle entre les éléments dans la direction X.

-    **Interval Y|VectorDistance**: spécifie l\'intervalle entre les éléments dans la direction Y.

-    **Interval Z|VectorDistance**: spécifie l\'intervalle entre les éléments dans la direction Z.

-    **Number X|Integer**: spécifie le nombre d\'éléments dans la direction X. Doit être au moins {{Value|1}}.

-    **Number Y|Integer**: spécifie le nombre d\'éléments dans la direction Y. Doit avoir au moins la valeur {{Value|1}}.

-    **Number Z|Integer**: spécifie le nombre d\'éléments dans la direction Z. Doit être au moins égal à {{Value|1}}.


{{TitleProperty|Polar array}}

Les propriétés de ce groupe sont masquées pour les réseaux circulaires et les réseaux orthogonaux.

-    **Angle|Angle**: spécifie l\'ouverture de l\'arc de cercle. Utilisez {{value|360&#176;}} pour un cercle complet.

-    **Interval Axis|VectorDistance**: spécifie l\'intervalle entre les éléments dans la direction **Axis**.

-    **Number Polar|Integer**: spécifie le nombre d\'éléments dans la direction polaire.


{{TitleProperty|Polar/circular array}}

Les propriétés de ce groupe sont cachées pour les réseaux orthogonaux.

-    **Axis|Vector**: spécifie la direction de l\'axe du réseau.

-    **Center|VectorDistance**: spécifie le point central du réseau. L\'axe du réseau passe par ce point. Pour les réseaux circulaires, il s\'agit d\'un décalage par rapport à **Placement** de l\'objet **Base**.

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

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

### Réseau paramétrique 

Pour créer un réseau orthogonal paramétrique, utilisez la méthode `make_array` ({{Version/fr|0.19}}) de l\'atelier Draft. Cette méthode remplace la méthode dépréciée `makeArray`. La méthode `make_array` peut créer des Draft Réseaux orthogonaux, [Draft Réseaux polaires](Draft_PolarArray/fr.md) et [Draft Réseaux circulaires](Draft_CircularArray/fr.md). Pour chaque type de réseau, un ou plusieurs wrappers sont disponibles.

La méthode principale :


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

Les wrappers pour les réseaux orthogonaux sont :


```python
array = make_ortho_array(base_object,
                         v_x=App.Vector(10, 0, 0), v_y=App.Vector(0, 10, 0), v_z=App.Vector(0, 0, 10),
                         n_x=2, n_y=2, n_z=1,
                         use_link=True)
```


```python
array = make_ortho_array2d(base_object,
                           v_x=App.Vector(10, 0, 0), v_y=App.Vector(0, 10, 0),
                           n_x=2, n_y=2,
                           use_link=True)
```

Les wrappers pour les réseaux rectangulaires sont :


```python
array = make_rect_array(base_object,
                        d_x=10, d_y=10, d_z=10,
                        n_x=2, n_y=2, n_z=1,
                        use_link=True)
```


```python
array = make_rect_array2d(base_object,
                          d_x=10, d_y=10,
                          n_x=2, n_y=2,
                          use_link=True)
```

-    `base_object`est l\'objet à mettre en réseau. Il peut également s\'agir du `Label` (chaîne de caractères) d\'un objet du document courant. (chaîne de caractères) d\'un objet dans le document actuel.

-    `v_x`, `v_y`, et `v_z` sont les vecteurs entre les points de base des éléments dans les directions respectives.

-    `d_x`, `d_y`, et `d_z` sont les distances entre les points de base des éléments dans les directions respectives.

-    `n_x`, `n_y`, et `n_z` sont les nombres d\'éléments dans les directions respectives.

-   Si `use_link` est `True`, les éléments créés sont des [App Links](App_Link/fr.md) au lieu de copies ordinaires.

-    `array`est restitué avec l\'objet réseau créé.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rect = Draft.make_rectangle(1500, 500)
v_x = App.Vector(1600, 0, 0)
v_y = App.Vector(0, 600, 0)

array = Draft.make_ortho_array2d(rect, v_x, v_y, 3, 4)
doc.recompute()
```

### Réseau non paramétrique 

Pour créer un réseau orthogonal non-paramétrique, utilisez la méthode `array` de l\'atelier Draft. Cette méthode renvoie `None`.


```python
array(objectslist, xvector, yvector, xnum, ynum)
array(objectslist, xvector, yvector, zvector, xnum, ynum, znum)
```

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rect = Draft.make_rectangle(1500, 500)
v_x = App.Vector(1600, 0, 0)
v_y = App.Vector(0, 600, 0)

Draft.array(rect, v_x, v_y, 3, 4)
doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft OrthoArray/fr
