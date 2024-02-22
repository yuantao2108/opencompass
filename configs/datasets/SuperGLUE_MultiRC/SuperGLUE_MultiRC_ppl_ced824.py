from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import PPLInferencer
from opencompass.openicl.icl_evaluator import AccEvaluator
from opencompass.datasets import MultiRCDataset

MultiRC_reader_cfg = dict(
    input_columns=["question", "text", "answer"],
    output_column="label",
)

MultiRC_infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template={
            0:
            dict(round=[
                dict(
                    role="HUMAN",
                    prompt="{text}\nQuestion: {question}\nAnswer: {answer}\nIs it true?"),
                dict(role="BOT", prompt="No, it is false."),
            ]),
            1:
            dict(round=[
                dict(
                    role="HUMAN",
                    prompt="{text}\nQuestion: {question}\nAnswer: {answer}\nIs it true?"),
                dict(role="BOT", prompt="Yes, it is true."),
            ]),
        },
    ),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=PPLInferencer),
)

MultiRC_eval_cfg = dict(evaluator=dict(type=AccEvaluator))

MultiRC_datasets = [
    dict(
        type=MultiRCDataset,
        abbr="MultiRC",
        path="./data/SuperGLUE/MultiRC/val.jsonl",
        reader_cfg=MultiRC_reader_cfg,
        infer_cfg=MultiRC_infer_cfg,
        eval_cfg=MultiRC_eval_cfg,
    )
]
