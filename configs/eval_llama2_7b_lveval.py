from mmengine.config import read_base

with read_base():
    from .datasets.lveval.lveval import LVEval_datasets as datasets
    from .models.hf_llama.hf_llama2_7b_chat import models
    from .summarizers.lveval import summarizer

