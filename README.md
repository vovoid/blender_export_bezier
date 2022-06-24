# Blender Export Bezier

Tested with Blender: 2.80

To install, create and put the .py files in the directory:

    blender-2.80-windows64/2.80/scripts/addons/io_scene_vovoid_bezier

You can also check out the git repository in that directory.

File produced looks like:

```
{
  "name": "BezierCurve",
  "points": [
    {
      "handle_left": [-1.50000, -0.50000, 0.00000],
      "vertex": [-1.00000, 0.00000, 0.00000],
      "handle_right": [-0.50000, 0.50000, 0.00000],
      "tilt": 0.00000
    },
    {
      "handle_left": [0.00000, 0.00000, 0.00000],
      "vertex": [1.00000, 0.00000, 0.00000],
      "handle_right": [2.00000, 0.00000, 0.00000],
      "tilt": 0.00000
    },
  ]
}
```