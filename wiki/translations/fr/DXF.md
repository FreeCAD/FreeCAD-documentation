# DXF/fr
## Historique

Le Drawing Exchange Format (DXF) est un format de données CAO propriétaire développé par Autodesk pour permettre l\'échange de fichiers entre son produit phare AutoCAD et d\'autres logiciels. Il existe un certain nombre de bonnes bibliothèques logicielles pour lire/écrire le format DXF.

Il existe de nombreuses versions du format DXF. Vous entendrez parler de certaines versions clés, comme la R12 (de 1992) ou la R14 (de 1997, qui comportait des splines). Les versions ultérieures du format DXF comportent des éléments 3D mais ceux-ci sont rarement utilisés ou mis en œuvre. La façon dont vous utilisez DXF pour partager des données CAO entre programmes dépend principalement des limitations et des bogues des lecteurs/importateurs et des rédacteurs/exportateurs correspondants. Ceux-ci sont rarement bien documentés et peuvent être une grande source de frustration.

Si vous éditez des fichiers DXF et que vous souhaitez qu\'ils restent quasiment identiques lorsque vous les enregistrez, nous vous recommandons d\'utiliser [LibreCAD](https://fr.wikipedia.org/wiki/LibreCAD) ou [QCad](https://fr.wikipedia.org/wiki/QCad) car les structures de données internes de ces programmes sont compatibles avec les objets du fichier DXF.

Dans FreeCAD, les lecteurs DXF doivent traduire la géométrie (par exemple, les formes des splines) du fichier DXF dans les représentations internes spécifiques de l\'atelier.



## Méthodes d\'importation du fichier DXF dans FreeCAD 

Si vous avez l'intention de vérifier fréquemment les paramètres, nous vous recommandons d'aller dans Edition → Préférences → Importer-Exporter → DXF et de cocher la case \"\[ \] Afficher cette boîte de dialogue lors de l'importation et de l'exportation\".

Vous trouverez plus d\'informations sur les pages [Draft DXF](Draft_DXF/fr.md) et [FreeCAD et Importation DXF](FreeCAD_and_DXF_Import/fr.md).

Si vous utilisez la géométrie importée pour créer des formes 3D dans l\'atelier PartDesign, essayez [Sketcher Valider une esquisse](Sketcher_ValidateSketch/fr.md) après avoir importé le fichier DXF dans une esquisse.



### Importateur DXF en C++ 

Cette implémentation est rapide, mais elle ignore certaines fonctions qu\'elle ne reconnaît pas, comme les splines de DXF. Elle ne peut pas également importer la géométrie dans l\'atelier Draft que sous forme d\'entrées individuelles dans l\'arborescence du modèle. Les couleurs de ces entrées peuvent être lues à partir du fichier si vous cochez cette option. Pour plus d\'informations, voir [ce post dans le forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=32493).



### Importateur DXF en Python 

Cet importateur doit être téléchargé et installé avant de pouvoir être utilisé. Utilisez l\'option \"\[ \] Autoriser FreeCAD à télécharger et à mettre à jour automatiquement les bibliothèques DXF\".

Cet importateur dispose de plus de fonctions (telles que l\'implémentation de splines) et a la possibilité de charger les formes DXF dans l\'atelier Sketcher. Cependant, il faut savoir que tous les éléments de l\'esquisse apparaîtront individuellement une deuxième fois dans l\'arborescence du modèle, ce qui peut prêter à confusion. Vous pouvez supprimer tous chacun de ces objets et conserver uniquement l\'esquisse (qui apparaît comme deuxième entrée dans la liste des nouveaux éléments).

Malheureusement, l\'atelier Sketcher n\'implémente pas les couleurs. Toute la géométrie apparaîtra donc au même niveau, ce qui pose problème si le fichier contient de nombreuses lignes de construction. Une solution consiste à ouvrir votre dessin dans LibreCAD et à supprimer toute la géométrie que vous ne souhaitez pas afficher avant d\'enregistrer un fichier contenant exactement la géométrie que vous souhaitez charger.

### Macros

Gardez un œil sur le forum de FreeCAD ou sur la [Liste des macros](Macros_recipes/fr.md) pour des implémentations alternatives d\'importation et de nettoyage DXF au fur et à mesure de leur développement.



## Sauvegarder au format DXF 

Outre les options du menu Edition → Préférences, l\'[atelier TechDraw](TechDraw_Workbench/fr.md) peut également exporter des pages de dessin au format DXF à l'aide de la fonction [TechDraw Exporter au format DXF](TechDraw_ExportPageDXF/fr.md).



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Draft](Category_Draft.md) > [TechDraw](Category_TechDraw.md) > [File_Formats](Category_File_Formats.md) > DXF/fr
