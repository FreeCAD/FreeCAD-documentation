---
 GuiCommand:
   Name: FEM PostPipelineFromResult
   Name/fr: FEM Pipeline de résultats
   MenuLocation: Résultats , Afficher le pipeline des résultats
   Workbenches: FEM_Workbench/fr
   Version: 0.17
   SeeAlso: FEM_ResultShow/fr, FEM_tutorial/fr
---

# FEM PostPipelineFromResult/fr

## Description

Pipeline est un objet résultat, qui crée une nouvelle représentation graphique des résultats de l\'analyse FEM sur la pièce analysée. Il ajoute une échelle de couleurs et des options d\'affichage.



## Utilisation

1.  Sélectionnez un objet résultat.
2.  Cliquez sur le bouton **<img src="images/FEM_PostPipelineFromResult.svg" width=16px> '''Afficher le pipeline des résultats'''** ou sélectionnez l\'option **Résultats → <img src="images/FEM_PostPipelineFromResult.svg" width=16px> Afficher le pipeline des résultats** dans le menu.
3.  Un nouvel objet appelé \"Pipeline\" est ajouté à votre analyse.
4.  Double-cliquez sur le nouvel objet Pipeline dans la [vue en arborescence](Tree_view/fr.md). Sélectionnez un mode d\'affichage et le champ de résultat. Par exemple, pour le mode {{Value|Surface}} et le champ {{Value|Contrainte de von Mises}}, le pipeline aura l\'aspect suivant :

<img alt="" src=images/Pipeline.PNG  style="width:500px;">

Si vous ne voyez aucun modèle dans la zone graphique, allez dans et activez **Édition → Préférences → Affichage → Vue 3D → Rendu → Couleur du rétroéclairage**.

Si vous utilisez un [système d\'unités](Preferences_Editor/fr#Unit.C3.A9s.md) de FreeCAD dérivé du [Système international d\'unités](https://fr.wikipedia.org/wiki/Syst%C3%A8me_international_d%27unit%C3%A9s), les valeurs de l\'échelle de sortie seront également basées sur les unités du système international d\'unités. Cela signifie que le déplacement est en mètre, la contrainte est en Pascal et la température est en Kelvin.



## Propriétés



### Boîte de dialogue 

Cette boîte de dialogue du pipeline a les paramètres suivants :

-   **Mode** : comment dessiner les résultats. Les modes possibles sont:
    -   **Contour** : le contour du maillage du résultat. En fait, n\'affiche aucun résultat mais seulement les bords du maillage.
    -   **Nœuds** : les nœuds du maillage résultant.
    -   **Surface** : valeur par défaut et elle affiche la surface de la maille résultante.
    -   **Surface avec bords** : comme **Surface** mais avec les bords du contour du maillage et les lignes de connexion des noeuds du maillage de surface.
-   **Champ** : propriété du résultat à dessiner.
-   **Vecteur** : n\'est actif que si **Champ** est un vecteur. Vous pouvez choisir d\'afficher le vecteur *Magnitude* ou ses composantes X, Y, Z.



### Échelle

Si vous double-cliquez sur l\'échelle, vous obtenez cette boîte de dialogue de paramétrage :

![](images/SIMTUT_05.PNG )

et vous pouvez modifier ces propriétés :

-   **Dégradé** : vous pouvez sélectionner l\'ordre inversé du gradient de couleur par défaut, *Rouge-Blanc-Bleu*, *Noir-Blanc* ou *Blanc-Noir*.
-   **Style** : l\'option par défaut *Flow* utilise la gamme complète des dégradés de couleurs. L\'option *Zero* n\'utilise que la gamme de couleurs du gradient en commençant par la couleur qui afficherait la valeur moyenne jusqu\'au maximum.
-   **Visibilité** : l\'option *Sortie griséee* colorera en gris tous les nœuds de la maille dont les valeurs sont en dehors de la plage minimum/maximum définie. L\'option *Sortie transparente* rendra ces mailles transparentes.
-   **Plage de paramètres** : les valeurs minimales et maximales sont remplies automatiquement. Vous pouvez les modifier, cependant assurez-vous de savoir ce que vous faites. Vous pouvez également modifier le nombre de décimales affichées et le nombre d\'étiquettes réparties sur la plage de paramètres.



### Éditeur de propriétés 

Dans l\'[éditeur de propriétés](Property_editor/fr.md), vous pouvez définir dans l\'onglet *Vue* les paramètres de la boîte de dialogue. Dans l\'onglet *Données*, vous pouvez également définir ces paramètres :

-    **Mode**: comment les filtres utilisés dans le pipeline seront traités. Les modes possibles sont :

    -   **Serial** : dans ce mode, chaque filtre prend le filtre précédent comme entrée. L\'ordre est donc l\'ordre de création. Le premier filtre créé prend le pipeline en entrée. Sa propriété **Input** est donc vide.
    -   **Parallel** : dans ce mode, tous les filtres prennent le pipeline en entrée.
    -   **Custom** : {{Version/fr|0.20}} mode par défaut, il garde les entrées des filtres telles qu\'elles sont. Il permet donc d\'avoir, par exemple, deux filtres qui prennent le pipeline en entrée, et un troisième filtre qui prend l\'un des deux filtres en entrée.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostPipelineFromResult/fr
