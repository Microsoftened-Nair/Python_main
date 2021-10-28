#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
;SetWorkingDir, C:\AHK\2nd-keyboard\ ;Or you could put the directory here. Whatevs.
Menu, Tray, Icon, shell32.dll, 283 ;changes the taskbar icon to something
;SetKeyDelay, 0 ;IDK exactly what this does.

;;EXACT LOCATION FOR WHERE TO PUT THIS SCRIPT:
; C:\AHK\2nd-keyboard\Intercept

;;Location for where to put a shortcut to the script, such that it will start when Windows starts:
;;  Here for just yourself:
;;  C:\Users\YOUR_USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
;;  Or here for all users:
;;  C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp

#NoEnv
SendMode Input
#InstallKeybdHook
;#InstallMouseHook ;<--You'll want to use this if you have scripts that use the mouse.
#UseHook On
#SingleInstance force ;only one instance of this script may run at a time!
#MaxHotkeysPerInterval 2000

;;The lines below are optional. Delete them if you need to.
#HotkeyModifierTimeout 60 ; https://autohotkey.com/docs/commands/_HotkeyModifierTimeout.htm
#KeyHistory 200 ; https://autohotkey.com/docs/commands/_KeyHistory.htm ; useful for debugging.
#MenuMaskKey vk07 ;https://autohotkey.com/boards/viewtopic.php?f=76&t=57683
#WinActivateForce ;https://autohotkey.com/docs/commands/_WinActivateForce.htm ;prevent taskbar flashing.
;;The lines above are optional. Delete them if you need to.

;________________________________________________________________________________________
;                                                                                        
;		    2ND KEYBOARD USING INTERCEPTION AND INTERCEPT.exe (Logitech K120)            
;________________________________________________________________________________________

; Please watch https://www.youtube.com/watch?v=y3e_ri-vOIo for a comprehensive tutorial. 
;________________________________________________________________________________________

; DANGER: Installing interception may cause your USB devices to stop working sometimes, because it is limited to supporting only 10 of each device class. You have to uninstall it to fix that. Here is a follow up video with new information: https://www.youtube.com/watch?v=Hn18vv--sFY

; For this reason, I now use the Hasu USB to USB keyboard converter. It's sweet.
; https://www.1upkeyboards.com/shop/controllers/usb-to-usb-converter/

;;|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||;;
;;||||||||||||| BEGIN SECOND KEYBOARD INTERCEPTION F23 ASSIGNMENTS ||||||||||||;;
;;|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||;;

;; You should DEFINITELY not be trying to add a 2nd keyboard unless you're already
;; familiar with how AutoHotkey works. I recommend that you at least take this tutorial:
;; https://autohotkey.com/docs/Tutorial.htm

;; You should probably use something better than Notepad for your scripting. (Do NOT use Word.)
;; I use Notepad++. "Real" programmers recoil from it, but it's fine for my purposes.
;; https://notepad-plus-plus.org/
;; You'll probably want the syntax highlighting:  https://stackoverflow.com/questions/45466733/autohotkey-syntax-highlighting-in-notepad


;;;WARNING - THIS IS KINDA UNTESTED SINCE I STOPPED USING IT. LET ME KNOW IF YOU HAVE ANY ISSUES, BY LEAVING A GITHUB... ISSUE.  https://github.com/TaranVH/2nd-keyboard/issues


#if (getKeyState("F23", "P")) ;<--Everything after this line will only happen on the secondary keyboard that uses F23.
F23::return ;this line is mandatory for proper functionality

escape::tooltip, [F23] You might wish to not give a command to escape. Could cause problems. IDK.
;escape::return ;<--to disable a key, just use a "return," like so.

F1::tooltip,
F2::
MouseGetPos, xpos, ypos
Clipboard := xpos ", " ypos
return
;SoundBeep, 900, 400
;tooltip, you pressed F2 AND get a beep sound!
;return
F3::tooltip, you pressed F3 but do not get a beep.
F4::

F5::Send, !m
F6::Send, ^k
F7::Send, ^+k
F8::Send, ^!z

F9::
{
Send, root = LabelFrame(win, text=' ', font=('Segoe UI', 20, 'bold'), bd=10) {Enter}
Send, root.pack() {Enter} {Enter} {Backspace}
}
return
F10::
{
Send, l1 = Label(root, text=' ', font=('Segoe UI', 15)) {Enter}
Send, l1.pack() {Enter} {Enter} {Backspace}
}
return
F11::
{
Send, e1 = Entry(root, font=('Segoe UI', 15)) {Enter}  ;tooltip, [F23]  %A_thishotKey%
Send, e1.pack() {Enter} {Enter} {Backspace}
}
return
F12::
{
Send, b1 = Button(root, text='Submit', font=('Segoe UI', 15)) {Enter} {Backspace}
Send, b1.pack() {Enter} {Enter} {Backspace}
}
return  ;tooltip, you pressed the function key %A_thishotkey% on the [F23] keyboard
;;Note that the assignment on the above line will apply to ALL prior lines ending in "::"
;;...which you should know from the AHK tutorial I linked you to.

;;------------------------NEXT ROW--------------------------;;

`::
{
MouseMove, 1564, 1088
sleep 500
MouseClick, right, 1558, 1064
}
return

1::Send, !a
2::Send, !v
3::Send, !y
4::Run, explorer.exe
5::Run, "C:\Users\nairm\OneDrive\Documents"
6::Run, "D:\Meghraj"
7::Run, "C:\Users\nairm\PycharmProjects"
8::Run, "C:\Users\nairm\OneDrive\Pictures"
9::Run, "C:\Users\nairm\AppData\Local"
0::
-::
=::
backspace::
{
Send, from tkinter import *
Send, {Enter}
Send, {Enter}
Send, win = Tk()
Send, {Enter}
Send, {Enter}
Send, {Enter}
Send, {Enter}
Send, win.mainloop()
Send, {Up} {Up}
}
return

;;------------------------NEXT ROW--------------------------;;

tab::Send ^+{F10}       ;tooltip, [F23]  %A_thisHotKey%
q::Send,!{Enter}    ;coolFunction("Hello World. From Q") ;<--This is just serving as an example of how you would assign functions to these keys
w::Send,!+^j        ;coolFunction("Hello World. From W")
e::Send, !j         ;coolFunction("Hello World. From W")
r::Send,^{/}
t::
Run, Chrome.exe "https://youtube.com/"
return
y::
Run, Chrome.exe "https://web.whatsapp.com/"
return
u::
Run, Chrome.exe "https://github.com/Microsoftened-Nair/Python_main"
return
i::Run, Notepad.exe
return
o::
p::
[::
]::
\::tooltip, [F23]  %A_thisHotKey%
;;capslock::tooltip, [F23] capslock - this should have been remapped to F20. Don't use this line.

;;------------------------NEXT ROW--------------------------;;

a::Send, ^d
s::Send, +{Del}
d::
{
Send, !{Ins}
sleep 50
Send, {Down}
sleep 50
Send, {Down}
sleep 50
Send, {Down}
sleep 50
Send, {Down}
sleep 50
Send, {Down}
sleep 50
Send, {Enter}
}
return
#if (getKeyState("F23", "P"))
f::
if WinActive ("C:\Users\nairm\OneDrive\Documents")
 {
	 {
        Send, +{Click Right}
        sleep 500
        Send, a
        sleep 100
        Send, a
        sleep 100
        Send, {Enter}
}
 }
 else
     Send, +{Click Right}
     sleep 500
	 Send, a
return


return
g::Run, pycharm64.exe

 #if (getKeyState("F23", "P"))
 h::
 if WinActive("ahk_exe chrome.exe")
 {
	 Send,^t
 }
 else
	 Run, chrome.exe
return

j::Run, Chrome.exe "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"
k::Send, ^+{Escape}
l::Send, #k
`;::
;for the above line, (semicolon) note that the ` is necessary as an escape character -- and that the syntax highlighting might get it wrong.
'::
enter:: tooltip, [F23]  %A_thisHotKey% ;Send, {Down} {End} ^v


;;------------------------NEXT ROW--------------------------;;

z::Send, ^z
 #if (getKeyState("F23", "P"))
x::
if WinActive("ahk_exe Photoshop.exe")
 {
	 Send,^+z
 }
 else
	 Send, ^y
return
c::Send, ^r
v::
{
Send, #r
sleep 50
Send, cmd
sleep 50
Send, ^+{Enter}
sleep 500
Send, {Left}
sleep 50
Send, {Enter}
}
return
b::Run, "D:\Meghraj\Python\Git\git-bash.exe"
n::Run, Chrome.exe "https://ryangroup.toppr.school/student/class/?tab=day-view"
return
m::Run, Chrome.exe "https://www.icloud.com/"
return
,::Send, #i
.::
/::tooltip, [F23]  %A_thishotKey%
space::Send, !{Space}
return

;tooltip, [F23] SPACEBAR. This will now clear remaining tooltips.
;sleep 500

;;And THAT^^ is how you do multi-line instructions in AutoHotkey.
;;Notice that the very first line, "space::" cannot have anything else on it.
;;Again, these are fundamentals that you should have learned from the tutorial.

;;===================== MODIFIERS =========================;;

;;Keep these commented out, as they are!
;Lshift::tooltip, do not use
;Lctrl::tooltip, do not use
;Lwin::tooltip, do not use
;Lalt::tooltip, do not use

;Ralt::tooltip, do not use
;Rwin::tooltip, do not use
;appskey::tooltip, This is not a modifier, but I replaced it with INTERNATIONAL4 (SC079) anyway, because it was able to misbehave.
;Rctrl::tooltip, do not use
;Rshift::tooltip, do not use


;;If you leave the modifier keys alone, it allows for lines like the ones below:
;+z::tooltip, you pressed SHIFT Z on the F23 keyboard.
;^z::tooltip, you pressed CTRL Z on the F23 keyboard.
;!z::tooltip, you pressed ALT Z on the F23 keyboard. I don't recommend this... ALT is dangerous because of menu acceleration, even if you try to disable it like I have
;^!z::tooltip, you pressed CTRL SHIFT Z on the F23 keyboard.
;;Etc.
;;However, I use few to no modifiers on my secondary keyboards... I prefer tap dance instead. The decision is up to you.


;;================= MODIFIERS REMAPPED ======================;;

;; When you replace these with your own functions, I recommend that you do NOT delete the tooltips. Just comment them out. That way, you always know what was changed to what. It gets very confusing very quickly otherwise.
;; Here is the full list of scan code substitutions that I made:
;; https://docs.google.com/spreadsheets/d/1GSj0gKDxyWAecB3SIyEZ2ssPETZkkxn67gdIwL1zFUs/edit#gid=824607963


 #if (getKeyState("F23", "P"))
SC070::
 if WinActive("ahk_exe mintty.exe")
 {
	 Send, +{Insert}
 }
 else
     Send, ^v
return                     ;tooltip, [F23] Lshift -to-> SC070-International

 #if (getKeyState("F23", "P"))
SC071::
 if WinActive("ahk_exe mintty.exe")
 {
	 Send, ^{Insert}
 }
 else
     Send, ^c
return
                ;tooltip, [F23] LCtrl -to-> SC071-Language 2
SC072::Send, ^x ;tooltip, [F23] LWin -to-> SC072-Language
SC073::
{
ClipSaved= %clipboard%
sleep 5
Send, ^c
sleep 5
ClipNew = %ClipSaved% %clipboard%
sleep 5
Clipboard := ClipNew
}
return ;tooltip, [F23] LAlt -to-> SC073-International 1
SC077::Send, ^s ;tooltip, [F23] RAlt -to-> SC077-Language 4
SC078::tooltip, [F23] RWin -to-> SC078-Language 3
;SC079::tooltip, [F23] AppsKey -to-> SC079-International 4
SC07B::tooltip, [F23] RCtrl -to-> SC07B-International 5
SC07D:: ;tooltip, [F23] RShift -to-> SC07D-International 3

;;================= LOCKING KEYS ======================;;

F20::tooltip, [F23] CapsLock -to-> SC06B-F20
SC05C::tooltip, [F23] NumLock -to-> SC05C-International 6
;Numlock is an AWFUL key. I prefer to leave it permanently on.
;It's been changed to International 6, so you can use it with no fear that it'll mess up your numpad.
SC061::tooltip, [F23] ScrollLock -to-> SC061 %A_thishotKey%

;;================= NEXT SECTION ======================;;

PrintScreen::tooltip, [F23] %A_thishotKey%
;;ScrollLock::do not use
SC07E::tooltip, [F23] Pause -to-> SC07E-Brazillian comma

;;Don't use the 3 keys below for your 2nd keyboard!
;Pause::msgbox, The Pause/Break key is a huge PITA. That's why I remapped it to SC07E
;Break::msgbox, Or is it THIS key? WHO KNOWS!
;CtrlBreak::msgbox, I have no idea what Ctrlbreak is. But it shows up sometimes.
;;Don't use the 3 keys above for your 2nd keyboard! Just don't!!



;Clipboard2 = %Clipboard%
;Clipboard3 = %Clipboard%

insert::
Clipboardtemp = %Clipboard%
Send, ^{c}
Clipboard2 = %Clipboard%
Clipboard = %Clipboardtemp%
return

delete::
Clipboardtemp = %Clipboard%
Clipboard = %Clipboard2%
Send, ^{v}
Clipboard = %Clipboardtemp%
return

home::
Clipboardtemp = %Clipboard%
Send, ^{c}
Clipboard3 = %Clipboard%
Clipboard = %Clipboardtemp%
return

end::
Clipboardtemp = %Clipboard%
Clipboard = %Clipboard3%
Send, ^{v}
Clipboard = %Clipboardtemp%
return


pgup::
Clipboardtemp = %Clipboard%
Send, ^{c}
Clipboard4 = %Clipboard%
Clipboard = %Clipboardtemp%
return

pgdn::
Clipboardtemp = %Clipboard%
Clipboard = %Clipboard4%
Send, ^{v}
Clipboard = %Clipboardtemp%
return

;;================= NEXT SECTION ======================;;

up::
down::
left::
right::tooltip,[F23] %A_thishotKey%

;;================== THE NUMPAD ======================;;

numpad0::
numpad1::
numpad2::
numpad3::
numpad4::
numpad5::
numpad6::
numpad7::
numpad8::
numpad9::tooltip,[F23] %A_thishotKey%


;;NumLock::tooltip, DO NOT USE THIS IN YOUR 2ND KEYBOARD!
numpadDiv::
numpadMult::
numpadSub::
numpadAdd::
numpadEnter::
numpadDot::tooltip, [F23] %A_thishotKey%


#if ;this line will end the F23 secondary keyboard assignments.

;;;--------------------IMPORTANT: HOW TO USE #IF THINGIES----------------------

;;You can use more than one #if thingy at a time, but it must be done like so:
#if (getKeyState("F23", "P")) and if WinActive("ahk_exe Adobe Premiere Pro.exe")
F1::msgbox, You pressed F1 on your secondary keyboard while inside of Premiere Pro

;; HOWEVER, You still would still need to block F1 using #if (getKeyState("F23", "P"))
;; If you don't, it'll pass through normally, any time Premiere is NOT active.
;; Does that make sense? I sure hope so.

;; Alternatively, you can use the following: (Comment it in, and comment out other instances of F1::)
; #if (getKeyState("F23", "P"))
; F1::
; if WinActive("ahk_exe Adobe Premiere Pro.exe")
; {
	; msgbox, You pressed F1 on your secondary keyboard while inside of Premiere Pro
	; msgbox, And you did it by using if WinActive()
; }
; else
	; msgbox, You pressed F1 on your secondary keyboard while NOT inside of Premiere Pro
;;This is easier to understand, but it's not as clean of a solution.

;; #if (getKeyState("F23", "P")) && (uselayer = 0) ;;you can also use a varibable like so, but I don't.

;; Here is a discussion about all this:
;; https://github.com/TaranVH/2nd-keyboard/issues/65

;;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
;;+|||||||||+ END OF INTERCEPTION SECOND KEYBOARD F23 ASSIGNMENTS +|||||||||||||+
;;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

;;Note that this whole script was written for North American keyboard layouts.
;;IDK what you foreign language peoples are gonna have to do!
;;At the very least, you'll have some duplicate keys.


#if

;;*******************************************************************************
;;~~~~~~~~~~~~~DEFINE YOUR NORMAL KEY ASSIGNMENTS BELOW THIS LINE~~~~~~~~~~~~~~~~
;;*******************************************************************************
#IfWinActive ahk_exe pycharm64.exe
9::Send, (
#IfWinActive

#IfWinActive ahk_exe pycharm64.exe
`;:: Send, {:}
#IfWinActive

#IfWinActive ahk_exe pycharm64.exe
+;:: Send, {;}
#IfWinActive




;;If you assign them BEFORE the second keyboard, they'll overrule it. You don't want that.
#ifwinactive ahk_exe ahk_exe Adobe Premiere Pro.exe
F2::msgbox, You pressed F2 on your normal keyboard while inside of Premiere Pro. `nThis is an autohotkey script by the way - in case you forgot.`nCheck your taskbar to find it.
;; You can of course delete the above line.
#ifwinactive

;;~~~~~~~~~~~~~~~~~DEFINE YOUR FUNCTIONS BELOW THIS LINE~~~~~~~~~~~~~~~~~~~~~~~~~


coolFunction(stuff)
{
msgbox, You called a function with the following parameter:`n`n%stuff%`n`nCongrats!
msgbox, You can put whatever you like in here. `nI've provided links to the functions I use.
; https://github.com/TaranVH/2nd-keyboard/blob/master/Almost_All_Premiere_Functions.ahk
; https://github.com/TaranVH/2nd-keyboard/blob/master/Almost_All_Windows_Functions.ahk
; NOTE that I use #include, rather than writing them out in the same .ahk file.
; https://autohotkey.com/docs/commands/_Include.htm
; This allows me to do fancy stuff, like direct launching scripts from my Stream Deck.
; But you don't need to do that at all. Just write out your functions in the same script.
}

anotherFunction()
{

}