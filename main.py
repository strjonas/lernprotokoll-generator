import time
import random
import docxtpl

what_can_I_says = ["war gut", "war okay", "war ganz gut"]
improves = ["bisschen mehr arbeiten", "nichts", "time management"]
faecher = ["mathe/raab", "kunst/roth", "info/huehne", "english/pitzen",
           "deutsch/bosshoefer", "physik/bloennigen", "sport/au", "reli/straszewski", "geschichte/bopp", "erdkunde/geib"]


dates = ["30.01.2021"]

# variables
what_can_I_say = ""
improve = ""


def generate(x):
    what_can_I_say = what_can_I_says[random.randint(0, len(what_can_I_says)-1)]
    improve = improves[random.randint(0, len(improves)-1)]
    doc = docxtpl.DocxTemplate("template.docx")
    n = x[:2]
    enddate = x[2:]
    enddate = f"{int(n)+5}{enddate}"
    context = {'what_can_I_say': what_can_I_say,
               "improve": improve, "date": x, "enddate": enddate, "name": "jonas strabel"}
    for i, y in enumerate(faecher):
        context[f"lerninhalt{i}"] = y
        t = random.randint(60, 180)
        m = t % 10
        t = t-m
        context[f"time{i}"] = f"{t}min"
    doc.render(context)
    doc.save(f"lernzeitprotokoll{x}.docx")


if __name__ == "__main__":
    for x in dates:
        generate(x)
