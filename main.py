from tkinter import Tk, Label, Entry, Button, Frame, filedialog, Text, CENTER, Scrollbar, messagebox
import tkinter as tk
import os
from src import process_data
from src import prepare_display
from src import user_input_validation

markers = ['DYS576','DYS389I','DYS448','DYS389II','DYS19','DYS391','DYS481','DYS549','DYS533','DYS438','DYS437','DYS570','DYS635','DYS390','DYS439','DYS392','DYS643','DYS393','DYS458','DYS385A/B','DYS456','Y-GATA-H4']

def main():
  entry_fields = {}
  docx_paths = []
  user_input = {}

  def get_results():
    if len(docx_paths) > 0:
      if os.path.exists(docx_paths[0]):
        file_name, file_extension = os.path.splitext(docx_paths[0])
        if file_extension != '.docx':
          text_display.delete('1.0', tk.END)
          text_display.insert('1.0', "The file selected is not a .docx file! Please select a .docx file to compare")
        file_size = os.path.getsize(docx_paths[0])
        if file_size > 200000:
          big_file_answer = messagebox.askquestion("Warning", "This file is big and can take some time to be processed. \n\nContinue anyway?")
          if big_file_answer == "no":
            return
          if big_file_answer == "yes":
            text_display.delete('1.0', tk.END)
            text_display.insert('1.0', "Please wait, the comparison is in progress...")
            browse_button.config(state=tk.DISABLED)
            results_button.config(state=tk.DISABLED)
            window.update()
        get_user_values()
        browse_button.config(state=tk.NORMAL)
        results_button.config(state=tk.NORMAL)

      else:
        text_display.delete('1.0', tk.END)
        text_display.insert('1.0', "Please select a .docx file to compare")
    else:
      text_display.delete('1.0', tk.END)
      text_display.insert('1.0', "Please select a .docx file to compare")


  def get_user_values():
    for marker in markers:
      value = entry_fields[marker].get()
      if user_input_validation.validate(value):
        user_input[marker] = value
      else:
        text_display.delete('1.0', tk.END)
        text_display.insert('1.0', '\n\n   Please complete the pattern to analyze.\n\n   The accepted inputs for each cell are:\n\n   -An integer number\n   -A decimal number \n   -Multiple numbers separated by slashes\n   -The expression "ND" (not determined).\n\n\n   Examples: \n   18 \n   9/10/11\n   17/18.2\n   ND')
        return
    user_input['MUESTRA'] = "user"
    process_and_report()

  def process_and_report():  
    text_display.tag_remove("center", "1.0", "end")
    report = process_data.process(docx_paths[0], user_input)
    final_report = prepare_display.process(report)
    text_display.delete('1.0', tk.END)
    text_display.insert('1.0', final_report)

  def browse():
    file_path = filedialog.askopenfilename()
    if file_path not in docx_paths:
      browse_input.delete(0, tk.END)
      browse_input.insert(0, file_path)
      docx_paths.insert(0, file_path)
      list_of_docs.config(text='\n'.join(docx_paths))

  window = Tk()
  window.geometry('720x730')

  color1 = '#E3F2FD'
  color2 = '#BBDEFB'
  color3 = '#90CAF9'

  window.configure(bg=color3)

  first_box = Frame(window, bg=color1)
  first_box.pack(fill="x")

  second_box = Frame(window, bg=color2)
  second_box.pack(fill="x")

  third_box = Frame(window, bg=color3)
  third_box.pack(fill="x")

  user_sample_label = Label(first_box, text="Insert the sample data here", bg=color1, font="Verdana")
  user_sample_label.pack(pady=10) 

  user_input_frame = Frame(first_box, bg=color1)
  user_input_frame.pack(pady=10)

  for i, marker in enumerate(markers):
    if i<11:
      row_order = 2
      column_order = i
    else:
      row_order = 4
      column_order = i - 11
    label = Label(user_input_frame, text=marker, width=8 , bg=color1)
    label.grid(row=row_order, column=column_order)

    entry = Entry(user_input_frame, width=8) 
    entry.grid(row=row_order + 1, column=column_order)

    entry_fields[marker] = entry

  browse_frame_label = Label(second_box, text='Press the "Browse" button to select the .docx document to compare against', bg=color2, font="Verdana")
  browse_frame_label.pack(pady=(10, 5)) 

  browse_frame = Frame(second_box, bg=color2)
  browse_frame.pack(pady=10)

  list_of_docs = Label(second_box, text='', bg=color2)
  list_of_docs.pack(pady=5)

  browse_input = Entry(browse_frame, width=70)
  browse_input.grid(row = 0, column = 0, padx=(0, 10))

  browse_button = Button(browse_frame, text="Add new .docx file", command=browse)
  browse_button.config(state=tk.NORMAL)
  browse_button.grid(row = 0, column = 1)

  results_button = Button(third_box, text="Get results", font="Verdana", command=get_results)
  results_button.config(state=tk.NORMAL)
  results_button.pack(pady=10)

  ascii_art = '''`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`
   `=`,'=/     `=`,'=/     `=`,'=/     `=`,'=/   `=`,'=/     `=`,'=/     
     y==/        y==/        y==/        y==/     y==/        y==/       
   ,=,-<=`.    ,=,-<=`.    ,=,-<=`.    ,=,-<=`.   ,=,-<=`.    ,=,-<=`.   
,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,'''


  display_frame = Frame(third_box)
  display_frame.pack(pady = 10)

  text_display = Text(display_frame, wrap="word")

  scrollbar = Scrollbar(display_frame)

  text_display.configure(yscrollcommand=scrollbar.set)
  scrollbar.configure(command=text_display.yview)

  text_display.insert('1.0', "\n\nWelcome!\n\nPlease insert the pattern to match\nand select the .docx document to compare against.\nThe results will be displayed here\n\n\n" + ascii_art + '\n\n\n' + ascii_art)
  text_display.tag_configure("center", justify=CENTER)
  text_display.tag_add("center", "1.0", "end")

  text_display.pack(side="left", fill="y")
  scrollbar.pack(side="right", fill="y")

  window.mainloop()

if __name__ == "__main__":
    main()
