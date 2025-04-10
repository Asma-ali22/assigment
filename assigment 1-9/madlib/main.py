def mad_libs():
    print("lets play Mad libs! fill in the blanks with your own words")

    name=input("Give me a name: ")
    place=input("Give me a place: ")
    funny_adj=input("Give me a funny adjective: ")
    random_object=input("Give  me a random object: ")
    animal=input("Give me an animal: ")
    action_verb=input("Give me an action verb: ")
    funny_exclamation=input("Give me funny Exclamation: ")

    story=f'''
    Once upon a time,there was a person named {name} who lived in a {place}.
    One day,they found a {funny_adj} {random_object} that belonged to a {animal}.
    The {animal} was very upset and started to {action_verb} around.
    {name} couldn't help but laugh and shouted "{funny_exclamation}" '''


    print("Here is your Mad libs story: ")
    print(story)

if __name__ == "__main__":
    mad_libs()