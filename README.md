# CISC 121 Final Project - Linear Search 

## Chosen Algorithm
The algorithm I chose is Linear Search. I chose this algorithm because it is simple, easy to understand, and very straightforward to visualize. Since this project is about creating an educational app that shows how an algorithm works, choosing something I fully understand makes it easier for me to explain the steps clearly and show them in a user-friendly way.

## Demo video/gif/screenshot of test 
[Screen Recording 2025-12-05 at 3.22.59 PM.zip](https://github.com/user-attachments/files/23970205/Screen.Recording.2025-12-05.at.3.22.59.PM.zip)

## Problem Breakdown & Computational Thinking

### Decomposition 
I broke my project into steps to make it easier to implement:
1. Have a user input a list of numbers separated by commas, a target value, and click to see each step of the search.
2. I split the string input by the user into the parts where the comma is 
3. I go through the list one item at a time and compare each value to the target. If matches, I stop, if no match is found by the end of the list, the target is not found.
4. My program will show the steps in the search. Each time it checks a number in the list, it prints out what index it's checking and the value.
5. Display the results 

### Pattern Recognition
For linear search, it repeats the same pattern every time
- look at the first value 
- compare first value to target value
- move to next index 
-repeat until finished
The pattern is a check compare move pattern

### Abstraction 
I decide what is important for the user to see to understand the concept, and what is not important. The important stuff is showing which index is being checked, the value of the index, if the target was found or not, etc., as for not so important stuff would be the technical stuff to make the app work.

### Algorithm Design 
Input
- A list of numbers typed as text 
- A target value

Process
- Take the input list and split it at each comma
- Remove extra spaces and turn each piece into a number
- Turn the target into a number
- start at the first number in the list and compare it to the target 
- Move through the list one item at a time
	- If the item matches the target stop
	- If the end of the list is reached with no match, mark as "match not found."
- Build a message that shows the steps of the search and the final result

Output 
- A text box in Gradio app that shows:
- Each step of the search
- If numbers or target not inserted properly an error will show 
- A final line saying whether the target was found, at what index, or that it was not found
  <img width="730" height="1358" alt="image" src="https://github.com/user-attachments/assets/b1ee1d54-2a64-4302-bc30-f74d38733bea" />


  ## Hugging Face Link
  https://huggingface.co/spaces/valeria-1m/LinearSearch

  ## Author & Acknowledgment
 - Valeria Mata Garcia 25smcj@queensu.ca
 - AI Level 4 (ChatGPT) was used inside of this project
 - Python Version: 3.14.0 UI Framework: Gradio
 - Course information: CISC 121
