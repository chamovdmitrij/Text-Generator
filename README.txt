This project implements the simplest text generator based on Markov chains.
There is Corpus.txt, which has 300,000 words.

Preprocessing:
 - the simplest tokenization by spaces;
	 Tokenization could be done using NLTK,
 	 but I used the usual str.split () because  it was in the problem statement.	
 - creating trigrams (the nearest three words from the current one), where
	 head: the first two tokens from the triplet,
	 tail: last token;
	 
Conditions:
 - To start processing corpus, the user must enter a line that will contain the name of the file containing the course. (corpus.txt)	
 - build 10 pseudo-sentences, each on a new line;
 - each sentence consists of at least 5 tokens;
 - the sentence ends with one of the following characters ".?!";
 - The first word of a sentence must begin with a capital letter;
 - The first word of a sentence must not end with ".?!".

Learning and implementing this project from JBAcademy, I didn't feel like doing machine learning.
Can you suggest what can be improved / changed / made more difficult, in which direction to look in order to
experience the full power of machine learning?
Thanks for the help!
