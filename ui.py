from tkinter import *
from quizz import QuizBrain
from PIL import ImageTk

THEME_COLOR = "#375362"
class QuizInterface:

    
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.score = 0
        self.quiz = quiz_brain
        self.window =  Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150,125,text="Some Question Text", fill=THEME_COLOR, font=("Arial", 10, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)       
        
        self.button_one = Button(command=self.left_hero_button, highlightthickness=0)
        self.button_one.grid(row=2, column=0)
        self.button_two = Button(command=self.right_hero_button, highlightthickness=0)
        self.button_two.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_img(self):
        self.left_hero_img = ImageTk.PhotoImage(file=fr"{self.quiz.hero_one_img}")
        self.button_one.config(self.button_one, image=self.left_hero_img)

        self.right_hero_img = ImageTk.PhotoImage(file=fr"{self.quiz.hero_two_img}")
        self.button_two.config(self.button_two, image=self.right_hero_img)


    def get_next_question(self):
        q_text = self.quiz.random_picks()
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.get_img()

    def left_hero_button(self):
        if self.quiz.winrate_hero_one > self.quiz.winrate_hero_two:
            self.score_increase()
        else:
            print(f"{self.quiz.hero_name_two} has higher winrate!")
        self.get_next_question()

    def right_hero_button(self):
        if self.quiz.winrate_hero_two > self.quiz.winrate_hero_one:
            self.score_increase()
        else:
            print(f"{self.quiz.hero_name_one} has higher winrate!")
        self.get_next_question()

    def score_increase(self):
        self.score += 100
        self.score_label.config(text=f"Score: {self.score}")