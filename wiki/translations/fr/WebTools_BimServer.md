---
- GuiCommand:
   Name:WebTools BimServer
   Name/fr:WebTools BimServer
   MenuLocation:Web Tools - BIM server
   Workbenches:[WebTools](WebTools_Workbench/fr.md)
---

# WebTools BimServer/fr


**A partir de FreeCAD v0.17, cet outil a été enlevé de l'atelier Arch et fait maintenant partie de l'[atelier externe WebTools](WebTools_Workbench/fr.md) qui peut être installé depuis le menu Outils → <img src="images/Std_AddonMgr.svg" width=24px> [Gestionnaire des extensions](Std_AddonMgr/fr.md).
**

## Description

Cette commande permet d\'interagir avec une instance [BIMServer](http://www.bimserver.org), d\'ouvrir des fichiers stockés sur le serveur BIM, et de sauvegarder de nouvelles révisions de ces fichiers. BIMServer est un système serveur gratuit et libre conçu pour travailler avec des fichiers IFC. Dans son état actuel, il permet de gérer des projets avec de nombreux fichiers IFC et de gérer les révisions. Sa base de données extensible et son architecture de greffons permettent aussi de concevoir des outils avancés de recherche et de validation et des processus de fusion intelligents.

Pentru a utiliza această comandă, trebuie îndeplinite următoarele condiții:

-   Les modules Python **json** et **requests** doivent être installés sur votre système
-   Vous devez avoir accès à une instance BIMServer (lisez la [BIMServer documentation](https://github.com/opensourceBIM/BIMserver/wiki) pour installer un BIMServer localement) et disposer des informations d\'identification (nom d\'utilisateur et mot de passe) pour ce serveur. Au moment de la rédaction de ce manuel, la version stable de BIMServer est 1.4, mais nous vous recommandons d'installer une des versions bêta 1.5.X disponibles, qui installe automatiquement de nombreux plug-ins (dans la version 1.4, vous devez l'installer manuellement).
-   Tous les transferts de fichiers avec le serveur BIMServer sont effectués avec des fichiers IFC. Par conséquent, vous devez savoir comment travailler avec [IFC files](Arch_IFC/fr.md).

## Utilisation

1.  Assurez-vous que les conditions ci-dessus sont remplies et que vous avez accès à une instance BIMServer en cours d\'exécution.
2.  Selectionnez le menu **Web Tools → <img src="images/WebTools_BimServer.svg" width=16px> [BIM Server](WebTools_BimServer/fr.md)
**
3.  Appuyez sur le bouton **Connect** et entrez vos informations d\'identification.
4.  Une fois la connexion au serveur BIMS établie, choisissez un projet à utiliser dans la liste déroulante **Project**.

## Options

![](images/Arch_Bimserver_panel.jpg )

-   Si vous vous connectez à un serveur BIM depuis FreeCAD pour la première fois, appuyez sur le bouton **Connecter** et entrez l\'URL du serveur, votre identifiant (qui est toujours une adresse électronique) et votre mot de passe dans la boîte de dialogue. boîte qui va apparaître. Si vous souhaitez vous connecter automatiquement la prochaine fois que vous utiliserez la commande BimServer, cochez l\'option **enregistrer les informations d\'identification** (votre identifiant et votre mot de passe ne sont pas enregistrés par FreeCAD, seulement un cookie de session).
-   Une fois que FreeCAD s\'est connecté avec succès à une instance BIMServer, le bouton **Connecter** se transformera en **Connecté**. Cliquez à nouveau sur le bouton pour vous déconnecter. Cela effacera également le cookie de session stocké. Vous devrez donc saisir vos identifiants à nouveau la prochaine fois.
-   Afin de supprimer manuellement le cookie de session et de tout réinitialiser, vous pouvez simplement supprimer l\'URL BIMServer stockée dans **Edit → Préférences → Arch → BimServer**.
-   Le bouton **Ouvrir dans le navigateur** ouvrira l\'interface Web du serveur BIMServer dans le navigateur Web interne de FreeCAD ou, si vous avez marqué cette option dans **Edit → Préférences → Arch → BimServer**, dans un navigateur Web externe. Cela permet par exemple de créer de nouveaux projets ou d\'analyser le contenu stocké sur le serveur BIMServer.

### Téléchargement de révisions 

-   La liste déroulante **Projet** affiche les projets disponibles stockés sur le serveur BIM. Choisissez-en une pour voir les révisions disponibles pour ce projet.
-   Sélectionnez une révision et cliquez sur **Ouvrir** pour télécharger et ouvrir le fichier IFC correspondant à cette révision dans FreeCAD.
-   Lorsque vous appuyez sur le bouton **Ouvrir**, une boîte de dialogue s\'ouvre pour vous permettre de sauvegarder le fichier IFC téléchargé à l\'emplacement de votre choix avant de l\'ouvrir. Si vous appuyez sur **Annuler**, le fichier sera enregistré sous un nom temporaire dans le répertoire temporaire du système.

### Téléchargement de révisions 

-   Si vous souhaitez télécharger une nouvelle révision, assurez-vous que le bon projet a été sélectionné dans la liste déroulante **Projet**
-   Choisissez l\'objet **Objet racine** que vous souhaitez télécharger. Il doit s\'agir d\'un [Arch Site](Arch_Site/fr.md) ou d\'un [Arch Bâtiment](Arch_Building/fr.md). Seuls les objets appartenant à cet objet racine seront téléchargés.
-   Ecrivez un **Commentaire**, ce sera la description (nom) de la révision.
-   Appuyez sur le bouton **Upload**. Une boîte de dialogue s\'ouvre pour vous permettre de sauvegarder le fichier IFC produit à l\'emplacement de votre choix avant de le télécharger. Si vous appuyez sur **Annuler**, le fichier sera enregistré sous un nom temporaire dans le répertoire temporaire du système.



---
![](images/Button_right.svg) [documentation index](../README.md) > WebTools BimServer/fr
