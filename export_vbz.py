# <pep8 compliant>

import os
import bpy


def save(context, filepath):
    ob = context.active_object
    if ob.type != 'CURVE':
        return {'FINISHED'}

    file = open(filepath, "w")
    file.write('{\n')
    for spline in ob.data.splines:
        if len(spline.bezier_points) > 0:
            file.write("  \"name\": \"%s\",\n" % ob.name)
            file.write("  \"points\": [\n")
            is_first = 1
            for bezier_point in spline.bezier_points.values():
                handle_left = ob.matrix_world @ bezier_point.handle_left
                co = ob.matrix_world @ bezier_point.co
                handle_right = ob.matrix_world @ bezier_point.handle_right

                if is_first != 1:
                    file.write(",\n")

                file.write("    {\n")
                file.write("      \"handle_left\": [%.5f, %.5f, %.5f],\n" % (-handle_left.x, handle_left.z, handle_left.y))
                file.write("      \"vertex\": [%.5f, %.5f, %.5f],\n" % (-co.x, co.z, co.y))
                file.write("      \"handle_right\": [%.5f, %.5f, %.5f],\n" % (-handle_right.x, handle_right.z, handle_right.y))
                file.write("      \"tilt\": %.5f\n" % (bezier_point.tilt))
                file.write("    }")
                is_first = 0

    file.write("\n")
    file.write("  ]\n")
    file.write("}\n")
    file.close()

    return {'FINISHED'}
