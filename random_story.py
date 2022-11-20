#  Importing random module
import random
  
# Defining list of phrases which will help to build a story
  
Sentence_starter = ['About 100 years ago', ' In the 1 BC', 'Once upon a time']
character = [' there lived a king.',' there was a teacher named Sahil Chopra.',
             ' there lived a farmer.',' there was a brilliant student named Shivam.']
time = [' One day', ' One full-moon night',' One dark night',' One morning']
story_plot = [' he was passing by',' he was going for a picnic to ',' he was busycalculating the marks of students']
place = [' the mountains', ' the garden',' the university',' the school',' the playground']
second_character = [' he saw a man', ' he saw a young lady',' he saw a beautiful girl']
age = [' who seemed to be in late 20s', ' who seemed very old and feeble',' who seemed to be in her early 30s']
work = [' searching something.', ' digging a well on roadside.',' helping another weak person.',' teaching a student named jack.',' Singing a song for a homeless person.']
  
# Selecting an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+
      random.choice(time)+random.choice(story_plot) +
      random.choice(place)+random.choice(second_character)+
      random.choice(age)+random.choice(work))