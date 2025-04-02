from alinea.adel.adel_dynamic import AdelDyn
from alinea.adel.echap_leaf import echap_leaves
from fspmwheat import elongwheat_facade
import pandas as pd
import os

def elongwheat() :

    """
    Chargement des inputs elong-wheat et écriture dans le MTG
    """
    
    AXES_INITIAL_STATE_FILENAME = 'axes_initial_state.csv'
    ORGANS_INITIAL_STATE_FILENAME = 'organs_initial_state.csv'
    HIDDENZONES_INITIAL_STATE_FILENAME = 'hiddenzones_initial_state.csv'
    ELEMENTS_INITIAL_STATE_FILENAME = 'elements_initial_state.csv'
    SOILS_INITIAL_STATE_FILENAME = 'soils_initial_state.csv'

    inputs_dataframes = {}
    for inputs_filename in (AXES_INITIAL_STATE_FILENAME,
                            ORGANS_INITIAL_STATE_FILENAME,
                            HIDDENZONES_INITIAL_STATE_FILENAME,
                            ELEMENTS_INITIAL_STATE_FILENAME,
                            SOILS_INITIAL_STATE_FILENAME):
        inputs_dataframe = pd.read_csv(os.path.join("inputs", inputs_filename))
        inputs_dataframes[inputs_filename] = inputs_dataframe.where(inputs_dataframe.notnull(), None)

    # -- ELONGWHEAT (created first because it is the only facade to add new metamers) --
    # Initial states
    elongwheat_hiddenzones_initial_state = inputs_dataframes[HIDDENZONES_INITIAL_STATE_FILENAME][
        elongwheat_facade.converter.HIDDENZONE_TOPOLOGY_COLUMNS + [i for i in elongwheat_facade.simulation.HIDDENZONE_INPUTS if i in
                                                                    inputs_dataframes[HIDDENZONES_INITIAL_STATE_FILENAME].columns]].copy()
    elongwheat_elements_initial_state = inputs_dataframes[ELEMENTS_INITIAL_STATE_FILENAME][
        elongwheat_facade.converter.ELEMENT_TOPOLOGY_COLUMNS + [i for i in elongwheat_facade.simulation.ELEMENT_INPUTS if i in
                                                                inputs_dataframes[ELEMENTS_INITIAL_STATE_FILENAME].columns]].copy()
    elongwheat_axes_initial_state = inputs_dataframes[AXES_INITIAL_STATE_FILENAME][
        elongwheat_facade.converter.AXIS_TOPOLOGY_COLUMNS + [i for i in elongwheat_facade.simulation.AXIS_INPUTS if i in inputs_dataframes[AXES_INITIAL_STATE_FILENAME].columns]].copy()

    phytoT_df = pd.read_csv(os.path.join("inputs", 'phytoT.csv'))

    # Facade initialisation
    shared_axes_inputs_outputs_df = pd.DataFrame()
    shared_hiddenzones_inputs_outputs_df = pd.DataFrame()
    shared_elements_inputs_outputs_df = pd.DataFrame()
    elongwheat_facade_ = elongwheat_facade.ElongWheatFacade(g,
                                                            1 * 3600,
                                                            elongwheat_axes_initial_state,
                                                            elongwheat_hiddenzones_initial_state,
                                                            elongwheat_elements_initial_state,
                                                            shared_axes_inputs_outputs_df,
                                                            shared_hiddenzones_inputs_outputs_df,
                                                            shared_elements_inputs_outputs_df,
                                                            adel_wheat, phytoT_df,
                                                            False,
                                                            update_shared_df=False)
    
#-----  Début des tests -----
adel_wheat = AdelDyn(seed=1, scene_unit='m', leaves=echap_leaves(xy_model='Soissons_byleafclass'))
g = adel_wheat.load(dir="inputs")

#Test avant update
print("Test avant update")
print(g.properties()["geometry"])

#Test du update géométrie seul
print("Test du update géométrie seul")
adel_wheat.update_geometry(g)
print(g.properties()["geometry"])

#Test après chargement d'elong-wheat avant update
print("Test après chargement d'elong-wheat avant update")
elongwheat()
print(g.properties()["geometry"])

#Test du update géométrie après chargement d'elong-wheat
print("Test du update géométrie après chargement d'elong-wheat")
adel_wheat.update_geometry(g)
print(g.properties()["geometry"])




    
