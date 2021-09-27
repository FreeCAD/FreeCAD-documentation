# Naming project/fr
**
Ce plan de développement est probablement obsolète. Pour plus d'informations, voir [Plan de développement](Development_roadmap/fr.md).<br>
Si vous n'êtes pas impliqué dans le développement discuté ici :<br>
!!! S'IL VOUS PLAÎT, NE MODIFIEZ PAS ET NE TRADUISEZ PAS !!!
**


{{TOCright}}

Ce modèle est la ligne directrice pour un projet de développement de FreeCAD. Il suit les règles de la procédure _.

## Buts et principes 

Il s\'agit d\'un développement et d\'un effort de conception pour mettre en œuvre un robuste nommage topologique dans FreeCAD.

Plus de détails au sujet du nommage topologique dans **[Problème de dénomination topologique](Topological_naming_problem/fr.md)**.

## Résultat

1.  \'\'\'Interface \'\'\' en (Part::TopoShape) pour référencer (nommer) des formes et sous-formes (faces, arêtes, sommets), grâce à une chaîne de caractères (nom du sous-élément comme « Face1 »)
    Nous avons besoin d\'une interface de Part::TopoShape avec toutes les informations nécessaires pour le nommage, par exemple NewShape, des renseignements supplémentaires auprès d\'une \"part\", comme supprimer une face, modélisation de l\'étape (pour 2) et\...
2.  \'\'\'Association \'\'\' des étapes de modélisation avec les faces/arêtes résultantes.
    Dans le cas d\'un grand modèle, l\'utilisateur est perdu s\'il y a des centaines de congés ou de trous traversants. Donc, si les faces/arêtes savaient à quelle étape de modélisation elles étaient créées, nous pourrions appliquer un double-clic sur arête/face pour ouvrir la bonne fonctionnalité !
3.  \'\'\' Algorithme \'\'\' pour conserver l\'appellation stable tout au long de l\'évolution de l\'historique de modélisation, comme le fractionnement de bord/faces, et le déplacement des sommets.
    ![](images/NamingExample.jpg )
4.  (facultatif) **optimisation de la structure des données en mémoire**, seulement pour garder les changements des faces et arêtes de chaque étapes de la modélisation.
    Cela devient important lorsque les modèles s\'agrandissent. Ce n\'est pas efficace pour copier la plupart des formes juste \"à travers\". Il serait beaucoup plus efficace de partager des faces/arêtes inchangées entre Éléments et ne copier que ce qui est modifié.

## Remue-méninges 

Beaucoup de discussions ont été débattues dans le [\"Robust Reference\" Post](http://forum.freecadweb.org/viewtopic.php?f=10&t=2656) de jrheinlaender.

### Autres

-   [Catia V5 Topology and Generic Naming](http://www.maruf.ca/files/caadoc/CAATopTechArticles/JournalMethodology.htm#Definition) et [Catia V5 Objectives of Generic Naming](http://www.maruf.ca/files/caadoc/CAAMmrTechArticles/CAAMmrGenericNaming.htm#Objectives%20of%20GN)
-   [Topological naming in OCAF (Open CASCADE Application Framework)](https://www.opencascade.com/doc/occt-7.4.0/overview/html/occt_user_guides__ocaf.html#occt_ocaf_5_6)

### Bibliographie & Documents 

-   J Kripac, \"A mechanism for persistently naming topological entities in history-based parametric solid models, Symposium on Solid Modeling and Applications 1995, p.21-30\"

:   Décrit une méthode pour faire les trois premiers points dans la liste. Donne l\'approche utilisée par Catia et OCC-TNaming. Garde au moins la même apparence d\'interface. Le document n\'est plus accessible au téléchargement. J\'ai du l\'acheter. Si quelqu\'un est intéressé, je peux lui envoyer par courrier électronique.

-   [Dago AGBODAN, David MARCHEIX and Guy PIERRA, \"PERSISTENT NAMING FOR PARAMETRIC MODELS, 2000\"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.29.2836&rep=rep1&type=pdf)

:   Approche intéressante via shell-graphs, s\'attaque au point quatre de la liste en réutilisant des faces/arêtes non modifiées.

-   [Duhwan Mun and Soonhung Han, \"Identification of Topological Entities and Naming Mapping for Parametric CAD Model Exchanges, INTERNATIONAL JOURNAL OF CAD/CAM, 2005, p 69-82\"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.106.3087&rep=rep1&type=pdf)

:   Très bonne vue d\'ensemble et exemples

-   [Farjana, S.H., Han, S. \"Mechanisms of Persistent Identification of Topological Entities in CAD Systems: A Review\", Alexandria Engineering Journal, Volume 57, Issue 4, Décembre 2018, Pages 2837-2849](https://research-management.mq.edu.au/ws/portalfiles/portal/100931773/Publisher_version_open_access_.pdf)

-   [Assembly Solving for Neutral Re-Imported Product Models Tahir A. Jauhar, Soonhung Han, Soonjo Kwon , p.108-123 , CAD Journal 2020, Volume 17 Numéro 1](http://www.cad-journal.net/files/vol_17/CAD_17(1)_2020_108-123.pdf)

### Résumé des travaux à ce jour 

Au 13 juin 2016, voici un résumé des travaux effectués pour ce projet :

-   jrheinlaender a produit beaucoup de code en 2012 qui s\'appuie fortement sur l\'atelier Sketch pour solutionner des \"références robustes\"
-   ickby a tenté de l\'incorporer au nouveau code de FreeCAD. [Cet article](http://forum.freecadweb.org/viewtopic.php?f=10&t=2656&start=60#p124844) a un lien vers son dépôt github.
-   En 2016, ezzieyguywuf a relancé le fil de jrheinlaender et a ensuite lancé le sien. Vous pouvez le [voir ici](http://forum.freecadweb.org/viewtopic.php?f=10&t=15847).
-   ezzieyguywuf a développé un programme opencascade \"léger\" pour simuler des résultats de dénomination topologique et tester des solutions potentielles. Voir [freecadTopoTesting](https://github.com/ezzieyguywuf/freecadTopoTesting) ici
-   ezzieyguywuf a incorporé la boîte à outils TNaming opencascade dans son code de test, et a montré en quoi cela pouvait aider à résoudre certains problèmes de dénomination topologique. Voir le dépôt github
-   [Topological Naming](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming) dépôt github par realthunder
-   [Topological Naming Algorithm](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming-Algorithm) dépôt github par realthunder

## Organisation

### Information sur TNaming 

Voir _ pour un article sérieux sur le dépôt github de ezzieyguywuf. Voici quelques faits saillants :

-   Le TNaming opencascade s'appuie sur [l\'environnement de travail TDF\_Data](https://dev.opencascade.org/doc/occt-7.5.0/refman/html/class_t_d_f___reference.html#details).
-   TDF\_Data est un composant clé du logiciel OPAF opencascade, mais peut être utilisé indépendamment de celui-ci.
-   TDF\_Data est essentiellement une arborescence dans laquelle des données sont ajoutées puis lues à une date ultérieure
-   Lorsqu\'un attribut TNaming\_NamedShape est ajouté à un nœud de l\'arborescence TDF\_Data, un attribut TNaming\_UsedShapes est ajouté à la racine de l\'arborescence.
    -   **REMARQUE :** cet attribut TNaming\_UsedShapes est essentiel pour l\'utilitaire de la boîte à outils TNaming. Il contient l'historique de toutes les TopoDS\_Shape utilisées pendant l'historique de la pièce.
-   TNaming\_Builder est utilisé pour ajouter des informations à l\'arborescence TDF\_Data. Il ajoute un TNaming\_NamedShape à un nœud donné de l'arbre et met à jour la base de données TNaming\_UsedShapes selon les besoins.
-   Chaque fois que TopoDS\_Shape est modifié, il doit être enregistré dans la structure TDF\_Data.
    -   TNaming\_Builder est encore utilisé pour cela
    -   [Voir ici](http://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__ocaf.html#occt_ocaf_5_6_1) dans la documentation opencascade pour un tableau listant ce qui doit être stocké dans la base de données. **REMARQUE :** ce tableau semble être incomplet. Des tests supplémentaires peuvent être nécessaires
    -   En bref, chaque fois que TopoDS\_Shape est modifié, toutes les fonctions modifiées/générées/supprimées doivent être consignées. Pour la plupart, étant donné que nous traitons avec des solides, cela signifie que nous devons consigner les faces modifiées/générées/supprimées sur le solide.
-   La classe TNaming\_Selector est utilisée pour \"sélectionner\" une fonctionnalité suivie dans l\'arborescence TDF\_Data
    -   Un élément \"sélectionné\" est unique pour l\'algorithme TNaming d\'OpenCascade qui conserve une référence constante, quels que soient les changements topologiques

## Actions prochaines 

-   Définition de la portée
-   Protocole de test Python
-   Interface pour Part::TopoShape (+ liaison python)

### Prochaines étapes (à compter du 13 juin 2016) 

1.  Déterminer si le toolkit opencascade TNaming résout complètement le problème de dénomination topologique dans FreeCAD
    -   Quels sont tous les cas où la dénomination topologique est un problème ?
    -   Quels sont les scénarios complexes où cette approche devra fonctionner ?
2.  Incorporer du code TNaming dans FreeCAD
    1.  Commencer par une approche simple, c\'est-à-dire créer un cube et un cylindre, fusionner, arrondir, puis redimensionner le cylindre. L\'arrondi ne doit pas bouger.
    2.  Ajouter progressivement plus de fonctionnalités.
3.  Déterminer si TNaming sera la solution à long terme.
4.  Que TNaming soit ou non la solution à long terme, trouver un moyen de \"sérialiser/désérialiser\" les données que TNaming utilise pour la persistance entre les sessions




_

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > Naming project/fr
