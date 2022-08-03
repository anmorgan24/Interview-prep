def detectCapitalUse(self, word):
        if word.isupper() == True or word.islower() == True or word.istitle() == True:
            return True
        else:
            return False