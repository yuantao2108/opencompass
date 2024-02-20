from mmengine.config import read_base

with read_base():
    from .lveval_cmrc_mixup_gen_a50c77 import LongBench_2wikimqa_datasets  # noqa: F401, F403
