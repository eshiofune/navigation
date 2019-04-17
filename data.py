from data_structures import Node

gate = Node("Unilag Gate", (0,0))
education = Node("Faculty of Education", (5,2))
sports = Node("Sports Centre", (0,5))
new_hall = Node("New Hall", (0,13))
dli = Node("DLI", (15,2))
fss = Node("Faculty of Social Sciences", (7,13))
cca = Node("Cultural and Creative Arts", (10,13))
cits = Node("CITS", (0,18))
bookshop = Node("Bookshop", (0,23))
arts = Node("Faculty of Arts", (-2,26))
senate = Node("Senate Building", (-2,28))
library = Node("Main Library", (0,30))
bus_ad = Node("Faculty of Business Administration", (-5,33))
law = Node("Faculty of Law", (-2,30))
science = Node("Faculty of Science", (12,25))
eng = Node("Faculty of Engineering", (8,28))

EDGES = [
    (gate, education),
    (gate, sports),
    (sports, education),
    (education, dli),
    (sports, new_hall),
    (new_hall, fss),
    (fss, cca),
    (cca, dli),
    (cca, science),
    (new_hall, cits),
    (cits, bookshop),
    (bookshop, arts),
    (arts, senate),
    (senate, law),
    (law, library),
    (law, bus_ad),
    (arts, bus_ad),
    (bookshop, science),
    (science, eng),
    (eng, library)
]
