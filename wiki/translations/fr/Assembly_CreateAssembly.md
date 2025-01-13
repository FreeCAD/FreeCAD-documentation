---
 GuiCommand:
   Name: Assembly CreateAssembly
   Name/fr: Assembly Assemblage
   MenuLocation: Assemblage , Créer un assemblage
   Workbenches: Assembly_Workbench/fr
   Shortcut: **A**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateAssembly/fr

## Description

L\'outil <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Assembly Assemblage](Assembly_CreateAssembly/fr.md) crée un assemblage racine (objet Assemblage) dans le document en cours ou un sous-assemblage d\'un assemblage actif préexistant. Un document ne peut contenir qu\'un seul assemblage racine.

Chaque objet Assembly est créé avec un objet [Origin](App_OriginGroupExtension/fr.md) et un conteneur Joints vide par défaut.



## Utilisation

1.  Si le document contient déjà un ou plusieurs assemblages : activer un assemblage.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Assembly_CreateAssembly.svg" width=16px> [Créer un assemblage](Assembly_CreateAssembly/fr.md)**.
    -   Sélectionnez l\'option **Assemblage → <img src="images/Assembly_CreateAssembly.svg" width=16px> Créer un assemblage** du menu.
    -   Utilisez le raccourci clavier : **A**.
3.  Un nouvel objet Assembly est créé, soit dans le document, soit dans l\'assemblage activé.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet **Assembly**, ou formellement un {{Incode|Assembly::AssemblyObject}}, possède les propriétés suivantes :



### Données


{{TitleProperty|Base}}

-    **Type|String**:

-    **Material|Link**:

-    **Meta|Map|Hidden**:

-    **Id|String**:

-    **Uid|UUID|Hidden**:

-    **License|String**:

-    **License URL|String**:

-    **Color|Color**:

-    **Placement|Placement**:

-    **Label|String**:

-    **Label2|String|Hidden**:

-    **Expression Engine|ExpressionEngine|Hidden**:

-    **Visibility|Bool|Hidden**:

-    **Origin|Link|Hidden**:

-    **Group|LinkList**:

-    **_ Group Touched|Bool|Hidden**:



### Vue


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: {{value|Group}} (la seule option pour l\'instant).

-    **Show In Tree|Bool**: {{value|true}} par défaut.

-    **Visibility|Bool**: {{value|true}} par défaut.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**:

-    **Selection Style|Enumeration**:





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateAssembly/fr
