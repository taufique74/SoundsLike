import pickle


class Dictionary:
    def __init__(
        self,
        custom_dict: str = "assemblyai/third_party/SoundsLike/pn_phoneme_dict.pickle",
    ):
        self.dictionary = self.load_dictionary(custom_dict)
        self.dset = set(list(self.dictionary.keys()))
        self.phoneme_word_dict = self.create_phoneme_word_dict()

    def create_phoneme_word_dict(self):
        phoneme_word_dict = {}
        for word in self.dset:
            phoneme_word = [self._unstressed_phone(p) for p in self.dictionary[word]]
            phoneme_word_dict[word] = phoneme_word
        return phoneme_word_dict

    def _unstressed_phone(cls, phone):
        """Takes a phone and removes the stress marker if it exists"""
        if not phone[-1].isdigit():
            return phone
        else:
            return phone[:-1]

    def load_dictionary(self, custom_dict):
        with open(custom_dict, "rb") as f:
            dictionary = pickle.load(f)
        return dictionary

    def __getitem__(self, key):
        return self.dictionary[key]
