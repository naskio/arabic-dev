import os


class LuceneArabicAnalyzerStemmer():

    # Get the article content

    def readContent(article):

        if os.path.exists(article):
            return open(article, 'r', encoding="utf-8").read()

    def stem(self, content):

        #luceneArabicAnalyzerStemmerJar = os.path.join('.', 'lucene-arabic-analyzer.jar')

        tmp = os.path.join('libs/stemmers/services/lucene_arabic_analyzer', 'tmp')

        if os.path.exists(tmp):
            os.system('rm ' + tmp)

        open(tmp, 'w', encoding="utf-8").write(content)
        tmpStem = os.path.join('libs/stemmers/services/lucene_arabic_analyzer', 'tmpStem.txt')

        if os.path.exists(tmpStem):
            os.system('rm ' + tmpStem)

        os.system('java -Dfile.encoding=UTF-8 -jar libs/stemmers/services/lucene_arabic_analyzer/lucene-arabic-analyzer.jar ' + tmp +' '+ tmpStem)

        lines = self.readContent(tmpStem)

        os.system('rm ' + tmpStem)
        os.system('rm ' + tmp)

        words = lines.split()
        stems_list = []
        for word in words:
            # add new stem to dict
            stems_list.append(word)

        return stems_list

