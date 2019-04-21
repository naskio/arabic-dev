import os


class ShereenKhojaStemmer():

    # Get the article content

    def readContent(article):

        if os.path.exists(article):
            return open(article, 'r', encoding="utf-8").read()

    def stem(self, content):

        #jarShereenKhojaSegmenter = os.path.join('.', 'KhojaStemmer.jar')

        tmp = os.path.join('libs/stemmers/services/shereen_khoja_stemmer', 'tmp')

        if os.path.exists(tmp):
            os.system('rm ' + tmp)

        open(tmp, 'w', encoding="utf-8").write(content)

        tmpStem = os.path.join('libs/stemmers/services/shereen_khoja_stemmer', 'tmpStem.txt')

        if os.path.exists(tmpStem):
            os.system('rm ' + tmpStem)

        os.system('java -Dfile.encoding=UTF-8 -jar libs/stemmers/services/shereen_khoja_stemmer/KhojaStemmer.jar ' + tmp + ' ' + tmpStem)

        string = self.readContent(tmpStem)

        os.system('rm ' + tmpStem)
        os.system('rm ' + tmp)

        words = string.split()
        stems_list = []
        for word in words:
            # add new stem to dict
            stems_list.append(word)

        return stems_list

