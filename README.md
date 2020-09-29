Rumba Assignment

**1. Running the Program**
- First download the directory, and extract it if necessary. 
- Then open terminal/cmd prompt and navigate to the location
in which you downloaded the directory.
- If you do not have python installed, install python. Make sure you
are running python version 3, the program is not compatible with version 2.
- Once you have navigated to the correct location and are in terminal
run: python RumbaStart.py 

**2. Testing the Program**
- The program can be tested by simply following the console print statements.
- After any task is executed, the console prints the status of the blackboard
and asks the user to check the status before continuing. This allows
for easy testing. Note that these pauses are not included in the Rumba's
running time. They are simply added to allow debugging and testing to be
easy.
- By following the sequence through which the tasks are executed, how exactly
the program follows the behaviour tree can be measured.

**3. Design**
- The tree is designed as a series of hierarchical nodes. 
- The base Node class is inherited by all other nodes.
- The base Task class, Composite class, Decorator class and Condition class 
inherits from the base Node class and are inherited by all specific nodes of their type. 
- The priority composite runs the tree as follows
   1.  each sequence and selection is defined in the priority node class. These build upon
   eachother. For example, the spot cleaning sequence is made up of three tasks and is a child
   of the general/spot selection, which is a child of the first priority node selection.
   2. In this way, by simply running the priority node, the entire tree executes in a depth
   first manner.

**4. Documentation**
- Every important class or function is documented in the source code. Thus the source code
acts as the documentation.