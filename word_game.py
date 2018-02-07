import string

def found_match(searchpattern):
   freader = open("words.txt","rU")
   for line in freader:
      word = line.split("--")
      if (word[0] == searchpattern):
         print ("Found word")
         freader.close()
         return word[1]

   return 0
   freader.close()

def alreadyPlayed(search_word, foundList):
   for w in foundList:
      if w == search_word:
         return 1
         break
   return 0

def scrabble_game(rounds,players):
   foundList = [] 
   playerScore = []
   index = 0

   for k in range(0,players+1):
      playerScore.append(0)
      
   for i in range(0,rounds):
      print ("Playing round %d" % i)
      play = 1 
      search_word = ''
      while play == 1:
         for j in range(0,players+1):
            letter = str(input("Enter the letter by player %d " % j))
            search_word = search_word + letter
            print (search_word)
            if (not alreadyPlayed(search_word, foundList)):
               score = (int)(found_match(search_word))
               if (score):
                  foundList.append(search_word)
                  index = int(j+1 % players)
                  playerScore[index] += score
                  play = 0 
                  print ("Player {0} won in round{1} - score {2}" .format(index, rounds, playerScore[index]))
                  break
               

def main():
   print ("File loading is done")
   rounds = 0
   players = 0 
   try:
      rounds = int(input("Enter the no of rounds\n"))
   except:
      print ("Enter a non-negative integer value")

   try:
      players = int(input("Enter the no of players\n"))
   except:
      print ("Enter a non-negative integer value")

   scrabble_game(rounds,players)

if __name__ == "__main__":
   main()
