#!/bin/bash 

file_data=$1
target_dir=$2
base_dir=$3

my_bash_function() { 
    # Activate ufish environment
    # Run in it function ufish_detection
    # take target_dir and build script_path2='/home/user/Documents/FISH/Data_analysis/pipeline_smfish/src/detection_fish/ufish_detection.py'
    # found command "$(conda shell.bash hook)" in:  https://saturncloud.io/blog/activating-conda-environments-from-scripts-a-guide-for-data-scientists/


    # Extract the base directory of the input string
    script_path2="${base_dir}/ufish_detection.py"

    eval "$(conda shell.bash hook)"
    conda activate ufish_env
    export MPLBACKEND=agg

    result=$(python "$script_path2" "$file_data" "$target_dir")
    echo "Python result: $result"    
    conda deactivate
    } 

# Call the function 
my_bash_function 

