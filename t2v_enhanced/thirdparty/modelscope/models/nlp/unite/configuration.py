# These codes are copied from modelscope revision c58451baead80d83281f063d12fb377fad415257 
# Copyright (c) Alibaba, Inc. and its affiliates.
"""UniTE model configuration"""

from enum import Enum

from modelscope.utils import logger as logging
from modelscope.utils.config import Config

logger = logging.get_logger()


class InputFormat(Enum):
    SRC = 'src'
    REF = 'ref'
    SRC_REF = 'src-ref'


class UniTEConfig(Config):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
