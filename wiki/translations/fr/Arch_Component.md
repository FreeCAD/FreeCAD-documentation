---
 GuiCommand:
   Name: Arch Component
   Name/fr: Arch Composant
   MenuLocation: 3D/BIM , Outils 3D génériques , Composant
   Workbenches: BIM_Workbench/fr
---

# Arch Component/fr

## Description

Crée un composant [Arch](BIM_Workbench/fr.md) non-paramétrique à partir de n\'importe quel objet [Part](Part_Workbench/fr.md). Cela donne un objet de base Part avec les mêmes attributs et propriétés que les autres objets Arch et permet de préciser comment il doit être exporté au format IFC en définissant sa propriété **Ifc Type**.



## Utilisation

1.  Sélectionnez un objet issu de l\'[atelier Part](Part_Workbench/fr.md)
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Arch_Component.svg" width=16px> [Composant](Arch_Component/fr.md)**.
    -   Sélectionnez l\'option **3D/BIM → Outils 3D génériques → <img src="images/Arch_Component.svg" width=16px> Composant** du menu.



## Propriétés

L\'objet Composant de Arch est également une base partagée par tous les autres objets Arch ([Mur](Arch_Wall/fr.md), [Structure](Arch_Structure/fr.md) etc.). Par conséquent, certaines de ses propriétés et comportements sont communs à tous les objets Arch (à l\'exception des outils qui ne produisent pas d\'objets solides, comme [Plan de coupe](Arch_SectionPlane/fr.md) ou [Axes](Arch_Axis/fr.md)).



### Données


{{TitleProperty|Component}}

-    **Additions|LinkList**: les composants Arch ont une propriété d\'addition, qui peut contenir une référence à un nombre quelconque d\'autres objets basés sur la [forme](Part_Workbench/fr.md). La forme de ces ajouts sera liée à la forme de base du composant, pour produire la forme finale. Voir [Remarques](##Remarques.md).

-    **Axis|Link**: un axe ou un système d\'axes facultatif sur lequel cet objet doit être dupliqué.

-    **Base|Link**: les composants Arch sont toujours basés sur un objet de base de l\'[atelier Part](Part_Workbench/fr.md). Certains types d\'objets Arch vont simplement utiliser la forme de base telle quelle, d\'autres (par exemple [Arch Mur](Arch_Wall/fr.md)) effectueront des opérations supplémentaires, comme une extrusion. Certains types, avoir un objet de base n\'est pas obligatoire ([Arch Structure](Arch_Structure/fr.md))

-    **Clone Of|Link**: tout composant Arch peut être un clone d\'un autre composant Arch du même type (un mur ne peut être qu\'un clone d\'un autre mur, etc.). La seule exception est le composant Arch générique (produit par cette commande), qui peut être un clone de tout autre type (mur, structure, fenêtre, etc.). Cela permet d\'utiliser un composant Arch générique pour remplacer le type d\'un autre composant Arch.

-    **Hi Res|Link**: les composants Arch peuvent utiliser la forme d\'un autre objet avec une résolution plus élevée. Pour cela, la propriété Hi Res et le mode d\'affichage Hi Res doivent être définis. Cela permet, par exemple, de créer un simple mur, puis de modéliser chaque brique qui compose le mur, par exemple avec un [Part Cube](Part_Box/fr.md). Ensuite, utilisez un composé de ces briques comme une version haute résolution du mur. La forme du mur n\'est pas modifiée en ajoutant un objet Hi-Res. Seule sa représentation dans la [vue 3D](3D_view/fr.md) changera en adoptant la représentation de la version haute résolution à la place de la sienne.

-    **Horizontal Area|Area**: la zone de projection de cet objet sur le plan XY (en lecture seule).

-    **Material|Link**: tous les composants Arch ont un emplacement Material, qui peut contenir un [matériau](Arch_SetMaterial/fr.md) ou un [multi-matériaux](Arch_MultiMaterial/fr.md) (tous les types d\'objets Arch ne supportent pas l\'utilisation d\'un [multi-matériaux](Arch_MultiMaterial/fr.md)). Les propriétés DiffuseColor et Transparency du matériau attaché définiront la couleur de la forme et la transparence du composant Arch. Le matériel sera importé et exporté vers [IFC](Arch_IFC/fr.md), [OBJ](Arch_OBJ/fr.md) et [DAE](Arch_DAE/fr.md).

-    **Move Base|Bool**: spécifie si le déplacement de cet objet déplace sa base à la place.

-    **Move With Host|Bool**: lorsqu\'un composant est incorporé dans un autre composant (par exemple une fenêtre à l\'intérieur d\'un mur), définir cette propriété à True fera bouger l\'objet et pivoter avec son objet hôte lorsqu\'il sera déplacé ou pivoté en utilisant [Draft Déplacer](Draft_Move/fr.md) ou [Draft Pivoter](Draft_Rotate/fr.md).

-    **Perimeter Length|Length**: longueur du périmètre de la surface horizontale (en lecture seule).

-    **Standard Code|String**: code standard optionnel (OmniClass, etc\...) pour ce composant.

-    **Subtractions|LinkList**: les composants Arch ont une propriété de soustraction, qui peut contenir une référence à un nombre quelconque d\'autres objets basés sur la [forme](Part_Workbench/fr.md). La forme de ces objets sera soustraite de la forme de base du composant pour produire la forme finale. Voir [Remarques](##Remarques.md).

-    **Vertical Area|Area**: surface de toutes les faces verticales de cet objet (en lecture seule).


{{TitleProperty|IFC}}

-    **Ifc Data|Map|Hidden**:

-    **Ifc Properties|Map|Hidden**:

-    **Ifc Type|Enumeration**: chaque composant Arch, en plus de la fonction définie par son type (mur, fenêtre, etc.), possède également une propriété Role, qui peut définir davantage le type de fonction qu\'il remplit. Par exemple, une [Arch Structure](Arch_Structure/fr.md) peut avoir un rôle de poutre ou de colonne. Les composants génériques d\'Arch (tels que produits par cette commande) peuvent avoir n\'importe quel rôle disponible dans l\'ensemble de l\'atelier d\'Arch. Le rôle est utilisé pour définir le type d\'objet IFC à exporter lorsque [exportation vers IFC](Arch_IFC/fr.md).


{{TitleProperty|IFC Attributes}}

-    **Description|String**: tous les composants Arch ont un champs Description, qui peut contenir n\'importe quel texte. Ceci est utilisé avec [exportation vers IFC](Arch_IFC/fr.md).

-    **Global Id|String**:

-    **Object Type|String**:

-    **Predefined Type|Enumeration**:

-    **Tag|Enumeration**: la propriété Tag est un autre champs de texte qui peut être utilisé pour donner une identité personnalisée supplémentaire aux objets.



## Remarques

-   Le placement d\'un composant Arch est appliqué après que les ajouts et soustractions ont été effectués, de sorte qu\'ils sont effectués par rapport à l\'objet de base à son emplacement de base. Ensuite, le résultat est déplacé à l\'emplacement du placement.

-   Les objets peuvent être ajoutés ou supprimés dans/à partir de listes Additions et Soustractions d\'un composant en sélectionnant à la fois l\'objet et le composant, et en utilisant les commandes [Arch Ajouter](Arch_Add/fr.md) ou [Arch Supprimer](Arch_Remove/fr.md), ou le panneau des tâches en double-cliquant sur le composant dans la [vue en arborescence](Tree_view/fr.md). Le panneau de tâches permet également de vérifier quel objet fait actuellement partie de ces listes.



---
⏵ [documentation index](../README.md) > Arch Component/fr
