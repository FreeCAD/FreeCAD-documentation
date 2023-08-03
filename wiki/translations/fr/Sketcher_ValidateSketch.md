---
 GuiCommand:
   Name: Sketcher ValidateSketch
   Name/fr: Sketcher Valider l'esquisse
   MenuLocation: Esquisse , Valider l'esquisse...
   Workbenches: Sketcher_Workbench/fr, PartDesign_Workbench/fr
   SeeAlso: Sketcher_ConstrainCoincident/fr, Topological_naming_problem/fr
---

# Sketcher ValidateSketch/fr

## Description

L\'utilitaire **Valider l\'esquisse** permet d\'analyser et de réparer une esquisse qui n\'est plus modifiable ou d\'ajouter des [contraintes de coïncidence](Sketcher_ConstrainCoincident/fr.md) manquantes à une esquisse créée à partir de géométrie importée, par exemple de fichiers DXF. Il peut aussi être utile pour localiser une coïncidence manquante à une esquisse native qui génère une erreur \"can\'t validate broken face\" (ne peut pas valider une face cassée) en tentant d\'appliquer une fonction PartDesign à celle-ci.

![](images/Sketcher_ValidateSketch_taskpanel.png ) 
*Le panneau des tâches de validation de Sketcher*

## Utilisation

1.  Cet outil ne peut pas être utilisé sur une esquisse en mode édition. Si nécessaire, quittez le mode d\'édition en effectuant l\'une des opérations suivantes :
    -   Appuyez sur le bouton **[<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [Quitter l'esquisse](Sketcher_LeaveSketch/fr.md)**.
    -   Appuyez sur le bouton **Fermer** en haut du [Panneau des tâches](Task_panel/fr.md).
    -   Utilisez le raccourci clavier : **Echap** (si activé dans [Sketcher Préférences](Sketcher_Preferences/fr#G.C3.A9n.C3.A9ral.md)).
2.  Sélectionnez l\'esquisse à valider dans la [Vue en arborescence](Tree_view/fr.md) ou en cliquant sur l\'une de ses arêtes dans la [Vue 3D](3D_view/fr.md).
3.  Pour ouvrir l\'utilitaire de validation d\'esquisse, effectuez l\'une des opérations suivantes :
    -   Sélectionnez l\'option **Esquisse → Valider l'esquisse...** dans le menu.
    -   Appuyez sur le bouton **[<img src=images/Sketcher_ValidateSketch.svg style="width:16px"> [Valider l'esquisse](Sketcher_ValidateSketch/fr.md)** (non disponible dans l\'[atelier PartDesign](PartDesign_Workbench/fr.md)).
4.  Voir [Options](#Options.md) ci-dessous pour les opérations disponibles.
5.  Appuyez sur le bouton **Fermer** lorsque vous avez terminé.

## Options

### Coincidences manquantes 

Trouve les coïncidences manquantes pour les sommets qui se chevauchent et les ajoute. Appuyez sur le bouton **Rechercher**. une boîte de dialogue apparaîtra pour indiquer combien de coïncidences manquantes ont été trouvées ; elles seront affichées dans la vue 3D sous forme de croix jaunes. Appuyez sur **OK** pour fermer la boîte de dialogue, puis appuyez sur le bouton **Réparer** pour ajouter les coïncidences manquantes.

Si nécessaire, définissez une valeur de tolérance supérieure dans le champ déroulant.

Appuyez sur **Surligner les sommets posant problème** pour mettre en évidence les sommets qui sont en dehors de cette tolérance.

Cette tolérance est utilisée par le processus **Rechercher**/**Réparer**.

Laissez la case à cocher \"Ignorer les géométries de construction\" cochée pour ignorer la géométrie de construction dans l\'analyse.

### Contraintes non valides 

Vérifie les contraintes mal faites.

Par exemple, s\'il y a une contrainte Cercle-Ligne-Tangente mais qu\'elle fait référence à deux lignes, elle est considérée comme non valable.

(Cela se produit parfois en raison du [problème de dénomination topologique](Topological_naming_problem/fr.md), c\'est-à-dire que la géométrie externe change de type).

Effectue également d\'autres contrôles, par exemple pour les liens vides.

### Géométrie dégénérée 

Une géométrie dégénérée peut résulter des actions du solveur dans une esquisse.

Par exemple, si une ligne est obligée de se raccourcir pour devenir presque un point.

Autres exemples : une ligne de longueur zéro ou un cercle/arc de rayon zéro.

### Géométrie externe inversée 

Une géométrie externe inversée peut se produire parce que le traitement de la géométrie inversée a été modifié autour de la révision 0.15.

Ce processus peut être utile si les esquisses à géométrie externe ne peuvent être résolues en raison de ces changements.

### Contrainte de verrouillage d\'orientation 

Les contraintes tangentes et perpendiculaires sont mises en œuvre (via-point).

En interne, elles fonctionnent en contraignant l\'angle entre les vecteurs tangents. Avec une contrainte de tangente par exemple, l\'angle peut être de 0 ou 180 degrés (vecteurs co-dirigés ou opposés). L\'angle réel est mémorisé dans les données de contrainte (\"l\'orientation de la contrainte est verrouillée\"), cela protège contre le retournement. Mais l\'angle peut être effacé (\"déverrouillage d\'orientation de la contrainte\") ou mis à jour. Ces outils font exactement cela.

Le mécanisme de verrouillage fonctionne généralement bien et cet outil ne devrait pas être nécessaire. **Il ne doit être utilisé qu\'après avoir effectué une sauvegarde du document ouvert.**





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ValidateSketch/fr
