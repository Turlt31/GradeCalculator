from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("Grade Calculator")
root.resizable(False, False)
root.configure(bg="#2a2b2b")

gradesFrame = Frame(root)
gradesFrame.place(x=10, y=10, height=100, width=480)

def displayGrades(gradesL):
    gradesVar.set(", ".join(gradesL))

gradesVar = StringVar()

Label(gradesFrame, textvariable=gradesVar, font=('arial', 30)).place(x=10, y=25)


gradeFrame = Frame(root, bg="#2a2b2b")
gradeFrame.place(x=10, y=120, height=100, width=480)

def calDisplayGrade(gradeL):
    if gradeL:
        numbers = [float(num) for num in gradeL]
        grade = round(sum(numbers) / len(numbers), 2)
        gradeVar.set(grade)
        if round(grade) >= 1 and round(grade) <= 3:
            roundedGradeVar.set(f"{round(grade)} (Noob)")
        elif round(grade) >= 4 and round(grade) <= 6:
            roundedGradeVar.set(f"{round(grade)} (Not Bad)")
        elif round(grade) >= 7 and round(grade) <= 10:
            roundedGradeVar.set(f"{round(grade)} (OP)")
    else:
        gradeVar.set("")
        roundedGradeVar.set("")

gradeCanvas = Canvas(gradeFrame)
gradeCanvas.place(x=0, y=0, width=140)

gradeVar = StringVar()
Label(gradeCanvas, textvariable=gradeVar, font=('arial', 40)).place(x=15, y=20)

roundedGradeCanvas = Canvas(gradeFrame)
roundedGradeCanvas.place(x=150, y=0)

roundedGradeVar = StringVar()
Label(roundedGradeCanvas, textvariable=roundedGradeVar, font=('arial', 30)).place(x=20, y=25)

buttonFrame = Frame(root, bg="#2a2b2b")
buttonFrame.place(x=10, y=230, height=160, width=480)

gradeList = []
def addGrade(grade):
    global gradeList
    if grade != "CLEAR":
        gradeList.append(grade)
    else:
        gradeList = []
    displayGrades(gradeList)
    calDisplayGrade(gradeList)


button_positions = [
    (0, 10), (75, 10), (150, 10), (225, 10), (300, 10),
    (0, 85), (75, 85), (150, 85), (225, 85), (300, 85)
]

for i, position in enumerate(button_positions, start=1):
    button_text = str(i)
    Button(
        buttonFrame, text=button_text, font=('arial', 30),
        command=lambda text=button_text: addGrade(text)
    ).place(x=position[0], y=position[1], height=65, width=65)

buttonClear = Button(buttonFrame, text="Clear\nScreen", font=('arial', 25), command=lambda:addGrade("CLEAR"))
buttonClear.place(x=375, y=10, height=140, width=105)


root.mainloop()