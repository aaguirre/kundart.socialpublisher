import json
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from kundart.socialpublisher import social


class SocialPublisherWidgetView(BrowserView):
    render = ViewPageTemplateFile('templates/social_publisher.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.annotations = social.setupAnnotations(self.context)

    def __call__(self):
        return self.render()

    def canPublish(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                       name='plone_portal_state')
        return not portal_state.anonymous()


    def getStatus(self):
        return social.getSocialIndexStatus(self.context)
        


class PublishToSocialView(BrowserView):

    def __call__(self, REQUEST, RESPONSE):
        form = self.request.form

        if form.get('form.twitter_post',False):
            social.publishToTwitter(self.context)

        if form.get('form.facebook_post', False):
            social.publishToFacebook(self.context)

            
        status = social.getSocialIndexStatus(self.context)
        RESPONSE.setHeader('Content-Type', 'application/javascript')
        return json.dumps(status)
