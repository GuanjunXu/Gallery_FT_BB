#!/usr/bin/env python
from uiautomatorplug.android import device as d
from uiautomator import device as dd
import unittest
import time
import sys
import commands
import string
import random
import math
import os

PACKAGE_NAME = 'com.intel.android.gallery3d'
ACTIVITY_NAME = PACKAGE_NAME + '/.app.Gallery'

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
                                                                         #
online  = os.getcwd() + '/script/' #File path for running cases on line  *
offline = sys.path[0]              #File path for run offline            #
                                                                         #
#Just change this value to modify the file path                          *
PATH = online
                                                                         #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

#View mode list, just use their index in the list
ViewModeList = ['albumview', 'gridview', 'fullview']

##########################################################################
#SetOption properties
fxList       = ['None','Punch','Vintage','B/W','Bleach','Instant','Latte','Blue','Litho','X Process']
borderList   = ['None','4x5','Brush','Grunge','Sumi E','Tape','Black','Black R','White','White R','Cream','Cream R']
geometryList = {'straighten':'Straighten',
                'crop':'Crop',
                'rotate':'Rotate',
                'flip':'Mirror'}
colorsList   = ['Autocolor','Exposure','Vignette','Contrast','Shadows','Vibrance','Sharpness','Curves','Hue','Saturation','BW Filter','Negative','Edges','Posterize'] #'Graduated','Highlights',
editList     = {'fx':fxList,
                'border':borderList,
                'geometry':geometryList,
                'colors':colorsList}
##########################################################################

class Util():

    def __init__(self):
        pass

    def unlockScreen(self):
        if d(resourceId = 'com.android.systemui:id/lock_icon').wait.exists(timeout = 1000):
            lockWindowBounds = d(resourceId = 'com.android.systemui:id/lock_icon').info.get('bounds')
            startPoint_x = (lockWindowBounds['right']+lockWindowBounds['left'])/2
            startPoint_y = (lockWindowBounds['bottom']+lockWindowBounds['top'])/2
            d.swipe(startPoint_x,startPoint_y,startPoint_x,startPoint_y-700)

    def launchGallery(self):
        d.start_activity(component = ACTIVITY_NAME)
        if d(text = 'Camera Roll').wait.exists(timeout = 3000):
            d(text = 'Camera Roll').click.wait()
            d(text = 'Albums').click.wait()
            self.setMenuOptions('Sort by name, A-Z')
        time.sleep(1) #Switch filter may take a few seconds

    def selectFilter(self,galleryfilter):
        d(resourceId = 'android:id/up').click.wait()
        d(text = galleryfilter).click.wait()

    def getSizeOfGallery(self):
        gallerybounds = d(resourceId = 'com.intel.android.gallery3d:id/cardpop').info.get('bounds')
        top           = gallerybounds['top']
        bottom        = gallerybounds['bottom']
        left          = gallerybounds['left']
        right         = gallerybounds['right']
        centerx       = (left + right)/2-20
        centery       = (top + bottom)/2
        return top, bottom, left, right, centerx, centery

    def tapOnCenter(self):
        d.click(self.getSizeOfGallery()[4], self.getSizeOfGallery()[5])
        time.sleep(1)

    def showPopCard(self):
        d.click(self.getSizeOfGallery()[4], self.getSizeOfGallery()[0] + 1)
        d(description = 'More options').click.wait()
        if d(text = 'View photonotes').wait.exists(timeout = 2000):
            d(text = 'View photonotes').click.wait()
        else:
            d.press('back')
        time.sleep(1)

    def holdTheCenter(self):
        d.swipe(self.getSizeOfGallery()[4], self.getSizeOfGallery()[5], self.getSizeOfGallery()[4] + 1, self.getSizeOfGallery()[5] + 1)

    def enterXView(self,viewmode):
        for i in range (0, ViewModeList.index(viewmode)):
            self.tapOnCenter()

    def clickDoneButton(self):
        d.click(2350,1080)

    def pressBack(self,touchtimes):
        for i in range(0,touchtimes):
            d.press('back')

    def slideDown(self):
        homesize = d(resourceId = 'android:id/action_bar').info.get('bounds')
        bottom      = homesize['bottom']
        d.swipe(self.getSizeOfGallery()[4], bottom+1, self.getSizeOfGallery()[4], self.getSizeOfGallery()[1])

    def slideUp(self):
        homesize = d(resourceId = 'android:id/action_bar').info.get('bounds')
        bottom      = homesize['bottom']
        d.swipe(self.getSizeOfGallery()[4], self.getSizeOfGallery()[5], self.getSizeOfGallery()[4], bottom+1)

    def getMenuSize(self):
        menubounds = d(className = 'android.widget.FrameLayout').info.get('bounds')
        top        = menubounds['top']
        bottom     = menubounds['bottom']
        left       = menubounds['left']
        right      = menubounds['right']
        centerx    = (left + right)/2
        return top, bottom, left, right, centerx

    def shareItem(self,shareto = None):
        '''
            The function simulate user sharing items in gallery.
            Usage:
                If you want to share item with Facebook(this item at the bottom of the share list as default)
                
                -> shareItem('Facebook')
                
                *Do not write press menu/share icon step before using
        '''
        d(description = 'Share').click.wait()
        if shareto != None:
            if d(text = shareto).wait.gone(timeout = 2000):
                d(text = 'See all').click.wait()
                if d(text = shareto).wait.gone(timeout = 2000):
                    x_1 = self.getMenuSize()[4]
                    y_1 = self.getMenuSize()[1] * 0.9 #Cuz it goes out of screen...
                    x_2 = self.getMenuSize()[4]
                    y_2 = self.getMenuSize()[0]
                    d.swipe(x_1,y_1,x_2,y_2)
            d(text = shareto).click.wait()
        if d(text = 'Add a Google Account').wait.exists(timeout = 2000):
            raise Exception('Please sign your account in')

    def setMenuOptions(self,setoption = None):
        if setoption == 'Slideshow':
            d(resourceId = 'com.intel.android.gallery3d:id/action_slideshow').click.wait()
        else:
            d(description = 'More options').click.wait()
            if d(text = setoption).wait.exists(timeout = 1000):
                d(text = setoption).click.wait()
            else:
                d.press('back')
        if d(text = 'Choose an action').wait.exists(timeout = 2000):
            d(text = 'com.intel.android.gallery3d').click.wait()

##########################################################################################################
#                                                                                                        #
#                           BELOW IS FOR THE TESTING FILE PREPARING...                                   #
#                                                                                                        #
##########################################################################################################

    def _deleteFoldersInDCIM(self):
        picNo = commands.getoutput('adb shell ls -l /mnt/sdcard/DCIM/100ANDRO/ | wc -l')
        if string.atoi(picNo) != 0:
            commands.getoutput('adb shell rm -r /mnt/sdcard/DCIM/100ANDRO/*')
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
        time.sleep(2)
    
    def _deleteConvertFile(self):
        """
        Delete Convert File in /sdcard/Sharing/
        """
        resultNO1 = commands.getoutput('adb shell ls -l /sdcard/ | grep Sharing | wc -l')
        if string.atoi(resultNO1) !=0:
            resultNO2 = commands.getoutput('adb shell ls -l /sdcard/Sharing/ | wc -l')
            if string.atoi(resultNO2) != 0 :
                commands.getoutput('adb shell rm -r /sdcard/Sharing/*')
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
        time.sleep(2)

    def _deleteDepthSample(self):
        commands.getoutput('adb shell rm -r /sdcard/DepthSampleImages')

    def _clearAllResource(self):
        self._deleteFoldersInDCIM()
        self._deleteTestResource()
        #delete /sdcard/Sharing/ Convert files
        self._deleteConvertFile()
        #Remove pre-load depth sample images
        self._deleteDepthSample()
    
    def _deleteTestResource(self):
        resultNO = commands.getoutput('adb shell ls -l /sdcard/ | grep test | wc -l')
        if string.atoi(resultNO) != 0 :
            commands.getoutput('adb shell rm -r /mnt/sdcard/test*')
            #commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
            time.sleep(2)
        #Add on May 16th
        pngNo = commands.getoutput('adb shell ls -l /sdcard/ | grep png | wc -l')
        if string.atoi(pngNo) != 0:
            commands.getoutput('adb shell rm -r /mnt/sdcard/*.png')
            commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
            time.sleep(2)
    
    def _confirmResourceExists(self):
        """
        If not exists resource ,push the resource to sdcard
        """
        result = commands.getoutput('adb shell ls -l /sdcard/ | grep testalbum | wc -l')
        if string.atoi(result) == 0:
            self._clearAllResource()
            commands.getoutput('adb push ' + PATH + 'resource/testalbum/ ' + '/sdcard/testalbum')
            time.sleep(2)
        else:
            result1 = commands.getoutput('adb shell ls -l /sdcard/testalbum/test* | grep jpg | wc -l')
            if string.atoi(result1) != 40 :
                self._clearAllResource()
                commands.getoutput('adb push ' + PATH + 'resource/testalbum/ ' + '/sdcard/testalbum')
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard/')
        time.sleep(2)
        
    def _pushResourcesVideo(self):
        result2 = commands.getoutput('adb shell ls -l /sdcard/testvideo/ | grep 3gp | wc -l')
        if string.atoi(result2) == 0:
            commands.getoutput('adb push ' + PATH + 'resource/testvideo/ '+'/sdcard/testvideo')
            time.sleep(2)
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
        time.sleep(2)
    
    def _push1Picture(self):
        result = commands.getoutput('adb shell ls -l /sdcard/ | grep test | wc -l')
        resultNO = commands.getoutput('adb shell ls -l /sdcard/testpic1/ | grep jpg | wc -l')
        if string.atoi(result) != 1 :
            self._clearAllResource()
            commands.getoutput('adb push ' + PATH + 'resource/testpic1/ ' + '/sdcard/testpic1')
        elif string.atoi(resultNO) != 1:
            self._clearAllResource()
            commands.getoutput('adb push ' + PATH + 'resource/testpic1/ ' + '/sdcard/testpic1')
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
        time.sleep(2)
        
    def _pushConvertPicture(self):
        resultNO = commands.getoutput('adb shell ls -l /sdcard/testConvertPics/ | grep jpg | wc -l')
        if string.atoi(resultNO) == 0 :
            commands.getoutput('adb push ' + PATH + 'resource/testConvertPics/ ' + '/sdcard/testConvertPics')
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
        time.sleep(2)
    
    def _discardGmailDraft(self):
        self.press('menu')
        self.touch('gmail_discard.png')
        self.touch('gmail_discard_OK.png')
    
    def _prepareVideo(self):
        resultNO = commands.getoutput('adb shell ls -l /sdcard/ | grep test | wc -l')
        if string.atoi(resultNO) != 1:
            self._clearAllResource()
            commands.getoutput('adb push ' + PATH + 'resource/testvideo/ ' + '/sdcard/testvideo')
            commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
            time.sleep(2)
        else:
            resultNo1 = commands.getoutput('adb shell ls -l /sdcard/ | grep testvideo | wc -l')
            if string.atoi(resultNo1) != 1:
                self._clearAllResource()
                commands.getoutput('adb push ' + PATH + 'resource/testvideo/ ' + '/sdcard/testvideo')
                commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
                time.sleep(2)
    
    def _checkBurstResource(self):
        self._deleteConvertFile()
        self._deleteTestResource()
        resultNO = commands.getoutput('adb shell ls -l /sdcard/DCIM/100ANDRO/ | wc -l')
        resultNO1 = commands.getoutput('adb shell ls -l /sdcard/DCIM/100ANDRO/ | grep BST | wc -l')
        if string.atoi(resultNO) != string.atoi(resultNO1):
            self._clearAllResource()
            commands.getoutput('adb push ' + PATH + 'resource/testburstpics/ ' + '/sdcard/DCIM/100ANDRO/')
            commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
            time.sleep(2)
        elif string.atoi(resultNO1) != 10 :
            self._clearAllResource()
            commands.getoutput('adb push ' + PATH + 'resource/testburstpics/ ' + '/sdcard/DCIM/100ANDRO/')
            commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard')
            time.sleep(2)
        time.sleep(5)
    
    def _getBurstPicturesNum(self):
        result = commands.getoutput('adb  shell ls -l /sdcard/DCIM/100ANDRO/ | grep BST | wc -l')
        return result
    
    def _getPictureNumber(self):
        result = commands.getoutput('adb shell ls -l /sdcard/test*/* | grep IM | wc -l')
        return result
        
    def _getConvertFileNum(self):
        """
        Get convert file number
        """
        result = commands.getoutput('adb shell ls /sdcard/Sharing/| wc -l')
        return result 
    
    def _getPictureNoInAndro(self):
        no = commands.getoutput('adb shell ls -l /mnt/sdcard/DCIM/100ANDRO/ | wc -l')
        return no

class SetOption():
    '''
    listViewID = 'com.intel.media.DepthFilter:id/listItems'
    '''
    def _getListOrdinate(self):
        listbounds = d(resourceId = 'com.intel.media.DepthFilter:id/listItems').info.get('bounds')
        listy = (listbounds['top'] + listbounds['bottom'])/2
        listx = (listbounds['right'] + listbounds['left'])/2
        return listx, listy, listbounds['top'], listbounds['bottom']

    def _slideListViewUp(self):
        x   = self._getListOrdinate()[0]
        y_1 = self._getListOrdinate()[1]
        y_2 = self._getListOrdinate()[2]
        d.swipe(x, y_1, x, y_2)
        time.sleep(2)
        
    def _slideListViewDown(self):
        x   = self._getListOrdinate()[0]
        y_1 = self._getListOrdinate()[1]
        y_2 = self._getListOrdinate()[3]
        d.swipe(x, y_1, x, y_2)
        time.sleep(2)


    def setListViewOption(self,bottombutton,suboption,cropscale=None):
        '''
            You need just know the NO. of the wanted option, e.g.:
                you want to set an image as 'Hue' in 'Colors',

                -> _editImage('colors',9)

                *Hue is NO.9 in the option list
                *An exception, if you set something in geometry(3rd button on the bottom), you may use func like:

                -> _editImage('geometry','crop')

                *You could just use the string shows on screen

            Comparison Table:

                NO.| bottombutton | suboption            | cropscale
            -------+--------------+----------------------+---------------------
                1. | fx           | int 1 ~ 10           |
                2. | border       | int 1 ~ 7            |
                3. | geometry     | str straighten       |
                   |              |     crop             | str 1:1
                   |              |                      |     4:3
                   |              |                      |     3:4
                   |              |                      |     5:7
                   |              |                      |     7:5
                   |              |                      |     None
                   |              |                      |     Original
                   |              |     rotate           |
                   |              |     flip (*'Mirror') |
                4. | colors       | int 1 ~ 11           |
            -------+--------------+----------------------+---------------------
        '''
        d(resourceId = 'com.intel.android.gallery3d:id/action_edit_localimages').click.wait()
        if d(text = 'Choose an action').wait.exists():
            d(text = 'com.intel.android.gallery3d').click.wait()
        #Click bottom button
        d(resourceId = 'com.intel.media.DepthFilter:id/%sButton'%bottombutton).click.wait()
        if bottombutton == 'geometry':
            d(description = editList[bottombutton][suboption]).click.wait()
        else:
            slideTimes = 0
            while not d(description = editList[bottombutton][suboption-1]).wait.exists(timeout = 2000):
                self._slideListViewUp()
                slideTimes = slideTimes+1
                if slideTimes>=20:
                    break
            assert d(description = editList[bottombutton][suboption-1]).wait.exists(timeout = 2000)
            d(description = editList[bottombutton][suboption-1]).click.wait()
        #When croping image, there are some expend options
        if cropscale != None:
            d(resourceId = 'com.intel.media.DepthFilter:id/applyEffect').click.wait()
            d(text = cropscale).click.wait()
        #Some effect may need user's applying
        if d(resourceId = 'com.intel.media.DepthFilter:id/applyFilter').wait.exists(timeout = 2000):
            d(resourceId = 'com.intel.media.DepthFilter:id/applyFilter').click.wait()
        #Save the changed image
        d(description = 'Save').click.wait()
