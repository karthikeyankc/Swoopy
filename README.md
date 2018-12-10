# Swoopy
A Python 2.X script to swoop and decrypt passwords from Chrome's local storage.

# Requirements & Expectations
Swoopy was written for Python 2.X, not for Python 3.X.

Swoopy expects that the Chrome passwords to decrypt are stored in the file "%HOMEPATH%\AppData\Local\Google\Chrome\User Data\Default\Login Data", which is the default location that Chrome stores them. Chromium stores them elsewhere.

Swoopy must be run on the same computer that "Login Data" was created/encrypted on.
