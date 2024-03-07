class Quote:

    def __init__(self, author, quote, tags):
        self.author = author
        self.quote = quote
        self.tags = tags
    
    def __str__(self):
        return '{0} \n   - {1}\n With Tags: {2}'.format(self.quote, self.author, self.tags)
    
    def __lt__(self, other):
        return len(self.quote) < len(other.quote)
    
    def __gt__(self, other):
        return len(self.quote) > len(other.quote)