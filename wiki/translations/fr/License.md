# License/fr
## Licences utilisées dansFreeCAD 

FreeCAD utilise deux licences différentes, l\'une pour l\'application et l\'autre pour la documentation :

**[Licence publique générale limitée GNU (LGPL2+)](https://fr.wikipedia.org/wiki/Licence_publique_g%C3%A9n%C3%A9rale_limit%C3%A9e_GNU)** pour tout le code source FreeCAD trouvé dans le [dépôt officiel Git](https://github.com/FreeCAD/FreeCAD). Le + signifie que vous pouvez également, à votre choix, utiliser FreeCAD selon les termes d\'une version ultérieure de la licence, telle que la LGPL3.

**[Creative Commons Attribution 3.0 License (CC-BY-3.0)](http://creativecommons.org/licenses/by/3.0/)** pour la [documentation](https://wiki.freecad.org/Main_Page/fr) et le [site web](https://www.freecad.org/index.php?lang=fr).

Voir le [debian copyright file](https://github.com/FreeCAD/FreeCAD/blob/master/package/debian/copyright) (en anglais) pour plus de détails sur les licences utilisées par les différents composants open-source utilisés dans FreeCAD



## Signification des licences 

Vous trouverez ci-dessous une explication plus claire de ce que la licence LGPL signifie pour vous :



#### Tous les utilisateurs 

Tout le monde peut **télécharger, utiliser et redistribuer FreeCAD gratuitement**, sans aucune restriction. Votre copie de FreeCAD est vraiment la vôtre, tout comme les fichiers que vous produisez avec FreeCAD. Vous ne serez pas obligé de mettre à jour FreeCAD après un certain temps, ni de modifier votre utilisation de FreeCAD. L\'utilisation de FreeCAD ne vous lie à aucun type de contrat ou d\'obligation. Le code source de FreeCAD est public et peut être inspecté. Il est donc possible de vérifier qu\'il ne fait rien à votre insu, tel que l\'envoi de vos données personnelles quelque part.



#### Les utilisateurs professionnels 

FreeCAD peut être **utilisé librement pour tout type de travail**, privé, commercial ou institutionnel. Toute version de FreeCAD peut être déployée et installée n'importe où, à tout moment. Vous pouvez également modifier et adapter FreeCAD à vos propres fins sans aucune restriction. Cependant, vous ne pouvez pas engager la responsabilité des développeurs FreeCAD sur d\'éventuels dommages ou pertes commerciales pouvant résulter de l\'utilisation de FreeCAD.



#### Développeurs de logiciels open source 

Vous pouvez utiliser FreeCAD comme base pour développer votre propre application ou simplement l\'étendre en créant de nouveaux modules. Si FreeCAD est intégré à votre propre application, vous pouvez choisir la licence GPL ou LGPL, ou toute autre licence compatible avec LGPL, pour autoriser ou non l\'utilisation de votre travail dans un logiciel propriétaire. Si vous développez un module à utiliser comme extension et n\'incluez aucun code FreeCAD dans celui-ci, vous pouvez alors choisir la licence que vous voulez. Cependant, si vous souhaitez que votre module soit un jour intégré à FreeCAD, il est préférable d\'utiliser la même licence LGPL que FreeCAD, car FreeCAD n\'accepte que les codes sous licence LGPL, MIT ou BSD.



#### Développeurs de logiciels au code fermé 

La licence LGPL vous permet d\'utiliser FreeCAD comme composant de votre propre application, et vous n\'êtes pas obligé de rendre votre application open source. Vous obtiendrez le soutien des développeurs de FreeCAD tant qu\'il ne s\'agit pas d\'une \"voie à sens unique\". La licence stipule toutefois deux conditions importantes :

1\) Vous devez clairement **informer vos utilisateurs que votre application utilise FreeCAD** et que FreeCAD est LGPL.

2\) La licence LGPL stipule également que vos utilisateurs doivent être en mesure d\'échanger votre composant FreeCAD modifié avec l\'équivalent FreeCAD original. Pour ce faire, il faut établir un lien dynamique avec les composants FreeCAD, de sorte que les utilisateurs soient autorisés à les modifier. Cependant, cela est souvent difficile à réaliser en raison des exigences actuelles. Chez FreeCAD, nous comprenons que le point important ici est de ne pas restreindre la liberté donnée aux utilisateurs de FreeCAD par la licence LGPL. Ainsi, un équivalent à la liaison dynamique est d\'offrir le choix à vos utilisateurs, en **rendant vos utilisateurs conscients de la possibilité d\'utiliser FreeCAD gratuitement**. Cela peut se faire de plusieurs manières.

Si l\'une des deux conditions ci-dessus est inacceptable pour vous ou ne peut être mise en œuvre, vous devez alors rendre votre composant FreeCAD également LGPL et publier le code source avec toutes les modifications que vous y avez apportées.

Il existe un cas particulier appelé **derivatives**, c\'est-à-dire lorsque vous publiez essentiellement une version \"rebrandée\" de FreeCAD. Les dérivés qui ne sont pas open-source sont interdits par la licence LGPL. La communauté FreeCAD est active et efficace pour trouver les versions rebrandées, les signaler aux plateformes où elles ont été trouvées et les exposer jusqu\'à ce qu\'elles soient supprimées.



#### Fichiers

Les modèles et autres fichiers produits avec FreeCAD ne sont soumis à aucune licence indiquée ci-dessus, ni à aucun type de restriction ou de propriété. Vos fichiers sont vraiment les vôtres. Vous pouvez définir le propriétaire du fichier et spécifier vos propres conditions de licence pour les fichiers que vous créez dans FreeCAD, via le menu Fichier → Informations sur le projet.

## Logo

Le logo FreeCAD est une [marque déposée appartenant à la FPA (association du projet FreeCAD)](https://fpa.freecad.org/documents/Trademark.pdf). Cela signifie que la [FPA](https://fpa.freecad.org) est le seul organisme autorisé à dire qui a le droit d\'utiliser le logo FreeCAD ou non. Les fichiers du logo, qui font partie du code source de FreeCAD ou qui sont disponibles ailleurs, par exemple sur ce wiki, sont toujours sous les mêmes licences que le reste de FreeCAD (LGPL pour le code source et Creative Commons pour ce wiki). Vous êtes toujours libre d\'utiliser le logo FreeCAD n\'importe où, dans les mêmes conditions que le reste de FreeCAD, ce qui signifie, en gros, que vous devez l\'utiliser pour faire référence à FreeCAD, et ne pas l\'utiliser, par exemple, pour votre propre produit, ou de toute autre manière qui ne fait pas référence à FreeCAD.



## Déclaration du principal développeur 

Je sais que la discussion sur le *\"droit\"* de licence pour l\'open source a occupé une partie importante de la bande passante d\'Internet alors voici la raison pour laquelle, à mon avis, FreeCAD doit être sous licence LGPL.

J\'ai choisi les licences [LGPL](http://fr.wikipedia.org/wiki/Licence_publique_g%C3%A9n%C3%A9rale_limit%C3%A9e_GNU) pour le projet, je sais qu'il y a des pros et des anti LGPL et je vous donnerai quelques raisons de cette décision.

FreeCAD est le mélange d\'une bibliothèque et d\'une application, de sorte que le GPL serait un peu fort pour cela. Il permettrait d\'éviter l\'écriture de modules commerciaux pour FreeCAD car elle empêcherait la liaison avec les librairies de base FreeCAD. Vous pouvez vous demander pourquoi des modules commerciaux ? Linux aurait-il autant de succès si les bibliothèques C GNU étaient sous licences GPL, et empêchaient donc les liaisons avec des applications non GPL ? Et bien que j\'aime la liberté de Linux, je veux aussi être en mesure d\'utiliser les très bon pilotes graphique NVIDIA 3D. Je comprends et j\'accepte les raisons pour lesquels NVIDIA ne souhaite pas donner les codes des pilotes. Nous travaillons TOUS pour des entreprises, et nous avons besoin d'argent, ou au moins de nourriture\... Pour moi, une coexistence de l\'open source et les logiciels à code source propriétaire n\'est pas une mauvaise chose, quand il obéit à des règles de la licence LGPL. Je voudrais voir quelqu\'un écrire un processus d'import / export CATIA pour FreeCAD et de le distribuer gratuitement ou pour de l\'argent. Je n\'aime pas forcer à donner plus que ce qu\'il ne veut. Ce ne serait pas bon ni pour lui ni pour FreeCAD.

Néanmoins, cette décision est prise seulement pour le système de base de FreeCAD. Chaque auteur d\'un module d\'application peut prendre sa propre décision.


{{Quote|Jürgen Riegel|15 October 2006}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > License/fr
