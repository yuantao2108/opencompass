from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.datasets import LVEvalOPTF1Evaluator, LVEvalmultifieldqaenDataset

LongBench_multifieldqa_en_mixup_reader_cfg = dict(
    input_columns=['context', 'input'],
    output_column='answers',
    extra_column='answer_keywords',
    train_split='test',
    test_split='test'
)

LongBench_multifieldqa_en_mixup_infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            round=[
                dict(role='HUMAN', prompt='Please answer the following question based on the given passages. Questions and answers are only relevant to one passage. Only give me the answer and do not output any other explanation and evidence.\n\nArticle: {context}\n\nPlease answer the following question based on the above passages. Questions and answers are only relevant to one passage. Only give me the answer and do not output any other explanation and evidence.\n\nQuestion: {input}\nAnswer:'),
            ], )),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=GenInferencer, max_out_len=64)
)

LongBench_multifieldqa_en_mixup_eval_cfg = dict(
    evaluator=dict(type=LVEvalOPTF1Evaluator),
    pred_role='BOT'
)

LongBench_multifieldqa_en_mixup_datasets = [
    dict(
        type=LVEvalmultifieldqaenDataset,
        abbr='LongBench_multifieldqa_en_mixup',
        path='Infinigence/LVEval',
        name='multifieldqa_en_mixup',
        reader_cfg=LongBench_multifieldqa_en_mixup_reader_cfg,
        infer_cfg=LongBench_multifieldqa_en_mixup_infer_cfg,
        eval_cfg=LongBench_multifieldqa_en_mixup_eval_cfg)
]