# Macro Unfold Box/pl
{{Macro
|Name=Macro Unfold Box
|Icon=Macro_Unfold_Box.png
|Description=The macro allows to unfold the surfaces of a box of any shape and to draw them on a page.
|Author=Hervé B., heda
|Version=1.1
|Date=2022-07-28
|FCVersion=
|Download=[https://www.freecadweb.org/wiki/images/e/e4/Macro_Unfold_Box.png ToolBar Icon]
}}

## Description

The macro allows to unfold the surfaces of a box of any shape and to draw them on a page.

<img alt="" src=images/Macro_unfoldBox1.png  style="width:480px;"> 
*Macro Unfold Box*

## Installation

Available in the [Addon manager](Std_AddonMgr.md).

Forum topic: [Macro for unfolding box surfaces](http://forum.freecadweb.org/viewtopic.php?f=17&t=4587).

## Options

-   Scale manually or automatically.
-   Page format: A4/A3, cartridge (cf FreeCAD templates).
-   Group drawings on the same page if possible.
-   Sew the edges of the pieces or not.

![Macro_unfoldBox](images/Macro_UnFoldBox_start_form.png )

## Usage

1.  Select a box made with the [Part Loft](Part_Loft.md) tool for example.
2.  [Draft Downgrade](Draft_Downgrade.md) it into separate faces.
3.  Select the faces.
4.  Execute the macro.

The unfolding algorithm will place the faces on the XY plane, however it seldom does the unfolding correctly. Thus some manual post-processing is needed to get to desired result, as shown in the picture below.

![Macro_unfoldBox](images/MacroUnFoldBoxInstruction.png )

Starting point is a box like the upper left picture.

1.  Select all faces and run the macro.
2.  Orient to Top View.
3.  Toggle the visibility on the created set of faces, the individual clones are to be visible, not the compound.
4.  Use [Draft Move](Draft_Move.md) and [Draft Rotate](Draft_Rotate.md) to reposition the unfolded cloned faces (a handful of clicks per face when snapping is used).
5.  The drawing updates automatically to the new positions.

The finished result is shown in the lower right picture above.

## Script

ToolBar icon ![](images/Macro_Unfold_Box.png )

**Macro_unfoldBox.FCMacro**

    # -*- coding: utf-8 -*-
    """
    FreeCAD Macro unfoldBox.

    Unfolding of planar surfaces
    """
    ##################################################
    # SEE https://wiki.freecadweb.org/Macro_Unfold_Box
    # ***************************************************************************
    # *                                                                         *
    # *   Copyright (c) 2013 - DoNovae/Herve BAILLY <hbl13@donovae.com>         *
    # *   Copyright (c) 2022 - heda <heda@fc-forum>                             *
    # *                                                                         *
    # *   This program is free software; you can redistribute it and/or modify  *
    # *   it under the terms of the GNU Lesser General Public License (LGPL)    *
    # *   as published by the Free Software Foundation; either version 2 of     *
    # *   the License, or (at your option) any later version.                   *
    # *   for detail see the LICENCE text file.                                 *
    # *                                                                         *
    # *   This program is distributed in the hope that it will be useful,       *
    # *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
    # *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
    # *   GNU Library General Public License for more details.                  *
    # *                                                                         *
    # *   You should have received a copy of the GNU Library General Public     *
    # *   License along with this program; if not, write to the Free Software   *
    # *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
    # *   USA                                                                   *
    # *                                                                         *
    # ***************************************************************************

    __Name__ = 'Unfold Box'
    __Comment__ = 'Unfolds planar surfaces and draws them on a page.'
    __Author__ = 'Hervé B., heda'
    __Version__ = '1.1'
    __Date__ = '2022-07-28'
    __License__ = 'LGPL-2.0-or-later'
    __Web__ = 'https://wiki.freecad.org/Macro_Unfold_Box'
    __Wiki__ = 'https://wiki.freecad.org/Macro_Unfold_Box'
    __Icon__ = ''
    __Help__ = ('Select surfaces, Explode them (cf Draft menu Downgrade), '
                'Select the exploded surfaces, Execute the macro')
    __Status__ = ''
    __Requires__ = ''
    __Communication__ = ''
    __Files__ = ''

    __doc__ = """
    select a face, or several and run the macro.
    a shell/solid needs to be draft/downgraded to get the faces as separate objects

    the macro is intended to unfold a set of planar faces,
    in current state, most of the times it does not place the faces correctly.
    thus one needs to do the final placement of the clones manually, with Draft/Move & Rotate
    regardless, the macro saves a lot of clicks compared to a fully manual unfold

    settings are not context aware, all settings not applicable are ignored.
    as example, using autoscaling ignores the scale-value in the form

    sew is always enabled, thus the drawing
    is always the sewed shape on a single page


    v1.1   (2022-07-28) py3/qt5 compat, cosmetic code changes,
           minor code tweaks for evolved fc-api
           added option to skip drawing, made layout engine with techdraw,
           the drawing wb layout engine is now called "legacy"
    v1.0.1 (2020-03-10) - on wiki
    v1.0   (2013-09-14) - on wiki

    note:
    - unfolding occasionally work as expected, but mostly not
    - anyone is free to improve functionality

    """

    import os, math

    from PySide import QtGui, QtCore

    import FreeCAD, FreeCADGui
    import Draft

    Vector = FreeCAD.Base.Vector
    Units = FreeCAD.Units
    PrintMessage = FreeCAD.Console.PrintMessage
    PrintError = FreeCAD.Console.PrintError

    fields_l = []
    unroll_l = []
    dwgtpllegacy = 'Mod/Drawing/Templates'
    dwgtpl = 'Mod/TechDraw/Templates'


    #####################################
    ###   Functions
    #####################################


    def errorDialog(msg):
        diag = QtGui.QMessageBox(QtGui.QMessageBox.Critical, 'Error Message', msg)
        diag.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        diag.exec_()


    def proceed():
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        PrintMessage('===========================================\n')
        PrintMessage('unfoldBox: start.\n')
        try:
            file_name = fields_l[0].text()
            makedwg = makedwg_check.isChecked()
            leglay = leglay_check.isChecked()
            scale = float(fields_l[1].text())
            scale_auto = scale_check.isChecked()
            a3 = a3_check.isChecked()
            cartridge = cartridge_check.isChecked()
            onedrawing = onedrawing_check.isChecked()
            sewed = sewed_check.isChecked()
            PrintMessage('unfoldBox.file_name: {}\n'.format(file_name))
            PrintMessage('unfoldBox.makedwg: {}\n'.format(makedwg))
            PrintMessage('unfoldBox.leglay: {}\n'.format(leglay))
            PrintMessage('unfoldBox.scale: {}\n'.format(scale))
            PrintMessage('unfoldBox.scale_check: {}\n'.format(scale_auto))
            PrintMessage('unfoldBox.a3_check: {}\n'.format(a3))
            PrintMessage('unfoldBox.cartridge: {}\n'.format(cartridge))
            PrintMessage('unfoldBox.onedrawing: {}\n'.format(onedrawing))
            PrintMessage('unfoldBox.sewed: {}\n'.format(sewed))
        except:
            msg = 'unfoldBox: wrong inputs...\n'
            PrintError(msg)
            errorDialog(msg)

        QtGui.QApplication.restoreOverrideCursor()
        DialogBox.hide()

        ## Get selection
        sel = FreeCADGui.Selection.getSelection()
        if not sel or len(sel) < 2:
            PrintMessage('unfoldBox: requires at least 2 selected faces, ending.\n')
            return

        doc = FreeCAD.ActiveDocument

        objnames_l=[]
        grp = doc.addObject('App::DocumentObjectGroup', str(file_name))
        for objid in range(len(sel)):
            obj = Draft.make_clone(sel[objid])
            grp.addObject(obj)
            objnames_l.append([ obj, sel[objid].Name ])

        doc.recompute()
        unfold = unfoldBox(doc)
        if sewed:
            objnames_l = unfold.done(objnames_l)
            grp.addObject(objnames_l[0][0])
        else:
            for objid in range(len(objnames_l)):
                unfold.moveXY(objnames_l[objid][0])

        if not makedwg:
            return

        if leglay:
            idx = 0
            while len(objnames_l) > 0:
                draw = Drawing2dLegacy(scale, scale_auto, a3,
                                       cartridge, onedrawing,
                                       doc.Name, 'Page'+str(idx))
                objnames_l = draw.all_(objnames_l)
                idx += 1
                PrintMessage('unfoldBox: obj_l= {}\n'.format(len(objnames_l)))
        else:
            draw = Drawing2d(scale, scale_auto, a3, cartridge)
            draw.drawpage(objnames_l[0], "{}Page".format(file_name))

        PrintMessage('unfoldBox: end.\n')
        PrintMessage('===========================================\n')


    def close():
        DialogBox.hide()


    def getType(obj):
        return type(obj).__name__

    def mkmm(l):
        return Units.Quantity(l, Units.Length)

    class unfoldBox:
        def __init__(self, doc):
            PrintMessage('unfoldBox.unfoldBox\n')
            self.doc = doc
            self.LIMIT = 0.0001

        def done(self, objnames_l):
            tree_l = self.makeTree(objnames_l)
            for idx in range(len(objnames_l)):
                face = objnames_l[idx]
                self.moveXY(face[0])
            self.sew(objnames_l, tree_l)
            return self.fusion(objnames_l)

        def getEndPoints(self, edge):
            return [v.Point for v in edge.Vertexes]

        def makeTree(self, objnames_l):
            ## Initialisation of tree_l.
            tree_l = []
            for k in range(len(objnames_l)):
                facek = objnames_l[k][0]
                facekEdges = facek.Shape.Edges
                facek_l = []
                for i in range(len(facekEdges)):
                    if False and getType(facekEdges[i].Curve) != 'GeomLineSegment':
                        ## this is a no-op...
                        facek_l.append([-1, -1])
                    else:
                        ## Search face link to the ith edge
                        #vki0 = facekEdges[i].Curve.StartPoint
                        #vki1 = facekEdges[i].Curve.EndPoint
                        vki0, vki1 = self.getEndPoints(facekEdges[i])
                        found = False
                        for l in range(k+1, len(objnames_l)):
                            facel = objnames_l[l][0]
                            facelEdges = facel.Shape.Edges
                            for j in range(len(facelEdges)):
                                #vlj0 = facelEdges[j].Curve.StartPoint
                                #vlj1 = facelEdges[j].Curve.EndPoint
                                vlj0, vlj1 = self.getEndPoints(facelEdges[j])
                                if (vki0.isEqual(vlj0, self.LIMIT)
                                    and vki1.isEqual(vlj1, self.LIMIT)):
                                    arelinked = False
                                    isfacek = isfacel = False
                                    for kk in range(k-1):
                                        for ii in range(len(tree_l[kk])):
                                            isfacek = tree_l[kk][ii][0] == k
                                            isfacel = tree_l[kk][ii][0] == l
                                        if isfacek and isfacel:
                                            arelinked = True
                                            break
                                    if not arelinked:
                                        facek_l.append([l, j])
                                        found = True
                                        break
                                if found:
                                    break
                    if not found:
                        facek_l.append([-1, -1])
                tree_l.append(facek_l)
            return tree_l

        def sew(self, objnames_l, tree_l):
            placed_l = []
            for k in range(len(tree_l)):
                iskplaced = False
                for p in range(len(placed_l)):
                    iskplaced = placed_l[p] == k
                if not iskplaced:
                    placed_l.append(k)
                facek = tree_l[k]
                objk = objnames_l[k][0]
                for i in range(len(facek)):
                    edgeki = facek[i]
                    l, j = edgeki[:2]
                    islplaced = False
                    for p in range(len(placed_l)):
                        if placed_l[p] == l:
                            islplaced = True
                            break
                    if not islplaced:
                        placed_l.append(l)
                    if l >= 0 and not (islplaced and iskplaced):
                        iskplaced = True
                        ## Move facel.edgelj to facek.edgeki.
                        objl = objnames_l[l][0]
                        #vki0 = objk.Shape.Edges[i].Curve.StartPoint
                        #vki1 = objk.Shape.Edges[i].Curve.EndPoint
                        vki0, vki1 = self.getEndPoints(objk.Shape.Edges[i])
                        #vlj0 = objl.Shape.Edges[j].Curve.StartPoint
                        #vlj1 = objl.Shape.Edges[j].Curve.EndPoint
                        vlj0, vlj1 = self.getEndPoints(objk.Shape.Edges[j])
                        vk = vki1.sub(vki0)
                        vl = vlj1.sub(vlj0)
                        alpk = vk.getAngle(vl) * 180 / math.pi
                        alpl = vl.getAngle(vk) * 180 / math.pi
                        self.isPlanZ(objk)
                        if islplaced:
                            Draft.move(objk, vlj0.sub(vki0))
                        else:
                            Draft.move(objl, vki0.sub(vlj0))
                        self.isPlanZ(objk)

                        if math.fabs(vk.dot(Vector(-vl.y, vl.x, 0))) > self.LIMIT:
                            if islplaced:
                                Draft.rotate(objk, -alpl, vlj0, self.vecto(vl, vk))
                            else:
                                Draft.rotate(objl, -alpk, vki0, self.vecto(vk, vl))
                        elif vk.dot(vl) < 0:
                            if islplaced:
                                Draft.rotate(objk, 180, vlj0, self.vecto(vl, Vector(-vl.y, vl.x, 0)))
                            else:
                                Draft.rotate(objl, 180, vki0, self.vecto(vk, Vector(-vk.y, vk.x, 0)))
                        ## Verifications.
                        #vki0 = objk.Shape.Edges[i].Curve.StartPoint
                        #vki1 = objk.Shape.Edges[i].Curve.EndPoint
                        vki0, vki1 = self.getEndPoints(objk.Shape.Edges[i])
                        #vlj0 = objl.Shape.Edges[j].Curve.StartPoint
                        #vlj1 = objl.Shape.Edges[j].Curve.EndPoint
                        vli0, vli1 = self.getEndPoints(objk.Shape.Edges[j])
                        vk = vki1.sub(vki0)
                        vl = vlj1.sub(vlj0)
                        self.isPlanZ(objk)

                        ## Flip or not.
                        bbl, bbk = objl.Shape.BoundBox, objk.Shape.BoundBox
                        L = max(bbl.XMax, bbk.XMax) - min(bbl.XMin, bbk.XMin)
                        W = max(bbl.YMax, bbk.YMax) - min(bbl.YMin, bbk.YMin)
                        S1 = L * W
                        if islplaced:
                            Draft.rotate(objk, 180, vlj0, vl)
                        else:
                            Draft.rotate(objl, 180, vki0, vk)
                        bbl, bbk = objl.Shape.BoundBox, objk.Shape.BoundBox
                        L = max(bbl.XMax, bbk.XMax) - min(bbl.XMin, bbk.XMin)
                        W = max(bbl.YMax, bbk.YMax) - min(bbl.YMin, bbk.YMin)
                        S2 = L * W
                        if S2 <= S1:
                            if islplaced:
                                Draft.rotate(objk, 180, vlj0, vl)
                            else:
                                Draft.rotate(objl, 180, vki0, vk)
                        self.isPlanZ(objk)

        def isPlanZ(self, obj):
            bb = obj.Shape.BoundBox
            L = bb.XMax - bb.XMin
            W = bb.YMax - bb.YMin
            H = bb.ZMax - bb.ZMin
            return H < self.LIMIT


        def fusion(self, objnames_l):
            ## Init.
            obj_l, objna_l =[], []
            obj0, name = objnames_l[0]
            objfuse = self.doc.addObject('Part::MultiFuse', 'Unfolding')
            for k in range(len(objnames_l)):
                objk = objnames_l[k][0]
                obj_l.append(objk)

            objfuse.Shapes = obj_l
            self.doc.recompute()
            objna_l.append([objfuse, name])
            return objna_l

        def get2Vectors(self, shape):
            """not used in v1.1"""
            v0, v1 = Vector(), Vector()

            edges = shape.Edges
            for idx in range(len(edges) - 1):
                e1, e2 = edges[idx], edges[idx + 1]
                ## .EndPoint errors out...
                va = e1.Curve.EndPoint.sub(e1.Curve.StartPoint)
                vb = e2.Curve.EndPoint.sub(e2.Curve.StartPoint)
                if vb.sub(va).Length > v1.sub(v0).Length:
                    v0, v1 = self.vect_copy(va), self.vect_copy(vb)
            return [v0, v1]

        def vecto(self, vect1, vect2):
            '''Function vecto.'''
            v = Vector()
            v.x = vect1.y * vect2.z - vect1.z * vect2.y
            v.y = vect1.z * vect2.x - vect1.x * vect2.z
            v.z = vect1.x * vect2.y - vect1.y * vect2.x
            return v

        def vect_copy(self, vect):
            '''Return a copy of vector.'''
            return vect.add(Vector())

        def moveXY(self, obj):
            ## Move to origin
            bb = obj.Shape.BoundBox
            Draft.move(obj, Vector(-bb.XMin, -bb.YMin, -bb.ZMin))

            ## Find 2 vectors defining the plan of surface
            #tab = self.get2Vectors(obj.Shape)
            #v0, v1 = tab[:2]
            #norm = self.vecto(v0, v1)
            #norm.normalize()
            ## above gives null vector, and errors out...

            ## probably sprung out of some api-change over time
            ## probably part.line vs part.linesegment...
            ## a part.line does not have edge.Curve.StartPoint, or .EndPoint any more
            ## the semantics is to get first & second point from a line,
            ## so edge.Curve.value(edge.Curve.FirstParameter) should get the sought values
            ## however easier to just use edge.Vertexes...
            ## which appears to have same orientation

            norm = obj.Shape.findPlane().Axis ## works for planar surfaces
            #norm = obj.Shape.Surface.Axis ## gives worse results...
            norm.normalize()

            ## Rotate.
            nx, ny, nz = (math.fabs(xyz) for xyz in norm)
            if nx < self.LIMIT and nz < self.LIMIT:
                Draft.rotate(obj, 90, Vector(0, 0, 0), Vector(1, 0, 0))
            elif ny < self.LIMIT and nz < self.LIMIT:
                Draft.rotate(obj, 90, Vector(0, 0, 0), Vector(0, 1, 0))
            else:
                ## Rotate following the angle to the normal direction of the plan.
                oz = Vector(0, 0, 1)
                alp = oz.getAngle(norm) * 180 / math.pi
                vecto = self.vecto(oz, norm)
                rotv = oz if vecto.isEqual(Vector(), self.LIMIT) else self.vecto(oz, norm)
                #rotv = norm if vecto.isEqual(Vector(), self.LIMIT) else self.vecto(oz, norm)
                ## flipping here seems to give worse results as well...
                Draft.rotate(obj, -alp, Vector(0, 0, 0), rotv)

            ## Move to z = 0.
            Draft.move(obj, Vector(0, 0, -obj.Shape.BoundBox.ZMin))


    class Scale:
        """keeps autoscaling to integers"""
        def __init__(self, scale):
            self.scale = scale if scale >= 1 else 1 / scale
            self.scale = int(self.scale)
            self.inverted = scale >= 1

        def get(self):
            if self.inverted:
                return self.scale, '{}:1'.format(self.scale)
            else:
                return 1/self.scale, '1:{}'.format(self.scale)


    class Drawing2d:
        def __init__(self, scale, scale_auto, a3, cartridge):
            """techdraw based layout for one page only"""
            self.scale = scale
            self.scale_auto = scale_auto
            self.a3 = a3
            self.cartridge = cartridge
            if a3:
                self.WH = 420, 297
            else:
                self.WH = 297, 210
            self.doc = FreeCAD.ActiveDocument

        def newPage(self, page_name):
            freecad_dir = os.path.join(FreeCAD.getResourceDir(), dwgtpl)
            page = self.doc.addObject('TechDraw::DrawPage', page_name)
            template = self.doc.addObject('TechDraw::DrawSVGTemplate', 'Template')
            size = 'A3' if self.a3 else 'A4'
            frame = 'TD' if self.cartridge else '_blank'
            template.Template = freecad_dir + '/{}_Landscape{}.svg'.format(size, frame)
            page.Template = template

            return page

        def drawpage(self, objname, page_name):
            page = self.newPage(page_name)
            faceset, name = objname

            bb = faceset.Shape.BoundBox
            ## bb does not auto-update, have to pick up new bb after manipulation
            if bb.YLength > bb.XLength: ## auto rotate
                Draft.rotate(faceset, 90)
                bb = faceset.Shape.BoundBox

            Draft.move(faceset, Vector(-bb.XMin, -bb.YMin, 0))
            bb = faceset.Shape.BoundBox

            W, H = self.WH
            xr, yr = W / bb.XLength, H / bb.YLength
            adjust = 0.7 if self.cartridge else 0.85
            scale = min(xr, yr) * adjust if self.scale_auto else self.scale
            scale, scr = Scale(scale).get()
            bb.scale(scale, scale, 1) ## faceset in xy-plane


            TopView = self.doc.addObject('TechDraw::DrawViewPart', 'TopView')
            page.addView(TopView)
            TopView.Source = faceset
            TopView.Direction = (0, 0, 1)
            TopView.XDirection = (1, 0, 0)
            TopView.Scale = scale

            Text = self.doc.addObject('TechDraw::DrawViewAnnotation', name)
            page.addView(Text)
            Text.Text = name
            Text.recompute() # for size
            bb.scale(scale, scale, scale)
            yt = (H - bb.YLength) / 2 - Text.TextSize.Value * 1.5
            Text.Y = max(1, yt)

            self.doc.recompute()
            page.ViewObject.doubleClicked()
            FreeCADGui.runCommand('TechDraw_ToggleFrame', 0)


    class Drawing2dLegacy:
        def __init__(self, scale, scale_auto, a3, cartridge, onedrawing,
                     drawing_name, page_name):
            """Function __init__

            - scale
            - scale_auto
            - a3
            - cartridge
            - onedrawing
            v1.1 - renamed to legacy, functional wise untouched
            """
            self.TopX_H = self.TopY_H = 0
            self.TopX_V = self.TopY_V = 0
            self.TopX_Hmax = self.TopY_Hmax = 0
            self.TopX_Vmax = self.TopY_Vmax = 0
            self.a3 = a3
            self.scale = scale
            self.scale_auto = scale_auto
            self.cartridge = cartridge
            self.onedrawing = onedrawing
            self.marge = 6
            if self.a3:
                self.L, self.H = 420, 297
            else:
                self.L, self.H = 297, 210
            self.page_name = page_name
            self.drawing_name = drawing_name
            self.doc = FreeCAD.ActiveDocument

        def newPage(self):
            freecad_dir = os.path.join(FreeCAD.getResourceDir(), dwgtpllegacy)
            page = self.doc.addObject('Drawing::FeaturePage', self.page_name)
            size = 'A3' if self.a3 else 'A4'
            frame = '' if self.cartridge else '_plain'
            page.Template = freecad_dir + '/{}_Landscape{}.svg'.format(size, frame)
            return page

        def all_(self, objnames_l):
            obj_l = []
            for objid in range(len(objnames_l)):
                if objid == 0 or not self.onedrawing:
                    self.newPage()
                obj_l.extend(self.done(objid, objnames_l[objid]))
            return obj_l

        def done(self, id_, objname):
            ## Init.
            obj_l = []
            obj, objname = objname
            bb = obj.Shape.BoundBox
            xmax, ymax = bb.XMax - bb.XMin, bb.YMax - bb.YMin
            if ymax > xmax:
                Draft.rotate(obj, 90)
                bb = obj.Shape.BoundBox

            Draft.move(obj, Vector(-bb.XMin, -bb.YMin, 0))
            bb = obj.Shape.BoundBox ## does not auto-update, have to pick up new obj
            xmax = bb.XMax - bb.XMin
            ymax = bb.YMax - bb.YMin

            scale = min((self.L-4*self.marge) / xmax, (self.H-4*self.marge) / ymax)

            if (not self.scale_auto) or (self.onedrawing):
                scale = self.scale

            if id_ == 0 or not self.onedrawing:
                ## Init.
                PrintMessage('Drawing2d: init\n')
                self.TopX_H = self.TopY_H = self.marge * 2
                TopX, TopY = self.TopX_H, self.TopY_H
                self.TopX_H = self.TopX_H + xmax * scale + self.marge
                self.TopY_H = self.TopY_H
                self.TopX_Hmax = max(self.TopX_Hmax, self.TopX_H)
                self.TopY_Hmax = max(self.TopY_Hmax,
                                     self.TopY_H + ymax*scale + self.marge)
                self.TopX_Vmax = max(self.TopX_Vmax, self.TopX_Hmax)
                self.TopX_V = max(self.TopX_Vmax, self.TopX_V)
                self.TopY_V = self.marge * 2

            elif self.onedrawing:
                if self.TopX_H + xmax * scale < self.L:
                    if self.TopY_H + ymax * scale + self.marge*2 < self.H:
                        ## H Add at right on same horizontal line.
                        PrintMessage('Drawing2d: horizontal\n')
                        TopX, TopY = self.TopX_H, self.TopY_H
                        self.TopX_H = self.TopX_H + xmax * scale + self.marge
                        self.TopX_Hmax = max(self.TopX_Hmax, self.TopX_H)
                        self.TopY_Hmax = max(self.TopY_Hmax,
                                             self.TopY_H + ymax*scale + self.marge)
                        self.TopX_Vmax = max(self.TopX_Hmax, self.TopX_Vmax)
                        self.TopX_Vmax = max(self.TopX_Vmax, self.TopX_Hmax)
                        self.TopX_V = max(self.TopX_Vmax, self.TopX_V)
                    else:
                        ## V Add at right on same horizontal line
                        PrintMessage('Drawing2d: vertival\n')
                        if (self.TopX_V + ymax * scale + 2 * self.marge < self.L
                            and self.TopY_V + xmax * scale + 2*self.marge < self.H):
                            Draft.rotate(obj, 90)
                            bb = obj.Shape.BoundBox
                            Draft.move(obj, Vector(-bb.XMin, -bb.YMin, 0))
                            self.TopX_V = max(self.TopX_Vmax, self.TopX_V)
                            TopX, TopY = self.TopX_V, self.TopY_V
                            self.TopX_V = self.TopX_V + ymax * scale + self.marge
                            self.TopY_Vmax = max(self.TopY_Vmax,
                                                 self.TopY_V + xmax * scale + self.marge)
                        else:
                            obj_l.append([obj, 'name'])
                            return obj_l
                else:
                    ## H Carriage return.
                    if (self.TopY_Hmax + ymax * scale + self.marge*2 < self.H):
                        msg = 'Drawing2d: carriage return: {} > {}\n'
                        PrintMessage(msg.format(self.TopY_H + ymax * scale, self.H))
                        TopX = self.marge*2
                        TopY = self.TopY_Hmax
                        self.TopX_H = TopX + xmax * scale + self.marge
                        self.TopY_H = TopY
                        self.TopX_Hmax = max(self.TopX_Hmax, self.TopX_H)
                        self.TopY_Hmax = self.TopY_Hmax + ymax*scale+self.marge
                        self.TopX_Vmax = max(self.TopX_Vmax, self.TopX_Hmax)
                        self.TopX_V = max(self.TopX_Vmax, self.TopX_V)
                    else:
                        ## V Add at right on same horizontal line.
                        msg = 'Drawing2d: vertical: {}, {}\n'
                        PrintMessage(msg.format(self.TopX_V, self.TopX_Vmax))
                        if (self.TopX_V + ymax * scale + 2*self.marge < self.L
                            and self.TopY_V + xmax * scale + 2*self.marge < self.H):
                            Draft.rotate(obj, 90)
                            bb = obj.Shape.BoundBox
                            Draft.move(obj, Vector(-bb.XMin, -bb.YMin, 0))
                            TopX, TopY = self.TopX_V, self.TopY_V
                            self.TopX_V = self.TopX_V + ymax * scale + self.marge
                            self.TopY_Vmax = max(self.TopY_Vmax,
                                                 self.TopY_V + xmax * scale + self.marge)
                        else:
                            obj_l.append([obj, 'name'])
                            return obj_l

            page = self.doc.getObject(self.page_name)

            ## Drawing wb (untouched)
            Text = self.doc.addObject('Drawing::FeatureViewAnnotation', objname + '_txt')
            Text.Text = objname
            Text.X = TopX + xmax / 2 * scale
            Text.Y = TopY + ymax / 2 * scale
            Text.Scale = 7 if self.a3 else 5

            TopView = self.doc.addObject('Drawing::FeatureViewPart', 'TopView')
            TopView.Source = obj
            TopView.Direction = (0.0, 0.0, 1)
            TopView.Rotation = 0
            TopView.X = TopX
            TopView.Y = TopY
            TopView.ShowHiddenLines = True
            TopView.Scale = scale
            page.addObject(TopView)
            page.addObject(Text)

            self.doc.recompute()
            page.ViewObject.doubleClicked()

            return obj_l


    #####################################
    ###   Dialog Box
    #####################################
    fields = [['Group Name', 'Unfolding']]
    fields.append(['Scale', '1'])

    DialogBox = QtGui.QDialog()
    DialogBox.resize(250, 250)
    DialogBox.setWindowTitle('unfoldBox')
    la = QtGui.QVBoxLayout(DialogBox)

    # Input fields.
    for id_ in range(len(fields)):
        la.addWidget(QtGui.QLabel(fields[id_][0]))
        fields_l.append(QtGui.QLineEdit(fields[id_][1]))
        la.addWidget(fields_l[id_])

    makedwg_check = QtGui.QCheckBox(DialogBox)
    makedwg_check.setObjectName('checkBox')
    makedwg_check.setChecked(True)
    la.addWidget(QtGui.QLabel('Make drawing'))
    la.addWidget(makedwg_check)

    leglay_check = QtGui.QCheckBox(DialogBox)
    leglay_check.setObjectName('checkBox')
    leglay_check.setChecked(False)
    la.addWidget(QtGui.QLabel('Legacy layout'))
    la.addWidget(leglay_check)

    scale_check = QtGui.QCheckBox(DialogBox)
    scale_check.setObjectName('checkBox')
    scale_check.setChecked(True)
    la.addWidget(QtGui.QLabel('Scale auto'))
    la.addWidget(scale_check)

    a3_check = QtGui.QCheckBox(DialogBox)
    a3_check.setObjectName('checkBox')
    la.addWidget(QtGui.QLabel('A3 Format'))
    a3_check.setChecked(False)
    la.addWidget(a3_check)

    cartridge_check = QtGui.QCheckBox(DialogBox)
    cartridge_check.setObjectName('checkBox')
    la.addWidget(QtGui.QLabel('Cartridge'))
    cartridge_check.setChecked(False)
    la.addWidget(cartridge_check)

    onedrawing_check = QtGui.QCheckBox(DialogBox)
    onedrawing_check.setObjectName('checkBox')
    la.addWidget(QtGui.QLabel('Group drawings in page'))
    onedrawing_check.setChecked(True)
    la.addWidget(onedrawing_check)

    sewed_check = QtGui.QCheckBox(DialogBox)
    sewed_check.setObjectName('checkBox')
    la.addWidget(QtGui.QLabel('Sewed surfaces'))
    sewed_check.setChecked(True)
    sewed_check.setEnabled(False)
    la.addWidget(sewed_check)

    box = QtGui.QDialogButtonBox(DialogBox)

    box = QtGui.QDialogButtonBox(DialogBox)
    box.setOrientation(QtCore.Qt.Horizontal)
    box.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
    la.addWidget(box)

    QtCore.QObject.connect(box, QtCore.SIGNAL('accepted()'), proceed)
    QtCore.QObject.connect(box, QtCore.SIGNAL('rejected()'), close)
    QtCore.QMetaObject.connectSlotsByName(DialogBox)
    DialogBox.show()



---
⏵ [documentation index](../README.md) > Macro Unfold Box/pl
