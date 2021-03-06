#!/usr/bin/python
# coding:utf-8

from uiautomatorplug.android import device as d
import unittest
import commands
import string
import time
import sys
import util

u = util.Util()

PACKAGE_NAME = 'com.intel.android.gallery3d'
ACTIVITY_NAME = PACKAGE_NAME + '/.app.Gallery'

class GalleryTest(unittest.TestCase):
    def setUp(self):
        super(GalleryTest,self).setUp()
        #Add on May 26th due to device always reboot by itself
        if d(text = 'Charging').wait.exists(timeout = 2000):
            commands.getoutput('adb root')
            time.sleep(5)
            commands.getoutput('adb remount')
            #d.swipe(530,1300,1000,1300)
            u.unlockScreen()
        u._clearAllResource()
        u._prepareVideo()
        u.launchGallery()
        u.enterXView('fullview')
        u.showPopCard()

    def tearDown(self):
        super(GalleryTest,self).tearDown()
        u.pressBack(4)
        #Discard sharing action
        if d(text = 'OK').wait.exists(timeout = 2000):
            d(text = 'OK').click.wait()
        u.pressBack(4)

    def testPlayVideoFile(self):
        '''
            Summary: Play video file
            Steps:   1.Launch socialgallery 
                     2. Select video file and Enter full view
                     3.Touch play icon and play video file
                     4.Touch screen any point twice and pause this video
                     5. Exit socialgallery 
        '''
        u.tapOnCenter()
        u.tapOnCenter() #Press playback icon
        if d(text = 'Open with').wait.exists(timeout = 2000):
            try:
                assert d(text = 'Always', enabled = 'true').wait.exists(timeout = 2000)
            except:
                d(text = 'Video player').click.wait()
            finally:
                d(text = 'Always').click.wait()
        time.sleep(10) #Play video file 10 s
        d.click(550,150) #Invoke pop card
        d.click(550,150) #Invoke pop card
        assert d(description = 'Share').wait.exists(timeout = 5000)
        #u.tapOnCenter() #Pause the video playback
        assert d(resourceId = 'com.intel.android.gallery3d:id/background_play_action_provider_button').wait.exists(timeout = 2000)

    def testShareVideoToYouTube(self):
        '''
            Summary: Share 1 video in Youtube
            Steps:   1.Enter full view
                     2.Click share icon
                     3.Click Youtube icon
        '''
        u.shareItem('YouTube')
        if d(text = 'Choose an account').wait.exists(timeout = 2000):
            d(resourceId = 'android:id/text1').click.wait()
            d(text = 'OK').click.wait()
        assert d(text = 'Upload').wait.exists(timeout = 2000)
















