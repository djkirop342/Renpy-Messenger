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

    class messenger :
        def __init__(self, con):
            self.con = con
            self.sent = []
            self.typing = ""
            self.speaker = None
            self.speaking = None
            self.msg = None
            self.wait = 0
            self.choose = None

        def test(self) :
            if self.wait > 0:
                self.wait -= 0.1
            else :
                if self.msg is None :
                    self.msg = self.con.pop(0)
                    self.wait = 1.0
                    if isinstance(self.msg, (int)):
                        self.speaker = self.msg
                        self.speaking = self.msg
                        self.msg = None
                    elif isinstance(self.msg, list):
                        self.choose = self.msg
                    elif self.choose:
                        pass
                else:
                    if self.typing == self.msg:
                        if self.speaker is not None:
                            self.sent.append([self.speaker,[self.msg]])
                            self.speaker = None
                            self.msg = None
                            Hide("chatRoom")()
                            Show("chatRoom", c=self)()
                            # Scroll("phone_vp", "vertical increase", 1000)()

                        else:
                            self.sent[-1][1].append(self.msg)
                            self.msg = None
                            Hide("chatRoom")()
                            Show("chatRoom", c = self)()
                            # Scroll("phone_vp", "vertical increase", 1000)()
                        self.typing = ""
                    else:
                        self.typing += str(self.msg[len(self.typing)])

init -2 :
    # 정의한 컬러
    define white = "#ffffff"
    define black = "#000000"
    define color_ebe376 = "#ebe376"
    define color_b8b2b2 = "#b8b2b2"
    define color_ee9494 = "#ee9494"
    define color_88ccf3 = "#88ccf3"

    default frameBg = white
    default chatName = ""
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
        [0, "이름1과 대화 테스트를 진행하겠습니다.", 1, "저는 이름1 입니다.\n대화를 진행하면 이렇게 됩니다."],
        [0, "이름2와 대화 테스트를 진행하겠습니다.", 1, "저는 이름2 입니다.\n대화를 진행하면 이렇게 됩니다."],
        [0, "이름3과 대화 테스트를 진행하겠습니다.", 1, "저는 이름3 입니다.\n대화를 진행하면 이렇게 됩니다."],
        [],
        [],
        [],
        [],
        []
    ]

    default sendChatList = [
        [],
        [],
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
                                            action [Hide("chatList", dissolve), Show("chatRoom", dissolve, messenger(chatRoomList[chatRoomIdx])), SetVariable("chatName", items["name"]), SetVariable("chatRoomIdx", chatRoomIdx)]
                                            at chatListHoverEffect
                                        textbutton items["desc"] :
                                            text_size 20
                                            text_color black
                                            xfill True
                                            ysize 25
                                            action [Hide("chatList", dissolve), Show("chatRoom", dissolve, messenger(chatRoomList[chatRoomIdx])), SetVariable("chatName", items["name"]), SetVariable("chatRoomIdx", chatRoomIdx)]
                                            at chatListHoverEffect

                            $ chatRoomIdx += 1

screen chatRoom(c) :
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
                    action [Hide("chatRoom", dissolve), Show("chatList", dissolve), SetVariable("chatRoomIdx", 0)]

                text chatName :
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

                    if len(c.con) or c.msg :
                        timer .1 repeat True action Function(c.test)

                    viewport :
                        draggable True
                        mousewheel True

                        vbox :
                            xfill True
                            spacing 4
                            
                            for i in c.sent :
                                if i[0] :
                                    for iii, ii in enumerate(i[1]):
                                        if iii :
                                            hbox:
                                                xalign 1.0 spacing 0 
                                                frame:
                                                    style "phone_right"
                                                    text ii color "#000" size 20
                                                # add c.people[i[0]] yalign 0.0
                                        else:
                                            frame:
                                                xalign 1.0
                                                style "phone_right_1"
                                                text ii color "#000" size 20
                                else :
                                    for iii, ii in enumerate(i[1]):
                                        if iii :
                                            hbox:
                                                xalign 0.0 spacing 0 
                                                # add c.people[i[0]] yalign 0.0
                                                frame:
                                                    style "phone_left"
                                                    text ii color "#000" size 20
                                        else:
                                            frame:
                                                xalign 0.0
                                                style "phone_left_1"
                                                text ii color "#000" size 20

                            
                # 전송하는 영역
                frame :
                    background white
                    xfill True
                    ysize 60
                    yalign 1.0

                    if c.speaking == 0 :
                        text c.typing yalign 0.5 xalign 0.0 color black size 15
                    else:
                        if c.wait > 0:
                            pass
                        else:
                            text "입력 중..." size 15 yalign 0.5 xalign 0.0 color black

                    # if not chatStart :
                    #     textbutton "대화하기" :
                    #         xalign 0.5 yalign 0.5
                    #         text_color black
                    #         text_hover_color color_b8b2b2
                    #         action SetVariable("chatStart", True)
                    # else :
                    #     hbox :
                    #         xalign 0.5 yalign 0.5
                    #         spacing 9

                            # text "보내는 중" :
                            #     color black

                            # text "." :
                            #     color black
                            #     at delayed_blink(0.0, 1.0) style "skip_triangle"
                            # text "." :
                            #     color black
                            #     at delayed_blink(0.2, 1.0) style "skip_triangle"
                            # text "." :
                            #     color black
                            #     at delayed_blink(0.4, 1.0) style "skip_triangle


style phone_text:
    size 22
    yalign .5

style phone_right:
    background Frame(im.Flip("phone/frm0.png",True), 10,20,76,10)
    padding(32,12,96,12)
    yminimum 64

style phone_left:
    background Frame("phone/frm0.png", 76,20,10,10)
    padding(96,12,32,12)
    yminimum 64

style phone_right_1:
    background Frame(im.Flip("phone/frm1.png",True), 10,20,76,10)
    padding(32,12,96,12)
    yminimum 64

style phone_left_1:
    background Frame("phone/frm1.png", 76,20,10,10)
    padding(96,12,32,12)
    yminimum 64