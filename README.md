# sphinx-basic-ng

A modernised skeleton for Sphinx themes.

## To demo this theme

1. Clone this repository

   ```shell
   git clone https://github.com/pradyunsg/sphinx-basic-ng
   ```

2. Install it locally

   ```shell
   pip install -e ./sphinx-basic-ng
   ```

3. Install `nox`

   ```shell
   pip install nox
   ```

4. Use `nox` to build a simple demo site


   ```shell
   nox -s docs-live -- ./tests/barebones
   ```
