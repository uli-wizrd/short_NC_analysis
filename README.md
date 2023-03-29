# Natural Constants and the stuff inside them

This short project pretends to explore an idea that came to me when I was still in college (I competed with others to see who knew more digits of Pi). This idea being "It's funny how there seems to be patterns in the digits of Pi, in particular at first the pattern XYX appears very often, where X is any number and Y is another number that acts as the pseudo-axis of symmetry".

I'm aware that there's information out there about the reasons behind these patterns however I wanted to explore them on my own just for the fun of it, alas I never gave myself the time to do so then. But now I'll give it a shot and see what I find, hopefully something interesting but more importantly I'll have fun working on this. 

So the idea here is just to "find out what's going on" with the digits of natural constants like Pi, Phi, e and sqrt(2). Also I'll be using my newly acquired data analyst skills.


##The questions to be answered

-Is there a tendency to these XYX patterns in the constants? 
  
  -Do the gaps between each XYX pattern become larger the more digits we have or viceversa?

-Does one digit appear more often than others?

  - How does the digit distribution behave in the first 240 digits of these constants?
  - How does the average digit frequency behave as we steadily approach 240 digits in each constant?
  - How does the standard deviation for the digit frequency behave as we steadily approach 240 decimal digits?

-How does the proportion of digits in XYX patterns behave as we approach 240 digits in these constants?

- Is there a XYX pattern that appears more often than others in these 240 digits? If so, Does it remain that way in 1234 digits?
-Is there an X value that appears more often than others in these 240 digits? If so, Does it remain that way in 1234 digits?
-Is there a Y value that appears more often than othersin these 240 digits? Does it remain that way in 1234 digits?

##Preparing the constants

We have to have a way to get all of these decimal digits, to achieve this I used the information provided in [link] where the library [] is mentioned as a way to get these constants to a precision specified by the user. 

##Processing the digits

I created a process that takes the decimal point away, transforms the float value into a text string type, then it transforms this value into a list of all the digits that composed the string value, after this every value in the list is transformed into an integer using the map function and to complete our digit list we insert in it some digits we had to convert into integers separately.

##Analizing the digits
  
1.- I started this process by creating a function that counts how many times a digit between 0-9 appears in the sequence inside the list created in the previous phase and create a summarized list of the frequency for every digit in the list. Also I use a simple sorting algorithm on my digit frequency list to give it an ascending order.

2.- After determining the frequency of the digits, I create a function to determine the average of the frequency and the standard deviation of the frequency values.

3.- I then created a process that counts how many digits pass before we have a set of values with the XYX pattern, this way we obtain the distribution of gaps in the sequence and the list of the XYX patterns.

4.-Next I create a process to determine how many digits appear in the sequence with the XYX pattern and how many remain without that pattern, in this step I also determine the average of the gap size and its standard deviation.

5.-Finally I create a process that counts how many and what values appear as X and Y in the XYX pattern.

6.-To end things I use the functions that determine the average and standard deviation.

## Visualizations

1.-Line graph and pie graph to view digit frequency distribution in the sequence analyzed as we approach 240 digits.
2.-Line graph to view the evolution of the average digit frequency as we approach 240 digits
3.-Line graph to view the change in gap distance as we approach 240 digits
4.-Line graph to view the evolution of the average gap distance as we approach 240 digits
5.-Line graph to view the evolution of the frequency of the X values and Y values in the XYX patterns

## Sharing my findings


## Acting

If anyone else wants to add something to this little project I would love to see what other things can be found and said about the digits of these natural constants. To me it was an amazing experience exploring this topic and answering the questions I proposed at the begining of the project.

I believe letting your curiosity guide you to new places can teach you about problem solving and trusting your analytical skills to search for the answers to your questions, even if these aren't what you wanted, i think the journey to findin these answers is what makes science fun.
