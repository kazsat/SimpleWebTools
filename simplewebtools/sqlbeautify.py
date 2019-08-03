import re

indent_string = ['select', 'from', 'where']
# TODO

class SQLBeautifier(object):

    def __init__(self):
        self.original_sql = ''
        self.beautified_sql = ''

    def set_original_sql(self, original_sql):
        self.original_sql = original_sql

    def beautify(self):
        # line = line.replace('\r', '')
        oneline = ''
        oneline = re.sub('[\r\n]', ' ', self.original_sql)

        

        self.beautified_sql = oneline

    def get_beautified_sql(self):
        return self.beautified_sql



