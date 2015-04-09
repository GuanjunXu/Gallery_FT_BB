#!/usr/bin/env python
# coding:utf-8

from uiautomatorplug.android import device as d
import time
import unittest
import commands
import string
import util

u  = util.Util()
so = util.SetOption()

class GalleryTest(unittest.TestCase):

    def setUp(self):
        super(GalleryTest,self).setUp()
        u.unlockScreen()
        u._clearAllResource()
        u._confirmResourceExists()
        u.launchGallery()
        u.enterXView('fullview')
        u.showPopCard()

    def tearDown(self):
        super(GalleryTest,self).tearDown()
        u.pressBack(1)
        if d(text = 'Cancel').wait.exists():
            d(text = 'Cancel').click.wait()
        u.pressBack(4)


    def testEnterEditScreen(self):
        '''
            Summary: Enter in edit interface
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
        '''
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_localimages').click.wait()
        if d(text = 'Choose an action').wait.exists():
            d(text = 'com.intel.android.gallery3d').click.wait()
        assert d(description = 'Save').wait.exists(timeout = 2000)

    def testEditWithToneNone(self):
        '''
            Summary: Enter toning interface with selected none mode 
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch toning icon
                     5.Touch none mode
                     6.Touch save
        '''
        so.setListViewOption('fx',1)
        assert d(text = 'Save').wait.gone(timeout = 2000)

    def testEditWithTonePunch(self):
        '''
            Summary: Enter toning interface with selected punch mode 
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch toning icon
                     5.Touch punch mode
                     6.Touch save
        '''
        so.setListViewOption('fx',2)

    def testEditWithToneVintage(self):
        '''
            Summary: Enter toning interface with selected vintage mode 
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch toning icon
                     5.Touch vintage mode
                     6.Touch save
        '''
        so.setListViewOption('fx',3)

    def testEditWithToneBW(self):
        '''
            Summary: Enter toning interface with selected B/W mode 
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch toning icon
                     5.Touch B/W mode
                     6.Touch save
        '''
        so.setListViewOption('fx',4)

    def testEditWithToneBleach(self):
        '''
            Summary: Enter toning interface with selected bleach mode 
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch toning icon
                     5.Touch bleach mode
                     6.Touch save
        '''
        so.setListViewOption('fx',5)

    def testEditWithToneInstant(self):
        '''
            Summary: Enter toning interface with selected instant mode 
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch toning icon
                     5.Touch instant mode
                     6.Touch save
        '''
        so.setListViewOption('fx',6)

    def testEditWithToneLatte(self):
        '''
            Summary: Enter toning interface with selected latte mode 
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch toning icon
                     5.Touch latte mode
                     6.Touch save
        '''
        so.setListViewOption('fx',7)

    def testEditWithToneBlue(self):
        '''
            Summary: Enter toning interface with selected blue mode 
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch toning icon
                     5.Touch blue mode
                     6.Touch save
        '''
        so.setListViewOption('fx',8)

    def testEditWithToneLitho(self):
        '''
            Summary: Enter toning interface with selected litho mode 
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch toning icon
                     5.Touch litho mode
                     6.Touch save
        '''
        so.setListViewOption('fx',9)

    def testEditWithToneXProcess(self):
        '''
            Summary: Enter toning interface with selected X-Process mode 
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch toning icon
                     5.Touch X-Process mode
                     6.Touch save
        '''
        so.setListViewOption('fx',10)

    def testEditWithFrame1(self):
        '''
            Summary: Enter photo frame interface with selected the first style  
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch photo frame icon
                     5.Touch the first style
                     6.Touch save
        '''
        so.setListViewOption('border',1)
        assert d(text = 'Save').wait.gone(timeout = 2000)

    def testEditWithFrame2(self):
        '''
            Summary: Enter photo frame interface with selected the second style  
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch photo frame icon
                     5.Touch the second style
                     6.Touch save
        '''
        so.setListViewOption('border',2)

    def testEditWithFrame3(self):
        '''
            Summary: Enter photo frame interface with selected the third style  
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch photo frame icon
                     5.Touch the third style
                     6.Touch save
        '''
        so.setListViewOption('border',3)

    def testEditWithFrame4(self):
        '''
            Summary: Enter photo frame interface with selected the forth style  
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch photo frame icon
                     5.Touch the forth style
                     6.Touch save
        '''
        so.setListViewOption('border',4)

    def testEditWithFrame5(self):
        '''
            Summary: Enter photo frame interface with selected the fifth style  
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch photo frame icon
                     5.Touch the fifth style
                     6.Touch save
        '''
        so.setListViewOption('border',5)

    def testEditWithFrame6(self):
        '''
            Summary: Enter photo frame interface with selected the sixth style  
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch photo frame icon
                     5.Touch the sixth style
                     6.Touch save
        '''
        so.setListViewOption('border',6)

    def testEditWithFrame7(self):
        '''
            Summary: Enter photo frame interface with selected the seventh style  
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch photo frame icon
                     5.Touch the seventh style
                     6.Touch save
        '''
        so.setListViewOption('border',7)

    def testEnterCropScreen(self):
        '''
            Summary: Enter Crop interface 
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Crop icon
        '''
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_localimages').click.wait()
        if d(text = 'Choose an action').wait.exists():
            d(text = 'com.intel.android.gallery3d').click.wait()
        d(resourceId = 'com.intel.media.DepthFilter:id/geometryButton').click.wait()
        assert d(text = 'Straighten').wait.exists(timeout = 2000)

    def testEditWithCropStraighten(self):
        '''
            Summary: Enter Crop interface with selected straighten mode 
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Crop icon
                     5.Touch straighten mode
                     6.Apply one positive straightening adjustment
                     7.Touch save
        '''
        so.setListViewOption('geometry','straighten')

    def testEditWithCropWith1ratio1(self):
        '''
            Summary: Enter Crop interface with selected Crop mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Crop icon
                     5.Touch Crop mode and select 1:1 option
                     6.Touch save
        '''
        so.setListViewOption('geometry','crop','1:1')

    def testEditWithCropWith1ratio2(self):
        '''
            Summary: Enter Crop interface with selected Crop mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Crop icon
                     5.Touch Crop mode and select 4:3 option
                     6.Touch save
        '''
        so.setListViewOption('geometry','crop','4:3')

    def testEditWithCropWith1ratio3(self):
        '''
            Summary: Enter Crop interface with selected Crop mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Crop icon
                     5.Touch Crop mode and select 3:4 option
                     6.Touch save
        '''
        so.setListViewOption('geometry','crop','3:4')

    def testEditWithCropWith1ratio4(self):
        '''
            Summary: Enter Crop interface with selected Crop mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Crop icon
                     5.Touch Crop mode and select 5:7 option
                     6.Touch save
        '''
        so.setListViewOption('geometry','crop','5:7')

    def testEditWithCropWith1ratio5(self):
        '''
            Summary: Enter Crop interface with selected Crop mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Crop icon
                     5.Touch Crop mode and select 7:5 option
                     6.Touch save
        '''
        so.setListViewOption('geometry','crop','7:5')

    def testEditWithCropWith1ratio6(self):
        '''
            Summary: Enter Crop interface with selected Crop mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Crop icon
                     5.Touch Crop mode and select None option
                     6.Touch save
        '''
        so.setListViewOption('geometry','crop','None')
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithCropWith1ratio7(self):
        '''
            Summary: Enter Crop interface with selected Crop mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Crop icon
                     5.Touch Crop mode and select Original option
                     6.Touch save
        '''
        so.setListViewOption('geometry','crop','Original')
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithCropWithRotate(self):
        '''
            Summary: Enter Crop interface with selected Rotate mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Crop icon
                     5.Touch Rotate mode
                     6.Drag screen from right to left  one time and Apply rotate 
                     7.Touch Save Icon
        '''
        so.setListViewOption('geometry','rotate')
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithCropWithMirror(self):
        '''
            Summary: Enter Crop interface with selected Mirror mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Crop icon
                     5.Touch Mirror mode
                     6.Drag screen from right to left  one time and Apply rotate 
                     7.Touch Save Icon
        '''
        so.setListViewOption('geometry','flip')
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithBrightnessWithAutocolor(self):
        '''
            Summary: Enter Brightness interface with selected Autocolor mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Brightness icon
                     5.Touch Autocolor mode
                     6.Apply and save it
        '''
        so.setListViewOption('colors',1)
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithBrightnessWithExposure(self):
        '''
            Summary: Enter Brightness interface with selected Exposure mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Brightness icon
                     5.Touch Exposure mode
                     6.Apply and save it
        '''
        so.setListViewOption('colors',2)
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithBrightnessWithVignette(self):
        '''
            Summary: Enter Brightness interface with selected Vignette mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Brightness icon
                     5.Touch Vignette mode
                     6.Apply and save it
        '''
        so.setListViewOption('colors',3)
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithBrightnessWithContrast(self):
        '''
            Summary: Enter Brightness interface with selected Contrast mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Brightness icon
                     5.Touch Contrast mode
                     6.Apply and save it
        '''
        so.setListViewOption('colors',4)
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithBrightnessWithShadows(self):
        '''
            Summary: Enter Brightness interface with selected Shadows mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Brightness icon
                     5.Touch Shadows mode
                     6.Apply and save it
        '''
        so.setListViewOption('colors',5)
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithBrightnessWithVibrance(self):
        '''
            Summary: Enter Brightness interface with selected Vibrance mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Brightness icon
                     5.Touch Vibrance mode
                     6.Apply and save it
        '''
        so.setListViewOption('colors',6)
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithBrightnessWithSharpness(self):
        '''
            Summary: Enter Brightness interface with selected Sharpness mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Brightness icon
                     5.Touch Sharpness mode
                     6.Apply and save it
        '''
        so.setListViewOption('colors',7)
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithBrightnessWithCurves(self):
        '''
            Summary: Enter Brightness interface with selected Curves mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Brightness icon
                     5.Touch Curves mode
                     6.Apply and save it
        '''
        so.setListViewOption('colors',8)
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithBrightnessWithHue(self):
        '''
            Summary: Enter Brightness interface with selected Hue mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Brightness icon
                     5.Touch Hue mode
                     6.Apply and save it
        '''
        so.setListViewOption('colors',9)
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithBrightnessWithSaturation(self):
        '''
            Summary: Enter Brightness interface with selected Saturation mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Brightness icon
                     5.Touch Saturation mode
                     6.Apply and save it
        '''
        so.setListViewOption('colors',10)
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithBrightnessWithBWFilter(self):
        '''
            Summary: Enter Brightness interface with selected B/WFilter mode
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch Brightness icon
                     5.Touch B/WFilter mode
                     6.Apply and save it
        '''
        so.setListViewOption('colors',11)
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithTonePunchRedoAndUndo(self):
        '''
            Summary: Enter enter interface select a mode and click undo then click redo
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch toning icon
                     5.Touch punch
                     6.Touch setting menu
                     7.Touch undo
                     8.Touch setting menu
                     9.Touch redo
                     10.Touch Save
        '''
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_localimages').click.wait()
        if d(text = 'Choose an action').wait.exists():
            d(text = 'com.intel.android.gallery3d').click.wait()
        #Tap on punch option
        d(index = 1, className = 'android.view.View').click.wait()
        d(description = 'Undo').click.wait()
        d(description = 'Redo').click.wait()
        #Save the changed image
        d(description = 'Save').click.wait()
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithTonePunchReset(self):
        '''
            Summary: Enter enter interface select a mode and click reset
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch toning icon
                     5.Touch punch
                     6.Touch setting menu
                     7.Touch Reset
                     8.Touch Save
        '''
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_localimages').click.wait()
        if d(text = 'Choose an action').wait.exists():
            d(text = 'com.intel.android.gallery3d').click.wait()
        #Tap on punch option
        d(index = 1, className = 'android.view.View').click.wait()
        u.setMenuOptions('Reset')
        #Save the changed image
        d(description = 'Save').click.wait()
        assert d(description = 'Share').wait.exists(timeout = 2000)

    def testEditWithTonePunchShowHistory(self):
        '''
            Summary: Enter enter interface select a mode and click Show history 
            Steps:   1.Enter full view
                     2.Click setting menu
                     3.Touch edit
                     4.Touch toning icon
                     5.Touch punch
                     6.Touch setting menu
                     7.Touch Show History
                     8.Touch Save
        '''
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_localimages').click.wait()
        if d(text = 'Choose an action').wait.exists():
            d(text = 'com.intel.android.gallery3d').click.wait()
        #Tap on punch option
        d(index = 1, className = 'android.view.View').click.wait()
        u.setMenuOptions('Show Applied Effects')
        assert d(resourceId = 'com.intel.media.DepthFilter:id/toggleVersionsPanel').wait.exists(timeout = 2000)
        #Save the changed image
        d(description = 'Save').click.wait()
        assert d(description = 'Share').wait.exists(timeout = 2000)

