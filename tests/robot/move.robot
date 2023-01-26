*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***         StartingX     StartingY     Direction     EndingX     EndingY
Move in middle of board    0             0             NORTH         0           1
Move on edge of board      0             0             SOUTH         0           0

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${direction}    ${endingX}    ${endingY}
    initialize_character_xpostion_with  ${startingX}
    initialize_character_ypostion_with  ${startingY}
    move_in_direction                    ${direction}
    character_xposition_should_be        ${endingX}
    character_yposition_should_be        ${endingY}
