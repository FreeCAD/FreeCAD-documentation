# Troubleshooting models

## Intro

This page is to help find solutions to problems that can occur across multiple modeling commands. Errors specific to a certain command should be put on the appropriate wiki page for the command.

## Troubleshooting FAQ 

**Part Turns Black**

-   Cause: Faces that should be on inside are on outside
-   Resolution: Try creating part using commands in a different order

**Part Design Command will not complete with Not Contiguous Solid error**

-   Cause: Part Design commands only work with continuous body
-   Solution: Create sepereate body if there should be space between bodies or check that sketches are at least flush with existing body.

**FreeCAD crashes while creating fillets or chamfers**

-   Cause: OCC bug that causes a crash when an invalid fillet or chamfer is attempted
-   Solution: Change radius to valid value

**My edge based features keep changing position**

-   Cause: Topological naming is not stable meaning edge and face names change, changing which face etc. you feature is based on.
-   Solution: Finish the main design work of your solid body before applying features like fillets and chamfers.

**My face based features keep changing position**

-   Cause: Topological naming is not stable meaning face names change, changing which face your feature is based on.
-   Solution: Do not use the attach to face feature for defining sketchs. Use a datum plane instead.

**Command fails to complete with TopoDS::Edge, TopoDS::Shell, BRep\_API: command not done or BRep\_Tool:: no parameter on edge**

-   Cause: OCC call fails. The selection(s) made to define your command are incorrect or lead to a case that is not handled by OCC.
-   Solution: Try using different selections for command or using a different command.
