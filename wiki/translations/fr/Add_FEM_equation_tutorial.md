# Add FEM equation tutorial/fr
{{TutorialInfo/fr
|Topic=Ajouter des équations FEM
|Level=Avancé
|Time=1 jour
|Author=_
|FCVersion=0.19
}}

## Introduction

Dans ce tutoriel, nous allons ajouter l\'équation de flux à FreeCAD et implémenter le support pour le solveur Elmer. Assurez-vous d\'avoir lu et compris [Module d\'extension FEM](Extend_FEM_Module/fr.md) avant de lire ce tutoriel.

La tâche peut être divisée en quatre parties:

-   La première étape consiste à informer l\'atelier de travail FEM d\'un nouveau type d\'équation. Cette étape ne doit être effectuée que si l\'équation n\'existe pas encore dans FreeCAD (par opposition à une équation qui est déjà dans FreeCAD mais qui n\'est pas prise en charge par le solveur cible).
-   La deuxième étape consiste à ajouter un objet document représentant l'équation spécifique d'Elmer.
-   La troisième étape consiste à ajouter la prise en compte de la nouvelle équation dans le solveur d\'Elmer.
-   Après cela, l\'exportation d\'analyse sous Elmer doit être étendue pour prendre en charge le nouveau type d\'équation.

## Ajout d\'un nouveau type d\'équation 

Dans cette étape, nous allons modifier le fichier suivant:

-    {{FileName|src/Mod/Fem/femsolver/equationbase.py}}
    

Le type d\'équation est partagé entre tous les objets équation des différents solveurs. Chaque type a un spécificateur de chaîne (par exemple, \"Heat\") et une commande dédiée qui ajoute l\'équation au solveur sélectionné. Cela permet une interface graphique plus simple où nous n\'avons qu\'un seul bouton pour l\'équation de chaleur qui est utilisé pour tous les solveurs supportés.

Tout d\'abord, ajoutez la nouvelle équation au module {{Incode|equationbase.py}}. Chaque équation nécessite deux classes. Un proxy de document et un proxy de vue. Ces deux classes seront utilisées plus tard comme classes de base pour les classes d\'équation spécifiques à Elmer. Il suffit de les copier-coller depuis un type d\'équation existant et d\'ajuster le chemin de l\'icône dans {{Incode|getIcon(self)}} du proxy d\'affichage.


```python
class FlowProxy(BaseProxy):
    pass

class FlowViewProxy(BaseViewProxy):
    def getIcon(self):
        return ":/icons/FEM_EquationFlow.svg"
```

## L\'objet équation d\'Elmer 

Dans cette étape, nous allons modifier le fichier suivant:

-    {{FileName|src/Mod/Fem/femsolver/elmer/equations/flow.py}}
    

et ajoutez le nouveau fichier suivant:

-    {{FileName|src/Mod/Fem/ObjectsFem.py}}
    

-    {{FileName|src/Mod/Fem/CMakeLists.txt}}
    

Commençons par le module qui implémente l\'objet document. Il peut être copié à partir d\'une équation existante.

-   Si la nouvelle équation ne prend en charge que les mots-clés des systèmes **linéaires**, copiez le module `femsolver/elmer/equations/elasticity.py`.
-   S\'il prend également en charge les mots-clés **non linéaires**, copiez `femsolver/elmer/equations/heat.py`.

L\'équation de l\'écoulement dans Elmer est une équation potentiellement non linéaire. Cela signifie que nous allons focaliser notre travail sur `heat.py`.

### Mots-clés 

-   Si la nouvelle équation ne supporte que les mots-clés pour les systèmes \"linéaires\", copiez le module {{Incode|femsolver/elmer/equations/elasticity.py}}.
-   Si la nouvelle équation supporte les mots-clés pour les systèmes *linéaires* et *non linéaires*, copiez le module {{Incode|femsolver/elmer/equations/heat.py}}.

L\'équation du flux dans Elmer est une équation potentiellement non linéaire. Cela signifie que nous allons baser notre travail sur {{Incode|heat.py}}.

### Modification des fichiers 

Après avoir copié `heat.py` dans `flow.py`, ajustez

-   l'argument name de la fonction create module,
-   l'attribut Type de la classe Proxy
-   les classes de base des classes `Proxy` et `ViewProxy`
-   ainsi que les propriétés ajoutées via la fonction `obj.addProperty(..)` à ceux requis par l\'équation.


```python
def create(doc, name="'''Flow'''"):
    return femutils.createObject(
        doc, name, Proxy, ViewProxy)

class Proxy(nonlinear.Proxy, equationbase.'''Flow'''Proxy):

    Type = "Fem::EquationElmer'''Flow'''"

    def __init__(self, obj):
        super(Proxy, self).__init__(obj)
        obj.Priority = 10

class ViewProxy(nonlinear.ViewProxy, equationbase.'''Flow'''ViewProxy):
    pass
```

Ensuite, vous devez changer les propriétés ajoutées via la fonction {{Incode|obj.addProperty(..)}} pour celles nécessaires à l\'équation.

Au moment de la rédaction de ce tutoriel, l\'équation de flux Elmer n\'a aucunes propriétés particulières. Voir l\'équation d\'élasticité d\'Elmer pour un exemple avec des propriétés.

Enfin, il faut enregistrer une définition de **makeEquationStatcurrent** dans `ObjectsFem.py` en dupliquant une entrée disponible.

Enfin et surtout, enregistrez le nouveau fichier de module (`flow.py`) dans les deux fichiers `src/Mod/Fem/CMakeLists.txt` comme décrit dans [Module d\'extension FEM](https://www.freecadweb.org/wiki/Extend_FEM_Module/fr). Les listes appropriées peuvent être facilement trouvées en recherchant les fichiers de modules d'équations existants d'Elmer.

## Extension de l\'objet du solveur 

Dans cette étape, nous allons modifier le fichier suivant:

-    {{FileName|src/Mod/Fem/femsolver/elmer/solver.py}}
    

À l\'heure actuelle, nous avons informé FreeCAD qu\'il existe un nouveau type d\'équation et nous avons même ajouté une commande qui ajoute cette équation à l\'objet solveur sélectionné. Nous avons également implémenté un objet d\'équation concret pour Elmer. Que reste-t-il à faire maintenant pour faire le lien entre Elmer et l\'équation de débit. Cela doit être fait directement dans l\'objet solveur Elmer.

Enregistrez le module dans lequel nous venons d\'implémenter notre nouvel objet équation (`flow.py`) avec le spécificateur d\'équation de l\'étape 1 (\"Flow\") dans la liste `_EQUATIONS` dans `elmer/solver.py`.


```python
from .equations import electrostatic
+from .equations import flow

...

_EQUATIONS = {
    "Heat": heat,
    "Elasticity": elasticity,
+    "Flow": flow,
}
```

## Extension de l\'analyse à l\'export 

Dans cette étape, nous allons modifier le fichier suivant:

-    {{FileName|src/Mod/Fem/femsolver/elmer/writer.py}}
    

C\'est la partie la plus exigeante de la mise en œuvre d\'une nouvelle équation. Ce fichier contient la classe `Writer` qui exporte l\'analyse au format sif d\'Elmer.

Pour chaque équation prise en charge, il existe une série de méthodes gérant l\'exportation de l\'équation respective. Copiez-les simplement à partir d\'une équation existante et ajustez-les à vos besoins. Notre équation de flux utilise les méthodes suivantes:

-    {{Incode|_getFlowSolver}}
    

-    {{Incode|_handleFlow}}
    

Vous devez enregistrer la méthode {{Incode|_handleFlow}} dans la classe {{Incode|Writer}} :


```python
class Writer(object):
...
    def write(self):
...
        self._handleFlow()

...

```


{{Incode|_handleFlow}}

peut contrôler une série d\'autres méthodes détaillées. Notre équation de flux utilise les méthodes détaillées suivantes :

-    {{Incode|_handleFlowConstants}}
    

-    {{Incode|_handleFlowMaterial}}
    

-    {{Incode|_handleFlowInitialVelocity}}
    

-    {{Incode|_handleFlowBndConditions}}
    

-    {{Incode|_handleFlowEquation}}
    

Nous avons maintenant terminé la partie fonction de la nouvelle équation. Ensuite, nous allons connecter la nouvelle équation à travers l\'interface graphique.

## Outil de l\'interface graphique pour créer une équation 

Nous venons de créer une nouvelle classe d\'équation. Pour y accéder depuis l\'interface graphique FEM, nous devons créer un bouton et le lier à la nouvelle classe d\'équation. Voici un tutoriel : [Tutoriel Ajouter un bouton à la barre d\'outils FEM](Add_button_to_FEM_toolbar_tutorial/fr.md).

_ _

---
[documentation index](../README.md) > [FEM](Category_FEM.md) > Add FEM equation tutorial/fr
