####################### Prompt ####################################
#The marketing team is spending way too much time typing in hashtags.
#Let's help them with our own Hashtag Generator!
#
#Here's the deal:
#
#It must start with a hashtag (#).
#All words must have their first letter capitalized.
#If the final result is longer than 140 chars it must return false.
#If the input or the result is an empty string it must return false.
#Examples
#" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
#"    Hello     World   "                  =>  "#HelloWorld"
#""                                        =>  false
###################################################################

######################## Solution #################################

def generate(s):
    #if input is empty then return false
    if not s:
        return False
    
    #create the new string
    ns = '#' + s.title().replace(' ', '')
    if len(ns) > 140:
        return False
    else:
        return ns

test = " Hello there thanks for trying my kata"
res = generate(test)
print(res)
