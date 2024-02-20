from datasets import Dataset, load_dataset

from opencompass.registry import LOAD_DATASET

from ..base import BaseDataset


@LOAD_DATASET.register_module()
class LVEvalmultifieldqaenDataset(BaseDataset):

    @staticmethod
    def load(**kwargs):
        dataset = load_dataset(**kwargs)
        split = 'test'
        raw_data = []
        for i in range(len(dataset[split])):
            question = dataset[split]['input'][i]
            context = dataset[split]['context'][i]
            answers = dataset[split]['answers'][i]
            confusing_facts = dataset[split]['confusing_facts'][i]
            answer_keywords = dataset[split]['answer_keywords'][i]
            raw_data.append({
                'input': question,
                'context': context,
                'answers_': answers,
                'answers': answers.append(answer_keywords),
                'confusing_facts':confusing_facts,
                'answer_keywords':answer_keywords,
            })
        dataset[split] = Dataset.from_list(raw_data)
        return dataset
