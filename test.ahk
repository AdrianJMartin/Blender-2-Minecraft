SetTitleMatchMode, RegEx
WinActivate , ^Minecraft* 

SetKeyDelay, 100

Send {Esc}

; x seems to be postive to the left -ve to the right
; y up +ve
; z forward +ve

Send /
Clipboard := "fill ~0 ~2 ~1 ~0 ~2 ~11 dirt"
Send ^v
Send {Return} 


Send /
Clipboard := "fill ~1 ~0 ~1 ~1 ~0 ~11 dirt"
Send ^v
Send {Return} 


Send /
Clipboard := "fill ~2 ~0 ~1 ~2 ~0 ~11 dirt"
Send ^v
Send {Return} 


Send {Esc}