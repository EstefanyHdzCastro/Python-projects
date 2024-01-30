import tkinter as tk
from tkinter import messagebox
import random
import time

class TypingSpeedTestApp:
    """A Tkinter GUI application for testing typing speed."""

    def __init__(self, master):
        """Initialize the TypingSpeedTestApp.

        Args:
            master (tk.Tk): The master tkinter window.
        """
        self.master = master
        self.master.title("Typing Speed Test")

        # List of texts for typing test
        self.texts = ["The quick brown fox jumps over the lazy dog.",
                      "A quick brown fox jumps over the lazy dog.",
                      "Pack my box with five dozen liquor jugs.",
                      "The five boxing wizards jump quickly.",
                      "How razorback-jumping frogs can level six piqued gymnasts!",
                      "Sphinx of black quartz, judge my vow.",
                      "The job requires extra pluck and zeal from every young wage earner.",
                      "Jinxed wizards pluck ivy from the big quilt.",
                      "Sixty zippers were quickly picked from the woven jute bag.",
                      "A large fawn jumped quickly over white zinc boxes."]

        self.current_text = ""  # Current text for typing
        self.start_time = 0     # Start time of typing
        self.end_time = 0       # End time of typing

        self.create_widgets()   # Create GUI widgets
        self.set_new_text()     # Set initial text for typing test

    def create_widgets(self):
        """Create GUI widgets."""
        # Label to display the text for typing
        self.text_label = tk.Label(self.master, text="", font=("Arial", 14), wraplength=400)
        self.text_label.pack(pady=20)

        # Entry field for typing
        self.input_entry = tk.Entry(self.master, font=("Arial", 12))
        self.input_entry.pack(pady=10, ipadx=10, ipady=5)
        self.input_entry.bind("<Return>", self.check_input)

        # Button to start typing test
        self.start_button = tk.Button(self.master, text="Start Typing Test", command=self.start_test)
        self.start_button.pack(pady=10, ipadx=10, ipady=5)

        # Label to display typing speed result
        self.speed_label = tk.Label(self.master, text="")
        self.speed_label.pack(pady=10)

    def set_new_text(self):
        """Set a new text for typing test."""
        self.current_text = random.choice(self.texts)
        self.text_label.config(text=self.current_text)
        self.input_entry.delete(0, tk.END)

    def start_test(self):
        """Start the typing test."""
        self.start_button.config(state=tk.DISABLED)
        self.set_new_text()
        self.start_time = time.time()

    def check_input(self, event):
        """Check the input text after typing."""
        self.end_time = time.time()
        typed_text = self.input_entry.get().strip()
        if typed_text == self.current_text:
            elapsed_time = self.end_time - self.start_time
            wpm = self.calculate_wpm(elapsed_time, len(self.current_text.split()))
            messagebox.showinfo("Result", f"You typed with a speed of {wpm} WPM.")
            self.start_button.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Incorrect typing. Try again.")
            self.input_entry.delete(0, tk.END)

    def calculate_wpm(self, elapsed_time, word_count):
        """Calculate words per minute (WPM) based on elapsed time and word count."""
        minutes = elapsed_time / 60
        wpm = word_count / minutes
        return round(wpm)

def main():
    """Main function to start the application."""
    root = tk.Tk()
    root.geometry("500x300")  # Set window size
    app = TypingSpeedTestApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
