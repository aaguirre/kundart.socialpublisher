from zope.interface import implements
from zope.viewlet.interfaces import IViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView


class SocialPublisherViewlet(BrowserView):
    """
    Render the thumbs view, but using the viewlet arch
    """
    implements(IViewlet)
    render = ViewPageTemplateFile('templates/social_publisher_viewlet.pt')

    def __init__(self, context, request, view=None, manager=None):
        super(SocialPublisherViewlet, self).__init__(context, request)
        self.context = context
