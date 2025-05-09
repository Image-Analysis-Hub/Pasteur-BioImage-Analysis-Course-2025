README.


1- install the environment spot_course_env:
     
     conda env create -f spot_course_env.yml


2- activate it:

    conda activate spot_course_env


3- add the kernel of the spot_course_env environment to your jupyter server:

    python -m ipykernel install --user --name=spot_course_env --display-name="spot_course_env"


4- install the backend ipympl
    
    pip install ipympl


5- clone big fish at:
        https://github.com/fish-quant/big-fish/tree/e951ea850b18be4be70c5d0a419ba524c3a59ada

    open it and (in the environment spot_course_env) do pip install . 

   Or simply enter into the folder bigfish and do  pip install .  in the environment spot_course_env



6- Go to the base environment:

    install the environment ufish environment:
    
         conda env create -f ufish_env.yml    

7-Return to your base environment:
  launch jupyter notebook
  
  jupyter notebook
  
8- Open the first jupyter notebook "Spot detection RNA imaging" and select the kernel: spot_course_env. 



Data: download your data and paste the .tif files in the /data file:

https://dl.pasteur.fr/fop/NLhWwW7V/D.tif
https://dl.pasteur.fr/fop/eL272JNp/C.tiff
https://dl.pasteur.fr/fop/0r7OPGkV/B.tif
https://dl.pasteur.fr/fop/0gtj5J3K/A.tif
https://dl.pasteur.fr/fop/50rDpYSI/XPO-Im1-Cy3_MMStack_Pos0.ome.tif



