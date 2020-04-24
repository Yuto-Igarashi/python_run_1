# python_run_1
pythonの実行確認のリポジトリ

python -m venv venv

■仮想環境に入る。
source venv/bin/activate

■仮想環境から離脱
deactivate

■仮想環境で、ライブラリインストール
pip install ●●●

■pip_packages.txtに書き込む。
pip freeze > pip_packages.txt

■pip_packages.txtの内容を書き込む。
pip install -r pip_packages.txt
