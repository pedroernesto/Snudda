from snudda_init import SnuddaInit
from collections import OrderedDict
import json
import os

if __name__ == "__main__":

  connectNeurons = False

  simName = "networks/customSmall"
  #simName = "LTStest"
  
  cnc = SnuddaInit(structDef={},configName=None,nChannels=1)
  #cnc.defineStriatum(nMSD1=4,nMSD2=4,nFS=4,nLTS=1,nChIN=1)
  # cnc.defineStriatum(nMSD1=0,nMSD2=0,nFS=100,nLTS=0,nChIN=0)
  cnc.defineStriatum(nMSD1=4,nMSD2=4,nFS=2,nLTS=1,nChIN=1)
  #cnc.defineStriatum(nMSD1=0,nMSD2=0,nFS=0,nLTS=10,nChIN=0)
  configName= simName + "/network-config.json"

  dirName = os.path.dirname(configName)
  
  if not os.path.exists(dirName):
    os.makedirs(dirName)

  cnc.writeJSON(configName)

  if(not connectNeurons):
    print("Removing all target information, and rewriting config file")
    # Reopen the config file, and remove all connectivity settings, to
    # get an unconnected network

    with open(configName,"r") as f:
      conData = json.load(f,object_pairs_hook=OrderedDict)

    for k in conData:
      if(k.lower() in ["volume", "channels"]):
        continue

      # Remove targets
      if(False):
        x = conData[k]
        del x["targets"]
      
    with open(configName,"w") as f:
      print("Writing to file: " + str(configName))
      json.dump(conData,f,indent=2)
      

  print("Now run:\n./snudda.py place " + simName)
  print("./snudda.py detect " + simName)
  print("./snudda.py prune " + simName)
  print("./snudda.py input " + simName + " --input YOURINPUTCONFIG")
  print("./snudda.py simulate " + simName + " --voltOut YOUROUTPUTFILE.csv --time 10.0")
