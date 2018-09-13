export VENV=~/koko/env
python3 -m venv $VENV

source ~/koko/env/bin/activate

pip install --upgrade pip setuptools
pip3 install pyramid
echo "export PATH=$HOME/.local/bin:$PATH" >> ~/.bash_profile

pip install cookiecutter

#cookiecutter gh:Pylons/pyramid-cookiecutter-alchemy

cd ~/koko/library/

# pull in dependencies for project and testing
pip install -e .
pip install -e ".[testing]"

