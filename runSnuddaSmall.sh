export IPYTHONDIR="`pwd`/.ipython"
export IPYTHON_PROFILE=Snudda_LOCAL

ipcluster start -n 12 --profile=$IPYTHON_PROFILE --ip=127.0.0.1&
sleep 20

simName=networks/smallRun1

if [ -d "$simName" ]; then
  echo "Directory $simName already exists!!"
  exit 666    
fi

./snudda.py init $simName --size 100000

./snudda.py place $simName 
#./snudda.py detect $simName --hvsize 50 --volumeID Striatum
./snudda.py detect $simName --volumeID Striatum
./snudda.py prune $simName

# Copy over template input
cp -a config/input-tinytest.json $simName/input.json

# Uncomment this to generate input
# ./snudda.py input $simName --input $simName/input.json

ipcluster stop


# Uncomment this to run simulation
# ./snudda.py simulate $simName
