from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import datetime
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-List')
        self.root.geometry('650x450+500+250')

        self.label = Label(self.root, text='To-Do-List-App',
                           font='ariel, 25 bold', width=10, bd=5, bg='cyan', fg='deeppink')
        self.label.pack(side='top', fill=BOTH)

        self.label1 = Label(self.root, text='Add Task',
                            font='ariel, 18 bold', width=10, bd=5, bg='deeppink', fg='cyan')
        self.label1.place(x=40, y=54)

        self.label2 = Label(self.root, text='Tasks',
                            font='ariel, 18 bold', width=10, bd=5, bg='deeppink', fg='cyan')
        self.label2.place(x=320, y=54)

        self.label3 = Label(self.root, text='Select Date',
                            font='ariel, 18 bold', width=10, bd=5, bg='deeppink', fg='cyan')
        self.label3.place(x=30, y=400)

        self.main_text = Listbox(self.root, height=9, bd=5, width=25, font='areil, 20 italic bold')
        self.main_text.place(x=200, y=100)

        self.text = Text(self.root, bd=5, height=2, width=23, font='ariel, 10 bold')
        self.text.place(x=20, y=120)

        self.cal = DateEntry(self.root, width=16, background='darkblue',
                             foreground='white', borderwidth=6, year=2023)
        self.cal.place(x=30, y=380)

        self.time_var = StringVar()
        self.time_entry = ttk.Combobox(self.root, textvariable=self.time_var, values=self.get_time_options())
        self.time_entry.place(x=220, y=380)

        self.button = Button(self.root, text='Add', font='sarif, 20 bold italic',
                             width=8, bd=5, bg='deeppink', fg='cyan', command=self.add)
        self.button.place(x=30, y=180)

        self.button1 = Button(self.root, text='Delete', font='sarif, 20 bold italic',
                              width=8, bd=5, bg='deeppink', fg='cyan', command=self.delete)
        self.button1.place(x=30, y=280)

        self.reminder_button = Button(self.root, text='Set Reminder',
                                      font='sarif, 12 bold italic', width=12, bd=5, bg='deeppink', fg='cyan',
                                      command=self.set_reminder)
        self.reminder_button.place(x=380, y=330)

    def get_time_options(self):
        """
        Returns a list of time options for the combobox.
        """
        # Create a list of time strings in HH:MM format
        times = [f"{hour:02d}:{minute:02d}" for hour in range(24) for minute in range(0, 60, 15)]
        return times

    def add(self):
        content = self.text.get(1.0, END)
        selected_date = self.cal.get_date()
        selected_time = self.time_var.get()

        if selected_date and selected_time:
            content_with_datetime = f"{selected_date} {selected_time}: {content}"
            self.main_text.insert(END, content_with_datetime)

            with open('data.txt', 'a') as file:
                file.write(content_with_datetime + '\n')

            self.text.delete(1.0, END)

    def delete(self):
        delete_ = self.main_text.curselection()
        self.main_text.delete(delete_)

        with open('data.txt', 'w') as f:
            items = self.main_text.get(0, END)
            for item in items:
                f.write(item)

    def set_reminder(self):
        selected_date = self.cal.get_date()
        selected_time = self.time_var.get()
        selected_task = self.main_text.get(ANCHOR)

        if selected_date and selected_time and selected_task:
            reminder_datetime_str = f"{selected_date} {selected_time}"
            reminder_datetime = datetime.datetime.strptime(reminder_datetime_str, "%Y-%m-%d %H:%M")

            current_datetime = datetime.datetime.now()

            time_difference = reminder_datetime - current_datetime

            if time_difference.total_seconds() > 0:
                messagebox.showinfo('Reminder', f'Reminder for task: {selected_task} at {reminder_datetime}')
            else:
                messagebox.showwarning('Invalid Date', 'Please select a future date and time for the reminder.')

        else:
            messagebox.showwarning('Missing Information', 'Please select a task, date, and time for the reminder.')


def main():
    root = Tk()
    ui = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
