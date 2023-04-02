# Natural Constants and the stuff inside them

This short project pretends to explore an idea that came to me when I was still in college (I competed with others to see who knew more digits of Pi). This idea being "It's funny how there seems to be patterns in the digits of Pi, in particular at first the pattern XYX appears very often, where X is any number and Y is another number that acts as the pseudo-axis of symmetry".<br>

I'm aware that there's information out there about the reasons behind these patterns however I wanted to explore them on my own just for the fun of it, alas I never gave myself the time to do so then. But now I'll give it a shot and see what I find, hopefully something interesting but more importantly I'll have fun working on this.<br> 

So the idea here is just to "find out what's going on" with the digits of natural constants like Pi, Phi, e and sqrt(2). Also I'll be using my newly acquired data analyst skills.<br>

Also before we begin, you can answer these questions too using the Jupyter notebook I created for this project: <a href="https://github.com/uli-wizrd/short_NC_analysis/blob/main/NDS_p1_ENG.ipynb" target="_blank"> Answers part 1 <a> and if you want to see the code I used to make the animations you can view it right here: <a href="https://github.com/uli-wizrd/short_NC_analysis/blob/main/NDS_p2_ENG.ipynb" target="_blank"> Answers part 2 <a> .<br> 

## The questions to be answered

- Is there a tendency to these XYX patterns in the first 1000 digits of the constants? No, even common XYX patterns happen a small number of times, and they appear at irregular intervals.<br> 
  
  - Do the gaps between each XYX pattern become larger the more digits we have or viceversa? No in both cases, however there's always a sudden jump in gap size that does seem to increase the more digits we include.<br>

  - Does one digit appear more often than others? No, they all appear almost the same amount of times the more digits we add.<br>
  
- How does the digit distribution behave in the first 240 digits of these constants? Almost uniformly.<br>

- How does the proportion of digits in XYX patterns behave as we approach 240 digits in these constants? At least in that interval there's some digits that appear more often than others.<br>
  
- Is there a XYX pattern that appears more often than others in these 240 digits? If so, Does it remain that way in 1000 digits? There's, but at 1000 digits it changes.<br>
  
- Is there an X value that appears more often than others in these 240 digits? If so, Does it remain that way in 1000 digits? There's, but it doesn't remain at 1000 digits.<br>
  
- Is there a Y value that appears more often than othersin these 240 digits? Does it remain that way in 1000 digits? There's, but it doesn't remain as we increase the number of digits.<br>
  
## Preparing the constants

We have to have a way to get all of these decimal digits, to achieve this I used the information provided in [link] where the library [] is mentioned as a way to get these constants to a precision specified by the user. 

## Processing the digits

I created a process that takes the decimal point away, transforms the float value into a text string type, then it transforms this value into a list of all the digits that composed the string value, after this every value in the list is transformed into an integer using the map function and to complete our digit list we insert in it some digits we had to convert into integers separately.

## Analizing the digits
  
1.- I started this process by creating a function that counts how many times a digit between 0-9 appears in the sequence inside the list created in the previous phase and create a summarized list of the frequency for every digit in the list. Also I use a simple sorting algorithm on my digit frequency list to give it an ascending order.<br>

2.- After determining the frequency of the digits, I create a function to determine the average of the frequency and the standard deviation of the frequency values.<br>

3.- I then created a process that counts how many digits pass before we have a set of values with the XYX pattern, this way we obtain the distribution of gaps in the sequence and the list of the XYX patterns.<br>

4.-Next I create a process to determine how many digits appear in the sequence with the XYX pattern and how many remain without that pattern, in this step I also determine the average of the gap size and its standard deviation.<br>

5.-Finally I create a process that counts how many times a pattern appears, how many and what values appear as X and Y in the XYX pattern.<br>

6.-To end things I use the functions that determine the average and standard deviation to see how these values change for the amount of digits in and out of XYX patters as we increase digits steadily to a number specified by the user.<br>

## Visualizations

1.-Bar graph and pie graph to view digit frequency distribution in the sequence analyzed.<br>
2.-Line graph to view the change in gap distance.<br>
3.-Line graph to view the evolution of the average gap distance and it's standard deviation.<br>
4.-Line graph to view the evolution of the amount of digits in XYX patterns.
5.-line graph to view the evolution of the percetages of digits in the pattern and digits not in the pattern.
6.-Bar graph to view the top 5 most popular patterns in the sequence for the amount of digits specified.
7.-Bar graph to view the the frequency of the X values and Y values in the XYX patterns

## Sharing my findings

Though the following repositorie and social media I've shared the answers to my initial questions, also I take the time to mention other things one can say and ask about the digits within these sequences.<br>

## Acting

If anyone else wants to add something to this little project I would love to see what other things can be found and said about the digits of these natural constants. To me it was an amazing experience exploring this topic and answering the questions I proposed at the begining of the project.

I believe letting your curiosity guide you to new places can teach you about problem solving and trusting your analytical skills to search for the answers to your questions, even if these aren't what you wanted, i think the journey to findin these answers is what makes science fun.

## References

In order to make the following project I used the following resources, so if you like what you see here please be sure to check them out. They're amaaaaazing!

1.- Library <a href="https://pandas.pydata.org/" target="_blank"> Pandas <a> <br>
2.- Library <a href="https://numpy.org/" target="_blank"> Numpy <a> <br>
3.- Library <a href="https://mpmath.org/doc/current/basics.html#number-types" target="_blank"> mp math <a> <br>
4.- Library <a href="https://matplotlib.org/stable/gallery/color/index.html" target="_blank"> Matplotlib <a> <br>
5.- Article <a href="https://jccraig.medium.com/baking-1000-digits-of-pi-from-3-small-lines-of-python-579da9c3bc49" target="_blank"> Baking digits of Pi <a>
