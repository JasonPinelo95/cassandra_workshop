#!/bin/bash

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

curl https://pyenv.run | bash

echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
cp ~/.profile tmp
(echo 'export PATH="$PYENV_ROOT/bin:$PATH"';cat tmp) > ~/.profile ;rm tmp
cp ~/.profile tmp
(echo 'export PYENV_ROOT="$HOME/.pyenv"';cat tmp) > ~/.profile ;rm tmp
echo 'eval "$(pyenv init --path)"' >> ~/.profile

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Creating environment
pyenv install -v 3.9.0
pyenv virtualenv 3.9.0 cassandra
pyenv local cassandra
