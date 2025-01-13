# <img alt="Icône de l\'atelier OSH Automated Documentation" src=images/Icon-osh-autodoc.svg  style="width:64px;"> OSH Automated Documentation/fr

## Introduction

OSH Automated Documentation est un logiciel qui vous permet de générer des instructions d\'assemblage visuelles de haute qualité pour des produits physiques conçus dans un logiciel de CAO. Il se compose de deux parties, cet atelier de FreeCAD et un compilateur pour la génération de fichiers PDF. Pour plus d\'informations, voir le [site web OSH Automated Documentation](https://osh-autodoc.org). Cette page traite principalement de l\'atelier disponible dans le gestionnaire des extensions de FreeCAD.



## Présentation

Ce logiciel est issu d\'un [article évalué par des pairs](https://openhardware.metajnl.com/articles/10.5334/joh.56) et, en tant que tel, reste un logiciel de recherche et n\'est pas prêt pour la production. À la demande générale, nous recherchons activement des fonds pour poursuivre ce travail et le rendre prêt pour la production.



## Utilisation

Le logiciel se compose d\'un \"atelier\" et d\'un \"compilateur\" qui génère un PDF sur la base d\'une description textuelle du manuel. L\'atelier permet de faire des annotations sur le modèle de CAO, par exemple un fichier STEP. Un exemple d\'annotation se trouve dans la figure ci-dessous, où la position de la caméra est enregistrée pour générer une image de haute qualité pour le manuel :

![](images/Screenshot-camera-position.png )

L\'atelier génère une structure de répertoire avec des images SVG et une nomenclature des pièces utilisées pour une étape d\'assemblage. La nomenclature est un fichier CSV contenant les images de chaque pièce. Cette sortie peut être utilisée par d\'autres logiciels, en particulier par notre compilateur qui l\'utilise pour créer des images PDF.

L\'interface entre notre compilateur et l\'atelier a été conçue de manière à ce que les résultats de l\'atelier puissent également être utilisés pour d\'autres flux de travail.

Pour plus d\'informations sur l\'utilisation de l\'atelier, voir le [site web OSH Automated Documentation](https://osh-autodoc.org).



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [External_Workbenches](Category_External_Workbenches.md) > OSH Automated Documentation/fr
