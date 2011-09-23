from plone.indexer.decorator import indexer
from zope.annotation.interfaces import IAnnotations
from interfaces import ITwitterPost, IFacebookPost
import social

@indexer(ITwitterPost)
def twitter_post(object, **kw):
    return social.getSocialIndexStatus(object)['twitter_status']


@indexer(IFacebookPost)
def facebook_post(object, **kw):
    return social.getSocialIndexStatus(object)['facebook_status']