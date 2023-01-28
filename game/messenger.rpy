init -2 :
    # 정의한 컬러
    define white = "#ffffff"
    define black = "#000000"
    define color_ebe376 = "#ebe376"
    define color_b8b2b2 = "#b8b2b2"
    define color_ee9494 = "#ee9494"
    define color_88ccf3 = "#88ccf3"

    default frameBg = white
    default chatNmae = ""
    default chatRoomIdx = 0
    default chatStart = False
    default chatRoomSW = False

    default chatListVar = [
        {"image" : "icon", "name" : "이름1", "desc" : "여기는 대화 내용 입니다.11"},
        {"image" : "icon", "name" : "이름2", "desc" : "여기는 대화 내용 입니다.22"},
        {"image" : "icon", "name" : "이름3", "desc" : "여기는 대화 내용 입니다.33"},
        {"image" : "icon", "name" : "이름4", "desc" : "여기는 대화 내용 입니다.44"},
        {"image" : "icon", "name" : "이름5", "desc" : "여기는 대화 내용 입니다.55"},
        {"image" : "icon", "name" : "이름6", "desc" : "여기는 대화 내용 입니다.66"},
        {"image" : "icon", "name" : "이름7", "desc" : "여기는 대화 내용 입니다.77"},
        {"image" : "icon", "name" : "이름8", "desc" : "여기는 대화 내용 입니다.88"}
    ]

    default chatRoomList = [
        [True, "이름1과 대화 테스트를 진행하겠습니다.", False, "저는 이름1 입니다.\n대화를 진행하면 이렇게 됩니다."],
        ["True", "이름2와 대화 테스트를 진행하겠습니다.", "False", "저는 이름2 입니다.\n대화를 진행하면 이렇게 됩니다."],
        ["True", "이름3과 대화 테스트를 진행하겠습니다.", "False", "저는 이름3 입니다.\n대화를 진행하면 이렇게 됩니다."],
        [],
        [],
        [],
        [],
        []
    ]

    transform chatListHoverEffect :
        on idle :
            ease 0.1 alpha 1.0
        on hover :
            ease 0.1 alpha 0.5

init python :
    import time
    import json

    def currentTime() :
        return time.strftime("%H:%M")

    def currentDate() :
        return time.strftime("%m월 %d일")

    def chatList() :
        chatListVar = [
            {"image" : "icon", "name" : "이름1", "desc" : "여기는 대화 내용 입니다."},
            {"image" : "icon", "name" : "이름2", "desc" : "여기는 대화 내용 입니다.22"},
            {"image" : "icon", "name" : "이름3", "desc" : "여기는 대화 내용 입니다.33"},
            {"image" : "icon", "name" : "이름4", "desc" : "여기는 대화 내용 입니다.44"},
            {"image" : "icon", "name" : "이름5", "desc" : "여기는 대화 내용 입니다.55"},
            {"image" : "icon", "name" : "이름6", "desc" : "여기는 대화 내용 입니다.66"},
            {"image" : "icon", "name" : "이름7", "desc" : "여기는 대화 내용 입니다.77"},
            {"image" : "icon", "name" : "이름8", "desc" : "여기는 대화 내용 입니다.88"},
        ]

        for items in chatListVar :
            jsonStr = json.dumps(items)
            data = json.loads(jsonStr)
            print(data["image"])


screen chatList :
    frame : 
        background None
        xsize 500 
        ysize 800
        xalign 0.5 yalign 0.3
        xpadding 0
        ypadding 0

        vbox :
            # 상단바 시간, 날짜 영역
            frame :
                background color_ee9494
                xfill True
                ysize 40

                text currentTime() :
                    xalign 0.5
                    yalign 0.5
                    size 22

                text currentDate() :
                    xalign 1.0
                    yalign 0.5
                    size 20

            # 대화방 리스트
            frame :
                background white
                xfill True
                yfill True
                xpadding 0
                ypadding 0

                viewport :
                    draggable True
                    mousewheel True

                    vbox :
                        spacing 10


                        for items in chatListVar :
                            frame :
                                background None
                                ysize 100
                                xfill True
                                yfill True                                

                                hbox :
                                    spacing 30

                                    add items["image"] :
                                        xysize(80, 80)
                                        xpos 20
                                    
                                    vbox :
                                        yalign 0.5
                                        spacing 10

                                        textbutton items["name"] :
                                            text_size 20
                                            text_color black
                                            xfill True
                                            ysize 25
                                            action [Hide("chatList", dissolve), Show("chatRoom", dissolve), SetVariable("chatNmae", items["name"]), SetVariable("chatRoomIdx", chatRoomIdx)]
                                            at chatListHoverEffect
                                        textbutton items["desc"] :
                                            text_size 20
                                            text_color black
                                            xfill True
                                            ysize 25
                                            action [Hide("chatList", dissolve), Show("chatRoom", dissolve), SetVariable("chatNmae", items["name"]), SetVariable("chatRoomIdx", chatRoomIdx)]
                                            at chatListHoverEffect

                            $ chatRoomIdx += 1

screen chatRoom() :
    frame :
        background None
        xsize 500 
        ysize 800
        xalign 0.5 yalign 0.3
        xpadding 0
        ypadding 0                                
        
        vbox :
            # 상단바 시간, 날짜 영역
            frame :
                background color_ee9494
                xfill True
                ysize 40

                text currentTime() :
                    xalign 0.5
                    yalign 0.5
                    size 22

                text currentDate() :
                    xalign 1.0
                    yalign 0.5
                    size 20

            # 타이틀 영역
            frame :
                background white
                xfill True
                ysize 80

                textbutton "닫기" :
                    yalign 0.5
                    text_color black
                    text_hover_color color_b8b2b2
                    action [Hide("chatRoom", dissolve), Show("chatList", dissolve)]

                text chatNmae :
                    xalign 0.5 yalign 0.5
                    color black

            frame :
                background None
                xfill True
                yfill True
                xpadding 0
                ypadding 0

                # 대화하는 영역
                frame :
                    background color_ebe376
                    xfill True
                    ysize 620

                    viewport :
                        draggable True
                        mousewheel True

                        vbox :
                            xfill True
                            for i in chatRoomList[chatRoomIdx] :
                                # if i[0] == True:
                                #     text "[i]" :
                                #         size 20
                                #         color "#000" 
                                #         xalign 0.0
                                # else :
                                #     text "[i]" :
                                #         size 20
                                #         color "#000" 
                                #         xalign 1.0

                                if i:
                                    if i == 0:
                                        hbox:
                                            xalign 1.0 spacing 0 
                                            frame:
                                                text ii color "#000"
                                            add c.people[i[0]] yalign 0.0
                                    else:
                                        frame:
                                            xalign 1.0
                                            text ii color "#000"
                                else:
                                    if i == True0:
                                        hbox:
                                            xalign 0.0 spacing 0 
                                            add c.people[i[0]] yalign 0.0
                                            frame:
                                                text ii color "#000"
                                    else:
                                        frame:
                                            xalign 0.0
                                            text ii color "#000"

                            
                # 전송하는 영역
                frame :
                    background white
                    xfill True
                    ysize 60
                    yalign 1.0

                    if not chatStart :
                        textbutton "대화하기" :
                            xalign 0.5 yalign 0.5
                            text_color black
                            text_hover_color color_b8b2b2
                            action SetVariable("chatStart", True)
                    else :
                        hbox :
                            xalign 0.5 yalign 0.5
                            spacing 9

                            text "보내는 중" :
                                color black

                            text "." :
                                color black
                                at delayed_blink(0.0, 1.0) style "skip_triangle"
                            text "." :
                                color black
                                at delayed_blink(0.2, 1.0) style "skip_triangle"
                            text "." :
                                color black
                                at delayed_blink(0.4, 1.0) style "skip_triangle"


style phone_right_1:
    background Frame(im.Flip("frm1.png",True), 10,20,76,10)
    padding(32,12,96,12)
    yminimum 64

style phone_left_1:
    background Frame("frm1.png", 76,20,10,10)
    padding(96,12,32,12)
    yminimum 64