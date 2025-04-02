import os
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

delta_t_simuls = 0
meteo_data = pd.read_csv(os.path.join('inputs', 'meteo_Ljutovac2002.csv'), index_col='t')


def phloem(df_current_organs, df_marion_organs, tmin, tmax):
    fig, axs = plt.subplots(2, 2)

    # phloem sucrose & AA

    # 1
    axs[0, 0].plot(df_current_organs[(df_current_organs.organ == 'phloem')]['t'], df_current_organs[(df_current_organs.organ == 'phloem')]['Conc_Sucrose'], label='current')
    axs[0, 0].plot(df_marion_organs[(df_marion_organs.organ == 'phloem')]['t'], df_marion_organs[(df_marion_organs.organ == 'phloem')]['Conc_Sucrose'], label='Marion')
    axs[0, 0].legend()
    axs[0, 0].set_xlim(tmin, tmax)
    axs[0, 0].set_ylabel('Concentration sucrose (µmol g-1)')

    # 2
    axs[0, 1].plot(df_current_organs[(df_current_organs.organ == 'phloem')]['t'], df_current_organs[(df_current_organs.organ == 'phloem')]['sucrose'], label='current')
    axs[0, 1].plot(df_marion_organs[(df_marion_organs.organ == 'phloem')]['t'], df_marion_organs[(df_marion_organs.organ == 'phloem')]['sucrose'], label='Marion')
    axs[0, 1].legend()
    axs[0, 1].set_xlim(tmin, tmax)
    axs[0, 1].set_ylim(0, 500)
    axs[0, 1].set_ylabel('Amount of sucrose (µmol C)')

    # 3
    axs[1, 0].plot(df_current_organs[(df_current_organs.organ == 'phloem')]['t'], df_current_organs[(df_current_organs.organ == 'phloem')]['Conc_Amino_Acids'], label='current')
    axs[1, 0].plot(df_marion_organs[(df_marion_organs.organ == 'phloem')]['t'], df_marion_organs[(df_marion_organs.organ == 'phloem')]['Conc_Amino_Acids'], label='Marion')
    axs[1, 0].legend()
    axs[1, 0].set_xlim(tmin, tmax)
    axs[1, 0].set_ylim(0, 200)
    axs[1, 0].set_ylabel('Concentration amino acids (µmol g-1)')

    # 4
    axs[1, 1].plot(df_current_organs[(df_current_organs.organ == 'phloem')]['t'], df_current_organs[(df_current_organs.organ == 'phloem')]['amino_acids'], label='current')
    axs[1, 1].plot(df_marion_organs[(df_marion_organs.organ == 'phloem')]['t'], df_marion_organs[(df_marion_organs.organ == 'phloem')]['amino_acids'], label='Marion')
    axs[1, 1].legend()
    axs[1, 1].set_xlim(tmin, tmax)
    axs[1, 1].set_ylim(0, 25)
    axs[1, 1].set_ylabel('amino acids (µmol N)')

    plt.tight_layout()
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()


def dry_mass(df_current_axes, df_marion_axes, df_current_organs, df_marion_organs, tmin, tmax):
    fig, axs = plt.subplots(2, 2, sharex=True)

    # Dry mass shoot
    axs[0, 0].plot(df_current_axes['t'], df_current_axes['sum_dry_mass_shoot'], label='current')
    axs[0, 0].plot(df_marion_axes['t'], df_marion_axes['sum_dry_mass_shoot'], label='Marion')
    axs[0, 0].legend()
    axs[0, 0].set_xlim(tmin, tmax)
    # axs[0, 0].set_ylim(0, 0.3)
    axs[0, 0].set_ylabel('Dry mass shoot (g)')

    # Dry mass roots
    axs[0, 1].plot(df_current_axes['t'], df_current_axes['sum_dry_mass_roots'], label='current')
    axs[0, 1].plot(df_marion_axes['t'], df_marion_axes['sum_dry_mass_roots'], label='Marion')
    axs[0, 1].legend()
    axs[0, 1].set_xlim(tmin, tmax)
    # axs[0, 1].set_ylim(0, 0.3)
    axs[0, 1].set_ylabel('Dry mass roots (g)')

    # mstruct shoot
    axs[1, 0].plot(df_current_axes['t'], df_current_axes['mstruct_shoot'], label='current')
    axs[1, 0].plot(df_marion_axes['t'], df_marion_axes['mstruct_shoot'], label='Marion')
    axs[1, 0].legend()
    axs[1, 0].set_xlim(tmin, tmax)
    # axs[1, 0].set_ylim(0, 0.3)
    axs[1, 0].set_ylabel('mstruct shoot (g)')

    # mstruct roots
    axs[1, 1].plot(df_current_organs[df_current_organs['organ'] == 'roots']['t'], df_current_organs[df_current_organs['organ'] == 'roots']['mstruct'], label='current')
    axs[1, 1].plot(df_marion_organs[df_marion_organs['organ'] == 'roots']['t'], df_marion_organs[df_marion_organs['organ'] == 'roots']['mstruct'], label='Marion')
    axs[1, 1].legend()
    axs[1, 1].set_xlim(tmin, tmax)
    # axs[1, 1].set_ylim(0, 0.3)
    axs[1, 1].set_ylabel('mstruct roots (g)')

    plt.tight_layout()
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()

    # shoot : root
    fig, axis = plt.subplots()
    axis.plot(df_current_axes['t'], df_current_axes['shoot_roots_ratio'], label='current')
    axis.plot(df_marion_axes['t'], df_marion_axes['shoot_roots_ratio'], label='Marion')
    axis.legend()
    axis.set_xlim(tmin, tmax)
    axis.set_ylim(0, 2)
    axis.set_ylabel('shoot : root ratio')

    plt.tight_layout()
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()


def N_mass(df_current_axes, df_marion_axes, df_current_organs, df_marion_organs, tmin, tmax):
    fig, axs = plt.subplots(2, 2, sharex=True)

    # % N axis
    axs[0, 0].plot(df_current_axes['t'], df_current_axes['N_content'], label='current')
    axs[0, 0].plot(df_marion_axes['t'], df_marion_axes['N_content'], label='Marion')
    axs[0, 0].legend()
    axs[0, 0].set_xlim(tmin, tmax)
    axs[0, 0].set_ylim(0, 10)
    axs[0, 0].set_ylabel('N content axis (% DM)')

    # N shoot
    axs[0, 1].plot(df_current_axes['t'], df_current_axes['N_content_shoot'], label='current')
    axs[0, 1].plot(df_marion_axes['t'], df_marion_axes['N_content_shoot'], label='Marion')
    axs[0, 1].legend()
    axs[0, 1].set_xlim(tmin, tmax)
    axs[0, 1].set_ylabel('N content shoot (% DM)')

    # N axis
    axs[1, 0].plot(df_current_axes['t'], df_current_axes['sum_N_g'], label='current')
    axs[1, 0].plot(df_marion_axes['t'], df_marion_axes['sum_N_g'], label='Marion')
    axs[1, 0].legend()
    axs[1, 0].set_xlim(tmin, tmax)
    axs[1, 0].set_ylabel('N content axis (g)')

    # N uptake
    axs[1, 1].plot(df_current_organs[df_current_organs['organ'] == 'roots']['t'], df_current_organs[df_current_organs['organ'] == 'roots']['Uptake_Nitrates'], label='current')
    axs[1, 1].plot(df_marion_organs[df_marion_organs['organ'] == 'roots']['t'], df_marion_organs[df_marion_organs['organ'] == 'roots']['Uptake_Nitrates'], label='Marion')
    axs[1, 1].legend()
    axs[1, 1].set_xlim(tmin, tmax)
    axs[1, 1].set_ylabel('Nitrate uptake (µmol)')

    plt.tight_layout()
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()


def surface(df_current_elements, df_marion_elements, tmin, tmax):
    fig, axis = plt.subplots(1, 1)

    # green area
    axis.plot(df_current_elements['t'].unique(), df_current_elements.groupby('t')['green_area'].sum(), label='current')
    axis.plot(df_marion_elements['t'].unique(), df_marion_elements.groupby('t')['green_area'].sum(), label='Marion')
    axis.legend()
    axis.set_xlim(tmin, tmax)
    axis.set_ylabel('Total  green area (m²)')

    plt.tight_layout()
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()


def include_images(graphs_path):
    graphs_to_include = ['leaf_L_hz.PNG', 'Leaf_Lmax.PNG', 'RER_comparison.PNG', 'phyllochron.PNG', 'lamina_Wmax.PNG', 'SSLW.PNG']

    for graph in graphs_to_include:
        im = plt.imread(os.path.join(graphs_path, graph))
        fig = plt.figure(figsize=(13, 10))
        fig.figimage(im)
        pdf.savefig()  # saves the current figure into a pdf page
        plt.close()


def leaf_length_mstruct(df_current_hz, df_marion_hz, tmin, tmax):
    # Loop through phytomer
    for phyto_id in df_current_hz['metamer'].unique():
        if phyto_id in (0, 1, 2):
            continue
        fig, axs = plt.subplots(2, 1)
        axs[0].plot(df_current_hz[(df_current_hz.metamer == phyto_id)]['t'], df_current_hz[(df_current_hz.metamer == phyto_id)]['leaf_L'], color='c', marker='.', label='current')
        axs[0].plot(df_marion_hz[(df_marion_hz.metamer == phyto_id)]['t'], df_marion_hz[(df_marion_hz.metamer == phyto_id)]['leaf_L'], color='orange', marker='.', label='Marion')
        axs[0].set_xlim(tmin, tmax)
        axs[0].set_ylabel('Leaf_L' + ' (m)')
        axs[0].set_title('Leaf' + '_' + str(phyto_id))
        axs[0].legend()
        axs[0].set_xticks([])

        axs[1].plot(df_current_hz[(df_current_hz.metamer == phyto_id)]['t'], df_current_hz[(df_current_hz.metamer == phyto_id)]['mstruct'], color='c', marker='.', label='current')
        axs[1].plot(df_marion_hz[(df_marion_hz.metamer == phyto_id)]['t'], df_marion_hz[(df_marion_hz.metamer == phyto_id)]['mstruct'], color='orange', marker='.', label='Marion')
        axs[1].set_xlim(tmin, tmax)
        axs[1].set_ylabel('mstruct' + ' (g)')
        axs[1].legend()

        plt.tight_layout()
        pdf.savefig()  # saves the current figure into a pdf page
        plt.close()


def leaf_emergence(df_current_hz, df_marion_hz):
    dict_current, dict_marion = {'phyto_id': [], 't_emergence': []}, {'phyto_id': [], 't_emergence_marion': []}
    for phyto_id in df_current_hz['metamer'].unique():
        if not df_current_hz[(df_current_hz.metamer == phyto_id)]['leaf_is_emerged'].any():
            continue
        dict_current['phyto_id'].append(phyto_id)
        dict_current['t_emergence'].append(df_current_hz[(df_current_hz.metamer == phyto_id) & (df_current_hz.leaf_is_emerged == True)]['t'].iloc[0])
    for phyto_id in df_marion_hz['metamer'].unique():
        if phyto_id == 3 or not df_marion_hz[(df_marion_hz.metamer == phyto_id)]['leaf_is_emerged'].any():
            continue
        dict_marion['phyto_id'].append(phyto_id)
        dict_marion['t_emergence_marion'].append(df_marion_hz[(df_marion_hz.metamer == phyto_id) & (df_marion_hz.leaf_is_emerged == True)]['t'].iloc[0])

    df_current = pd.DataFrame.from_dict(dict_current)
    df_marion = pd.DataFrame.from_dict(dict_marion)
    df_merged = df_current.merge(df_marion, on='phyto_id', how='left')
    axis = df_merged.plot(kind='bar')
    axis.set_xlabel('N° de feuille')
    axis.set_ylabel('Temps emergence (hour)')

    fig = axis.get_figure()

    plt.tight_layout()
    pdf.savefig(fig)  # saves the current figure into a pdf page
    plt.close()


if __name__ == '__main__':
    # get current directory
    path = os.getcwd()
    POSTPROCESSING = os.path.join(path, 'postprocessing')
    GRAPHS = os.path.join(path, 'graphs')

    # Path Marion
    dirpath_marion = r'C:\Users\jboeuf\Documents\Vegetative_stages - V2 Marion\Vegetative_stages - V2 Marion'
    POSTPROCESSING_MARION = os.path.join(dirpath_marion, 'postprocessing')

    # Axes
    df_current_axes = pd.read_csv(os.path.join(POSTPROCESSING, 'axes_postprocessing.csv'))
    df_current_axes = df_current_axes[df_current_axes['axis'] == 'MS']
    df_marion_axes = pd.read_csv(os.path.join(POSTPROCESSING_MARION, 'axes_postprocessing.csv'))
    df_marion_axes = df_marion_axes[df_marion_axes['axis'] == 'MS']
    df_marion_axes['t'] = df_marion_axes['t'] + delta_t_simuls
    # Organs
    df_current_organs = pd.read_csv(os.path.join(POSTPROCESSING, 'organs_postprocessing.csv'))
    df_current_organs = df_current_organs[df_current_organs['axis'] == 'MS']
    df_marion_organs = pd.read_csv(os.path.join(POSTPROCESSING_MARION, 'organs_postprocessing.csv'))
    df_marion_organs = df_marion_organs[df_marion_organs['axis'] == 'MS']
    df_marion_organs['t'] = df_marion_organs['t'] + delta_t_simuls
    # Elements
    df_current_elements = pd.read_csv(os.path.join(POSTPROCESSING, 'elements_postprocessing.csv'))
    df_current_elements = df_current_elements[df_current_elements['axis'] == 'MS']
    df_marion_elements = pd.read_csv(os.path.join(POSTPROCESSING_MARION, 'elements_postprocessing.csv'))
    df_marion_elements = df_marion_elements[df_marion_elements['axis'] == 'MS']
    df_marion_elements['t'] = df_marion_elements['t'] + delta_t_simuls
    # HZ
    df_current_hz = pd.read_csv(os.path.join(POSTPROCESSING, 'hiddenzones_postprocessing.csv'))
    df_current_hz = df_current_hz[df_current_hz['axis'] == 'MS']
    df_marion_hz = pd.read_csv(os.path.join(POSTPROCESSING_MARION, 'hiddenzones_postprocessing.csv'))
    df_marion_hz = df_marion_hz[df_marion_hz['axis'] == 'MS']
    df_marion_hz['t'] = df_marion_hz['t'] + delta_t_simuls

    tmin = df_current_axes.t.min()
    tmax = df_current_axes.t.max()

    # plot graphs
    with PdfPages('Comparison_Marion.pdf') as pdf:
        # phloem
        phloem(df_current_organs, df_marion_organs, tmin, tmax)

        # dry mass & shoot : root
        dry_mass(df_current_axes, df_marion_axes, df_current_organs, df_marion_organs, tmin, tmax)

        # N mass
        N_mass(df_current_axes, df_marion_axes, df_current_organs, df_marion_organs, tmin, tmax)

        # Surfaces
        surface(df_current_elements, df_marion_elements, tmin, tmax)
        include_images(GRAPHS)

        # Leaf length & mstruct
        leaf_length_mstruct(df_current_hz, df_marion_hz, tmin, tmax)

        # Leaf emergence date
        leaf_emergence(df_current_hz, df_marion_hz)
