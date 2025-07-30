print("\33[33m\nHello, I am Eliza. I'll be your therapist today. (enter 'q' to quit, at any prompt)")

key_nouns = ["mother", "python", "the sandman"]

key_verbs = ["avoid", "worry", "fear"]

prompt= ("\33[33m\nHow can I help you today?: ".upper())


while True:
    user_input = input(prompt)

    if user_input == "q":
        print("\33[33m\nGoodbye, see you next time!".upper())
        break

    prompt = ("\33[33m\nTell me more. ".upper())

    for word in key_verbs:
      if word in user_input.lower():
        start_index = user_input.find(word)
        end_index = user_input.find(".")

        if end_index == -1:
          end_index = len(user_input)

        partial_response = user_input[start_index:end_index]
        prompt = (f"\33[33m\nWhy do you {partial_response}? ".upper())


    for word in key_nouns:
        if word in user_input.lower():
            prompt = (f"\33[33m\nWhat made you think of {word}? ".upper())