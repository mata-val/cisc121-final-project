import gradio as gr

def convert_string_to_list(text):
  parts = text.split(",")
  nums = []
  for p in parts:
    cleaned = p.strip()
    if cleaned != "":
      nums.append(int(cleaned))
  return nums

def linear_search(list_string, target_string):
  nums = convert_string_to_list(list_string)
  try:
    target = int(target_string)
  except:
    return "Target must be a number."
  
  steps = ""
  for i, value in enumerate(nums):
      steps += f"Checking index {i}: value = {value}\n"
      if value == target:
          steps += f"\n Target found at index {i}!"
          return steps
  steps += "\n Target not found in the list."   
  return steps
# Gradio interface
interface = gr.Interface(
    fn=linear_search,
    inputs=[
        gr.Textbox(label="Enter a list of numbers (comma-separated)"),
        gr.Textbox(label="Enter the target number")
    ],
    outputs=gr.Textbox(label="Step-by-step results"),
    title="Linear Search Visualizer",
    description="See how linear search checks each item in the list."
)

interface.launch()



 