# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named BokehDisc_GLExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from BokehDisc_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.BokehDisc_GL"

def getLabel():
    return "BokehDisc_GL"

def getVersion():
    return 1

def getIconPath():
    return "BokehDisc_GL.png"

def getGrouping():
    return "Community/GLSL/Blur"

def getPluginDescription():
    return "Defocus Blur."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("separator01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator01 = param
    del param

    param = lastNode.createStringParam("separator02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator02 = param
    del param

    param = lastNode.createSeparatorParam("BokehDisc_GL", "BokehDisc_GL")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.BokehDisc_GL = param
    del param

    param = lastNode.createStringParam("separator03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator03 = param
    del param

    param = lastNode.createStringParam("separator04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator04 = param
    del param

    param = lastNode.createSeparatorParam("line01", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line01 = param
    del param

    param = lastNode.createStringParam("separator05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator05 = param
    del param

    param = lastNode.createDoubleParam("Blur_Size", "Blur Size")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(200, 0)
    param.setDefaultValue(10, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Blur_Size = param
    del param

    param = lastNode.createStringParam("separator06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator06 = param
    del param

    param = lastNode.createDoubleParam("Samples", "Samples")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1000, 0)
    param.setDefaultValue(150, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Samples = param
    del param

    param = lastNode.createSeparatorParam("line08", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line08 = param
    del param

    param = lastNode.createBooleanParam("Modulate", "Modulate")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Modulate = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("separator19", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator19 = param
    del param

    param = lastNode.createStringParam("separator20", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator20 = param
    del param

    param = lastNode.createSeparatorParam("line02", "BokehDisc_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line02 = param
    del param

    param = lastNode.createStringParam("separator21", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator21 = param
    del param

    param = lastNode.createStringParam("separator22", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator22 = param
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

    param = lastNode.createStringParam("separator23", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator23 = param
    del param

    param = lastNode.createStringParam("separator24", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator24 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("separator25", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator25 = param
    del param

    param = lastNode.createStringParam("separator26", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator26 = param
    del param

    param = lastNode.createSeparatorParam("conversion", " (Fabrice Fernandez - 2017)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.conversion = param
    del param

    param = lastNode.createStringParam("separator27", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator27 = param
    del param

    param = lastNode.createStringParam("separator28", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator28 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 3997)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4139, 3698)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Mask"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Mask")
    lastNode.setLabel("Modulate")
    lastNode.setPosition(4319, 3846)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupMask = lastNode

    del lastNode
    # End of node "Mask"

    # Start of node "Shadertoy2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy2")
    lastNode.setLabel("Shadertoy2")
    lastNode.setPosition(4139, 3845)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy2 = lastNode

    param = lastNode.getParam("imageShaderPreset")
    if param is not None:
        param.set("Blur/Bokeh Disc")
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("// https://www.shadertoy.com/view/4d2Xzw\n// Bokeh disc.\n// original fast version by David Hoskins.\n// License Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.\n\n// Fixed and adapted to Natron by F. Devernay:\n// - avoid numerical divergence (length of vangle growing)\n// - use mipmaps to limit noise when the spacing between samples is too large.\n\n// iChannel0: Source, filter=mipmap, wrap=clamp\n// iChannel1: Modulate (Image containing a factor to be applied to the Blur size in the first channel), filter=linear, wrap=clamp\n// BBox: iChannel0\n\n// The Golden Angle is (3.-sqrt(5.0))*PI radians, which doesn\'t precompiled for some reason.\n// The compiler is a dunce I tells-ya!!\n#define GOLDEN_ANGLE 2.39996\n\nconst vec2 iRenderScale = vec2(1.,1.);).\nconst vec2 iChannelOffset[4] = vec2[4]( vec2(0.,0.), vec2(0.,0.), vec2(0.,0.), vec2(0.,0.) );\nuniform float size = 10.; // Blur Size (Blur size in pixels), min=0., max=200.\nuniform int ITERATIONS = 150; // Samples (Number of samples - higher is better and slower), min=2, max=1024\nuniform bool perpixel_size = false; // Modulate (Modulate the blur size by multiplying it by the first channel of the Modulate input)\n\nmat2 rot = mat2(cos(GOLDEN_ANGLE), sin(GOLDEN_ANGLE), -sin(GOLDEN_ANGLE), cos(GOLDEN_ANGLE));\nfloat sqrtiter = sqrt(float(ITERATIONS));\n\n// The original fast version had the following issue:\n// - the length of the vangle vector changes, although it should remain the same -> renormalize\n// - the radius was sqrt(2) too large => properly compute the base norm\n//-------------------------------------------------------------------------------------------\nvec4 Bokeh(sampler2D tex, vec2 uv, float radius)\n{\n    // the spacing is the square root of the density on average: sqrt(pi*r^2/n)\n    float spacing = sqrt(3.141592652) * radius * iRenderScale.x / sqrtiter;\n    float level = log2(spacing);\n\n    vec4 acc = vec4(0);\n    float r = 1.;\n    vec2 vangle = vec2(0.,1.);\n    float vanglenorm = radius / sqrtiter / sqrt(2);\n    vec2 uvscale = iRenderScale.xy / iResolution.xy;\n    for (int j = 0; j < ITERATIONS; j++) {  \n        // the approx increase in the scale of sqrt(0, 1, 2, 3...)\n        r += 1. / r;\n\t    // r = 1. + sqrt(j) * sqrt(2); // slow version - gives almost the same result\n        vangle = rot * vangle;\n\t    vangle /= length(vangle);\n\t    // vangle = vec2(cos(GOLDEN_ANGLE*j), sin(GOLDEN_ANGLE*j)); // slow version\n        vec4 col = texture2D(tex, uv + (r-1.) * vangle * vanglenorm * uvscale, level).rgba; /// ... Sample the image\n        acc += col;\n    }\n    return acc / ITERATIONS;\n}\n\n#if 0\n// reference implementation\n//-------------------------------------------------------------------------------------------\nvec4 Bokeh2(sampler2D tex, vec2 uv, float radius)\n{\n    // the spacing is the square root of the density on average: sqrt(pi*r^2/n)\n    float spacing = sqrt(3.141592652/ITERATIONS) * radius * iRenderScale.x;\n    float level = log2(spacing);\n\n    vec4 acc = vec4(0);\n\n    // Vogel\'s method, described at http://blog.marmakoide.org/?p=1\n    for (int j = 0; j < ITERATIONS; j++) {  \n        float theta = GOLDEN_ANGLE * j;\n        float r = sqrt(j) / sqrtiter;\n        vec2 p = r * vec2(cos(theta), sin(theta));\n        vec4 col = texture2D(tex, uv + radius * p * iRenderScale.xy / iResolution.xy, level).rgba; /// ... Sample the image\n        acc += col;\n    }\n    return acc / ITERATIONS;\n}\n#endif\n\n//-------------------------------------------------------------------------------------------\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n    vec2 uv = fragCoord.xy / iResolution.xy;\n    \n    float rad = size;\n    if (perpixel_size) {\n        rad *= texture2D(iChannel1, (fragCoord.xy-iChannelOffset[1].xy)/iChannelResolution[1].xy).x;\n    }\n    \n    fragColor = Bokeh(iChannel0, uv, rad);\n}\n")
        del param

    param = lastNode.getParam("wrap0")
    if param is not None:
        param.set("clamp")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source")
        del param

    param = lastNode.getParam("mipmap1")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("wrap1")
    if param is not None:
        param.set("clamp")
        del param

    param = lastNode.getParam("inputLabel1")
    if param is not None:
        param.setValue("Modulate")
        del param

    param = lastNode.getParam("inputHint1")
    if param is not None:
        param.setValue("Image containing a factor to be applied to the Blur size in the first channel")
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("size")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Blur Size")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("Blur size in pixels")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramMinFloat0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat0")
    if param is not None:
        param.setValue(200, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("ITERATIONS")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Samples")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("Number of samples - higher is better and slower")
        del param

    param = lastNode.getParam("paramDefaultInt1")
    if param is not None:
        param.setValue(150, 0)
        del param

    param = lastNode.getParam("paramMinInt1")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("paramMaxInt1")
    if param is not None:
        param.setValue(1024, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("perpixel_size")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Modulate")
        del param

    param = lastNode.getParam("paramHint2")
    if param is not None:
        param.setValue("Modulate the blur size by multiplying it by the first channel of the Modulate input")
        del param

    del lastNode
    # End of node "Shadertoy2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy2)
    groupShadertoy2.connectInput(0, groupSource)
    groupShadertoy2.connectInput(1, groupMask)

    param = groupShadertoy2.getParam("paramValueFloat0")
    param.slaveTo(group.getParam("Blur_Size"), 0, 0)
    del param
    param = groupShadertoy2.getParam("paramValueInt1")
    param.slaveTo(group.getParam("Samples"), 0, 0)
    del param
    param = groupShadertoy2.getParam("paramValueBool2")
    param.slaveTo(group.getParam("Modulate"), 0, 0)
    del param

    try:
        extModule = sys.modules["BokehDisc_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
