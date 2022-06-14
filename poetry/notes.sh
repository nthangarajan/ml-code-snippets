Recreating Poetry environment
Do the following in the folder with pyproject.toml:

# Stop the current virtualenv if active or alternative use
# `exit` to exit from a Poetry shell session
deactivate

# Remove all the files of the current environment of the folder we are in
rm -rf `poetry env info -p` 

# Reactivate Poetry shell
poetry shell

# Install everything
poetry install



jupyter kernelspec list


#uninstalling
jupyter kernelspec uninstall atap


python -m ipykernel install --user --name "atap" --display-name "atap"
cat ~/.local/share/jupyter/kernels/atap/kernel.json

