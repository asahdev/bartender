import random
def main():

  questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
                }

  ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
                }
  answers = {}   
  
  def choice():
    """Ask questions to the customer"""
    for keys in questions:
      print(questions[keys])
      print("Enter yes/no or press y/n") 
      answer_var = input()
      print("Answer is " + answer_var)
      if answer_var == "Yes" or answer_var == "y" or answer_var == "yes" or answer_var == "YES":
         answers[keys] = "True"
      else:
        answers[keys] = "False"
    return answers

  def drink(answers):
    """Shoot out reciepie"""
    ingre = []
    flattened_list = []
    for key, value in answers.items():
      if "True" == value:
        ingre.append(ingredients[key])
    for i in ingre:
      print(random.choice(i))

  choice()
 
  print("The awesome reciepie is coming up......")
  drink(answers)
  print("Would you like to have another drink?")
  answer = input()
  answer = str(answer).upper()
  print("Your answer is " + answer)
  answer_list = ["YES","Y"]
  while answer in answer_list:
    choice()
    print("The awesome reciepie is coming up......")
    drink(answers)
    print("Would you like to have another drink?")
    answer = input()
    answer = str(answer).upper()
if __name__ == "__main__":
  main()
