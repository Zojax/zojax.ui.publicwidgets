##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
import simplejson
from zope.app.component.hooks import getSite
from zope.app.component.interfaces import ISite
from zope.component import getMultiAdapter

from z3c.breadcrumb.interfaces import IBreadcrumb

from zojax.seo.interfaces import IHTMLTags


class SharePublic(object):
    
    def getTitle(self):
        context = self.context
        request = self.request

        tags = IHTMLTags(context, None)
        if tags is not None and tags.isAvailable() and tags.title:
            title = tags.title
        else:
            title = getMultiAdapter(
                (context, request), IBreadcrumb).name
        
        if not ISite.providedBy(context):
            site = getSite()
            tags = IHTMLTags(site, None)
            if tags is not None and tags.isAvailable() and tags.title:
                portal_title = tags.title
            else:
                portal_title = getMultiAdapter((site, request), IBreadcrumb).name
            return simplejson.dumps('%s - %s'%(title, portal_title))
        else:
            return simplejson.dumps(title)