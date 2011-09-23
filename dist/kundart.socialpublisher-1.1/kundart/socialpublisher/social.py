import logging
import urllib,urllib2
import twitter as twitterapi
import bitly

from BTrees.OIBTree import OIBTree
from zope.annotation.interfaces import IAnnotations
from zope.component import getUtility

from kundart.socialpublisher.interfaces import ISocialPublisherSettings

twitter = 'kundart.socialpublisher.twitter'
facebook = 'kundart.socialpublisher.facebook'

settings = None

logger = logging.getLogger('kundart.socialpublisher')

def setupAnnotations(context):
    annotations = IAnnotations(context)

    if not twitter in annotations:
        annotations[twitter] = OIBTree()

    if not facebook in annotations:
        annotations[facebook] = OIBTree()

    return annotations


def shortUrl(url):
    settings = getUtility(ISocialPublisherSettings,'kundart.socialpublisher.settings')
    api = bitly.Api(login=settings.bitly_account, apikey=settings.bitly_token)
    return api.shorten(url)

def publishToTwitter(context):
    try:
        settings = getUtility(ISocialPublisherSettings,'kundart.socialpublisher.settings')
        api = twitterapi.Api(consumer_key=settings.twitter_consumer_key,
                  consumer_secret=settings.twitter_consumer_secret,
                  access_token_key=settings.twitter_access_token_key,
                  access_token_secret=settings.twitter_access_token_secret)

        message = context.title
        url = shortUrl(context.absolute_url())

        total = len(message + url)
        if total > 140:
            message = message[:-(total - 136)] + '...'

        resp = api.PostUpdate('%s %s' % (message,url))
        annotations = IAnnotations(context)
        annotations[twitter]['status'] = 1
        context.reindexObject(idxs=['twitter_post'])
    except Exception as e:
        logger.error('Error sending the Tweet, %s' % (e.message))
    


def publishToFacebook(context):
    try:
        settings = getUtility(ISocialPublisherSettings,'kundart.socialpublisher.settings')
        url = 'https://graph.facebook.com/%s/feed' % (settings.facebook_page_id)
        message = context.title
        values = dict(access_token= settings.facebook_access_token,message= message.encode('utf-8'),link= shortUrl(context.absolute_url()))
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        resp = urllib2.urlopen(req)
        annotations = IAnnotations(context)

        annotations[facebook]['status'] = 1
        context.reindexObject(idxs=['facebook_post'])
    except Exception as e:
        logger.error('Error posting to Facebook, %s' % (e.message))

def getSocialIndexStatus(context):

    annotations = IAnnotations(context)


    if 'status' not in annotations[twitter]:
        twitter_status = 0
    else:
        twitter_status = annotations[twitter]['status']

    if 'status' not in annotations[facebook]:
        facebook_status = 0
    else:
        facebook_status = annotations[facebook]['status']


    return {
               'twitter_status' : twitter_status,
               'facebook_status' : facebook_status
           }