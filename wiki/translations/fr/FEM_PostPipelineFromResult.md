---
- GuiCommand   */fr
   Name   *FEM PostPipelineFromResult
   Name/fr   *FEM Pipeline à partir du résultat
   MenuLocation   *Résultats → Afficher le pipeline à partir du résultat
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   Version   *0.17
   SeeAlso   *[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM PostPipelineFromResult/fr

## Description

Pipeline est un objet résultat, qui crée une nouvelle représentation graphique des résultats de l\'analyse FEM sur la pièce analysée. Il ajoute une échelle de couleurs et des options d\'affichage.

## Utilisation

1.  Sélectionnez un objet résultat.
2.  Cliquez sur le bouton **<img src="images/FEM_PostPipelineFromResult.svg" width=16px>**, ou sélectionnez l\'option **Résultats → <img src="images/FEM_PostPipelineFromResult.svg" width=16px> Afficher le pipeline à partir du résultat** dans le menu.
3.  Un nouvel objet appelé \"Pipeline\" est ajouté à votre analyse.
4.  Double-cliquez sur le nouvel objet Pipeline dans la [Vue en arborescence](Tree_view/fr.md) et sélectionnez un mode d\'affichage et le champ de résultat. Par exemple, pour le mode {{Value|Surface}} et le champ {{Value|Contrainte de von Mises}}, le pipeline aura l\'aspect suivant    *

<img alt="" src=images/Pipeline.PNG  style="width   *500px;">

Si vous ne voyez aucun modèle dans la zone graphique, allez dans et activez **Edition → Préférences → Affichage → Vue 3D → Rendu → Couleur du rétroéclairage**.

Si vous utilisez un dérivé du [https   *//fr.wikipedia.org/wiki/Syst%C3%A8me\_international\_d%27unit%C3%A9s SI](https   *//fr.wikipedia.org/wiki/Syst%C3%A8me_international_d%27unit%C3%A9s_SI.md) du [système d\'unités](Preferences_Editor/fr#Unit.C3.A9s.md) de FreeCAD, les valeurs de l\'échelle de sortie sont également basées sur les unités SI. Cela signifie que le déplacement est en mètre, la contrainte est en Pascal et la température est en Kelvin.

## Propriétés

### Boîte de dialogue 

Cette Boîte de dialogue de pipeline a les paramètres suivants    *

-   **Mode**    * Comment dessiner les résultats. Les modes possibles sont
    -   **Outline**    * Le contour du maillage du résultat. En fait, n\'affiche aucun résultat mais seulement les bords du maillage.
    -   **Nodes**    * Les nœuds du maillage résultat
    -   **Surface**    * C\'est la valeur par défaut et elle affiche la surface de la maille résultante.
    -   **Surface with Edges**    * Comme **Surface** mais avec les bords du contour du maillage et les lignes de connexion des noeuds du maillage de surface.
-   **Champ**    * La propriété du résultat à dessiner.
-   **Vecteur**    * N\'est actif que si **Champ** est un vecteur. Vous pouvez choisir d\'afficher le vecteur *Magnitude* ou ses composantes X, Y, Z.

### Echelle

Si vous double-cliquez sur l\'échelle, vous obtenez cette boîte de dialogue de paramétrage    *

![](images/SIMTUT_05.PNG )

et vous pouvez ses propriétés    *

-   **Dégradé**    * Vous pouvez sélectionner l\'ordre inversé du gradient de couleur par défaut, *Rouge-Blanc-Bleu*, *Noir-Blanc* ou *Blanc-Noir*.
-   **Style**    * L\'option par défaut *Flux* utilise la gamme complète des dégradés de couleurs. L\'option *Zéro* n\'utilise que la gamme de couleurs du gradient en partant de la couleur qui afficherait la valeur moyenne jusqu\'au maximum.
-   **Visibilité**    * L\'option *Sortie griséee* colorera en gris tous les nœuds de la maille dont les valeurs sont en dehors de la plage minimum/maximum définie. L\'option *Sortie transparente* rendra ces mailles transparentes.
-   **Gamme de paramètres**    * Les valeurs minimales et maximales sont remplies automatiquement. Vous pouvez les modifier, cependant assurez-vous de savoir ce que vous faites. Vous pouvez également modifier le nombre de décimales affichées et le nombre d\'étiquettes réparties sur la plage de paramètres.

### Éditeur de propriétés 

Dans l\'[éditeur de propriétés](Property_editor/fr.md), vous pouvez définir dans l\'onglet *Vue* les paramètres de la boîte de dialogue. Dans l\'onglet *Données*, vous pouvez également définir ces paramètres    *

-    **Mode**   * Comment les filtres utilisés dans le pipeline seront traités. Ces modes possibles sont    *

    -   **Serial**    * Dans ce mode, chaque filtre prend le filtre précédent comme entrée. L\'ordre est donc l\'ordre de création. Le premier filtre créé prend le pipeline en entrée. Sa propriété **Input** est donc vide.
    -   **Parallel**    * Dans ce mode, tous les filtres prennent le pipeline en entrée.
    -   **Custom**    * {{Version/fr|0.20}} C\'est le mode par défaut et il garde les entrées des filtres telles qu\'elles sont. Il permet donc d\'avoir, par exemple, deux filtres qui prennent le pipeline en entrée, et un troisième filtre qui prend l\'un des deux filtres en entrée.

## Limitations

La représentation en pipeline des résultats (appelée VTK) sur la partie affichée est différente des résultats en gradient de couleur qui sont visibles lorsque vous terminez la solution. Les valeurs de l\'échelle de gradient ne peuvent pas être appliquées à l\'objet de résultat de solution.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostPipelineFromResult/fr
