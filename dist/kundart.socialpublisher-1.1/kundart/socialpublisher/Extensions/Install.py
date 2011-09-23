from Products.CMFCore.utils import getToolByName
from kundart.socialpublisher.setuphandlers import unregisterUtility

def uninstall(portal, reinstall=False):

    if not reinstall:
        setup_tool = getToolByName(portal, 'portal_setup')
        setup_tool.runAllImportStepsFromProfile('profile-kundart.socialpublisher:uninstall')
        unregisterUtility(portal)

        return "Ran all uninstall steps."

