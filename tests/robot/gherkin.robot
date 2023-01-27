*** Settings ***
Documentation     Example test case using the gherkin syntax.
Library           GameControllerLibrary.py

*** Test Cases ***
Game controller initialized with character name
    Given controller has been initialized
    When character is created with name "ArbitraryName"
    Then actual character name is "ArbitraryName"

Game controller initialized without character name
    Given controller has been initialized
    When character is created with name ""
    Then actual character name is "Character"

Game controller initialized map
    Given controller has been initialized
    Then Map has been initialized

Game controller start the game
    Given controller has been initialized
    Given character is created with name ""
    When Game start
    Then character position should be at map starting position

*** Keywords ***
Controller has been initialized
    Initialize controller

Character is created with name "${provided}"
    Create character with name   ${provided}

Actual character name is "${actual}"
    Character name should be   ${actual}

Map has been initialized
    Initialize map

Game start
    Start game

Character position should be at map starting position
    Character position at starting position