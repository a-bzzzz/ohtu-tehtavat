*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  Bil  12pAle34
    Output Should Contain  New user registered
Register With Already Taken Username And Valid Password
    Input Credentials  Pal  pAle1111
    Output Should Contain  User with username Pal already exists
Register With Too Short Username And Valid Password
    Input Credentials  me  too00oot
    Output Should Contain  Username is in wrong format!
Register With Valid Username And Too Short Password
    Input Credentials  myy  12
    Output Should Contain  Password is in wrong format!
Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  myy  Pikkuinen
    Output Should Contain  Password is in wrong format!

*** Keywords ***
Input New Command And Create User   
    Input New Command
    Create User  Pal  pAle1111