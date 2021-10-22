---
- GuiCommand:/fr
   Name:Std LinkReplace
   Name/fr:Std Remplacer par un lien
   MenuLocation:Aucun
   Workbenches:Tous
   Version:0.19
   SeeAlso:[Std Créer un lien](Std_LinkMake/fr.md), [Std Créer un lien relatif](Std_LinkMakeRelative/fr.md), [Std Délier](Std_LinkUnlink/fr.md)
---

# Std LinkReplace/fr

## Description


**<img src=images/Std_LinkReplace.svg style="width:16px"> [Std Remplacer par un lien](Std_LinkReplace/fr.md)**

remplace un objet qui se trouve dans un autre objet pour une version [App Link](App_Link/fr.md) de l\'ancien.

Cette opération agit sur les \"enfants\" d\'un objet \"parent\" comme vu dans la <img src=images/Part_Boolean.svg style="width:Vue en arborescence](Tree_view/fr.md). Par exemple, étant donné deux objets (A et B) qui participent à une opération **[16px"> [Part Booléenne](Part_Boolean/fr.md)**, disons C = A + B, l\'objet A peut être remplacé par un Link (Lien) de sorte que C = A_link + B.

Cette opération peut être effectuée pour remplacer des objets imbriqués qui sont dans un <img src=images/Std_LinkUnlink.svg style="width:assemblage](assembly/fr.md) complexe pour un lien, ce qui peut être plus efficace si cet objet imbriqué est utilisé plusieurs fois dans différents sous-assemblages. L\'opération inverse est **[16px"> <img src=images/Std_LinkMake.svg style="width:Std Délier](Std_LinkUnlink/fr.md)**. Pour créer un lien générique voir **[16px"> [Std Créer un lien](Std_LinkMake/fr.md)**.

## Utilisation

1.  Assurez-vous que vous avez un objet dans un autre. Par exemple, considérez qu\'une **<img src=images/Part_Fuse.svg style="width:16px"> <img src=images/Part_Sphere.svg style="width:Part Union](Part_Fuse/fr.md)** a été utilisée avec deux objets précédemment créés, une **[16px"> <img src=images/Part_Cylinder.svg style="width:Part Sphère](Part_Sphere/fr.md)** et un **[16px"> [Part Cylindre](Part_Cylinder/fr.md)**.
2.  Sélectionnez <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:16px;"> [Sphère](Part_Sphere/fr.md) dans la [Vue en arborescence](Tree_view/fr.md).
3.  Appuyez sur **<img src=images/Std_LinkReplace.svg style="width:16px"> [Std Remplacer par un lien ](Std_LinkReplace/fr.md)**.

La <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:16px;"> <img src=images/Part_Fuse.svg style="width:Sphère](Part_Sphere/fr.md) originale doit maintenant se trouver en dehors de **[16px"> [Part Union](Part_Fuse/fr.md)** ; et à l\'intérieur, il doit y avoir un Lien à la place (une petite flèche superposée est affichée dans l\'icône).

![](images/Std_Link_tree_replace_fuse_1_example.png ) ![](images/Std_Link_tree_replace_fuse_2_example.png )



*Un objet à l'intérieur d'un autre est remplacé par un lien; le lien est maintenant à l'intérieur et l'objet réel est placé à l'extérieur.*

Cela peut également être fait avec des objets contenus dans des {{button|<img src=images/Std_Part.svg style="width:16px"> <img src=images/Std_Group.svg style="width:Std Parts](Std_Part/fr.md)}} et {{button|[16px"> [Std Groupes](Std_Group/fr.md)}}.

![](images/Std_Link_tree_replace_part_1_examples.png ) ![](images/Std_Link_tree_replace_part_2_examples.png )



*Un objet à l'intérieur d'un conteneur est remplacé par un lien ; le lien est maintenant à l'intérieur et l'objet réel est placé à l'extérieur.*

## Propriétés

Cette commande crée un nouveau <img src=images/Std_LinkMake.svg style="width:App Link](App_Link/fr.md). Ses propriétés sont décrites dans **[16px"> [Std Créer un lien](Std_LinkMake/fr.md)**.





{{Std Base navi

}}

---
[documentation index](../README.md) > Std LinkReplace/fr
