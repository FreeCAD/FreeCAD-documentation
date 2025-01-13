# Console API/fr
**(octobre 2019) Ne pas éditer cette page. L'information est incomplète et obsolète. Pour la dernière API, voir la [https://www.freecadweb.org/api documentation de l'API générée automatiquement], ou générez la documentation vous-même, voir [Documentation du code source](Source_documentation/fr.md).**

Ce module est contenu dans le module FreeCAD et contient des méthodes pour envoyer le texte à la console de sortie FreeCAD et à la barre d\'état. Les messages seront de couleur différente suivant s\'ils sont des messages, des avertissements ou des erreurs.

Exemple: 
```python
import FreeCAD
FreeCAD.Console.PrintMessage("Hello World!\n")
```


{{APIFunction | GetStatus | "Connexion" ou "Msg" ou "Avert" ou "Err" | Obtenir le statut soit pour la Connexion, Msg, Avert ou erreur pour un observateur |. Une chaîne d'état}}

{{APIFunction | PrintError | chaîne | Imprime un message d'erreur à la sortie | rien}} 


{{APIFunction | PRINTLOG | chaîne | Imprime un message de de connexion à la sortie | rien}}


{{APIFunction | PrintMessage | chaîne | Imprime un message à la sortie | rien}}


{{APIFunction | PrintWarning | chaîne | Imprime un avertissement à la sortie | rien}}


{{APIFunction | SetStatus | chaîne | Définir les états pour soit Connexion, Msg, Avert ou erreur pour un observateur |}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Console API/fr
