*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***         StartingX     StartingY     Direction     EndingX     EndingY    StartingMC  EndingMC
Move in middle of board    0             0             NORTH         0           1          3           4
Move on edge of board      0             0             SOUTH         0           0          5           6

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
