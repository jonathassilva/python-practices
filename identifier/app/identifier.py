class Identifier:
    def validate_identifier(self, s):
        achar = ''
        valid_id = False
        achar = s[0]
        valid_id = self.valid_s(achar)
        if len(s) > 1:
            achar = s[1]
            i = 1
            while i < len(s) - 1:
                achar = s[i]
                if not self.valid_f(achar):
                    valid_id = False
                i += 1
        if valid_id and (len(s) >= 1) and (len(s) < 6):
            return True
        else:
            return False

    def valid_s(self, ch):
        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
            return True
        else:
            return False

    def valid_f(self, ch):
        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9'):
            return True
        else:
            return False
