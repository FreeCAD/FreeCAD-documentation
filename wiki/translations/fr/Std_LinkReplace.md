---
 GuiCommand:
   Name: Std LinkReplace
   Name/fr: Std Remplacer par un lien
   MenuLocation: Aucun
   Workbenches: Tous
   Version: 0.19
   SeeAlso: Std_LinkMake/fr, Std_LinkMakeRelative/fr, Std_LinkUnlink/fr
---

# Std LinkReplace/fr

## Description


**[<img src=images/Std_LinkReplace.svg style="width:16px"> [Std Remplacer par un lien](Std_LinkReplace/fr.md)**

remplace un objet qui se trouve dans un autre objet par une version [App Link](App_Link/fr.md) du premier.

Cette opération agit sur les \"enfants\" d\'un objet \"parent\" comme vu dans la [vue en arborescence](Tree_view/fr.md). Par exemple, soient deux objets (A et B) qui participent à une opération **[<img src=images/Part_Boolean.svg style="width:16px"> [Part Booléenne](Part_Boolean/fr.md)**, disons C = A + B, l\'objet A peut être remplacé par un Link (Lien) de sorte que C = A_link + B.

Cette opération peut être effectuée pour remplacer des objets imbriqués qui sont dans un [assemblage](assembly/fr.md) complexe pour un lien, ce qui peut être plus efficace si cet objet imbriqué est utilisé plusieurs fois dans différents sous-assemblages. L\'opération inverse est **[<img src=images/Std_LinkUnlink.svg style="width:16px"> [Std Délier](Std_LinkUnlink/fr.md)**. Pour créer un lien générique voir **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std Créer un lien](Std_LinkMake/fr.md)**.



## Utilisation

1.  Assurez-vous que vous avez un objet dans un autre. Par exemple, considérez qu\'une **[<img src=images/Part_Fuse.svg style="width:16px"> [Part Union](Part_Fuse/fr.md)** a été utilisée avec deux objets créés, une **[<img src=images/Part_Sphere.svg style="width:16px"> [Part Sphère](Part_Sphere/fr.md)** et un **[<img src=images/Part_Cylinder.svg style="width:16px"> [Part Cylindre](Part_Cylinder/fr.md)**.
2.  Sélectionnez la <img alt="" src=images/Part_Sphere.svg  style="width:16px;"> [sphère](Part_Sphere/fr.md) dans la [vue en arborescence](Tree_view/fr.md).
3.  Appuyez sur **[<img src=images/Std_LinkReplace.svg style="width:16px"> [Remplacer par un lien](Std_LinkReplace/fr.md)**.

La <img alt="" src=images/Part_Sphere.svg  style="width:16px;"> [sphère](Part_Sphere/fr.md) d\'origine doit maintenant se trouver en dehors de la **[<img src=images/Part_Fuse.svg style="width:16px"> [Part Union](Part_Fuse/fr.md)** et il doit y avoir un lien à l\'intérieur à la place (une petite flèche superposée est affichée dans l\'icône).

![](images/Std_Link_tree_replace_fuse_1_example.png ) ![](images/Std_Link_tree_replace_fuse_2_example.png )



*Un objet à l'intérieur d'un autre est remplacé par un lien; le lien est maintenant à l'intérieur et l'objet réel est placé à l'extérieur.*

Cela peut également être fait avec des objets contenus dans des {{button|[<img src=images/Std_Part.svg style="width:16px"> [Std Parts](Std_Part/fr.md)}} et {{button|[<img src=images/Std_Group.svg style="width:16px"> [Std Groupes](Std_Group/fr.md)}}.

![](images/Std_Link_tree_replace_part_1_examples.png ) ![](images/Std_Link_tree_replace_part_2_examples.png )



*Un objet à l'intérieur d'un conteneur est remplacé par un lien ; le lien est maintenant à l'intérieur et l'objet réel est placé à l'extérieur.*



## Propriétés

Cette commande crée un nouveau [App Link](App_Link/fr.md). Ses propriétés sont décrites dans **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std Créer un lien](Std_LinkMake/fr.md)**.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std LinkReplace/fr
