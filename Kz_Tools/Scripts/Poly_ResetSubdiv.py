# python
# -*- coding: utf-8 -*-

import lx

# Select Subdivs and Catmull-Clark polygons
lx.eval('select.polygon add type subdiv')
lx.eval('select.polygon add type psubdiv')

# Convert polygon type
lx.eval('poly.convert face subpatch true')
lx.eval('select.drop polygon')
