import subprocess, os, sys

# so... what I want to do is check if the user enters input on the command line
# if not then ask for the question
# if there are command line args pass them to chatgpt

def ask_gpt(query):
    answer=subprocess.check_output(['tgpt', '-q', f'{query}'])
    FNULL=open(os.devnull, 'w')
    subprocess.run(['espeak', '-ven+m1', '-x', f'{answer}'], stdout=FNULL, stderr=subprocess.STDOUT)
    print(f'Transcript:\n${answer}')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query=sys.argv[1]
        ask_gpt(query)
    else:
        query=input("What do you wanna search for? ")
        ask_gpt(query)
