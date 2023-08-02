---
- GuiCommand:
   Name: Std LinkUnlink
   Name/fr: Std Délier
   MenuLocation: Aucun
   Workbenches: Tous
   Version: 0.19
   SeeAlso: Std_LinkMake/fr, Std_LinkMakeRelative/fr, Std_LinkReplace/fr
---

# Std LinkUnlink/fr

## Description


**[<img src=images/Std_LinkUnlink.svg style="width:16px"> [Std Délier](Std_LinkUnlink/fr.md)**

est essentiellement l\'opération inverse à **[<img src=images/Std_LinkReplace.svg style="width:16px"> [Std Remplacer par un lien](Std_LinkReplace/fr.md)**.

Cette opération est utilisée pour supprimer un lien d\'un conteneur comme **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)** et placez à la place l\'objet réel à l\'intérieur.

## Utilisation

1.  Assurez-vous d\'avoir un lien à l\'intérieur d\'un conteneur, par exemple, un lien vers une **[<img src=images/Part_Sphere.svg style="width:16px"> [Part Sphère](Part_Sphere/fr.md)** à l\'intérieur d\'un **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)**.
2.  Sélectionnez le lien interne dans la [Vue en arborescence](Tree_view/fr.md).
3.  Appuyez sur **[<img src=images/Std_LinkUnlink.svg style="width:16px"> [Std Délier](Std_LinkUnlink/fr.md)**.

La <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:16px;"> [Sphère](Part_Sphere/fr.md) originale doit maintenant se trouver dans le **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)** et le lien doit être à l\'extérieur. Maintenant, ce lien peut être supprimé s\'il n\'est plus nécessaire et il ne cassera pas le conteneur.

![](images/Std_Link_tree_replace_1_example.png ) ![](images/Std_Link_tree_unlink_1_example.png )



*Un lien à l'intérieur d'un autre objet est dissocié et l'objet réel est placé à l'intérieur à la place.*

![](images/Std_Link_tree_replace_2_example.png ) ![](images/Std_Link_tree_unlink_2_example.png )



*Un lien à l'intérieur d'un groupe est dissocié et l'objet réel est placé à l'intérieur à la place.*





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std LinkUnlink/fr
