import dash
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

import Physics_Semiconductors
import Physics_SurfacepotForce
import Physics_BandDiagram


################################################################################
################################################################################
# FIGURE

def fig_surface(slider_Vg, slider_zins, slider_bandgap, slider_epsilonsem, slider_WFmet, slider_EAsem, slider_donor, slider_acceptor, slider_emass, slider_hmass, slider_T, slider_alpha):

    # input (slider) parameters
    Vg = slider_Vg*(1-slider_alpha) #eV
    zins = slider_zins*1e-7 #cm
    bandgap = slider_bandgap #eV
    epsilon_sem = slider_epsilonsem #dimensionless
    WFmet = slider_WFmet #eV
    EAsem = slider_EAsem #eV
    Nd = round((10**slider_donor*10**8)/(1000**3)) #/cm^3
    Na = round((10**slider_acceptor*10**8)/(1000**3)) #/cm^3
    mn = slider_emass*Physics_Semiconductors.me #kg
    mp = slider_hmass*Physics_Semiconductors.me #kg
    T = slider_T #K
    sampletype = False #False=semiconducting; True=metallic

    Vg_array = np.arange(200)/10-10 #eV
    zins_array = (np.arange(200)/10+0.05)*1e-7 #cm


    Vs, F = Physics_SurfacepotForce.VsF(1,sampletype,   Vg,zins,bandgap,epsilon_sem,WFmet,EAsem,Nd,Na,mn,mp,T)
    Vs_biasarray, F_biasarray, Vs_zinsarray, F_zinsarray = Physics_SurfacepotForce.VsF_arrays(Vg_array,zins_array,sampletype,   Vg,zins,bandgap,epsilon_sem,WFmet,EAsem,Nd,Na,mn,mp,T)
    LD, zD, zD_biasarray, Cs_biasarray, Qs_biasarray, zD_zinsarray, Cs_zinsarray, Qs_zinsarray = Physics_SurfacepotForce.VsF_supp(Vs,Vg_array,zins_array,Vs_biasarray,Vs_zinsarray,   Vg,zins,bandgap,epsilon_sem,WFmet,EAsem,Nd,Na,mn,mp,T)

    Ec, Ev, Ei, Ef, zsem, psi, z_array, E_array, Q_array, Insulatorx, Insulatory, Vacuumx, Vacuumy, Gatex, Gatey, ni = Physics_BandDiagram.BandDiagram(Vs,sampletype,   Vg,zins,bandgap,epsilon_sem,WFmet,EAsem,Nd,Na,mn,mp,T)

    #########################################################
    #########################################################
    fig = make_subplots(
        rows=8, cols=3, shared_yaxes=False, shared_xaxes=True,
        column_widths=[0.2, 0.2, 0.2], row_heights=[0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7,1.5],
        specs=[
        [{"rowspan":4}, {"rowspan":2}, {"rowspan":2}],
        [None, None, None],
        [None, {"rowspan":2}, {"rowspan":2}],
        [None, None, None],
        [{}, {}, {}],
        [{}, {}, {}],
        [{}, {}, {}],[{}, {}, {}]])
    fig.add_trace(go.Scatter(
        x = zsem*1e7, y = Ev-psi,
        name = "Valence Band", mode='lines', showlegend=False,
        line_color=color_Ev
        ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x = zsem*1e7, y = Ei-psi,
        name = "Intrinsic Energy", mode='lines', showlegend=False,
        line_color=color_Ei
        ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x = zsem*1e7, y = Ec-psi,
        name = "Conduction Band", mode='lines', showlegend=False,
        line_color=color_Ec
        ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x = zsem*1e7, y = 0*zsem+Ef,
        name = "Fermi Energy", mode='lines', showlegend=False,
        line_color=color_Ef
        ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x = Insulatorx, y = Insulatory,
        name = "Insulator", mode='lines', showlegend=False,
        line_color=color_ox
        ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x = Gatex, y = Gatey,
        name = "Gate Fermi Energy", mode='lines', showlegend=False,
        line_color=color_met
        ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x = Vacuumx, y = Vacuumy,
        name = "Vacuum Energy", mode='lines', showlegend=False,
        line_color=color_vac
        ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x = Vacuumx, y = Vacuumy,
        name = "Potential", mode='lines', showlegend=False,
        line_color=color_met
        ), row=5, col=1)
    fig.add_trace(go.Scatter(
        x = z_array, y = E_array,
        name = "Electric Field", mode='lines', showlegend=False,
        line_color=color_met
        ), row=6, col=1)
    fig.add_trace(go.Scatter(
        x = z_array, y = Q_array,
        name = "Charge Density", mode='lines', showlegend=False,
        line_color=color_met
        ), row=7, col=1)

    fig.add_trace(go.Scatter(
        x = Vg_array, y = Vs_biasarray,
        name = "Contact Potential (bias)", mode='lines', showlegend=False,
        line_color=color_other
        ), row=1, col=2, secondary_y=False)
    fig.add_trace(go.Scatter(
        x = [Vg], y = [Vs],
        name = "This Contact Potential (bias)", mode='markers', showlegend=False,
        marker=dict(color=color_indicator,size=10),
        ), row=1, col=2, secondary_y=False)
    fig.add_trace(go.Scatter(
        x = Vg_array, y = F_biasarray,
        name = "Force (bias)", mode='lines', showlegend=False,
        line_color=color_other
        ), row=3, col=2)
    fig.add_trace(go.Scatter(
        x = [Vg], y = [F],
        name = "This Force (bias)", mode='markers', showlegend=False,
        marker=dict(color=color_indicator,size=10),
        ), row=3, col=2)
    fig.add_trace(go.Scatter(
        x = Vg_array, y = zD_biasarray*10**9,
        name = "Depletion Width (bias)", mode='lines', showlegend=False,
        line_color=color_ox
        ), row=5, col=2)
    fig.add_trace(go.Scatter(
        x = [Vg], y = [zD*10**9],
        name = "This Depletion Width (bias)", mode='markers', showlegend=False,
        marker=dict(color=color_indicator,size=10),
        ), row=5, col=2)
    fig.add_trace(go.Scatter(
        x = Vg_array, y = Cs_biasarray,
        name = "C/Cox (bias)", mode='lines', showlegend=False,
        line_color=color_ox
        ), row=6, col=2)
    #fig.add_trace(go.Scatter(
    #    x = [Vg], y = [zD*10**9],
    #    name = "This C/Cox (bias)", mode='markers', showlegend=False,
    #    marker=dict(color=color_indicator,size=10),
    #    ), row=6, col=2)
    fig.add_trace(go.Scatter(
        x = Vg_array, y = Qs_biasarray*10**9,
        name = "Charge (bias)", mode='lines', showlegend=False,
        line_color=color_ox
        ), row=7, col=2)
    #fig.add_trace(go.Scatter(
    #    x = [Vg], y = [zD*10**9],
    #    name = "This Charge (bias)", mode='markers', showlegend=False,
    #    marker=dict(color=color_indicator,size=10),
    #    ), row=7, col=2)

    fig.add_trace(go.Scatter(
        x = zins_array*1e7, y = Vs_zinsarray,
        name = "Contact Potential (zins)", mode='lines', showlegend=False,
        line_color=color_other
        ), row=1, col=3, secondary_y=False)
    fig.add_trace(go.Scatter(
        x = [zins*1e7], y = [Vs],
        name = "This Contact Potential (zins)", mode='markers', showlegend=False,
        marker=dict(color=color_indicator,size=10),
        ), row=1, col=3, secondary_y=False)
    fig.add_trace(go.Scatter(
        x = zins_array*1e7, y = F_zinsarray,
        name = "Force (zins)", mode='lines', showlegend=False,
        line_color=color_other
        ), row=3, col=3)
    fig.add_trace(go.Scatter(
        x = [zins*1e7], y = [F],
        name = "This Force (zins)", mode='markers', showlegend=False,
        marker=dict(color=color_indicator,size=10),
        ), row=3, col=3)
    fig.add_trace(go.Scatter(
        x = zins_array*1e7, y = zD_zinsarray*10**9,
        name = "Depletion Width (zins)", mode='lines', showlegend=False,
        line_color=color_ox
        ), row=5, col=3)
    fig.add_trace(go.Scatter(
        x = [zins*1e7], y = [zD*10**9],
        name = "This Depletion Width (zins)", mode='markers', showlegend=False,
        marker=dict(color=color_indicator,size=10),
        ), row=5, col=3)
    fig.add_trace(go.Scatter(
        x = zins_array*1e7, y = Cs_zinsarray,
        name = "C/Cox (zins)", mode='lines', showlegend=False,
        line_color=color_ox
        ), row=6, col=3)
    #fig.add_trace(go.Scatter(
    #    x = [zins*1e7], y = [zD*10**9],
    #    name = "This C/Cox (zins)", mode='markers', showlegend=False,
    #    marker=dict(color=color_indicator,size=10),
    #    ), row=6, col=3)
    fig.add_trace(go.Scatter(
        x = zins_array*1e7, y = Qs_zinsarray,
        name = "Charge (zins)", mode='lines', showlegend=False,
        line_color=color_ox
        ), row=7, col=3)
    #fig.add_trace(go.Scatter(
    #    x = [zins*1e7], y = [zD*10**9],
    #    name = "This Charge (zins)", mode='markers', showlegend=False,
    #    marker=dict(color=color_indicator,size=10),
    #    ), row=7, col=3)


    fig.add_trace(go.Scatter(
        x = Vs_biasarray, y = np.abs(Qs_biasarray),
        name = "C/Cox (bias)", mode='lines', showlegend=False,
        line_color=color_other
        ), row=8, col=2)

    # Automated axis scaling
    biasmin = -3
    biasmax = +3
    if biasmin<Vg and Vg>biasmax:
        biasrange_indexmin = find_nearest(Vg_array,biasmin)
        biasrange_indexmax = find_nearest(Vg_array,Vg+1)
    elif biasmin>Vg and Vg<biasmax:
        biasrange_indexmin = find_nearest(Vg_array,Vg-1)
        biasrange_indexmax = find_nearest(Vg_array,biasmax)
    else:
        biasrange_indexmin = find_nearest(Vg_array,biasmin)
        biasrange_indexmax = find_nearest(Vg_array,biasmax)

    fig.update_layout(transition_duration=300, height=1000, margin=dict(t=0), showlegend=False)

    fig.update_xaxes(title_standoff=5, title_text="", row=1, col=1)
    fig.update_xaxes(title_standoff=5, title_text="", row=3, col=1)
    fig.update_xaxes(title_standoff=5, title_text="z (nm)", row=7, col=1)
    fig.update_xaxes(title_standoff=5, title_text="", row=1, col=2)
    fig.update_xaxes(title_standoff=5, title_text="", row=3, col=2)
    fig.update_xaxes(title_standoff=5, title_text= "Gate Bias (eV)", range=[Vg_array[biasrange_indexmin], Vg_array[biasrange_indexmax]],row=7,col=2)
    fig.update_xaxes(title_standoff=5, title_text="", row=1, col=3)
    fig.update_xaxes(title_standoff=5, title_text="", row=3, col=3)
    fig.update_xaxes(title_standoff=5, title_text= "Insulator Thickness (nm)", range=[min(zins_array*1e7), max(zins_array*1e7)], row=7, col=3)

    fig.update_yaxes(title_standoff=5, title_text="E (eV)", row=1, col=1)
    fig.update_yaxes(title_standoff=5, title_text="V (V)", row=5, col=1)
    fig.update_yaxes(title_standoff=5, title_text="E (eV/nm)", row=6, col=1)
    fig.update_yaxes(title_standoff=5, title_text="Q (eV/nm^2)", row=7, col=1)
    fig.update_yaxes(title_standoff=5, title_text="Vs (eV)", row=1, col=2)
    fig.update_yaxes(title_standoff=5, title_text="F (N/nm^2)", row=3, col=2, range=[min(F_biasarray[biasrange_indexmin], F_biasarray[biasrange_indexmax]), max(F_biasarray)])
    fig.update_yaxes(title_standoff=5, title_text="zd (nm)", row=5, col=2)
    fig.update_yaxes(title_standoff=5, title_text="C/Cox", row=6, col=2)
    fig.update_yaxes(title_standoff=5, title_text="Qs", row=7, col=2)
    fig.update_yaxes(title_standoff=5, title_text="Vs (eV)", row=1, col=3)
    fig.update_yaxes(title_standoff=5, title_text="F (N/nm^2)", row=3, col=3, range=[min(F_biasarray[biasrange_indexmin], F_biasarray[biasrange_indexmax]), max(F_biasarray)])
    fig.update_yaxes(title_standoff=5, title_text="zd (nm)", row=5, col=3)
    fig.update_yaxes(title_standoff=5, title_text="C/Cox", row=6, col=3)
    fig.update_yaxes(title_standoff=5, title_text="Qs", row=7, col=3)

    #zD = Vg_array[biasrange_indexmax][0]

    return fig, format(ni, ".1E"), format(LD*10**9, ".1f"), format(zD*10**9, ".1f")




################################################################################
################################################################################
# READOUTS

def readouts_surface(slider_Vg, slider_zins, slider_bandgap, slider_epsilonsem, slider_WFmet, slider_EAsem, slider_donor, slider_acceptor, slider_emass, slider_hmass, slider_T, slider_alpha):
    readout_Vg = '{0:.4g}'.format(slider_Vg)
    readout_zins = '{0:.0f}'.format(slider_zins)
    readout_bandgap = '{0:.1f}'.format(slider_bandgap)
    readout_epsilonsem = '{0:.1f}'.format(slider_epsilonsem)
    readout_WFmet = '{0:.2f}'.format(slider_WFmet)
    readout_EAsem = '{0:.2f}'.format(slider_EAsem)
    readout_donor = '{0:.0e}'.format(round((10**slider_donor*10**8)/(1000**3)))
    readout_acceptor = '{0:.0e}'.format(round((10**slider_acceptor*10**8)/(1000**3)))
    readout_emass = '{0:.1f}'.format(slider_emass)
    readout_hmass = '{0:.1f}'.format(slider_hmass)
    readout_T = '{0:.4g}'.format(slider_T)
    readout_alpha = '{0:.4g}'.format(slider_alpha)
    return readout_Vg, readout_zins, readout_bandgap, readout_epsilonsem, readout_WFmet, readout_EAsem, readout_donor, readout_acceptor, readout_emass, readout_hmass, readout_T, readout_alpha


################################################################################
################################################################################
# FUNCTIONALITY

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

################################################################################
################################################################################
# APPEARANCE

color_fc='#2ca02c'
color_fv='#bcbd22'
color_Ef='#1f77b4'
color_Ei='#17becf'
color_Ev='#9467bd'
color_Ec='#e377c2'
color_n='#ff7f0e'
color_p='#8c564b'
color_ox='#a9a9a9'
color_met='#2f4f4f'
color_vac='#888888'
color_indicator='#2ca02c'
color_other='#2f4f4f'
