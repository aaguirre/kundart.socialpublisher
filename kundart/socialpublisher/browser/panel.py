from plone.app.controlpanel.form import ControlPanelForm
from zope.component import getUtility

from kundart.socialpublisher.interfaces import ISocialPublisherSettings
from kundart.socialpublisher import _

from zope.formlib import form


def social_publisher_settings(context):
    return getUtility(ISocialPublisherSettings,name='kundart.socialpublisher.settings')



class SocialPublisherControlPanel(ControlPanelForm):
    form_fields = form.FormFields(ISocialPublisherSettings)

    form_name = _(u"Social Publisher Settings")
    label = _(u"Social Publisher settings")
    description = _(u"Please enter the appropriate values for each variable")
    