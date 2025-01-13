---
 GuiCommand:
   Name: Std DlgParameter
   Name/fr: Std Éditeur de paramètres
   MenuLocation: Outils , Éditer les paramètres...
   Workbenches: Tous
   SeeAlso: Preferences_Editor/fr 
---

# Std DlgParameter/fr

## Description

La commande **Std Éditeur des paramètres** ouvre l\'éditeur de paramètres. Dans l\'éditeur de paramètres, les paramètres qui contrôlent le comportement de FreeCAD et de ses ateliers peuvent être inspectés et éventuellement supprimés, ajoutés ou modifiés. Les paramètres sont stockés dans un fichier appelé **user.cfg**, l\'emplacement de ce fichier dépend de votre système d\'exploitation.

L\'utilisation de l\'éditeur de paramètres requiert une certaine expérience. Pour les paramètres les plus courants, il est préférable d\'utiliser l\'[éditeur de préférences](Preferences_Editor/fr.md).

![](images/Std_DlgParameter_dialog.png ) 
*La fenêtre de dialogue de l'éditeur de paramètres*



## Utilisation

1.  Sélectionnez l\'option **Outils → <img src="images/Std_DlgParameter.svg" width=16px> Éditer les paramètres...** du menu.
2.  La fenêtre de dialogue **Éditeur de paramètres** s\'ouvre. Pour plus d\'informations, voir [Options](#Options.md).
3.  Appuyez sur le bouton **Sauvegarder sur le disque** pour mettre à jour immédiatement le fichier **user.cfg**. Cela n\'est pas nécessaire car FreeCAD mettra automatiquement à jour ce fichier à la fermeture de l\'application.
4.  Appuyez sur le bouton **Fermer** pour fermer la fenêtre de dialogue et terminer la commande.

## Options



### Panneau gauche 

Le panneau de gauche montre une arborescence avec des groupes de paramètres et des sous-groupes.

*Les options suivantes sont disponibles dans le menu contextuel du panneau :*



#### Développer/réduire

1.  Si un groupe sélectionné possède un ou plusieurs sous-groupes, il peut être développé ou réduit en choisissant cette option dans le menu contextuel. Mais vous pouvez également développer et réduire l\'arbre de la manière habituelle.



#### Ajouter un sous-groupe 

1.  Sélectionnez un groupe.
2.  Sélectionnez l\'option **Ajouter un sous-groupe** dans le menu contextuel.
3.  Entrez un nom pour le nouveau sous-groupe dans la boîte de dialogue qui s\'ouvre.
4.  Appuyez sur le bouton **OK**.



#### Supprimer un groupe 

1.  Sélectionnez un groupe.
2.  Sélectionnez l\'option **Supprimer le groupe** dans le menu contextuel.
3.  Appuyez sur le bouton **Oui** dans la fenêtre de dialogue qui s\'ouvre pour confirmer que vous souhaitez supprimer le groupe (y compris tous ses sous-groupes et tous les paramètres du groupe et de ses sous-groupes).



#### Renommer un groupe 

1.  Sélectionnez un groupe.
2.  Sélectionnez l\'option **Renommer le groupe** dans le menu contextuel.
3.  Saisissez un nouveau nom.
4.  Un groupe peut également être renommé en double-cliquant dessus.



#### Exporter un paramètre 

1.  Sélectionnez un groupe.
2.  Sélectionnez l\'option **Exporter le paramètre** dans le menu contextuel.
3.  Entrez un nom de fichier dans la boîte de dialogue.
4.  Appuyez sur le bouton **Sauvegarder**.



#### Importer un paramètre 

1.  Sélectionnez un groupe qui ne contient aucun sous-groupe ou supprimez-les d\'abord. Tous les paramètres existants du groupe seront perdus.
2.  Sélectionnez l\'option **Importer le paramètre** dans le menu contextuel.
3.  Sélectionnez un fichier \*.FCParam dans la boîte de dialogue.
4.  Appuyez sur le bouton **Ouvrir**.



### Panneau droit 

Le panneau droit affiche les paramètres du groupe sélectionné dans le panneau gauche. Si ce groupe ne contient que des sous-groupes, le panneau de droite sera vide.

*Les options suivantes sont disponibles dans le menu contextuel du panneau :*



#### Modifier une valeur 

1.  Sélectionnez un paramètre.
2.  Sélectionnez l\'option **Changer la valeur** dans le menu contextuel.
3.  Entrez une nouvelle valeur dans la fenêtre de dialogue qui s\'ouvre.
4.  Appuyez sur le bouton **OK**.
5.  La valeur d\'un paramètre peut également être modifiée en double-cliquant sur son champ \"Type\" ou \"Valeur\".



#### Supprimer une clé 

1.  Sélectionnez un paramètre.
2.  Sélectionnez l\'option **Supprimer la clé** dans le menu contextuel.



#### Renommer une clé 

1.  Sélectionnez un paramètre.
2.  Sélectionnez l\'option **Renommer la clé** dans le menu contextuel.
3.  Saisissez un nouveau nom.
4.  Un paramètre peut également être renommé en double-cliquant sur son champ \"Nom\".



#### Nouvelle chaîne de caractère 

1.  Sélectionnez l\'option **Nouvelle chaîne de caractère** ou **Nouveau → Nouvelle chaîne de caractère** dans le menu contextuel.
2.  Saisissez un nom dans la fenêtre de dialogue qui s\'ouvre.
3.  Appuyez sur le bouton **OK**.
4.  Entrez une valeur dans la fenêtre de dialogue suivante.
5.  Appuyez sur le bouton **OK**.



#### Nouvelle variable flottante 

1.  Sélectionnez l\'option **Nouvelle variable flottante** ou **Nouveau → Nouvelle variable flottante** dans le menu contextuel.
2.  Les étapes suivantes sont similaires à celles d\'un [nouvelle chaîne de caractère](#Nouvelle_chaîne_de_caractère.md)



#### Nouvelle variable entière 

1.  Sélectionnez l\'option **Nouvelle variable entière** ou **Nouveau → Nouvelle variable entière** dans le menu contextuel.
2.  Les étapes suivantes sont similaires à celles d\'une [nouvelle chaîne de caractère](#Nouvelle_chaîne_de_caractère.md).



#### Nouvelle variable non signée 

1.  Sélectionnez l\'option **Nouvelle variable non signée** ou **Nouveau → Nouvelle variable non signée** dans le menu contextuel.
2.  Les étapes suivantes sont similaires à celles d\'une [nouvelle chaîne de caractère](#Nouvelle_chaîne_de_caractère.md).



#### Nouvelle variable booléenne 

1.  Sélectionnez l\'option **Nouvelle variable booléenne** ou **Nouveau → Nouvelle variable booléenne** dans le menu contextuel.
2.  Les étapes suivantes sont similaires à celles d\'une [nouvelle chaîne de caractère](#Nouvelle_chaîne_de_caractère.md).



### Tri

Par défaut, les groupes de chaque niveau d\'arborescence du panneau de gauche sont triés par ordre alphabétique et les paramètres du panneau de droite sont également triés par ordre alphabétique. Mais l\'ordre dans chaque panneau peut être inversé en cliquant respectivement sur l\'en-tête \"Groupe\" ou \"Nom\".



### Recherche rapide 

La saisie d\'une chaîne (partielle) dans cette zone de saisie développera complètement l\'arborescence dans le panneau de gauche et mettra en surbrillance tous les groupes dont les noms correspondent à la valeur entrée. Si aucune correspondance n\'est trouvée, l\'arrière-plan de la zone de saisie devient rouge.



### Rechercher

1.  Dans le panneau de gauche, sélectionnez le groupe dans lequel vous souhaitez commencer votre recherche. La direction de recherche est en baisse. La recherche n\'est pas limitée au groupe et à ses sous-groupes, mais plutôt au groupe sélectionné et à tout ce qui se trouve en dessous dans l\'arborescence sera recherché.
2.  Appuyez sur le bouton **Rechercher...**.
3.  Saisissez une chaîne dans la zone de saisie **Ce qu\'il faut rechercher**. La recherche est insensible à la casse.
4.  Cochez une ou plusieurs des cases **Groupes**, **Noms** et **Valeurs**. Notez que seules les valeurs de chaîne seront recherchées.
5.  Facultativement (décochez) la case **Ne faire correspondre que la chaîne complète**.
6.  Appuyez sur le bouton **Recherche le suivant** pour sélectionner le premier groupe avec une correspondance. Les paramètres correspondants ne sont pas mis en évidence individuellement. Vous pouvez répéter cette opération jusqu\'à ce qu\'aucune autre correspondance ne soit trouvée.
7.  Il est possible de lancer une nouvelle recherche sans fermer la boîte de dialogue. Une fois encore, la sélection du groupe à partir duquel commencer la recherche est généralement requise.
8.  Utilisez le bouton **Annuler** pour fermer la fenêtre de dialogue.



## Remarques

-   La page [Réglage fin](Fine-tuning/fr.md) répertorie un certain nombre de paramètres qui peuvent être intéressants.



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Les préférences sont accessibles à partir des scripts Python en utilisant leur chemin correspondant dans l\'[éditeur des paramètres](Std_DlgParameter/fr.md). Par exemple, la préférence **Édition → Préférences → Import-Export → DXF → Options d'Import → Joindre la géométrie** apparaît dans **Outils → Éditeur de paramètres → BaseApp → Préférences → Mod → Draft → dxfCreatePart** et a le type `Boolean`. Il est donc accessible en Python à l\'aide du code suivant :


```python
# get:
App.ParamGet("User parameter:BaseApp/Preferences/Mod/Draft").GetBool('dxfCreatePart')
# set:
App.ParamGet("User parameter:BaseApp/Preferences/Mod/Draft").SetBool('dxfCreatePart', True)
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std DlgParameter/fr
