import os


class ArabicStemmingToolkitStemmerAlgo3():

    # Get the article content

    def readContent(article):

        if os.path.exists(article):
            return open(article, 'r', encoding="utf-8").read()

    def stem(self, content):

        #jarASTalgo3 = os.path.join('Arabic-Stemmers/libs/stemmers/services/arabic_stemming_toolkit/ast_algo3', 'AST3.jar')

        tmp = os.path.join('libs/stemmers/services/arabic_stemming_toolkit/ast_algo3', 'tmp')

        if os.path.exists(tmp):
            os.system('rm ' + tmp)

        open(tmp, 'w', encoding="utf-8").write(content)

        tmpStem = os.path.join('libs/stemmers/services/arabic_stemming_toolkit/ast_algo3', 'tmpStem.txt')

        if os.path.exists(tmpStem):
            os.system('rm ' + tmpStem)

        os.system('java -Dfile.encoding=UTF-8 -jar libs/stemmers/services/arabic_stemming_toolkit/ast_algo3/AST3.jar ' + tmp +' '+ tmpStem)

        lines = self.readContent(tmpStem)

        os.system('rm ' + tmpStem)
        os.system('rm ' + tmp)

        words = lines.split()
        stems_list = []
        for word in words:
            # add new stem to dict
            stems_list.append(word)

        return stems_list

