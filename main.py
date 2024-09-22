import tkinther as tk
import sys
import io

class RedirectText:
   def __init__(self, text_widget):
      self.output_text = text_widget
   def write(self, string):
      self.output_text.insert(tk.END, string)
      self.output_text.see(tk.END)
   def flush(self):
      pass
  def run_code():
      user_code = code_entry.get("1.0", tk.END)
      output_text.delete("1.0", tk.END)
      try:
          sys.stdout = RedirectText(output_text)
          result = eval(user_code)
          if result is not None:
             print(result)
      except Exception:
           try:
              exec(user_code)
              except Exception as e:
                  print(f"Error: {e}")
      finally:
           sys.stdout = sys.__stdout__
root = tk.Tk()
root.title("Simple Python Interpreter")
code_entry = tk.Text(root, height=10, width=50)
code_entry.pack()
run_button = tk.Button(root, text=run, command=run_code)
run_button.pack()
output_text = tk.Text(root, height=10, width=50)
output_text.pack()
root.mainloop()
