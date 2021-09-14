# FreeCAD development model project/fr




{{VeryImportantMessage|
Ce plan de développement est probablement obsolète. Pour plus d'informations, voir [Plan de développement](Development_roadmap/fr.md).<br>
Si vous n'êtes pas impliqué dans le développement discuté ici :<br>
!!! S'IL VOUS PLAÎT, NE MODIFIEZ PAS ET NE TRADUISEZ PAS !!!
}}


{{TOCright}}

Cette page est une transition du code FreeCAD dans [GIT](http://fr.wikipedia.org/wiki/Git) pour un modèle de développement plus apte. Il suit les règles de la [démarche d\'organisation personnelle](http://fr.wikipedia.org/wiki/Getting_Things_Done). Les projets sont collectés dans la [feuille de route](Development_roadmap/fr.md).

## But et principes 

Ce projet vise à définir un nouveau développement, et, un modèle de gouvernance pour FreeCAD. Nous arrivons au point, où, le référentiel [SVN](http://fr.wikipedia.org/wiki/Apache_Subversion) est difficile à gérer. Travailler avec des **patchs** est ennuyeux, et, compliqué pour les personnes désireuses de contribuer à l\'écriture du code. Donner à chacun un accès en écriture au référentiel SVN est dangereux. Les gens, peuvent involontairement \"casser\" quelque chose dans le système de base, ou, dans des décisions en cas de forces majeures.

Git est utilisé en tant que système de contrôle de versions distribués (DVCS), mailing lists et superviseurs.

## Résultats

## Réflexions

### Git

-   Utiliser Git en tant que système de contrôle des nouvelles versions.
-   Garder SVN (au moins pour tout).
    -   utiliser comme une sorte de libération référentielle pour garder le flux de travail APP, et, les numéros de révision.
    -   restreindre l\'écriture SVN à [Werner](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=69), [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68) et [Jurgen](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=67) (ligne officielle).
    -   toutes les autres choses, comme le développement, les branches, les expériences vont dans Git !
    -   **Option** : passer complètement à Git.
        -   donner des collatéraux dans les numéros de version, et, construction ppa \....
-   donner les droits en écriture (push) à toutes personnes intéressées.

### Développement et listes de diffusion (mailing list) 

Le forum a ses limites, je voudrais utiliser une ou plusieurs listes de diffusion pour gérer les branches, et, traiter les demandes.

Cela a des avantages :

-   pouvoir travailler hors ligne.
-   utiliser le puissant moteur de recherche des clients de messageries.
-   aucune restriction dans la taille et les pièces jointes.

### Clarifier les responsabilités 

Nous allons bientôt avoir de plus en plus de développeurs, et, les utilisateurs auront des demandes de fonctionnalités contradictoires.
Nous devons avoir une structure, filtrer les responsabilités et décider de telles demandes et de commencer l'écriture du code.

#### Sont volontaires 

Adrian Przekwas:
Publicity - G+, Youtube,
Tutorials - [http://freecad-tutorial.blogspot.com](http://freecad-tutorial.blogspot.com)
Translation (unsure) - Polish (Wiki, Crowdin)

Yorik van Havre:
Software: arch module, draft module, artwork
Documentation: general wiki organization and design
Translation: french, dutch, brazilian portuguese
Publicity: articles on [http://yorik.uncreated.net/guestblog.php](http://yorik.uncreated.net/guestblog.php), G+, facebook

## Organisation

Les règles décidées et les informations sont sur décrites sur le document [FreeCAD development model](FreeCAD_development_model/fr.md).

## Actions suivantes 



[Category:Roadmap](Category:Roadmap.md)
