import os
import json


class WordCard:
    def __init__(self,
                 word,
                 mean=None,
                 mean_r=None,
                 pron=None,
                 pron_r=None,
                 other=None):
        self.word = word
        self.mean = mean
        self.mean_r = mean_r
        self.pron = pron
        self.pron_r = pron_r
        self.other = other


class WordCardDict:
    def __init__(self, path=None):
        self.dict = {}
        if path:
            self.create_from_json(path)

    def append(self, word_card):
        if type(word_card) is str:
            self.dict[word_card] = WordCard(word_card)
        else:
            self.dict[word_card.word] = word_card

    def save(self, path):
        word_card_list_path = os.path.join(path, "word_card.json")
        json_data = self.to_dict()
        with open(word_card_list_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

    def create_from_json(self, path):
        word_card_json_path = os.path.join(path, "word_card.json")
        if os.path.exists(word_card_json_path):
            with open(word_card_json_path, 'r', encoding='utf-8') as f:
                word_card_data = json.load(f)
            for key, value in word_card_data.items():
                word_card = WordCard(key, value['mean'], value['mean_r'], value['pron'], value['pron_r'], value['other'])
                self.append(word_card)

    def to_dict(self):
        data_dict = {}
        for word, word_card in self.dict.items():
            data_dict[word] = {
                "mean": word_card.mean,
                "mean_r": word_card.mean_r,
                "pron": word_card.pron,
                "pron_r": word_card.pron_r,
                "other": word_card.other
            }
        return data_dict
