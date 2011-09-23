import transaction

from zope.component import getUtility

from kundart.socialpublisher.interfaces import ISocialPublisherSettings

def unregisterUtility(context):
    utility = getUtility(ISocialPublisherSettings,'kundart.socialpublisher.settings')
    context.getSiteManager().unregisterUtility(utility, ISocialPublisherSettings,'kundart.socialpublisher.settings')
    del utility

    transaction.commit()
