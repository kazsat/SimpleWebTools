class SQLBeautifier(object):

    def __init__(self):
        self.original_sql = ''
        self.beautified_sql = ''

    def set_original_sql(self, original_sql):
        self.original_sql = original_sql

    def beautify(self):
        self.beautified_sql = self.original_sql

    def get_beautified_sql(self):
        return self.beautified_sql

