import tkinter as tk
from tkinter import ttk
from tkinter import Menu, messagebox

class HomeScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # -------------------- Window Properties --------------------
        self.title("Reproducing Scattering Amplitude Simplification - GUI")

        self.geometry("1200x500")  # Wider window ( WIDTH x HIEGHT )
        self.config(bg="#2C3E50")  # Dark navy background
        
        # -------------------- Menu Bar --------------------
        menu_bar = Menu(self)
        self.config(menu=menu_bar)
        
        # File Menu
        file_menu = Menu(menu_bar, tearoff=False)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        menu_bar.add_cascade(label="File", menu=file_menu)
        
        # Edit Menu
        edit_menu = Menu(menu_bar, tearoff=False)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        
        # Help Menu
        help_menu = Menu(menu_bar, tearoff=False)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        
        # -------------------- Main Content Frame --------------------
        main_frame = tk.Frame(self, bg="#34495E", bd=2, relief=tk.RIDGE)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # -------------------- Welcome Label --------------------
        welcome_label = tk.Label(
            main_frame,
            text="App Home Screen",
            font=("Arial", 28, "bold"),
            fg="#ECF0F1",  # Light text
            bg="#34495E"
        )
        welcome_label.pack(pady=30)
        
        # Subtext Label
        subtext_label = tk.Label(
            main_frame,
            text="The objectives of this application are to showcase the knowledge gained during our efforts to replicate a model that can simplify scattering amplitudes.",
            font=("Arial", 14),
            fg="#ECF0F1",
            bg="#34495E"
        )
        subtext_label.pack(pady=10)
        
        # -------------------- Buttons Frame --------------------
        button_frame = tk.Frame(main_frame, bg="#34495E")
        button_frame.pack(pady=30)

        style = ttk.Style(main_frame)

        style.theme_use("clam")


        style.configure(
            "CustomButton.TButton",
            background="#2980B9",      # Background
            foreground="#ECF0F1",      # Text
            font=("Arial", 12, "bold"),
            padding=6
        )
        # You can also define how it looks when hovered or pressed:
        style.map(
            "CustomButton.TButton",
            background=[("active", "#3498DB")],   # Hover/active background
            foreground=[("active", "#ECF0F1")]
        )

        # 4. Create the Button using your new style
        btn1 = ttk.Button(button_frame, text="Test Trasnformer", style="CustomButton.TButton" , command= lambda: self.handle_option_1() )
        btn2 = ttk.Button(button_frame, text="Pending....", style="CustomButton.TButton", command= lambda: self.handle_option_2())
        btn3 = ttk.Button(button_frame, text="Pending....", style="CustomButton.TButton",  command= lambda: self.handle_option_2())
        btn4 = ttk.Button(button_frame, text="Pending....", style="CustomButton.TButton", command= lambda: self.handle_option_2())
        btn5 = ttk.Button(button_frame, text="Pending....", style="CustomButton.TButton", command= lambda: self.handle_option_2())
        

        btn1.grid(row=0, column=0, padx=10, pady=10)
        btn2.grid(row=0, column=1, padx=10, pady=10)
        btn3.grid(row=0, column=2, padx=10, pady=10)
        btn4.grid(row=0, column=3, padx=10, pady=10)
        btn5.grid(row=0, column=4, padx=10, pady=10)
        
    # -------------------- Menu Command Methods --------------------
    def new_file(self):
        messagebox.showinfo("New File", "Create a new file...")

    def open_file(self):
        messagebox.showinfo("Open File", "Open an existing file...")

    def save_file(self):
        messagebox.showinfo("Save File", "Save the current file...")

    def exit_app(self):
        self.destroy()
        
    def cut_text(self):
        messagebox.showinfo("Cut", "Cut text...")

    def copy_text(self):
        messagebox.showinfo("Copy", "Copy text...")

    def paste_text(self):
        messagebox.showinfo("Paste", "Paste text...")

    def show_about(self):
        messagebox.showinfo("About", "This may open a window containing mor information on the app.")
    
    # -------------------- Button Command Methods --------------------
    def handle_option_1(self):
        print('Test Transformer was pressed')

    def handle_option_2(self):
        print('Button not ready yet')


# Run the application
if __name__ == "__main__":
    app = HomeScreen()
    app.mainloop()
