*** Settings ***
LEVELUP GAMES: VIPER WORLD
Documentation	 These test cases moves the character position one step based on the given direction. If the character is at the end of the map, the position will will not be moved but only the step count will be incremented.
Test Template	Move character
Library		MoveLibrary.py

*** Test Cases ***		StartingX	StartingY	Direction	EndingX		EndingY
Move North in middle of board		4		4	NORTH		3		4
Move South in middle of board		4		4	SOUTH		5		4

***Keywords ***
Move character
[Arguments]	${startingX}	${startingY}	${direction}	${endingX}	${endingY}
Initialize character xposition with	${startingX}
Initialize character yposition with	${startingY}
Move in direction			${direction}
Character xposition should be		${endingX}
Character yposition should be		${endingY}
