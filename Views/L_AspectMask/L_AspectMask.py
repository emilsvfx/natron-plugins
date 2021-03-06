# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named L_AspectMaskExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from L_AspectMaskExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.L_AspectMask"

def getLabel():
    return "L_AspectMask"

def getVersion():
    return 1

def getIconPath():
    return "L_AspectMask.png"

def getGrouping():
    return "Community/Views"

def getPluginDescription():
    return "Apply standard formats overlay over an image."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("L_AspectMask", "L_AspectMask")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.L_AspectMask = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createSeparatorParam("line06", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line06 = param
    del param

    param = lastNode.createDoubleParam("Aspect", "Aspect")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(3, 0)
    param.setDefaultValue(2.35, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Aspect = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createColorParam("CropColorcolor", "Color", True)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(1, 1)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(1, 2)
    param.setDisplayMinimum(0, 3)
    param.setDisplayMaximum(1, 3)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CropColorcolor = param
    del param

    param = lastNode.createStringParam("sep21", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep21 = param
    del param

    param = lastNode.createStringParam("sep22", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep22 = param
    del param

    param = lastNode.createDoubleParam("Merge1mix", "Mix")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(0.9, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Merge1mix = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createSeparatorParam("Name", "L_AspectMask")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.Name = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createStringParam("sep10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    param = lastNode.createSeparatorParam("line03", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line03 = param
    del param

    param = lastNode.createStringParam("sep11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep11 = param
    del param

    param = lastNode.createStringParam("sep12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep12 = param
    del param

    param = lastNode.createSeparatorParam("CR_FR", "Version NATRON des Gizmos Nuke développés par Luma Pictures")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CR_FR = param
    del param

    param = lastNode.createStringParam("sep17", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep17 = param
    del param

    param = lastNode.createStringParam("sep18", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep18 = param
    del param

    param = lastNode.createSeparatorParam("CR_ENG", "NATRON version of Nuke Gizmos developed by Luma Pictures")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CR_ENG = param
    del param

    param = lastNode.createStringParam("sep19", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep19 = param
    del param

    param = lastNode.createStringParam("sep20", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep20 = param
    del param

    param = lastNode.createSeparatorParam("FF", "(Fabrice Fernandez - 2017)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FF = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "rgba"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("rgba")
    lastNode.setLabel("rgba")
    lastNode.setPosition(802, 7)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    grouprgba = lastNode

    del lastNode
    # End of node "rgba"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(802, 617)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "getIsize"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("getIsize")
    lastNode.setLabel("getIsize")
    lastNode.setPosition(1115, 135)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupgetIsize = lastNode

    del lastNode
    # End of node "getIsize"

    # Start of node "Shuffle1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle1")
    lastNode.setLabel("Shuffle1")
    lastNode.setPosition(1245, 135)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1 = lastNode

    param = lastNode.getParam("outputR")
    if param is not None:
        param.set("0")
        del param

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("0")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("0")
        del param

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("1")
        del param

    del lastNode
    # End of node "Shuffle1"

    # Start of node "Invert1"
    lastNode = app.createNode("net.sf.openfx.Invert", 2, group)
    lastNode.setScriptName("Invert1")
    lastNode.setLabel("Invert1")
    lastNode.setPosition(1245, 405)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.48, 0.66, 1)
    groupInvert1 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Invert1"

    # Start of node "Crop1_2"
    lastNode = app.createNode("net.sf.openfx.CropPlugin", 1, group)
    lastNode.setScriptName("Crop1_2")
    lastNode.setLabel("Crop1_2")
    lastNode.setPosition(1245, 304)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupCrop1_2 = lastNode

    param = lastNode.getParam("rectangleInteractEnable")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(1950, 0)
        param.setValue(1200, 1)
        del param

    param = lastNode.getParam("reformat")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Crop1_2"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(802, 397)
    lastNode.setSize(80, 73)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("b")
        del param

    param = lastNode.getParam("BChannelsA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("mix")
    if param is not None:
        param.setValue(0.9, 0)
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(835, 156)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "CropColor"
    lastNode = app.createNode("net.sf.openfx.ConstantPlugin", 1, group)
    lastNode.setScriptName("CropColor")
    lastNode.setLabel("CropColor")
    lastNode.setPosition(1096, 267)
    lastNode.setSize(104, 78)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupCropColor = lastNode

    param = lastNode.getParam("extent")
    if param is not None:
        param.set("size")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(1950, 0)
        param.setValue(1200, 1)
        del param

    param = lastNode.getParam("hideInputs")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "CropColor"

    # Start of node "Shuffle2"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle2")
    lastNode.setLabel("Shuffle2")
    lastNode.setPosition(1108, 405)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle2 = lastNode

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.A")
        del param

    del lastNode
    # End of node "Shuffle2"

    # Start of node "Premult1"
    lastNode = app.createNode("net.sf.openfx.Premult", 2, group)
    lastNode.setScriptName("Premult1")
    lastNode.setLabel("Premult1")
    lastNode.setPosition(978, 405)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupPremult1 = lastNode

    del lastNode
    # End of node "Premult1"

    # Start of node "Transform1"
    lastNode = app.createNode("net.sf.openfx.TransformPlugin", 1, group)
    lastNode.setScriptName("Transform1")
    lastNode.setLabel("Transform1")
    lastNode.setPosition(1245, 226)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupTransform1 = lastNode

    param = lastNode.getParam("scale")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(0.6914893617021276, 1)
        del param

    param = lastNode.getParam("center")
    if param is not None:
        param.setValue(975, 0)
        param.setValue(600, 1)
        del param

    param = lastNode.getParam("transformCenterChanged")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("filter")
    if param is not None:
        param.set("mitchell")
        del param

    del lastNode
    # End of node "Transform1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupMerge1)
    groupgetIsize.connectInput(0, groupDot1)
    groupShuffle1.connectInput(1, groupgetIsize)
    groupInvert1.connectInput(0, groupCrop1_2)
    groupCrop1_2.connectInput(0, groupTransform1)
    groupMerge1.connectInput(0, groupDot1)
    groupMerge1.connectInput(1, groupPremult1)
    groupDot1.connectInput(0, grouprgba)
    groupShuffle2.connectInput(0, groupInvert1)
    groupShuffle2.connectInput(1, groupCropColor)
    groupPremult1.connectInput(0, groupShuffle2)
    groupTransform1.connectInput(0, groupShuffle1)

    param = groupCrop1_2.getParam("size")
    param.setExpression("rod = Shuffle1.getRegionOfDefinition(frame,view)\nret = rod.width()", True, 0)
    param.setExpression("rod = Shuffle1.getRegionOfDefinition(frame,view)\nret = rod.height()", True, 1)
    del param
    param = groupMerge1.getParam("mix")
    group.getParam("Merge1mix").setAsAlias(param)
    del param
    param = groupCropColor.getParam("size")
    param.setExpression("rod = Shuffle1.getRegionOfDefinition(frame,view)\nret = rod.width()", True, 0)
    param.setExpression("rod = Shuffle1.getRegionOfDefinition(frame,view)\nret = rod.height()", True, 1)
    del param
    param = groupCropColor.getParam("color")
    group.getParam("CropColorcolor").setAsAlias(param)
    del param
    param = groupTransform1.getParam("scale")
    param.setExpression("ret = 1", False, 0)
    param.setExpression("Isize = Shuffle1.getRegionOfDefinition(frame,view)\nAspRat = Isize.width()/Isize.height()\nMyAspect = thisGroup.Aspect.get()\nret = AspRat/MyAspect", True, 1)
    del param
    param = groupTransform1.getParam("center")
    param.setExpression("rod = Shuffle1.getRegionOfDefinition(frame,view)\nret = rod.width()/2", True, 0)
    param.setExpression("rod = Shuffle1.getRegionOfDefinition(frame,view)\nret = rod.height()/2", True, 1)
    del param

    try:
        extModule = sys.modules["L_AspectMaskExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
