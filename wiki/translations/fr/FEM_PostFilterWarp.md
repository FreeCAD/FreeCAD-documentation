---
 GuiCommand:
   Name: FEM PostFilterWarp
   Name/fr: FEM Filtre des déformations
   MenuLocation: Résultats , Filtre des déformations
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_PostPipelineFromResult/fr, FEM_tutorial/fr
---

# FEM PostFilterWarp/fr

## Description

Affiche la forme déformée du modèle en utilisant un facteur d\'échelle spécifié. Par conséquent, un filtre des déformations n\'a d\'effet que pour les vecteurs de résultat qui déforment la forme.

Le résultat sera le même qu\'avec le curseur *Déplacement* de la boîte de dialogue d\'[Afficher les résultats](FEM_ResultShow/fr.md) avec la différence que le déplacement est pour le filtre des déformations dans l\'unité de mesure SI. Par exemple, si vous utilisez un [système d\'unités](Preferences_Editor/fr#Unit.C3.A9s.md) où l\'unité de longueur est le mm et que vous définissez un facteur de déplacement de 100 dans le dialogue d\'[Afficher les résultats](FEM_ResultShow/fr.md), vous devez définir pour le filtre des déformations un facteur de 100.000 pour obtenir le même résultat.

![](images/FEM_Warp-Filter-Example.gif )

*Un filtre des déformations du déplacement d\'une poutre immobilisée d\'un côté.*



## Utilisation

1.  Sélectionnez un [pipeline de résultats](FEM_PostPipelineFromResult/fr.md) précédemment créé.
2.  Lancez la commande soit en :
    -   Appuyant sur le bouton **<img src="images/FEM_PostFilterWarp.svg" width=16px> '''Filtre des déformations'''**.
    -   Utiliser le menu **Résultats → <img src="images/FEM_PostFilterWarp.svg" width=16px> Filtre des déformations**.
3.  Ajustez les **Résultats** options d\'affichage comme pour le [Pipeline de résultats](FEM_PostPipelineFromResult/fr.md). Masquez ce pipeline pour voir l\'effet d\'un filtre des déformations.
4.  Spécifiez directement le **Facteur de déformation** ou utilisez le curseur pour le définir. Les champs **Déformation mini** et **Déformation max** vous permettent de régler la plage du curseur.
5.  Cliquez sur le bouton **OK** pour terminer la commande.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterWarp/fr
