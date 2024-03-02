# trace generated using paraview version 5.11.2
# import paraview
# paraview.compatibility.major = 5
# paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML MultiBlock Data Reader'
case_1vtmseries = XMLMultiBlockDataReader(
    registrationName="Case_$i.vtm.series",
    FileName=[
        "/home/miguel/Desktop/OpenFOAM_Proyects/ball_auto/Case_$i/VTK/Case_$i.vtm.series"
    ],
)
case_1vtmseries.CellArrayStatus = ["p", "U"]
case_1vtmseries.PointArrayStatus = ["p", "U"]

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate("RenderView")

# show data in view
case_1vtmseriesDisplay = Show(case_1vtmseries, renderView1, "GeometryRepresentation")

# trace defaults for the display properties.
case_1vtmseriesDisplay.Representation = "Surface"
case_1vtmseriesDisplay.ColorArrayName = [None, ""]
case_1vtmseriesDisplay.SelectTCoordArray = "None"
case_1vtmseriesDisplay.SelectNormalArray = "None"
case_1vtmseriesDisplay.SelectTangentArray = "None"
case_1vtmseriesDisplay.OSPRayScaleArray = "U"
case_1vtmseriesDisplay.OSPRayScaleFunction = "PiecewiseFunction"
case_1vtmseriesDisplay.SelectOrientationVectors = "None"
case_1vtmseriesDisplay.ScaleFactor = 0.8
case_1vtmseriesDisplay.SelectScaleArray = "None"
case_1vtmseriesDisplay.GlyphType = "Arrow"
case_1vtmseriesDisplay.GlyphTableIndexArray = "None"
case_1vtmseriesDisplay.GaussianRadius = 0.04
case_1vtmseriesDisplay.SetScaleArray = ["POINTS", "U"]
case_1vtmseriesDisplay.ScaleTransferFunction = "PiecewiseFunction"
case_1vtmseriesDisplay.OpacityArray = ["POINTS", "U"]
case_1vtmseriesDisplay.OpacityTransferFunction = "PiecewiseFunction"
case_1vtmseriesDisplay.DataAxesGrid = "GridAxesRepresentation"
case_1vtmseriesDisplay.PolarAxes = "PolarAxesRepresentation"
case_1vtmseriesDisplay.SelectInputVectors = ["POINTS", "U"]
case_1vtmseriesDisplay.WriteLog = ""

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
case_1vtmseriesDisplay.ScaleTransferFunction.Points = [
    0.0,
    0.0,
    0.5,
    0.0,
    0.0020000000949949026,
    1.0,
    0.5,
    0.0,
]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
case_1vtmseriesDisplay.OpacityTransferFunction.Points = [
    0.0,
    0.0,
    0.5,
    0.0,
    0.0020000000949949026,
    1.0,
    0.5,
    0.0,
]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(case_1vtmseriesDisplay, ("FIELD", "vtkBlockColors"))

# show color bar/color legend
case_1vtmseriesDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction("vtkBlockColors")

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction("vtkBlockColors")

# get 2D transfer function for 'vtkBlockColors'
vtkBlockColorsTF2D = GetTransferFunction2D("vtkBlockColors")

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName="PlotOverLine1", Input=case_1vtmseries)
plotOverLine1.Point2 = [8.0, 5.0, 0.10000000149011612]

# Properties modified on plotOverLine1
plotOverLine1.Point1 = [0.0, 0.25, 0.05]
plotOverLine1.Point2 = [1.5, 0.25, 0.05]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, "GeometryRepresentation")

# trace defaults for the display properties.
plotOverLine1Display.Representation = "Surface"
plotOverLine1Display.ColorArrayName = [None, ""]
plotOverLine1Display.SelectTCoordArray = "None"
plotOverLine1Display.SelectNormalArray = "None"
plotOverLine1Display.SelectTangentArray = "None"
plotOverLine1Display.OSPRayScaleArray = "U"
plotOverLine1Display.OSPRayScaleFunction = "PiecewiseFunction"
plotOverLine1Display.SelectOrientationVectors = "None"
plotOverLine1Display.ScaleFactor = 0.8
plotOverLine1Display.SelectScaleArray = "None"
plotOverLine1Display.GlyphType = "Arrow"
plotOverLine1Display.GlyphTableIndexArray = "None"
plotOverLine1Display.GaussianRadius = 0.04
plotOverLine1Display.SetScaleArray = ["POINTS", "U"]
plotOverLine1Display.ScaleTransferFunction = "PiecewiseFunction"
plotOverLine1Display.OpacityArray = ["POINTS", "U"]
plotOverLine1Display.OpacityTransferFunction = "PiecewiseFunction"
plotOverLine1Display.DataAxesGrid = "GridAxesRepresentation"
plotOverLine1Display.PolarAxes = "PolarAxesRepresentation"
plotOverLine1Display.SelectInputVectors = ["POINTS", "U"]
plotOverLine1Display.WriteLog = ""

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [
    0.0,
    0.0,
    0.5,
    0.0,
    0.0020000000949949026,
    1.0,
    0.5,
    0.0,
]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [
    0.0,
    0.0,
    0.5,
    0.0,
    0.0020000000949949026,
    1.0,
    0.5,
    0.0,
]

# Create a new 'Line Chart View'
lineChartView1 = CreateView("XYChartView")

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, "XYChartRepresentation")

# trace defaults for the display properties.
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = "arc_length"
plotOverLine1Display_1.SeriesVisibility = ["p", "U_Magnitude"]
plotOverLine1Display_1.SeriesLabel = [
    "arc_length",
    "arc_length",
    "p",
    "p",
    "U_X",
    "U_X",
    "U_Y",
    "U_Y",
    "U_Z",
    "U_Z",
    "U_Magnitude",
    "U_Magnitude",
    "vtkValidPointMask",
    "vtkValidPointMask",
    "Points_X",
    "Points_X",
    "Points_Y",
    "Points_Y",
    "Points_Z",
    "Points_Z",
    "Points_Magnitude",
    "Points_Magnitude",
]
plotOverLine1Display_1.SeriesColor = [
    "arc_length",
    "0",
    "0",
    "0",
    "p",
    "0.8899977111467154",
    "0.10000762951094835",
    "0.1100022888532845",
    "U_X",
    "0.220004577706569",
    "0.4899977111467155",
    "0.7199969481956207",
    "U_Y",
    "0.30000762951094834",
    "0.6899977111467155",
    "0.2899977111467155",
    "U_Z",
    "0.6",
    "0.3100022888532845",
    "0.6399938963912413",
    "U_Magnitude",
    "1",
    "0.5000076295109483",
    "0",
    "vtkValidPointMask",
    "0.6500038147554742",
    "0.3400015259021897",
    "0.16000610360875867",
    "Points_X",
    "0",
    "0",
    "0",
    "Points_Y",
    "0.8899977111467154",
    "0.10000762951094835",
    "0.1100022888532845",
    "Points_Z",
    "0.220004577706569",
    "0.4899977111467155",
    "0.7199969481956207",
    "Points_Magnitude",
    "0.30000762951094834",
    "0.6899977111467155",
    "0.2899977111467155",
]
plotOverLine1Display_1.SeriesOpacity = [
    "arc_length",
    "1.0",
    "p",
    "1.0",
    "U_X",
    "1.0",
    "U_Y",
    "1.0",
    "U_Z",
    "1.0",
    "U_Magnitude",
    "1.0",
    "vtkValidPointMask",
    "1.0",
    "Points_X",
    "1.0",
    "Points_Y",
    "1.0",
    "Points_Z",
    "1.0",
    "Points_Magnitude",
    "1.0",
]
plotOverLine1Display_1.SeriesPlotCorner = [
    "arc_length",
    "0",
    "p",
    "0",
    "U_X",
    "0",
    "U_Y",
    "0",
    "U_Z",
    "0",
    "U_Magnitude",
    "0",
    "vtkValidPointMask",
    "0",
    "Points_X",
    "0",
    "Points_Y",
    "0",
    "Points_Z",
    "0",
    "Points_Magnitude",
    "0",
]
plotOverLine1Display_1.SeriesLabelPrefix = ""
plotOverLine1Display_1.SeriesLineStyle = [
    "arc_length",
    "1",
    "p",
    "1",
    "U_X",
    "1",
    "U_Y",
    "1",
    "U_Z",
    "1",
    "U_Magnitude",
    "1",
    "vtkValidPointMask",
    "1",
    "Points_X",
    "1",
    "Points_Y",
    "1",
    "Points_Z",
    "1",
    "Points_Magnitude",
    "1",
]
plotOverLine1Display_1.SeriesLineThickness = [
    "arc_length",
    "2",
    "p",
    "2",
    "U_X",
    "2",
    "U_Y",
    "2",
    "U_Z",
    "2",
    "U_Magnitude",
    "2",
    "vtkValidPointMask",
    "2",
    "Points_X",
    "2",
    "Points_Y",
    "2",
    "Points_Z",
    "2",
    "Points_Magnitude",
    "2",
]
plotOverLine1Display_1.SeriesMarkerStyle = [
    "arc_length",
    "0",
    "p",
    "0",
    "U_X",
    "0",
    "U_Y",
    "0",
    "U_Z",
    "0",
    "U_Magnitude",
    "0",
    "vtkValidPointMask",
    "0",
    "Points_X",
    "0",
    "Points_Y",
    "0",
    "Points_Z",
    "0",
    "Points_Magnitude",
    "0",
]
plotOverLine1Display_1.SeriesMarkerSize = [
    "arc_length",
    "4",
    "p",
    "4",
    "U_X",
    "4",
    "U_Y",
    "4",
    "U_Z",
    "4",
    "U_Magnitude",
    "4",
    "vtkValidPointMask",
    "4",
    "Points_X",
    "4",
    "Points_Y",
    "4",
    "Points_Z",
    "4",
    "Points_Magnitude",
    "4",
]

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesOpacity = [
    "arc_length",
    "1",
    "p",
    "1",
    "U_X",
    "1",
    "U_Y",
    "1",
    "U_Z",
    "1",
    "U_Magnitude",
    "1",
    "vtkValidPointMask",
    "1",
    "Points_X",
    "1",
    "Points_Y",
    "1",
    "Points_Z",
    "1",
    "Points_Magnitude",
    "1",
]
plotOverLine1Display_1.SeriesPlotCorner = [
    "Points_Magnitude",
    "0",
    "Points_X",
    "0",
    "Points_Y",
    "0",
    "Points_Z",
    "0",
    "U_Magnitude",
    "0",
    "U_X",
    "0",
    "U_Y",
    "0",
    "U_Z",
    "0",
    "arc_length",
    "0",
    "p",
    "0",
    "vtkValidPointMask",
    "0",
]
plotOverLine1Display_1.SeriesLineStyle = [
    "Points_Magnitude",
    "1",
    "Points_X",
    "1",
    "Points_Y",
    "1",
    "Points_Z",
    "1",
    "U_Magnitude",
    "1",
    "U_X",
    "1",
    "U_Y",
    "1",
    "U_Z",
    "1",
    "arc_length",
    "1",
    "p",
    "1",
    "vtkValidPointMask",
    "1",
]
plotOverLine1Display_1.SeriesLineThickness = [
    "Points_Magnitude",
    "2",
    "Points_X",
    "2",
    "Points_Y",
    "2",
    "Points_Z",
    "2",
    "U_Magnitude",
    "2",
    "U_X",
    "2",
    "U_Y",
    "2",
    "U_Z",
    "2",
    "arc_length",
    "2",
    "p",
    "2",
    "vtkValidPointMask",
    "2",
]
plotOverLine1Display_1.SeriesMarkerStyle = [
    "Points_Magnitude",
    "0",
    "Points_X",
    "0",
    "Points_Y",
    "0",
    "Points_Z",
    "0",
    "U_Magnitude",
    "0",
    "U_X",
    "0",
    "U_Y",
    "0",
    "U_Z",
    "0",
    "arc_length",
    "0",
    "p",
    "0",
    "vtkValidPointMask",
    "0",
]
plotOverLine1Display_1.SeriesMarkerSize = [
    "Points_Magnitude",
    "4",
    "Points_X",
    "4",
    "Points_Y",
    "4",
    "Points_Z",
    "4",
    "U_Magnitude",
    "4",
    "U_X",
    "4",
    "U_Y",
    "4",
    "U_Z",
    "4",
    "arc_length",
    "4",
    "p",
    "4",
    "vtkValidPointMask",
    "4",
]

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ["U_Magnitude"]

# set active view
SetActiveView(renderView1)

# destroy renderView1
Delete(renderView1)
del renderView1

# close an empty frame
layout1.Collapse(1)

# set active view
SetActiveView(lineChartView1)

# layout/tab size in pixels
layout1.SetSize(1612, 808)

# save animation
SaveAnimation(
    "/home/miguel/Desktop/OpenFOAM_Proyects/ball_auto/Case_$i/animation_PlotU1_case_$i.ogv",
    lineChartView1,
    ImageResolution=[1920, 1080],
    FrameRate=100,
    FrameWindow=[0, 1000],
)

# ================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
# ================================================================

# --------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1612, 808)

# --------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
