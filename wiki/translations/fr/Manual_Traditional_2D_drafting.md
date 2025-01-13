# Manual:Traditional 2D drafting/fr
{{Manual:TOC}}

L\'atelier Draft de FreeCAD sert de passerelle entre le dessin 2D et la modélisation 3D, ce qui le rend unique par rapport aux systèmes de CAO 2D traditionnels tels qu\'AutoCAD. Alors que FreeCAD fonctionne dans un environnement entièrement 3D, l\'atelier Draft est conçu pour fournir aux utilisateurs des outils de dessin 2D familiers tout en offrant la flexibilité d\'une transition en douceur entre les esquisses 2D et les objets 3D. Par exemple, vous pouvez définir des plans de travail personnalisés pour dessiner sur des surfaces ou des orientations spécifiques, ce qui permet de construire des modèles paramétriques. FreeCAD étant paramétrique, toute modification apportée aux dimensions est automatiquement répercutée sur l\'ensemble du projet.

L\'un des points forts de l\'atelier Draft est son ensemble d\'outils complet, qui comprend à la fois des outils de dessin de base et des outils de modification avancés. Ces outils peuvent être utilisés non seulement pour le dessin en 2D, mais aussi pour la manipulation d\'objets dans l\'espace 3D. Vous pouvez définir des plans de travail, des grilles et appliquer des contraintes pour vous assurer que les relations géométriques restent intactes dans votre conception. Les objets dessinés peuvent être modifiés et repositionnés à l\'aide de modes d\'accrochage et d\'une variété de contraintes, ce qui facilite grandement la précision du dessin.

Quelques-uns des outils présents dans l\'atelier de dessin :

1.  Outils de dessin :

-   <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Ligne](Draft_Line/fr.md), <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Polyligne](Draft_Wire/fr.md) : ces outils permettent de créer des segments de ligne droite ou des polylignes continues, qui peuvent être contraints et convertis en formes 3D.
-   <img alt="" src=images/Draft_Circle.svg  style="width:16px;"> [Cercle](Draft_Circle/fr.md), <img alt="" src=images/Draft_Ellipse.svg  style="width:16px;"> [Ellipse](Draft_Ellipse/fr.md), et <img alt="" src=images/Draft_Arc.svg  style="width:16px;"> [Arc](Draft_Arc/fr.md) : utilisées pour définir des formes circulaires et elliptiques de base, avec des options pour une manipulation plus poussée.

1.  Outils de manipulation :

-   <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Déplacer](Draft_Move/fr.md), <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Pivoter](Draft_Rotate/fr.md) ou <img alt="" src=images/Draft_Scale.svg  style="width:16px;"> [Échelle](Draft_Scale/fr.md) : ces opérations fonctionnent aussi bien en 3D qu\'en 2D, ce qui offre une grande souplesse dans le positionnement des objets.
-   <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Décaler](Draft_Offset/fr.md) : semblable aux systèmes de CAO traditionnels, cette fonction vous permet de créer des lignes ou des courbes parallèles.
-   <img alt="" src=images/Draft_Trimex.svg  style="width:16px;"> [Ajuster ou prolonger](Draft_Trimex/fr.md) et <img alt="" src=images/Draft_Stretch.svg  style="width:16px;"> [Étirer](Draft_Stretch/fr.md) : modifier les lignes et les formes en les coupant ou en les prolongeant pour qu\'elles croisent ou rencontrent d\'autres objets.
-   <img alt="" src=images/Draft_Mirror.svg  style="width:16px;"> [Miroir](Draft_Mirror/fr.md) et <img alt="" src=images/Draft_Array.svg  style="width:16px;"> [Réseau](Draft_Array/fr.md) : ces outils reproduisent et modèlent les objets, ce qui est idéal pour les composants répétitifs.

Le système d\'aimantation de l\'atelier Draft de FreeCAD est conçu pour la précision. Que vous travailliez en 2D ou en 3D, vous pouvez vous aimanter à des points critiques tels que les points d\'extrémité, les points médians et les centres de cercles, ce qui facilite le positionnement des éléments les uns par rapport aux autres. Des modes tels que l\'aimantation perpendiculaire, tangente et à l\'intersection améliorent encore la précision. Associés au plan de travail et au système de grille, ces outils garantissent l\'alignement précis des objets et des composants.

La nature paramétrique de FreeCAD permet d\'appliquer des contraintes aux éléments dessinés, ce qui garantit que les relations géométriques restent intactes. Par exemple, vous pouvez rendre les lignes parallèles ou perpendiculaires et définir des distances fixes entre les éléments. Ces contraintes peuvent être ajustées ultérieurement, ce qui rend les modifications de conception fluides et cohérentes sur l\'ensemble du projet. L\'atelier Draft s\'intègre également de manière transparente à d\'autres ateliers FreeCAD, tels que Sketcher, conçu pour une conception 2D paramétrique plus contraignante, et TechDraw, qui produit des dessins techniques en 2D à des fins de documentation.

Les fonctionnalités avancées de l\'atelier Draft incluent la possibilité d\'importer et d\'exporter des fichiers dans des formats tels que DXF et SVG, ce qui vous permet de travailler avec des utilisateurs d\'autres programmes de CAO ou de partager des conceptions avec eux. Les scripts Python améliorent encore les capacités de FreeCAD, vous permettant d\'automatiser des tâches ou de créer des flux de travail personnalisés. Vous pouvez écrire des scripts qui génèrent des objets de dessin en fonction de règles géométriques spécifiques, rationalisant ainsi les tâches répétitives.

Pour montrer le travail et les possibilités de l\'ébauche de travail, nous réaliserons un exercice simple, dont le résultat sera ce petit dessin, montrant le plan d\'étage d\'une petite maison qui ne contient qu\'un dessus de cuisine (un plan d\'appartement très absurde, mais on peut faire ce que nous voulons ici, n\'est-ce pas?) :

<img alt="" src=images/Exercise_cabin_01.jpg  style="width:600px;">

-   Passez à l**\'atelier Draft**\'
-   Comme dans toutes les applications de dessin technique, il est sage de configurer votre environnement correctement, cela vous fera gagner beaucoup de temps. Si vous souhaitez personnaliser votre expérience dans l\'atelier Draft, vous pouvez facilement le faire en ajustant divers paramètres dans le panneau des préférences de Draft en allant dans **Édition → Préférences → Draft**. Dans cet exercice, cependant, nous agirons comme si ces paramètres étaient laissés à leurs valeurs par défaut.

<img alt="" src=images/FreeCAD_DraftPreferences.png  style="width:600px;">

-   Le panneau des préférences de Draft de FreeCAD vous permet de personnaliser divers aspects de votre environnement de dessin 2D. Dans les **Paramètres généraux**, vous pouvez définir le plan de travail par défaut, ajuster la précision décimale et définir la largeur, le style et la couleur de ligne par défaut pour les objets. La section **Grille et aimantation** vous permet de contrôler la visibilité de la grille, l\'espacement et les modes d\'aimantation, ce qui permet un alignement et un positionnement précis des éléments. Les options **Paramètres graphiques** vous permettent de personnaliser l\'apparence des objets et de la grille, y compris les couleurs de ligne et de remplissage. Dans **Texte et dimensions**, vous pouvez configurer la taille, la police et la couleur du texte par défaut pour les annotations, afin de garantir la clarté des dessins techniques.

![](images/Draft_toolbars.png )

L\'activation de tous les boutons d\'accrochage est pratique, mais ralentit également le dessin, car il faut effectuer davantage de calculs lorsque vous déplacez le curseur de la souris. Il est souvent préférable de ne garder que ceux que vous utiliserez réellement.

-   Commençons par activer le **mode construction**, ce qui nous permettra de tracer des lignes directrices sur lesquelles nous dessinerons notre géométrie finale. Vous pouvez le faire en appuyant sur la commande <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:24px;"> [Basculer en mode construction](Draft_ToggleConstructionMode/fr.md).
-   Si vous préférez, vous pouvez régler le plan de travail sur XY. Cela verrouillera le plan de travail, garantissant qu\'il reste sur le plan XY quelle que soit la façon dont vous changez la vue. Si vous choisissez de ne pas le faire, le plan de travail s\'adaptera automatiquement à la vue en cours, ce qui signifie que vous devrez vous assurer que vous êtes dans la vue du dessus chaque fois que vous souhaitez dessiner sur le plan XY (sol) afin d\'éviter des changements d\'orientation involontaires.

Maintenant basculez sur l\'atelier Part et commencez à créer la première patte de la table.

-   Appuyez sur le bouton <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> **Draft Rectangle**.
-   Dessinez un rectangle de 2 mètres par 2 mètres à partir du point (0,0,0), en laissant la coordonnée Z à zéro. Vous pouvez effectuer ce processus de manière efficace en utilisant le clavier, sans avoir besoin de la souris. Il suffit de taper :
    -   **re**, **Enter**, **Enter**, **Enter**, 2m, **Enter**, 2m, **Enter**, 0 et **Enter**.

Ce flux de travail au clavier accélère la rédaction, en particulier pour les tâches répétitives ou les saisies de précision, ce qui en fait un outil idéal pour les utilisateurs désireux de rationaliser leur flux de travail. Vous pouvez visualiser les frappes pour chaque objet en survolant le bouton correspondant.

-   Dupliquez ce rectangle de 15 cm à l\'intérieur, en utilisant l\'outil <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Décalage](Draft_Offset/fr.md), en activant son mode Copie et en lui donnant une distance de 15 cm :

<img alt="" src=images/Exercise_cabin_02.png  style="width:600px;">

-   Nous pouvons ensuite tracer quelques lignes verticales pour définir l\'emplacement des portes et des fenêtres, en utilisant l\'outil <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Ligne](Draft_Line/fr.md). (notez que la case du mode « relatif » doit être décochée pour cette étape). Le croisement de ces lignes avec nos deux rectangles nous donnera des intersections utiles sur lesquelles nous pourrons fixer nos murs. Tracez la première ligne en définissant les points suivants :
    -   **P1** (15cm, 1m, 0) et **P2** (15cm, 3m, 0).
-   Nous allons maintenant dupliquer cette ligne 5 fois. Appuyez sur la <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Déplacer](Draft_Move/fr.md) avec le mode <img alt="" src=images/Draft_Clone.svg  style="width:16px;"> [Cloner](Draft_Clone/fr.md) activé. Assurez-vous que le **Mode relatif** est activé. Le mode Copie permet de s\'assurer que chaque mouvement crée une nouvelle ligne au lieu de déplacer l\'original, tandis que le mode relatif permet de définir des mouvements basés sur des distances relatives, ce qui facilite le positionnement sans avoir à calculer les coordonnées exactes. Commencez par sélectionner la ligne d\'origine et lancez l\'opération de déplacement en choisissant un point de départ quelconque, tel que (0,0,0). Après chaque déplacement, effectuez l\'opération suivante sur la ligne nouvellement créée, de sorte que chaque copie s\'appuie sur la précédente. Définissez les extrémités relatives de chaque nouvelle ligne
    -   line001: x: 10cm
    -   line002: x: 120cm
    -   line003: x: -55cm, y: -2m
    -   line004: x: 80cm
    -   line005: x: 15cm

<img alt="" src=images/Exercise_cabin_03.jpg  style="width:600px;">

-   C\'est tout ce dont nous avons besoin maintenant, nous pouvons donc désactiver le mode de construction. Vérifiez que toute la géométrie de la construction a été placée dans un groupe \"Construction\", ce qui permet de le masquer tout à la fois ou même de le supprimer complètement plus tard.
-   Maintenant, dessinons nos deux morceaux de mur en utilisant l\'outil <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Polyligne](Draft_Wire/fr.md). Assurez-vous que l\'outil <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:16px;"> [Aimantation d\'intersection](Draft_Snap/fr.md) est activé, car nous aurons besoin de nous aimanter aux intersections de nos lignes et rectangles. Dessinez deux fils comme suit, en cliquant sur tous les points de leurs contours. Pour les fermer, cliquez à nouveau sur le premier point, ou appuyez sur le bouton *Fermer* :

<img alt="" src=images/Exercise_cabin_04.jpg  style="width:600px;">

-   Nous pouvons donner aux murs un joli motif de hachures. Sélectionnez les deux murs, assurez-vous que leur propriété **Make Face** (onglet Données) est réglée sur **`True`**, puis réglez leur propriété **Pattern** sur **Simple** (onglet Vue), et leur **Pattern size** à votre convenance, par exemple **0.005**.

<img alt="" src=images/Draft_Pattern.png  style="width:600px;">

-   Nous pouvons maintenant cacher la géométrie de construction en cliquant avec le bouton droit sur le groupe Construction et en choisissant **Masquer la sélection**.
-   Dessinons maintenant les fenêtres et les portes. Assurez-vous que l\'<img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:16px;"> [aimantation au point milieu](Draft_Snap/fr.md) est activé et tracez six lignes comme suit :

<img alt="" src=images/Exercise_cabin_06.jpg  style="width:600px;">

-   Nous allons maintenant changer la ligne de porte pour créer un symbole de porte ouvert. Commencez par faire tourner la ligne à l\'aide de l\'outil <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Pivoter](Draft_Rotate/fr.md). Cliquez sur l\'extrémité de la ligne en tant que centre de rotation, lui donner un angle de départ de **0** et un angle d\'extrémité de **-90**.
-   Ensuite, créez l\'arc d\'ouverture avec l\'outil <img alt="" src=images/Draft_Arc.svg  style="width:16px;"> [Arc](Draft_Arc/fr.md). Choisissez le même point que le centre de rotation que nous avons utilisé dans l\'étape précédente comme le centre, cliquez sur l\'autre point de la ligne pour donner le rayon, puis les points de début et de fin comme suit :

<img alt="" src=images/Exercise_cabin_07.jpg  style="width:600px;">

-   Nous pouvons maintenant placer des meubles. Pour commencer, placez un compteur en dessinant un rectangle du coin supérieur gauche et en lui donnant une largeur de 170cm et une hauteur de -60cm. Dans l\'image ci-dessous, la propriété **Transparence** du rectangle est configurée à 80%, pour lui donner un bon aspect des meubles.
-   Ensuite, ajoutons un lavabo et une table de cuisson. Dessiner ces types de symboles à la main peut être très fastidieux, et ils sont généralement faciles à trouver sur Internet, par exemple sur <http://www.cad-blocks.net>. Dans la section **Téléchargements** ci-dessous, pour plus de commodité, nous avons récupéré un évier et une table de cuisson sur ce site et les avons sauvegardés en tant que fichiers DXF. Vous pouvez télécharger ces deux fichiers en visitant les liens ci-dessous et en cliquant avec le bouton droit sur le bouton **Raw**, puis en sélectionnant **Enregistrer sous**.
-   L\'insertion d\'un fichier DXF dans un document FreeCAD ouvert peut être effectuée soit en choisissant l\'option du menu **Fichier → Importer**, soit en faisant glisser et déposer le fichier DXF depuis votre explorateur de fichiers dans la fenêtre FreeCAD. Le contenu des fichiers DXF peut ne pas apparaître directement au centre de votre vue actuelle, selon l\'endroit où ils se trouvaient dans le fichier DXF. Vous pouvez utiliser le menu **Affichage → Affichage standard → Afficher tout** pour faire un zoom arrière et trouver les objets importés. Insérez les deux fichiers DXF et déplacez-les à un emplacement approprié sur le dessus de la table :

<img alt="" src=images/Exercise_cabin_08.jpg  style="width:600px;">

-   Nous pouvons maintenant placer quelques dimensions à l\'aide de l\'outil <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [Dimension](Draft_Dimension/fr.md). Pour créer une dimension, vous commencez par sélectionner trois points : le premier point définit le début de la mesure, le deuxième point définit le point final et le troisième point détermine l\'endroit où la ligne de dimension et le texte seront placés. En cliquant soigneusement sur ces points, vous vous assurez que la dimension représente bien la distance entre les deux points sélectionnés. Si vous voulez forcer la dimension à être parfaitement horizontale ou verticale, même si les points de départ et d\'arrivée ne sont pas alignés, maintenez la touche **Maj** enfoncée tout en cliquant sur le deuxième point. La dimension est ainsi verrouillée dans l\'orientation souhaitée. Vous pouvez encore affiner la cote en ajustant les propriétés telles que la taille du texte, la précision et la couleur dans le panneau des propriétés, afin de vous assurer que les cotes correspondent aux normes visuelles et techniques de votre projet.
-   Vous pouvez modifier la position d\'un texte de cote en double-cliquant sur la dimension dans l\'arborescence. Un point de contrôle vous permettra de déplacer le texte graphiquement. Dans notre exercice, les textes \"0.15\" ont été déplacés pour une meilleure clarté.
-   Vous pouvez modifier le contenu du texte de cote en éditant leur propriété **Override**. Dans notre exemple, les textes des dimensions des portes et des fenêtres ont été édités pour indiquer leurs hauteurs :

<img alt="" src=images/Exercise_cabin_09.jpg  style="width:600px;">

-   Ajoutons des textes de description à l\'aide de l\'outil <img alt="" src=images/Draft_Text.svg  style="width:16px;"> [Texte](Draft_Text/fr.md). Cliquez sur un point pour positionner le texte, puis entrez les lignes de texte, en appuyant sur Entrée après chaque ligne. Pour terminer, appuyez deux fois sur Entrée.
-   Les lignes de repère (également appelées «leaders») qui relient les textes à l\'élément qu\'ils décrivent se font simplement avec l\'outil Polyligne. Dessinez les polylignes, à partir de la position du texte, jusqu'à l\'endroit décrit. Une fois que cela est fait, vous pouvez ajouter une bille ou une flèche à la fin des fils en définissant leur propriété **End Arrow** (extrémité de la flèche) sur **TRUE**.

<img alt="" src=images/Exercise_cabin_10.jpg  style="width:600px;">

-   Notre dessin est maintenant complet ! Compte tenu du nombre d\'objets contenus dans le dessin, il convient de procéder à un certain nombre d\'ajustements et de restructurations avant de considérer que le dessin est terminé. L\'organisation de tous les éléments en groupes clairs et logiques permettra non seulement de maintenir le projet bien structuré, mais aussi de faciliter considérablement la navigation et la compréhension du fichier par d\'autres personnes. En regroupant des éléments connexes, tels que des meubles, des appareils ou des éléments architecturaux, vous pouvez simplifier la mise en page et améliorer la clarté de la conception. Les modifications ou ajustements futurs seront également beaucoup plus faciles à gérer, en particulier si le projet doit être partagé ou faire l\'objet d\'une collaboration. En outre, une structure claire permet à toute personne qui examine le dessin de trouver rapidement des éléments spécifiques sans avoir à fouiller dans un espace de travail encombré, ce qui contribue en fin de compte à un produit final plus professionnel et plus soigné. Prendre le temps de s\'organiser maintenant peut faire gagner beaucoup de temps et d\'efforts par la suite :

<img alt="" src=images/Draft_Organised.png  style="width:600px;">

-   Nous pouvons maintenant imprimer notre travail en le plaçant sur une feuille de dessin, que nous allons montrer plus loin dans ce manuel, ou exporter directement notre dessin vers d\'autres applications de CAO en l\'exportant vers un fichier DXF. Il suffit de sélectionner notre groupe \"Floor Plan\", sélectionnez le menu **Fichier → Exporter**, et sélectionnez le format **Autodesk DXF**. Le fichier peut alors être ouvert dans n\'importe quelle autre application CAO 2D telle que [LibreCAD](http://www.librecad.org). Vous pouvez remarquer quelques différences selon les configurations de chaque application.

<img alt="" src=images/Exercise_cabin_12.jpg  style="width:600px;">

-   L\'aspect le plus important de l\'atelier Draft est que la géométrie 2D que vous créez peut servir de base à la création d\'objets 3D. Vous pouvez facilement extruder ces formes en 3D à l\'aide de l\'outil <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part Extrusion](Part_Extrude/fr.md) dans l\'[atelier Part](Part_Workbench/fr.md). Si vous préférez rester dans l\'atelier Draft, vous pouvez utiliser l\'outil <img alt="" src=images/Draft_Trimex.svg  style="width:16px;"> [Ajuster ou prolonger](Draft_Trimex/fr.md), qui combine les fonctionnalités de découpe, d\'extension et d\'extrusion. L\'outil Ajuster ou prolonger exécute essentiellement une extrusion de pièce sous le capot, mais le fait « à la manière d\'une ébauche », ce qui vous permet d\'indiquer visuellement et de fixer la longueur d\'extrusion, vous donnant ainsi un meilleur contrôle et une plus grande précision lorsque vous travaillez directement dans votre environnement d\'ébauche. Cette flexibilité rend la transition de la 2D à la 3D transparente et intuitive, en particulier pour ceux qui sont familiers avec les flux de travail 2D, tout en offrant des capacités de modélisation 3D avancées.
-   En appuyant sur le bouton Sélectionner le <img alt="" src=images/Draft_SelectPlane.svg  style="width:16px;"> [plan de travail](Draft_SelectPlane/fr.md) après avoir sélectionné une face d\'un objet, vous pouvez également placer le plan de travail n\'importe où et, par conséquent, dessiner des objets Draft dans différents plans, par exemple sur le dessus des murs. Ceux-ci peuvent ensuite être extrudés pour former d\'autres solides 3D. Expérimentez le réglage du plan de travail sur l\'une des faces supérieures des murs, puis tracez des rectangles dessus.

<img alt="" src=images/Exercise_cabin_13.jpg  style="width:600px;">

-   Toutes sortes d\'ouvertures peuvent également être faites aussi facilement en dessinant des objets Draft sur les faces des murs, puis en les extrudant, puis en utilisant les outils booléens de l'atelier Part pour les soustraire d\'un autre solide, comme nous l\'avons vu dans le chapitre précédent.

Fondamentalement, l\'atelier Draft offre une approche plus graphique et intuitive de la création d\'opérations de base, similaires à celles de l\'atelier Part. Dans l\'atelier Part, le positionnement des objets implique souvent d\'ajuster manuellement des paramètres tels que les valeurs de placement (pour la position, la rotation, etc.), ce qui vous donne un contrôle précis mais peut parfois sembler moins intuitif, en particulier pour les modifications rapides. En revanche, l\'atelier Draft vous permet d\'effectuer ces mêmes opérations visuellement à l\'écran, ce qui facilite le déplacement, la rotation et la manipulation des objets directement dans l\'espace de travail à l\'aide d\'outils d\'accrochage et d\'options de positionnement relatif.

C\'est dans cette différence que les ateliers se complètent. L\'atelier Draft est idéal pour une conception rapide et interactive, car il permet de dessiner et de positionner des objets sans avoir à saisir constamment des valeurs numériques précises. En revanche, l\'atelier Part offre un contrôle paramétrique plus détaillé sur les propriétés des objets, ce qui le rend plus adapté à des ajustements très précis, notamment dans le cadre de projets d\'ingénierie ou de conception technique.

La beauté de FreeCAD est que vous n\'avez pas besoin de choisir entre l\'un ou l\'autre. Vous pouvez créer des [barres d\'outils personnalisées](Interface_Personnalisation/fr.md) en combinant des outils des ateliers Draft et Part, ce qui vous donne la possibilité de passer d\'une méthode graphique à une méthode paramétrique en fonction de vos besoins. Vous pouvez ainsi bénéficier du meilleur des deux mondes - des ajustements rapides à l\'écran à partir de l\'atelier Draft et la précision de l\'atelier Part - en fonction des besoins de votre projet. En outre, l\'utilisation de raccourcis clavier et de barres d\'outils personnalisées peut accélérer votre flux de travail, en facilitant la transition entre les différentes opérations sans interrompre votre processus de conception.



## Téléchargements

-   Le fichier créé lors de cet exercice : <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/cabin.FCStd>
-   Le fichier DXF de l\'évier : <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/sink.dxf>
-   Le fichier DXF de la table de cuisson : <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/cooktop.dxf>
-   Le fichier final DXF produit lors de cet exercice : <Https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.dxf>



## En relation 

-   [L'atelier Draft](Draft_Workbench/fr.md)
-   [Draft Aimantation](Draft_Snap/fr.md)
-   [Draft Le plan de travail](Draft_SelectPlane/fr.md)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Draft](Category_Draft.md) > Manual:Traditional 2D drafting/fr
