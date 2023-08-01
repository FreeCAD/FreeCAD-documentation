# History/fr
\_\_FORCETOC\_\_

## Historique

<img alt="Balbutiements FreeCAD, version inconnue." src=images/Screenshot_mesh.jpg  style="width:300px;"> <img alt="FreeCAD, version 0.7 de 2009." src=images/Part_BooleanOperations.png  style="width:300px;">

### Comment tout a démarré 

FreeCAD a commencé en janvier 2001 lorsque [Jürgen Riegel](User_Jriegel.md) a commencé à travailler sur le projet Cas.CADE. Cas.CADE était un framework de développement logiciel commercial qui comprenait un [noyau de modélisation géométrique](Glossary/fr#Geometric_modeling_kernel.md) (ou noyau CAO): il a été publié sous une licence open source en 2000 et renommé [Open CASCADE](OpenCASCADE/fr.md). Cela a rendu possible la réalisation d\'un programme CAO 3D open source, car avoir à programmer un noyau CAO à partir de zéro aurait nécessité un travail énorme.

Le discours de Jürgen :


{{Quote|text=''The FreeCAD project was started by me in January 2001, as a so called GOM (Graphical Object Modeler), with the idea to use Qt, Python and Cas.CADE, an commercial CAD-Kernel that time I used in Daimler's projects. Cas.CADE gone open source shortly before, so the time seemed right to try a move in the, at that time, empty space of open source CAD. I had a two year experience with OpenCascade in a project called QSpect in which, at the end, I was the main software designer. I learned a lot about 3D and CAD programming. I also was influenced by Catia V5 and its very special user and programming interface… In March 17 2002, within the OpenCascade Project, I registered the software as FreeCAD. I couldn't think of a better name, I'm very bad on names… In April 2003, Werner Meyer, one of the colleges in the QSpect project, switched to a company called Imetric. The contact to Imetric resulted very promising since they searched for a new 3D software platform for their 3D sensors. In 2005, Imetric donated most of its Mesh Module to FreeCAD and the Open Source community, and since then they used FreeCAD as basis for their sensor system software. Since that time, Werner Meyer is a very active developer of FreeCAD. In 2005, after one year of struggle, I decided to rip of the OpenCascade document framework and replace it with an own implementation. So, at the end, we only use the CAD kernel of OpenCascade and not the rest of its Framework. 2007 was another interesting milestone. We switched to QT4 and, therefore, to the LGPL. At that time we did much work, mainly Werner''.
|sign=[Jürgen Riegel](User_Jriegel.md)|source=''[http://forum.freecadweb.org/viewtopic.php?f=8&t=295 Who is behind FreeCad?]''}}


{{Quote|text=''Le projet FreeCAD a été lancé par moi-même en janvier 2001 sous le nom de GOM (Graphical Object Modeler), avec l’idée d’utiliser Qt, Python et Cas.CADE, un noyau CAD commercial que j’ai utilisé dans les projets de Daimler. Cas.CADE étant devenu open source peu de temps auparavant, le temps semblait donc bien choisi pour tenter de le faire évoluer dans l’espace vide de la CAO open source. J'ai eu une expérience de deux ans avec OpenCascade dans un projet appelé QSpect dans lequel, à la fin, j'étais le principal concepteur de logiciel. J'ai beaucoup appris sur la programmation 3D et la CAO. J'ai également été influencé par Catia V5 et son interface utilisateur et de programmation très spéciale… Le 17 mars 2002, dans le cadre du projet OpenCascade, j'ai enregistré le logiciel sous le nom de FreeCAD. Je ne pouvais pas penser à un meilleur nom, je suis très mauvais en noms… En avril 2003, Werner Meyer, l'un des collèges participant au projet QSpect, est passé à une société appelée Imetric. Le contact avec Imetric a été très prometteur car ils recherchaient une nouvelle plate-forme logicielle 3D pour leurs capteurs 3D. En 2005, Imetric a fait don de la majeure partie de son module de maillage à FreeCAD et à la communauté Open Source. Depuis lors, ils ont utilisé FreeCAD comme base de leur logiciel de système de capteurs. Depuis ce temps, Werner Meyer est un développeur très actif de FreeCAD. En 2005, après un an de lutte, j'ai décidé de supprimer le cadre de documentation OpenCascade et de le remplacer par une implémentation propre. Finalement, nous n'utilisons que le noyau CAD d'OpenCascade et pas le reste de son Framework. L'année 2007 a été une autre étape intéressante. Nous sommes passés à QT4 et, par conséquent, à la LGPL. À cette époque, nous travaillions beaucoup, principalement Werner''.
|sign=[Jürgen Riegel](User_Jriegel.md)}}

Le projet a été annoncé au grand public lors du [forum OpenCascade](https://dev.opencascade.org/forums) en 2003.


{{Quote|text=''Hi together, my name is Juergen Riegel and today I want announce an OpenCasCade project, FreeCAD. It is an Open Source CAx RAD based on OpenCasCade, QT and Python. It features some key concepts like Macro Recording, Workbenches, ability to run as a server and as a dynamically loadable applications' extension, and it is designed to be platform independent… Although it is in an early stage and not usable for users nor developers—the first user release is planned for the end of 2003—, I would like to get some feedback on the direction and design of FreeCAD. The GUI is nearly finished and now we, my co-developer Werner Mayer and me, have started adding the first CAD functions. FreeCAD can be seen as a general purpose mechanical CAD system, but its first audience, I think, will be CAx developers which need groundwork for own development''.
|sign=[Jürgen Riegel](User_Jriegel.md)|source=''[http://www.opencascade.org/org/forum/thread_6572/?forum=11 Announcing FreeCAD Project]''}}


{{Quote|text=''Bonjour à tous, je m'appelle Juergen Riegel et je souhaite aujourd'hui annoncer un projet OpenCasCade, FreeCAD. Il s'agit d'un RAD CAx Open Source basé sur OpenCasCade, QT et Python. Il présente des concepts clés tels que l'enregistrement de macros, les ateliers, la capacité de fonctionner en tant que serveur et en tant qu'extension d'applications à chargement dynamique, et il est conçu pour être indépendant de la plate-forme… Bien qu'il soit à un stade précoce et qu'il ne soit utilisable ni par les utilisateurs ni par les développeurs - la première version utilisateur est prévue pour la fin de 2003 - j'aimerais avoir votre avis sur l'orientation et la conception de FreeCAD. Le GUI est presque terminée et maintenant nous, mon co-développeur Werner Mayer et moi-même, avons commencé à ajouter les premières fonctions de CAO. FreeCAD peut être considéré comme un système de CAO mécanique à usage général, mais son premier public sera, je pense, les développeurs de CAx qui ont besoin d’un travail préparatoire pour leur propre développement''.
|sign=[Jürgen Riegel](User_Jriegel.md)|source=''[https://dev.opencascade.org/content/announcing-freecad-project Annonce du projet FreeCAD sur Sun, 08/17/2003 - 19:23]''}}

### Werner Mayer 

Werner Mayer a rejoint le projet dès qu\'il a été annoncé comme projet open source (avant l\'annonce, le projet était un projet privé de Jürgen). Voir ce message de Werner sur le forum en allemand: <https://forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>

Au fil du temps, le projet a pris de l\'ampleur et a vu l\'ajout de nouveaux contributeurs clés dans la communauté.

-   **Début avec Linux**


{{Quote|text=''A fun fact is that he wanted to have an open-source CAD software mainly for Linux because at that time there existed actually nothing for this platform. However, from the beginning on we exclusively developed on Windows for the next 1.5 years. Then a Czech guy made a contribution to make the code of the core build on Linux: https://github.com/berndhahnebach/All_FreeCAD/commit/9fd2e27c95ba3dc84778d92e2564cd094793ce2f#diff-480477e89f9b6ddafb30c4383dcdd705''}}


{{Quote|text=''Half a year later I continued the Linux build: https://github.com/berndhahnebach/All_FreeCAD/commit/35b962d7d751dd80f7c7781df60f93bc9a3da992''}}


{{Quote|text=''Un fait amusant est qu'il voulait avoir un logiciel de CAO open source principalement pour Linux car à l'époque il n'existait en fait rien pour cette plate-forme. Cependant, depuis le début, nous avons développé exclusivement sur Windows pour les 1,5 ans à venir. Puis un gars tchèque a fait une contribution pour faire le code du noyau construit sur Linux:https://github.com/berndhahnebach/All_FreeCAD/commit/9fd2e27c95ba3dc84778d92e2564cd094793ce2f#diff-480477e89f9b6ddafb30c4383dcdd705''}}


{{Quote|text=''Six mois plus tard, j'ai continué la construction Linux:https://github.com/berndhahnebach/All_FreeCAD/commit/35b962d7d751dd80f7c7781df60f93bc9a3da992''}}

**Q:** Could you share how that first 1.5 years went? Were you meeting in person or online?

**Q :** Pourriez-vous nous dire comment se sont déroulées ces 1,5 premières années ? Vous rencontriez-vous en personne ou en ligne ?


{{Quote|text=''Well, at that time we were colleagues (until 2005) so we could discuss things face to face. After that time we still had some personal meetings but discussed most things by email or phone.''}}


{{Quote|text=''Eh bien, à cette époque, nous étions collègues (jusqu'en 2005), pour pouvoir discuter des choses en face à face. Après cette période, nous avions encore des réunions personnelles, mais nous avons discuté de la plupart des choses par e-mail ou par téléphone.''}}


{{Quote|text=''As third core developer Yorik joined around end of 2007 but it took another 3 or 4 years until the community and number of contributors started to grow significantly.''}}


{{Quote|text=''En tant que troisième développeur principal, Yorik s'est joint à la fin de 2007, mais il a fallu encore 3 ou 4 ans pour que la communauté et le nombre de contributeurs commencent à augmenter de manière significative.''}}

**Q:** Did you divide the tasks or work on competing implementations?

**Q :** Avez-vous réparti les tâches ou travaillé sur des implémentations concurrentes?


{{Quote|text=''Yes. Jürgen was designing and implementing most of the application and document logic and I was doing the basics of the GUI.''}}


{{Quote|text=''Oui. Jürgen concevait et implémentait la plupart de la logique d'application et de document et je faisais les bases de l'interface graphique.''}}


{{Quote|text=''However, this wasn't a gradual process but we have experimented with many things at the beginning. For example, in the initial version we used OCC's document framework OCAF and its viewer but after a year or two we got into a dead end because documentation about OCC was very poor and we couldn't get it to work to extend OCAF with our own feature types. So, we decided to only use OCC's modeling capacities but develop our own application/document framework.''}}


{{Quote|text=''Cependant, ce n'était pas un processus graduel mais nous avons expérimenté beaucoup de choses au début. Par exemple, dans la version initiale, nous avons utilisé le document de framework d'OCC, l'OCAF et son visualiseur, mais après un an ou deux, nous nous sommes retrouvés dans une impasse car la documentation sur OCC était très pauvre et nous ne pouvions pas le faire marcher pour étendre l'OCAF avec nos propres fonctionnalités. Nous avons donc décidé de n'utiliser que les capacités de modélisation d'OCC mais de développer notre propre framework d'application / document.''}}

**Q:** At the time did you think FreeCAD would be where it is today?

**Q :** À l\'époque, pensiez-vous que FreeCAD serait là où il est aujourd\'hui ?


{{Quote|text=''We didn't know but we hoped. Of course we couldn't anticipate how exactly FreeCAD will look today.<br>
The most important design decisions were to make it available on all major platforms and make the whole SW as accessible as possible, i.e. to impose all important functions to Python so that (power) users are able to extend FreeCAD with own functions. This way we hoped to get a broad audience.''}}


{{Quote|text=''Nous ne savions pas mais nous espérions. Bien sûr, nous ne pouvions pas prévoir à quoi ressemblerait exactement FreeCAD aujourd'hui.<br>
Les décisions de conception les plus importantes ont été de le rendre disponible sur toutes les principales plates-formes et de rendre l'ensemble du logiciel aussi accessible que possible, c'est-à-dire d'imposer toutes les fonctions importantes à Python, afin que les utilisateurs (expérimentés) puissent étendre FreeCAD avec leurs propres fonctions. De cette façon, nous espérions avoir un large public.''}}

(Voir ce message de Werner sur le forum [Re: FreeCAD History](https://forum.freecadweb.org/viewtopic.php?f=8&t=47703#p411612))

### Yorik rejoint le projet 

[Yorik van Havre](User_Yorik.md) a rejoint le projet en 2008 et a commencé à travailler sur l\'[atelier Draft](Draft_Workbench/fr.md). Auparavant, il n\'existait aucun moyen de créer une géométrie 2D via l\'[interface graphique](Glossary/fr#GUI.md). Ce module a été entièrement programmé en Python plutôt qu\'en C++, le langage de programmation principal utilisé dans FreeCAD. Le nouvel atelier Draft a prouvé que l\'intégration Python était un succès et pouvait être utilisée pour étendre ou personnaliser les fonctionnalités de FreeCAD. En plus de son travail sur le module Draft, Yorik a amélioré la documentation de FreeCAD et est devenu *de facto* \"directeur artistique\" de FreeCAD, créant de nombreuses icônes pour le GUI de FreeCAD et [définissant son style](Artwork/fr.md).

La version 0.7 de FreeCAD publiée en avril 2009 a été la première à inclure le module Draft. Le module Part fournit un simple flux de travail [CSG](Glossary/fr#Constructive_Solid_Geometry.md) avec la création de formes primitives et d\'opérations booléennes accessibles via le menu de la pièce. L\'extrusion de profils 2D et le filetage étaient également possibles.

La version 0.8 publiée en juillet 2009 a vu s\'étoffer le module Draft, en y ajoutant un nouvel outil Dimension. Le module Part a bénéficié d'une nouvelle barre d'outils ainsi que de nouveaux outils, Revolve et Section.

À la fin de 2009, FreeCAD était intégré en tant que paquet Debian dans les dépôts Debian. FreeCAD a été ajouté aux dépôts Ubuntu 10.04 en 2010.

### Le projet continue 

La version 0.10 a été publiée en juillet 2010 et a introduit l\'[atelier Sketcher](Sketcher_Workbench/fr.md), basé sur Sketchsolve, un solveur basé sur les contraintes pour créer une géométrie 2D. La première version se limitait à la création de rectangles et de lignes.

Début 2011, profitant de l'opportunité donnée par la plate-forme en ligne [Launchpad](https://launchpad.net), l'[équipe de maintenance FreeCAD](https://launchpad.net/~freecad-maintainers) a été créée pour fournir de nouvelles versions stables ainsi que des packages de construction quotidiens de FreeCAD aux utilisateurs du système d'exploitation Ubuntu.

La version 0.11, publiée en mai 2011, a introduit le nouvel atelier Part Design qui comprenait des outils tels que Pad, Pocket, Fillet et Chamfer. L\'atelier Draft a reçu des améliorations et de nouveaux outils, comme BSpline. L\'atelier Robot comportait plus d\'outils d\'interface graphique.

La version 0.12 fut publiée en janvier 2012 et comportait un atelier Sketcher plus complet. Il incluait un résolveur totalement réécrit, FreeGCS. C'est le résultat de nombreux mois de travail des principaux développeurs de FreeCAD, comme des nouveaux venus logari81 (qui a programmé le solveur) et mrlukeparry. D\'autres outils ont été ajoutés à l\'atelier PartDesign.

### Augmentation de l\'équipe principale de développeurs 

En avril 2019, l\'équipe de développeurs principaux a été élargie: Jürgen, Werner et Yorik ont été rejoints par Abdullah, Bernd, Sliptonic et WandererFan

## Messages intéressants sur le forum 

-   à propos de PartDesignNext et d'autres décisions de conception : <https://forum.freecadweb.org/viewtopic.php?f=8&t=34923&start=130#p297074>
-   sur l\'histoire du Forum : <https://forum.freecadweb.org/viewtopic.php?f=8&t=7448&start=200#p287106>
-   à propos de l\'histoire du Projet : <https://forum.freecadweb.org/viewtopic.php?f=8&t=47703>
-   à propos de l\'histoire du Code : <https://forum.freecadweb.org/viewtopic.php?f=10&t=46733&start=10#p405068> Entre-temps, la première vérification du code a eu lieu le 18 mars 2002 (c\'est peut-être l\'anniversaire ?).
-   à propos de la Raison d\'être de l\'OpenSource : <https://forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>
-   à propos de L\'historique des validations : <https://forum.freecadweb.org/viewtopic.php?f=8&t=23695#p184940>
-   à propos de Qui est derrière FreeCAD : <http://forum.freecadweb.org/viewtopic.php?f=8&t=295>
-   à propos de l\'histoire de la MEF : <https://forum.freecadweb.org/viewtopic.php?f=18&t=48646#p416389>
-   à propos de l\'histoire du mailleur MEF : <https://forum.freecadweb.org/viewtopic.php?f=18&t=48733#p417627>



## Historique des versions 

#### Vue d\'ensemble 

  Version   Nom de version   Date de sortie              Notes de version                                            Version de validation                                                                            Branches avec corrections de bogues
       
  0.21                       en cours de développement   [Notes de version 0.21](Release_notes_0.21/fr.md)   [head master](https://github.com/FreeCAD/FreeCAD/commits/master)                                 
  0.20      \-               2022-06-14                  [Notes de version 0.20](Release_notes_0.20/fr.md)   [Version de validation 0.20](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-20)   [Branches avec corrections de bogues 0.20](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-20)
  0.19      \-               2021-03-20                  [Notes de version 0.19](Release_notes_0.19/fr.md)   [Version de validation 0.19](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-19)   [Branches avec corrections de bogues 0.19](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-19)
  0.18      \-               2019-03-12                  [Notes de version 0.18](Release_notes_0.18/fr.md)   [Version de validation 0.18](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-18)   [Branches avec corrections de bogues 0.18](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-18)
  0.17      Roland           2018-04-06                  [Notes de version 0.17](Release_notes_0.17/fr.md)   [Version de validation 0.17](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-17)   [Branches avec corrections de bogues 0.17](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-17)
  0.16      \-               2016-04-18                  [Notes de version 0.16](Release_notes_0.16/fr.md)   [Version de validation 0.16](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-16)   [Branches avec corrections de bogues 0.16](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-16)
  0.15      \-               2015-04-08                  [Notes de version 0.15](Release_notes_0.15/fr.md)   [Version de validation 0.15](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-15)   [Branches avec corrections de bogues 0.15](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-15)
  0.14      \-               2014-07-01                  [Notes de version 0.14](Release_notes_0.14/fr.md)   [Version de validation 0.14](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-14)   [Branches avec corrections de bogues 0.14](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-14)
  0.13      \-               2013-01-29                  [Notes de version 0.13](Release_notes_0.13/fr.md)   [Version de validation 0.13](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-13)   [Branches avec corrections de bogues 0.13](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-13)
  0.12      \-               2011-12-20                  [Notes de version 0.12](Release_notes_0.12/fr.md)                                                                                                    
  0.11      \-               2011-05-03                  [Notes de version 0.11](Release_notes_0.11/fr.md)                                                                                                    
  0.10      \-               2010-07-24                                                                                                                                                                               
  0.9       \-               2010-01-16                                                                                                                                                                               
  0.8       \-               2009-07-10                                                                                                                                                                               
  0.7       \-               2009-04-24                                                                                                                                                                               
  0.6       \-               2007-02-27                                                                                                                                                                               
  0.5       \-               2006-10-05                                                                                                                                                                               
  0.4       \-               2006-01-15                                                                                                                                                                               
  0.3       \-               2005-10-31                                                                                                                                                                               
  0.2       \-               2005-08-09                                                                                                                                                                               
  0.1       \-               2003-01-27                                                                                                                                                                               
  0.0.1     \-               2002-10-29                  Première version                                                                                                                                             



#### Légende

  Color   Type de version
   
          Future version
          Dernière pré-version
          **Dernière version**
          Ancienne version, toujours supportée
          Ancienne version
          

## Liens externes 

-   [SourceForge Files section](http://sourceforge.net/projects/free-cad/files/)
-   [SourceForge Old Files section](http://sourceforge.net/projects/free-cad/files/OldFiles/)
-   [Announcing FreeCAD Project](http://www.opencascade.org/org/forum/thread_6572/?forum=11) Annonces sur le forum Open Cascade



---
![](images/Button_right.svg) [documentation index](../README.md) > [News](Category_News.md) > History/fr
