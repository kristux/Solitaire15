# Solitaire15
Short excercise to validate whether my tactic of solving the solitaire I know only as 15 is sane

The Solitaire
-------------------
It is a pretty simple one. You arrange the cards in a 4 by 4 matrix and leave the rest to the side, face down. You then try to group the cards based on some rules.

1. If you have all the face cards of the same suit you can remove them
2. If you have all the tens you can remove them
3. Cards of the same suit that add up to 15 can be removed i.e. 9 of hearts and 6 of hearts can be removed or 2 of spades, 5 of spades and 8 of spades.

When cards have been removed from the board you should add more from the pile you left to the side.

The Tactic
-------------------
There isn't really a lot choices you can make. If you have all the face cards of the same suit then it really makes no sense to not just remove them from the board. The same goes for the tens. For the cards that should add up to 15 is the place where we have some choice.

My hypothesis is that it is always better to clear as many cards of the table as you possibly can. That is if we have of the same suit 8, 7, 1, 6 then it is better to go for the combination (8, 6, 1) rather than the equally valid combination (8, 7). However that does leave us with the 7 that now needs to be combined with at least two other cards to add up to 15 and it will also mean that we can no longer join the 9 with the 6 to get 15.

The Code
-------------------
This isn't a particularly complex problem but it is quite easy to make a mess of it, especially if you don't write tests. This code was written with TDD. I wrote it "Outside In" that is I started with creating a class called a game with a single method simulate. I really didn't want to implement the whole solution at one so I passed in a deck and a player.

It is kind of weird to write class that just interacts with other classes but it does allow you to see very clearly what is the responsibility of the game. In my case it is simply the macro loop of the game that is: populate board -> pick cards -> fill in new cards until 
* You can't pick any cards (boo you lost)
* There are no more cards to pull (yay you won)

Once the Game had been implmented all I had to do was implement the player and deck which now had pretty clear requirements.
