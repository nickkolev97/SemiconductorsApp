def presets_surface(button_presets, toggle_type, slider_Vg, slider_zins, slider_bandgap, slider_epsilonsem, slider_WFmet, slider_EAsem, slider_donor, slider_acceptor, slider_emass, slider_hmass, slider_T):
    if button_presets == 1: #MoSe2
        toggle_type = True
        slider_Vg = -1.4
        slider_zins = 5.2
        slider_bandgap = 1.5
        slider_epsilonsem = 5.9
        slider_WFmet = 4.1
        slider_EAsem = 3.5
        slider_emass = 1
        slider_hmass = 1
        slider_donor = 0
        slider_acceptor = 18.8
        slider_T = 300
        stylen = {'color': '#7f7f7f', 'fontSize': 15, 'text-align': 'right'}
        stylep = {'color': '#57c5f7', 'fontSize': 15, 'text-align': 'right'}
        disabledn = True
        disabledp = False
    elif button_presets == 2: #SiO2
        toggle_type = True
        slider_Vg = -1.4
        slider_zins = 4
        slider_bandgap = 1.1
        slider_epsilonsem = 11.8
        slider_WFmet = 4.1
        slider_EAsem = 4.0
        slider_emass = 1
        slider_hmass = 1
        slider_donor = 0
        slider_acceptor = 18.92
        slider_T = 300
        stylen = {'color': '#7f7f7f', 'fontSize': 15, 'text-align': 'right'}
        stylep = {'color': '#57c5f7', 'fontSize': 15, 'text-align': 'right'}
        disabledn = True
        disabledp = False
    elif button_presets == 3: #Pentacene
        toggle_type = False
        slider_Vg = -1.4
        slider_zins = 4
        slider_bandgap = 2.2
        slider_epsilonsem = 11.8
        slider_WFmet = 4.1
        slider_EAsem = 4.0
        slider_emass = 1
        slider_hmass = 1
        slider_donor = 18.92
        slider_acceptor = 0
        slider_T = 300
        stylen = {'color': '#57c5f7', 'fontSize': 15, 'text-align': 'right'}
        stylep = {'color': '#7f7f7f', 'fontSize': 15, 'text-align': 'right'}
        disabledn = False
        disabledp = True
    else:
        toggle_type = toggle_type
        slider_Vg = slider_Vg
        slider_zins = slider_zins
        slider_bandgap = slider_bandgap
        slider_epsilonsem = slider_epsilonsem
        slider_WFmet = slider_WFmet
        slider_EAsem = slider_EAsem
        slider_emass = slider_emass
        slider_hmass = slider_hmass
        slider_donor = slider_donor
        slider_acceptor = slider_acceptor
        slider_T = slider_T
        if toggle_type == True: #p-type
            stylen = {'color': '#7f7f7f', 'fontSize': 15, 'text-align': 'right'}
            stylep = {'color': '#57c5f7', 'fontSize': 15, 'text-align': 'right'}
            disabledn = True
            disabledp = False
            if slider_acceptor == 0:
                slider_acceptor = slider_donor
            else:
                slider_acceptor = slider_acceptor
            slider_donor = 0
        elif toggle_type == False: #n-type
            stylen = {'color': '#57c5f7', 'fontSize': 15, 'text-align': 'right'}
            stylep = {'color': '#7f7f7f', 'fontSize': 15, 'text-align': 'right'}
            disabledn = False
            disabledp = True
            if slider_donor == 0:
                slider_donor = slider_acceptor
            else:
                slider_donor = slider_donor
            slider_acceptor = 0
    return toggle_type, slider_Vg, slider_zins, slider_bandgap, slider_epsilonsem, slider_WFmet, slider_EAsem, slider_donor, slider_acceptor, slider_emass, slider_hmass, slider_T, button_presets, stylen, stylep, disabledn, disabledp

def togglefunctions(toggle_type, slider_donor, slider_acceptor):
    if toggle_type == True: #p-type
        stylen = {'color': '#7f7f7f', 'fontSize': 15, 'text-align': 'right'}
        stylep = {'color': '#57c5f7', 'fontSize': 15, 'text-align': 'right'}
        disabledn = True
        disabledp = False
        slider_donor = 0
        slider_acceptor = slider_acceptor
    elif toggle_type == False: #n-type
        stylen = {'color': '#57c5f7', 'fontSize': 15, 'text-align': 'right'}
        stylep = {'color': '#7f7f7f', 'fontSize': 15, 'text-align': 'right'}
        disabledn = False
        disabledp = True
        slider_donor = slider_donor
        slider_acceptor = 0
    return stylen, stylep, disabledn, disabledp, slider_donor, slider_acceptor