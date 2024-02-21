from mmengine.config import read_base

with read_base():
    # from .datasets.lveval.lveval import LVEval_datasets as datasets
    from .datasets.lveval.lvevalmultifieldqa_zh_mixup.lveval_multifieldqa_zh_mixup_gen import LVEval_multifieldqa_zh_mixup_datasets as datasets
    from .models.chatglm.hf_chatglm3_6b_32k import models
    from .summarizers.lveval import summarizer

