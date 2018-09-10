
import logging

from .lti_consumer import LtiConsumerXBlock

from django.conf import settings

from xblock.utils import component_factory


logger = logging.getLogger('__name__')


class FUNLtiConsumerXBlockBase(LtiConsumerXBlock):
    display_name = "I'm a FUN xblock"
    description = "I'm a FUN xblock's description"
    def __init__(self, *args, **kwargs):
        self.__class__.XBLOCKS_FACTORY = getattr(settings, "XBLOCKS_FACTORY")
        super(FUNLtiConsumerXBlockBase, self).__init__(*args, **kwargs)


    #def studio_view(self, context):
    #    """
    #    Create a fragment used to display the edit view in the Studio.
    #    """
#
#
#
    #    context.update({
    #        "self": self
    #    })
#
    #    #fragment = Fragment()
    #    #fragment.add_content(loader.render_template("static/html/cohortxblock_edit.html",context))
    #    #fragment.add_javascript(self.resource_string("static/js/src/cohortxblock_edit.js"))
    #    #fragment.initialize_js('CohortXBlockEdit')
    #    return fragment