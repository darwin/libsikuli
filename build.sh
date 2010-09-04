#!/bin/sh
#
# This worked for Antonin, Sep 4 (OSX 10.6.5)
#
# Prerequisities
# 1. install homebrew (http://github.com/mxcl/homebrew)
# 2. brew install cmake
# 3. brew install python (you need 64-bit Python 2.7, after the installation check> python --version, which python should print /usr/local/bin/python)
# 4. brew install opencv (this installed opencv/2.1.1-pre in my case)
# 5. (optional) install cxxtest (http://cxxtest.tigris.org/, I skipped this step)
# 6. (optional) install latest SWIG (I have 1.3.31 in OSX which worked fine)

cmake . || exit 1
make || exit 2
cp src/libsikuli.a lib || exit 3
cd interfaces/python || exit 4
./run_swig.sh || exit 5
python setup.py install || exit 6