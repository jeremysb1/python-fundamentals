class StringUtil:
    @staticmethod
    def is_palindrome(s, case_insensitive=True):
        s = ''.join(c for c in s if c.isalnum())
        if case_insensitive:
            s = s.lower()
        for c in range(len(s) // 2):
            if s[c] != s[-c-1]:
                return False
        return True
    
    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())

print(StringUtil.is_palindrome('Radar', case_insensitive=False))
print(StringUtil.get_unique_words('I like to code. I really really enjoy it!'))