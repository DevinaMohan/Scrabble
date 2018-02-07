import operator
import re

D = {}
word_freq = {}
word_list = []

def main():
##   search = ["the","and","to","a","she","of","said","it","was"]
##   f = open('alice.txt','rU')
##
##   for txt in search:
##      D[txt] = 0
##
##   for line in f:
##      words = line.split()
##      for w in  words:
##         if w in D:
##            print (w)
##            D[w] = D[w] + 1
##      print (line)
##
##   print (D)
##   f.close()
   rank_words()

def remove_special_chars(word):
   result = re.match("[\W]*",word)
   if result:
      str1 = re.sub("[\W]*",'',word)
      print (word,"---",str1)
      return str1
   else:
      return word

def rank_words():
   f = open("alice.txt","rU")
   fwriter = open("words.txt","w")
  
   for line in f:
      words = line.split()
      for w in words:
         if w.lower() in word_freq:
##         if word_freq.has_key(w.lower()): (used in python2)
            word_freq[w.lower()] = word_freq[w.lower()] + 1
         else:
            word_freq[w.lower()] = 1

   word_list = sorted(word_freq.items(), reverse=True, key=operator.itemgetter(1))
   print ("--------------------")
   for w in word_list[:20]:
      print (w[0], "----", w[1])

   for w in word_list:
      str1 =  remove_special_chars(w[0])
      fwriter.write(str(str1))
      fwriter.write("--")
      fwriter.write(str(w[1]))
      fwriter.write("\n")

   f.close()
   fwriter.close()

if __name__ == "__main__":
   main()

