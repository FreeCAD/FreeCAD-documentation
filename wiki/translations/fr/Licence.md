# Licence/fr







{{TOCright}}

## Licences utilisées 

FreeCAD utilise deux licences différentes, l\'une pour l\'application et l\'autre pour la documentation :

**[Licence publique générale limitée GNU (LGPL2+)](http://fr.wikipedia.org/wiki/Licence_publique_g%C3%A9n%C3%A9rale_limit%C3%A9e_GNU)** Pour tout le code source FreeCAD trouvé dans l\'[official Git repository](https://github.com/FreeCAD/FreeCAD)

**[Creative Commons Attribution 3.0 License (CC-BY-3.0)](http://creativecommons.org/licenses/by/3.0/)** Pour la documentation sur <https://www.freecadweb.org>

Voir le [debian copyright file](https://github.com/FreeCAD/FreeCAD/blob/master/package/debian/copyright) (en anglais) pour plus de détails sur les licences utilisées par les différents composants open-source utilisés dans FreeCAD

## Effet des licences 

Vous trouverez ci-dessous une explication plus claire de ce que la licence LGPL signifie pour vous :

#### Tous les utilisateurs 

Tout le monde peut télécharger, utiliser et redistribuer FreeCAD gratuitement, sans aucune restriction. Votre copie de FreeCAD est vraiment la vôtre, tout comme les fichiers que vous produisez avec FreeCAD. Vous ne serez pas obligé de mettre à jour FreeCAD après un certain temps, ni de modifier votre utilisation de FreeCAD. L\'utilisation de FreeCAD ne vous lie à aucun type de contrat ou d\'obligation. Le code source de FreeCAD est public et peut être inspecté. Il est donc possible de vérifier qu\'il ne fait rien à votre insu, tel que l\'envoi de vos données personnelles quelque part.

#### Les utilisateurs professionnels 

FreeCAD peut être utilisé librement pour tout type de travail privé, commercial ou institutionnel. Toute version de FreeCAD peut être déployée et installée n'importe où, à tout moment. Vous pouvez également modifier et adapter FreeCAD à vos propres fins sans aucune restriction. Cependant, vous ne pouvez pas engager la responsabilité des développeurs FreeCAD sur d\'éventuels dommages ou pertes commerciales pouvant résulter de l\'utilisation de FreeCAD.

#### Développeurs open source 

Vous pouvez utiliser FreeCAD comme base pour développer votre propre application ou simplement l\'étendre en créant de nouveaux modules. Si FreeCAD est intégré à votre propre application, vous pouvez choisir la licence GPL ou LGPL, ou toute autre licence compatible avec LGPL, pour autoriser ou non l\'utilisation de votre travail dans un logiciel propriétaire. Si vous développez un module à utiliser comme extension et n\'incluez aucun code FreeCAD dans celui-ci, vous pouvez choisir la licence de votre choix. Toutefois, si vous souhaitez que votre module soit utilisé autant que possible, il est judicieux d\'utiliser la même licence LGPL que FreeCAD, afin de pouvoir utiliser plus facilement des parties de votre code dans d\'autres modules ou même dans FreeCAD.

#### Les développeurs professionnels 

Vous pouvez utiliser FreeCAD comme base pour votre propre application sans être obligé de rendre votre application open source. La licence LGPL demande toutefois deux choses de base : 1) informer clairement vos utilisateurs que votre application utilise FreeCAD et que FreeCAD est sous licence LGPL, et 2) que vous séparez clairement votre propre application des composants FreeCAD. Cela se fait généralement soit en créant un lien dynamique avec les composants FreeCAD, afin de permettre aux utilisateurs de le modifier, soit en mettant le code source de FreeCAD, ainsi que les modifications que vous y avez apportées, à la disposition de vos utilisateurs. Vous obtiendrez une assistance des développeurs FreeCAD, à condition que ce ne soit pas \"à sens unique\".

#### Fichiers

Les modèles et autres fichiers produits avec FreeCAD ne sont soumis à aucune licence indiquée ci-dessus, ni à aucun type de restriction ou de propriété. Vos fichiers sont vraiment les vôtres. Vous pouvez définir le propriétaire du fichier et spécifier vos propres conditions de licence pour les fichiers que vous créez dans FreeCAD, via le menu Fichier → Informations sur le projet.

## Déclaration du fondateur 

Je sais que la discussion sur le *« droit »* de licence pour l\'open source a occupé une partie importante de la bande passante Internet alors voici la raison pour laquelle, à mon avis, FreeCAD doit être sous licence LGPL.

J\'ai choisi les licences [LGPL](http://fr.wikipedia.org/wiki/Licence_publique_g%C3%A9n%C3%A9rale_limit%C3%A9e_GNU) pour le projet, je sais qu'il y a des pros et des anti LGPL et je vous donnerai quelques raisons de cette décision.

FreeCAD est le mélange d\'une bibliothèque et d\'une application, de sorte que le GPL serait un peu fort pour cela. Il permettrait d\'éviter l\'écriture de modules commerciaux pour FreeCAD car elle empêcherait la liaison avec les librairies de base FreeCAD. Vous pouvez vous demander pourquoi des modules commerciaux ? Linux aurait-il autant de succès si les bibliothèques C GNU étaient sous licences GPL, et empêchaient donc les liaisons avec des applications non GPL ? Et bien que j\'aime la liberté de Linux, je veux aussi être en mesure d\'utiliser les très bon pilotes graphique NVIDIA 3D. Je comprends et j\'accepte les raisons pour lesquels NVIDIA ne souhaite pas donner les codes des pilotes. Nous travaillons TOUS pour des entreprises, et nous avons besoin d'argent, ou au moins de nourriture\... Pour moi, une coexistence de l\'open source et les logiciels à code source propriétaire n\'est pas une mauvaise chose, quand il obéit à des règles de la licence LGPL. Je voudrais voir quelqu\'un écrire un processus d'import / export CATIA pour FreeCAD et de le distribuer gratuitement ou pour de l\'argent. Je n\'aime pas forcer à donner plus que ce qu\'il ne veut. Ce ne serait pas bon ni pour lui ni pour FreeCAD.

Néanmoins, cette décision est prise seulement pour le système de base de FreeCAD. Chaque auteur d\'un module d\'application peut prendre sa propre décision.


{{Quote|Jürgen Riegel|15 October 2006}}





 

[Category:Developer Documentation](Category:Developer_Documentation.md)
