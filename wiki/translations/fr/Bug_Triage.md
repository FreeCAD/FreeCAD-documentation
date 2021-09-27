# Bug Triage/fr
{{TOCright}}

## Pourquoi


{{ColoredParagraph|Triageː

1a : le tri et la répartition du traitement entre les patients et en particulier les victimes de combats et de catastrophes selon un système de priorités conçu pour maximiser le nombre de survivants

1b : le tri des patients (comme dans une salle d'urgence) en fonction de l'urgence de leur besoin de soins

2 : attribution d'un ordre de priorité aux projets en fonction des domaines dans lesquels les fonds et autres ressources peuvent être utilisés, utilisés le mieux ou le plus susceptibles de réussir
}}

Le triage des bogues est important pour organiser et hiérarchiser les bogues / fonctionnalités/correctifs par rapport à FreeCAD [Bug Tracker](Tracker/fr.md). Si cette tâche est négligée, un projet peut souffrir de ce qu\'on appelle \"Bugtracker Bloat\", qui consiste essentiellement en une accumulation et une décomposition de tickets négligés. Le triage aide également à identifier les tickets en double qui ont tendance à s\'accumuler, en particulier s\'il existe un problème non résolu de longue date que l\'équipe FC connaît mais ne dispose pas des ressources nécessaires, quelle qu\'en soit la raison.

## Comment trier 

### Statut du ticket 

#### Nouveau

Per MantisBT docs ː {{ColoredText|C'est le statut d'entrée pour les nouvelles émissions. Les problèmes restent dans cet état jusqu'à ce qu'ils soient ː attribués, reconnus, confirmés ou résolus.}}

En d\'autres termes, le statut **NEW** indique plusieurs choses ː

1.  Le ticket n\'a pas été confirmé.
2.  Le ticket est toujours en cours, c'est-à-dire que Les Trieurs/développeurs évaluent/clarifient les détails du ticket de l'OP.
3.  L\'équipe de FreeCAD n\'a pas encore décidé quoi faire avec ce ticket.

Tous les [tickets FreeCAD ouverts avec le statut **NEW**](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=10&hide_status=80).

#### Reconnu

#### Feedback

Les billets sont désignés dans cet état lorsqu\'il est demandé à OP de fournir plus d\'informations.

Le billet est en attente sur la base de la participation de OP. Par exemple, il manque des informations sur la version du FC dans le ticket. ou peut-être qu\'un certain nom de bibliothèque ou version de tierce partie est requis, etc. Les développeurs doivent définir ce statut chaque fois qu\'ils répondent à OP afin d\'indiquer que le ticket est en attente. Ceci est important en raison de la possibilité pour OP de ne pas répondre, ce qui a une forte probabilité que le ticket «se décompose» dans le suivi.

Lorsque OP répond, le statut du ticket revient automatiquement à **Nouveau**. Ensuite, le billet doit être réexaminé pour décider de ce qui est nécessaire.

Une discussion plus approfondie sur ce sujet dans le [forum FreeCAD](https://forum.freecadweb.org/viewtopic.php?f=10&t=23005).

Tous [open FreeCAD tickets with **FEEDBACK** status](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=20&hide_status=80) dans le FC bugtracker.

#### Confirmé

Lorsqu\'un ticket est confirmé, il a été soit

-   un bug qui a été reproduit
-   une fonctionnalité qui a été mise au vert pour être considérée comme valide.

Il est maintenant prêt à être assigné à ou par un dev.

Tous [open FreeCAD tickets with **CONFIRMED** status](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=40&hide_status=80) dans le FC tracker.

#### Assigné

Explicites, ces tickets ont été attribués à un développeur spécifique.

Tous [open FreeCAD tickets with **ASSIGNED** status](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=50&hide_status=80) dans le FC tracker.

#### Résolu

Ces tickets ont été résolus mais pas encore fermés, probablement parce qu\'ils ont besoin de la confirmation que le ticket a été corrigé.

------------------------------------------------------------------------

### Ticket Résolu 

#### Ouvert

Cela se passe d\'explication, tous les billets restent \"ouverts\" s\'ils restent pertinents, à la discrétion de l\'équipe du FC.

#### Fixé

Tickets a bien été fixé.

#### Impossible de reproduire 

Billets réputés non reproductibles

#### Dupliquer

Billets qui sont ou ont un billet en double.

#### Aucun changement requis 

Billets où il a été vérifié qu\'aucune modification n\'est nécessaire.

#### Ne résoudra pas 

L'équipe FC a rejeté la demande de billet pour quelque raison que ce soit.

#### Non réparable 

#### Rouvert

Les billets qui ont été fermés me sont ensuite rouverts pour une raison pertinente. Très probablement, le problème a refait surface ou n\'a pas été totalement résolu.

#### Suspendu

### Priorité du ticket 

#### Immédiat

#### Urgent

#### Haute

#### Normal

#### Faible

#### None

### Sévérité du ticket 

#### Bloc

#### Crash

#### Majeur

#### Mineur

#### Tweak

#### Texte

#### Trivial

#### Fonctionnalité

## Marquage des tickets 

Une méthodologie importante pour suivre les tickets par sujet/thème/catégorie. Il est important que les balises existantes soient utilisées pour baliser les problèmes avant que de nouvelles balises ne soient créées. Si des tags en double ou superflus sont créés, l'administrateur de suivi des bogues est responsable de les supprimer et, si possible, de recaler les tickets.

## En relation 

[Traqueur de bogues](Tracker/fr.md)







_ _

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Bug Triage/fr
