from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class PolicyIntranetacstjosse(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import policy.intranetacstjosse
        xmlconfig.file('configure.zcml',
                       policy.intranetacstjosse,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'policy.intranetacstjosse:default')

POLICY_INTRANETACSTJOSSE_FIXTURE = PolicyIntranetacstjosse()
POLICY_INTRANETACSTJOSSE_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(POLICY_INTRANETACSTJOSSE_FIXTURE, ),
                       name="PolicyIntranetacstjosse:Integration")