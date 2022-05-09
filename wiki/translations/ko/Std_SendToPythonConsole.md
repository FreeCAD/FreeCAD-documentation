---
- GuiCommand   */ko
   Name   *Std SendToPythonConsole
   Name/ko   *표준 파이썬 콘솔로 보내기
   MenuLocation   *편집 → 파이썬 콘솔로 보내기
   Workbenches   *모두
   Shortcut   ***Ctrl**+**Shift**+**P**
   Version   *0.19
---

# Std SendToPythonConsole/ko

## 설명


<div class="mw-translate-fuzzy">

**표준 파이썬 콘솔로 보내기(Std SendToPythonConsole)** 명령은 선택한 개체를 참조하는 변수를 [파이썬 콘솔](Python_console/ko.md) 안에 생성합니다. 만약 개체의 하위 셰이프를 선택했다면 변수 2개가 더 생성됩니다. 하나는 개체의 셰이프를 참조하고 다른 하나는 하위 셰이프 자체를 참조합니다. 관련 변수와 코드는 파이썬 코드를 작성하는데 사용할 수 있습니다.


</div>

Depending on the selected object and its selected subshapes, if any, the following variables are created   *

+++
| Variable name   | Referenced object(s)                                                                                                                                    |
+=================+=========================================================================================================================================================+
|  | The document containing the selected object                                                                                                             |
| {{Incode|doc}}  |                                                                                                                                                         |
|              |                                                                                                                                                         |
+++
|  | The selected Link object (only created if the selected object is a Link)                                                                                |
| {{Incode|lnk}}  |                                                                                                                                                         |
|              |                                                                                                                                                         |
+++
|  | Depending on the selected object   *                                                                                                                       |
| {{Incode|obj}}  | The selected object itself (if the selected object is not a Link)                                                                                       |
|              | The Linked object (if the selected object is a Link)                                                                                                    |
+++
|  | Depending on the type of {{Incode|obj}}   *                                                                                                  |
| {{Incode|shp}}  | The {{Incode|Shape}} property of {{Incode|obj}} (for objects derived from the {{Incode|Part   *   *Feature}} class) |
|              | The {{Incode|Mesh}} property of {{Incode|obj}} (for Mesh objects)                                                           |
|                 | The {{Incode|Points}} property of {{Incode|obj}} (for Points objects)                                                       |
+++
|  | The first selected subshape (only created if at least one subshape is selected)                                                                         |
| {{Incode|sub}}  |                                                                                                                                                         |
|              |                                                                                                                                                         |
+++
|  | A list containing all subshapes (only created if two or more subshapes are selected)                                                                    |
| {{Incode|subs}} |                                                                                                                                                         |
|              |                                                                                                                                                         |
+++

>>> ### Begin command Std_SendToPythonConsole
>>> try   *
>>>     del(doc,lnk,obj,shp,sub,subs)
>>> except Exception   *
>>>     pass
>>> 
>>> doc = App.getDocument("Unnamed")
>>> lnk = doc.getObject("Link")
>>> obj = lnk.getLinkedObject()
>>> shp = obj.Shape
>>> sub = obj.getSubObject("Edge10")
>>> subs = [obj.getSubObject("Edge10"),obj.getSubObject("Face3"),obj.getSubObject("Vertex5"),]
>>> ### End command Std_SendToPythonConsole


<div class="mw-translate-fuzzy">



*출력 예시   * [부품 상자](Part_Box/ko.md)의 모서리가 선택된 경우*


</div>

## 용법


<div class="mw-translate-fuzzy">

1.  단일 개체를 선택합니다.
2.  이 명령을 실행하는 방법은 여러 가지입니다   *
    -   메뉴에서 **편집 → <img src="images/Std_SendToPythonConsole.svg" width=16px> 파이썬 콘솔로 보내기** 옵션을 선택합니다.
    -   [트리 보기의](Tree_view/ko.md) 상황에 맞는 메뉴 혹은 [3D 보기의](3D_view/ko.md) 상황에 맞는 메뉴에서 **<img src="images/Std_SendToPythonConsole.svg" width=16px> 파이썬 콘솔로 보내기** 옵션을 선택합니다.
    -   단축키를 사용합니다   * **Ctrl**+**Shift**+**P**.


</div>

## Notes

-   All previously created variables are deleted each time the command is run.

-   If the selected object is a Link ({{Incode|App   *   *Link}}) and the Linked object is derived from the {{Incode|Part   *   *Feature}} class, the {{Incode|shp}} variable will be the shape of the Linked object. If the Link has been transformed or scaled and you want to access the scaled/transformed shape, you can do so with this code   *

   *   
    
```pythonlnk_shp = Part.getShape(lnk)```
    





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SendToPythonConsole/ko
