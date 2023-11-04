import os, pathlib
import pytest

os.chdir(pathlib.Path.cwd() / 'test')  # run tests from test/ dir

pytest.main()
