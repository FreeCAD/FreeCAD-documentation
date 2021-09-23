---
- GuiCommand:/fr
   Name:Path Sanity
   Name/fr:Path Rechercher des erreurs
   MenuLocation:Path → Vérifier le travail path pour les erreurs courantes
   Workbenches:[Path](Path_Workbench/fr.md)
   Shortcut:**P** **S**
   Version:0.19
---

# Path Sanity/fr

## Description

De nombreux utilisateurs de Path sont des amateurs et des bricoleurs. En tant que tels, ils utilisent leurs machines CNC pour exécuter le G-code qu\'ils ont configuré et généré eux-mêmes. Ce n\'est pas le cas de la plupart des utilisateurs professionnels/commerciaux. Dans les ateliers professionnels, les personnes chargées de créer le G-code (programmeurs CNC) et celles qui l\'exécutent sur les machines (opérateurs CNC) sont différentes.

Les amateurs exécutent généralement le G-code quelques minutes après le post-traitement et probablement seulement une ou deux fois. Chez un professionnel, un G-code éprouvé peut être exécuté plusieurs fois pendant des mois ou des années après sa création initiale.

Un problème qui se pose dans un atelier CNC professionnel est qu\'il existe de nombreuses hypothèses faites par le programmeur qui ne sont PAS communiquées dans le G-code lui-même. Par exemple, le G-code peut appeler un outil \"T3\" mais à moins qu\'il ne soit commenté, le G-code ne dit pas à quel type d\'outil \"T3\" se réfère. On suppose simplement que T3 dans le système CAM est le même que T3 sur la machine. Il existe de nombreuses hypothèses comme celle-ci concernant la configuration de la machine, l\'outillage, le matériau, l\'orientation des pièces, etc. Même si le G-code est parfait, si l\'opérateur ne configure pas la machine avec les mêmes hypothèses, il peut planter.

Les ateliers commerciaux créent souvent un \'manuel d\'installation\' qui documente toutes ces hypothèses et donne aux opérateurs ce dont ils ont besoin pour configurer la machine et produire une pièce.

[Path Rechercher des erreurs](Path_Sanity/fr.md) est l\'outil de l\'atelier Path pour générer ce type d\'informations. La sortie de la commande Path Sanity est un fichier .html autonome avec des images intégrées. <img alt="Ci-dessus: exemple de rapport généré par Path Rechercher des erreurs" src=images/Sanity.jpg  style="width:400" height="600px;">

## À propos du rapport 

Autant que possible, le contenu est indépendant de FreeCAD. L\'opérateur CNC ne peut jamais utiliser FreeCAD, donc la terminologie propre à FreeCAD/Path prête à confusion. Le rapport comporte des sections distinctes et est formaté pour rendre la recherche des choses facile et prévisible.

### Part Information 

Cette section donne un aperçu de ce qui est fait. Idéalement, l\'image doit montrer les objets de base. S\'il existe plusieurs objets de base, l\'image doit montrer comment ils s\'imbriquent.

### Run Summary 

Donne une vue rapide des hauteurs minimales et maximales et des temps de fonctionnement.

### Rough Stock 

Détaille l\'objet Stock de la Tâche (Job). C\'est un domaine dans lequel Path bénéficierait d\'une certaine amélioration. Une propriété matérielle rudimentaire pour le stock serait utile ici et pourrait également être utilisée pour aider à suggérer des alimentations/vitesses.

### Tool Data 

Comporte des sous-sections pour chaque numéro d\'outil utilisé dans la tâche. Elle détaille ce que le programmeur suppose être l\'outil et quelles opérations l\'utilisent. Cette section ne fonctionne qu\'avec le nouveau système Toolbit. Il s\'agit d\'un autre domaine dans lequel Path doit être amélioré. Plus précisément, les Toolbits ont besoin d\'attributs supplémentaires concernant l\'outil, comme le fabricant, l\'adresse et le numéro de pièce.

### Output

Donne des détails sur où et quand le G-code a été post-traité. Il indique également si le travail comporte des arrêts facultatifs/obligatoires afin que l\'opérateur sache s\'il peut s\'éloigner de la machine en toute sécurité pendant une course.

### Coolant

Liquide de refroidissement.

### Fixtures and Work-holding 

Affiche les pièces dans le contexte de l\'enveloppe du stock et montre également l\'origine de la pièce.

### Squawks

Avertissements et erreurs détectés par [Path Rechercher des erreurs](Path_Sanity/fr.md). Ceux-ci peuvent ou non être des problèmes, mais ils sont notés pour une attention supplémentaire. Par exemple, si le même numéro d\'outil est utilisé pour différents outils, il s\'affichera comme une erreur. Si un contrôleur d\'outil n\'a pas d\'avance / vitesse configurée, il apparaîtra comme un avertissement. Il détectera également et avertira les contrôleurs d\'outils inutilisés. Path bénéficierait ici de la possibilité d\'ajouter des notes ou des avertissements arbitraires.

## Utilisation

1.  Sélectionnez un <img alt="" src=images/Path_Job.svg  style="width:16px;"> [Path Tâche](Path_Job/fr.md) dans la [Vue en arborescence](Tree_view/fr.md).
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Path_Sanity.svg" width=16px> [Vérifier le travail path pour les erreurs courantes](Path_Sanity/fr.md)**.
    -   Sélectionnez **Path → <img src="images/Path_Sanity.svg" width=16px> Vérifier le travail path pour les erreurs courantes** dans le menu.
    -   Utilisez le raccourci clavier : **P** puis **S**.
3.  Les informations pertinentes sont rassemblées dans un dictionnaire Python puis formatées au format asciidoc.
4.  Le fichier asciidoc est écrit sur le disque au même endroit que le fichier qui sera post-traité.
5.  Un processus externe appelle asciidoctor pour lire le fichier asciidoc et générer le fichier .html.
6.  Ceci lancera automatiquement le navigateur web du système pour visualiser le rapport HTML autonome généré.

## Notez un ASCIIDOC et un Asciidoctor 

Asciidoc est un format de balisage léger pour la création de notes, d\'articles, de livres, etc. Il est lisible par l\'homme et facilement traduit dans d\'autres formats.

Asciidoctor est un processeur de texte open-source rapide pour la conversion d\'asciidoc en HTML, PDF ou d\'autres formats. Il est disponible pour Linux, Windows et MacOS. Asciidoctor n\'est pas installé avec FreeCAD. Si vous utilisez Path Sanity sans installer Asciidoctor, le fichier source asciidoc sera généré mais le HTML résultant ne sera pas produit. [Site Asciidoctor](https://asciidoctor.org/)





{{Path_Tools_navi

}}

---
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path Sanity/fr
