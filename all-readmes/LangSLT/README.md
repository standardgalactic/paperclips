# The sign language action description dataset

## License

All code in this repository is licensed under Apache License 2.0.

The dataset is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Privacy and Ethical Considerations for DailyMoth-70h Dataset

The DailyMoth dataset consists of publicly available videos featuring real ASL interpreters providing news in American Sign Language. 
These videos were created and shared by the Daily Moth project with the explicit consent of the participants for educational and accessibility purposes. 
All content is licensed under a Creative Commons Attribution-NonCommercial (CC-BY-NC) license, 
which permits non-commercial research use provided proper attribution is given (Daily Moth, 2018–present; available at https://www.dailymoth.com/). 
We confirm compliance with these terms: the dataset was used solely for training and evaluating our sign language model in a controlled academic setting. 
No personally identifiable information was extracted or stored beyond what is publicly available, and no face recognition or tracking applications were developed.
To mitigate privacy risks, we processed videos locally without redistribution and applied anonymization techniques (e.g., cropping non-essential frames) where feasible. 
This use aligns with ethical guidelines for AI research involving human subjects, ensuring respect for the deaf community and data subjects' rights.

## Installation :wrench:

We recommend setting up a conda environment for the project:
```shell
conda create --name=LangSLT python=3.10
conda activate LangSLT

git clone https://github.com/dlearing/LangSLT.git
cd LangSLT
pip install -r requirements.txt

export PYTHONPATH="./:$PYTHONPATH"
```
## Prompt Templates

1. Prompts  for sign language action descriptions.
```shell
You are a sign language expert, please translate the inputs into a sign language action description text with strict format:
<Gestures: [Action 1 Description]; [Action 2 Description];…> 
<Nation: [National]>
<Language: [Language]>
The inputs are expressed in { National} sign language .Please describe the sign language action corresponding to the inputs  in {Language}.

2.the semantics represented by the action description.


You are {Nation}  sign language expert. please generate a reasonable  {Language}   spoken  text  based on the action description of  {Nation}   sign language.