# Macro clone explicit/fr
{{Macro/fr
|Name=Macro Clone explicit
|Name/fr=Macro Clone explicit
|Icon=Macro_clone_explicit.png
|Description=Crée une copie de chaque objet sélectionné et définit ses propriétés en fonction d'une expression liée à l'objet original, ce qui en fait un clone explicite et modifiable.
|Author=Raph82
|Version=0.1
|Date=2018-12-15
|FCVersion=18 et plus
|Download=[https://wiki.freecad.org/images/a/ab/Macro_clone_explicit.png Icône de la barre d'outils]
|SeeAlso=[Expressions](Expressions/fr.md)
}}

## Description

Cette macro crée une copie de chaque objet sélectionné et fixe ses propriétés à une [expression](Expressions/fr.md) liée à l\'objet original, ce qui en fait un clone explicite et modifiable.

Ce clone est une copie de l\'objet original, comme dans la commande **Edition → Dupliquer la sélection**, mais ses propriétés sont définies par des expressions.



### Comment ce \"clone explicite et modifiable\" diffère-t-il d\'un objet Clone ? 

\"Explicite\" parce que toutes les propriétés de l\'objet original sont visibles. Dans un objet Clone d\'un Cube, pouvez-vous voir sa hauteur par exemple ? Lorsque vous utilisez une expression pour un objet Clone, pouvez-vous accéder facilement aux propriétés de son parent ?

\"Editable\" parce que, contrairement à un objet Clone, vous pouvez modifier l\'expression de n\'importe quelle propriété. Il est donc possible de faire en sorte que l\'objet ne clone que certaines propriétés de son parent, tandis que vous modifiez les autres.



## Utilisation

1.  Sélectionnez au moins un objet.

2.  
    **Macro → Macros...**
    

3.  Sélectionnez la **clone_explicit.FCMacro** dans la liste.

4.  Appuyez sur le bouton **Exécuter**.

## Script

Icône de la barre d\'outils ![](images/Macro_clone_explicit.png )

**Macro_clone_explicit.FCMacro**


{{MacroCode|code=
__Title__ = "clone_explicit"
__Author__ = "Raph82"
__URL__     = "http://www.freecadweb.org/index-fr.html"
__Version__ = "0.1"
__Date__    = "2018-12-15" #YYYY-MM-DD
__Comment__ = "This macro creates a copy of the selected objects and sets their properties to an expression linking to the original object, making it an explicit and editable clone"
__Web__ = "http://www.freecadweb.org/"
__Wiki__ = "http://www.freecadweb.org/wiki/index.php?title=Macro_clone_explicit"
__Icon__  = "https://wiki.freecad.org/images/a/ab/Macro_clone_explicit.png"
__IconW__  = "C:/Users/User Name/AppData/Roaming/FreeCAD/Macro_clone_explicit.png"
__Help__ = "Select at least one object and run the macro to make explicit and editable clone(s)"
__Status__ = "dev"
__Requires__ = "All FreeCAD"
__Communication__ = "http://www.freecadweb.org/wiki/index.php?title=User:raph82"

#IMPORTS:
import sys

##################################################
def set_expression(obj, property_to_set, expression):
    """"""
    try:
        print type(obj)
        obj.setExpression(property_to_set, expression)
#    except 'Base.FreeCADError':
    except Exception as detail:
        print detail
        print type(detail)
        if detail['swhat'] == 'Property not found':
            App.Console.PrintMessage('Object "{obj}" has no property "{prop}"\r\n'.format(obj=obj.Name, prop=property_to_set))
        else:
            raise

##################################################
def clone_explicit(mode):
    """Copy the selected objects and sets their properties to an expression, making it an explicit and editable clone.

     This clone is called "explicit and editable" because the link with its parent is visible and can be changed in the object properties.

     The link to the original object can be either "direct" or "transient", depending on the mode argument:
     - a direct clone has expressions pointing to its parent: clone.Length = parent.Length
     - a transient clone has expressions pointing to its ancestor. Say parent.Length = Box001.Length. With a transient clone, clone.Length = Box001.Length, whereas with a direct clone, clone.Length = parent.Length.
       This indirect link to Box001 (via the parent object) could be severed, accidentally or not, depending on what relationship you're looking for.

     If you're lost, try with a direct clone first."""

    App.Console.PrintMessage("Start of clone_explicit macro"+"\r\n")

    #Current selection check:
    sel = FreeCADGui.Selection.getSelection()

    App.Console.PrintMessage(str(len(sel))+" object(s) selected\r\n")
    if len(sel) != 0:
        for i in range(len(sel)):
            obj=sel[i]

            #copying current object:
            App.Console.PrintMessage('Copying "'+obj.Label+'" ('+obj.Name+')\r\n')
            obj_copy=App.ActiveDocument.copyObject(obj, False) #https://www.freecadweb.org/api/d8/d3e/classApp_1_1Document.html#a08f1d7d90f4a7276a02918fb6445a04a
            App.Console.PrintMessage('"'+obj_copy.Label+'" ('+obj_copy.Name+') created\r\n')

            if mode == 'direct':
                #defining expressions pointing to the original object:
                set_expression(obj_copy, 'Placement.Base.x',          obj.Name+u'.Placement.Base.x')
                set_expression(obj_copy, 'Placement.Base.y',          obj.Name+u'.Placement.Base.y')
                set_expression(obj_copy, 'Placement.Base.z',          obj.Name+u'.Placement.Base.z')
                set_expression(obj_copy, 'Placement.Rotation.Angle',  obj.Name+u'.Placement.Rotation.Angle')
                set_expression(obj_copy, 'Placement.Rotation.Axis.x', obj.Name+u'.Placement.Rotation.Axis.x')
                set_expression(obj_copy, 'Placement.Rotation.Axis.y', obj.Name+u'.Placement.Rotation.Axis.y')
                set_expression(obj_copy, 'Placement.Rotation.Axis.z', obj.Name+u'.Placement.Rotation.Axis.z')
                set_expression(obj_copy, 'Length',                    obj.Name+u'.Length')
                set_expression(obj_copy, 'Width',                     obj.Name+u'.Width')
                set_expression(obj_copy, 'Height',                    obj.Name+u'.Height')

            elif mode == 'transient':
                #defining expressions pointing to the utmost original object:
                define_transient_expression(obj, obj_copy, 'Placement.Base.x')
                define_transient_expression(obj, obj_copy, 'Placement.Base.y')
                define_transient_expression(obj, obj_copy, 'Placement.Base.z')
                define_transient_expression(obj, obj_copy, 'Placement.Rotation.Angle')
                define_transient_expression(obj, obj_copy, 'Placement.Rotation.Axis.x')
                define_transient_expression(obj, obj_copy, 'Placement.Rotation.Axis.y')
                define_transient_expression(obj, obj_copy, 'Placement.Rotation.Axis.z')
                define_transient_expression(obj, obj_copy, 'Length')
                define_transient_expression(obj, obj_copy, 'Width')
                define_transient_expression(obj, obj_copy, 'Height')
            else:
                App.Console.PrintError('Programming error: mode value not recognized.\r\n')

            App.Console.PrintMessage('('+obj_copy.Label+'" ('+obj_copy.Name+') expressions set\r\n')

        FreeCAD.ActiveDocument.recompute()
        App.Console.PrintMessage('End of clone_explicit macro\r\n')

    else:
        App.Console.PrintError('Select at least one object first\r\n')

    sel = ""
    obj = ""
    obj_copy = ""

##################################################
def find_expression(source_object, property_to_define):
    """"""

    for var_tuple in source_object.ExpressionEngine: #https://forum.freecadweb.org/viewtopic.php?f=22&t=21950
        # .ExpressionEngine returns tuple like [('Placement.Base.z', 'Length')], see https://docs.python.org/2.7/tutorial/datastructures.html#tuples-and-sequences
        App.Console.PrintMessage('var_tuple[0]='+var_tuple[0]+'\r\n')
        if var_tuple[0] == property_to_define:
           return var_tuple[1]

##################################################
def define_transient_expression(source_object, target_object, property_to_define):
    """"""
    expressions = source_object.ExpressionEngine #https://forum.freecadweb.org/viewtopic.php?f=22&t=21950
    # returns tuple like [('Placement.Base.z', 'Length')], see https://docs.python.org/2.7/tutorial/datastructures.html#tuples-and-sequences

    expression = find_expression(source_object, property_to_define)
    if expression != None:
#        App.Console.PrintMessage("target_object.Name="+target_object.Name+"\r\n")
#        App.Console.PrintMessage("property_to_define="+property_to_define+"\r\n")
#        App.Console.PrintMessage("expressions[property_to_define]="+expressions[property_to_define]+"\r\n")

        set_expression(target_object, property_to_define, expression)
    else:
        set_expression(target_object, property_to_define, source_object.Name+'.'+property_to_define)

    expressions = ""

##################################################
clone_explicit('direct')
#clone_explicit('transient')
}}

## Options

Une option mode était prévue. Elle n\'a pas encore été mise en œuvre. Elle semble maintenant beaucoup plus complexe qu\'initialement prévu, peut-être trop complexe pour moi à mettre en œuvre.

L\'idée est que l\'on peut préférer l\'un ou l\'autre comportement :

-   le clone continue à imiter son parent même si les propriétés *expressions* du parent changent. C\'est le mode direct,
-   le clone conserve les propriétés *expressions* que le parent avait au moment de la création du clone. C\'est le mode transitoire.

Remarquez l\'accent mis sur le mot \"expressions\". Une expression est une couche d\'abstraction au-dessus d\'une valeur.

Voici un exemple. Imaginons que l\'objet parent (celui que vous sélectionnez avant d\'exécuter la macro) ait sa propriété Height définie par l\'expression Object**3**.Height * 2.

-   Lorsque vous êtes en mode direct :
    -   Clone.Height = Parent.Height,
    -   devient une valeur Object**3**.Height qui affecterait à la fois l\'objet parent et les objets clones,
    -   devient une *expression* Parent.Height qui affecterait **aussi** les deux objets :
        -   Parent.Height = Object**4**.Height * 2 et
        -   Clone.Height = Parent.Height encore.
-   Lorsque vous êtes en mode transient :
    -   Clone.Height = Object**3**.Height * 2,
    -   devient une valeur Object**3**.Height qui affecterait à la fois l\'objet parent et les objets clones,
    -   devient une *expression* Parent.Height qui affecterait **seulement** l\'objet parent :
        -   Parent.Height = Object**4**.Height * 2 et
        -   Clone.Height = Object**3**.Height * 2 encore.

Pour l\'instant, la macro est exécutée avec le paramètre mode réglé sur direct et aucun choix n\'est proposé à l\'utilisateur.

## Limitations

-   Ne fonctionne bien qu\'avec les cubes pour le moment. Pour étendre à de nombreux types, je dois :
    -   trouver comment identifier un type d\'objet pour traiter ses différentes propriétés en conséquence ;
    -   trouver comment attraper l\'erreur Property not found.



## Historique des versions 

-   0.1 : première version publique



---
⏵ [documentation index](../README.md) > Macro clone explicit/fr
