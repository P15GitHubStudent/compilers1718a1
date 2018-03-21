
def getchar(words, pos):
    """ returns char at pos of words, or None if out of bounds """

    if pos < 0 or pos >= len(words):
        return None

    if words[pos] == ':' or words[pos] == '.':
        return "TSEP"
    elif words[pos] >= "0":
                if words[pos] <= "1":
                    return "RONE" # RANGE FROM 0-1
                elif words[pos] == "2":
                    return "TWO"
                elif words[pos] == "3":
                    return "THREE"
                elif words[pos] <= "5":
                    return "RFIVE"
                elif words[pos] <= "9":
                    return "ODIGIT"
    else:
        return None


def scan(text, transition_table, accept_states):
    """ Scans `text` while transitions exist in 'transition_table'.
    After that, if in a state belonging to `accept_states`,
    returns the corresponding token, else ERROR_TOKEN.
    """
    # initial state
    pos = 0
    state = 'q0'

    while True:

        c = getchar(text, pos)  # get nex# t char

       # print('c=', c)

        if state in transition_table and c in transition_table[state]:

            state = transition_table[state][c]  # set new state
            pos += 1  # advance to next char

        else:  # no transition found
            print('state=', state)
            # check if current state is accepting
            if state in accept_states:
                return accept_states[state], pos

            # current state is not accepting
            return 'ERROR_TOKEN', pos

td = {'q0': {'RONE': 'q1', 'TWO': 'q2', 'THREE':'q3', 'RFIVE': 'q3', 'ODIGIT': 'q3'},
      'q1': {'RONE': 'q3', 'TWO': 'q3', 'THREE': 'q3', 'RFIVE': 'q3', 'ODIGIT': 'q3', 'TSEP': 'q4'},
      'q2': {'RONE': 'q3', 'TWO': 'q3', 'THREE': 'q3', 'TSEP': 'q4'},
      'q3': {'TSEP': 'q4'},
      'q4': {'RONE': 'q5', 'TWO': 'q5', 'THREE': 'q5', 'RFIVE': 'q5'},
      'q5': {'RONE': 'q6', 'TWO': 'q6', 'THREE': 'q6', 'RFIVE': 'q6', 'ODIGIT': 'q6'}
      }

# the dictionary of accepting states and their
# corresponding token
ad = {'q6': 'TIME_TOKEN'}
# get a string from input
text = input('give some input>')

# scan text until no more input
while text:  # that is, while len(text)>0

    # get next token and position after last char recognized
    token, position = scan(text, td, ad)

    if token == 'ERROR_TOKEN':
        print('unrecognized input at pos', position + 1, 'of', text)
        break

    print("token:", token, "string:", text[:position])

    # remaining text for next scan
    text = text[position:]
