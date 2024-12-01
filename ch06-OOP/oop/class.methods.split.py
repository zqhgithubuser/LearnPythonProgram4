class StringUtil:
    @classmethod
    def is_palindrome(cls, s, case_insensitive=True):
        s = cls._strip_string(s)
        if case_insensitive:
            s = s.lower()
        return cls._is_palindrome(s)

    @staticmethod
    def _strip_string(s):
        return "".join(c for c in s if s.isalnum())

    @staticmethod
    def _is_palindrome(s):
        for c in range(len(s) // 2):
            if s[c] != s[-1 - c]:
                return False
        return True

    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())


print(StringUtil.is_palindrome("A nut for a jar of tuna"))
print(StringUtil.is_palindrome("A nut for a jar of beans"))
