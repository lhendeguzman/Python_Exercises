print("Baby by Justin Bieber")

"""
I used the song Baby by Justin Bieber 
because I think it would be funny to choose a repetitive song in doing this

I cleaned up the lyrics by removings the capitalization, parentheses and apostrophes to avoid syntax confusion. 

"""

baby_lyrics =  """
ooh whoa  ooh whoa  ooh whoa
you know you love me  i know you care
just shout whenever and i’ll be there
you are my love  you are my heart
and we will never  ever  ever be apart
are we an item? girl quit playing
were just friends  what are you saying
said there’s another  look right in my eyes
my first love  broke my heart for the first time
and i was like baby  baby  baby oh
like baby  baby  baby no
like baby  baby  baby oh
i thought you’d always be mine mine
baby  baby  baby oh
like baby  baby  baby no
like baby  baby  baby ooh
i thought you’d always be mine
oh for you  i would have done whatever
and i just can’t believe we aint together
and i wanna play it cool
but im losing you
i’ll buy you anything
i’ll buy you any ring
and im in pieces  baby fix me
and just shake me  til you wake me from this bad dream
im going down  down  down  down
and i can’t just believe my first love won’t be around
and i’m like baby  baby  baby oh
like baby  baby  baby no
like baby  baby  baby oh
i thought you’d always be mine mine
baby  baby  baby oh
like baby  baby  baby no
like baby  baby  baby ooh
i thought you’d always be mine
luda  when i was thirteen  i had my first love
there was nobody that compared to my baby
and nobody came between us no one could ever come above
she had me going crazy
oh  i was starstruck
she woke me up daily
don’t need no starbucks
she made my heart pound
and skip a beat when i see her in the street and
at school on the playground
but i really wanna see her on the weekend
she know she got me dazing
cause she was so amazing
and now my heart is breaking
but i just keep on saying
baby  baby  baby oh
like baby  baby  baby no
like baby  baby  baby oh
i thought you’d always be mine mine
baby  baby  baby oh
like baby  baby  baby no
like baby  baby  baby ooh
i thought you’d always be mine
now im gone
yeah  yeah  yeah
yeah  yeah  yeah now im all gone
yeah  yeah  yeah
yeah  yeah  yeah now im all gone
yeah  yeah  yeah
yeah  yeah  yeah now im all gone
gone  gone  gone  im gone
""".format("World")

## Splitting the lyrics into a list and counting the number of words ##
print(baby_lyrics)
lyrics = baby_lyrics.split()
total_wordcount = len(lyrics)
string1 = "Total Number of Words in the Song: {}".format(total_wordcount)
print(string1 + "\n")


wordcount = {}
for word in lyrics:
   if word in wordcount:
      wordcount[word] += 1
   else:
      wordcount[word] = 1

count = wordcount
count1 = sorted(count.items())

for key,value in count1:
    print("{}, {}".format(key, value))

unique_words = set(lyrics)
total_unique = (len(unique_words))
string2 = "Total number of Unique Words: {}".format(total_unique)

percent = (total_unique / total_wordcount)*100
string3  = "That's only {} percent of the song".format(percent)

print("\n" + string2 + "\n" + string3)