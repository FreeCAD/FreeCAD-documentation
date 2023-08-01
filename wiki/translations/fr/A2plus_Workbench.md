# <img alt="Icône de l\'atelier Assembly2+" src=images/A2p_workbench.svg  style="width:64px;"> A2plus Workbench/fr

## Introduction


{{TOCright}}

L\'atelier A2plus est un [atelier externe](External_workbenches/fr.md) de Freecad qui permet l\'[assemblage](Assembly/fr.md) de plusieurs pièces.

Cette documentation d\'A2plus porte sur la version **0.4.56 ou plus récente**.



## Installation

L'atelier A2plus est un complément à FreeCAD. Il peut être facilement installé via le menu <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md) à partir de **Outils → Gestionnaire des extensions**. A2plus est en cours de développement et bénéficiera fréquemment de nouvelles fonctionnalités. Par conséquent, vous devez le mettre à jour régulièrement en utilisant également le menu **Outils→ [Gestionnaire des extensions](Std_AddonMgr/fr.md)**. Le code A2plus est hébergé et développé [sur GitHub](https://github.com/kbwbe/A2plus) et peut également être installé manuellement en le copiant dans le répertoire **Mod** de FreeCAD.



## Commencer

Commencez par passer à la barre d'outils A2plus dans FreeCAD. Pour créer un assemblage, créez un nouveau fichier dans FreeCAD. Au début, ce fichier doit être enregistré. Il est recommandé (mais pas nécessaire) de l'enregistrer dans le même dossier que les pièces à assembler.

Vous pouvez maintenant ajouter des pièces à l\'assemblage à l\'aide du bouton de la barre d\'outils <img alt="" src=images/A2p_ImportPart.svg  style="width:24px;"> ou <img alt="" src=images/A2p_ShapeReference.svg  style="width:24px;">. Le bouton <img alt="" src=images/A2p_ImportPart.svg  style="width:24px;"> ajoute tous les corps du fichier sélectionné en une seule pièce. Lorsque vous utilisez le bouton <img alt="" src=images/A2p_ShapeReference.svg  style="width:24px;"> vous pouvez choisir quelle partie d\'un fichier doit être importée en tant que partie. De cette façon, on peut par exemple uniquement importer une esquisse pour assembler d\'autres pièces en utilisant l\'esquisse pour déterminer les positions des pièces.

La première pièce ajoutée obtient une position fixe par défaut. (Vous pouvez la modifier ultérieurement via la propriété {{PropertyData/fr|fixed Position}}.)

Les pièces déjà présentes dans l\'assemblage peuvent être clonées avec le bouton de la barre d\'outils <img alt="" src=images/A2p_DuplicatePart.svg  style="width:24px;">.

Pour modifier une pièce de l\'assemblage, sélectionnez-la dans l\'arbre du modèle et utilisez le bouton de la barre d\'outils <img alt="" src=images/A2p_EditPart.svg  style="width:24px;">. Cela ouvrira la pièce dans un nouvel onglet dans FreeCAD ou basculera vers son onglet si le fichier est déjà ouvert.

Pour mettre à jour les pièces modifiées dans les assemblages, cliquez sur le bouton de la barre d\'outils <img alt="" src=images/A2p_ImportPart_Update.svg  style="width:24px;">. Le bouton de la barre d\'outils <img alt="" src=images/A2p_RecursiveUpdate.svg  style="width:24px;"> importe également les pièces mais de manière récursive sur les [Sous-assemblages](#Sous-assemblages.md) possibles. Si vous sélectionnez une ou plusieurs pièces dans l\'arborescence de FreeCAD, A2plus vous demandera de ne mettre à jour que les pièces sélectionnées.

Les pièces importées conservent leurs dépendances externes et peuvent être modifiées. Pour des pièces bien définies telles que des vis, il est toutefois utile que leur forme ne puisse pas être modifiée. Ceci peut être réalisé avec le bouton de la barre d'outils <img alt="" src=images/A2p_ConvertPart.svg  style="width:24px;"> qui convertit la pièce sélectionnée en une copie statique de la pièce d\'origine.

Pour enregistrer l'ensemble et le refermer par la suite, vous pouvez utiliser le bouton de la barre d'outils <img alt="" src=images/A2p_Save_and_exit.svg  style="width:24px;">.

Le basculement du bouton de la barre d\'outils <img alt="" src=images/A2p_CD_OneButton.svg  style="width:24px;"> définit la manière dont vous pouvez sélectionner plusieurs arêtes, faces, etc. : soit par un simple clic, soit par **Ctrl**+clic.



## Assemblage

L\'assemblage des pièces se fait en ajoutant des contraintes entre les pièces. Après une contrainte, A2plus déplacera les pièces en fonction de la contrainte, si possible.

Pour créer une contrainte entre les pièces, maintenez la touche **Ctrl** enfoncée et sélectionnez soit une arête soit une face de deux pièces. Cliquez ensuite sur le bouton de la barre d\'outils de la contrainte souhaitée. Une boîte de dialogue apparaîtra, décrite dans la section [Contraintes](#Contraintes.md). La contrainte sera ajoutée dans l\'arborescence du modèle attachée aux pièces affectées.

Pour les contraintes complexes entre les pièces, A2plus peut ne pas résoudre les contraintes. Par conséquent, consultez également la section [Dépannage](#Dépannage.md) pour connaître les stratégies permettant de résoudre de tels cas.



### Garder la trace 

Plus vous ajoutez de pièces, plus il est important de conserver une trace. A2plus propose donc ces outils pour déplacer et visualiser des pièces :

-   Pour déplacer une pièce dans l\'assemblage, sélectionnez-la dans l\'arborescence du modèle et utilisez le bouton de la barre d\'outils <img alt="" src=images/A2p_MovePart.svg  style="width:24px;">. Lorsque vous avez placé la pièce où vous le souhaitez, faites un clic gauche avec la souris. Si la pièce déplacée a déjà des contraintes, elle sera placée en conséquence en appuyant sur le bouton de la barre d\'outils <img alt="" src=images/A2p_solver.svg  style="width:24px;"> car cela déclenche la résolution de toutes les contraintes de l'assemblage.
-   Pour afficher une contrainte, sélectionnez-la dans l\'arborescence du modèle et utilisez le bouton de la barre d\'outils <img alt="" src=images/A2p_ViewConnection.svg  style="width:24px;">. Cela rendra tout l\'assemblage transparent et mettra en évidence les deux éléments liés via la contrainte. Pour revenir à la vue normale, cliquez avec le bouton gauche de la souris dans l\'assemblage.
-   Pour afficher uniquement certaines pièces de l\'assemblage, sélectionnez-les dans l\'arborescence du modèle et utilisez le bouton de la barre d\'outils <img alt="" src=images/A2p_Isolate_Element.svg  style="width:24px;">.Vous pouvez également masquer une certaine partie en la sélectionnant dans l\'arborescence du modèle et en appuyant sur la touche **Espace** pour modifier sa visibilité.
-   Pour basculer l\'affichage de la transparence de l\'ensemble, vous pouvez utiliser le bouton de la barre d\'outils <img alt="" src=images/A2p_ToggleTransparency.svg  style="width:24px;">.
-   Chaque pièce peut être rendue transparente par l\'édition normale de FreeCAD. Cependant, le réglage de la transparence des pièces est parfois perdu lors de la réouverture de l\'assemblage en raison d\'un bogue dans FreeCAD. Pour contourner le problème, vous pouvez utiliser le bouton de la barre d'outils <img alt="" src=images/A2p_Restore_Transparency.svg  style="width:24px;"> pour restaurer les paramètres de transparence.



### Contraintes

Lors de la création d\'une contrainte, une boîte de dialogue s\'affiche après avoir appuyé sur un bouton de la barre d\'outils de contrainte:

![](images/A2p_ConstraintPropertiesDialog.png ) 
*Ci-dessus: la boîte de dialogue Propriétés de la contrainte A2plus*

Pour certaines contraintes, il vous permet de modifier la direction des contraintes. Avec le bouton **<img src="images/A2p_solver.svg" width=24px> Solve** vous pouvez vérifier au préalable si cette nouvelle contrainte peut être résolue par A2plus. Sinon, consultez la section [Dépannage](#D.C3.A9pannage.md).

Les contraintes peuvent être désactivées en modifiant sa [visibilité](Std_ToggleVisibility/fr.md). Pour ce faire, sélectionnez la contrainte dans l\'arborescence et appuyez sur **Espace**. Cela bascule la propriété **Suppressed**. Une contrainte supprimée n\'est pas prise en compte lorsque l\'assemblage est résolu.

A2plus fournit les contraintes suivantes :



#### Point sur Point 

Sélectionnez un [sommet](Glossary#Vertex.md) (point) sur chaque pièce. Le bouton de la barre d\'outils  <img alt="" src=images/A2p_PointIdentity.svg  style="width:24px;"> ajoute la contrainte {{Variable|pointIdentity}}. Cela fera coïncider les sommets.



#### Point sur Ligne 

Sélectionnez un [vertex](Glossary/fr#Vertex.md) (point) ou un [edge](Glossary/fr#_Edge.md) (ici arc) de cercle (sélectionnera son centre) ou une [face](Glossary_#_Face/fr.md) sphérique (sélectionnera également son centre) d\'une part et un [edge](Glossary#Edge.md) d\'autre part. Le bouton de la barre d\'outils <img alt="" src=images/A2p_PointOnLineConstraint.svg  style="width:24px;"> ajoute la contrainte {{Variable|pointOnLine}}. Cela mettra le vertex sur l\'edge.



#### Point sur Plan 

Sélectionnez un [vertex](Glossary/fr#Vertex.md) (point) ou un [edge](Glossary/fr#Edge.md) (ici arc) de cercle (sélectionnera son centre) ou la [face](Glossary#Face/fr.md) d\'une sphère (sélectionnera également son centre) d\'une par et un plan d\'autre part. Le bouton de la barre d'outils <img alt="" src=images/A2p_PointOnPlaneConstraint.svg  style="width:24px;"> ajoute la contrainte {{Variable|pointOnPlane}}. Le dialogue de contrainte vous permet de spécifier un décalage entre le point et le plan. Ce décalage peut également être inversé entre les deux côtés du plan. Si le décalage est nul, la contrainte placera le sommet sur le plan.



#### Sphère sur Sphère 

Sélectionnez une [face](Glossary/fr#Face.md) sphérique ou un [vertex](Glossary/fr#Vertex.md) (point) sur les deux pièces. Le bouton de la barre d\'outils <img alt="" src=images/A2p_SphericalSurfaceConstraint.svg  style="width:24px;"> ajoute la contrainte {{Variable|sphereCenterIdent}}. Cela fera coïncider les centres des sphères, le centre de la sphère et le sommet, ou les sommets.



#### Bord circulaire sur bord circulaire 

Sélectionnez un [bord](Glossary/fr#Edge.md) circulaire sur les deux pièces. Le bouton de la barre d\'outils  ajoute la contrainte {{Variable|circularEdge}}. Le dialogue de contrainte vous permet de spécifier un décalage entre les arêtes. Ce décalage peut également être inversé. Vous pouvez en outre définir le sens de la contrainte et verrouiller la rotation des pièces. Si le décalage est nul, la contrainte placera les arêtes concentriques dans le même plan.



#### Axes coïncidents 

Sélectionnez une [face](Glossary/fr#Face.md) cylindrique ou un [bord](Glossary/fr#Edge.md) linéaire sur les deux pièces. Le bouton de la barre d\'outils <img alt="" src=images/A2p_AxialConstraint.svg  style="width:24px;"> ajoute la contrainte {{Variable|axisCoincident}}. Le dialogue de contrainte vous permet de spécifier la direction de l\'axe.La boîte de dialogue vous permet en outre de verrouiller la rotation des pièces. La contrainte fera coïncider les axes ou les lignes.



#### Axes parallèles 

Sélectionnez une [face](Glossary/fr#Face.md) cylindrique ou un [bord](Glossary/fr#Edge.md) linéaire sur les deux pièces. Le bouton de la barre d\'outils <img alt="" src=images/A2p_AxisParallelConstraint.svg  style="width:24px;"> ajoute la contrainte {{Variable|axisParallel}}. Le dialogue de contrainte vous permet de spécifier la direction de l\'axe. La contrainte rendra les axes ou les lignes parallèles.



#### Axe sur plan parallèle 

Sélectionnez une [face](Glossary/fr#Face.md) cylindrique ou un [bord](Glossary/fr#Edge.md) linéaire sur une pièce et un plan sur l\'autre pièce. Le bouton de la barre d\'outils <img alt="" src=images/A2p_AxisPlaneParallelConstraint.svg  style="width:24px;"> ajoute la contrainte {{Variable|axisPlaneParallel}}. La contrainte rendra l\'axe ou la ligne parallèle au plan.



#### Axe sur plan normal 

Sélectionnez une [face](Glossary#Face.md) cylindrique ou un [bord](Glossary#Edge.md) linéaire sur une partie et un plan sur l\'autre partie. Le bouton de la barre d'outils <img alt="" src=images/A2p_AxisPlaneVerticalConstraint.svg  style="width:24px;"> ajoute la contrainte {{Variable|axisPlaneNormal}}. La contrainte rendra l\'axe ou la ligne normale au plan.



#### Axe sur plan d\'angle 

Sélectionnez une [face](Glossary#Face.md) cylindrique ou une [arête](Glossary#Edge.md) linéaire sur une partie et un plan sur l\'autre partie. Le bouton de la barre d\'outils <img alt="" src=images/A2p_AxisPlaneAngleConstraint.svg  style="width:24px;"> ajoute la contrainte {{Variable|axisPlaneAngle}}. La contrainte rendra d\'abord l\'axe parallèle au plan. Ensuite, vous pouvez ajuster l\'angle de l\'axe dans la boîte de dialogue des paramètres de contrainte qui apparaît.



#### Plans parallèles 

Sélectionnez un plan sur les deux pièces. Le bouton de la barre d\'outils <img alt="" src=images/A2p_PlanesParallelConstraint.svg  style="width:24px;"> ajoute la contrainte {{Variable|planesParallel}}. La boîte de dialogue de contrainte vous permet de spécifier le sens de la contrainte. La contrainte rendra les plans parallèles.



#### Plan sur plan 

Sélectionnez un plan sur les deux pièces. Le bouton de la barre d\'outils <img alt="" src=images/A2p_PlaneCoincidentConstraint.svg  style="width:24px;"> ajoute la contrainte {{Variable|planeCoincident}}. La boîte de dialogue de contrainte vous permet de spécifier une direction de contrainte et un décalage entre les plans. Ce décalage peut également être inversé. Si le décalage est nul, la contrainte fera coïncider les plans.



#### Angle entre plans 

Sélectionnez un plan sur les deux pièces. Le bouton de la barre d\'outils <img alt="" src=images/A2p_AngleConstraint.svg  style="width:24px;"> ajoute la contrainte {{Variable|angledPlanes}}. Le dialogue de contrainte vous permet de spécifier un angle entre les plans. La contrainte va d\'abord rendre les plans parallèles et définir l\'angle spécifié.



#### Coïncidence au centre de masse 

Sélectionnez un [bord](Glossary/fr#Edge.md) fermé ou un plan sur les deux pièces. Le bouton de la barre d\'outils <img alt="" src=images/A2p_CenterOfMassConstraint.svg  style="width:24px;"> ajoute la contrainte {{Variable|centerOfMass}}. Le dialogue de contrainte vous permet de spécifier un décalage entre les arêtes ou les plans. Ce décalage peut également être inversé. Vous pouvez en outre définir le sens de la contrainte et verrouiller la rotation des pièces. Si le décalage est nul, la contrainte placera les arêtes ou les plans dans le même plan.



### Sous-assemblages 

Un assemblage peut contenir d\'autres assemblages. Ils sont ajoutés comme des pièces en appuyant sur le bouton de la barre d'outils <img alt="" src=images/A2p_ImportPart.svg  style="width:24px;"> et en sélectionnant un fichier ***.FCStd** contenant un assemblage. De tels sous-ensembles peuvent également être édités comme des pièces à l'aide du bouton de la barre d'outils <img alt="" src=images/A2p_EditPart.svg  style="width:24px;">. Assurez-vous, pour les étapes d\'assemblage supérieures, que vous mettez à jour l\'assemblage via le bouton de la barre d\'outils <img alt="" src=images/A2p_ImportPart_Update.svg  style="width:24px;"> quand il y a eu des changements.



## Traitement des contraintes 

Les contraintes possibles pour une sélection sont affichées dans la barre d'outils et dans la boîte de dialogue \"Outils de contrainte\" en activant les boutons correspondants. La boîte de dialogue \"Outils de contrainte\" s'ouvre via le bouton de la barre d'outils <img alt="" src=images/A2p_DefineConstraints.svg  style="width:24px;">. Il est prévu de rester ouvert pour pouvoir ajouter rapidement plusieurs contraintes à l'assemblage.

Les contraintes existantes peuvent être modifiées en les sélectionnant dans l\'arborescence du modèle, puis en double-cliquant dessus ou en utilisant le bouton de la barre d\'outils <img alt="" src=images/A2p_EditConstraint.svg  style="width:24px;">. Cela ouvre la boîte de dialogue \"Propriétés de contrainte\".

Les contraintes peuvent être temporairement supprimées en les sélectionnant dans l\'arbre du modèle et en modifiant la propriété de l\'élément d\'arbre{{PropertyData/fr|Suppressed}}.

Les contraintes peuvent être supprimées en les sélectionnant dans l\'arborescence du modèle et en appuyant sur **Suppr** ou en sélectionnant une pièce avec des contraintes dans l\'arborescence du modèle et en utilisant le bouton de la barre d\'outils <img alt="" src=images/A2p_DeleteConnections.svg  style="width:24px;">.

Toutes les contraintes peuvent être résolues à tout moment avec le bouton de la barre d'outils <img alt="" src=images/A2p_solver.svg  style="width:24px;">. Si le bouton de la barre d\'outils <img alt="" src=images/A2p_ToggleAutoSolve.svg  style="width:24px;"> est activé, une résolution est automatiquement effectuée après chaque édition d\'une contrainte.

Le bouton de la barre d\'outils <img alt="" src=images/A2p_FlipConstraint.svg  style="width:24px;"> affecte la contrainte qui a été ajoutée le plus récemment. Il inverse la direction de la contrainte.

Avec l\'outil <img alt="" src=images/A2p_CD_ConstraintViewer.svg  style="width:24px;">, il est possible d\'afficher et d\'inspecter les contraintes existantes. Après avoir cliqué sur l\'outil, une boîte de dialogue s\'ouvre. Vous pouvez alors soit sélectionner une pièce dans l\'arborescence et cliquer sur le bouton **Import from part** pour obtenir toutes les contraintes de cette pièce, soit sélectionner une ou plusieurs contraintes dans l\'arborescence et cliquer sur le bouton **Import from Tree**. Le résultat est que vous obtenez toutes les informations sur les contraintes. En cliquant dans la colonne *Suppress*, une seule contrainte peut être supprimée. Pour plus de fonctionnalités, suivez les infobulles des autres boutons de la boîte de dialogue.



## Listes de pièces 

Pour créer des listes de pièces d\'assemblages, les différentes pièces de l\'assemblage doivent obtenir des informations sur les pièces pouvant être lues par A2plus. Ceci est fait en éditant la pièce en utilisant le bouton de la barre d'outils <img alt="" src=images/A2p_EditPart.svg  style="width:24px;">. Dans la partie ouverte, appuyez sur le bouton de la barre d'outils <img alt="" src=images/A2p_PartsInfo.svg  style="width:24px;"> et une [feuille de calcul](Spreadsheet_Workbench/fr.md) portant le nom *#PARTINFO#* est créée.

La structure de la feuille de calcul est la suivante :

![](images/A2p_PartinfoTable.png )

Remplissez les champs gris avec les informations que vous avez et que vous souhaitez inclure dans la liste de pièces finale.

Dans l\'assemblage ou le sous-assemblage, utilisez le bouton de la barre d\'outils <img alt="" src=images/A2p_PartsList.svg  style="width:24px;">. Il vous demandera si vous souhaitez effectuer une itération récursive sur tous les sous-assemblages. Cliquez sur \"Oui\". Cela crée une nouvelle feuille de calcul avec le nom *#PARTSLIST#*. Il contient les informations des différentes feuilles de calcul *#PARTSINFO#* des pièces dans une liste comme celle-ci :

![](images/A2p_PartslistTable.png )

La position (POS) est automatiquement définie en fonction de l\'apparence des pièces dans l\'arbre du modèle. La pièce de niveau supérieur recevra POS 1.

La quantité (QTY) est automatiquement calculée à partir de l\'assemblage. Si une pièce est deux fois dans l\'assemblage, elle aura QTY 2.

Si vous avez mis à jour une information de pièce, vous pouvez actualiser la liste de pièces en appuyant sur le bouton de la barre d'outils <img alt="" src=images/A2p_PartsList.svg  style="width:24px;"> à nouveau.

Pour les sous-ensembles, vous pouvez également créer une feuille de calcul d'informations à l'aide du bouton de la barre d'outils <img alt="" src=images/A2p_PartsInfo.svg  style="width:24px;">. Lorsque vous créez ou mettez à jour la liste de pièces de l\'assemblage principal, cette information est utilisée si vous cliquez sur \"Non\" pour la question si vous souhaitez effectuer une itération récursive sur tous les sous-assemblages. Ensuite, les différentes pièces ne figurent pas dans la liste de pièces, mais uniquement les sous-assemblages.



## Fonctions spéciales 



### Structure d\'assemblage 

Le bouton de la barre d\'outils <img alt="" src=images/A2p_Treeview.svg  style="width:24px;"> crée un fichier HTML avec la structure de votre assemblage. Le fichier sera créé par défaut dans le dossier de votre fichier d\'assemblage. La structure ressemble à celle-ci:

:   ![](images/A2p_Dependency-Tree.jpg )



### Degrés de liberté 

Le bouton <img alt="" src=images/A2p_DOFs.svg  style="width:24px;"> permet d'étiqueter chaque partie de l'assemblage avec ses degrés de liberté. De plus, il affiche une liste avec toutes les pièces et leurs dépendances. La liste est sortie dans le widget *Vue rapport* de FreeCAD. Si ce widget n\'est actuellement pas visible, vous pouvez l\'afficher soit en cliquant avec le bouton droit de la souris sur une partie vide de la zone de la barre d\'outils FreeCAD, puis en le choisissant dans le menu contextuel qui apparaît, ou avec le menu **Affichage → Panneaux → [Vue rapport](Report_view/fr.md)**.

Les libellés des degrés de liberté peuvent être supprimées en cliquant à nouveau sur le bouton <img alt="" src=images/A2p_DOFs.svg  style="width:24px;">.



### Étiquetage

Le bouton <img alt="" src=images/A2p_PartLabel.svg  style="width:24px;"> identifie chaque partie de l\'assemblage dans la vue 3D par son nom. Les étiquettes des pièces peuvent être supprimées en cliquant sur le bouton <img alt="" src=images/A2p_PartLabelRemove.svg  style="width:24px;">.



### Forme de l\'assemblage complet 

Parfois, il est nécessaire de combiner l'ensemble du montage en une seule forme. Cette forme peut ensuite être utilisée par exemple pour l'impression 3D dans l'[atelier Mesh](Mesh_Workbench/fr.md) ou pour les dessins dans l'[atelier TechDraw](TechDraw_Workbench/fr.md). Il est créé en utilisant le bouton de la barre d'outils <img alt="" src=images/A2p_SimpleAssemblyShape.svg  style="width:24px;">. La forme est par défaut non visible.Utilisez le même bouton de la barre d'outils pour mettre à jour la forme en cas de modification de l'assemblage.



### Convertir les chemins absolus en chemins relatifs 

Avec le menu **A2plus → Misc → [<img src=images/A2p_SetRelativePathes.svg style="width:24px"> Convert absolute paths of imported parts to relative ones** vous pouvez convertir les chemins absolus des pièces importées en pièces relatives.



## Préférences

Les préférences de a2plus sont accessibles via le menu  **Edition → [Préférences](Preferences_Editor/fr.md)** de FreeCAD et dans la section \"A2plus\". Vous pouvez définir les options suivantes :



### Méthode de résolution par défaut 

Utiliser la résolution de systèmes partiels: Le solveur commence par une pièce ayant la propriété {{PropertyData/fr|fixed Position}} définie sur \"true\" et une pièce contrainte à celle-ci. Toutes les autres pièces ne sont pas calculées. Si une solution peut être trouvée, la prochaine pièce contrainte est ajoutée pour le calcul, etc.
Utilisez un solveur \"magnétique\", résolvant toutes les pièces à la fois: Le solveur essaie de déplacer toutes les pièces en même temps en direction d\'une pièce pour laquelle la propriété {{PropertyData/fr|fixed Position}} a la valeur \"true\". Notez que dans la plupart des cas, cela prend plus de temps pour le calcul d\'une solution.
Forcez en position fixe: Ceci définit la propriété {{PropertyData/fr|fixed Position}} à \"true\" pour toutes les pièces de l'assemblage. Ensuite, aucun calcul n\'est réellement effectué, car toutes les pièces seront toujours fixées aux positions où elles ont été créées.



### Comportement par défaut du solveur 

Résoudre automatiquement si une propriété de contrainte est modifiée: Le solveur sera automatiquement lancé. Identique à l\'activation du bouton de la barre d\'outils <img alt="" src=images/A2p_ToggleAutoSolve.svg  style="width:24px;">.



### Comportement lors de la mise à jour de pièces importées 

Recalculez les pièces importées avant de les mettre à jour: Toutes les pièces de l\'assemblage, y compris les sous-assemblages, seront ouvertes dans FreeCAD pour être reconstruites à l\'aide des valeurs des feuilles de calcul.
Cette fonctionnalité est conçue pour une construction totalement paramétrique. **Remarque:** cette fonctionnalité est très expérimentale et n\'est pas recommandée pour des projets importants.

Problèmes connus :

-   L\'assemblage peut être détruit à cause de fausses références à des noms topologiques dans des pièces
-   Les feuilles de calcul principales peuvent être endommagées lorsqu\'elles sont modifiées alors qu\'un fichier de pièce référencé est déjà fermé. Cela peut planter FreeCAD.

Activez la mise à jour récursive des pièces importées: Ouvre tous les sous-assemblages de manière récursive pour les mettre à jour.





Utilisez un nom topologique expérimental: Lors de l'importation de pièces dans l'assemblage, un algorithme génère des noms topologiques pour chaque sous-élément de la forme importée. Les noms topologiques sont écrits dans {{PropertyData/fr|mux Info}}. Lorsqu\'une pièce importée doit être mise à jour, ces noms topologiques sont utilisés pour mettre à jour les sous-éléments des contraintes. Ainsi, les assemblages deviennent plus robustes face aux nombres volatils de sous-éléments de FreeCAD.
**Remarque:** Cela augmente la taille des fichiers et le temps de calcul lors de l\'importation de pièces. Si la dénomination topologique doit être utilisée, elle doit être activée avant la création de l\'assemblage.

 

Héritage par transparence des pièces et des sous-assemblages: Utilisez les paramètres de couleur et de transparence des pièces importées.
**Remarque :** cette fonctionnalité est très expérimentale et n\'est pas recommandée pour des projets importants.

   

N\'importez pas de formes invisibles: Cela masquera les formes de données/construction invisibles. **Remarque:** Aucune contrainte ne doit être connectée aux formes de référence/construction dans les sous-ensembles supérieurs ou autres, sinon vous risquez de casser l\'assemblage.

   

Utilisez l\'union solide pour importer des pièces et des sous-assemblages: Toutes les pièces importées seront directement assemblées en tant que union.
Cette fonctionnalité est utile pour les simulations [FEM](FEM_Workbench/fr.md) ou [l'impression 3D](Manual:Preparing_models_for_3D_printing/fr.md) si un seul solide est autorisé. L\'alternative consiste à créer ultérieurement une [forme de l\'assemblage complet](#Forme_de_l.27assemblage_complet.md).



### Paramètres de l\'interface utilisateur 

Afficher les contraintes dans la barre d\'outils: Si cette option n\'est pas utilisée, les boutons de la barre d\'outils pour les différentes contraintes ne sont pas visibles pour économiser de l\'espace dans la barre d\'outils. De nouvelles contraintes peuvent toujours être définies à l'aide de la boîte de dialogue *Outils de contrainte* (bouton de la barre d'outils <img alt="" src=images/A2p_DefineConstraints.svg  style="width:24px;">).
Utiliser le gestionnaire de fichiers natif de votre système d\'exploitation: si cette option est utilisée, vous obtenez la boîte de dialogue de fichier de votre système d\'exploitation lorsque vous sélectionnez des fichiers pour les assemblages.

 



### Stockage des fichiers 

Utiliser des chemins relatifs pour les pièces importées: UUtilise les chemins de fichiers relatifs aux fichiers de pièce.
Utiliser des chemins absolus pour les pièces importées: Utilise des chemins de fichier absolus pour les fichiers de pièces.
Tous les fichiers sont dans ce dossier de projet: Tous les fichiers de projet doivent être dans le dossier spécifié. Peu importe s\'ils se trouvent dans les sous-dossiers de ce dossier.**Remarque:** aucun fichier ne peut exister plusieurs fois dans le dossier (par exemple, dans différents sous-dossiers).
Cette option est utile pour travailler sur différentes machines car il suffit ensuite de copier le dossier du projet.



## Dépannage

Tôt ou tard, vous aurez le problème qu\'A2plus ne peut pas résoudre les contraintes que vous avez définies.Pour surmonter cela, il existe différentes stratégies :



### Utilisation de l\'outil de recherche de conflits 

Il s\'agit de la méthode la plus sûre lorsque vous avez plusieurs contraintes: cet outil tente de résoudre une contrainte après l\'autre jusqu\'à ce qu\'il trouve la contrainte en conflit. Ensuite, vous pouvez continuer avec les autres stratégies pour résoudre la contrainte identifiée. L\'outil est appelé à l\'aide du bouton de la barre d\'outils <img alt="" src=images/A2p_SearchConstraintConflicts.svg  style="width:24px;">.



### Vérification de la direction de la contrainte 

Parfois, les contraintes semblent être systématiquement définies mais elles ne peuvent néanmoins pas être résolues. Un exemple: supposons que vous ayez un ensemble de contraintes {{Variable|[plans Parallèles](#Plane_Parallel.md)}} pour deux plans. Vous souhaitez maintenant définir pour les mêmes plans la contrainte {{Variable|[plans coïncidents](#Plane_on_Plane.md)}} et A2plus ne peut pas résoudre ce problème. Alors les directions de contrainte des {{Variable|planesParallel}} et {{Variable|planeCoincident}} sont différentes. Utilisez la même direction pour les deux contraintes afin de résoudre ce problème.

A2plus propose de vérifier automatiquement la bonne direction pour **toutes** les contraintes de l\'assemblage à l\'aide du bouton de la barre d\'outils <img alt="" src=images/A2p_ReAdjustConstraints.svg  style="width:24px;">.



### Suppression de contraintes 

La plupart des cas de contraintes insolubles se produisent directement lors de l\'ajout d\'une nouvelle contrainte. La solution consiste alors à supprimer la dernière contrainte que vous avez ajoutée. A2plus le proposera également.

Parfois, la stratégie de suppression est la seule, par exemple lorsque vous modifiez une pièce dans FreeCAD afin que des faces ou des arêtes liées à des contraintes soient manquantes. Vous devez ensuite supprimer une contrainte liée à la pièce modifiée à la fois. Utilisez le bouton de la barre d\'outils <img alt="" src=images/A2p_solver.svg  style="width:24px;"> après chaque suppression pour voir si vous avez atteint un état que le solveur peut résoudre.

Lorsque vous avez un assemblage qui peut être résolu, ajoutez étape par étape les contraintes dont vous avez besoin.



### Pièces mobiles 

Dans de nombreux cas, le solveur ne nécessite que des meilleures valeurs de départ pour résoudre les contraintes. Prenons par exemple le cas où vous avez une pièce essieu et une pièce roue. Vous ajoutez une contrainte {{Variable|axisCoincident }} et n\'obtenez aucune information sur l\'échec du solveur, mais les pièces ne sont pas déplacées en conséquence et dans le l\'onglet Afficher rapport de FreeCAD, vous voyez \"*REACHED POS-ACCURACY :0.0*\". Une solution à cela consiste à rapprocher les pièces de la position souhaitée par la contrainte.

**Remarque :** Assurez-vous qu\'au moins une pièce de la contrainte a la propriété **Position fixe** définie sur *false*.



### Définition de la propriété Fonction résultante 

Si vous avez oublié certaines fonctionnalités de votre pièce après l\'importation dans un assemblage A2plus, vérifiez la propriété {{PropertyData/fr|[Tip](PartDesign_MoveTip/fr.md)}}.

A2plus importe des corps de pièces avec toutes leurs fonctions jusqu\'à la fonction Tip. Cela est judicieux car le fait de définir Tip sur une certaine fonction signifie que toutes les fonctions derrière Tip ne doivent pas apparaître dans la partie finale. Donc, si vous manquez une fonction de pièce dans A2plus, ouvrez la pièce via le bouton de la barre d\'outils <img alt="" src=images/A2p_EditPart.svg  style="width:24px;"> puis sélectionnez un corps et regardez sa propriété {{PropertyData/fr|Tip}}. Si Tip ne se trouve pas à la fonction où vous le souhaitez, cliquez avec le bouton droit sur la fonction où Tip devrait être et choisissez **[<img src=images/PartDesign_MoveTip.svg style="width:24px"> Set tip**. Enfin, enregistrez la pièce et rechargez l\'assemblage à l\'aide du bouton de la barre d\'outils <img alt="" src=images/A2p_ImportPart_Update.svg  style="width:24px;">.



### Réparation de l\'arbre d\'assemblage 

Si vous ne voyez pas clairement pourquoi certaines contraintes ne peuvent pas être résolues, vous pouvez utiliser le bouton de la barre d'outils <img alt="" src=images/A2p_RepairTree.svg  style="width:24px;">. Ceci résoudra toutes les contraintes et les regroupera à nouveau sous les différentes pièces.



### Migration d\'anciens assemblages A2plus 

Les assemblages créés avec A2plus antérieurs à mars 2019 n\'affichent pas les icônes correctes pour les pièces importées et ont des propriétés obsolètes. Ces assemblages peuvent être migrés vers A2plus version 0.4.35 et plus récente à l\'aide du menu **[<img src=images/A2p_RecursiveUpdate.svg style="width:24px"> Migrer les proxys de pièces importées**. Après cela, vous devez enregistrer et rouvrir votre fichier d\'assemblage.



### Éviter les caractères accentués 

**Cette stratégie n\'est pas nécessaire pour Windows.**

Sur certains systèmes d\'exploitation, vous pouvez rencontrer des problèmes si les noms de fichier ou les chemins de fichier des pièces ou de l\'assemblage contiennent des caractères accentués. Par conséquent, évitez ces caractères et les caractères spéciaux en général.



### Position de fixation 

**Cette stratégie n\'est plus nécessaire pour les assemblages créés avec A2plus 0.3.11 ou une version plus récente, car A2plus émet désormais un avertissement pour les positions fixes manquantes.**

Lorsque vous définissez une contrainte entre deux pièces et qu\'aucune pièce n\'a la propriété {{PropertyData/fr|Position fixe}} définie sur *true* ou est liée par une contrainte à une pièce avec {{PropertyData/fr|Position fixe}} définie sur *true*, la contrainte ne peut pas être résolue. La même chose se produit si les deux pièces de la contrainte ont {{PropertyData/fr|Position fixe}} défini sur *true*.

Ensuite, A2plus transmet les informations relatives à la solution défaillante, mais parfois, vous voyez que les pièces ne sont pas déplacées en conséquence et dans l\'onglet Afficher rapport de FreeCAD, vous voyez \"*REACHED POS-ACCURACY :0.0*\". Cela signifie que le solveur a fini sans erreurs mais qu\'il n\'a pas pu résoudre les contraintes.

Par conséquent, vérifiez qu\'au moins une de vos pièces de l\'ensemble a {{PropertyData/fr|Position fixe}} définie sur *true*. Assurez-vous ensuite que vous ne définissez des contraintes que sur une pièce qui est en quelque sorte connectée à la pièce fixe. Pour visualiser ces dépendances, reportez-vous à la section [Structure de l\'assemblage](#Structure_d.27assemblage.md).



### Pièces tournantes 

**Cette stratégie n\'est plus nécessaire pour les assemblages créés avec A2plus 0.4.0 ou plus récent, car A2plus fait pivoter automatiquement les pièces en arrière-plan afin d\'obtenir un angle de départ suffisant pour le solveur.**

Le solveur échoue souvent pour la contrainte {{Variable|angledPlanes}} si les deux plans sélectionnés ont actuellement un angle de 0 ° ou 180 °. (Les pièces ne sont pas déplacées en conséquence et dans l\'onglet \"Vue Rapport\" de FreeCAD, vous voyez \"*REACHED POS-ACCURACY :0.0*\".) Une solution consiste à faire pivoter une pièce de quelques degrés à l\'aide de la fonction de transformation de FreeCAD (cliquez avec le bouton droit de la souris sur la pièce dans l'arbre du modèle et sélectionnez dans le menu contextuel **Transformer**).

**Remarque:** Assurez-vous qu\'au moins une pièce de la contrainte a la propriété {{PropertyData/fr|Position fixe}} définie sur *false*.

## Animation

A2plus propose des animations par glisser-déposer et via des scripts Python.



### Glisser

Les animations de glissement sont interactives. Vous les déclenchez en faisant glisser une partie de l\'assemblage. Pour obtenir ce genre d\'animations:

1.  Contraindre complètement la partie dont le mouvement ou la rotation doit être animé.
2.  Cliquez sur le bouton de la barre d\'outils <img alt="" src=images/A2p_MovePartUnderConstraints.svg  style="width:24px;">. Cela active le mode de glissement.
3.  Cliquez sur la pièce souhaitée dans l\'assemblage.
4.  Vous pouvez maintenant déplacer la souris et la pièce suivra le mouvement de la souris dans les contraintes définies.
5.  Pour terminer le mode de glissement, faites un clic gauche dans l\'assemblage ou appuyez sur ÉCHAP.

Voici un exemple d\'assemblage pour tester l\'animation de glissement: [A2p_example-for-dragging-animation.FCStd](https://forum.freecadweb.org/download/file.php?id=99204)

![](images/A2p_dragging-animation-result.gif )



*Ci-dessus: l'animation de glissement à l'aide de l'exemple d'assemblage*



### Script

Bien que le mode glisser offre de belles animations interactives, elles ne sont parfois pas assez précises pour les screencasts ou les vidéos. Les animations scriptées ont l\'avantage d\'animer des mouvements et des rotations d\'une manière définie. Vous pouvez par exemple faire pivoter une pièce exactement de 10° d\'avant en arrière. Les exemples suivants utilisent un assemblage dans lequel une pièce doit être tournée. Si vous essayez d\'animer cela en utilisant le mode glisser, vous verrez à quel point il est difficile d\'obtenir une rotation d\'avant en arrière que vous pouvez par exemple montrez votre patron dans une présentation. Avec l\'exemple de script interactif, c\'est une tâche facile.

Une animation scriptée fonctionne généralement de cette façon:

1.  L\'assemblage est entièrement contraint.
2.  Le script modifie un paramètre, par exemple la position ou l\'angle de rotation d\'une pièce.
3.  Après le changement de paramètre, les contraintes d\'assemblage sont résolues.
4.  Les étapes 2 et 3 sont répétées pour obtenir l\'animation.

Il est également possible de modifier au lieu d\'un paramètre de placement une contrainte, par exemple la distance entre 2 plans.



#### Exemple simple de script 

La façon la plus simple de scénariser une animation est une animation non interactive qui suit un mouvement défini. Voici un exemple : Téléchargez d\'abord ce fichier d\'assemblage : [A2p_animated-example.FCStd](https://forum.freecadweb.org/download/file.php?id=97554) et aussi ce script Python : [A2p_animation-exemple-script.py](https://forum.freecadweb.org/download/file.php?id=97981).


<div class="mw-collapsible mw-collapsed toccolours">

Contenu du script. Les lignes commençant par un \'#\' décrivent ce que font les différentes lignes de script:


<div class="mw-collapsible-content">


```python
# import libraries
import time, math, PySide
import A2plus.a2p_solversystem as a2p_solver

# nous utilisons des pas de 1 degré
step = 1
# attendez 1 ms entre chaque étape
timeout = 0.001
# l'angle initial est de 0 degré
angle = 0
# nous prenons le document actuellement ouvert
document = FreeCAD.activeDocument()
# on veut changer plus tard l'angle de rotation de la pièce "star_wheel_001"
starWheel = document.getObject("star_wheel_001")
# définir une boîte de dialogue de progression allant de 0 à 360
progressDialog = PySide.QtGui.QProgressDialog(u"Animation progress", u"Stop", 0, 360)

# le bloc while est la boucle principale pour changer l'angle et résoudre
# les contraintes d'assemblage par la suite
while angle < 360: # exécute cette boucle jusqu'à ce que nous ayons fait un tour complet (360 degrés)
     # augmenter l'angle de rotation
     angle += step
     # définit le nouvel angle dans la boîte de dialogue de progression
     progressDialog.setValue(angle)
     # change l'angle de rotation de la pièce "star_wheel_001"
     starWheel.Placement.Rotation.Angle = math.radians(angle)
     # résoud les contraintes
     a2p_solver.solveConstraints(document, useTransaction=True)
     # mettre à jour la vue après la résolution ('Gui' signifie 'interface utilisateur graphique')
     FreeCADGui.updateGui()
     # met en avant la boîte de dialogue de progression
     PySide.QtGui.QWidget.raise_(progressDialog)
     # si 'Stop' a été pressé dans la boîte de dialogue, quitte la boucle
     if progressDialog.wasCanceled():
        angle = 360
     # attend un peu avant d'effectuer l'étape suivante
     time.sleep(timeout)
```


</div>


</div>

Pour utiliser le script pour effectuer l\'animation, nous devons:

1.  Ouvrir le fichier d\'assemblage dans FreeCAD.
2.  Ouvrir le fichier de script dans FreeCAD.
3.  Cliquer sur le bouton de la barre d\'outils <img alt="" src=images/Menu_Std_DlgMacroExecute_fr_02.png  style="width:24px;"> pour exécuter le script (également appelé macro).
4.  Passer à l\'onglet de l\'assemblage pour voir la rotation.

Pour vous entraîner, changez simplement quelque chose dans le script et exécutez-le ensuite. Par exemple, augmentez «step» à «5».

Voici le résultat de l\'exemple d\'animation:

![](images/A2p_animated-example-result.gif )



#### Exemple de script interactif 

Le premier exemple de script a montré comment créer une animation sans rétroaction de l\'utilisateur. Pour la plupart des applications, vous devez interagir avec l\'animation. Par exemple, le problème intéressant dans l\'exemple est de voir comment les broches d\'entraînement traversent la rainure centrale de la roue. Pour regarder de plus près, vous pouvez présenter ce détail à vos collègues. Vous avez donc besoin d\'une solution interactive.

Cela peut être fait en utilisant une boîte de dialogue d\'animation personnalisée avec un curseur. En déplaçant le curseur, vous pouvez définir l\'angle de rotation et donc faire pivoter d\'avant en arrière à une position intéressante.

Nous utilisons le même fichier d\'assemblage:[A2p_animated-example.FCStd](https://forum.freecadweb.org/download/file.php?id=97554) et ce script Python: [A2p_animation-example-script.py](https://forum.freecadweb.org/download/file.php?id=97982).


<div class="mw-collapsible mw-collapsed toccolours">

Voici le contenu du script pour obtenir la boîte de dialogue d\'animation interactive:


<div class="mw-collapsible-content">


```python
# import libraries
import time, math, PySide, sys
import FreeCAD.A2plus.a2p_solversystem as a2p_solver
from FreeCAD import Units
from PySide import QtCore, QtGui

# attendre 1 ms après chaque calcul
timeout = 0.001
# nous prenons le document actuellement ouvert
document = FreeCAD.activeDocument()
# on veut changer plus tard l'angle de rotation de la pièce "star_wheel_001"
starWheel = document.getObject("star_wheel_001")

class AnimationDlg(QtGui.QWidget): # the animation dialog

    def __init__(self): # to initialize the dialog
        super(AnimationDlg, self).__init__()
        self.initUI()

    def initUI(self): # définition des composants de dialogue
        self.setMinimumSize(self.minimumSizeHint()) # définir la taille minimale de la boîte de dialogue au minimum
        self.setWindowTitle('Animation Dialog')
        # utiliser une disposition de grille pour l'ensemble du formulaire
        self.mainLayout = QtGui.QGridLayout()
        self.lineNo = 0 # first dialog grid line
        # ajouter une étiquette de description
        DescriptionLabel = QtGui.QLabel(self)
        DescriptionLabel.setText("Change slider to change rotation angle")
        self.mainLayout.addWidget(DescriptionLabel,self.lineNo,0,1,4)
         # ligne de grille de dialogue suivante
        self.lineNo += 1
        # ajouter une étiquette; il n'y a pas besoin du «moi». préfixe parce que nous ne voulons pas changer l'étiquette plus tard
        LabelMin = QtGui.QLabel(self)
        LabelMin.setText("Min")
        LabelMin.setFixedHeight(32)
        self.mainLayout.addWidget(LabelMin,self.lineNo,0)
        # ajouter une modification du spin pour définir le minimum du curseur
        self.MinEdit = QtGui.QSpinBox(self)
        # obtenir l'unité d'angle sous forme de chaîne
        self.MinEdit.setSuffix(" " + str(FreeCAD.Units.Quantity(1, FreeCAD.Units.Angle))[2:])
        self.MinEdit.setMaximum(999)
        self.MinEdit.setMinimum(0)
        self.MinEdit.setSingleStep(10)
        self.MinEdit.setValue(0)
        self.MinEdit.setFixedHeight(32)
        self.MinEdit.setToolTip("Minimal angle for the slider")
        QtCore.QObject.connect(self.MinEdit, QtCore.SIGNAL("valueChanged(int)"), self.setMinEdit)
        self.mainLayout.addWidget(self.MinEdit,self.lineNo,1)
        # ajoutez le curseur
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setRange(0, 360)
        self.slider.setValue(0)
        self.slider.setFixedHeight(32)
        self.slider.setToolTip("Move the slider to change the rotation angle")
        QtCore.QObject.connect(self.slider, QtCore.SIGNAL("sliderMoved(int)"), self.handleSliderValue)
        self.mainLayout.addWidget(self.slider,self.lineNo,2)
        # ajouter une étiquette
        LabelMax = QtGui.QLabel(self)
        LabelMax.setText("Max")
        LabelMax.setFixedHeight(32)
        self.mainLayout.addWidget(LabelMax,self.lineNo,3)
        # ajouter une modification de spin pour définir le maximum du curseur
        self.MaxEdit = QtGui.QSpinBox(self)
        # obtenir l'unité d'angle sous forme de chaîne
        self.MaxEdit.setSuffix(" " + str(FreeCAD.Units.Quantity(1, FreeCAD.Units.Angle))[2:])
        self.MaxEdit.setMaximum(999)
        self.MaxEdit.setMinimum(1)
        self.MaxEdit.setSingleStep(10)
        self.MaxEdit.setValue(360)
        self.MaxEdit.setFixedHeight(32)
        self.MaxEdit.setToolTip("Maximal angle for the slider")
        QtCore.QObject.connect(self.MaxEdit, QtCore.SIGNAL("valueChanged(int)"), self.setMaxEdit)
        self.mainLayout.addWidget(self.MaxEdit,self.lineNo,4)
        # ligne de grille de dialogue suivante
        self.lineNo += 1
        # ajouter un espaceur
        self.mainLayout.addItem(QtGui.QSpacerItem(10,10), 0, 0)
        # ajouter une étiquette
        LabelCurrent = QtGui.QLabel(self)
        LabelCurrent.setText("Current angle:")
        LabelCurrent.setFixedHeight(32)
        self.mainLayout.addWidget(LabelCurrent,self.lineNo,1)
        # afficher l'angle actuel
        self.CurrentAngle = QtGui.QLineEdit(self)
        self.CurrentAngle.setText(str(0))
        self.CurrentAngle.setFixedHeight(32)
        self.CurrentAngle.setToolTip("Current rotation angle")
        self.CurrentAngle.isReadOnly()
        self.mainLayout.addWidget(self.CurrentAngle,self.lineNo,2)
        # ajouter une étiquette pour l'unité
        LabelUnit = QtGui.QLabel(self)
        LabelUnit.setText("deg")
        LabelUnit.setFixedHeight(32)
        self.mainLayout.addWidget(LabelUnit,self.lineNo,3)
        # bouton pour fermer la boîte de dialogue
        self.Close = QtGui.QPushButton(self)
        self.Close.setText("Close")
        self.Close.setFixedHeight(32)
        self.Close.setToolTip("Closes the dialog")
        QtCore.QObject.connect(self.Close, QtCore.SIGNAL("clicked()"), self.CloseClicked)
        self.mainLayout.addWidget(self.Close,self.lineNo,4)
        # place la disposition de grille définie dans la boîte de dialogue
        self.setLayout(self.mainLayout)
        self.update()

    def handleSliderValue(self):
         # définir la valeur du curseur comme angle
         starWheel.Placement.Rotation.Angle = math.radians(self.slider.value())
         # angle de courant de sortie
         self.CurrentAngle.setText(str(self.slider.value()))
         # résoudre les contraintes
         a2p_solver.solveConstraints(document)
         # mettre à jour la vue après la résolution ('Gui' signifie 'interface utilisateur graphique')
         FreeCADGui.updateGui()
         # attendre un certain temps, important de donner du temps pour effectuer des calculs
         time.sleep(timeout)

    def setMinEdit(self):
         # assurez-vous que le minimum est plus petit que le maximum
        if self.MinEdit.value() >=  self.MaxEdit.value():
            self.MaxEdit.setValue(self.MinEdit.value() + 1)
        self.slider.setRange(self.MinEdit.value(), self.MaxEdit.value())

    def setMaxEdit(self):
        # assurer que le minimum est plus petit que le maximum
        if self.MinEdit.value() >=  self.MaxEdit.value():
            self.MinEdit.setValue(self.MaxEdit.value() - 1)
        self.slider.setRange(self.MinEdit.value(), self.MaxEdit.value())

    def CloseClicked(self):
        AnimationDialog.close()

# créer et afficher la boîte de dialogue définie
AnimationDialog = AnimationDlg()
AnimationDialog.show()

# exécuter cette boucle lorsque la boîte de dialogue est visible
while AnimationDialog.isVisible():
    # mettre à jour la vue; important de donner la rétroaction du système d'exploitation le dialogue est vivant
    FreeCADGui.updateGui()
    # amène la boîte de dialogue au premier plan, pour que la boîte de dialogue soit toujours visible
    QtGui.QWidget.raise_(AnimationDialog)
    # valeur de curseur de sortie ici aussi car pendant le calcul, le curseur a peut-être été déplacé
    AnimationDialog.CurrentAngle.setText(str(AnimationDialog.slider.value()))
```


</div>


</div>

La boîte de dialogue définie dans le script ressemble à ceci:

![](images/A2p_AnimationDialog.png )



### Commandes de script 

Pour mieux comprendre la syntaxe du script, voici quelques informations de commande: 
```python starWheel.Placement.Rotation.Angle = math.radians(angle)```

Ici, nous changeons la propriété de placement `Rotation.Angle` de la pièce récupérée précédemment en tant que `starWheel`. Cette propriété obtient l\'angle comme [radian](https://fr.wikipedia.org/wiki/Radian). La fonction `radians()` de la bibliothèque `math` convertit l\'angle du degré en radian.

La propriété `Rotation.Angle` utilise l\'axe de placement actuel de la pièce (dans notre exemple l\'axe X). Pour faire pivoter la pièce, par ex. autour de l\'axe Z, on peut définir l\'axe de rotation (avant d\'appeler la commande de rotation) en utilisant la commande: 
```python starWheel.Placement.Rotation.Axis = FreeCAD.Vector(0,0,1)``` Au lieu de tourner, les pièces peuvent également être déplacées. Pour changer par exemple le placement dans la direction Y de la roue, la commande serait: 
```python starWheel.Placement.Base.y = PositionShift``` Dans ce cas, nous ne définirions pas la variable `angle` mais `PositionShift` que nous modifions à chaque boucle.

Il existe différentes manières de définir le placement d\'une pièce. Certains sont [documentés ici](Placement/fr.md). Malheureusement, il n\'y a pas (encore) de liste avec toutes les commandes de placement possibles. 
```pythona2p_solver.solveConstraints(document, useTransaction=False/True)```

Il s\'agit d\'une commande spécifique à A2plus. Elle résout les contraintes d\'assemblage de l\'assemblage que nous avons précédemment obtenu en tant que `document`. L\'option `useTransaction` spécifie si FreeCAD doit stocker chaque modification dans la pile annuler/refaire. Pour les grandes animations, vous pouvez donc la régler sur `False`.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > A2plus Workbench/fr
