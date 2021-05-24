#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on January 29, 2021, at 21:48
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Go-No Go'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mauspad\\Desktop\\OEA_task_test\\go_nogo\\go_no_go.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "hi"
hiClock = core.Clock()
start = keyboard.Keyboard()
press = visual.TextStim(win=win, name='press',
    text='Press enter to continue',
    font='Arial',
    pos=(0, -350), height=25, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructions = visual.ImageStim(
    win=win,
    name='instructions', 
    image='images/Intro1.bmp', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ready_2"
ready_2Clock = core.Clock()
ready = visual.TextStim(win=win, name='ready',
    text='Get Ready!',
    font='Arial',
    pos=(0, 0), height=70, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practice_run"
practice_runClock = core.Clock()
practice_response = keyboard.Keyboard()
practice_text = visual.TextStim(win=win, name='practice_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=70, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "practice_ITI"
practice_ITIClock = core.Clock()
ITIprac = visual.TextStim(win=win, name='ITIprac',
    text='boo',
    font='Arial',
    pos=(0, 0), height=70, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "hi_2"
hi_2Clock = core.Clock()
start_2 = keyboard.Keyboard()
press_2 = visual.TextStim(win=win, name='press_2',
    text='Press enter to begin the test',
    font='Arial',
    pos=(0, -350), height=25, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructions_2 = visual.ImageStim(
    win=win,
    name='instructions_2', 
    image='images/Intro2.bmp', mask=None,
    ori=0, pos=(0, 75), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ready_2"
ready_2Clock = core.Clock()
ready = visual.TextStim(win=win, name='ready',
    text='Get Ready!',
    font='Arial',
    pos=(0, 0), height=70, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "task_run"
task_runClock = core.Clock()
run_response = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=70, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "task_ITI"
task_ITIClock = core.Clock()
runITI = visual.TextStim(win=win, name='runITI',
    text='boo',
    font='Arial',
    pos=(0, 0), height=70, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "hi_3"
hi_3Clock = core.Clock()
start_3 = keyboard.Keyboard()
press_3 = visual.TextStim(win=win, name='press_3',
    text='Press enter to begin the test',
    font='Arial',
    pos=(0, -350), height=25, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructions_3 = visual.ImageStim(
    win=win,
    name='instructions_3', 
    image='images/Intro3.bmp', mask=None,
    ori=0, pos=(0, 75), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ready_2"
ready_2Clock = core.Clock()
ready = visual.TextStim(win=win, name='ready',
    text='Get Ready!',
    font='Arial',
    pos=(0, 0), height=70, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "task_run"
task_runClock = core.Clock()
run_response = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=70, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "task_ITI"
task_ITIClock = core.Clock()
runITI = visual.TextStim(win=win, name='runITI',
    text='boo',
    font='Arial',
    pos=(0, 0), height=70, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "end"
endClock = core.Clock()
bye = visual.TextStim(win=win, name='bye',
    text='You have completed the task :)',
    font='Arial',
    pos=(0, 0), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "hi"-------
# update component parameters for each repeat
start.keys = []
start.rt = []
# keep track of which components have finished
hiComponents = [start, press, instructions]
for thisComponent in hiComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
hiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "hi"-------
while continueRoutine:
    # get current time
    t = hiClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=hiClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start* updates
    waitOnFlip = False
    if start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start.frameNStart = frameN  # exact frame index
        start.tStart = t  # local t and not account for scr refresh
        start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start, 'tStartRefresh')  # time at next scr refresh
        start.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start.status == STARTED and not waitOnFlip:
        theseKeys = start.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *press* updates
    if press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        press.frameNStart = frameN  # exact frame index
        press.tStart = t  # local t and not account for scr refresh
        press.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(press, 'tStartRefresh')  # time at next scr refresh
        press.setAutoDraw(True)
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hiComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hi"-------
for thisComponent in hiComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "hi" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ready_2"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
ready_2Components = [ready]
for thisComponent in ready_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ready_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ready_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ready_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ready_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready* updates
    if ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ready.frameNStart = frameN  # exact frame index
        ready.tStart = t  # local t and not account for scr refresh
        ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready, 'tStartRefresh')  # time at next scr refresh
        ready.setAutoDraw(True)
    if ready.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ready.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            ready.tStop = t  # not accounting for scr refresh
            ready.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ready, 'tStopRefresh')  # time at next scr refresh
            ready.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ready_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready_2"-------
for thisComponent in ready_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
practicetrials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice.xlsx'),
    seed=None, name='practicetrials')
thisExp.addLoop(practicetrials)  # add the loop to the experiment
thisPracticetrial = practicetrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticetrial.rgb)
if thisPracticetrial != None:
    for paramName in thisPracticetrial:
        exec('{} = thisPracticetrial[paramName]'.format(paramName))

for thisPracticetrial in practicetrials:
    currentLoop = practicetrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracticetrial.rgb)
    if thisPracticetrial != None:
        for paramName in thisPracticetrial:
            exec('{} = thisPracticetrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_run"-------
    routineTimer.add(0.250000)
    # update component parameters for each repeat
    practice_response.keys = []
    practice_response.rt = []
    practice_text.setText(stim)
    # keep track of which components have finished
    practice_runComponents = [practice_response, practice_text]
    for thisComponent in practice_runComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_runClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "practice_run"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_runClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_runClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_response* updates
        waitOnFlip = False
        if practice_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_response.frameNStart = frameN  # exact frame index
            practice_response.tStart = t  # local t and not account for scr refresh
            practice_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_response, 'tStartRefresh')  # time at next scr refresh
            practice_response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(practice_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if practice_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_response.tStartRefresh + .25-frameTolerance:
                # keep track of stop time/frame for later
                practice_response.tStop = t  # not accounting for scr refresh
                practice_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practice_response, 'tStopRefresh')  # time at next scr refresh
                practice_response.status = FINISHED
        if practice_response.status == STARTED and not waitOnFlip:
            theseKeys = practice_response.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
        
        # *practice_text* updates
        if practice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_text.frameNStart = frameN  # exact frame index
            practice_text.tStart = t  # local t and not account for scr refresh
            practice_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_text, 'tStartRefresh')  # time at next scr refresh
            practice_text.setAutoDraw(True)
        if practice_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_text.tStartRefresh + .25-frameTolerance:
                # keep track of stop time/frame for later
                practice_text.tStop = t  # not accounting for scr refresh
                practice_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practice_text, 'tStopRefresh')  # time at next scr refresh
                practice_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_runComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_run"-------
    for thisComponent in practice_runComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "practice_ITI"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    practice_ITIComponents = [ITIprac]
    for thisComponent in practice_ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "practice_ITI"-------
    while continueRoutine:
        # get current time
        t = practice_ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ITIprac* updates
        if ITIprac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITIprac.frameNStart = frameN  # exact frame index
            ITIprac.tStart = t  # local t and not account for scr refresh
            ITIprac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITIprac, 'tStartRefresh')  # time at next scr refresh
            ITIprac.setAutoDraw(True)
        if ITIprac.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITIprac.tStartRefresh + ITI-frameTolerance:
                # keep track of stop time/frame for later
                ITIprac.tStop = t  # not accounting for scr refresh
                ITIprac.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ITIprac, 'tStopRefresh')  # time at next scr refresh
                ITIprac.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_ITI"-------
    for thisComponent in practice_ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practice_ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practicetrials'


# ------Prepare to start Routine "hi_2"-------
# update component parameters for each repeat
start_2.keys = []
start_2.rt = []
# keep track of which components have finished
hi_2Components = [start_2, press_2, instructions_2]
for thisComponent in hi_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
hi_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "hi_2"-------
while continueRoutine:
    # get current time
    t = hi_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=hi_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_2* updates
    waitOnFlip = False
    if start_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_2.frameNStart = frameN  # exact frame index
        start_2.tStart = t  # local t and not account for scr refresh
        start_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_2, 'tStartRefresh')  # time at next scr refresh
        start_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(start_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_2.status == STARTED and not waitOnFlip:
        theseKeys = start_2.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *press_2* updates
    if press_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        press_2.frameNStart = frameN  # exact frame index
        press_2.tStart = t  # local t and not account for scr refresh
        press_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(press_2, 'tStartRefresh')  # time at next scr refresh
        press_2.setAutoDraw(True)
    
    # *instructions_2* updates
    if instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_2.frameNStart = frameN  # exact frame index
        instructions_2.tStart = t  # local t and not account for scr refresh
        instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_2, 'tStartRefresh')  # time at next scr refresh
        instructions_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hi_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hi_2"-------
for thisComponent in hi_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "hi_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ready_2"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
ready_2Components = [ready]
for thisComponent in ready_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ready_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ready_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ready_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ready_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready* updates
    if ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ready.frameNStart = frameN  # exact frame index
        ready.tStart = t  # local t and not account for scr refresh
        ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready, 'tStartRefresh')  # time at next scr refresh
        ready.setAutoDraw(True)
    if ready.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ready.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            ready.tStop = t  # not accounting for scr refresh
            ready.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ready, 'tStopRefresh')  # time at next scr refresh
            ready.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ready_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready_2"-------
for thisComponent in ready_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
run1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='run1')
thisExp.addLoop(run1)  # add the loop to the experiment
thisRun1 = run1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun1.rgb)
if thisRun1 != None:
    for paramName in thisRun1:
        exec('{} = thisRun1[paramName]'.format(paramName))

for thisRun1 in run1:
    currentLoop = run1
    # abbreviate parameter names if possible (e.g. rgb = thisRun1.rgb)
    if thisRun1 != None:
        for paramName in thisRun1:
            exec('{} = thisRun1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "task_run"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    run_response.keys = []
    run_response.rt = []
    text.setText(stim)
    # keep track of which components have finished
    task_runComponents = [run_response, text]
    for thisComponent in task_runComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    task_runClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "task_run"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = task_runClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=task_runClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *run_response* updates
        waitOnFlip = False
        if run_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            run_response.frameNStart = frameN  # exact frame index
            run_response.tStart = t  # local t and not account for scr refresh
            run_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(run_response, 'tStartRefresh')  # time at next scr refresh
            run_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(run_response.clock.reset)  # t=0 on next screen flip
        if run_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > run_response.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                run_response.tStop = t  # not accounting for scr refresh
                run_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(run_response, 'tStopRefresh')  # time at next scr refresh
                run_response.status = FINISHED
        if run_response.status == STARTED and not waitOnFlip:
            theseKeys = run_response.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if run_response.keys == []:  # then this was the first keypress
                    run_response.keys = theseKeys.name  # just the first key pressed
                    run_response.rt = theseKeys.rt
                    # was this 'correct'?
                    if (run_response.keys == str(corrans)) or (run_response.keys == corrans):
                        run_response.corr = 1
                    else:
                        run_response.corr = 0
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + .25-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_runComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task_run"-------
    for thisComponent in task_runComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if run_response.keys in ['', [], None]:  # No response was made
        run_response.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           run_response.corr = 1;  # correct non-response
        else:
           run_response.corr = 0;  # failed to respond (incorrectly)
    # store data for run1 (TrialHandler)
    run1.addData('run_response.keys',run_response.keys)
    run1.addData('run_response.corr', run_response.corr)
    if run_response.keys != None:  # we had a response
        run1.addData('run_response.rt', run_response.rt)
    run1.addData('text.started', text.tStartRefresh)
    run1.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "task_ITI"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    task_ITIComponents = [runITI]
    for thisComponent in task_ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    task_ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "task_ITI"-------
    while continueRoutine:
        # get current time
        t = task_ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=task_ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *runITI* updates
        if runITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            runITI.frameNStart = frameN  # exact frame index
            runITI.tStart = t  # local t and not account for scr refresh
            runITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(runITI, 'tStartRefresh')  # time at next scr refresh
            runITI.setAutoDraw(True)
        if runITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > runITI.tStartRefresh + ITI-frameTolerance:
                # keep track of stop time/frame for later
                runITI.tStop = t  # not accounting for scr refresh
                runITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(runITI, 'tStopRefresh')  # time at next scr refresh
                runITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task_ITI"-------
    for thisComponent in task_ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "task_ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'run1'


# ------Prepare to start Routine "hi_3"-------
# update component parameters for each repeat
start_3.keys = []
start_3.rt = []
# keep track of which components have finished
hi_3Components = [start_3, press_3, instructions_3]
for thisComponent in hi_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
hi_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "hi_3"-------
while continueRoutine:
    # get current time
    t = hi_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=hi_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_3* updates
    waitOnFlip = False
    if start_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_3.frameNStart = frameN  # exact frame index
        start_3.tStart = t  # local t and not account for scr refresh
        start_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_3, 'tStartRefresh')  # time at next scr refresh
        start_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(start_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_3.status == STARTED and not waitOnFlip:
        theseKeys = start_3.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *press_3* updates
    if press_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        press_3.frameNStart = frameN  # exact frame index
        press_3.tStart = t  # local t and not account for scr refresh
        press_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(press_3, 'tStartRefresh')  # time at next scr refresh
        press_3.setAutoDraw(True)
    
    # *instructions_3* updates
    if instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_3.frameNStart = frameN  # exact frame index
        instructions_3.tStart = t  # local t and not account for scr refresh
        instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_3, 'tStartRefresh')  # time at next scr refresh
        instructions_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hi_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hi_3"-------
for thisComponent in hi_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "hi_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ready_2"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
ready_2Components = [ready]
for thisComponent in ready_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ready_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ready_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ready_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ready_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready* updates
    if ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ready.frameNStart = frameN  # exact frame index
        ready.tStart = t  # local t and not account for scr refresh
        ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready, 'tStartRefresh')  # time at next scr refresh
        ready.setAutoDraw(True)
    if ready.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ready.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            ready.tStop = t  # not accounting for scr refresh
            ready.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ready, 'tStopRefresh')  # time at next scr refresh
            ready.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ready_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready_2"-------
for thisComponent in ready_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "task_run"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    run_response.keys = []
    run_response.rt = []
    text.setText(stim)
    # keep track of which components have finished
    task_runComponents = [run_response, text]
    for thisComponent in task_runComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    task_runClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "task_run"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = task_runClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=task_runClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *run_response* updates
        waitOnFlip = False
        if run_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            run_response.frameNStart = frameN  # exact frame index
            run_response.tStart = t  # local t and not account for scr refresh
            run_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(run_response, 'tStartRefresh')  # time at next scr refresh
            run_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(run_response.clock.reset)  # t=0 on next screen flip
        if run_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > run_response.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                run_response.tStop = t  # not accounting for scr refresh
                run_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(run_response, 'tStopRefresh')  # time at next scr refresh
                run_response.status = FINISHED
        if run_response.status == STARTED and not waitOnFlip:
            theseKeys = run_response.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if run_response.keys == []:  # then this was the first keypress
                    run_response.keys = theseKeys.name  # just the first key pressed
                    run_response.rt = theseKeys.rt
                    # was this 'correct'?
                    if (run_response.keys == str(corrans)) or (run_response.keys == corrans):
                        run_response.corr = 1
                    else:
                        run_response.corr = 0
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + .25-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_runComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task_run"-------
    for thisComponent in task_runComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if run_response.keys in ['', [], None]:  # No response was made
        run_response.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           run_response.corr = 1;  # correct non-response
        else:
           run_response.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('run_response.keys',run_response.keys)
    trials.addData('run_response.corr', run_response.corr)
    if run_response.keys != None:  # we had a response
        trials.addData('run_response.rt', run_response.rt)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "task_ITI"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    task_ITIComponents = [runITI]
    for thisComponent in task_ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    task_ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "task_ITI"-------
    while continueRoutine:
        # get current time
        t = task_ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=task_ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *runITI* updates
        if runITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            runITI.frameNStart = frameN  # exact frame index
            runITI.tStart = t  # local t and not account for scr refresh
            runITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(runITI, 'tStartRefresh')  # time at next scr refresh
            runITI.setAutoDraw(True)
        if runITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > runITI.tStartRefresh + ITI-frameTolerance:
                # keep track of stop time/frame for later
                runITI.tStop = t  # not accounting for scr refresh
                runITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(runITI, 'tStopRefresh')  # time at next scr refresh
                runITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task_ITI"-------
    for thisComponent in task_ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "task_ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [bye]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *bye* updates
    if bye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bye.frameNStart = frameN  # exact frame index
        bye.tStart = t  # local t and not account for scr refresh
        bye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bye, 'tStartRefresh')  # time at next scr refresh
        bye.setAutoDraw(True)
    if bye.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bye.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            bye.tStop = t  # not accounting for scr refresh
            bye.frameNStop = frameN  # exact frame index
            win.timeOnFlip(bye, 'tStopRefresh')  # time at next scr refresh
            bye.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
