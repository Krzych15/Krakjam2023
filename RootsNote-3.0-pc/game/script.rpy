# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define Ste = Character(_("Wieśniak"), color="#7e1616")
define Zie = Character (_("Zielarka"), color="#167e16")
define Drw = Character (_("Drwal"), color="#d6b80a")
define TreeG = Character (_("Drzewiec"), color="#dd7b0b")

default StefanTalk = False
default BasementInfo = False
default PrimeHouse = False
default PrimeHouseKey = False
default DywanQuest = False
default DywanQuestKey = False 
default checkdoor = False
#default checkdoor2 = False
default opendoor = False
default GrazynaExist = False

default studnia = False 
#default studnia = True 
default againagain = False

default mazekey = False
#default mazekey = True
default elixir = False

default checktrawa = True 
default zielarkadialog = False
default axething = False
default axequest = False
#default axequest = True
default axequest2 = False
default AXE = False
default torch = True
default torch2 = False
default drzewiecpiwnica = False
default secretcode = False

default drwalpierwszy = True
default drwalquest = False 


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene intro1
    " "
    scene intro2

    " "
    scene intro3
    
    " "

    scene bg_road

    play music "Blizzstar - Elapse Things.mp3"fadeout 1
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.
    
    "Dotarłem do miasta. I co dalej?"
    "Lepiej sprawdzę mapę"


    call screen przycisk_startmap

label mapa:
    call screen maps   
#drwal 
label drwalhouse:
    scene bg_offroad
    
    menu:
        "Siekiera":
            if AXE:
                "Tutaj kiedyś była wbita mocarna siekiera~~"
                "Heh... teraz jest {b}MOJA {/b}"
            else:
                if axequest:
                    "Głupio tak zabrać bez pytania..."
                    jump drwalhouse
                else:  
                    if axequest2:
                        "Wkrótce będziesz moja~~ "
                        jump drwalhouse
                    else:    
                        "Lekko zardzewiałą siekiera wbita w pień"
                        jump drwalhouse
           

        "Przeszukaj trawę":
            "A może coś jest w tej trawie?"
            ". . ."
            ". . ."
            "{b}AHA !{/b}" 
            "Jest to trawa..."
            "Ładnie rośnie"
            "...i miło dotknąć"
            jump drwalhouse
        "Porozmawiaj z mieszkańcem ":
            jump drwaltext            
        "Wróć do mapy":
            jump mapa

label drwaltext:
    show ger_n at right
    if drwalpierwszy:
        "Dzień dobry, jesteś drwalem, prawda? "
        Drw "Zgadza się. Obróbka drewna to moja specjalność."
        $ drwalpierwszy = False 
    menu:
        "Wiesz może, gdzie znajdę Korzeniec?":
            show ger_sz at right
            Drw "Nie szukaj tego przekleństwa, jeśli chcesz stąd w ogóle wrócić." 
            Drw "To coś nie przynosi niczego dobrego. Nie ma żadnej długowieczności."
            Drw "Jest tylko długowieczne cierpienie."
            show ger_n at right
            menu: 
                "Co masz na myśli mówiąc długowieczność?":
                    jump drwalA
                "Jakie cierpienie?":
                    jump drwalB
        "Wiesz coś więcej o tej chorobie?":
            show ger_n at right
            jump drwalC
        "Mogę pożyczyć siekierę? "if axequest:
            jump timberquest

        "Apropo odrdzewiacza " if axequest2:
            jump timberquest2  
        "Siekiera" if AXE:
            Drw " Ah to dobra siekiera, będzie ci dobrze służyć, tylko mam nadzieje żę ją kiedyś oddać"
            jump drwalhouse    

        "Ok dzięki":
            jump drwalhouse    
                
label drwalA: 
    show ger_sz at right
    Drw "Był już taki jeden, który szukał Korzeńca. Opętany mówił, że to klucz i jedyna opcja do długowieczności."
    Drw "I stał się…" 
    Drw "{size=-10}drzewem...{/size}"
    Drw "A kolejni powielili jego los."

    menu:
        "A o jakim cierpieniu wspominałeś?":
            Drw "Tamta noc była długa, a nasz zryw błędem." 
            Drw "Próbowaliśmy zniszczyć to, co dopiero powstało, nie zauważyliśmy, kiedy korzenie nas poharatały."
            Drw "W ułamek chwili zostaliśmy skażeni. Idź stąd, póki jeszcze mam siły."
            menu:
                "Czekaj":
                    Drw "Zapomnij o czym mówiłem. Daj mi chwilę, proszę."
                    jump drwalhouse
                "Zakończ rozmowe":
                    jump drwalhouse

        "Tyle mi wystarczy, dziękuję":
            jump drwalhouse

label drwalB: 
    show ger_sz at right          
    Drw "Tamta noc była długa, a nasz zryw błędem." 
    Drw "Próbowaliśmy zniszczyć to, co dopiero powstało, nie zauważyliśmy, kiedy korzenie nas poharatały."
    Drw "W ułamek chwili zostaliśmy skażeni. Idź stąd, póki jeszcze mam siły."
    menu:
        "Co miałeś na myśli mówiąc długowieczność?":
                Drw "Był już taki jeden, który szukał Korzeńca. Opętany mówił, że to klucz i jedyna opcja do długowieczności."
                Drw "I stał się…" 
                Drw "{size=-10}drzewem...{/size}"
                Drw "A kolejni powielili jego los."
                menu:
                    "Czekaj":
                        Drw "Zapomnij o czym mówiłem. Daj mi chwilę, proszę."
                        jump drwalhouse
                    "Zakończ rozmowe":
                        jump drwalhouse

        "Tyle mi wystarczy, dziękuję":
            jump drwalhouse        

label drwalC:
    show ger_n at right
    Drw "Wiem. Wiem aż za dobrze."
    Drw "To wstręctwo wcale nie jest zwykłą chorobą, to klątwa, przekleństwo za naszą wybuchowość, przekleństwo za chciwość jednego z nas."
    Drw "To nie daje nam być sobą, nie pozwala uciec"
    show ger_sz at right
    menu:
        "Nie pozwala uciec?":
            "Jesteśmy uwięzieni, póki drzewo rozpościera nad nami swoją koronę."
            menu:
                "Czekaj":
                    Drw "Zapomnij o czym mówiłem. Daj mi chwilę, proszę."
                    jump drwalhouse
                "Zakończ rozmowe":
                    jump drwalhouse

        "Można wam jakoś pomóc?":
            "Możesz pomóc tylko sobie. Uciekaj stąd, póki możesz. Rusz się, póki mam jeszcze siły"
            menu:
                "Czekaj":
                    Drw "Zapomnij o czym mówiłem. Daj mi chwilę, proszę."
                    jump drwalhouse
                "Zakończ rozmowe":
                    jump drwalhouse
label timberquest:
    show ger_sz at right
    Drw "Hmm. Dlaczego miałbym ci ją pożyczyć."
    show ger_n at right
    menu:
        "Bardzo jej potrzebuje.":
            Drw "Nie przekonuje mnie to."
            "No dobra. Oferuje swoją pomoc w czymkolwiek zechcesz."
            show ger_wes at right
            Drw "o już jakoś brzmi. Mam dwie siekiery, jedna z nich jest zbyt zardzewiała, by ją w ogóle używać." 
            Drw "Jak przyniesiesz mi odrdzewiacz autorstwa zielarki, to dostaniesz ją w dobrej formie."
            $ drwalquest = True
            $ axequest2 = True
            $ axequest = False
            jump drwalhouse

        "Oferuje swoją pomoc w czymkolwiek zechcesz.":
            show ger_wes at right   
            Drw "To już jakoś brzmi. Mam dwie siekiery, jedna z nich jest zbyt zardzewiała, by ją w ogóle używać." 
            Drw "Jak przyniesiesz mi odrdzewiacz autorstwa zielarki, to dostaniesz ją w dobrej formie."
            $ drwalquest = True
            $ axequest2 = True
            $ axequest = False
            jump drwalhouse

label timberquest2:
    if axething:
        menu:
            "Przyniosłem odrdzewiacz":
                show ger_wes at right
                Drw "Dzięki. Siekierze przyda się trochę polerowania. Proszę, jest twoja, oddaj ją potem."
                "Dzięki ci"
                $ axequest2 = False
                $ AXE = True
                jump drwalhouse

            "Przyniosłem odrdzewiacz. Zielarka chciała powiedzieć ci, że kiedyś miałeś więcej jaj.": 
                show ger_sz at right
                Drw "Ehh. A ona dalej to rozpamiętuje. Proszę, tu jest twoja siekiera, oddaj ją potem."
                "Dzięki ci"   
                $ axequest2 = False
                $ AXE = True
                jump drwalhouse

    else:
        Drw "Jak wspomniałem ..." 
        Drw "Jak przyniesiesz mi odrdzewiacz autorstwa zielarki, to dostaniesz ją w dobrej formie."  
        jump drwalhouse    

# rynek i stefan 
label rynek:
    scene bg_rynek

    play music "Blizzstar - Elapse Things.mp3"fadeout 1
    
    menu:
        "Porozmawiaj z osobą na rynku":
            jump StefanDialog1
        "Dom Sołtysa" if PrimeHouse:
                " "
                if opendoor:
                    " "
                else:    
                    if checkdoor:
                        "Już sprawdzałem, bez klucza nie da rady..."
                        jump rynek        
                    else:
                        "Podchodzisz do drzwi"
                        "Chwytasz za klamkę"
                        if PrimeHouseKey:
                            "Używasz klucza który znalazłeś i udaje ci się wejść do środka"
                            jump PrimeHouseEnter
                            $ opendoor = True
                        else:    
                            "Ale..."
                            "No kto by się spodziewał, są zamkniętę"   
                            $ checkdoor = True
                            #$ checkdoor2 = True
                            jump rynek   
        "Studnia":
            jump Wellwell  

        "Wróć do mapy":
            jump mapa
#rozmowa z stefanem
label StefanDialog1:
    show st_neutral at left

    if StefanTalk:
        menu: 
            "Zapytaj o innych mieszkańców":
                jump Zielarkathing
            "Szukam poszlak Korzeńca. Ponoć widziano go kiedyś w tej wiosce.":  
                jump piwnicainfo  
            "Otworzy pan drzwi do ratusza?"if checkdoor:
                Ste "Gdybym miał klucz to bym ci otworzył. Ale zgubiłem. Więc ci nie otworzę."
                jump rynek
            "Zakończ dialog":
                jump rynek
    else:    
        jump AskStefan

label AskStefan:
    $ StefanTalk = True
    "Czy wszystko z panem w porządku?"
    Ste "..."
    show st_n2 at left
    "Wygląda Pan blado. Może mogę w czymś pomóc? "
    Ste "..."
    jump StefanDialog1

label Zielarkathing:
    "Jesteś tu sam?"
    Ste "Jest jeszcze zielarka i drwal. Idź do nich zawracać gitarę."
    $ GrazynaExist = True

    menu: 
        "Wróć do rozmowy":
            jump StefanDialog1
        
        "Zakończ rozmowę":
            jump rynek    

label piwnicainfo:
        show st_neutral at left
        Ste "Legenda, mówi że spoczywa gdzieś w kopalniach pod wioską."
        $ PrimeHouse = True  
        
        menu: 
            "Wiesz jak można się tam dostać?":
                show st_n2 at left
                Ste "Ktoś kiedyś próbował przez podziemia pod ratuszem. Albo przez studnie. Już nie pamiętam dokładnie, to było dawno..."   
                show st_neutral at left
                jump StefanDialog1
            "Skąd to wiesz?":
                show st_n2 at left
                Ste ". . ."
                jump StefanDialog1   
        
            "Zakończ rozmowę":
                jump rynek 

label wellenter:
    scene bg_kop
    play music "mystery_villgae_WITCH.mp3"fadeout 1
    menu:
        "Próba przejścia":
            if mazekey:
                "teraz mogę wejść"
                jump WellMaze    
            else:
                "Przez tę opary nie dam rady przejść"
                "Przydało by się zwiększyć odporność"
                "Może Zielarka będzie wstanie pomóć" 
                $ elixir = True
                jump wellenter
        "Wyjdź z studni":
            "Muszę znaleźć coś na te pnącza..."  
            jump rynek


label PrimeHouseEnter:
    if DywanQuest:
        scene bg_indoor2
    else:    
        scene bg_indoor

    menu :
        "Kot":
            if DywanQuest:
                "Kot wydaje się być również zaskoczony"
                ". . ."
                "Ale tym że go nie głaszczesz, nie tajnym przejściem"
                jump PrimeHouseEnter
            else:
                "Nie wydaje się mieć czegoś przydatnego, ale możesz go pogłaskać"
                "Głaszczesz kota"
                "Kot wydaje się być zadowolony"
                jump PrimeHouseEnter

        "Szafka":
            if DywanQuest:
                "Jakieś naczynia i talerze..., ale nic po za tym"
                "Chociaż ..."
                "Jest jakaś notatka"
                show  note_soltreg
                " "
                hide note_soltreg

                jump PrimeHouseEnter
            else:
                "Jakieś naczynia i talerze"
                "Chociaż ..."
                "Jest jakaś notatka"
                show  note_soltreg
                " "
                hide note_soltreg

                jump PrimeHouseEnter
        "Skrzynka na górze szafy": 
            if DywanQuest:
                "Jakieś stare kosztowności"
                "Stare kosztowności, ale klucza brak"
                "Noi list"
                show note_soltszaf
                " "
                hide note_soltszaf
                
                jump PrimeHouseEnter
            else:
                "Jakieś stare kosztowności"
                "I list?"
                show note_soltszaf
                " "
                hide note_soltszaf

                jump PrimeHouseEnter

        "Dywan":   
            if DywanQuest:
                " "
                if DywanQuestKey:
                    "Pasuje..."
                    jump secretplace
                    pause .5
                    jump PrimeHouseEnter
                else:
                    "Przydał by się klucz, powinien gdzieś tu być..."
                    jump PrimeHouseEnter  
            else: 
                "Sprawdzasz pod dywanem..."   
                $ DywanQuest = True
                pause .5 
                "..."
                "Oczywiście jeszcze kłódka"
                "Za łatwo by było..."
                "Ale myślę że klucz będzie gdzieś tutaj..."
                jump PrimeHouseEnter 
            
        "Lampka wina":
            if DywanQuest:
                "No tutaj tego nie ma, a nie wydaje się to zdatne do picia"
                jump PrimeHouseEnter
            else:
                "Wino, dobre? " 
                jump PrimeHouseEnter

        "Kubek":
            if DywanQuest:
                "To tutaj jest klucz?!"
                $ DywanQuestKey = True
                jump PrimeHouseEnter
            else:
                "Co może być ciekwego w kubku??" 
                jump PrimeHouseEnter       

        "Mapa":
            "O mapa"
            "Lepiej się przyjrzę"
            show map_1_1
            $ studnia = True
            " "
            "Wygląda na to że jest coś pod studnią"
            hide map_1_1

            jump PrimeHouseEnter
            #jump mapazbliska
        "Wyjdź z domu z powrotem na Rynek":
            jump rynek    

label secretplace:  
    if secretcode:
        scene bg_piwnica2
    else:     
        scene bg_piwnica1 
    play music "mystery_villgae_WITCH.mp3"fadeout 1 
    menu: 
        "Pochodnia" if torch:
            "W sumie może się przydać "
            $ torch = False
            $ torch2 = True
            jump secretplace      

        "Człowiek ?":
            if secretcode:
                    show ms_2 at right
                    TreeG "O.Shniec…Tknij…O.Shniec…Ecno… "

                    TreeG "O.Shniec…Dzew…O.Shniec…Orz…"

                    TreeG "O.Shniec…Zabra…A…Ecno…"

                    TreeG "O.Shniec…Ie.Kzwd…Ie…Pdpalj"
    
                    jump secretplace

            else:    
                if drzewiecpiwnica:
                    "Może teraz się uda"
                else:  
                    show ms_1 at right  
                    "Hej...Wszystko w porządku ?"
                    TreeG ". . ."
                    "Przydało by się jakoś odsłonić twarz..."
                if AXE:
                    show ms_1 at right
                    "Ok, teraz"
                    show ms_2 at right
                    "Jesteś wstanie coś powiedzieć?"
                    "Wszystko wporząku ?"
                    TreeG "O.Shniec…Tknij…O.Shniec…Ecno… "

                    TreeG "O.Shniec…Dzew…O.Shniec…Orz…"

                    TreeG "O.Shniec…Zabra…A…Ecno…"

                    TreeG "O.Shniec…Ie.Kzwd…Ie…Pdpalj"

                    $ secretcode = True     
                    jump secretplace

                else:
                    show ms_2 at right
                    if torch:
                        "Może nie będę próbował pochodnią..." 
                        $ axequest = True 
                        $ drzewiecpiwnica = True
                        jump secretplace
                    else:   
                        "Przydała by się siekiera"  
                        $ axequest = True 
                        $ drzewiecpiwnica = True
                        jump secretplace

        "Rozejrzyj się":   
            ". . ."
            ". . ."
            "Tam jest jakaś kartka ~~"
            show note_p
            " "
            hide note_p
            "hm..."
            jump secretplace

        "Wróć na górę":
            jump PrimeHouseEnter    

label Wellwell:
    if studnia:
        "Studnia"
        if AXE:
            "Rozwalasz deski siekierą i wchodzisz do środka"
            jump wellenter
        else:
            "Niestety zabita dechami.."
            $ axequest = True
            jump rynek    
    else:
        "No jest to Studnia"
        jump rynek    

# dom zielarki 
label domzielarki:
    scene bg_house

    menu:
        "Przeszukaj trawę, kto wie co tam może być" if checktrawa:
            " "
            if checkdoor:
                "O to klucz, ciekawe czy będzie pasował~~"
                $ PrimeHouseKey = True 
                $ checktrawa = False
                $ checkdoor = False
                jump domzielarki
            else:
                "O klucz hm... klucz, może się przydać" 
                $ PrimeHouseKey = True
                $ checktrawa = False
                jump domzielarki
        "Porozmawiaj z kobietą":
            jump zielarkadialog

        "Notatka ":
            " "
            show note_dom
            " "
            hide note_dom
            jump domzielarki
            


        "Wróć do mapy":
            jump mapa

label zielarkadialog:
    show bal_n at right
    if GrazynaExist:
        if zielarkadialog:
            Zie "Potrzebujesz jeszcze czegoś ?"
            show bal_ang at right
            jump grazynadialog
        else:       
            "Dzień dobry, pani jest zapewne zielarką?"
            "A tak się składa że poszukuje poszlak na temat Korzeńca"
            show bal_sz at right
            Zie "Korzeńca? Musisz być bardzo ostrożny, nie pozwól sobie na nawet najmniejsze zacięcie, a najlepiej to {size=+10} wynoś się stąd! {/size}"   
            "Co? Skąd ta gwałtowna reakcja?"
            show bal_n at right
            Zie "Powiedzmy sobie, że mam taki dzień, a zwłaszcza drażnią mnie obłąkane dzieci. Jeszcze jakieś pytania?"
            $ zielarkadialog = True
            jump grazynadialog
    else:
        Zie "Nie mam czasu rozmawiać z obłąkanymi."
        jump domzielarki          

label grazynadialog:
    menu:
            "Co się stało z wieśniakiem?":
                
                show bal_ang at right
                Zie "Nic, po prostu jest dziwny. I chory, tak jak my."
                Zie "Zastępuje sołtysa od czasu jego śmierci i paskudnie mu to wychodzi."
                Zie "Kiedyś to jeszcze chociaż dzień dobry powiedział."
                Zie "Teraz za nic się nie odezwie." 
                show bal_n at right
                Zie "Tylko swojego kota wydaje się lubić, a sierściuchowi dolega z kolei ból brzucha, co przekłada się na to, 
                    że właściciel jest jeszcze bardziej zgorzkniały."
                jump grazynadialog

            "Skąd wzięło się to gigantyczne drzewo?":
                Zie "Długa historia."
                jump grazynadialog

            "Gdzie jest reszta?":
                Zie "Choroba doprowadziła ich do takiego stanu, że nie chcą się już więcej pokazywać. Smutne, Ale prawdziwe."
                jump grazynadialog

            "Zapytaj o odrdzewiacz" if drwalquest:
                jump drwalquestline

            "Potrzebuje od ciebie specjalnego wywaru. " if elixir:  
                jump elixirdialog  

            #dodać opcje "nie pytałeś już o to ?"

            "Zakończ rozmowę":
                jump domzielarki     

label drwalquestline:
    show bal_n at right
    "Drwal przysłał mnie po odrdzewiacz. Masz coś takiego?"
    show bal_sz at right
    show bal_ang at right 
    Zie "Gerwazy? Co za tchórz. Boi się przyjść do sklepu. Co za ciapa…! Ehh, dobra dobra, znajdzie się coś. Może być?"
    show bal_n at right
    "Myślę że tak, dzięki"
    show bal_ang at right
    Zie "Przekaż mu ode mnie, że kiedyś miał większe jaja." 
    $ axething = True  
    
    menu:
        "Huh? Czym drwal zarobił sobie na taką opinie?":    
            show bal_n at right 
            Zie "Ten łajdak? Skradł mi serce." 
            Zie "Na początku twardo się stawiałam, nie lubię bajkopisarzy, ale on każdą bajkę zamieniał w rzeczywistość,przynajmniej próbował." 
            Zie "Chwilę to zajęło, ale w końcu mu się udało." 
            show bal_ang at right
            Zie "Letniego wieczoru poszliśmy we dwojga na polanę, ja tu gotowa wyznać mu miłość, a on mi mówi, że to była pomyłka i że kocha inną." 
            Zie "Jak się nie wściekłam! Aż mu się nie dziwię, że mnie unika. Jednak trzeba przyznać. Drugiego takiego jak on to nigdy nie spotkałam."
            "Oh rozumiem..."
            $ drwalquest = False
            jump domzielarki
        "Um... rozumiem? (Zakończ rozmowę)":
            $ drwalquest = False
            jump domzielarki

label elixirdialog:
    Zie "Potrzebować to ty se możesz. Do czego ci?"
    "Muszę zejść w podziemia."
    Zie "{b}Chyba cię opętało!{/b} Możesz sobie pomarzyć, że ci w tym pomogę!"
    "... Proszę?"
    Zie "Dobra, pomogę ci, ale musisz mi podać przepis na..."
    Zie "{b}Ludione{b}"
    "Ludiona tak?"
    "Dobrze już podaję..."
    jump ludionaquest1

label ludionaquest1:
    show bal_n at right
    Zie "Dobrze, więc ile liści laurowych potrzebuje Ludiona?"
    menu: 
        "4": 
            Zie "Jesteś pewien?"     
            show bal_sz at right
            jump ludionaquest1
        "8":  
            Zie "Ok~~"
            jump ludionaquest2
        "6":
            Zie "No nie jestem pewna..."
            show bal_ang at right
            jump ludionaquest1

label ludionaquest2:
    show bal_n at right
    Zie "Ile litrów krwawniku potrzebuje Ludiona?"
    menu: 
        "9": 
            show bal_sz at right
            Zie "Trochu mało chyba, co nie ? Ja bym wincyj wlała"
            jump ludionaquest2
        "3":
            show bal_ang at right
            Zie "Tylko tyle? To szkoda nawet otwierać"   
            jump ludionaquest2
        "12":
            Zie "Masz rację, chyba tyle wystarczy"
            jump ludionaquest3

label ludionaquest3:
    show bal_n at right
    Zie "Ile liści mięty potrzebuje Ludiona?"
    menu: 
        "6":
            "...No chyba nie..."
            "Chociaż~~"
            jump ludionaquestend
        "4":
            show bal_sz at right
            "Hmm... ja bym więcej dała"
            jump ludionaquest3

        "8":
            show bal_ang at right
            "Jejku, tyle chcesz tego tam upchać? Nie przesadzajmy"
            jump ludionaquest3       

label ludionaquestend:
    show bal_n at right
    "Udało ci się. A więc dotrzymam słowa."
    "Dziękuje ci"
    $ elixir = False
    $ mazekey = True
    jump domzielarki

#labirynt w studni 
label WellMaze:
    scene bg_kop1
    if againagain:
        "Huh, czy to początek?"
        "Czy ja chodzę w kółko?"
    else:
        "ok, to gdzie teraz ?"
    menu: 
        "skręć w lewo":
            "no to w lewo"
            with Dissolve(.5)
            pause .5
            jump goodA1
        "Idź prosto":
            with Dissolve(.5)
            pause .5
            jump goodB1
        "Skręć w prawo":
            with Dissolve(.5)
            pause .5
            jump goodC1

label ahagain:
    $ againagain = True
    jump WellMaze

label goodA1:
    "Idziesz dalej w głąb tunnelu"
    scene bg_kop2
    menu: 
        "skręć w lewo":
            "no to w lewo"
            with Dissolve(.5)
            pause .5            
            jump ahagain
        "Idź prosto":
            "to prosto" 
            with Dissolve(.5)
            pause .5            
            jump goodA2
        "Skręć w prawo":
            "może w prawo" 
            with Dissolve(.5)
            pause .5            
            jump goodB2   

label goodA2:
    "Chyba idę w dobrą stronę..."
    "..."
    "Prawda??"
    scene bg_kop3
    menu: 
        "skręć w lewo":
            "no to w lewo"
            with Dissolve(.5)
            pause .5            
            jump ahagain
        "Idź prosto":
            "to prosto" 
            with Dissolve(.5)
            pause .5            
            jump ahagain
        "Skręć w prawo":
            "może w prawo" 
            with Dissolve(.5)
            pause .5            
            jump ahagain

label goodB1:
    "Hm... Gdzie teraz?"
    scene bg_kop1
    menu: 
        "skręć w lewo":
            "no to w lewo"
            with Dissolve(.5)
            pause .5            
            jump goodA2
        "Idź prosto":
            "to prosto"
            with Dissolve(.5)
            pause .5             
            jump goodB2
        "Skręć w prawo":
            "może w prawo"
            with Dissolve(.5)
            pause .5             
            jump goodC2   

label goodB2:
    "Co teraz?"
    scene bg_kop3
    menu:    
        "skręć w lewo":
            "no to w lewo"
            with Dissolve(.5)
            pause .5            
            jump ahagain
        "Idź prosto":
            "to prosto"
            with Dissolve(.5)
            pause .5             
            jump ahagain
        "Skręć w prawo":
            "może w prawo"
            with Dissolve(.5)
            pause .5 
            jump finaale

label goodC1: 
    "Mam nadzieję, że jestem już blisko..."
    scene bg_kop2
    menu: 
        "skręć w lewo":
            "no to w lewo"
            with Dissolve(.5)
            pause .5            
            jump goodC2
        "Idź prosto":
            "to prosto"
            with Dissolve(.5)
            pause .5             
            jump ahagain
        "Skręć w prawo":
            "może w prawo" 
            with Dissolve(.5)
            pause .5           
            jump ahagain

label goodC2:
    "Połowa drogi !"
    "Mam nadzieję..."
    scene bg_kop1
    menu:
        "skręć w lewo":
            "no to w lewo"
            with Dissolve(.5)
            pause .5            
            jump goodB2
        "Idź prosto":
            "to prosto"
            with Dissolve(.5)
            pause .5            
            jump ahagain
        "Skręć w prawo":
            "może w prawo" 
            with Dissolve(.5)
            pause .5            
            jump ahagain

label finaale:
    scene bg_final  
    pause .5
    " "
    menu:
        "Dotknij kamienia":
            "Dotykam Korzeńca. Moje ciało oplatają korzenie. Są ostre, zaczynam krwawić..."
            "Przyciągają mnie w stronę drzewa. Upuszczam dziennik. Tracę przytomność na ułamek chwili..."
            "a kiedy się budzę, nie mogę się ruszyć..."
            "Przed sobą widzę jedynie postać... nagą, spoglądającą na mnie jakby z litością."
            "Ona wychodzi..."
            "Ja zostaję tutaj..."
            "{i}Na wieczność{/i}"
            "Otwórz dziennik na 10 kartce..."
            jump returnn

        "Nie dotykaj kamienia":
            "Staję przed Korzeńcem."
            "Znam prawdę..."
            "Nie dotykam go."
            "Odchodzę. w ciszy~~"
            "Otwórz dziennik na 11 kartce..."

            jump returnn

        "Użyj pochodni"if torch2:
            "Staję przed Korzeńcem." 
            "Znam prawdę..."
            "Podpalam korzenie to jedyny sposób..."
            "Patrzę, jak ogień trawi drzewo..."
            "Słyszę odgłosy radości"
            "Udało się !"
            "Wszyscy odzyskali wolność" 
            "..."
            "Prawie wszyscy."
            "Drzewo spłonęło, więc 12 kartka dziennika zniknęła razem z nim..."
            "Przekaż dziennik dalej~~"

            jump returnn

label returnn:
    " "
    return


screen przycisk_startmap:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.28
        idle "mapicon_iddle.png"
        hover "mapicon_hover.png"
        action Jump ("mapa")   
