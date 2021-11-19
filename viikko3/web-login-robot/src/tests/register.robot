*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  anni
    Set Password  anni2222
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  my
    Set Password  123my456
    Submit Credentials
    Register Should Fail With Message  Username is in wrong format!

Register With Valid Username And Too Short Password
    Set Username  myy
    Set Password  p1kku
    Submit Credentials
    Register Should Fail With Message  Password is in wrong format!

Login After Successful Registration
    Set Username  mym
    Set Password  123mym45
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  myy
    Set Password  p1kku
    Submit Credentials
    Login Should Fail With Message  Password is in wrong format!

*** Keywords ***
Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Welcome Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
