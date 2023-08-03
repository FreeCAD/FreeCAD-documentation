---
 GuiCommand:
   Name: Std LinkSelectLinkedFinal
   Name/fr: Std Lien objet lié primaire
   MenuLocation: ''Aucun''
   Workbenches: Tous
   Version: 0.19
   SeeAlso: Std_LinkSelectLinked/fr, Std_LinkSelectAllLinks/fr, Std_SelBack/fr, Std_SelForward/fr
---

# Std LinkSelectLinkedFinal/fr

## Description

La commande **Std Lien objet lié primaire** sélectionne {{PropertyData/fr|Linked Object}}, l\'objet source, d\'un objet [App Link](App_Link/fr.md), un lien. Mais si cet objet source est également un lien, son objet lié est sélectionné à la place. Ceci est répété jusqu\'à ce que l\'objet lié ne soit pas un lien. Cet objet source final est l\'objet lié le plus profond.



## Utilisation

1.  Sélectionnez un lien.
2.  Sélectionnez l\'option **Actions sur les liens → <img src="images/Std_LinkSelectLinkedFinal.svg" width=16px> Aller à l'objet lié le plus lointain** dans le menu contextuel de la [Vue en arborescence](Tree_view/fr.md).
3.  L\'objet lié le plus profond est sélectionné. Si cet objet appartient à un document externe, ce document est activé.
4.  Utilisez éventuellement **<img src="images/Std_SelBack.svg" width=16px> [Std Rétablir](Std_SelBack/fr.md)** pour resélectionner le lien.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std LinkSelectLinkedFinal/fr
