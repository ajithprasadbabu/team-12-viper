*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***         StartingX     StartingY     Direction     EndingX     EndingY    StartingMC  EndingMC
Move N middle of board     4             4             NORTH         3           4          3           4
Move S middle of board     4             4             SOUTH         5           4          5           6
Move E middle of board     4             4             EAST          4           5          6           7
Move W middle of board     4             4             SOUTH         4           3          8           9
Move N 0X0.   of board     0             0             NORTH         0           0          3           4
Move S 0X0.   of board     0             0             SOUTH         1           0          5           6
Move E 0X0.   of board     0             0             EAST          0           1          6           7
Move W 0X0.   of board     0             0             SOUTH         0           0          8           9
Move N 9X9.   of board     9             9             NORTH         8           9          3           4
Move S 9X9.   of board     9             9             SOUTH         9           9          5           6
Move E 9X9.   of board     9             9             EAST          9           9          6           7
Move W 9X9.   of board     9             9             SOUTH         9           8          8           9
Move N 0X9.   of board     0             9             NORTH         0           9          3           4
Move S 0X9.   of board     0             9             SOUTH         1           9          5           6
Move E 0X9.   of board     0             9             EAST          0           9          6           7
Move W 0X9.   of board     0             9             SOUTH         0           8          8           9
Move N 9X0.   of board     0             9             NORTH         8           0          3           4
Move S 9X0.   of board     0             9             SOUTH         9           0          5           6
Move E 9X0.   of board     0             9             EAST          9           1          6           7
Move W 9X0.   of board     0             9             SOUTH         9           0          8           9
*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${direction}    ${endingX}    ${endingY}    ${startingMC}    ${endingMC}
    initialize_character_xposition_with  ${startingX}
    initialize_character_yposition_with  ${startingY}
    move_in_direction                    ${direction}
    character_xposition_should_be        ${endingX}
    character_yposition_should_be        ${endingY}
    starting_move_count                  ${startingMC}
    ending_move_count                    ${endingMC}
