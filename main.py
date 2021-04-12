import time
import random
import docxtpl

what_can_I_says = ["war gut", "war okay", "war ganz gut"]
improves = ["bisschen mehr arbeiten", "nichts", "time management"]
faecher = ["mathe", "kunst", "info", "english",
           "deutsch", "physik", "sport", "reli", "geschichte"]


dates = ["19.02.2020", "30.01.2021"]

# variables
what_can_I_say = ""
improve = ""


def generate(x):
    what_can_I_say = what_can_I_says[random.randint(0, len(what_can_I_says)-1)]
    improve = improves[random.randint(0, len(improves)-1)]
    doc = docxtpl.DocxTemplate("template.docx")
    context = {'what_can_I_say': what_can_I_say, "improve": improve}
    doc.render(context)
    doc.save(f"lernzeitprotokoll{x}.docx")


if __name__ == "__main__":
    for x in range(len(dates)-1):
        generate(dates[x])
