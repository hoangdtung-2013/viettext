import unicodedata2, string, re

PUNCTS = tuple(string.punctuation)

class Vnese:
    @staticmethod
    def removeTones(s):
        return (''.join(c for c in unicodedata2.normalize('NFD', s) if unicodedata2.category(c) != 'Mn')).replace('đ', 'd').replace('Đ', 'D')
    
    def fixTyping(s):
        return ' '.join(word.capitalize() for word in s.strip().lower().split())

class Cases:
    def __init__(self, text):
        self.text = text
        
    def upperCase(self):
        return self.text.upper()
    
    def lowerCase(self):
        return self.text.lower()
    
    def titleCase(self):
        return self.text.lower().title()
    
    def sentenceCase(self):
        a = self.text.strip()
        if not a.endswith(PUNCTS):
            a += '.'
        return a.capitalize()
    
    def swapCase(self):
        return self.text.swapcase()
    
    def snakeCase(self, remove_tones=True):
        a = self.text.translate(str.maketrans({c: '' for c in PUNCTS}))
        return removeTones(a.lower().replace(' ', '_')) if remove_tones else a.lower().replace(' ', '_')
    
    def camelCase(self, remove_tones=True):
        a = self.text.translate(str.maketrans({c: '' for c in PUNCTS})); b = a.split()
        b[0] = b[0].lower()
        for i in range(1, len(b)):
            b[i] = b[i].capitalize()
        return removeTones(''.join(b)) if remove_tones else ''.join(b)
    
    def pascalCase(self, remove_tones=True):
        a = self.text.translate(str.maketrans({c: '' for c in PUNCTS})); b = a.split()
        for i in range(len(b)):
            b[i] = b[i].capitalize()
        return removeTones(''.join(b)) if remove_tones else ''.join(b)
    
    def screamingSnakeCase(self, remove_tones=True):
        return Convert.snakeCase(self, remove_tones = remove_tones).upper()
        
    def kebabCase(self, remove_tones=True):
        a = self.text.translate(str.maketrans({c: '' for c in PUNCTS})).lower(); b = a.split()
        return removeTones('-'.join(b)) if remove_tones else '-'.join(b)
    
    def trainCase(self, remove_tones=True):
        a = self.text.translate(str.maketrans({c: '' for c in PUNCTS})); b = a.split()
        for i in range(len(b)):
            b[i] = b[i].capitalize()
        return removeTones('-'.join(b)) if remove_tones else '-'.join(b)
            
class Processor:
    @staticmethod
    def addPreSuffix(lines, prefix=None, suffix=None):
        if prefix is None and suffix is None:
            raise ValueError('viettext.Processor.addPreSuffix() requires to provide "prefix" or "suffix"')
        else:
            if prefix:
                for i in range(len(lines)):
                    lines[i] = prefix + lines[i]
            if suffix:
                for i in range(len(lines)):
                    lines[i] = lines[i] + suffix
        return lines
    
    @staticmethod
    def lineBreakTextOccurrence(lines, mode, char):
        r = []
        for s in lines:
            if mode == "before":
                s = s.replace(char, "\n" + char).linestrip("\n")
            elif mode == "after":
                s = s.replace(char, char + "\n")
            elif mode == "instead":
                s = s.replace(char, "\n")
            r += s.splitlines()
        return r
    
    @staticmethod
    def lineBreakCharPosition(lines, break_num):
        r = []
        for i in lines:
            for j in range(0, len(s), n):
                r.append(s[i:i+n])
        return r
    
    @staticmethod
    def lineBreakAddNLine(lines, n):
        r = []
        for i in range(len(lines)):
            r.append(lines[i])
            for _ in range(n):
                r.append('')
        return r
    
    @staticmethod
    def reverseWords(s):
        return ' '.join(s.split()[::-1])
    
    @staticmethod
    def reverseLetters(s):
        return s[::-1]
    
    @staticmethod
    def removeEmoji(s):
        return re.sub(r'[\U00010000-\U0010ffff]', '', s)
