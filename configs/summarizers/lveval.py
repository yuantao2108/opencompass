from mmengine.config import read_base

with read_base():
    from .groups.lveval import lveval_summary_groups

summarizer = dict(
    dataset_abbrs = [
        '--------- LVEval Single-Hop QA ---------', # category
        'LVEval_loogle-SD-mixup', 
        'LVEval_cmrc-mixup',
        '--------- LVEval Single-Hop CQA ---------', # category
        'LVEval_multifieldqa-en-mixup', 
        'LVEval_multifieldqa-zh-mixup',
        '--------- LVEval Multi-Hop QA ---------', # category
        'LVEval_dureader-mixup', 
        'LVEval_loogle-CR-mixup', 
        'LVEval_loogle-MIR-mixup',
        '--------- LVEval Multi-Hop CQA ---------', # category
        'LVEval_hotpotwikiqa-mixup', 
        'LVEval_lic-mixup',
        '--------- LVEval Factrecall CQA ---------', # category
        'LVEval_factrecall-en', 
        'LVEval_factrecall-zh',
    ],
    summary_groups=sum([v for k, v in locals().items() if k.endswith('_summary_groups')], []),
)
