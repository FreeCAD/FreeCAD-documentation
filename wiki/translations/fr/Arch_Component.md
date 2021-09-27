---
- GuiCommand:/fr
   Name:Arch Component
   Name/fr:Arch Composant
   MenuLocation:Arch → Utilitaires → Composant
   Workbenches:[Arch](Arch_Workbench/fr.md)
   Shortcut:**C** **M**
---

# Arch Component/fr

## Description

Crée un composant [Arch](Arch_Workbench/fr.md) non-paramétrique à partir de n\'importe quel objet [Part](Part_Workbench/fr.md). Cela donne un objet de base Part avec les mêmes attributs et propriétés que les autres objets Arch et permet de préciser comment il doit être exporté au format IFC en définissant sa propriété ou son *Rôle*.

## utilisation

1.  Sélectionnez un objet issu de [Atelier Part](Part_Workbench/fr.md)
2.  Lancer Arch Composant en utilisant plusieurs méthodes :
    -   En appuyant sur le bouton **<img src="images/Arch_Component.svg" width=16px>** dans la barre d\'outils.
    -   En utilisant le raccourci clavier **C** **M**.
    -   En faisant **Arch** → **Utilities** → **<img src="images/Arch_Component.svg" width=16px> [Composant](Arch_Component/fr.md)** depuis le menu supérieur.

## Propriétés communes aux composants Arch 

L\'objet Composant Arch est également une base partagée par tous les autres objets Arch (**<img src="images/Arch_Wall.svg" width=16px>[Mur](Arch_Wall/fr.md)**, **<img src="images/Arch_Structure.svg" width=16px>[Structure](Arch_Structure/fr.md)** etc.). Par conséquent, certaines de ses propriétés et comportements sont communs à tous les objets Arch (à l\'exception des outils qui ne produisent pas d\'objets solides, comme **<img src="images/Arch_SectionPlane.svg" width=16px>[Plan de section](Arch_SectionPlane/fr.md)** ou **<img src="images/Arch_Axis.svg" width=16px>[Axes](Arch_Axis/fr.md)**) :

-   **Base shape** : Les composants Arch sont toujours basés sur un objet de base de l\'[Atelier Part](Part_Workbench/fr.md). Certains types d\'objets Arch vont simplement utiliser la forme de base telle quelle, d\'autres (par exemple **<img src="images/Arch_Wall.svg" width=16px>[Mur](Arch_Wall/fr.md)**) effectueront des opérations supplémentaires, comme une extrusion. Certains types, ayant un objet de base n\'est pas obligatoire (**<img src="images/Arch_Structure.svg" width=16px>[Structure](Arch_Structure/fr.md)**)

-   **Additions** : Les composants Arch ont une propriété d\'addition, qui peut contenir une référence à un nombre quelconque d\'autres objets basés sur [Shape](Part_Workbench/fr.md). La forme de ces ajouts sera liée à la forme de base du composant, pour produire la forme finale.

-   **Subtractions** : Arch Les composants ont une propriété de soustraction, qui peut contenir une référence à un nombre quelconque d\'autres objets [Shape](Part_Workbench/fr.md). La forme de ces objets sera soustraite de la forme de base du composant, pour produire la forme finale.

-   Le placement du composant Arch est appliqué après que les ajouts et soustractions ont été effectués, de sorte qu\'ils sont effectués par rapport à l\'objet de base à son emplacement de base. Ensuite, le résultat est déplacé à l\'emplacement du placement.

-   Les objets peuvent être ajoutés ou supprimés dans/à partir de listes Additions et Soustractions d\'un composant en sélectionnant à la fois l\'objet et le composant, et en utilisant les commandes **<img src="images/Arch_Add.svg" width=16px>[Arch Ajouter](Arch_Add/fr.md)** ou **<img src="images/Arch_Remove.svg" width=16px> [Arch Soustraire](Arch_Remove/fr.md)** le panneau des tâches en double-cliquant sur le composant dans l\'arborescence. Le panneau de tâches permet également de vérifier quel objet fait actuellement partie de ces listes.

-   **Role** : En plus de la fonction définie par son type, chaque composant Arch, (wall, window, etc.), possède également une propriété Rôle, qui permet de définir plus précisément le type de fonction qu\'il effectue. Par exemple, une **<img src="images/Arch_Structure.svg" width=16px>[Structure](Arch_Structure/fr.md)** peut avoir un rôle de poutre ou de colonne. Les Generic Arch Components (produits par cette commande) peuvent avoir n\'importe quel rôle disponible dans l\'ensemble du plan de travail Arch. Le rôle est celui qui est utilisé pour définir le type d\'objet IFC lorsqu\'on utilise [exportation vers IFC](Arch_IFC/fr.md).

-   **Clone Of** : Tout composant Arch peut être un clone d\'un autre composant Arch du même type (un mur ne peut être qu\'un clone d\'un autre mur, etc.). La seule exception est le composant Arch générique (produit par cette commande), qui peut être un clone de tout autre type (Wall, structure, fenêtre, etc.). Cela permet d\'utiliser un composant Arch générique pour remplacer le type d\'un autre composant Arch.

-   **Description** : Tous les composants Arch ont un champs Description, qui peut contenir n\'importe quel texte. Ceci est utilisé avec [exporting to IFC](Arch_IFC/fr.md).

-   **Tag** : La propriété Tag est un autre champs de texte, qui peut être utilisé pour donner une identité personnalisée supplémentaire aux objets.

-   **Material** : Tous les composants Arch ont un emplacement Material, qui peut contenir un [Material](Arch_SetMaterial/fr.md) ou un [MultiMaterial](Arch_MultiMaterial/fr.md) (tous les types d\'objets Arch ne supportent pas l\'utilisation de MutiMaterials). Les propriétés DiffuseColor et Transparency du matériau attaché définiront la couleur du Shape et la transparence du composant Arch. Le matériel sera importé et exporté vers [IFC](Arch_IFC/fr.md), [OBJ](Arch_OBJ/fr.md) et [DAE](Arch_DAE/fr.md).

-   **Move with Host** : Lorsqu\'un composant est incorporé dans un autre (par exemple une fenêtre à l\'intérieur d\'un mur), définir cette propriété sur True fera bouger l\'objet et tournera avec son objet hôte lorsqu\'il sera déplacé ou pivoté en utilisant **<img src="images/Draft_Move.svg" width=16px> [Draft Déplacer](Draft_Move/fr.md)** or **<img src="images/Draft_Rotate.svg" width=16px> [Draft Rotation](Draft_Rotate/fr.md)**.

-   **Hi Res** : Les composants Arch peuvent utiliser la forme d\'un autre objet avec une résolution plus élevée. Pour cela, la propriété Hi Res et le mode d\'affichage Hi Res doivent être définis. Cela permet, par exemple, de créer un simple mur, puis de modéliser chaque brique qui compose le mur, par exemple avec **<img src="images/Part_Box.svg" width=16px> [Part Cube](Part_Box/fr.md)**. Ensuite, utilisez un composé de ces briques comme une version haute résolution du mur. La forme du mur n\'est pas modifiée en ajoutant un objet Hi-Res. Seule sa représentation dans la vue 3D changera en adoptant la représentation de la version haute résolution à la place de la sienne.

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Component/fr
