import os
import json


class SentenceCard:
    def __init__(self,
                 sentence,
                 translate=None):
        self.sentence = sentence
        self.translate = translate


class SentenceCardDict:
    def __init__(self, path=None):
        self.dict = {}
        if path:
            self.create_from_json(path)

    def append(self, sentence_card):
        if type(sentence_card) is str:
            self.dict[sentence_card] = SentenceCard(sentence_card)
        else:
            self.dict[sentence_card.sentence] = sentence_card

    def save(self, path):
        word_card_list_path = os.path.join(path, "sentence_card.json")
        json_data = self.to_dict()
        with open(word_card_list_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

    def delete(self, sentence):
        if sentence in self.dict:
            del self.dict[sentence]

    def create_from_json(self, path):
        sentence_json_path = os.path.join(path, "sentence_card.json")
        if os.path.exists(sentence_json_path):
            with open(sentence_json_path, 'r', encoding='utf-8') as f:
                word_card_data = json.load(f)
            for key, value in word_card_data.items():
                word_card = SentenceCard(key, value['translate'])
                self.append(word_card)

    def to_dict(self):
        data_dict = {}
        for sentence, sentence_card in self.dict.items():
            data_dict[sentence] = {
                "translate": sentence_card.translate
            }
        return data_dict
