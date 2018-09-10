"""
Runtime will load the XBlock class from here.
"""

from django.conf import settings

from .lti_consumer import LtiConsumerXBlock
from .lti_consumer_fun import FUNLtiConsumerXBlockBase
