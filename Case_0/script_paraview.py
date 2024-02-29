# trace generated using paraview version 5.11.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML MultiBlock Data Reader'
case_$ivtmseries = XMLMultiBlockDataReader(registrationName='Case_$i.vtm.series', FileName=['/home/miguel/Desktop/OpenFOAM_Proyects/ball_auto/Case_$i/VTK/Case_$i.vtm.series'])
case_$ivtmseries.CellArrayStatus = ['p', 'U']
case_$ivtmseries.PointArrayStatus = ['p', 'U']

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# set active source
SetActiveSource(case_$ivtmseries)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
case_$ivtmseriesDisplay = Show(case_$ivtmseries, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
case_$ivtmseriesDisplay.Representation = 'Surface'
case_$ivtmseriesDisplay.ColorArrayName = [None, '']
case_$ivtmseriesDisplay.SelectTCoordArray = 'None'
case_$ivtmseriesDisplay.SelectNormalArray = 'None'
case_$ivtmseriesDisplay.SelectTangentArray = 'None'
case_$ivtmseriesDisplay.OSPRayScaleArray = 'U'
case_$ivtmseriesDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
case_$ivtmseriesDisplay.SelectOrientationVectors = 'None'
case_$ivtmseriesDisplay.ScaleFactor = 0.8
case_$ivtmseriesDisplay.SelectScaleArray = 'None'
case_$ivtmseriesDisplay.GlyphType = 'Arrow'
case_$ivtmseriesDisplay.GlyphTableIndexArray = 'None'
case_$ivtmseriesDisplay.GaussianRadius = 0.04
case_$ivtmseriesDisplay.SetScaleArray = ['POINTS', 'U']
case_$ivtmseriesDisplay.ScaleTransferFunction = 'PiecewiseFunction'
case_$ivtmseriesDisplay.OpacityArray = ['POINTS', 'U']
case_$ivtmseriesDisplay.OpacityTransferFunction = 'PiecewiseFunction'
case_$ivtmseriesDisplay.DataAxesGrid = 'GridAxesRepresentation'
case_$ivtmseriesDisplay.PolarAxes = 'PolarAxesRepresentation'
case_$ivtmseriesDisplay.SelectInputVectors = ['POINTS', 'U']
case_$ivtmseriesDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
case_$ivtmseriesDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.10999999940395355, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
case_$ivtmseriesDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.10999999940395355, 1.0, 0.5, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# reset view to fit data
renderView1.ResetCamera(False)

# set scalar coloring
ColorBy(case_$ivtmseriesDisplay, ('POINTS', 'U', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
case_$ivtmseriesDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
case_$ivtmseriesDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')

# get 2D transfer function for 'U'
uTF2D = GetTransferFunction2D('U')

# show data in view
case_$ivtmseriesDisplay = Show(case_$ivtmseries, renderView1, 'GeometryRepresentation')

# reset view to fit data
renderView1.ResetCamera(False)

# show color bar/color legend
case_$ivtmseriesDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)

# change scalar bar placement
uLUTColorBar.Orientation = 'Horizontal'
uLUTColorBar.WindowLocation = 'Any Location'
uLUTColorBar.Position = [0.3130817610062891, 0.8707488986784142]
uLUTColorBar.ScalarBarLength = 0.33

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
uLUT.ApplyPreset('Turbo', True)

animationScene1.GoToLast()

# rescale color and/or opacity maps used to exactly fit the current data range
case_$ivtmseriesDisplay.RescaleTransferFunctionToDataRange(False, True)

animationScene1.GoToFirst()

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1920, 1080)

# current camera placement for renderView1
renderView1.CameraPosition = [4.0, 2.5, 15.112872637897196]
renderView1.CameraFocalPoint = [4.0, 2.5, 0.05000000074505806]
renderView1.CameraParallelScale = 4.7172555580628135

# save animation
SaveAnimation('/home/miguel/Desktop/OpenFOAM_Proyects/ball_auto/Case_$i/animation_case_$i.ogv', renderView1, ImageResolution=[1920, 1080],
    FrameRate=100,
    FrameWindow=[0, 1000])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1920, 1080)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [4.0, 2.5, 15.112872637897196]
renderView1.CameraFocalPoint = [4.0, 2.5, 0.05000000074505806]
renderView1.CameraParallelScale = 4.7172555580628135

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
