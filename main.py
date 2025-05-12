import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage, font, ttk

# --> creating window
c1 = '#F7F9FC' # **Plano de fundo (claro)**
c2 = '#1A1A1A' # **Texto principal**
c3 = '#4F5D75' # **Texto secundário**
c4 = '#3A86FF' # **Botões/Ação principal**
c5 = '#06D6A0' # **Botão concluído/sucesso**
c6 = '#EF476F' # **Erro/alerta**
c7 = '#FFD166' # **Hover/realce**
c8 = '#1E1E2E' # **Plano de fundo escuro (modo escuro)**

window = tk.Tk()
window.title('To-do List')
window.configure(bg=c1)
window.geometry("500x600")
window.resizable(False, False)

frame_edit = None

# function add task

def add_task():
    global frame_edit

    task = enter_todo.get().strip()
    if task and task != 'Escreva sua tarefa aqui':
        if frame_edit is not None:
            update_task(task)
            frame_edit = None
        else:
            add_item_task(task)
            enter_todo.delete(0,tk.END)
    else:
        messagebox.showwarning('Entrada inválida', 'Por favor, insira uma tarefa')

# function update task

def add_item_task(entry):
    task_frame = tk.Frame(canvas_inter, bg = c1, bd=1, relief=tk.SOLID)
    task_label = tk.Label(task_frame, text=entry, font=('Roboto', 16), bg=c1, width=25, height=2, anchor = 'w')
    task_label.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

    edit_button = tk.Button(task_frame, image=icon_edit, command= lambda f=task_frame, l=task_label:preparing_edit(f,l), bg=c1, relief=tk.FLAT)
    edit_button.pack(side=tk.RIGHT, padx=5)

    delete_button = tk.Button(task_frame, image=icon_delete, command= lambda f=task_frame:delete_task(f), bg=c1, relief=tk.FLAT)
    delete_button.pack(side=tk.RIGHT, padx=10)

    task_frame.pack(fill=tk.X, padx=5, pady=5)

    check_button = ttk.Checkbutton(task_frame, command=lambda label = task_label:change_underlined(label))
    check_button.pack(side=tk.RIGHT, padx=5)

    canvas_inter.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))

def update_task(new_task):
    global frame_edit

    for widget in frame_edit.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text=new_task)
            
def preparing_edit(task_frame, task_label):
    global frame_edit
    
    frame_edit = task_frame
    enter_todo.delete(0, tk.END)
    enter_todo.insert(0, task_label.cget('text'))

def delete_task(task_frame):
    task_frame.destroy()
    canvas_inter.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))

def change_underlined(label):
    atual_font = label.cget('font')
    font_underlined = font.Font(font=atual_font)
    if font_underlined.cget('overstrike'):
        font_underlined.configure(overstrike=False)
    else:
        font_underlined.config(overstrike=True)
    label.config(font = font_underlined)

icon_edit = PhotoImage(file='assets/edit.png').subsample(8,8)
icon_delete = PhotoImage(file='assets/delete.png').subsample(8,8)

font_title = font.Font(family='Andromeda', size=20, weight='bold')
title = tk.Label(window, text = 'To-do List', font=font_title, bg = c1, fg = c2).pack(pady=20)

upFrame = tk.Frame(window, bg = c1)
upFrame.pack(pady=10)

enter_todo = tk.Entry(upFrame, font=('Roboto', 14), relief=tk.FLAT, bg=c3, fg=c1, width=30)
enter_todo.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(upFrame, command=add_task, text='Adicionar tarefa', bg = c4, fg = c1, height=1, width=15, font=('Roboto', 11), relief=tk.FLAT)
add_button.pack(side=tk.LEFT, padx=10)

# --> creating frame to do list with rolagem

list_frame = tk.Frame(window, bg = c5)
list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(list_frame, bg = c1)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) 

scroll_bar = ttk.Scrollbar(list_frame, orient='vertical', command=canvas.yview)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scroll_bar.set)
canvas_inter = tk.Frame(canvas, bg=c1)
canvas.create_window((0,0), window=canvas_inter, anchor='nw')
canvas_inter.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))



window.mainloop()
