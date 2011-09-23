from persistent import Persistent
from kundart.socialpublisher.interfaces import ISocialPublisherSettings
from zope.interface import implements

class SocialPublisherSettings(Persistent):

    implements(ISocialPublisherSettings)

    twitter_consumer_key = '--'

    twitter_consumer_secret = '--'

    twitter_access_token_key = '--'

    apache_fop_path = '--'

    twitter_access_token_secret = '--'

    facebook_page_id = '--'

    facebook_access_token = '--'

    bitly_account = '--'

    bitly_token = '--'