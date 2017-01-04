# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named DUCK_Denoise_v2Ext.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from DUCK_Denoise_v2Ext import *
except ImportError:
    pass

def getPluginID():
    return "DUCK_Denoise_v2"

def getLabel():
    return "DUCK_Denoise_v2"

def getVersion():
    return 2

def getIconPath():
    return "DUCK_Denoise_v2.png"

def getGrouping():
    return "Filter/Duck"

def getPluginDescription():
    return "It hepls to denoise a footage, since it is  not based on analisys: it just provides a  denoise for blak/white and coloured dots. It doesn�t make a recostruction of the denoised pixels but it helps to fix visually the problem."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("separator1", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator1 = param
    del param

    param = lastNode.createStringParam("separator2", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator2 = param
    del param

    param = lastNode.createSeparatorParam("Alpha_edge_manager", "DUCK_Denoise_v2")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("\n")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.Alpha_edge_manager = param
    del param

    param = lastNode.createStringParam("separator3", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator3 = param
    del param

    param = lastNode.createStringParam("separator4", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator4 = param
    del param

    param = lastNode.createSeparatorParam("line1", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line1 = param
    del param

    param = lastNode.createStringParam("separator5", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator5 = param
    del param

    param = lastNode.createStringParam("separator6", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator6 = param
    del param

    param = lastNode.createSeparatorParam("black_noise_removal", "black noise removal")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.black_noise_removal = param
    del param

    param = lastNode.createStringParam("separator7", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator7 = param
    del param

    param = lastNode.createStringParam("separator8", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator8 = param
    del param

    param = lastNode.createDouble2DParam("Blur_w_d_msize", "Size")
    param.setMinimum(0, 0)
    param.setMaximum(1000, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setMinimum(0, 1)
    param.setMaximum(1000, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(100, 1)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Blur_w_d_msize = param
    del param

    param = lastNode.createStringParam("separator9", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator9 = param
    del param

    param = lastNode.createStringParam("separator10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator10 = param
    del param

    param = lastNode.createSeparatorParam("white_noise_removal", "white noise removal")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.white_noise_removal = param
    del param

    param = lastNode.createStringParam("separator11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator11 = param
    del param

    param = lastNode.createStringParam("separator12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator12 = param
    del param

    param = lastNode.createDouble2DParam("Blur_d_remsize", "Size")
    param.setMinimum(0, 0)
    param.setMaximum(1000, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setMinimum(0, 1)
    param.setMaximum(1000, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(100, 1)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Blur_d_remsize = param
    del param

    param = lastNode.createStringParam("separator13", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator13 = param
    del param

    param = lastNode.createStringParam("separator14", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator14 = param
    del param

    param = lastNode.createSeparatorParam("colored_noise_removal", "colored noise removal")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.colored_noise_removal = param
    del param

    param = lastNode.createStringParam("separator15", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator15 = param
    del param

    param = lastNode.createStringParam("separator16", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator16 = param
    del param

    param = lastNode.createDouble2DParam("Blur_c_n_rem1size", "Size")
    param.setMinimum(0, 0)
    param.setMaximum(1000, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setMinimum(0, 1)
    param.setMaximum(1000, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(100, 1)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Blur_c_n_rem1size = param
    del param

    param = lastNode.createDouble2DParam("Blur_color_nrsize", "Size")
    param.setMinimum(0, 0)
    param.setMaximum(1000, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setMinimum(0, 1)
    param.setMaximum(1000, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(100, 1)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Blur_color_nrsize = param
    del param

    param = lastNode.createStringParam("separator17", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator17 = param
    del param

    param = lastNode.createStringParam("separator18", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator18 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("separator35", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator35 = param
    del param

    param = lastNode.createStringParam("separator36", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator36 = param
    del param

    param = lastNode.createSeparatorParam("title", "DUCK Denoise v2")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.title = param
    del param

    param = lastNode.createStringParam("separator37", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator37 = param
    del param

    param = lastNode.createStringParam("separator38", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator38 = param
    del param

    param = lastNode.createSeparatorParam("line2", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line2 = param
    del param

    param = lastNode.createStringParam("separator39", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator39 = param
    del param

    param = lastNode.createStringParam("separator40", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator40 = param
    del param

    param = lastNode.createSeparatorParam("FR", "Version NATRON des Gizmos Nuke d�velopp�s par Niccolo Barbero")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("separator41", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator41 = param
    del param

    param = lastNode.createStringParam("separator42", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator42 = param
    del param

    param = lastNode.createSeparatorParam("ENG", "NATRON version of Nuke Gizmos developed by Niccolo Barbero ")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.ENG = param
    del param

    param = lastNode.createStringParam("separator43", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator43 = param
    del param

    param = lastNode.createStringParam("separator44", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator44 = param
    del param

    param = lastNode.createSeparatorParam("mail", "https://www.linkedin.com/in/niccolobarbero")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.mail = param
    del param

    param = lastNode.createStringParam("separator47", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator47 = param
    del param

    param = lastNode.createStringParam("separator48", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator48 = param
    del param

    param = lastNode.createSeparatorParam("conversion", " (Fabrice Fernandez - 2016)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.conversion = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "RGBToYCbCr7091"
    lastNode = app.createNode("net.sf.openfx.RGBToYCbCr709", 1, group)
    lastNode.setScriptName("RGBToYCbCr7091")
    lastNode.setLabel("RGBToYCbCr7091")
    lastNode.setPosition(1995, 337)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupRGBToYCbCr7091 = lastNode

    del lastNode
    # End of node "RGBToYCbCr7091"

    # Start of node "Shuffle_Y"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle_Y")
    lastNode.setLabel("Shuffle_Y")
    lastNode.setPosition(1536, 568)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle_Y = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("0")
        del param

    del lastNode
    # End of node "Shuffle_Y"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(1581, 351)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Blur_w_d_m"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur_w_d_m")
    lastNode.setLabel("Blur_w_d_m")
    lastNode.setPosition(1717, 568)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur_w_d_m = lastNode

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    del lastNode
    # End of node "Blur_w_d_m"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(1536, 673)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("max")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("max")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("B")
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "Dot2_2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2_2")
    lastNode.setLabel("Dot2_2")
    lastNode.setPosition(1762, 697)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2_2 = lastNode

    del lastNode
    # End of node "Dot2_2"

    # Start of node "Blur_d_rem"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur_d_rem")
    lastNode.setLabel("Blur_d_rem")
    lastNode.setPosition(1726, 871)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur_d_rem = lastNode

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    del lastNode
    # End of node "Blur_d_rem"

    # Start of node "Dot3"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot3")
    lastNode.setLabel("Dot3")
    lastNode.setPosition(1581, 885)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot3 = lastNode

    del lastNode
    # End of node "Dot3"

    # Start of node "Merge2"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge2")
    lastNode.setLabel("Merge2")
    lastNode.setPosition(1540, 975)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge2 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("min")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("min")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("B")
        del param

    del lastNode
    # End of node "Merge2"

    # Start of node "Dot4"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot4")
    lastNode.setLabel("Dot4")
    lastNode.setPosition(1771, 1001)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot4 = lastNode

    del lastNode
    # End of node "Dot4"

    # Start of node "Shuffle2"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle2")
    lastNode.setLabel("Shuffle2")
    lastNode.setPosition(1540, 1175)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle2 = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("0")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("0")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("0")
        del param

    del lastNode
    # End of node "Shuffle2"

    # Start of node "Shuffle_Cb"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle_Cb")
    lastNode.setLabel("Shuffle_Cb")
    lastNode.setPosition(1983, 563)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle_Cb = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.g")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.g")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("A.g")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("0")
        del param

    del lastNode
    # End of node "Shuffle_Cb"

    # Start of node "Blur_color_nr"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur_color_nr")
    lastNode.setLabel("Blur_color_nr")
    lastNode.setPosition(1983, 676)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur_color_nr = lastNode

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    del lastNode
    # End of node "Blur_color_nr"

    # Start of node "Shuffle1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle1")
    lastNode.setLabel("Shuffle1")
    lastNode.setPosition(1983, 778)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1 = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("0")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.g")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("0")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("0")
        del param

    del lastNode
    # End of node "Shuffle1"

    # Start of node "Merge3"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge3")
    lastNode.setLabel("Merge3")
    lastNode.setPosition(1546, 1563)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge3 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("plus")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("plus")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("B")
        del param

    del lastNode
    # End of node "Merge3"

    # Start of node "Dot5"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot5")
    lastNode.setLabel("Dot5")
    lastNode.setPosition(2034, 1589)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot5 = lastNode

    del lastNode
    # End of node "Dot5"

    # Start of node "Shuffle_Cr"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle_Cr")
    lastNode.setLabel("Shuffle_Cr")
    lastNode.setPosition(2312, 567)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle_Cr = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.g")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("A.b")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("A.a")
        del param

    del lastNode
    # End of node "Shuffle_Cr"

    # Start of node "Dot6"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot6")
    lastNode.setLabel("Dot6")
    lastNode.setPosition(2357, 351)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot6 = lastNode

    del lastNode
    # End of node "Dot6"

    # Start of node "Blur_c_n_rem1"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur_c_n_rem1")
    lastNode.setLabel("Blur_c_n_rem1")
    lastNode.setPosition(2312, 670)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur_c_n_rem1 = lastNode

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    del lastNode
    # End of node "Blur_c_n_rem1"

    # Start of node "Shuffle3"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle3")
    lastNode.setLabel("Shuffle3")
    lastNode.setPosition(2312, 769)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle3 = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("0")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("0")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("A.b")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("0")
        del param

    del lastNode
    # End of node "Shuffle3"

    # Start of node "Merge3_2"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge3_2")
    lastNode.setLabel("Merge3_2")
    lastNode.setPosition(1540, 1692)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge3_2 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("plus")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("plus")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("B")
        del param

    del lastNode
    # End of node "Merge3_2"

    # Start of node "Dot7"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot7")
    lastNode.setLabel("Dot7")
    lastNode.setPosition(2357, 1718)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot7 = lastNode

    del lastNode
    # End of node "Dot7"

    # Start of node "Input1"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input1")
    lastNode.setLabel("Input1")
    lastNode.setPosition(1983, 12)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput1 = lastNode

    del lastNode
    # End of node "Input1"

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(1540, 2104)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "YCbCrToRGB7091"
    lastNode = app.createNode("net.sf.openfx.YCbCrToRGB709", 1, group)
    lastNode.setScriptName("YCbCrToRGB7091")
    lastNode.setLabel("YCbCrToRGB7091")
    lastNode.setPosition(1552, 1916)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupYCbCrToRGB7091 = lastNode

    del lastNode
    # End of node "YCbCrToRGB7091"

    # Now that all nodes are created we can connect them together, restore expressions
    groupRGBToYCbCr7091.connectInput(0, groupInput1)
    groupShuffle_Y.connectInput(1, groupDot1)
    groupDot1.connectInput(0, groupRGBToYCbCr7091)
    groupBlur_w_d_m.connectInput(0, groupShuffle_Y)
    groupMerge1.connectInput(0, groupShuffle_Y)
    groupMerge1.connectInput(1, groupDot2_2)
    groupDot2_2.connectInput(0, groupBlur_w_d_m)
    groupBlur_d_rem.connectInput(0, groupDot3)
    groupDot3.connectInput(0, groupMerge1)
    groupMerge2.connectInput(0, groupDot3)
    groupMerge2.connectInput(1, groupDot4)
    groupDot4.connectInput(0, groupBlur_d_rem)
    groupShuffle2.connectInput(1, groupMerge2)
    groupShuffle_Cb.connectInput(1, groupRGBToYCbCr7091)
    groupBlur_color_nr.connectInput(0, groupShuffle_Cb)
    groupShuffle1.connectInput(1, groupBlur_color_nr)
    groupMerge3.connectInput(0, groupShuffle2)
    groupMerge3.connectInput(1, groupDot5)
    groupDot5.connectInput(0, groupShuffle1)
    groupShuffle_Cr.connectInput(1, groupDot6)
    groupDot6.connectInput(0, groupRGBToYCbCr7091)
    groupBlur_c_n_rem1.connectInput(0, groupShuffle_Cr)
    groupShuffle3.connectInput(1, groupBlur_c_n_rem1)
    groupMerge3_2.connectInput(0, groupMerge3)
    groupMerge3_2.connectInput(1, groupDot7)
    groupDot7.connectInput(0, groupShuffle3)
    groupOutput2.connectInput(0, groupYCbCrToRGB7091)
    groupYCbCrToRGB7091.connectInput(0, groupMerge3_2)

    param = groupBlur_w_d_m.getParam("size")
    group.getParam("Blur_w_d_msize").setAsAlias(param)
    del param
    param = groupBlur_d_rem.getParam("size")
    group.getParam("Blur_d_remsize").setAsAlias(param)
    del param
    param = groupBlur_color_nr.getParam("size")
    group.getParam("Blur_color_nrsize").setAsAlias(param)
    del param
    param = groupBlur_c_n_rem1.getParam("size")
    group.getParam("Blur_c_n_rem1size").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["DUCK_Denoise_v2Ext"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
