


class TextSorter(object):

    def __init__(self):
        self.original_text = ''
        self.result_text = ''

    def set_original_text(self, original_text):
        self.original_text = original_text

    def text_sort(self, is_sort=True, is_eliminate_dup=False):
        lines = self.original_text.splitlines()
        # return lines.sort()
        lines.sort()

        temp_text = ''

        for line in lines:
            temp_text = temp_text + line + '\n'

        self.result_text = temp_text

        # return "aaa\nbbb\nccc\n"
        return self.result_text
