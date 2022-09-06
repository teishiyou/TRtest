import json
import logging
import math
import os
import warnings
from dataclasses import dataclass, field
from typing import Optional

import pandas as pd
import torch
import transformers
from transformers import (
    CONFIG_MAPPING,
    MODEL_WITH_LM_HEAD_MAPPING,
    AutoConfig,
    AutoModelWithLMHead,
    DataCollatorForLanguageModeling,
    DataCollatorForPermutationLanguageModeling,
    HfArgumentParser,
    LineByLineTextDataset,
    PreTrainedTokenizer,
    TextDataset,
    XLNetLMHeadModel,
    set_seed,
)


model = AutoModelWithLMHead.from_pretrained(

    
)

tokenizer = ExpressionBertTokenizer.from_pretrained(
            model_args.model_name_or_path, cache_dir=model_args.cache_dir
        )