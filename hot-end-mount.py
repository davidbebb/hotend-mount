
cutter     = '1/8_endmill'
material   = 'delrin'
thickness  = 6

cutter_rad=milling.tools[cutter]['diameter']/2
corner_rad = 3
width = 40
height = 25

plane = camcam.add_plane(Plane('plane', cutter=cutter))

plane.add_layer(
    'mount-1',
    material = material,
    thickness = thickness,
    z0 = 0)

plane.add_layer(
    'mount-2',
    material = material,
    thickness = thickness,
    z0 = 0)

x = width/2
y = height/4
crush=0.1
pos = V(0,0)
bolt_offset = 10
main_bolt_offset = 30.7/2
hotend_rad=6.1
step_rad=8
step_depth=-.75
x_offset=hotend_rad+(cutter_rad+0.7)

border = Path(closed=True, side='out')
border.add_point(PIncurve(pos + V(-x, -y), radius=corner_rad, direction = 'CW'))
border.add_point(PIncurve(pos + V(-x,  y), radius=corner_rad, direction = 'CW'))

border.add_point(PIncurve(pos + V( -x_offset,  y), direction = 'CW'))
border.add_point(POutcurve(pos + V(0,y+0.1), radius=hotend_rad, direction = 'CW'))
border.add_point(PIncurve(pos + V(  x_offset,  y), direction = 'CW'))

border.add_point(PIncurve(pos + V( x,  y), radius=corner_rad, direction = 'CW'))
border.add_point(PIncurve(pos + V( x, -y), radius=corner_rad, direction = 'CW'))

offset = 8
step = Path(closed=False, side='out', z1=step_depth)
step.add_point(PIncurve(pos + V( -offset,  y), direction = 'CW'))
step.add_point(POutcurve(pos + V(0,5.95) , radius=step_rad, direction = 'CW'))
step.add_point(PIncurve(pos + V(  offset,  y), radius=-1.5,direction = 'CW'))# border = Path(closed=True, side='out')
# border.add_point(PIncurve(pos + V( x,  y), radius=0, direction = 'CW'))
# border.add_point(PIncurve(pos + V( x, -y), radius=0, direction = 'CW'))
#
# border.add_point(PAroundcurve(pos + V(0, -y), centre=pos+V(main_bolt_offset,-(y+crush/2)), radius=0.5, direction = 'CW'))
# border.add_point(PAroundcurve(pos + V(0, -y), centre=pos+V(bolt_offset,-(y+crush/2)), radius=0.5, direction = 'CW'))
#
# border.add_point(PAroundcurve(pos + V(0, -y), centre=pos+V(0,-(y+2)), radius=hotend_rad, direction = 'CW'))
#
# border.add_point(PAroundcurve(pos + V(0, -y), centre=pos+V(-bolt_offset,-(y+crush/2)), radius=0.5, direction = 'CW'))
# border.add_point(PAroundcurve(pos + V(0, -y), centre=pos+V(-main_bolt_offset,-(y+crush/2)), radius=0.5, direction = 'CW'))
#
# border.add_point(PIncurve(pos + V(-x, -y), radius=0, direction = 'CW'))
# border.add_point(PIncurve(pos + V(-x,  y), radius=0, direction = 'CW'))
#
# border.add_point(PAroundcurve(pos + V(0, y), centre=pos+V(-main_bolt_offset,(y+crush/2)), radius=0.5, direction = 'CW'))
# border.add_point(PAroundcurve(pos + V(0, y), centre=pos+V(-bolt_offset,(y+crush/2)), radius=0.5, direction = 'CW'))
# border.add_point(PAroundcurve(pos + V(0, y), centre=pos+V(bolt_offset,(y+crush/2)), radius=0.5, direction = 'CW'))
# border.add_point(PAroundcurve(pos + V(0, y), centre=pos+V(main_bolt_offset,(y+crush/2)), radius=0.5, direction = 'CW'))

mount_1 = plane.add(
    Part(name = 'mount-1',
        border = border,
        layer = 'mount-1',
        cutter = cutter
    )
)

mount_1.add_path(step)
