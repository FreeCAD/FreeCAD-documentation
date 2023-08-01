# Mesh to Part/ja
<div class="mw-translate-fuzzy">

## Partオブジェクトをメッシュに変換する


</div>


<div class="mw-translate-fuzzy">

[Part形状のような上位レベルのオブジェクトを](Part_Workbench/ja.md) [メッシュのような単純なオブジェクトに変換するのは比較的簡単な処理です](Mesh_Workbench/ja.md)。Partオブジェクトの全ての面を三角形に変換して、結果の三角形（モザイク）をメッシュ構築に使用すればいいのです：

# ドキュメントには一つだけPartオブジェクトが入っているとしましょう
# この数値がモザイクの精度を表します


</div>


```python
import Mesh

obj = FreeCADGui.Selection.getSelection()[0] # a Part object must be preselected
shp = obj.Shape
faces = []

triangles = shp.tessellate(1) # the number represents the precision of the tessellation
for tri in triangles[1]:
    face = []
    for i in tri:
        face.append(triangles[0][i])
    faces.append(face)

m = Mesh.Mesh(faces)
Mesh.show(m)
```

Alternative example:


```python
import Mesh
import MeshPart

obj = FreeCADGui.Selection.getSelection()[0] # a Part object must be preselected
shp = obj.Shape

mesh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")
mesh.Mesh = MeshPart.meshFromShape(
        Shape=shp,
        LinearDeflection=0.01,
        AngularDeflection=0.025,
        Relative=False)
```


<div class="mw-translate-fuzzy">

## メッシュをPartオブジェクトに変換する


</div>


<div class="mw-translate-fuzzy">

メッシュからPartオブジェクトへの変換はCADでの作業でも非常に重要な操作です。他の人たちからメッシュ形式の3Dデータを受け取ったり、他のアプリケーションからメッシュ形式の3Dデータを出力するというのはよくあることだからです。自由形状や大きな描画シーンを表現する場合にはメッシュは非常に実用的です。とても軽量だからです。しかしCADでの用途を考えた場合、一般的には三角形ではなく曲線で作成された面やソリッドなど、もっと多くの情報を保持できるより上位のオブジェクトの方が好まれます。


</div>


<div class="mw-translate-fuzzy">

メッシュからこういった（FreeCADの[パートモジュールで扱われる様な](Part_Module/jp.md) ）上位オブジェクトへの変換は簡単な処理ではありません。メッシュは数千もの三角形で構成されている場合もありますし（例えば3Dスキャナーによって生成されている場合）、面と同じだけの数のソリッドを持った場合には処理がとんでもなく重くなることも考えられます。従って多くの場合、変換時に最適化を施す必要があるのです。


</div>


<div class="mw-translate-fuzzy">

FreeCADでは現在、メッシュをPartオブジェクトに変換する二つのメソッドが用意されています。一つ目は単純なもので何の最適化も施さずに直接変換を行います：

 # 二つ目の引数は縫い合わせの許容誤差です


</div>


```python
import Mesh
import Part

mesh = Mesh.createTorus()
shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Topology, 0.05) # the second arg is the tolerance for sewing
solid = Part.makeSolid(shape)
Part.show(solid)
```


<div class="mw-translate-fuzzy">

二つ目のメソッドではメッシュの二つのファセットが作る角度が特定の値を下回る場合にその二つを同一面とみなします。これによってより単純な形状が作成できるのです：

# ドキュメントには一つだけMeshオブジェクトが入っているとしましょう
# ここではより厳しい許容誤差を使用します
for i in segments:
  if len(i) > 0:
     # 線分は内部に穴を持つことができます
     wires = MeshPart.wireFromSegment(mesh, i)
     # 外部境界が最大のバウンディングボックスを持つものであると仮定します
     if len(wires) > 0:
        ext=None
        max_length=0
        for i in wires:
           if i.BoundBox.DiagonalLength > max_length:
              max_length = i.BoundBox.DiagonalLength
              ext = i
        wires.remove(ext)
        # 内部のワイヤーが全てマークされ、向きが反転されなければなりません。さもなければPart.Faceが失敗します
        for i in wires:
           i.reverse()
        # 外部のワイヤーがリストの先頭になっていることを確認してください
        wires.insert(0, ext)
        faces.append(Part.Face(wires))
shell=Part.Compound(faces)
Part.show(shell)
#solid = Part.Solid(Part.Shell(faces))
#Part.show(solid)


</div>


```python
import Mesh
import Part
import MeshPart

obj = FreeCADGui.Selection.getSelection()[0] # a Mesh object must be preselected
mesh = obj.Mesh
segments = mesh.getPlanarSegments(0.00001) # use rather strict tolerance here
faces = []

for i in segments:
    if len(i) > 0:
        # a segment can have inner holes
        wires = MeshPart.wireFromSegment(mesh, i)
        # we assume that the exterior boundary is that one with the biggest bounding box
        if len(wires) > 0:
            ext = None
            max_length=0
            for i in wires:
                if i.BoundBox.DiagonalLength > max_length:
                    max_length = i.BoundBox.DiagonalLength
                    ext = i

            wires.remove(ext)
            # all interior wires mark a hole and must reverse their orientation, otherwise Part.Face fails
            for i in wires:
                i.reverse()

            # make sure that the exterior wires comes as first in the list
            wires.insert(0, ext)
            faces.append(Part.Face(wires))

solid = Part.Solid(Part.Shell(faces))
Part.show(solid)
```


 {{Mesh Tools navi}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Mesh](Mesh_Workbench.md) > Mesh to Part/ja
