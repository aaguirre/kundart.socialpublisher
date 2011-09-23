from zope.interface import Interface
from zope import schema

from kundart.socialpublisher import _

class ITwitterPost(Interface):
    """ Marker interface for the Facebook post index
    """

class IFacebookPost(Interface):
    """
       Marker interface for the Facebook post index
    """

class ISocialPost(Interface):
    """
       Marker interface to show the social publisher viewlet
    """


class ISocialPublisherSettings(Interface):
    """Social Publisher Settings.
    """

    twitter_consumer_key = schema.ASCIILine(
        title=_(u'Twitter Consumer Key'),
        description=_(u'Twitter Consumer Key'),
        required=True)

    twitter_consumer_secret = schema.ASCIILine(
        title=_(u'Twitter Consumer Secret'),
        description=_(u'Twitter Consumer Secret'),
        required=True)

    twitter_access_token_key = schema.ASCIILine(
        title=_(u'Twitter Access Token Key'),
        description=_(u'Twitter Access Token Key'),
        required=True)

    twitter_access_token_secret = schema.ASCIILine(
        title=_(u'Twitter Access Token Secret'),
        description=_(u'Twitter Access Token Secret'),
        required=True)

    facebook_page_id = schema.ASCIILine(
        title=_(u'Facebook Page ID'),
        description=_(u'Facebook Page ID'),
        required=True)

    facebook_access_token = schema.ASCIILine(
        title=_(u'Facebook Access Token'),
        description=_(u'Facebook Access Token'),
        required=True)

    bitly_account = schema.ASCIILine(
        title=_(u'Bitly Account'),
        description=_(u'Bitly Account'),
        required=True)

    bitly_token = schema.ASCIILine(
        title=_(u'Bitly Token'),
        description=_(u'Bitly Token'),
        required=True)