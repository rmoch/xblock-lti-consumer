
import logging

from .lti_consumer import LtiConsumerXBlock

from django.conf import settings

from xblock.utils import component_factory


logger = logging.getLogger('__name__')

# https://groups.google.com/forum/#!topic/edx-code/3hQVXPd1sRM

#editable_fields = (
#'display_name', 'description', 'lti_id', 'launch_url', 'custom_parameters', 'launch_target', 'button_text',
#'inline_height', 'modal_height', 'modal_width', 'has_score', 'weight', 'hide_launch', 'accept_grades_past_due',
#'ask_to_send_username', 'ask_to_send_email'
#)


class FUNLtiConsumerXBlockBase(LtiConsumerXBlock):
    def __init__(self, *args, **kwargs):
        self.__class__.XBLOCKS_FACTORY = getattr(settings, "XBLOCKS_FACTORY")
        self.block_type = kwargs["scope_ids"].usage_id.block_type  # Hi, this is my name (ie: lti_consumer_Video)
        super(FUNLtiConsumerXBlockBase, self).__init__(*args, **kwargs)
        import ipdb; ipdb.set_trace()
        self.editable_fields = list(self.editable_fields)

        self.set_defaults()

    @property
    def _user_is_staff(self):
        return getattr(self.runtime, 'user_is_staff', False)

    def set_defaults(self):
        """
        Set default values for configured fields and remove from editable list
        """
        for field, value in self.get_configuration()['default_values'].items():
            if not self.fields[field].is_set_on(self):
                self.fields[field].write_to(self, value)
            if not self._user_is_staff:
                self.editable_fields.pop(self.editable_fields.index(field))

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
        Override parent's method to use credentials from Django settings if available
        instead of courses settings
        """
        configuration = self.get_configuration()
        if "lti" in configuration:
            return configuration["lti"]["key"], configuration["lti"]["secret"]
        return super(FUNLtiConsumerXBlockBase, self).lti_provider_key_secret


    def studio_view(self, context):
        #self.editable_fields = ['lti_id', 'launch_url', ]
        #if not self.lti_id:
        #    self.lti_id = "LTI ID test"

        return super(FUNLtiConsumerXBlockBase, self).studio_view(context)


    #def author_view(self, context):
    #    return super(FUNLtiConsumerXBlockBase, self).author_view()
