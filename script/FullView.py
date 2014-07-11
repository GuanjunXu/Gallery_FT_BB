#!/usr/bin/env python
# coding:utf-8

from uiautomatorplug.android import device as d
import time
import unittest
import commands
import string
import util

u = util.Util()

class GalleryTest(unittest.TestCase):

    def setUp(self):
        super(GalleryTest,self).setUp()
        u._clearAllResource()
        u._confirmResourceExists()
        u.launchGallery()
        u.enterXView('fullview')
        u.showPopCard()

    def tearDown(self):
        super(GalleryTest,self).tearDown()
        u.pressBack(4)

    def testSlidePictures(self):
        '''
            Summary: Slide the photo left 4 times then right 4 times
            Steps:   1.Enter full view
                     2.Slide the photo to right 4 times
                     3.Slide the photo to left 4 times
        '''
        #Step 2
        for i in range(4):
            d().swipe.left()
        #Step 3
        for j in range(4):
            d().swipe.right()

    def testCheckShareListIcons(self):
        '''
            Summary: Click share icon the share list would appear
            Steps:   1.Enter full view
                     2.Click share icon
        '''
        u.shareItem()
        assert d(text = 'See all').wait.exists(timeout = 2000)

    def testSharePictureToBlueTooth(self):
        '''
            Summary: Share 1 picture in bluetooth
            Steps:   1.Enter full view
                     2.Click share icon
                     3.Click bluetooth icon
        '''
        u.shareItem('Bluetooth')
        if d(text = 'Turn on').wait.exists(timeout = 2000):
            d(text = 'Turn on').click.wait()
        assert d(text = 'Bluetooth device chooser').wait.exists(timeout = 2000)

    def testSharePictureToPicasa(self):
        '''
            Summary: Share 1 picture in picasa
            Steps:   1.Enter full view
                     2.Click share icon
                     3.Click picasa icon
        '''
        u.shareItem('Picasa')
        assert d(text = 'Upload').wait.exists(timeout = 2000)

    def testSharePictureTowifidirect(self):
        '''
            Summary: Share 1 picture in Wi‑Fi Direct
            Steps:   1.Enter full view
                     2.Click share icon
                     3.Click Wi‑Fi Direct icon
        '''
        u.shareItem('Wi‑Fi Direct')
        assert d(text = 'Peer devices').wait.exists(timeout = 2000)

    def testSharePictureToGmail(self):
        '''
            Summary: Share 1 picture in Gmail
            Steps:   1.Enter full view
                     2.Click share icon
                     3.Click Gmail icon
        '''
        u.shareItem('Gmail')
        assert d(text = 'Subject').wait.exists(timeout = 2000)

    def testSharePictureToDrive(self):
        '''
            Summary: Share 1 picture in Drive
            Steps:   1.Enter full view
                     2.Click share icon
                     3.Click Drive icon
        '''
        u.shareItem('Drive')
        assert d(text = 'Upload to Drive').wait.exists(timeout = 2000)

    def testSharePictureToFacebook(self):
        '''
            Summary: Share 1 picture in FaceBook
            Steps:   1.Enter full view
                     2.Click share icon
                     3.Click FaceBook icon
        '''
        u.shareItem('Facebook')
        assert d(text = 'Loading...').wait.exists(timeout = 2000)

    def testDeleteSingle(self):
        '''
            Summary: Delete the photo
            Steps:   1.Enter full view
                     2.Touch trash icon
                     3.Touch delete
        '''
        u.setMenuOptions('Delete')
        d(text = 'Delete').click.wait()
        assert d(text = 'Delete').wait.gone(timeout = 2000)

    def testDeleteCancel(self):
        '''
            Summary: Delete the photo
            Steps:   1.Enter full view
                     2.Touch trash icon
                     3.Touch cancel
        '''
        u.setMenuOptions('Delete')
        d(text = 'Cancel').click.wait()
        assert d(text = 'Delete').wait.gone(timeout = 2000)



    
