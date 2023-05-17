# Mock Interviews
## Feature Tasks

1- Ask the candidate to write a ‘Max Stack’ which is defined as a Stack with an additional getMax() member function which returns the ‘biggest’ element in the Stack.

2- The candidate can assume that only numeric values will be stored in the Stack, but she/he has to ask before the interviewer can state this.

3- The internal memory of the Stack can be approached in different ways.(Linked List/Array/Using a Node class and manually creating connections by maintaining a reference to the ‘top’ of the stack)

4- This ‘getMax()’ member function can be approached in several ways as well:

* Modifying the traditional push and pop methods to keep track on the maximum value so far.
* Use a maxStack instance variable, and each time you push a number, you check if it’s >= the peek on maxStack; if so, push it onto both maxStack and the actual stack. Then when popping, check if equal to max on maxStack, and if so, also pop maxStack.
* Traversing the entire Stack to calculate the maximum value


## Whiteboard Process

![Alt text](./Untitled%20(7).jpg)

## Approach & Efficiency

Big O= O(N).

## Interview Document

https://docs.google.com/spreadsheets/d/1sCJ8---jfg0Dle_atQjqlQg5CPM7is_oVPEeOe4R0AM/edit?usp=sharing
