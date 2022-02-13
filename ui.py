from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class GameInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Brain")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.question_space = Canvas(height=250, width=300, bg="red")
        self.question_text = self.question_space.create_text(150, 125, text="TEST",
                                                             font=('Arial', 20, 'italic'), width=280)
        self.question_space.grid(column=0, row=1, columnspan=2, pady=50)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.true_pressed)
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.false_pressed)

        self.right_button.grid(column=0, row=2)
        self.wrong_button.grid(column=1, row=2)

        self.update_question()

        self.window.mainloop()

    def update_question(self):
        self.question_space.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.question_space.itemconfig(self.question_text, text=question)
        else:
            self.question_space.itemconfig(self.question_text, text="The End")
            self.wrong_button.config(state="disabled")
            self.right_button.config(state="disabled")
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.question_space.config(bg="green")
        else:
            self.question_space.config(bg="red")
        self.question_space.update()
        self.window.after(1000, self.update_question())
