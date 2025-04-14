students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}
while True:
     name = input("\nEntrez le nom de l’étudiant : ").capitalize()
     if name in students:
          notes = []
          for matiere, note in students[name].items():
               print(f"\n{matiere} : Note de {name} : {note}")
               notes.append(note)
          print(f"\nMoyenne de {name} : {sum(notes)/len(notes)}")

     else:
          print(f"\nL’étudiant {name} n’existe pas dans la liste.")