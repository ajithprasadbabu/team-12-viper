*** Settings ***
Documentation
...	These test cases moves the character position one step based on the given direction. 
...	If the character is at the end of the map, the position will will not be moved but only the step count will be incremented.
...	https://github.com/level-up-program/team-12-viper/blob/main/tests/robot/20221016_002256.jpg
...	https://github.com/level-up-program/team-12-viper/blob/main/tests/robot/Model.jpg
...	https://github.com/level-up-program/team-12-viper/blob/main/tests/robot/Comm_Diagram.jpg
Test Template	Move character
Library		MoveLibrary.py

*** Test Cases ***		StartingX	StartingY	Direction	EndingX		EndingY
Move North in middle of board		4	4	NORTH	3	4
Move South in middle of board		4	4	SOUTH	5	4
Move East in middle of board		4	4	EAST	4	5
Move West in middle of board		4	4	WEST	4	3
Move North from 0,0 of board		0	0	NORTH	0	0
Move South from 0,0 of board		0	0	SOUTH	1	0
Move East from 0,0 of board		0	0	EAST	0	1
Move West from 0,0 of board		0	0	WEST	0	0

***Keywords ***
Move character
[Arguments]	${startingX}	${startingY}	${direction}	${endingX}	${endingY}
Initialize character xposition with	${startingX}
Initialize character yposition with	${startingY}
Move in direction			${direction}
Character xposition should be		${endingX}
Character yposition should be		${endingY}
