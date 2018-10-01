
import logging

from .lti_consumer import LtiConsumerXBlock

from django.conf import settings

from xblock.utils import component_factory


logger = logging.getLogger('__name__')


class FUNLtiConsumerXBlockBase(LtiConsumerXBlock):
    display_name = "I'm a FUN xblock"
    description = "I'm a FUN xblock's description"
    def __init__(self, *args, **kwargs):
        super(FUNLtiConsumerXBlockBase, self).__init__(*args, **kwargs)
        self.__class__.XBLOCKS_FACTORY = getattr(settings, "XBLOCKS_FACTORY")
        self.block_type = kwargs["scope_ids"].usage_id.block_type  # Hi, this is my name (ie: lti_consumer_Video)

        self.display_name = "TEST"

    def get_configuration(self):
        """
        Retrieving component configuration from Django settings
        """
        for component in self.__class__.XBLOCKS_FACTORY["components"]:
            if self.block_type.startswith(component["module"]):
                suffix = self.block_type[len(component["module"]) + 1:]
                conf = [subclass for subclass in component["subclasses"] if subclass["suffix"] == suffix][0]
                return conf

    @property
    def lti_provider_key_secret(self):
        """
        Override parent's method to use credentials from Django settings instead
        of courses settings
        """
        configuration = self.get_configuration()
        return configuration["lti"]["key"], configuration["lti"]["secret"]


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