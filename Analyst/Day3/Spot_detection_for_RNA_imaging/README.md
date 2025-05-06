README.


1- install the environment spot_course_env:
     
     conda env create -f spot_course_env.yml


2- activate it:

    conda activate spot_course_env


3- add the kernel of the spot_course_env environment to your jupyter server:

    python -m ipykernel install --user --name=spot_course_env --display-name="spot_course_env"


3- clone big fish at:
        https://github.com/fish-quant/big-fish/tree/e951ea850b18be4be70c5d0a419ba524c3a59ada

    open it and (in the environment spot_course_env) do pip install . 



4- Go to the base environment:

    install the environment ufish environment:
    
         conda env create -f ufish_env.yml    




