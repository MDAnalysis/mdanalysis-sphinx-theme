`mdanalysis-sphinx-theme`
=========================

This builds on [msmb_theme](https://github.com/msmbuilder/msmb_theme) to apply slight modifications to
`sphinx_rtd_theme`. It needs the forementioned theme to be installed.

### Modifications

 - Styling tweaks in `msmb.css`
 - Styling for Jupyter notebooks

### Jupyter CSS

Jupyter css is committed to this repository. It is slightly modified from
the upstream stylesheet. You can regenerate `jupyer.min.css`:

 - Ensure the `notebook/` submodule is initialized.
 - Apply `wrap-notebook-css.patch` to it.
 - Run `compile_jupyter_less.py` to turn the patched `less` files into
   `css`.


## Acknowledgements

This theme builds on [msmb_theme](https://github.com/msmbuilder/msmb_theme)
and the [openff-sphinx-theme](https://github.com/openforcefield/openff-sphinx-theme).