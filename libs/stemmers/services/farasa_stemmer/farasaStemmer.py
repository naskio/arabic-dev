import os


class FarasaStemmer():

    # Get the article content

    def readContent(article):

        if os.path.exists(article):
            return open(article, 'r', encoding="utf-8").read()

    def stem(self, content):

        #jarFarasaSegmenter = os.path.join('.', 'FarasaSegmenterJar.jar')

        tmp = os.path.join('libs/stemmers/services/farasa_stemmer', 'tmp')

        if os.path.exists(tmp):
            os.system('rm ' + tmp)

        open(tmp, 'w', encoding="utf-8").write(content)
        tmpStem = os.path.join('libs/stemmers/services/farasa_stemmer', 'tmpLemma.txt')

        if os.path.exists(tmpStem):
            os.system('rm ' + tmpStem)

        os.system('java -Dfile.encoding=UTF-8 -jar libs/stemmers/services/farasa_stemmer/FarasaSegmenterJar.jar  -l true -i ' + tmp + ' -o ' + tmpStem)

        string = self.readContent(tmpStem)

        os.system('rm ' + tmpStem)
        os.system('rm ' + tmp)

        words = string.split()
        stems_list = []
        for word in words:
            # add new stem to dict
            stems_list.append(word)

        return stems_list

