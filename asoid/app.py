import configparser as cfg
from pathlib import Path
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import base64
from io import StringIO

from apps import *
from config.help_messages import UPLOAD_CONFIG_HELP, IMPRESS_TEXT
from utils.load_workspace import load_data


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def img_to_html(img_path, width=500):
    img_html = f"<img src='data:image/png;base64,{img_to_bytes(img_path)}'  width='{width}px', class='img-fluid'>"
    return img_html


def index():
    """
    :param application_options: dictionary (app_key: apps)
    :return:
    """
    HERE = Path(__file__).parent.resolve()

    step1_fname = HERE.joinpath("images/data_process_wht.png")
    step2_fname = HERE.joinpath("images/feature_extraction_wht.png")
    step3_fname = HERE.joinpath("images/baseline_classifier_wht.png")
    step4_fname = HERE.joinpath("images/active_learning_schematic.png")
    step5_fname = HERE.joinpath("images/app_discovery.png")

    st.markdown(f" <h1 style='text-align: left; color: #f6386d; font-size:30px; "
                f"font-family:Avenir; font-weight:normal'>Welcome to A-SOiD</h1> "
                , unsafe_allow_html=True)
    st.write("---")
    st.markdown(f" <h1 style='text-align: left; color: #FFFFFF; font-size:18px; "
                f"font-family:Avenir; font-weight:normal'>"
                f"Introducing A-SOiD, the innovative no code website for building supervised classifiers. "
                f"With our platform, you can input pose and behavioral labels to create a customized classifier "
                f"that accurately identifies and classifies animal behavior. "
                f"Our active learning paradigm ensures balanced training data, "
                f"while our manual refinement process allows you to expand and refine behavioral classes "
                f"in an iterative fashion, 'learning the animal behavior as you go.'"
                f"And with our unsupervised segmentation technology, "
                f"A-SOiD can further dissect subtle differences within the same human-defined behavior, "
                f"providing even deeper insights into animal behavior."
                f"Best of all, A-SOiD's performance outperforms state-of-the-art solutions, "
                f"all without the need for a GPU. With in-depth analysis and interactive visuals, "
                f"as well as downloadable CSVs for easy integration into your existing workflow, "
                f"A-SOiD is the ultimate tool for building your own animal behavior classifiers. "
                f"Try A-SOiD today and unlock a new level of insights into animal behavior."
                , unsafe_allow_html=True)
    # st.write("---")
    st.markdown(f" <h1 style='text-align: left; color: #f6386d; font-size:18px; "
                f"font-family:Avenir; font-weight:normal'>Get Started by Selecting a Step</h1> "
                , unsafe_allow_html=True)


    step1 = st.expander("Step 1 - Upload Config File", expanded = True)
    with step1:
        colL, colR = st.columns(2)
        
        colL.subheader("Start your A-SOiD Journey")

        colL.markdown("To begin the workshop, copy the path to the **WORKSHOP_START** project into the config upload, then press **:red[Upload]**"
        " \n\n >Tip: It should be the default path entered already.\n\n **If you have any issues along the way, there is a backup version, you can upload as well.**"
                        , unsafe_allow_html=True)
        colR.markdown("<p style='text-align: right; color: grey; '>" + img_to_html(step1_fname, width=350) + "</p>",
                        unsafe_allow_html=True)
    step2 = st.expander("Step 2 - Feature Extraction")
    with step2:
        colL, colR = st.columns(2)
        colL.subheader("Extract spatio-temporal features from pose")
        colL.markdown(f"In this step,"
                        f" you will examine the distribution of your annotated behaviors. "
                        f"Once you define your minimum duration, features are then computed "
                        f"across time.", unsafe_allow_html=True)
        colL.markdown("-  **Select the best window to fit the data!** \n\n  > But be carefull, the smaller the window, the longer the training time later...")
        colR.markdown("<p style='text-align: right; color: grey; '>" + img_to_html(step2_fname, width=350) + "</p>",
                        unsafe_allow_html=True)
    step3 = st.expander("Step 3 - Active learning")
    with step3:
        colL, colR = st.columns(2)
        colL.subheader("Training a classifier")
        colL.markdown(f" In this step,"
                        f" you will build a machine learning classifier. "
                        f"A-SOiD automatically balances your training data to prevent  "
                        f"emphasis on large classes.", unsafe_allow_html=True)
        colL.markdown("- **Find the right parameters and train the best classifier**")
        colR.markdown("<p style='text-align: right; color: grey; '>" + img_to_html(step3_fname, width=350) + "</p>",
                        unsafe_allow_html=True)

    step4 = st.expander("Step 4 - Predict new data")

    with step4:
        colL, colR = st.columns(2)
        colL.subheader("Predict on new data")
        colL.markdown(" In this step,"
                        f" you use your trained machine learning classifier to predict on new data. "
                        f" \n For this, enter this path: :green[data/mouse083_task1_annotator1_alt.csv] and start to predict!"
                        , unsafe_allow_html=True)
        colL.markdown("-**This is only a demo, so relax!**")
        colR.markdown("<p style='text-align: right; color: grey; '>" + img_to_html(step3_fname, width=350) + "</p>",
                        unsafe_allow_html=True)


    bottom_cont = st.container()

    with bottom_cont:
        st.markdown("""---""")
        st.write('')
        st.markdown('<span style="color:grey">{}</span>'.format(IMPRESS_TEXT), unsafe_allow_html=True)


def main():
    HERE = Path(__file__).parent.resolve()
    logo_fname_ = HERE.joinpath("images/asoid_logo.png")
    logo_im_ = Image.open(logo_fname_)
    # set webpage icon and layout
    st.set_page_config(
        page_title="A-SOiD Workshop",
        page_icon=logo_im_,
        layout="wide",
        menu_items={
        }
    )
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"]{
            min-width: 250px;
            max-width: 250px;   
        }
        [data-testid="stSidebar"][aria-expanded="false"] {
            margin-left: -250px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    header_container = st.container()
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Step 1'
    if 'config' not in st.session_state:
        st.session_state['config'] = None

    # if in main menu, display applications, see above index for item layout
    with st.sidebar:
        le, ri = header_container.columns([1, 1])

        with le.form("config".upper(), clear_on_submit=True):
            
            if st.session_state["config"] is not None:
                default = st.session_state['config']["Project"].get("PROJECT_NAME")
            else:
                default = "workshop_project/WORKSHOP_START/config.ini"

            uploaded_config = st.text_input("Set path for Config File", default, help = UPLOAD_CONFIG_HELP)
            if st.session_state['config'] is None:
                submitted = st.form_submit_button("Upload")
                if submitted and uploaded_config is not None:
                    # read stringio
                    project_config = cfg.ConfigParser()
                    project_config.optionxform = str
                    project_config.read(uploaded_config)
                    st.session_state['config'] = project_config
                   
                    st.experimental_rerun()
            elif st.session_state['config'] is not None:
                cleared = st.form_submit_button(":red[Delete]")
                if cleared:
                    st.session_state['config'] = None
                    st.session_state['page'] = None
                    st.experimental_rerun()

        _, mid_im, _ = st.columns([0.35, 1, 0.35])

        mid_im.image(logo_im_)
        mid_im.subheader("Workshop v0.3")
        st.write('---')
        try:
            working_dir = st.session_state['config']["Project"].get("PROJECT_PATH")
            prefix = st.session_state['config']["Project"].get("PROJECT_NAME")
            data, config = load_data(working_dir,
                                     prefix)
            menu_options = ['Menu'
            , 'Upload Data'
            , 'Extract Features'
            , 'Active Learning'
            #, 'Refine Behaviors'
            #, 'Create New Dataset'
            , 'Predict'
            #, 'Discover'
            ]
            icon_options = ['window-desktop',
                            'upload',
                            'bar-chart-line',
                            'diagram-2',
                            #'images',
                            #'file-earmark-plus',
                            'robot',
                            #"signpost-split",
                            ]

        except:
            menu_options = ['Menu'
            , 'Upload Data'
            , 'Active Learning'
            #, 'Refine Behaviors'
            #, 'Create New Dataset'
            , 'Predict'
            #, 'Discover'
            ]
            icon_options = ['window-desktop',
                            'upload',

                            'diagram-2',
                            #'images',
                            #'file-earmark-plus',
                            'robot',
                            #"signpost-split",
                            ]

        nav_options = option_menu(None, menu_options,
                                  icons=icon_options,
                                  menu_icon="",
                                  default_index=0,
                                  # orientation="horizontal",
                                  styles={
                                      "container": {"padding": "0!important",
                                                    "background-color": "#131320",
                                                    },
                                      "icon": {"color": "white",
                                               "font-size": "20px"},
                                      "nav-link": {
                                          "font-size": "15px",
                                          "text-align": "left",
                                          "margin": "2px",
                                          "--hover-color": "#000000"},
                                      "nav-link-selected": {
                                          "font-weight": "normal",
                                          "color": "#FFFFFF",
                                          "background-color": '#f6386d'},
                                  }
                                  )

    if nav_options == 'Menu':
        index()
    elif 'Upload Data' in nav_options:
        if "config" in st.session_state.keys():
            A_data_preprocess.main(config=st.session_state['config'])
        else:
            A_data_preprocess.main(config=None)
    elif 'Extract Features' in nav_options:
        if "config" in st.session_state.keys():
            B_extract_features.main(config=st.session_state['config'])
        else:
            B_extract_features.main(config=None)
    elif 'Active Learning' in nav_options:
        if "config" in st.session_state.keys():
            C_auto_active_learning.main(ri=ri, config=st.session_state['config'])
        else:
            C_auto_active_learning.main(ri=ri, config=None)
    elif 'Refine Behaviors' in nav_options:
        if "config" in st.session_state.keys():
            D_manual_active_learning.main(ri=ri, config=st.session_state['config'])
        else:
            D_manual_active_learning.main(ri=ri, config=None)
    elif 'Create New Dataset' in nav_options:
        if "config" in st.session_state.keys():
            E_create_new_training.main(ri=ri, config=st.session_state['config'])
        else:
            E_create_new_training.main(ri=ri, config=None)
    elif 'Predict' in nav_options:
        if "config" in st.session_state.keys():
            F_predict.main(ri=ri, config=st.session_state['config'])
        else:
            F_predict.main(ri=ri, config=None)
    elif 'Discover' in nav_options:
        if "config" in st.session_state.keys():
            G_unsupervised_discovery.main(ri=ri, config=st.session_state['config'])
        else:
            G_unsupervised_discovery.main(ri=None, config=None)


if __name__ == "__main__":
    main()
