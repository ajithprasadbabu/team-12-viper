*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***         StartingX     StartingY     Direction     EndingX     EndingY    StartingMC  EndingMC
Move N middle of board     4             4             NORTH         3           4          3           4
Move S middle of board     4             4             SOUTH         5           4          5           6
Move E middle of board     4             4             EAST          4           5          6           7
Move W middle of board     4             4             SOUTH         4           3          8           9

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${direction}    ${endingX}    ${endingY}    ${startingMC}    ${endingMC}
    initialize_character_xposition_with  ${startingX}
    initialize_character_yposition_with  ${startingY}
    starting_move_count                  ${startingMC}
    move_in_direction                    ${direction}
    character_xposition_should_be        ${endingX}
    character_yposition_should_be        ${endingY}
    ending_move_count                    ${endingMC}
