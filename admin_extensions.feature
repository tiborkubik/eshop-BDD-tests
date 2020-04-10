# Feature contains scenarios describing some of the operations admin can do with extensions
Feature: Admin extensions operations


    Scenario: Google Analytics edit
        Given administrator is at Analytics page
        And Google Analytics is in the list
        When administrator starts editing the Google Analytics extension
        And administrator fills out the code
        And administrator sets status of extension
        And administrator saves changes
        Then administrator is back at Analytics page
        And Google Analytics extension is modifed


    Scenario Outline: Basic Captcha setup
        Given administrator is at Captcha page
        And "<captcha>" is not installed
        When administrator installs "<captcha>"
        And administrator starts editing "<captcha>"
        And administrator sets status to Enabled
        And administrator saves changes
        Then administrator is back at Captcha page
        And "<captcha>" is installed
        And "<captcha>" is enabled

        Examples:
            |       captcha       |
            |    Basic Captcha    |
            |   Google reCAPTCHA  |
