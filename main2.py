from pyscript import display, document

name = "Georgina Erica A. Sarmiento"
age = 15
birthday = 'February 16, 2011'
hobbies = {'Violin', 'Painting', 'Photography', 'Clay-making', 'Embroidery'}
hobbylist = "<br>".join(hobbies)
shows = ('Sherlock', 'A Series of Unfortunate Events', 'Peaky Blinders', 'Percy Jackson', 'Haunting of Hill House', 'Arcane', 'Avatar: The Last Airbender')
musicals = ('Cabaret', 'The Great Gatsby', 'Hadestown', 'Hamilton', 'Miss Saigon', 'Hadestown', 'Les Miserables', 'Ride the Cyclone')

display(f'Name: {name}', f'Age: {age}', f'Birthday: {birthday}', target='info')
document.getElementById('info').innerHTML += f"<br>Hobbies:<br>{hobbylist}"

display('I like watching shows as well!', f'Such as: {shows}', target='info')

display('I also like musicals!', f'My favorite ones are: {musicals}', target='info')