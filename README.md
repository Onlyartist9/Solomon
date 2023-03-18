# Solomon
A data exploration tool.

![Example of how to use Data Explorer](https://github.com/Onlyartist9/Solomon/blob/main/utils/images/Example%20of%20Solomon%20at%20work.png "Data Explorer in action")

## How it works.
Solomon/Data Explorer makes use of the Streamlit library to render views. The underlying processing of Natural Language is managed by the Open AI api. The app currently uses the Code-Davinci-002 model(Codex) but can and should be replaced with the GPT 3.5 and/or 4 api if users have access to them.

All code is in the Solomon.py file and can be modified as need be.

## To run the the app:

```
# clone the repo
$ git clone https://github.com/Onlyartist9/Solomon.git

# change the working directory to Solomon
$ cd Solomon

# install the requirements
$ python3 -m pip install -r requirements.txt

# Run the demo interface
$ streamlit run Solomon.py
```