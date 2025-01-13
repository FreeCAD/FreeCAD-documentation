---
 GuiCommand:
   Name: Std LinkSelectLinkedFinal
   Name/fr: Std Objet lié le plus profond
   MenuLocation: Affichage , Navigation par lien , Aller à l'objet lié le plus profond
   Workbenches: Tous
   Shortcut: **S** **D**
   Version: 0.19
   SeeAlso: Std_LinkSelectLinked/fr, Std_LinkSelectAllLinks/fr
---

# Std LinkSelectLinkedFinal/fr

## Description

La commande **Std Objet lié le plus profond** sélectionne **Linked Object**, l\'objet source, d\'un objet [App Link](App_Link/fr.md), un lien. Mais si cet objet source est également un lien, son objet lié est sélectionné à la place. Ceci est répété jusqu\'à ce que l\'objet lié ne soit pas un lien. Cet objet source final est l\'objet lié le plus profond.



## Utilisation

1.  Sélectionner un lien.
2.  Il y a plusieurs façons de lancer la commande :
    -   Sélectionnez l\'option **Affichage → Navigation par lien → <img src="images/Std_LinkSelectLinkedFinal.svg" width=16px> Aller à l'objet lié le plus profond** du menu.
    -   Sélectionnez l\'option **Actions sur les liens → <img src="images/Std_LinkSelectLinkedFinal.svg" width=16px> Aller à l'objet lié le plus profond** dans le menu contextuel de la [vue en arborescence](Tree_view/fr.md).
    -   Utilisez le raccourci clavier : **S** puis **D**.
3.  L\'objet source lié est sélectionné. Si cet objet appartient à un document externe, ce document est activé.
4.  Utiliser éventuellement <img alt="" src=images/Std_SelBack.svg  style="width:16px;"> [Std Sélection précédente](Std_SelBack/fr.md) pour resélectionner le lien.





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std LinkSelectLinkedFinal/fr
