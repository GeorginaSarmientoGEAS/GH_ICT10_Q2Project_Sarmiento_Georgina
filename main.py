from pyscript import display, document

def student_club(e):
    document.getElementById('result').innerHTML = ' '
    firstname = document.getElementById('first_name').value
    lastname = document.getElementById('last_name').value
    studentname = firstname + ' ' + lastname
    full_names = ['Liang-Pei Co', 'Rhys Lozano', 'Savannah Sunga', 'Zoe Reyes', 'Bonnie Nubla', 'Alexa Agnote', 'Gisella Liwag', 'LJ Gabia']
    member_checker = studentname in full_names

    display_message = (f"Sorry, you did not pass" , f"Congratulations {firstname} {lastname}, you are part of Bromine Buddies, OBMC's club of nonmetal nerds!")

    document.getElementById('results').innerHTML = (display_message[member_checker])


def add_member(e):
    document.getElementById('result').innerHTML = ' '
    grade7 = {'Liang-Pei Co', 'Rhys Lozano'}
    grade8 = {'Savannah Sunga', 'Zoe Reyes'}
    grade9 = {'Bonnie Nubla', 'Alexa Agnote'}
    grade10 = {'LJ Gabia', 'Gisella Liwag'}
    
    firstname = document.getElementById('first_name').value
    surname = document.getElementById('last_name').value
    full_name = firstname + ' ' + surname

    og_members = grade7.union(grade8 | grade9 | grade10)
    og_members.add(full_name)
    display(og_members, target='output')

    display("Club members:", len(og_members), target='output')


def symbol_search(e):
    document.getElementById('result').innerHTML = ' '
    element = document.getElementById('element_symbol').value

    nonmetals = {
    "H": {'Symbol': 'H', 'Name': 'Hydrogen', 'Number': '11', 'Mass': '1.008'},
    "He":{'Symbol': 'He', 'Name': 'Helium', 'Number': '2', 'Mass': '4.003'},
    "C": {'Symbol': 'C', 'Name': 'Carbon', 'Number': '6', 'Mass': '12.01'},
    "N": {'Symbol': 'N', 'Name': 'Nitrogen', 'Number': '7', 'Mass': '14.01'},
    "O": {'Symbol': 'O', 'Name': 'Oxygen', 'Number': '8', 'Mass': '16.00'},
    "F": {'Symbol': 'F', 'Name': 'fluorine', 'Number': '9', 'Mass': '19.00'},
    "Ne": {'Symbol': 'Ne', 'Name': 'Neon', 'Number': '10', 'Mass': '20.18'},
    "P": {'Symbol': 'P', 'Name': 'phosphorus', 'Number': '15', 'Mass': '30.97'},
    "S": {'Symbol': 'S', 'Name': 'sulfur', 'Number': '16', 'Mass': '32.07'},
    "Cl": {'Symbol': 'Cl', 'Name': 'Chlorine', 'Number': '17', 'Mass': '35.45'},
    "Ar": {'Symbol': 'Ar', 'Name': 'Argon', 'Number': '18', 'Mass': '39.95'},
    "Se": {'Symbol': 'Se', 'Name': 'Selenium', 'Number': '34', 'Mass': '78.96'},
    "Br": {'Symbol': 'Br', 'Name': 'Bromine', 'Number': '35', 'Mass': '79.90'},
    "Kr": {'Symbol': 'Kr', 'Name': 'Krypton', 'Number': '36', 'Mass': '83.80'},
    "I": {'Symbol': 'I', 'Name': 'Iodine', 'Number': '53', 'Mass': '126.9'},
    "Xe": {'Symbol': 'Xe', 'Name': 'Xenon', 'Number': '54', 'Mass': '131.3'},
    "Rn": {'Symbol': 'Rn', 'Name': 'Radon', 'Number': '86', 'Mass': '(222)'}}

    info_finder = element in nonmetals
    display_message = (f'That is not in our list of Non-metals', f'({nonmetals.get(element)})')

    document.getElementById('results').innerHTML = (display_message[info_finder])
