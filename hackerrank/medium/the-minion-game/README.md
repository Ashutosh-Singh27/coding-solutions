# The Minion Game

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Kevin and Stuart want to play the '__The Minion Game__'.<br>


__Game Rules__<br>

Both players are given the same string, $S$.<br>
Both players have to make substrings using the letters of the string $S$.<br>
Stuart has to make words starting with *consonants*.<br>
Kevin has to make words starting with *vowels*. <br>
The game ends when both players have made all possible substrings.
<br>


__Scoring__<br>
A player gets `+1` point for each occurrence of the substring in the string $S$.<br>

**For Example**:<br>
String $S$ = *BANANA*<br>
Kevin's vowel beginning word = *ANA*<br>
Here, *ANA* occurs twice in *BANANA*. Hence, Kevin will get `2` Points.
<br><br>
For better understanding, see the image below: <br>

<img src="https://s3.amazonaws.com/hr-challenge-images/9693/1450330231-04db904008-banana.png" title="banana.png" />

Your task is to determine the winner of the game and their score.

**Function Description**   

Complete the *minion_game* in the editor below.    

*minion_game* has the following parameters:   

- *string string:* the string to analyze   

**Prints**   

- *string:* the winner's name and score, separated by a space on one line, or `Draw` if there is no winner   

**Input Format**

A single line of input containing the string $S$.  
**Note**: The string $S$ will contain only uppercase letters: $[A-Z]$.  



**Constraints**

$0 < len(S) \leq 10^6$<br>
 

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T10:58:16.932Z  

```py
def minion_game(string):

    vowels = "AEIOU"
    n = len(string)
    kevin = 0
    stuart = 0
    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")



```

---

[View on HackerRank](https://www.hackerrank.com/challenges/the-minion-game/problem)